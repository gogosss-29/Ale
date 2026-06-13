"""Ejemplo: construir prompts de un anuncio sin necesidad de API keys.

Muestra el constructor de prompts (paso 3) y el filtro de realismo (paso 6),
que son las piezas que funcionan sin servicios externos.

    python examples/ejemplo_plan.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from avatarhype.brain.prompt_builder import ShotSpec, build_prompt, build_podcast_pair
from avatarhype.assembly.realism_grade import build_full_vf
from avatarhype.models import Acento, Formato

# Guion troceado a mano (en el pipeline real lo genera el LLM en brain/strategy.py)
guion_ugc = [
    "Yo hacía todo bien y aún así tenía la cara hinchada.",
    "Hasta que empecé a usar esto y en tres meses se notó.",
    "Si tienes más de 25 y no usas niacinamida, fatal, amiga.",
    "Te lo dejo por aquí abajo, comenta 'piel' y te paso el link.",
]

print("=== Anuncio UGC: prompts por clip (método 6C) ===\n")
for i, linea in enumerate(guion_ugc):
    shot = build_prompt(ShotSpec(
        formato=Formato.UGC,
        script_line=linea,
        acento=Acento.ESPANA,
        entorno="bright modern bathroom, soft morning daylight",
        microaccion="senalar_arriba_izq" if i == 1 else None,
        microaccion_antes=False,
        movimiento_camara="zoom_lento" if i == 0 else None,
        forzar_muletilla=True,
    ))
    print(f"--- CLIP {i+1} ({shot.duracion_s}s) ---")
    print(shot.prompt)
    print()

print("=== Podcast: par de prompts (cámara estática) ===\n")
izq, der = build_podcast_pair(
    "¿Y qué le recomendarías a alguien estresado todo el día?",
    "Pues mira, yo era escéptica, pero esto me cambió.",
)
print("[IZQUIERDA]\n", izq.prompt[:200], "...\n")
print("[DERECHA]\n", der.prompt[:200], "...\n")

print("=== Capa de realismo (filtro ffmpeg que se aplica en el ensamblado) ===")
print(build_full_vf())
