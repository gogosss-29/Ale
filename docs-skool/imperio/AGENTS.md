# AGENTS.md — Puerta de entrada para una IA

> **Para la IA que lee esto:** este directorio es el **archivo completo del curso de
> automatización e IA "Imperio Digital"** (Skool): 30 cursos, 826 lecciones, con notas y
> transcripciones, más recursos ejecutables (skills, plantillas n8n/Make, prompts).
> Tu objetivo es **aprender la metodología y poder ejecutarla**. Lee esta guía entera
> antes de actuar. El corpus completo son **~3,9M tokens** — NO intentes cargarlo todo;
> usa las capas de abajo.

## ⛔ Protocolo de fidelidad (anti-invención) — LÉELO PRIMERO
El usuario quiere que **repliques el curso tal cual**, no que improvises. Reglas
obligatorias:
1. **Solo fuente primaria.** Replica desde las **notas**, **transcripciones** y
   **recursos** (capas 2 y 3). Los documentos curados (capa 1: `RESUMEN-MAESTRO`,
   `INDICE-POR-CATEGORIA`, `categorias/`) son un **mapa**, NO la verdad — no cites pasos
   a partir de ellos.
2. **No inventes lo que no está.** Si un paso solo se ve en el vídeo (la transcripción
   dice "le damos *aquí*", "ponemos *esto*" sin el valor/UI exacto) o el dato no aparece
   en el archivo, **DETENTE y marca**: `⚠️ Paso no disponible en el archivo — requiere
   ver el vídeo: <enlace>`. NUNCA rellenes con un valor plausible inventado.
3. **Transcripciones = aproximadas.** Son auto-subtítulos con errores ("Cloud
   Code"→"Claude Code", "P3.1"→"Veo 3.1"). Corrige términos obvios y, ante duda,
   contrasta con las **notas** de esa lección; si sigue sin estar claro, márcalo.
4. **Credenciales:** las claves del creador están **redactadas** (`r8_REDACTED…`). Usa
   SIEMPRE las del usuario; nunca inventes ni reutilices claves.
5. Ante cualquier ambigüedad, **pregunta al usuario** antes de ejecutar algo irreversible.

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

## 🕳️ Huecos conocidos del archivo (qué NO está, para que no lo inventes)
- **Lo que se *ve* en los vídeos** (clics, ajustes en pantalla) **no está**: las
  transcripciones son solo audio. Donde un paso dependa de lo visual y la nota no lo
  detalle → márcalo (regla 2). Hueco **irreducible**.
- **3 vídeos sin transcripción** (2 directos + 1 webinar): solo título/notas.
- **Errores de auto-subtítulo** en las transcripciones (ver regla 3).
- **GIFs de pantalla:** se dejan como **enlace** a Skool (no archivados; muy pesados y no
  procesables por una IA). Las **capturas estáticas SÍ** están en [`imagenes/`](imagenes/).
- **Enlaces externos** (afiliados, Notion, Google Drive) referenciados: solo enlaces.
- **Cuentas/servicios en vivo:** ejecutar de verdad requiere cuentas y claves propias del
  usuario (Higgsfield, GoHighLevel, n8n, ElevenLabs, Airtable…).

## Estrategia de contexto (importante para una IA)
- ¿Chat con límite de contexto? Carga **solo la capa 1** para aprender, y pega lecciones
  puntuales de la capa 2 cuando hagan falta.
- ¿Agente con acceso a ficheros (Claude Code, etc.)? Lee la capa 1, luego **abre ficheros
  bajo demanda** vía `estructura.json` / `INDICE.md`. No cargues los 826 `.md` de golpe.
