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


def _shots_desde_guion(brief: ProductBrief, guion) -> list[ShotPrompt]:
    """Trocea un guion en prompts de plano, uno por línea (~8 s cada uno)."""
    lineas = guion.lineas or [guion.texto]
    shots = []
    for ln in lineas:
        spec = ShotSpec(
            formato=guion.formato,
            script_line=ln,
            acento=brief.acento,
            forzar_muletilla_espana=(brief.acento.value == "es-ES"),
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
    _img, video_engine = build_engines(cfg)

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
