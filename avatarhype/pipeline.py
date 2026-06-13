"""Orquestador end-to-end del sistema AvatarHype.

Flujo: ProductBrief -> estrategia -> guiones -> prompts (método 6C) -> imágenes ->
clips de vídeo -> ensamblado con capa de realismo -> Anuncio.

Cada paso es sustituible. La generación real necesita API keys (ver .env.example);
los pasos 1-3 (cerebro) y 6 (ensamblado) son los que más valor aportan y se pueden
ejecutar/validar de forma independiente.
"""
from __future__ import annotations

import os
from dataclasses import dataclass

from .brain import strategy
from .brain.prompt_builder import ShotSpec, build_prompt
from .config import EngineConfig, build_engines
from .models import Anuncio, Asset, Formato, ProductBrief, ShotPrompt


@dataclass
class PipelineResult:
    brief: ProductBrief
    estrategia: object
    guiones: list
    shots: list[ShotPrompt]
    anuncios: list[Anuncio]
    avatar_path: str | None = None  # imagen-ancla de identidad del avatar


# Prompt del paso de IDENTIDAD: convierte la foto de referencia del usuario en la
# imagen-ancla del avatar. Es el equivalente del curso (generar el avatar con GPT
# Image 2 / Nano Banana Pro) pero usando SU cara como referencia, no una de Pinterest.
_AVATAR_IDENTIDAD_PROMPT = (
    "A hyper-realistic vertical portrait of the exact same person from the reference "
    "image. Keep the same face, skin texture, hair and overall look. Natural casual "
    "appearance, relaxed neutral expression, looking straight at the camera, soft "
    "natural indoor lighting, plain uncluttered background. Photorealistic, candid, "
    "not retouched, not AI-generated, no beauty filter."
)


def generar_avatar_identidad(brief: ProductBrief, image_engine, out_dir: str,
                             aspect_ratio: str = "9:16") -> str | None:
    """Paso de IDENTIDAD: genera la imagen-ancla del avatar a partir de la foto de la
    cara del usuario. Esta imagen se usa luego como primer frame de los clips para que
    el avatar mantenga SU identidad. Devuelve el path de la imagen, o None si no hay
    foto de referencia. Cuesta 1 imagen (~0,012 € en GPT Image 2)."""
    if not brief.avatar_referencia_path:
        return None
    out = os.path.join(out_dir, "avatar_identidad.png")
    asset = image_engine.generar_imagen(
        _AVATAR_IDENTIDAD_PROMPT, out,
        referencias=[brief.avatar_referencia_path],
        aspect_ratio=aspect_ratio,
    )
    return asset.path


def _shots_desde_guion(brief: ProductBrief, guion) -> list[ShotPrompt]:
    """Trocea un guion en prompts de plano, uno por línea (~8 s cada uno)."""
    lineas = guion.lineas or [guion.texto]
    shots = []
    for ln in lineas:
        spec = ShotSpec(
            formato=guion.formato,
            script_line=ln,
            acento=brief.acento,
            forzar_muletilla=True,  # refuerza el acento (España, Argentina, México…) si lo tiene
        )
        shots.append(build_prompt(spec))
    return shots


def planificar(brief: ProductBrief) -> PipelineResult:
    """Pasos 1-3: estrategia + guiones + prompts. NO genera media (no gasta créditos)."""
    estrategia = strategy.analizar_producto(brief)
    guiones = strategy.generar_guiones(brief, estrategia)
    shots: list[ShotPrompt] = []
    for g in guiones:
        shots.extend(_shots_desde_guion(brief, g))
    return PipelineResult(brief, estrategia, guiones, shots, anuncios=[])


def producir(brief: ProductBrief, cfg: EngineConfig | None = None,
             musica: str | None = None) -> PipelineResult:
    """Pipeline completo: planifica + genera clips + ensambla los anuncios."""
    from .assembly.compositor import ensamblar

    cfg = cfg or EngineConfig.from_env()
    os.makedirs(cfg.out_dir, exist_ok=True)
    plan = planificar(brief)
    img_engine, video_engine = build_engines(cfg)

    # Paso de IDENTIDAD: o bien usamos un fotograma de avatar YA hecho tal cual
    # (avatar_frame_path), o lo GENERAMOS desde una foto de la cara (avatar_referencia_path).
    # Ese frame se usa como primer frame de cada clip (imagen->vídeo) para fijar la identidad.
    if brief.avatar_frame_path:
        avatar_path = brief.avatar_frame_path
    else:
        avatar_path = generar_avatar_identidad(brief, img_engine, cfg.out_dir)
    plan.avatar_path = avatar_path
    if avatar_path:
        for s in plan.shots:
            if not s.primer_frame:
                s.primer_frame = avatar_path

    # agrupar shots por formato para montar un anuncio por formato
    por_formato: dict[Formato, list[ShotPrompt]] = {}
    for s in plan.shots:
        por_formato.setdefault(s.formato, []).append(s)

    anuncios: list[Anuncio] = []
    for formato, shots in por_formato.items():
        clips: list[Asset] = []
        for i, shot in enumerate(shots):
            out = os.path.join(cfg.out_dir, f"{formato.value}_clip_{i:03d}.mp4")
            clips.append(video_engine.generar_video(shot, out))
        salida = os.path.join(cfg.out_dir, f"anuncio_{formato.value}.mp4")
        ensamblar([c.path for c in clips], salida, musica=musica)
        anuncios.append(Anuncio(
            formato=formato, path=salida, clips=clips,
            coste_total=sum(c.coste_estimado for c in clips),
        ))
    plan.anuncios = anuncios
    return plan
