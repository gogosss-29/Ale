"""Constructor de prompts de vídeo (método 6C / plantilla de 14 bloques).

Esta capa es DETERMINISTA: dadas las piezas (identidad, entorno, acción, guion,
acento, cámara...) ensambla el prompt final exactamente con la estructura que el
curso documenta como óptima. No necesita LLM.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from ..models import Acento, Formato, ShotPrompt
from . import realism


@dataclass
class ShotSpec:
    """Especificación de un plano antes de ensamblar el prompt."""

    formato: Formato
    script_line: str
    acento: Acento = Acento.ESPANA
    identidad: str = "the exact same person from the provided reference images"
    entorno: str = ""
    accion: str = "speaking naturally to camera"
    tono: str = "calm, confident, casual, not selling, not performing"
    camara: str = realism.CAMARA_HANDHELD
    movimiento_camara: Optional[str] = None     # clave de MOVIMIENTOS_CAMARA
    microaccion: Optional[str] = None           # clave de MICROACCIONES
    microaccion_antes: bool = True              # antes (True) o durante (False) el habla
    duracion_s: int = 8
    aspect_ratio: str = "9:16"
    primer_frame: Optional[str] = None
    ultimo_frame: Optional[str] = None
    forzar_muletilla_espana: bool = False


def _bloque_camara(spec: ShotSpec) -> str:
    if spec.movimiento_camara:
        mov = realism.MOVIMIENTOS_CAMARA.get(spec.movimiento_camara, spec.movimiento_camara)
        return mov
    return spec.camara


def _bloque_microaccion(spec: ShotSpec) -> str:
    if not spec.microaccion:
        return ""
    accion = realism.MICROACCIONES.get(spec.microaccion, spec.microaccion)
    if spec.microaccion_antes:
        return f"Before speaking, the person {accion}, then looks at the camera and speaks."
    return f"While speaking, the person {accion}."


def _script_final(spec: ShotSpec) -> str:
    line = spec.script_line.strip()
    if spec.forzar_muletilla_espana and spec.acento == Acento.ESPANA:
        # truco del curso: anteponer una muletilla muy de España (se corta en edición)
        line = f"{realism.MULETILLA_ESPANA.capitalize()}, {line[0].lower()}{line[1:]}"
    return line


def build_prompt(spec: ShotSpec) -> ShotPrompt:
    """Ensambla el prompt de vídeo final con la estructura de 14 bloques."""
    acento_txt = realism.ACENTO_BLOQUE[spec.acento]
    micro = _bloque_microaccion(spec)
    script = _script_final(spec)

    partes: list[str] = [
        f"A hyper-realistic {spec.aspect_ratio} handheld iPhone front-camera selfie video.",
        f"[CHARACTER] {spec.identidad}. Identity, face, skin texture, hair and outfit "
        f"must match perfectly at all times.",
        "[GOAL] Maximum realism. Must feel like a real casual UGC selfie, not AI-generated.",
    ]
    if spec.entorno:
        partes.append(f"[ENVIRONMENT] {spec.entorno}")
    partes.append(f"[ACTION] The subject is {spec.accion}.")
    partes.append(f"[HUMAN MOTION] {realism.FISICA_HUMANA}.")
    partes.append(f"[LANGUAGE] {acento_txt}")
    partes.append(f"[TONE] {spec.tono}.")
    if micro:
        partes.append(f"[MICRO-ACTION] {micro}")
    partes.append(f'[SCRIPT] "{script}"')
    partes.append(f"[BEHAVIOUR] {realism.COMPORTAMIENTO}.")
    partes.append(f"[CAMERA] {_bloque_camara(spec)}.")
    partes.append(f"[LIGHTING] {realism.LUZ}.")
    partes.append(f"[AUDIO] {realism.AUDIO}.")
    partes.append(f"[NEGATIVE PROMPT] {realism.NEGATIVE_PROMPT}.")

    if spec.primer_frame and spec.ultimo_frame:
        partes.append(
            "[START FRAME] Matches the first reference image. "
            "[END FRAME] Matches the second reference image."
        )

    prompt = "\n".join(partes)
    return ShotPrompt(
        formato=spec.formato,
        prompt=prompt,
        script_line=script,
        acento=spec.acento,
        duracion_s=spec.duracion_s,
        aspect_ratio=spec.aspect_ratio,
        primer_frame=spec.primer_frame,
        ultimo_frame=spec.ultimo_frame,
        negative_prompt=realism.NEGATIVE_PROMPT,
    )


def build_podcast_pair(line_izq: str, line_der: str, acento: Acento = Acento.ESPANA,
                       entorno: str = "podcast set with two people") -> list[ShotPrompt]:
    """Genera el par de prompts de un intercambio de podcast (cámara estática)."""
    izq = build_prompt(ShotSpec(
        formato=Formato.PODCAST, script_line=line_izq, acento=acento, entorno=entorno,
        camara=realism.CAMARA_ESTATICA, movimiento_camara="plano_fijo",
    ))
    der = build_prompt(ShotSpec(
        formato=Formato.PODCAST, script_line=line_der, acento=acento, entorno=entorno,
        camara=realism.CAMARA_ESTATICA, movimiento_camara="plano_fijo",
    ))
    return [izq, der]
