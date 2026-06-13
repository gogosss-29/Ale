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
    "google": {
        # API oficial de Google (Gemini). MUCHO más cara que APImart por clip.
        # Aproximaciones a confirmar con el pricing vigente de Google (~€/segundo).
        "video_veo31_8s": 3.20,       # Veo 3.1 con audio, 8 s
        "video_veo31fast_8s": 1.20,   # Veo 3.1 Fast, 8 s
        "image_nano_banana": 0.03,    # Gemini 2.5 Flash Image
    },
}


def coste_video(engine: str, modelo: str) -> float:
    return COSTES.get(engine, {}).get(modelo) or 0.0


def coste_imagen(engine: str, modelo: str) -> float:
    return COSTES.get(engine, {}).get(modelo) or 0.0
