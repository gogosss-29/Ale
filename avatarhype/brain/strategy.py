"""Análisis estratégico y generación de guiones (réplica de los agentes GPT del curso).

- `analizar_producto`: producto -> nicho, avatar, pain points, ángulos, datos.
- `generar_guiones`: estrategia -> guiones por formato (UGC, podcast, voz en off...).

Los prompts de sistema codifican la metodología del curso (ángulos que convierten,
tono UGC real, guiones de ~8 s pensados para clips).
"""
from __future__ import annotations

from ..models import Estrategia, Formato, Guion, ProductBrief
from . import llm

_SYS_ESTRATEGIA = """Eres un estratega de performance marketing para e-commerce, experto en \
anuncios UGC que convierten. Dado un producto, defines con precisión quirúrgica:
- nicho
- avatar objetivo (público concreto: edad, situación, deseo)
- pain points reales (lo que de verdad les duele)
- ángulos de venta más potentes
- datos estadísticos creíbles que se puedan usar en el anuncio
Respondes SIEMPRE en JSON con las claves: nicho, avatar_objetivo, pain_points (lista),
angulos_venta (lista), datos_estadisticos (lista). Nada de texto fuera del JSON."""

_SYS_GUIONES = """Eres un copywriter de anuncios UGC con IA. Escribes guiones que suenan a \
persona real, no a anuncio: tono casual, sin vender de forma obvia, con gancho en los \
primeros 2 segundos y un CTA natural al final (tipo 'comenta X y te paso el link').
Cada guion debe poder trocearse en clips de ~8 segundos.
Adaptas el guion al MERCADO y al ACENTO indicados.
Respondes SIEMPRE en JSON: {"texto": "...", "lineas": ["frase1", "frase2", ...]}.
Las 'lineas' son el guion troceado frase a frase para edición."""


def analizar_producto(brief: ProductBrief) -> Estrategia:
    user = (
        f"Producto: {brief.nombre}\n"
        f"Descripción: {brief.descripcion}\n"
        f"Mercado: {brief.mercado}\n"
        f"{('Notas: ' + brief.notas) if brief.notas else ''}"
    )
    d = llm.completar_json(_SYS_ESTRATEGIA, user, temperature=0.7)
    return Estrategia(
        nicho=d.get("nicho", ""),
        avatar_objetivo=d.get("avatar_objetivo", ""),
        pain_points=d.get("pain_points", []),
        angulos_venta=d.get("angulos_venta", []),
        datos_estadisticos=d.get("datos_estadisticos", []),
    )


def generar_guion(brief: ProductBrief, estrategia: Estrategia, formato: Formato) -> Guion:
    user = (
        f"Producto: {brief.nombre} — {brief.descripcion}\n"
        f"Mercado: {brief.mercado} · Acento: {brief.acento.value}\n"
        f"Nicho: {estrategia.nicho}\n"
        f"Avatar: {estrategia.avatar_objetivo}\n"
        f"Pain points: {'; '.join(estrategia.pain_points)}\n"
        f"Ángulos: {'; '.join(estrategia.angulos_venta)}\n"
        f"Datos: {'; '.join(estrategia.datos_estadisticos)}\n"
        f"Formato del anuncio: {formato.value}\n\n"
        "Escribe el guion para este formato."
    )
    d = llm.completar_json(_SYS_GUIONES, user, temperature=0.85)
    return Guion(formato=formato, texto=d.get("texto", ""), lineas=d.get("lineas", []))


def generar_guiones(brief: ProductBrief, estrategia: Estrategia) -> list[Guion]:
    return [generar_guion(brief, estrategia, f) for f in brief.formatos]
