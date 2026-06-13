"""Servicio web del pipeline AvatarHype — para correr TODO en la nube (botón único).

Expone el pipeline por HTTP + una página con formulario, para que Alexander genere
desde el navegador sin terminal ni código. Se despliega en cualquier host de
contenedores (Render, etc.). Las API keys se cargan como variables de entorno EN EL
HOST (su panel), no aquí.

Endpoints:
    GET  /            → formulario web (el "botón": pegás prompt + avatar → vídeo)
    POST /render      → genera UN clip (solo motor, sin LLM) y lo muestra/descarga
    GET  /salud       → estado + qué keys hay (sin revelarlas)
    POST /producir    → tema/producto → anuncio completo (necesita key LLM)
    POST /voz         → texto → audio con tu voz clonada
"""
from __future__ import annotations

import os
import uuid
from typing import Optional

try:
    from fastapi import FastAPI, Form, HTTPException
    from fastapi.responses import HTMLResponse
    from fastapi.staticfiles import StaticFiles
    from pydantic import BaseModel
except ImportError as e:  # pragma: no cover
    raise SystemExit("Falta el servicio: pip install -r requirements-service.txt") from e

from .config import EngineConfig
from .models import Acento, Formato, ProductBrief

app = FastAPI(title="AvatarHype", version="1.1")

OUT_DIR = "output"
os.makedirs(OUT_DIR, exist_ok=True)
app.mount("/files", StaticFiles(directory=OUT_DIR), name="files")

# Prompt de ejemplo (clip 1 del anuncio "estado de resultados", argentino) precargado.
PROMPT_EJEMPLO = (
    "A hyper-realistic 9:16 handheld iPhone front-camera selfie video. "
    "[CHARACTER] the exact same person from the provided reference image. Identity, face, "
    "skin texture, hair and outfit must match perfectly. "
    "[ACTION] speaking to the camera, medium shot, head and shoulders. "
    "[LANGUAGE] authentic Argentinian Rioplatense Spanish (voseo, porteño intonation). "
    "[SCRIPT] \"¿Tenés un negocio y mirás solo la plata que hay en la cuenta? Ese es el error más común.\" "
    "[CAMERA] slow gentle zoom in. [LIGHTING] natural daylight, soft shadows. "
    "[AUDIO] raw iPhone microphone, no music."
)


def _keys_presentes() -> dict:
    return {k: bool(os.environ.get(k)) for k in (
        "ANTHROPIC_API_KEY", "OPENAI_API_KEY", "APIMART_API_KEY",
        "GEMINI_API_KEY", "ELEVENLABS_API_KEY", "ELEVENLABS_VOICE_ID",
    )}


@app.get("/salud")
def salud():
    from .assembly.compositor import ffmpeg_disponible
    return {"ok": True, "ffmpeg": ffmpeg_disponible(), "keys": _keys_presentes()}


@app.get("/", response_class=HTMLResponse)
def home():
    return f"""
<!doctype html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AvatarHype · Generar</title>
<style>
 body{{font-family:system-ui,sans-serif;max-width:760px;margin:40px auto;padding:0 16px;color:#1a1a1a}}
 h1{{font-size:22px}} label{{font-weight:600;display:block;margin:16px 0 6px}}
 textarea,input,select{{width:100%;padding:10px;font-size:14px;border:1px solid #ccc;border-radius:8px;box-sizing:border-box}}
 textarea{{height:170px}} button{{margin-top:18px;padding:12px 22px;font-size:16px;border:0;border-radius:8px;background:#111;color:#fff;cursor:pointer}}
 small{{color:#666}}
</style></head><body>
<h1>🎬 Generar clip con tu avatar</h1>
<p><small>Pegá el prompt y la URL pública de tu fotograma de avatar. Genera 1 clip por APImart.</small></p>
<form method="post" action="/render">
  <label>Prompt del vídeo</label>
  <textarea name="prompt">{PROMPT_EJEMPLO}</textarea>
  <label>URL pública de tu fotograma de avatar <small>(opcional; sin ella es persona genérica)</small></label>
  <input name="avatar_frame_url" placeholder="https://...tu_avatar.png">
  <label>Modelo <small>(si uno está saturado, probá otro)</small></label>
  <select name="modelo_video">
    <option value="veo-3.1-fast">Veo 3.1 Fast (recomendado, estable)</option>
    <option value="omni-flash">Omni Flash</option>
    <option value="veo-3.1">Veo 3.1 Quality</option>
    <option value="sora-2">Sora 2</option>
  </select>
  <button type="submit">Generar clip</button>
</form>
<p><small>Free se "duerme": la primera vez puede tardar. La generación toma ~1-2 min.</small></p>
</body></html>"""


@app.post("/render", response_class=HTMLResponse)
def render(prompt: str = Form(...), avatar_frame_url: str = Form(""),
           ruta: str = Form("apimart"), modelo_video: str = Form("omni-flash")):
    from .brain.realism import NEGATIVE_PROMPT
    from .config import build_engines
    from .models import ShotPrompt

    name = f"clip_{uuid.uuid4().hex[:8]}.mp4"
    out = os.path.join(OUT_DIR, name)
    shot = ShotPrompt(
        formato=Formato.UGC, prompt=prompt, script_line="", acento=Acento.ARGENTINA,
        primer_frame=(avatar_frame_url.strip() or None), negative_prompt=NEGATIVE_PROMPT,
    )
    cfg = EngineConfig(ruta=ruta, modelo_video=modelo_video)
    try:
        _img, video_engine = build_engines(cfg)
        asset = video_engine.generar_video(shot, out)
    except Exception as e:  # noqa: BLE001
        return HTMLResponse(
            f"<p>❌ Error: {e}</p><p><a href='/'>← Volver</a></p>", status_code=400)
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<style>body{{font-family:system-ui;max-width:760px;margin:40px auto;padding:0 16px}}
video{{width:100%;border-radius:10px}}</style></head><body>
<h1>✅ Clip generado</h1>
<video controls src="/files/{name}"></video>
<p>Coste estimado: ~{asset.coste_estimado:.3f} €</p>
<p><a href="/files/{name}" download>⬇ Descargar</a> &nbsp;·&nbsp; <a href="/">← Generar otro</a></p>
</body></html>"""


class ProducirIn(BaseModel):
    nombre: str
    descripcion: str
    mercado: str = "Argentina"
    acento: str = "es-AR"
    formatos: list[str] = ["ugc"]
    avatar_frame_url: Optional[str] = None
    ruta: str = "apimart"
    modelo_video: str = "omni-flash"


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
    except Exception as e:  # noqa: BLE001
        raise HTTPException(status_code=400, detail=str(e))
    return {"anuncios": [{"formato": a.formato.value, "path": a.path,
                          "coste": round(a.coste_total, 3), "clips": len(a.clips)}
                         for a in r.anuncios]}


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
