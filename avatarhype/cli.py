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
        avatar_referencia_path=getattr(a, "avatar_referencia", None),
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
    p.add_argument("--avatar-referencia", default=None,
                   help="Foto de tu cara: el avatar se generará a partir de ella")
    p.add_argument("--paleta", default=None)
    p.add_argument("--notas", default=None)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="avatarhype")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_plan = sub.add_parser("plan", help="Estrategia + guiones + prompts (sin generar media)")
    _add_common(p_plan)

    p_avatar = sub.add_parser(
        "avatar",
        help="Solo el paso de identidad: genera tu avatar-ancla desde tu foto (1 imagen)")
    _add_common(p_avatar)
    p_avatar.add_argument("--ruta", default="apimart", choices=["apimart", "kie", "higgsfield"])
    p_avatar.add_argument("--out", default="output")

    p_prod = sub.add_parser("producir", help="Pipeline completo (requiere API keys)")
    _add_common(p_prod)
    p_prod.add_argument("--ruta", default="apimart", choices=["apimart", "kie", "higgsfield"])
    p_prod.add_argument("--modelo-video", default="omni-flash")
    p_prod.add_argument("--musica", default=None)
    p_prod.add_argument("--out", default="output")

    a = parser.parse_args(argv)
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
    elif a.cmd == "avatar":
        import os
        from .config import build_engines
        from .pipeline import generar_avatar_identidad
        if not brief.avatar_referencia_path:
            print("Falta --avatar-referencia (la foto de tu cara).", file=sys.stderr)
            return 2
        cfg = EngineConfig(ruta=a.ruta, out_dir=a.out)
        os.makedirs(cfg.out_dir, exist_ok=True)
        try:
            img_engine, _ = build_engines(cfg)
            path = generar_avatar_identidad(brief, img_engine, cfg.out_dir)
        except RuntimeError as e:
            print(f"No se pudo generar: {e}", file=sys.stderr)
            return 2
        print(f"Avatar-ancla generado: {path}")
    elif a.cmd == "producir":
        from .pipeline import producir
        cfg = EngineConfig(ruta=a.ruta, modelo_video=a.modelo_video, out_dir=a.out)
        try:
            r = producir(brief, cfg=cfg, musica=a.musica)
        except RuntimeError as e:
            print(f"No se pudo producir: {e}", file=sys.stderr)
            return 2
        for an in r.anuncios:
            print(f"[{an.formato.value}] {an.path}  (coste ~{an.coste_total:.3f} €, "
                  f"{len(an.clips)} clips)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
