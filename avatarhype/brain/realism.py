"""Constantes de realismo extraídas literalmente del curso AvatarHype.

Centraliza los "ingredientes secretos" del sistema: el negative prompt, los bloques
de idioma/acento, las microacciones, los movimientos de cámara y los valores exactos
de la capa de realismo de CapCut (traducidos a filtros ffmpeg en assembly/realism_grade.py).
"""
from __future__ import annotations

from ..models import Acento

# --- Negative prompt estándar (mata el "look IA") -------------------------------
NEGATIVE_PROMPT = (
    "studio lighting, beauty filter, perfect skin, ad-like polish, exaggerated "
    "gestures, robotic delivery, over-sharpening, artificial background, "
    "unnatural motion, flicker"
)

# --- Bloques de idioma/acento ---------------------------------------------------
# El español de España es el que más cuesta; con Veo 3.1 hay que forzarlo.
ACENTO_BLOQUE: dict[Acento, str] = {
    Acento.ESPANA: (
        "Use informal conversational Spanish as spoken in Spain. The phrasing, "
        "rhythm, and wording must feel like a real casual conversation between "
        'people in Spain. Include natural filler words typical in Spain such as '
        '"a ver…", "es que…", with small pauses and hesitations. '
        "Accent: Peninsular Spanish (Madrid neutral). Not Latin American Spanish."
    ),
    Acento.LATAM: "Spanish, neutral Latin American accent.",
    Acento.ARGENTINA: "Spanish with a natural Argentinian (Rioplatense) accent.",
    Acento.COLOMBIA: "Spanish with a natural Colombian accent.",
    Acento.MEXICO: "Spanish with a natural Mexican accent.",
    Acento.INGLES: "Natural conversational English.",
}

# Truco del curso: para forzar España, anteponer una palabra muy de España al guion
# y cortarla luego en edición. Con Omni Flash (Vol.4) casi no hace falta.
MULETILLA_ESPANA = "joder"


# --- Física humana / comportamiento (bloque 5 y 9) ------------------------------
FISICA_HUMANA = (
    "Movement must feel completely natural and human: slight vertical bounce, "
    "subtle side-to-side sway, natural shoulder movement, inconsistent "
    "micro-movements, and breathing that subtly affects motion and speech"
)

COMPORTAMIENTO = (
    "Starts speaking slightly mid-thought, blinks naturally, briefly glances away, "
    "subtle pauses between phrases, subtle facial micro-expressions"
)

# --- Cámara (bloque 10) ---------------------------------------------------------
CAMARA_ESTATICA = "static camera, no movement, as if mounted on a tripod"
CAMARA_HANDHELD = (
    "handheld iPhone selfie, slightly off-center framing, natural micro-shake, "
    "minor autofocus adjustments, rolling shutter effect, no stabilization"
)

# Movimientos de cámara de la biblioteca (Vol. 4)
MOVIMIENTOS_CAMARA = {
    "plano_fijo": "static camera, completely still",
    "zoom_lento": "slow gentle zoom in toward the face",
    "zoom_rapido": "fast abrupt zoom that snaps closer to the person's face",
    "movil_en_mano": "phone held in hand, slight natural shake as if recorded by a real person",
    "retroceso": "camera slowly pulls back revealing the environment",
    "seguimiento": "camera follows the person while they walk toward the camera",
}

# --- Microacciones / gestos (Vol. 4) --------------------------------------------
# Dan realismo. Se insertan antes o durante el habla.
MICROACCIONES = {
    "ajustarse_gorra": "adjusts their cap",
    "sorbo_cafe": "takes a sip of coffee",
    "tocarse_pelo": "touches their hair",
    "saludar_mano": "waves with their hand",
    "reir": "laughs briefly",
    "asentir": "nods while smiling",
    "senalar_arriba_izq": "points to the upper-left corner, as if pointing at an overlaid image",
    "senalar_arriba_der": "points to the upper-right corner, as if pointing at an overlaid image",
}

# --- Luz y audio (bloques 11 y 12) ----------------------------------------------
LUZ = "natural daylight only, slight exposure changes, soft uneven shadows"
AUDIO = "raw iPhone microphone, light ambient noise, audible breathing, no music"


# --- Prompts de imagen reutilizables (referencia visual) ------------------------
IMG_CAMBIAR_AVATAR = "make this woman/man a different one, {descripcion}"
IMG_REEMPLAZAR_FONDO = (
    "replace the person from file 1 with the person from file 2 wearing the same "
    "outfit as in file 2, talking to camera and gesticulating. {extra}"
)
IMG_PLANO_CERCANO = (
    "A closer view of this same image shows less background. The person is talking "
    "to the camera, you can see their teeth well"
)
IMG_FLIP = "Flip the image horizontally"
IMG_PODCAST_MIRADA = (
    "The person is looking to the {lado} side of the frame, as if talking to "
    "someone sitting next to them"
)

# --- Capa de realismo CapCut (Vol. 2) -------------------------------------------
# Valores en la escala de CapCut (-100..100). Se traducen a ffmpeg en realism_grade.py.
CAPCUT_REALISM = {
    "temperatura": -3,
    "tinte": 2,
    "saturacion": -6,
    "exposicion": -3,
    "contraste": 12,
    "highlights": -35,
    "sombras": -18,
    "fade": 6,
    "motion_blur": 20,   # %
    "particulas": 10,    # %
}
