"""Traduce la 'capa de realismo' de CapCut a un filtro ffmpeg.

El curso aplica en CapCut estos ajustes (escala -100..100):
    Temperatura -3 · Tinte +2 · Saturación -6 · Exposición -3 · Contraste +12
    Highlights -35 · Sombras -18 · Fade +6   (+ motion blur 20%, partículas 10%)

Aquí los aproximamos con filtros ffmpeg (eq, colorbalance, colortemperature).
Los mapeos son aproximaciones razonables y están centralizados para poder afinarlos.
"""
from __future__ import annotations

from ..brain.realism import CAPCUT_REALISM


def _lin(v: float, in_lo: float, in_hi: float, out_lo: float, out_hi: float) -> float:
    """Interpola linealmente v de [in_lo,in_hi] a [out_lo,out_hi]."""
    if in_hi == in_lo:
        return out_lo
    t = (v - in_lo) / (in_hi - in_lo)
    return out_lo + t * (out_hi - out_lo)


def build_eq_filter(grade: dict | None = None) -> str:
    """Construye la cadena de filtros ffmpeg que replica la capa de realismo.

    Devuelve algo como: "colortemperature=...,eq=...,colorbalance=...".
    """
    g = {**CAPCUT_REALISM, **(grade or {})}

    # eq: contrast (1.0 neutro), brightness (0 neutro, -1..1), saturation (1.0 neutro)
    # En CapCut 0 es neutro: -100..100 -> 0..2 para que 0 -> 1.0 (neutro).
    contrast = round(_lin(g["contraste"], -100, 100, 0.0, 2.0), 3)          # +12 -> ~1.12
    brightness = round(_lin(g["exposicion"], -100, 100, -1.0, 1.0), 3)       # -3 -> ~-0.03
    saturation = round(_lin(g["saturacion"], -100, 100, 0.0, 2.0), 3)        # -6 -> ~0.94

    # gamma para 'fade' (levanta negros): fade +6 -> gamma un pelín >1 + subir luma low
    gamma = round(_lin(g["fade"], 0, 100, 1.0, 1.3), 3)                       # +6 -> ~1.018

    eq = f"eq=contrast={contrast}:brightness={brightness}:saturation={saturation}:gamma={gamma}"

    # temperatura de color: -3 (más frío). colortemperature en Kelvin, 6500 neutro.
    kelvin = int(_lin(g["temperatura"], -100, 100, 8000, 5000))              # negativo -> más frío(<6500)
    temp = f"colortemperature=temperature={kelvin}"

    # tinte (verde/magenta) y sombras/highlights via colorbalance
    tint = round(_lin(g["tinte"], -100, 100, -0.3, 0.3), 3)                  # +2 -> hacia magenta
    shadows = round(_lin(g["sombras"], -100, 100, -0.3, 0.3), 3)            # -18 -> bajar sombras
    highs = round(_lin(g["highlights"], -100, 100, -0.3, 0.3), 3)          # -35 -> bajar highlights
    cb = (
        f"colorbalance=rs={shadows}:gs={-tint}:bs={-shadows}"
        f":rh={highs}:gh={-tint/2}:bh={-highs}"
    )

    return f"{temp},{eq},{cb}"


def build_full_vf(grade: dict | None = None, add_grain: bool = True) -> str:
    """Filtro completo: grade + grano sutil (las 'partículas' del curso)."""
    vf = build_eq_filter(grade)
    if add_grain:
        g = {**CAPCUT_REALISM, **(grade or {})}
        strength = round(_lin(g["particulas"], 0, 100, 0, 20), 1)            # 10% -> ~2
        vf += f",noise=alls={strength}:allf=t"
    return vf
