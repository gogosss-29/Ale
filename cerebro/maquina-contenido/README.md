# 🎬 Máquina de Contenido — Cerebro / Mia

Sistema agéntico que convierte un **ángulo** en el **paquete de producción
completo de un reel** (guion + prompts de avatar + prompts de B-rolls), siguiendo
el método documentado por Alexander en Notion. Es el primer caso de uso real del
sistema agéntico del curso, aplicado a Cerebro.

## Cómo se usa
En una sesión de Claude Code (acá en la web o en tu compu con las skills
copiadas), decí algo como:
> "Armemos un reel para Cerebro, objetivo TOFU, con este ángulo: …"

El orquestador `reel-cerebro` corre el pipeline con gates (te pide aprobar en
cada paso). Si no traés ángulo, lee 3 del banco de Notion y elegís.

## Las skills (viven en `.claude/skills/`)
| Skill | Qué hace | Estación |
|---|---|---|
| `reel-cerebro` | Orquesta todo (idea → paquete) y conecta Notion | — |
| `guion-cerebro` | Ángulo → guion en bloques de 10s (TOFU/MOFU/BOFU) | 1-4 |
| `director-avatar` | Locución → prompts del avatar (Veo 3.1) | 5 |
| `brolls-cerebro` | Momentos → prompts de Flow (8 bloques, 8 estilos) | 6-7 |

Cada skill es un porte fiel de tu documentación de Notion (Sistema Creador de
Guiones / B-Rolls / Director de Avatar). No inventan método.

## Dónde está aplicado el curso (framework SMART)
- **S — Skills:** las 4 skills de arriba. ✅
- **M — MCP:** el orquestador lee el banco de ideas y guarda el reel en **Notion**
  (conector). 🟡 (la generación de video sigue manual: Flow no tiene API)
- **A — Artifacts:** el paquete del reel (ver `ejemplos/`). ✅
- **R — Refine:** los gates + el ajuste de voz se vuelcan a las skills. ✅
- **T — Test:** cada guion aprobado se guarda en Notion "Guiones" (base de datos
  de voz real) y los mejores realimentan el few-shot. ✅ (bucle de mejora)

## 🔁 Bucle de mejora (importante)
Cada guion **aprobado/corregido** por Ale se guarda en la página **"Guiones"** de
Notion → así crece la base de datos de guiones reales. Los más representativos se
suman al few-shot (`guion-cerebro/referencias/ejemplos-reales.md`) y los giros
nuevos al perfil de voz (`voz-ale.md`). Resultado: la máquina suena cada vez más
a Ale. Solo entran guiones aprobados (voz real, no borradores de la máquina).

## Lo que es manual hoy (honesto)
1. Pegar los prompts en **Google Flow** y generar los clips (Flow no tiene API).
2. Edición final (Mayra): montar avatar + b-rolls + textos en pantalla.

## Roadmap
1. ✅ Fase 1 — Skills (hecho).
2. 🔜 Fase 2 — MCP a fondo: leer/guardar en Notion automático; experimento de
   auto-avatar con Higgsfield (Soul + voz).
3. ⏭️ Fase 3 — Hermes 24/7: correr el orquestador en horario (ej. 1 reel listo a
   las 6am) + captación por WhatsApp.

## Ejemplos
- `ejemplos/reel-001-ganancia-cero.md` — reel TOFU completo de punta a punta.
