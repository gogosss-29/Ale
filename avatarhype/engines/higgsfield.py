"""Motor Higgsfield: generación de imagen y vídeo.

DOS VÍAS DE INTEGRACIÓN:
  1) API REST de Higgsfield (producción): lee HIGGSFIELD_API_KEY / HIGGSFIELD_BASE_URL.
  2) MCP de Higgsfield (en una sesión de Claude Code con el server conectado): se usa para
     VALIDAR calidad/coste de forma interactiva, no desde un script suelto.

El coste real se toma del balance/credits de Higgsfield al integrarlo (ver engines/costs.py).
"""
from __future__ import annotations

import os
from typing import Optional

from ..models import Asset, ShotPrompt
from .base import ImageEngine, VideoEngine
from .rest_job import RestJobClient

DEFAULT_BASE = "https://api.higgsfield.ai"


def _client() -> RestJobClient:
    key = os.environ.get("HIGGSFIELD_API_KEY")
    if not key:
        raise RuntimeError("Falta HIGGSFIELD_API_KEY en el entorno")
    base = os.environ.get("HIGGSFIELD_BASE_URL", DEFAULT_BASE)
    return RestJobClient(base, key)


class HiggsfieldImage(ImageEngine):
    name = "higgsfield"
    SUBMIT_PATH = "/v1/images"
    STATUS_PATH = "/v1/jobs/{task_id}"

    def __init__(self, modelo: str = "default"):
        self.modelo = modelo

    def generar_imagen(self, prompt, out_path, referencias=None, aspect_ratio="9:16", resolucion="2K") -> Asset:
        c = _client()
        payload = {"model": self.modelo, "prompt": prompt, "aspect_ratio": aspect_ratio}
        if referencias:
            payload["references"] = referencias
        resp = c.post(self.SUBMIT_PATH, payload)
        task_id = resp.get("id") or resp.get("job_id")
        url = c.poll(
            check=lambda: c.get(self.STATUS_PATH.format(task_id=task_id)),
            is_done=lambda d: d.get("status") in ("completed", "succeeded"),
            is_failed=lambda d: d.get("status") in ("failed", "error"),
            get_result_url=lambda d: (d.get("result") or {}).get("url"),
        )
        c.download(url, out_path)
        return Asset(tipo="image", path=out_path, engine=self.name, meta={"modelo": self.modelo})


class HiggsfieldVideo(VideoEngine):
    name = "higgsfield"
    SUBMIT_PATH = "/v1/videos"
    STATUS_PATH = "/v1/jobs/{task_id}"

    def __init__(self, modelo: str = "default"):
        self.modelo = modelo

    def generar_video(self, shot: ShotPrompt, out_path: str) -> Asset:
        c = _client()
        payload = {
            "model": self.modelo,
            "prompt": shot.prompt,
            "aspect_ratio": shot.aspect_ratio,
            "duration": shot.duracion_s,
        }
        if shot.primer_frame:
            payload["first_frame"] = shot.primer_frame
        if shot.ultimo_frame:
            payload["last_frame"] = shot.ultimo_frame
        resp = c.post(self.SUBMIT_PATH, payload)
        task_id = resp.get("id") or resp.get("job_id")
        url = c.poll(
            check=lambda: c.get(self.STATUS_PATH.format(task_id=task_id)),
            is_done=lambda d: d.get("status") in ("completed", "succeeded"),
            is_failed=lambda d: d.get("status") in ("failed", "error"),
            get_result_url=lambda d: (d.get("result") or {}).get("url"),
        )
        c.download(url, out_path)
        return Asset(tipo="video", path=out_path, engine=self.name, meta={"modelo": self.modelo})
