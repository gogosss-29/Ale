"""Puente entre AvatarHype y la herramienta reel_cutter.

reel_cutter (plugin `plugins/reel-cutter/`) transcribe un video en español con
timestamps de palabra, corta en silencios sin partir palabras y exporta clips.
Este módulo lo invoca como subproceso y traduce sus salidas al modelo de datos
de AvatarHype (Asset), para usarlo como paso del pipeline (p. ej. trocear un
video largo grabado por el avatar en clips listos para montar).
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from dataclasses import dataclass, field

from ..models import Asset

# Rutas candidatas al script canónico (la fuente de verdad vive en el plugin).
_CANDIDATOS = (
    os.environ.get("REEL_CUTTER_SCRIPT"),
    # dentro de este repo: <root>/plugins/reel-cutter/skills/reel-cutter/scripts/reel_cutter.py
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        "plugins", "reel-cutter", "skills", "reel-cutter", "scripts", "reel_cutter.py",
    ),
)


def localizar_script() -> str:
    for c in _CANDIDATOS:
        if c and os.path.isfile(c):
            return c
    raise FileNotFoundError(
        "No encuentro reel_cutter.py. Define REEL_CUTTER_SCRIPT o asegúrate de "
        "que existe plugins/reel-cutter/skills/reel-cutter/scripts/reel_cutter.py"
    )


@dataclass
class ResultadoCorte:
    """Salida del corte: clips como Assets + metadatos por segmento."""

    clips: list[Asset] = field(default_factory=list)
    segments: list[dict] = field(default_factory=list)  # contenido de segments.json
    out_dir: str = ""

    @property
    def mapeo_md(self) -> str:
        return os.path.join(self.out_dir, "mapeo_clips.md")


def cortar_video(
    video: str,
    out_dir: str = "salida",
    max_s: float = 10.0,
    min_s: float = 4.0,
    noise_db: float = -32.0,
    min_silence: float = 0.16,
    cortes: str | None = None,
    modelo: str = "large-v3",
) -> ResultadoCorte:
    """Ejecuta reel_cutter sobre `video` y devuelve los clips como Assets.

    Cada Asset lleva en `meta` el texto del clip y sus palabras con tiempos
    relativos (para sincronizar animaciones en el montaje).
    """
    script = localizar_script()
    cmd = [
        sys.executable, script, video,
        "--salida", out_dir,
        "--max", str(max_s), "--min", str(min_s),
        "--noise", str(noise_db), "--min-silence", str(min_silence),
        "--modelo", modelo,
    ]
    if cortes:
        cmd += ["--cortes", cortes]

    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(
            f"reel_cutter falló (código {proc.returncode}):\n{proc.stderr[-2000:]}"
        )

    seg_path = os.path.join(out_dir, "segments.json")
    if not os.path.isfile(seg_path):
        raise RuntimeError(f"reel_cutter terminó pero no existe {seg_path}")
    with open(seg_path, encoding="utf-8") as f:
        segments = json.load(f)

    clips_dir = os.path.join(out_dir, "clips")
    clips: list[Asset] = []
    for seg in segments:
        nombre = f"seq_{seg['index']:02d}_{seg['inicio']:.2f}-{seg['fin']:.2f}s.mp4"
        clips.append(Asset(
            tipo="video",
            path=os.path.join(clips_dir, nombre),
            engine="reel_cutter",
            meta={
                "texto": seg["texto"],
                "inicio": seg["inicio"],
                "fin": seg["fin"],
                "duracion": seg["duracion"],
                "palabras": seg["palabras"],
            },
        ))
    return ResultadoCorte(clips=clips, segments=segments, out_dir=out_dir)
