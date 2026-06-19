# AGENTS.md — Puerta de entrada para una IA

> **Para la IA que lee esto:** este directorio es el **archivo completo del curso de
> automatización e IA "Imperio Digital"** (Skool): 30 cursos, 826 lecciones, con notas y
> transcripciones, más recursos ejecutables (skills, plantillas n8n/Make, prompts).
> Tu objetivo es **aprender la metodología y poder ejecutarla**. Lee esta guía entera
> antes de actuar. El corpus completo son **~3,9M tokens** — NO intentes cargarlo todo;
> usa las capas de abajo.

## Cómo está organizado (3 capas)

### 1️⃣ Capa CURADA — empieza por aquí (cabe en contexto, ~pocos miles de tokens)
Léela primero, en este orden. Con esto **aprendes el curso** sin ver las 245 h de vídeo:
1. [`RESUMEN-MAESTRO.md`](RESUMEN-MAESTRO.md) — el curso entero destilado: filosofía,
   mapa de los 30 cursos, frameworks y rutas.
2. [`INDICE-POR-CATEGORIA.md`](INDICE-POR-CATEGORIA.md) — 10 categorías: **qué te enseña
   cada una → resultado al aplicarla**.
3. [`categorias/`](categorias/) — fichas ampliadas por tema (p. ej.
   [`sistemas-agenticos.md`](categorias/sistemas-agenticos.md)).

### 2️⃣ Capa REFERENCIA PROFUNDA — consulta bajo demanda (NO la cargues entera)
- [`INDICE.md`](INDICE.md) — índice clicable de las 826 lecciones.
- [`estructura.json`](estructura.json) — árbol completo legible por máquina (ids,
  títulos, vídeos, rutas de fichero). **Úsalo para localizar** la lección exacta.
- `NN-<curso>/NNN-<leccion>.md` — cada lección: título, vídeo, recursos, **notas** y
  **transcripción**. Abre solo las que necesites para una tarea concreta.

### 3️⃣ Capa EJECUTABLE — los activos para *hacer*, no solo leer
En [`recursos/`](recursos/) (ver [`recursos/INDICE-RECURSOS.md`](recursos/INDICE-RECURSOS.md)):
- **Skills de Claude Code** (`.tar.gz`/`.zip`) — p. ej.
  [`recursos/ads-cabrones-ia/`](recursos/ads-cabrones-ia/) (generador de anuncios
  cinematográficos). Instalar: descomprimir el `.tar.gz` en `~/.claude/skills/`.
- **Motor Agéntico** (instaladores Mac/Windows) en `recursos/02-claude-code/`.
- **Plantillas n8n / Make** (`.json`) — importar en n8n/Make.
- **Bases Airtable, PDFs, bundles.**

## Cómo EJECUTAR (no solo aprender)
- **Para construir/automatizar:** identifica el objetivo → busca la categoría en
  `INDICE-POR-CATEGORIA.md` → abre las lecciones de ese curso → si hay un recurso
  asociado (skill/plantilla), úsalo.
- **Skills:** `tar -xzf <skill>.tar.gz -C ~/.claude/skills/`, reinicia el agente, invócalo.
- **Plantillas n8n/Make:** importar el `.json`; **conectar TUS credenciales**.
- **Biblioteca de Prompts:** las 178 lecciones del curso 17 son prompts listos (texto en
  las notas) — cópialos y adáptalos.

## ⚠️ Avisos
- **Claves redactadas:** algunas plantillas traían credenciales reales del creador
  (Replicate, webhooks de Make) → se sustituyeron por placeholders
  (`r8_REDACTED_API_TOKEN`, etc.). **Pon tus propias API keys** al usar una plantilla.
- **Idioma:** todo está en español; el usuario responde en español.
- **Uso:** material de un curso de pago archivado para uso personal del miembro. No
  redistribuir.

## Estrategia de contexto (importante para una IA)
- ¿Chat con límite de contexto? Carga **solo la capa 1** para aprender, y pega lecciones
  puntuales de la capa 2 cuando hagan falta.
- ¿Agente con acceso a ficheros (Claude Code, etc.)? Lee la capa 1, luego **abre ficheros
  bajo demanda** vía `estructura.json` / `INDICE.md`. No cargues los 826 `.md` de golpe.
