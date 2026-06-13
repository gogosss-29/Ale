# avatarhype — Pipeline de anuncios UGC con IA (automatización del sistema)

Implementación en Python del sistema AvatarHype documentado en
[`../docs/SISTEMA-AVATARHYPE.md`](../docs/SISTEMA-AVATARHYPE.md). Convierte el proceso
manual del curso (Pinterest → ChatGPT → APImart → CapCut) en un pipeline ejecutable.

## Flujo

```
ProductBrief ─▶ [1] estrategia ─▶ [2] guiones ─▶ [3] prompts (método 6C)
            ─▶ [4] imágenes ─▶ [5] clips de vídeo ─▶ [6] ensamblado (realismo) ─▶ Anuncio
```

### Avatar = TÚ (paso de identidad)

El curso genera avatares genéricos. Para que el avatar seas **tú**, pasa una foto de
tu cara como `avatar_referencia_path` (CLI: `--avatar-referencia`). El paso [4] genera
entonces una **imagen-ancla** tuya (GPT Image 2 con tu cara de referencia) que se usa
como primer frame de cada clip, manteniendo tu identidad. Esto sustituye la captura de
Pinterest del curso por tu propia cara; el resto del método (ángulo, guion, capa de
realismo) es idéntico.

```bash
# Solo el paso de identidad (1 imagen, ~0,012 €) — para ver qué tal funciona:
python -m avatarhype.cli avatar \
  --nombre "Alexander" --descripcion "avatar personal" \
  --avatar-referencia /ruta/a/tu_foto.jpg
```

- **Pasos 1-3 (cerebro):** `brain/` — réplica de los agentes GPT del curso (estrategia +
  guiones) + el constructor determinista de prompts de 14 bloques. Necesita una API de LLM.
- **Pasos 4-5 (motores):** `engines/` — proveedores intercambiables Google (Veo/Gemini) /
  APImart / Kie / Higgsfield. Necesitan las API keys de cada servicio.
  - **`google`** (ruta de Alexander): Veo por la API oficial de Google (`google-genai`).
    Omni Flash de AI Studio == `veo-3.1-...` por API. Imagen→vídeo con tu avatar como frame
    inicial; genera audio/voz nativo. Más caro por clip que APImart, pero usa tu mismo modelo.
    Key: `GEMINI_API_KEY`.
- **Paso 6 (ensamblado):** `assembly/` — une clips con ffmpeg y aplica la **capa de realismo
  exacta del curso** (valores de CapCut traducidos a filtros ffmpeg). No necesita keys.

## Estructura

| Módulo | Qué hace |
|---|---|
| `models.py` | Dataclasses del contrato (ProductBrief, Estrategia, Guion, ShotPrompt, Asset, Anuncio) |
| `brain/realism.py` | Constantes literales del curso (negative prompt, acentos, microacciones, valores CapCut) |
| `brain/prompt_builder.py` | Ensambla el prompt de vídeo (método 6C, 14 bloques) — **determinista, testeado** |
| `brain/llm.py` | Cliente LLM agnóstico (Anthropic / OpenAI) |
| `brain/strategy.py` | Análisis estratégico + generación de guiones |
| `engines/base.py` | Interfaces ImageEngine / VideoEngine / AudioEngine |
| `engines/google.py` | Conector Google: Veo (vídeo) + Gemini Image (Nano Banana) |
| `engines/elevenlabs.py` | TU voz clonada (TTS) para doblar los anuncios con tu voz real |
| `engines/apimart.py`, `kie.py`, `higgsfield.py` | Conectores de los motores |
| `engines/costs.py` | Tabla de costes por ruta (para comparar) |
| `assembly/realism_grade.py` | Traduce la capa de realismo de CapCut a ffmpeg — **testeado** |
| `assembly/compositor.py` | Concatena clips + realismo + música — **testeado con ffmpeg** |
| `pipeline.py` | Orquestador end-to-end |
| `cli.py` | Línea de comandos |

## Uso

```bash
pip install -r ../requirements.txt
cp ../.env.example ../.env   # y rellena las keys

# Solo planificar (estrategia + guiones + prompts). Gasta LLM, no créditos de vídeo:
python -m avatarhype.cli plan \
  --nombre "Sérum niacinamida" \
  --descripcion "Sérum para el acné y las manchas" \
  --mercado España --formatos ugc,podcast

# Pipeline completo por la ruta GOOGLE (Veo), usando un fotograma de tu avatar
# como frame inicial (imagen->vídeo). Requiere GEMINI_API_KEY:
python -m avatarhype.cli producir \
  --nombre "Sérum niacinamida" --descripcion "..." \
  --ruta google --avatar-frame avatar.png --musica pista.mp3
```

# TU voz (ElevenLabs) y doblaje sobre el vídeo:
python -m avatarhype.cli voz --texto "tu guion" --voice-id <tu_voz> --salida voz.mp3
python -m avatarhype.cli doblar --video clip.mp4 --audio voz.mp3 --salida clip_voz.mp4
```

> **Lip-sync:** `doblar` monta tu voz pero NO re-sincroniza los labios. Para que la boca
> cuadre con tu voz nueva hace falta un modelo de lip-sync dedicado (Higgsfield audio→vídeo,
> sync.so, etc.) — pendiente de enchufar como motor. Alternativa: generar el vídeo
> directamente audio→vídeo con un modelo talking-avatar a partir de tu voz.

```bash
Comparar rutas: cambia `--ruta google|apimart|kie|higgsfield`. Cada `Asset` reporta su
coste estimado y el anuncio suma el total, para comparar coste/calidad entre motores.
La ruta `google` es la de Alexander (Veo/Omni Flash oficial); `apimart` es la económica
para volumen.

## Estado

- ✅ **Cerebro determinista** (constructor de prompts 6C) — implementado y testeado.
- ✅ **Ensamblado + capa de realismo** (ffmpeg) — implementado y testeado con vídeo real.
- 🔌 **Estrategia/guiones (LLM)** — implementado; requiere `ANTHROPIC_API_KEY` u `OPENAI_API_KEY`.
- 🔌 **Motores (APImart/Kie/Higgsfield)** — conectores listos; requieren API keys. Los paths
  exactos de cada API se confirman contra su documentación al enchufar las credenciales.

## Tests

```bash
python tests/test_prompt_builder.py    # estructura de prompts (sin red)
python tests/test_realism_grade.py     # filtro de realismo + ensamblado ffmpeg real
```
