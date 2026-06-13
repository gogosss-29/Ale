"""Modelos de datos del pipeline AvatarHype.

Definen el contrato entre las capas: brief de producto -> estrategia -> guiones ->
prompts de plano -> assets generados -> anuncio final.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Formato(str, Enum):
    """Los formatos de anuncio que enseña el curso."""

    UGC = "ugc"                  # un avatar hablando a cámara
    UGC_VOZ_OFF = "ugc_voz_off"  # voz en off + clips por encima
    PODCAST = "podcast"          # dos avatares, cámara estática
    DUALCAST = "dualcast"        # dos avatares interactuando a cámara
    TREND = "trend"              # recrear un trend viral (antes/después)
    IMAGEN = "imagen"            # image ad estático


class Acento(str, Enum):
    ESPANA = "es-ES"
    LATAM = "es-419"
    ARGENTINA = "es-AR"
    COLOMBIA = "es-CO"
    MEXICO = "es-MX"
    INGLES = "en-US"


@dataclass
class ProductBrief:
    """Entrada del pipeline: lo que el usuario describe."""

    nombre: str
    descripcion: str
    mercado: str = "España"
    acento: Acento = Acento.ESPANA
    formatos: list[Formato] = field(default_factory=lambda: [Formato.UGC])
    imagen_producto_path: Optional[str] = None  # foto del producto (referencia)
    avatar_referencia_path: Optional[str] = None  # foto de la CARA del usuario (se GENERA el avatar desde ella)
    avatar_frame_path: Optional[str] = None      # fotograma de un avatar YA hecho (se usa TAL CUAL como frame inicial)
    paleta_colores: Optional[str] = None         # para image ads
    notas: Optional[str] = None


@dataclass
class Estrategia:
    """Salida del análisis estratégico (el agente de scripts del curso)."""

    nicho: str
    avatar_objetivo: str          # descripción del público
    pain_points: list[str]
    angulos_venta: list[str]
    datos_estadisticos: list[str] = field(default_factory=list)


@dataclass
class Guion:
    """Un guion para un formato concreto."""

    formato: Formato
    texto: str                    # el guion completo
    lineas: list[str] = field(default_factory=list)  # frase a frase (para podcast/dualcast)


@dataclass
class ShotPrompt:
    """Prompt estructurado de un plano/clip, listo para el motor de vídeo."""

    formato: Formato
    prompt: str                   # prompt final ensamblado (método 6C, 14 bloques)
    script_line: str              # lo que dice el avatar en este clip
    acento: Acento
    duracion_s: int = 8
    aspect_ratio: str = "9:16"
    primer_frame: Optional[str] = None   # path imagen frame inicial
    ultimo_frame: Optional[str] = None   # path imagen frame final
    negative_prompt: str = ""


@dataclass
class Asset:
    """Un archivo generado (imagen o clip de vídeo)."""

    tipo: str                     # "image" | "video" | "audio"
    path: str
    engine: str                   # qué motor lo generó (apimart/kie/higgsfield)
    coste_estimado: float = 0.0   # en EUR, para comparar rutas
    meta: dict = field(default_factory=dict)


@dataclass
class Anuncio:
    """Resultado final: un anuncio montado."""

    formato: Formato
    path: str
    clips: list[Asset] = field(default_factory=list)
    coste_total: float = 0.0
