"""Ensamblado final del anuncio con ffmpeg.

Une los clips, aplica la capa de realismo, normaliza a 9:16 y añade música.
Equivale a la edición que el curso hace a mano en CapCut, pero automatizada.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import tempfile

from .realism_grade import build_cine_vf, build_full_vf


def _run(cmd: list[str]) -> None:
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg falló:\n{' '.join(cmd)}\n{proc.stderr[-2000:]}")


def poner_voz(video: str, audio: str, salida: str) -> str:
    """Reemplaza el audio del vídeo por `audio` (tu voz de ElevenLabs). Doblaje simple:
    monta tu voz sobre el clip y descarta la voz del modelo. Devuelve `salida`.

    OJO: esto NO re-sincroniza los labios. Si la voz nueva no cuadra con el movimiento
    de boca generado por el modelo, hace falta un paso de LIP-SYNC aparte (modelo
    dedicado: Higgsfield audio→vídeo, sync.so, etc.). Ver pipeline/README."""
    if not ffmpeg_disponible():
        raise RuntimeError("ffmpeg no está instalado")
    for f in (video, audio):
        if not os.path.exists(f):
            raise FileNotFoundError(f)
    _run([
        "ffmpeg", "-y", "-i", video, "-i", audio,
        "-map", "0:v", "-map", "1:a",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", salida,
    ])
    return salida


def ffmpeg_disponible() -> bool:
    return shutil.which("ffmpeg") is not None


def aplicar_realismo(
    clip: str,
    salida: str,
    grade: dict | None = None,
    grano: bool = True,
    estilo: str = "ugc",
) -> str:
    """Aplica SOLO la capa de realismo a un clip (sin concatenar ni música).

    `estilo`: "ugc" (look selfie crudo del curso) o "cine" (estética de anuncio).
    Para clips generados a mano (Omni Flash) que solo necesitan el grade final.
    Devuelve `salida`."""
    if not ffmpeg_disponible():
        raise RuntimeError("ffmpeg no está instalado")
    if not os.path.exists(clip):
        raise FileNotFoundError(clip)
    builder = build_cine_vf if estilo == "cine" else build_full_vf
    vf = builder(grade, add_grain=grano)
    _run([
        "ffmpeg", "-y", "-i", clip, "-vf", vf,
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-c:a", "copy", salida,
    ])
    return salida


def ensamblar(
    clips: list[str],
    salida: str,
    musica: str | None = None,
    grade: dict | None = None,
    grano: bool = True,
    volumen_musica_db: float = -30.0,
    fps: int = 30,
    width: int = 1080,
    height: int = 1920,
) -> str:
    """Concatena clips -> aplica realismo -> (opcional) música. Devuelve `salida`.

    - `volumen_musica_db`: el curso pone la música a ~-30 dB.
    - `grade`: overrides de los valores de realismo (ver brain/realism.CAPCUT_REALISM).
    """
    if not ffmpeg_disponible():
        raise RuntimeError("ffmpeg no está instalado")
    if not clips:
        raise ValueError("no hay clips para ensamblar")

    vf_realism = build_full_vf(grade, add_grain=grano)
    tmp = tempfile.mkdtemp(prefix="avhype_")
    try:
        # 1) normalizar cada clip a 9:16/fps y aplicar la capa de realismo
        norm_clips = []
        for i, c in enumerate(clips):
            out = os.path.join(tmp, f"norm_{i:03d}.mp4")
            vf = (
                f"scale={width}:{height}:force_original_aspect_ratio=increase,"
                f"crop={width}:{height},{vf_realism},fps={fps}"
            )
            _run([
                "ffmpeg", "-y", "-i", c, "-vf", vf,
                "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                "-c:a", "aac", "-b:a", "128k", out,
            ])
            norm_clips.append(out)

        # 2) concatenar
        lista = os.path.join(tmp, "concat.txt")
        with open(lista, "w") as f:
            for nc in norm_clips:
                f.write(f"file '{nc}'\n")
        concat_out = os.path.join(tmp, "concat.mp4")
        _run([
            "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lista,
            "-c", "copy", concat_out,
        ])

        # 3) música de fondo (opcional)
        if musica and os.path.exists(musica):
            _run([
                "ffmpeg", "-y", "-i", concat_out, "-i", musica,
                "-filter_complex",
                f"[1:a]volume={volumen_musica_db}dB[bg];[0:a][bg]amix=inputs=2:duration=first[a]",
                "-map", "0:v", "-map", "[a]",
                "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-shortest", salida,
            ])
        else:
            shutil.copy(concat_out, salida)

        return salida
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
