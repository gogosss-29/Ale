"""CLI del pipeline AvatarHype.

Ejemplos:
    # Solo planificar (estrategia + guiones + prompts), no gasta créditos:
    python -m avatarhype.cli plan --nombre "Sérum niacinamida" \
        --descripcion "Sérum para el acné y manchas" --mercado España --formatos ugc,podcast

    # Pipeline completo (requiere API keys, ver .env.example):
    python -m avatarhype.cli producir --nombre "..." --descripcion "..." --ruta apimart
"""
from __future__ import annotations

import argparse
import json
import sys

from .config import EngineConfig
from .models import Acento, Formato, ProductBrief


def _parse_formatos(s: str) -> list[Formato]:
    return [Formato(x.strip()) for x in s.split(",") if x.strip()]


def _brief_from_args(a) -> ProductBrief:
    return ProductBrief(
        nombre=a.nombre,
        descripcion=a.descripcion,
        mercado=a.mercado,
        acento=Acento(a.acento),
        formatos=_parse_formatos(a.formatos),
        imagen_producto_path=a.imagen_producto,
        paleta_colores=a.paleta,
        notas=a.notas,
    )


def _add_common(p):
    p.add_argument("--nombre", required=True)
    p.add_argument("--descripcion", required=True)
    p.add_argument("--mercado", default="España")
    p.add_argument("--acento", default="es-ES")
    p.add_argument("--formatos", default="ugc")
    p.add_argument("--imagen-producto", default=None)
    p.add_argument("--paleta", default=None)
    p.add_argument("--notas", default=None)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="avatarhype")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_plan = sub.add_parser("plan", help="Estrategia + guiones + prompts (sin generar media)")
    _add_common(p_plan)

    p_prod = sub.add_parser("producir", help="Pipeline completo (requiere API keys)")
    _add_common(p_prod)
    p_prod.add_argument("--ruta", default="apimart", choices=["apimart", "kie", "higgsfield"])
    p_prod.add_argument("--modelo-video", default="omni-flash")
    p_prod.add_argument("--musica", default=None)
    p_prod.add_argument("--out", default="output")

    p_cut = sub.add_parser(
        "cortar",
        help="Trocear un video grabado en clips cortados en silencios (reel_cutter)",
    )
    p_cut.add_argument("video", help="Ruta al video (mp4/mov)")
    p_cut.add_argument("--max", type=float, default=10.0)
    p_cut.add_argument("--min", type=float, default=4.0)
    p_cut.add_argument("--noise", type=float, default=-32.0)
    p_cut.add_argument("--min-silence", type=float, default=0.16, dest="min_silence")
    p_cut.add_argument("--cortes", default=None)
    p_cut.add_argument("--modelo", default="large-v3")
    p_cut.add_argument("--out", default="salida")

    a = parser.parse_args(argv)

    if a.cmd == "cortar":
        from .assembly.reel_cutter_bridge import cortar_video
        r = cortar_video(
            a.video, out_dir=a.out, max_s=a.max, min_s=a.min,
            noise_db=a.noise, min_silence=a.min_silence,
            cortes=a.cortes, modelo=a.modelo,
        )
        for c in r.clips:
            print(f"[{c.meta['duracion']:.2f}s] {c.path}\n    «{c.meta['texto']}»")
        print(f"\nMapeo legible: {r.mapeo_md}")
        return 0

    brief = _brief_from_args(a)

    if a.cmd == "plan":
        from .pipeline import planificar
        r = planificar(brief)
        out = {
            "estrategia": r.estrategia.__dict__,
            "guiones": [{"formato": g.formato.value, "texto": g.texto, "lineas": g.lineas}
                        for g in r.guiones],
            "shots": [{"formato": s.formato.value, "script": s.script_line,
                       "prompt": s.prompt} for s in r.shots],
        }
        print(json.dumps(out, ensure_ascii=False, indent=2))
    elif a.cmd == "producir":
        from .pipeline import producir
        cfg = EngineConfig(ruta=a.ruta, modelo_video=a.modelo_video, out_dir=a.out)
        r = producir(brief, cfg=cfg, musica=a.musica)
        for an in r.anuncios:
            print(f"[{an.formato.value}] {an.path}  (coste ~{an.coste_total:.3f} €, "
                  f"{len(an.clips)} clips)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
