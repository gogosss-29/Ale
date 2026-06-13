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
        avatar_frame_path=getattr(a, "avatar_frame", None),
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
                   help="Foto de tu cara: el avatar se GENERARÁ a partir de ella")
    p.add_argument("--avatar-frame", default=None,
                   help="Fotograma de un avatar YA hecho: se usa TAL CUAL como frame inicial")
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
    p_avatar.add_argument("--ruta", default="apimart", choices=["apimart", "kie", "higgsfield", "google"])
    p_avatar.add_argument("--out", default="output")

    p_prod = sub.add_parser("producir", help="Pipeline completo (requiere API keys)")
    _add_common(p_prod)
    p_prod.add_argument("--ruta", default="apimart", choices=["apimart", "kie", "higgsfield", "google"])
    p_prod.add_argument("--modelo-video", default="omni-flash")
    p_prod.add_argument("--musica", default=None)
    p_prod.add_argument("--out", default="output")

    p_render = sub.add_parser(
        "render", help="Genera UN clip desde un prompt + fotograma de avatar (solo motor, sin LLM)")
    p_render.add_argument("--prompt", required=True, help="Prompt de vídeo")
    p_render.add_argument("--avatar-frame", default=None, help="Fotograma inicial (imagen->vídeo)")
    p_render.add_argument("--ruta", default="google", choices=["apimart", "kie", "higgsfield", "google"])
    p_render.add_argument("--modelo-video", default="veo-3.1-fast-generate-preview")
    p_render.add_argument("--duracion", type=int, default=8)
    p_render.add_argument("--aspect", default="9:16")
    p_render.add_argument("--salida", default="output/clip.mp4")

    p_voz = sub.add_parser("voz", help="Genera audio con tu voz clonada (ElevenLabs)")
    p_voz.add_argument("--texto", required=True, help="Texto a locutar")
    p_voz.add_argument("--voice-id", default=None, help="ID de tu voz clonada (o ELEVENLABS_VOICE_ID)")
    p_voz.add_argument("--salida", default="output/voz.mp3")

    p_dob = sub.add_parser("doblar", help="Pone tu voz sobre un vídeo (reemplaza el audio)")
    p_dob.add_argument("--video", required=True)
    p_dob.add_argument("--audio", required=True, help="Tu voz (mp3/wav)")
    p_dob.add_argument("--salida", default=None, help="por defecto *_voz.mp4")

    p_real = sub.add_parser(
        "realismo", help="Aplica la capa de realismo del curso a un clip (solo ffmpeg)")
    p_real.add_argument("--clip", required=True, help="Vídeo de entrada")
    p_real.add_argument("--salida", default=None, help="Vídeo de salida (por defecto *_real.mp4)")
    p_real.add_argument("--estilo", default="ugc", choices=["ugc", "cine"],
                        help="ugc = selfie crudo del curso · cine = estética de anuncio")
    p_real.add_argument("--sin-grano", action="store_true", help="No añadir grano/partículas")

    a = parser.parse_args(argv)
    if a.cmd == "voz":
        import os
        from .engines.elevenlabs import ElevenLabsVoice
        os.makedirs(os.path.dirname(a.salida) or ".", exist_ok=True)
        try:
            asset = ElevenLabsVoice().generar_voz(a.texto, a.salida, a.voice_id)
        except RuntimeError as e:
            print(f"No se pudo generar la voz: {e}", file=sys.stderr)
            return 2
        print(f"Voz generada: {asset.path}")
        return 0
    if a.cmd == "doblar":
        import os
        from .assembly.compositor import poner_voz
        salida = a.salida or os.path.splitext(a.video)[0] + "_voz.mp4"
        try:
            out = poner_voz(a.video, a.audio, salida)
        except (RuntimeError, FileNotFoundError) as e:
            print(f"No se pudo doblar: {e}", file=sys.stderr)
            return 2
        print(f"Vídeo con tu voz: {out}")
        return 0
    if a.cmd == "realismo":
        import os
        from .assembly.compositor import aplicar_realismo
        salida = a.salida or os.path.splitext(a.clip)[0] + "_real.mp4"
        try:
            out = aplicar_realismo(a.clip, salida, grano=not a.sin_grano, estilo=a.estilo)
        except (RuntimeError, FileNotFoundError) as e:
            print(f"No se pudo aplicar el realismo: {e}", file=sys.stderr)
            return 2
        print(f"Clip con capa de realismo: {out}")
        return 0
    if a.cmd == "render":
        import os
        from .config import build_engines
        from .brain.realism import NEGATIVE_PROMPT
        from .models import Acento, Formato, ShotPrompt
        os.makedirs(os.path.dirname(a.salida) or ".", exist_ok=True)
        shot = ShotPrompt(
            formato=Formato.UGC, prompt=a.prompt, script_line="", acento=Acento.ESPANA,
            duracion_s=a.duracion, aspect_ratio=a.aspect,
            primer_frame=a.avatar_frame, negative_prompt=NEGATIVE_PROMPT,
        )
        cfg = EngineConfig(ruta=a.ruta, modelo_video=a.modelo_video)
        try:
            _img, video_engine = build_engines(cfg)
            asset = video_engine.generar_video(shot, a.salida)
        except (RuntimeError, FileNotFoundError) as e:
            print(f"No se pudo renderizar: {e}", file=sys.stderr)
            return 2
        print(f"Clip generado: {asset.path}  (coste ~{asset.coste_estimado:.2f} €)")
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
