"""Interfaces comunes de los motores de generación.

Permiten enchufar varias rutas (APImart, Kie, Higgsfield) y compararlas por
coste/calidad sin cambiar el resto del pipeline.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from ..models import Asset, ShotPrompt


class ImageEngine(ABC):
    """Genera imágenes (avatares, productos, frames)."""

    name: str = "base"

    @abstractmethod
    def generar_imagen(
        self,
        prompt: str,
        out_path: str,
        referencias: Optional[list[str]] = None,
        aspect_ratio: str = "9:16",
        resolucion: str = "2K",
    ) -> Asset:
        ...


class VideoEngine(ABC):
    """Genera clips de vídeo a partir de un ShotPrompt."""

    name: str = "base"

    @abstractmethod
    def generar_video(self, shot: ShotPrompt, out_path: str) -> Asset:
        ...


class AudioEngine(ABC):
    """Genera voz en off (ElevenLabs)."""

    name: str = "base"

    @abstractmethod
    def generar_voz(self, texto: str, out_path: str, voice_id: str) -> Asset:
        ...
