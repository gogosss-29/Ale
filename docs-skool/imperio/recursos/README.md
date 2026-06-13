# Recursos descargables del curso (adjuntos)

Los adjuntos de las lecciones (skills `.zip`/`.tar.gz`, plantillas n8n/Make `.json`,
bases de Airtable, etc.) **no** viajan en el contenido de la lección: Skool los sirve
con URLs firmadas. Se descargan con `POST /files/<file_id>/download-url` (ver
`../../METODO-ACCESO-SKOOL.md`) — implementado en `skool/api.py:download_resource()`.

## ads-cabrones-ia — Generador de anuncios cinematográficos
Skill de Claude Code de Imperio Digital. Toma 3 inputs (money shot + concept board +
brief) y genera un **comercial cinematográfico completo** en ~6 min por ~$7-8:
imágenes (GPT Image 2) → vídeos (Seedance 2.0 1080p, duraciones variables) → voz y
música (ElevenLabs) → edición FULL + CUTS narrativo (ffmpeg) → persistencia en
Airtable. Vía **Higgsfield MCP** + Claude Code. Es agnóstico de marca/estética.

- **`ads-cabrones-ia/ads-cabrones-ia-v2.3.tar.gz`** — el skill instalable (30 KB).
- **`ads-cabrones-ia/ads-cabrones-ia/`** — el skill descomprimido (SKILL.md, system/,
  templates/, scripts/, references/) para leerlo sin extraer.
- **`ads-cabrones-ia/0X-*.md`** — guías: instalación, Airtable, Higgsfield MCP,
  Airtable PAT, ElevenLabs, y un caso de estudio real (Ford F150 "viejo oeste").
- **`ads-cabrones-ia/concept-board-template.png`** — grid vacío para tus assets.

### Instalación rápida
```bash
mkdir -p ~/.claude/skills
tar -xzf ads-cabrones-ia-v2.3.tar.gz -C ~/.claude/skills
# reinicia Claude Code; en un proyecto nuevo: "vamos a hacer un ad cinematográfico"
# la primera vez corre el wizard de onboarding (~2 min, pide credenciales).
```
Requiere: Claude Code, Higgsfield (MCP), ElevenLabs (API key), Airtable (PAT), ffmpeg.
Detalle completo en `ads-cabrones-ia/README.md` y `ads-cabrones-ia/01-instalacion.md`.

> Procedencia: adjunto de la lección **Claude Code › "Ads Cinemáticos con Higgsfield +
> Claude Code"** (`v3_imperio-ads_claudecode.zip`). Descargado con tu sesión.
