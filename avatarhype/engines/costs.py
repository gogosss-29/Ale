"""Tabla de costes por ruta (EUR), según el curso, para comparar motores.

Sirve a la feature 'comparar Higgsfield vs APImart/Kie': cada Asset reporta su
coste estimado y el pipeline suma el total por anuncio.
Precios aproximados del curso (actualizar si cambian).
"""
from __future__ import annotations

# EUR por unidad. clip = 8 s salvo que se indique.
COSTES = {
    "kie": {
        "video_sora2_15s": 0.15,
    },
    "apimart": {
        "video_veo31_8s": 0.08,
        "video_omniflash_8s": 0.08,
        "video_kling_5s": 0.12,
        "image_gpt_image_2": 0.012,
        "image_nano_banana_pro": 0.15,
    },
    "higgsfield": {
        # se rellena con el balance/credits reales de Higgsfield al integrarlo
        "video_default_clip": None,
        "image_default": None,
    },
}


def coste_video(engine: str, modelo: str) -> float:
    return COSTES.get(engine, {}).get(modelo) or 0.0


def coste_imagen(engine: str, modelo: str) -> float:
    return COSTES.get(engine, {}).get(modelo) or 0.0
