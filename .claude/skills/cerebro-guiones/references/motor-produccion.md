# ⚙️ Motor de Producción — qué herramienta usa el sistema y cuándo

> Regla del sistema: **no hay una única manera de hacer las cosas.** Cada pieza de
> contenido se produce con la herramienta más fuerte para ESE momento. Este archivo
> es el router: la skill lo consulta al armar el plan de producción de cada reel y
> declara la herramienta elegida por pieza (nunca por default ciego).

## Las herramientas del equipo

| Herramienta | Qué es | Su fuerte | Su debilidad |
|---|---|---|---|
| **Omni / Flow (Veo)** | IA generativa de video | Personas hablando, fotorrealismo, escenas orgánicas, metáforas con materia (escultura, tinta, oro), explorar looks rápido. **Omni además renderiza TEXTO en pantalla correctamente (Ale, 2026-07-06)** | **Veo/Flow y Veo por API deforman texto** y números (comprobado 2026-07-06); timing impreciso, cada intento sale distinto y cuesta créditos |
| **Remotion** | Video programado (React), lo renderiza Claude y entrega .mp4 | Texto/tipografía perfectos, datos y números reales, timing al frame (sync con locución), marca idéntica en cada reel, gratis, parametrizable | No genera personas ni fotorrealismo; texturas orgánicas complejas cuestan mucho código |
| **CapCut** | Edición humana | Montaje final, ritmo fino, capa de realismo, música/ducking | Manual |
| *(futuro)* APIs Kie/APImart | Generativa por API (curso AvatarHype) | Volumen barato de UGC ads | Por integrar |

## 🧭 La regla de oro (decisión en 3 preguntas)
1. **¿Aparece una persona / el avatar?** → **Omni/Flow. Siempre.**
2. **¿El contenido es texto, dato, número, chart o marca que debe salir EXACTA?** → **Remotion.**
3. **¿Es una escena/metáfora que debe parecer REAL u orgánica?** → **Flow.**
> Híbrido válido: fondo/escena generado en Flow + capa de datos/texto en Remotion o CapCut encima.

## Router por tipo de pieza

| Momento / pieza del contenido | Herramienta | Estilo |
|---|---|---|
| Avatar hablando (todos los clips) | **Omni/Flow** | Director de Avatar |
| B-roll de datos: charts, KPIs, comparativas, rankings | **Remotion** | #11 Data Motion |
| B-roll tipográfico: hooks, punchlines, intros de lista | **Remotion** | #13 Kinetic Typography |
| Firma de marca: intros/cierres, glifo, lower thirds | **Remotion** | #99 Cerebro Signature |
| Mostrar una plataforma/app con UI **exacta** | **Remotion** | #12 (variante UI) |
| Mostrar plataforma con mood cinematográfico (glow, 3D) | **Flow** | #12 Dark Tech Reveal |
| Metáfora conceptual orgánica (escultura, collage, vintage) | **Flow** | #05/#06 elevados |
| Escenarios y sesiones de fotos (imagen de referencia) | **Flow** | banco de escenarios |
| Textos en pantalla sobre el avatar | **CapCut** (o Remotion overlay) | — |
| UGC ads de producto | **Omni/Flow** (+ APIs a futuro) | avatarhype |
| Exploración de un look/estilo nuevo | **Flow** primero (rápido); si se adopta como marca → portar a **Remotion** (exacto y repetible) | crear-estilo-broll |

## Reglas del router
1. **Declarar la herramienta por pieza** en el plan de producción de cada reel (columna "Herramienta"), con el porqué si no es obvio.
2. **Nunca texto/números importantes en generativa**: si un b-roll de Flow necesita un dato exacto, el dato va en Remotion/CapCut encima, o la pieza entera pasa a Remotion.
3. **Marca = código**: todo elemento de identidad repetible (glifo, intro, cierre, lower third) se hace UNA vez en Remotion y se reutiliza. La marca no se regenera, se renderiza.
4. **Explorar en Flow, industrializar en Remotion**: la generativa es el laboratorio; lo que se vuelve estándar de marca se programa.
5. Si una pieza falla 2+ veces en una herramienta, el router evalúa la otra (o el híbrido) antes de insistir.

## Estado
- Omni/Flow: ✅ operativo (manual, sin API).
- Remotion: 🔜 **pendiente de piloto** — instalar en el repo y renderizar el BR3 del
  reel-003 como validación. Si el piloto pasa, portar #11, #13 y #99 a plantillas.
- CapCut: ✅ operativo (Ale/Mayra).
