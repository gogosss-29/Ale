# 00 — Visión & Conexión

## Qué es este sistema
El "cerebro" central para crear y operar el **avatar digital de Alexander** en
Higgsfield: una identidad reutilizable (Soul) entrenada con su cara + su voz, con
la que se generan imágenes fotorrealistas y vídeos hablados con sincronización
labial. La meta es que el proceso sea **reproducible por cualquier IA o persona**
sin depender de un chat puntual.

## Principio rector
**Un chat es efímero; el cerebro es permanente.** Nada importante debe vivir solo
en una conversación. Todo conocimiento (proceso, técnicas, IDs, estado) se escribe
aquí. Cualquier agente nuevo: 1) lee el cerebro, 2) abre la sección que necesita,
3) ejecuta, 4) actualiza el estado al terminar.

## Cómo se conecta una IA
1. **Contexto base**: leer `00`, `03` (activos) y `04` (estado) siempre al empezar.
2. **Para ejecutar una tarea**: leer `02` (playbook técnico) la sección relevante.
3. **Para entender el porqué / replicar de cero**: leer `01` (el curso).
4. **Herramientas**: el sistema usa el conector MCP de **Higgsfield** (generación) y
   opcionalmente Google Drive (origen de material) y Notion (cerebro espejo).

## Dónde vive el cerebro
- **Repositorio git** — fuente de verdad, persistente y versionada. `CLAUDE.md` se
  autocarga en cada sesión. Contiene:
  - `cerebro/` — este índice/brain (visión, curso, playbook, activos, estado).
  - `docs/` — **EL CURSO REAL extraído** (AvatarHype): documento maestro,
    transcripciones, y las bibliotecas de prompts. ⚠️ No reescribir el curso en
    `cerebro/`; siempre apuntar a `docs/`.
  - `avatarhype/` — pipeline en Python para automatizar el sistema.
- **Notion** (espejo legible para humanos) — proyecto "Sistema Avatar IA" (proyecto
  del clon, independiente del "Cerebro · Consultora IA"). Se sincroniza desde una
  sesión con permisos de escritura aprobados.
- **Cuenta de Higgsfield** — guarda los activos reales (Soul, medios, voz). IDs en `03`.

## Regla anti-error (importante)
Antes de documentar o "construir el brain", **explorar TODO el repo primero**
(`docs/`, `avatarhype/`), no solo `cerebro/`. El curso completo ya está en `docs/`;
no duplicarlo ni ignorarlo.

## Aprendizaje clave sobre el entorno (leer antes de frustrarse)
Las operaciones MCP que **escriben/crean** (generar vídeo, crear páginas en Notion)
requieren una **aprobación interactiva** que un entorno automático/remoto no puede
conceder, y fallan con `MCP tool call requires approval`. Las de **lectura** pasan
siempre. Las de generación de imagen y subida de medios funcionaron porque ya
estaban aprobadas. ⇒ Para tareas de escritura nuevas, usar una **sesión interactiva**
(app/escritorio/web), donde el diálogo de aprobación sí se puede aceptar.
