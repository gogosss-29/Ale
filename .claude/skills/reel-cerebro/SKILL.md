---
name: reel-cerebro
description: >-
  Orquestador de la máquina de contenido de Cerebro/Mia. De un ángulo (que trae
  Ale o que lee del banco "Ideas y Ángulos" en Notion) produce el paquete
  completo de un reel encadenando las skills guion-cerebro → director-avatar →
  brolls-cerebro, y (opcional) guarda el reel terminado en Notion. Úsala cuando
  Ale diga "armemos un reel", "dame el reel completo", "máquina de contenido" o
  pida el paquete de producción de punta a punta.
---

# 🎛️ Reel Cerebro — Orquestador de la máquina de contenido

> Esta skill NO reescribe el método: **coordina** las tres skills de producción y
> los conectores (MCP). Es el "agente con herramientas": Skills (S) + MCP (M) del
> framework SMART del curso, aplicados al caso real de Cerebro.

## Mapa del pipeline (cada paso tiene gate: confirmar antes de seguir)

```
[Notion: Ideas y Ángulos]                 ← MCP (opcional, Estación 1)
            │  (o ángulo que trae Ale)
            ▼
   1) guion-cerebro      → guion 10s + pista B-rolls + handoff
            ▼  (gate: Ale aprueba esqueleto y guion)
   2) director-avatar    → prompts del avatar por secuencia
            ▼
   3) brolls-cerebro     → prompts de Flow (8 bloques)
            ▼
   4) Ensamblar paquete  → 1 documento: guion + avatar + b-rolls
            ▼  (gate: Ale aprueba)
   5) [Notion: guardar reel terminado]    ← MCP (opcional, Estación T)
```

## Pasos

**1 — TEMA (Estación 1).**
- Si Ale trae un ángulo → usarlo.
- Si pide ideas → leer el banco con Notion MCP (`notion-fetch` de la página
  "💡 Ideas y Ángulos de Contenido", id `3435f7242166812e9682ddfe2a8ff85b`),
  proponer 3 ángulos y que elija. **No avanzar sin ángulo elegido.**

**2 — GUION.** Invocar **guion-cerebro** con el ángulo. Definir marca
(Cerebro/Mia) y objetivo (TOFU/MOFU/BOFU). Gate: Ale aprueba el esqueleto, luego
el guion segmentado.

**3 — AVATAR.** Pasar la "locución sin comas" del handoff a **director-avatar**.
Salida: un prompt por secuencia (Sec 1 completa + Sec 2+ con frame de referencia).

**4 — B-ROLLS.** Pasar las entradas BR a **brolls-cerebro**. Antes de escribir
prompts, proponer 2-4 conceptos por momento y que Ale elija. Salida: prompts de
Flow (8 bloques).

**5 — ENSAMBLAR.** Unir todo en un solo documento de producción:
`# Título · marca · objetivo · duración · 9:16`
`## 1 Guion (10s) · ## 2 Avatar (prompts) · ## 3 B-rolls (prompts Flow) · ## 4 Textos en pantalla`
Guardar copia local en `cerebro/maquina-contenido/ejemplos/`.

**6 — GUARDAR + REALIMENTAR (regla fija, no opcional).** Cuando Ale **aprueba o
corrige** un guion, SIEMPRE:
1. Guardarlo en Notion como sub-página de **"Guiones"**
   (`notion-create-pages`, parent page_id `37b5f7242166804795f2f1d1bba84c76`),
   con el guion en bloques de 10s y metadata al inicio:
   `Marca · Objetivo (TOFU/MOFU/BOFU) · Duración · Estado: Aprobado · Fecha`.
   Esto construye la **base de datos de guiones reales** de Ale.
2. Si el guion es notablemente bueno/representativo, **sumarlo al few-shot**
   `guion-cerebro/referencias/ejemplos-reales.md` (curado, ver Bucle de mejora).
> Solo se guardan guiones **aprobados/corregidos por Ale** (no borradores de la
> máquina): la base de datos es voz real, no aproximaciones.

## Qué automatiza y qué no (honesto)
- **Automatiza (acá mismo):** la idea→guion→todos los prompts (el "cerebro").
- **Manual (Flow no tiene API):** pegar los prompts en Google Flow y generar los
  clips; y la edición final (Mayra) que monta avatar + b-rolls + textos.
- **Futuro (Fase 3):** correr este orquestador en horario fijo desde Hermes (ej.
  dejar 1 reel listo a las 6am) y/o auto-generar el avatar con Higgsfield.

## 🔁 Bucle de mejora (Refine/Test) — la máquina aprende sola
Cada guion aprobado alimenta a la siguiente generación:
- **Notion "Guiones" = base de datos completa** (todos los aprobados, con metadata).
- **`ejemplos-reales.md` = few-shot curado** (selección representativa por objetivo
  TOFU/MOFU/BOFU y formato; ~3-6 ejemplos). No meter todo acá: se elige lo mejor
  para que el modelo imite calidad, no cantidad.
- **`voz-ale.md`** se refresca cuando aparezcan giros/metáforas/muletillas nuevas
  recurrentes en los guiones aprobados.
- Periódicamente (o cuando la base crezca), revisar la base de Notion y actualizar
  el few-shot y el perfil de voz con lo mejor.
> Nota de entorno: si guardar en Notion devuelve "requires approval", pedir a Ale
> que apruebe el conector, o dejar el guion listo para que lo pegue él.

## Reglas
- Respetar las reglas inmutables de cada skill hija (no duplicarlas acá).
- Un solo reel por corrida (no batch salvo que Ale pida "plan de racimo" → ver el
  Multiplicador de Ángulo en guion-cerebro).
- Gates obligatorios: nunca generar prompts de avatar/b-roll sin guion aprobado.

## Anti-patrones
Saltar gates · armar b-rolls sin proponer conceptos antes · mezclar marcas
(Cerebro vende, Mia nunca) · inventar el ángulo en vez de pedirlo/leerlo.
