"""Configuración del pipeline: selección de motores y rutas, desde entorno o por código."""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class EngineConfig:
    """Qué motor/modelo usar en cada paso. 'ruta' permite comparar Higgsfield vs APImart/Kie."""

    ruta: str = "apimart"          # "apimart" | "kie" | "higgsfield"
    modelo_imagen: str = "gpt-image-2"
    modelo_video: str = "omni-flash"  # recomendado por el curso (Vol.4)
    out_dir: str = "output"

    @classmethod
    def from_env(cls) -> "EngineConfig":
        return cls(
            ruta=os.environ.get("AVATARHYPE_RUTA", cls.ruta),
            modelo_imagen=os.environ.get("AVATARHYPE_MODELO_IMAGEN", cls.modelo_imagen),
            modelo_video=os.environ.get("AVATARHYPE_MODELO_VIDEO", cls.modelo_video),
            out_dir=os.environ.get("AVATARHYPE_OUT", cls.out_dir),
        )


def build_engines(cfg: EngineConfig):
    """Devuelve (image_engine, video_engine) según la ruta elegida."""
    if cfg.ruta == "apimart":
        from .engines.apimart import ApimartImage, ApimartVideo
        return ApimartImage(cfg.modelo_imagen), ApimartVideo(cfg.modelo_video)
    if cfg.ruta == "kie":
        from .engines.apimart import ApimartImage   # imagen vía APImart
        from .engines.kie import KieVideo
        return ApimartImage(cfg.modelo_imagen), KieVideo("sora-2")
    if cfg.ruta == "higgsfield":
        from .engines.higgsfield import HiggsfieldImage, HiggsfieldVideo
        return HiggsfieldImage(cfg.modelo_imagen), HiggsfieldVideo(cfg.modelo_video)
    if cfg.ruta == "google":
        from .engines.google import GoogleGeminiImage, GoogleVeoVideo
        # modelo_video de Google: veo-3.1-fast-generate-preview (barato) o veo-3.1-generate-preview
        modelo = cfg.modelo_video if cfg.modelo_video.startswith("veo") else "veo-3.1-fast-generate-preview"
        return GoogleGeminiImage(), GoogleVeoVideo(modelo)
    raise ValueError(f"ruta desconocida: {cfg.ruta}")
