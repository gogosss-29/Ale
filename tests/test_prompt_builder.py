"""Tests del constructor de prompts (determinista, sin LLM ni red)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from avatarhype.brain.prompt_builder import ShotSpec, build_prompt, build_podcast_pair
from avatarhype.brain import realism
from avatarhype.models import Acento, Formato


def test_estructura_14_bloques():
    shot = build_prompt(ShotSpec(
        formato=Formato.UGC,
        script_line="Llevo tres meses usando esto y se nota.",
        acento=Acento.ESPANA,
        entorno="bright bathroom, morning light",
        microaccion="sorbo_cafe",
    ))
    p = shot.prompt
    for bloque in ["[CHARACTER]", "[ACTION]", "[HUMAN MOTION]", "[LANGUAGE]",
                   "[TONE]", "[SCRIPT]", "[CAMERA]", "[LIGHTING]", "[AUDIO]",
                   "[NEGATIVE PROMPT]", "[MICRO-ACTION]"]:
        assert bloque in p, f"falta {bloque}"
    assert realism.NEGATIVE_PROMPT in p
    assert "Peninsular Spanish" in p  # acento España forzado
    assert shot.negative_prompt == realism.NEGATIVE_PROMPT


def test_muletilla_espana():
    shot = build_prompt(ShotSpec(
        formato=Formato.UGC, script_line="esto me cambió la piel.",
        acento=Acento.ESPANA, forzar_muletilla_espana=True,
    ))
    assert shot.script_line.lower().startswith("joder")


def test_acento_latam_no_fuerza_muletilla():
    shot = build_prompt(ShotSpec(
        formato=Formato.UGC, script_line="esto funciona.",
        acento=Acento.LATAM, forzar_muletilla_espana=True,
    ))
    assert not shot.script_line.lower().startswith("joder")
    assert "Latin American" in shot.prompt


def test_frames_start_end():
    shot = build_prompt(ShotSpec(
        formato=Formato.UGC, script_line="mira el antes y después.",
        primer_frame="a.png", ultimo_frame="b.png",
    ))
    assert "[START FRAME]" in shot.prompt and "[END FRAME]" in shot.prompt


def test_podcast_pair():
    izq, der = build_podcast_pair("¿Y qué recomiendas?", "Pues mira, esto.")
    assert izq.formato == Formato.PODCAST and der.formato == Formato.PODCAST
    assert "static camera" in izq.prompt.lower()


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn(); print(f"PASS {name}")
    print("OK")
