# Prompt maestro para retomar (pegar en un chat nuevo)

> Copia TODO el bloque de abajo y pégalo en el chat nuevo.

---

Hola, retomamos un proyecto en curso. Lee este contexto entero antes de actuar y, si estás
en el repo `gogosss-29/Ale` (rama `claude/upbeat-lamport-ec6bjh`), abre también `CLAUDE.md`,
`cerebro/` y `docs/` para el detalle completo. Respóndeme en español.

## Qué es el proyecto
Crear y operar el **avatar digital ("clon IA") de Alexander**: una identidad reutilizable
entrenada en Higgsfield (cara + voz) para generar imágenes fotorrealistas y vídeos hablados
con sincronización labial. Es un proyecto **independiente** de mi otro proyecto "Cerebro ·
Consultora IA" (no mezclar).

## Dónde está todo (fuente de verdad = el repo)
- Repo `gogosss-29/Ale`, rama `claude/upbeat-lamport-ec6bjh`. `CLAUDE.md` se autocarga.
- `cerebro/` — el brain: `00-vision`, `01-el-curso` (apunta al curso real), `02-playbook`
  (cómo técnico), `03-activos` (IDs), `04-estado`, y `PARA-NOTION.md` (doc operativo
  consolidado, listo para pegar en Notion).
- `docs/` — **EL CURSO REAL extraído** (AvatarHype): `SISTEMA-AVATARHYPE.md` (maestro),
  `transcripciones/`, `recursos-prompts/` (los prompts reales), `notas-lecciones/`.
- `avatarhype/` — pipeline en Python (esqueleto) para automatizar el sistema.
- Notion: proyecto "Sistema Avatar IA" (espejo, con título a corregir: emoji duplicado y
  página "El Curso" a actualizar con el contenido de `cerebro/PARA-NOTION.md`).

## Activos vivos en Higgsfield (cuenta de Alexander, válidos entre sesiones)
- Soul "Alexander v2" (USAR): `9ffc9c16-eeb2-465d-b2b5-03a7b14a227d`
- Retrato base v2: `43c9b6e8-e08c-47af-b8b7-94b61bae1b2e`
- Voz clip 12 s: `41bd653e-a16f-4089-baea-60cbcfba1d18`
- Voz completa 3:27: `efc51158-010b-4a2f-ae28-a9b1d4026f90`
- Generar imagen: `generate_image` model `soul_2` + `soul_id`. Vídeo: `generate_video`
  model `seedance_2_0`, start_image=retrato, audio=clip 12 s, 9:16, 12 s, 720p.

## El curso (AvatarHype) en una línea
Enseña a producir anuncios de e-commerce con avatares IA hiperrealistas (UGC, podcast, voz
en off, dualcast, image-ads) por la ruta barata: revender modelos vía **Kie.ai / APImart**
(Veo 3.1, **Omni Flash**, GPT Image 2) + ElevenLabs + CapCut. Clave: ángulo + guion, no la
herramienta. Detalle completo en `docs/SISTEMA-AVATARHYPE.md`.

## Estado
- HECHO: Soul v2 entrenado, voz subida, retratos generados (buen parecido), curso
  documentado en `docs/`, cerebro en el repo.
- PENDIENTE: generar el vídeo hablado; volcar `cerebro/PARA-NOTION.md` a Notion; decidir
  ruta de producción; automatizar el pipeline.

## Bloqueos y lecciones clave (MUY importante)
1. **Las operaciones MCP de escritura se bloquean en sesiones automáticas/remotas** con
   `MCP tool call requires approval`: esto afecta a `generate_video` (Higgsfield) y a crear/
   editar páginas en Notion. Las de lectura y `generate_image` SÍ funcionan. ⇒ El vídeo y la
   escritura en Notion hay que hacerlos en una **sesión interactiva** (app/escritorio/web),
   donde el diálogo de aprobación se puede aceptar. No es el archivo de permisos de Claude.
2. **El avatar (Higgsfield) se hizo con criterio propio, NO con el curso.** El curso usa otra
   ruta (APImart/Veo/Omni Flash), no Higgsfield. Son dos métodos paralelos para el mismo fin;
   falta decidir cuál estandarizar o si combinarlos (Higgsfield para identidad + curso para volumen).
3. **Seguridad:** en la sesión anterior se pegó una cookie de Whop con tokens vivos. Alexander
   debe cerrar sesión en Whop y reentrar para invalidarla. No volver a pegar credenciales en chat.

## Decisiones ya tomadas por Alexander
- El "clon IA" es un proyecto aparte de "Cerebro · Consultora IA".
- NO quiere validar el curso generando imágenes UGC de prueba con Higgsfield (lo descartó).

## Cómo continuar
Pregúntame por dónde quiero seguir. Las opciones abiertas son: (a) generar el vídeo hablado
(en sesión interactiva), (b) volcar el cerebro a Notion, (c) decidir la ruta de producción y
empezar a **automatizar el pipeline** (n8n + APIs del curso + Higgsfield). No asumas; confirmá
conmigo el rumbo antes de ejecutar acciones que consuman créditos o escriban en sitios externos.
