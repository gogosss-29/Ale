"""Motor ElevenLabs: genera voz (TTS) con tu voz clonada.

Para poner TU voz real en los anuncios (en vez de la voz que genera el modelo de
vídeo). Tu voz clonada se crea una vez en ElevenLabs a partir de tus clips (ya tenés
material: el clip de 12 s y el completo de 3:27). Eso te da un `voice_id` reutilizable.

API (https://elevenlabs.io/docs):
  POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}?output_format=mp3_44100_128
  header: xi-api-key: <ELEVENLABS_API_KEY>
  body:   {text, model_id, voice_settings}
  resp:   bytes de audio (mp3)
"""
from __future__ import annotations

import os

from ..models import Asset
from .base import AudioEngine

DEFAULT_MODEL = "eleven_multilingual_v2"   # buen español/multilingüe
BASE = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"


class ElevenLabsVoice(AudioEngine):
    name = "elevenlabs"

    def __init__(self, modelo: str = DEFAULT_MODEL, output_format: str = "mp3_44100_128"):
        self.modelo = modelo
        self.output_format = output_format

    def generar_voz(self, texto: str, out_path: str, voice_id: str) -> Asset:
        key = os.environ.get("ELEVENLABS_API_KEY")
        if not key:
            raise RuntimeError("Falta ELEVENLABS_API_KEY en el entorno")
        voice_id = voice_id or os.environ.get("ELEVENLABS_VOICE_ID")
        if not voice_id:
            raise RuntimeError("Falta voice_id (tu voz clonada) o ELEVENLABS_VOICE_ID")

        import requests
        url = f"{BASE.format(voice_id=voice_id)}?output_format={self.output_format}"
        r = requests.post(
            url,
            headers={"xi-api-key": key, "Content-Type": "application/json",
                     "Accept": "audio/mpeg"},
            json={
                "text": texto,
                "model_id": self.modelo,
                "voice_settings": {"stability": 0.5, "similarity_boost": 0.8,
                                   "style": 0.0, "use_speaker_boost": True},
            },
            timeout=120,
        )
        r.raise_for_status()
        with open(out_path, "wb") as f:
            f.write(r.content)
        return Asset(tipo="audio", path=out_path, engine=self.name,
                     meta={"voice_id": voice_id, "modelo": self.modelo})
