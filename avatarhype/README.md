# avatarhype — Pipeline de anuncios UGC con IA (automatización del sistema)

Implementación en Python del sistema AvatarHype documentado en
[`../docs/SISTEMA-AVATARHYPE.md`](../docs/SISTEMA-AVATARHYPE.md). Convierte el proceso
manual del curso (Pinterest → ChatGPT → APImart → CapCut) en un pipeline ejecutable.

## Flujo

```
ProductBrief ─▶ [1] estrategia ─▶ [2] guiones ─▶ [3] prompts (método 6C)
            ─▶ [4] imágenes ─▶ [5] clips de vídeo ─▶ [6] ensamblado (realismo) ─▶ Anuncio
```

- **Pasos 1-3 (cerebro):** `brain/` — réplica de los agentes GPT del curso (estrategia +
  guiones) + el constructor determinista de prompts de 14 bloques. Necesita una API de LLM.
- **Pasos 4-5 (motores):** `engines/` — proveedores intercambiables APImart / Kie / Higgsfield
  (patrón submit→poll→download). Necesitan las API keys de cada servicio.
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

# Pipeline completo (requiere keys de motor):
python -m avatarhype.cli producir \
  --nombre "Sérum niacinamida" --descripcion "..." \
  --ruta apimart --modelo-video omni-flash --musica pista.mp3
```

Comparar rutas: cambia `--ruta apimart|kie|higgsfield`. Cada `Asset` reporta su coste
estimado y el anuncio suma el total, para comparar coste/calidad entre motores.

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
