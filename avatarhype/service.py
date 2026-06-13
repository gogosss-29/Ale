"""Servicio web del pipeline AvatarHype — para correr TODO en la nube (botón único).

Expone el pipeline por HTTP para que un orquestador (n8n) o un formulario lo dispare.
Se despliega en cualquier host de contenedores (Render, Railway, Fly, Cloud Run, VPS).
Las API keys se cargan como variables de entorno EN EL HOST (su panel), no aquí.

Arranque local (para probar):
    pip install -r requirements.txt -r requirements-service.txt
    uvicorn avatarhype.service:app --host 0.0.0.0 --port 8000

Endpoints:
    GET  /salud           → estado + qué keys están presentes (sin revelarlas)
    POST /producir        → tema/producto → anuncio (guion→frame→vídeo→voz→grade)
    POST /voz             → texto → audio con tu voz clonada
"""
from __future__ import annotations

import os
from typing import Optional

try:
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
except ImportError as e:  # pragma: no cover
    raise SystemExit("Falta el servicio: pip install -r requirements-service.txt") from e

from .config import EngineConfig
from .models import Acento, Formato, ProductBrief

app = FastAPI(title="AvatarHype", version="1.0")


def _keys_presentes() -> dict:
    """Reporta qué keys hay (True/False), sin revelar valores."""
    return {k: bool(os.environ.get(k)) for k in (
        "ANTHROPIC_API_KEY", "OPENAI_API_KEY", "APIMART_API_KEY",
        "GEMINI_API_KEY", "ELEVENLABS_API_KEY", "ELEVENLABS_VOICE_ID",
    )}


@app.get("/salud")
def salud():
    from .assembly.compositor import ffmpeg_disponible
    return {"ok": True, "ffmpeg": ffmpeg_disponible(), "keys": _keys_presentes()}


class ProducirIn(BaseModel):
    nombre: str
    descripcion: str
    mercado: str = "Argentina"
    acento: str = "es-AR"
    formatos: list[str] = ["ugc"]
    avatar_frame_url: Optional[str] = None   # URL pública del frame del avatar
    ruta: str = "apimart"
    modelo_video: str = "omni-flash"
    voice_id: Optional[str] = None           # tu voz clonada (ElevenLabs)
    musica_url: Optional[str] = None


@app.post("/producir")
def producir_endpoint(inp: ProducirIn):
    from .pipeline import producir
    brief = ProductBrief(
        nombre=inp.nombre, descripcion=inp.descripcion, mercado=inp.mercado,
        acento=Acento(inp.acento), formatos=[Formato(f) for f in inp.formatos],
        avatar_frame_path=inp.avatar_frame_url,
    )
    cfg = EngineConfig(ruta=inp.ruta, modelo_video=inp.modelo_video)
    try:
        r = producir(brief, cfg=cfg)
    except Exception as e:  # noqa: BLE001 — devolver el error al orquestador
        raise HTTPException(status_code=400, detail=str(e))
    return {
        "anuncios": [{"formato": a.formato.value, "path": a.path,
                      "coste": round(a.coste_total, 3), "clips": len(a.clips)}
                     for a in r.anuncios],
        "guiones": [{"formato": g.formato.value, "texto": g.texto} for g in r.guiones],
    }


class VozIn(BaseModel):
    texto: str
    voice_id: Optional[str] = None
    salida: str = "output/voz.mp3"


@app.post("/voz")
def voz_endpoint(inp: VozIn):
    from .engines.elevenlabs import ElevenLabsVoice
    os.makedirs(os.path.dirname(inp.salida) or ".", exist_ok=True)
    try:
        asset = ElevenLabsVoice().generar_voz(inp.texto, inp.salida, inp.voice_id)
    except Exception as e:  # noqa: BLE001
        raise HTTPException(status_code=400, detail=str(e))
    return {"path": asset.path}
