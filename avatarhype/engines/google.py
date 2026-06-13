"""Motor Google (Gemini API): Veo para vídeo, Gemini 2.5 Flash Image (Nano Banana) para imagen.

Esta es la ruta de Alexander: genera con Omni Flash / Veo en Google AI Studio, así que
automatizamos el render con la **API oficial de Google** (no hace falta APImart).

Usa el SDK `google-genai` (pip install google-genai). Lee la key del entorno:
    GEMINI_API_KEY  (o GOOGLE_API_KEY)

NOTA DE COSTE: la API oficial de Google es bastante más cara por clip que la ruta
revendida del curso (APImart). Veo 3.1 ~ varios € / 8 s con audio; Veo 3.1 Fast es más
barato. Para volumen, APImart sigue siendo la ruta económica. Ver engines/costs.py.

Referencia: https://ai.google.dev/gemini-api/docs/video
"""
from __future__ import annotations

import mimetypes
import os
import time

from ..models import Asset, ShotPrompt
from .base import ImageEngine, VideoEngine
from .costs import coste_imagen, coste_video

# Omni Flash (AI Studio) == Veo 3.1 por API. Fast = más barato / rápido.
DEFAULT_VIDEO_MODEL = "veo-3.1-fast-generate-preview"
DEFAULT_IMAGE_MODEL = "gemini-2.5-flash-image"  # "Nano Banana"
POLL_SEGUNDOS = 10


def _client():
    """Crea el cliente de google-genai. Lee GEMINI_API_KEY / GOOGLE_API_KEY del entorno."""
    if not (os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")):
        raise RuntimeError("Falta GEMINI_API_KEY (o GOOGLE_API_KEY) en el entorno")
    try:
        from google import genai  # import perezoso: el resto del pipeline no depende del SDK
    except ImportError as e:
        raise RuntimeError("Falta el SDK: pip install google-genai") from e
    return genai.Client()


def _load_image(path: str):
    """Carga una imagen local como types.Image del SDK (para imagen->vídeo)."""
    from google.genai import types
    with open(path, "rb") as f:
        data = f.read()
    mime = mimetypes.guess_type(path)[0] or "image/jpeg"
    return types.Image(image_bytes=data, mime_type=mime)


class GoogleVeoVideo(VideoEngine):
    """Genera vídeo con Veo. Si el shot trae primer_frame (tu avatar), hace imagen->vídeo
    para mantener tu identidad. Veo genera el audio/voz de forma nativa a partir del guion."""

    name = "google"

    def __init__(self, modelo: str = DEFAULT_VIDEO_MODEL, resolucion: str = "720p"):
        self.modelo = modelo
        self.resolucion = resolucion

    def generar_video(self, shot: ShotPrompt, out_path: str) -> Asset:
        client = _client()                       # valida key + SDK con mensaje limpio
        from google.genai import types

        config = types.GenerateVideosConfig(
            aspect_ratio=shot.aspect_ratio,          # "9:16" | "16:9"
            resolution=self.resolucion,              # "720p" | "1080p"
            number_of_videos=1,
        )
        if shot.negative_prompt:
            config.negative_prompt = shot.negative_prompt

        kwargs = {"model": self.modelo, "prompt": shot.prompt, "config": config}
        if shot.primer_frame:
            kwargs["image"] = _load_image(shot.primer_frame)   # imagen->vídeo (tu avatar)
        if shot.ultimo_frame:
            config.last_frame = _load_image(shot.ultimo_frame)

        op = client.models.generate_videos(**kwargs)
        while not op.done:
            time.sleep(POLL_SEGUNDOS)
            op = client.operations.get(op)

        video = op.response.generated_videos[0]
        client.files.download(file=video.video)
        video.video.save(out_path)

        modelo_key = "video_veo31fast_8s" if "fast" in self.modelo else "video_veo31_8s"
        return Asset(tipo="video", path=out_path, engine=self.name,
                     coste_estimado=coste_video("google", modelo_key),
                     meta={"modelo": self.modelo, "resolucion": self.resolucion})


class GoogleGeminiImage(ImageEngine):
    """Genera imagen con Gemini 2.5 Flash Image (Nano Banana). Acepta imágenes de
    referencia (tu cara) para mantener identidad."""

    name = "google"

    def __init__(self, modelo: str = DEFAULT_IMAGE_MODEL):
        self.modelo = modelo

    def generar_imagen(self, prompt, out_path, referencias=None, aspect_ratio="9:16", resolucion="2K") -> Asset:
        client = _client()
        contents: list = [prompt]
        for ref in (referencias or []):
            contents.append(_load_image(ref))  # las referencias guían la identidad

        resp = client.models.generate_content(model=self.modelo, contents=contents)
        # extraer los bytes de imagen de la primera parte inline
        for part in resp.candidates[0].content.parts:
            inline = getattr(part, "inline_data", None)
            if inline and inline.data:
                with open(out_path, "wb") as f:
                    f.write(inline.data)
                break
        else:
            raise RuntimeError("La respuesta de Gemini no devolvió imagen")

        return Asset(tipo="image", path=out_path, engine=self.name,
                     coste_estimado=coste_imagen("google", "image_nano_banana"),
                     meta={"modelo": self.modelo})
