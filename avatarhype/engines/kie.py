"""Motor Kie.ai: ruta alternativa (Sora 2 y otros modelos de vídeo/imagen).

Misma mecánica que APImart (submit -> poll -> download). Paths a confirmar con la
doc de Kie. Lee credenciales del entorno: KIE_API_KEY, KIE_BASE_URL (def https://api.kie.ai).
"""
from __future__ import annotations

import os

from ..models import Asset, ShotPrompt
from .base import VideoEngine
from .costs import coste_video
from .rest_job import RestJobClient

DEFAULT_BASE = "https://api.kie.ai"


def _client() -> RestJobClient:
    key = os.environ.get("KIE_API_KEY")
    if not key:
        raise RuntimeError("Falta KIE_API_KEY en el entorno")
    base = os.environ.get("KIE_BASE_URL", DEFAULT_BASE)
    return RestJobClient(base, key)


class KieVideo(VideoEngine):
    name = "kie"
    SUBMIT_PATH = "/v1/video/generate"
    STATUS_PATH = "/v1/video/status/{task_id}"

    def __init__(self, modelo: str = "sora-2"):
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
            payload["image"] = shot.primer_frame  # Sora 2: imagen->vídeo
        resp = c.post(self.SUBMIT_PATH, payload)
        task_id = resp.get("task_id") or resp.get("id")
        url = c.poll(
            check=lambda: c.get(self.STATUS_PATH.format(task_id=task_id)),
            is_done=lambda d: d.get("status") in ("succeeded", "completed"),
            is_failed=lambda d: d.get("status") in ("failed", "error"),
            get_result_url=lambda d: (d.get("output") or {}).get("url") or d.get("result_url"),
        )
        c.download(url, out_path)
        return Asset(tipo="video", path=out_path, engine=self.name,
                     coste_estimado=coste_video("kie", "video_sora2_15s"),
                     meta={"modelo": self.modelo})
