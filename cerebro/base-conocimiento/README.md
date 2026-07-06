# 📚 Base de conocimiento — Cerebro

Destilado de contenido de calidad (negocio, finanzas, emprendimiento) para
alimentar la máquina de contenido. Viene del proyecto de Antigravity de Ale, que
descarga canales de YouTube y analiza cada video.

## Qué hay
- `videos-analizados.md` — 67 videos **completados**, cada uno con: Conceptos
  Clave · Información Útil · Casos y Experiencias · Citas Destacadas.
- `INDICE.md` — listado con título, URL y programa.

## Cobertura honesta (estado al 2026-06-19)
- **408 videos** en el proyecto. **67 completados** (los que están acá).
- **316 sin transcripción** todavía · **25 con error de LLM**.
- Es decir: esta base es **parcial** (~16%). Crece a medida que el proyecto de
  Antigravity procesa el resto.

## Para qué se usa (y para qué NO)
- ✅ **Materia prima de ÁNGULOS, casos y datos** para los guiones de Cerebro/Mia.
  Es una fuente de la Estación 1 (TEMA), junto al banco "Ideas y Ángulos" de Notion.
- ✅ Inspiración de estructura y frameworks de creadores de negocio.
- ❌ **NO es la voz de Ale.** La voz sale de sus propios guiones
  (`.claude/skills/guion-cerebro/referencias/`). Lo de acá se **reescribe** en su voz.
- ⚠️ Citas y casos son de **terceros**: van **atribuidos**, nunca como propios ni
  como estadísticas inventadas.

## Cómo se actualiza (patrón de acceso)
Mientras la base esté en tu máquina local:
1. **Rápido (lo que hicimos):** exportás el `analisis_videos.xlsx` y me lo pasás;
   yo regenero esta base. Repetible cuando haya más completados.
2. **Escala (recomendado a futuro):** Claude Code local + **Graphify** (lección
   036) sobre la carpeta de transcripciones → base consultable con 4x menos tokens,
   sin exportar a mano.

## Regenerar desde el xlsx
`python3 -` con el script de ingesta (ver historial de la sesión): filtra
`Estado == 'Completado'` y vuelca los 4 campos a `videos-analizados.md` + `INDICE.md`.
