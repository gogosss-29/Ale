"""Motor APImart (apimart.ai): GPT Image 2, Nano Banana Pro, Veo 3.1, Omni Flash, Kling.

NOTA DE INTEGRACIÓN: los paths exactos de la API de APImart deben confirmarse contra su
documentación oficial. Están centralizados aquí como atributos de clase para poder
ajustarlos en un solo sitio sin tocar la lógica. Lee credenciales de variables de entorno:
    APIMART_API_KEY, APIMART_BASE_URL (por defecto https://api.apimart.ai)
"""
from __future__ import annotations

import os
from typing import Optional

from ..models import Asset, ShotPrompt
from .base import ImageEngine, VideoEngine
from .costs import coste_imagen, coste_video
from .rest_job import RestJobClient

DEFAULT_BASE = "https://api.apimart.ai"


def _client() -> RestJobClient:
    key = os.environ.get("APIMART_API_KEY")
    if not key:
        raise RuntimeError("Falta APIMART_API_KEY en el entorno")
    base = os.environ.get("APIMART_BASE_URL", DEFAULT_BASE)
    return RestJobClient(base, key)


class ApimartImage(ImageEngine):
    name = "apimart"
    # paths a confirmar con la doc de APImart
    SUBMIT_PATH = "/v1/images/generations"
    STATUS_PATH = "/v1/tasks/{task_id}"

    def __init__(self, modelo: str = "gpt-image-2"):
        self.modelo = modelo

    def generar_imagen(self, prompt, out_path, referencias=None, aspect_ratio="9:16", resolucion="2K") -> Asset:
        c = _client()
        payload = {
            "model": self.modelo,
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "resolution": resolucion,
        }
        if referencias:
            payload["reference_images"] = referencias  # subir/encodear según doc
        resp = c.post(self.SUBMIT_PATH, payload)
        task_id = resp.get("task_id") or resp.get("id")
        url = c.poll(
            check=lambda: c.get(self.STATUS_PATH.format(task_id=task_id)),
            is_done=lambda d: d.get("status") in ("succeeded", "completed"),
            is_failed=lambda d: d.get("status") in ("failed", "error"),
            get_result_url=lambda d: (d.get("output") or {}).get("url") or d.get("result_url"),
        )
        c.download(url, out_path)
        modelo_key = "image_gpt_image_2" if "gpt" in self.modelo else "image_nano_banana_pro"
        return Asset(tipo="image", path=out_path, engine=self.name,
                     coste_estimado=coste_imagen("apimart", modelo_key),
                     meta={"modelo": self.modelo})


class ApimartVideo(VideoEngine):
    name = "apimart"
    SUBMIT_PATH = "/v1/videos/generations"
    STATUS_PATH = "/v1/tasks/{task_id}"

    def __init__(self, modelo: str = "veo-3.1"):
        self.modelo = modelo  # "veo-3.1" | "omni-flash" | "kling-3"

    def generar_video(self, shot: ShotPrompt, out_path: str) -> Asset:
        c = _client()
        payload = {
            "model": self.modelo,
            "prompt": shot.prompt,
            "negative_prompt": shot.negative_prompt,
            "aspect_ratio": shot.aspect_ratio,
            "duration": shot.duracion_s,
        }
        if shot.primer_frame:
            payload["first_frame"] = shot.primer_frame
        if shot.ultimo_frame:
            payload["last_frame"] = shot.ultimo_frame
        resp = c.post(self.SUBMIT_PATH, payload)
        task_id = resp.get("task_id") or resp.get("id")
        url = c.poll(
            check=lambda: c.get(self.STATUS_PATH.format(task_id=task_id)),
            is_done=lambda d: d.get("status") in ("succeeded", "completed"),
            is_failed=lambda d: d.get("status") in ("failed", "error"),
            get_result_url=lambda d: (d.get("output") or {}).get("url") or d.get("result_url"),
        )
        c.download(url, out_path)
        modelo_key = {"veo-3.1": "video_veo31_8s", "omni-flash": "video_omniflash_8s",
                      "kling-3": "video_kling_5s"}.get(self.modelo, "video_veo31_8s")
        return Asset(tipo="video", path=out_path, engine=self.name,
                     coste_estimado=coste_video("apimart", modelo_key),
                     meta={"modelo": self.modelo})
