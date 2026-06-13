"""Motor APImart (apimart.ai): la ruta económica del curso para VOLUMEN.

Vídeo: Omni Flash / Veo 3.1 / Sora 2 / Kling. Imagen: GPT Image 2, Nano Banana.
Mucho más barato que la API oficial de Google (revende los mismos modelos).

API confirmada (https://docs.apimart.ai):
  - Enviar vídeo:  POST /v1/videos/generations
        body: {model, prompt, duration, resolution, aspect_ratio, image_urls?[]}
        resp: {code, data:[{status, task_id}]}
  - Enviar imagen: POST /v1/images/generations  (mismo patrón)
  - Estado:        GET  /v1/tasks/{task_id}
        resp: {code, data:{status, cost, result:{videos|images:[{url:[...]}]}}}
        status: pending|processing|completed|failed|cancelled
  - Auth: Authorization: Bearer <APIMART_API_KEY>
  - Las URLs de resultado caducan a las 24 h: descargar enseguida.

IMAGEN→VÍDEO: APImart recibe `image_urls` (URLs públicas), no archivos locales. El
fotograma del avatar debe estar accesible por URL https.
"""
from __future__ import annotations

import os
from typing import Optional

from ..models import Asset, ShotPrompt
from .base import ImageEngine, VideoEngine
from .costs import coste_imagen, coste_video
from .rest_job import RestJobClient

DEFAULT_BASE = "https://api.apimart.ai"

# Alias amigables -> nombre de modelo real en APImart.
VIDEO_MODELOS = {
    "omni-flash": "omni-flash-ext",
    "omni-flash-ext": "omni-flash-ext",
    "veo-3.1": "veo3.1-quality",
    "veo-3.1-fast": "veo3.1-fast",
    "veo3.1-fast": "veo3.1-fast",
    "veo3.1-quality": "veo3.1-quality",
    "sora-2": "sora-2",
    "kling-3": "kling-3",
}


def _client() -> RestJobClient:
    key = os.environ.get("APIMART_API_KEY")
    if not key:
        raise RuntimeError("Falta APIMART_API_KEY en el entorno")
    base = os.environ.get("APIMART_BASE_URL", DEFAULT_BASE)
    return RestJobClient(base, key)


def _task_id(resp: dict) -> str:
    """Extrae el task_id del submit ({code, data:[{task_id}]})."""
    data = resp.get("data")
    if isinstance(data, list) and data:
        data = data[0]
    if isinstance(data, dict) and data.get("task_id"):
        return data["task_id"]
    # algún endpoint puede devolverlo en la raíz
    return resp.get("task_id") or resp.get("id")


def _status(d: dict) -> str:
    return ((d.get("data") or {}).get("status") or d.get("status") or "").lower()


def _result_url(d: dict, clave: str) -> Optional[str]:
    """clave = 'videos' | 'images'. Devuelve la primera URL del resultado."""
    result = (d.get("data") or {}).get("result") or d.get("result") or {}
    items = result.get(clave) or []
    if not items:
        return None
    first = items[0]
    url = first.get("url") if isinstance(first, dict) else first
    if isinstance(url, list):
        url = url[0] if url else None
    return url


class ApimartImage(ImageEngine):
    name = "apimart"
    SUBMIT_PATH = "/v1/images/generations"
    STATUS_PATH = "/v1/tasks/{task_id}"

    def __init__(self, modelo: str = "gpt-image-2"):
        self.modelo = modelo

    def generar_imagen(self, prompt, out_path, referencias=None, aspect_ratio="9:16", resolucion="2K") -> Asset:
        c = _client()
        payload = {"model": self.modelo, "prompt": prompt, "aspect_ratio": aspect_ratio,
                   "resolution": resolucion}
        if referencias:
            payload["image_urls"] = referencias  # URLs https
        resp = c.post(self.SUBMIT_PATH, payload)
        task_id = _task_id(resp)
        url = c.poll(
            check=lambda: c.get(self.STATUS_PATH.format(task_id=task_id)),
            is_done=lambda d: _status(d) == "completed",
            is_failed=lambda d: _status(d) in ("failed", "cancelled"),
            get_result_url=lambda d: _result_url(d, "images"),
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

    def __init__(self, modelo: str = "omni-flash"):
        self.modelo = VIDEO_MODELOS.get(modelo, modelo)

    def generar_video(self, shot: ShotPrompt, out_path: str) -> Asset:
        c = _client()
        payload = {
            "model": self.modelo,
            "prompt": shot.prompt,
            "aspect_ratio": shot.aspect_ratio,
            "duration": shot.duracion_s,
            "resolution": "720p",
        }
        if shot.negative_prompt:
            payload["negative_prompt"] = shot.negative_prompt
        # imagen->vídeo: APImart espera URLs públicas en image_urls (máx 1)
        if shot.primer_frame:
            if not str(shot.primer_frame).startswith("http"):
                raise RuntimeError(
                    "APImart necesita el fotograma como URL pública (image_urls), no un "
                    f"archivo local: {shot.primer_frame}. Súbelo y pasa la URL https.")
            payload["image_urls"] = [shot.primer_frame]
        resp = c.post(self.SUBMIT_PATH, payload)
        task_id = _task_id(resp)
        url = c.poll(
            check=lambda: c.get(self.STATUS_PATH.format(task_id=task_id)),
            is_done=lambda d: _status(d) == "completed",
            is_failed=lambda d: _status(d) in ("failed", "cancelled"),
            get_result_url=lambda d: _result_url(d, "videos"),
        )
        c.download(url, out_path)
        modelo_key = {"veo3.1-quality": "video_veo31_8s", "veo3.1-fast": "video_veo31_8s",
                      "omni-flash-ext": "video_omniflash_8s",
                      "kling-3": "video_kling_5s"}.get(self.modelo, "video_omniflash_8s")
        return Asset(tipo="video", path=out_path, engine=self.name,
                     coste_estimado=coste_video("apimart", modelo_key),
                     meta={"modelo": self.modelo})
