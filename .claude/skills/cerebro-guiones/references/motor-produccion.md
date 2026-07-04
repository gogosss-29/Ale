# ⚙️ Motor de Producción — qué herramienta usa el sistema y cuándo

> Regla del sistema: **no hay una única manera de hacer las cosas.** Cada pieza de
> contenido se produce con la herramienta más fuerte para ESE momento. Este archivo
> es el router: la skill lo consulta al armar el plan de producción de cada reel y
> declara la herramienta elegida por pieza (nunca por default ciego).

## Las herramientas del equipo

| Herramienta | Qué es | Su fuerte | Su debilidad |
|---|---|---|---|
| **Omni / Flow (Veo)** | IA generativa de video | Personas hablando, fotorrealismo, escenas orgánicas, metáforas con materia (escultura, tinta, oro), explorar looks rápido | Deforma texto, números inexactos, timing impreciso, cada intento sale distinto y cuesta créditos |
| **Remotion** | Video programado (React), lo renderiza Claude y entrega .mp4 | Texto/tipografía perfectos, datos y números reales, timing al frame (sync con locución), marca idéntica en cada reel, gratis, parametrizable | No genera personas ni fotorrealismo; texturas orgánicas complejas cuestan mucho código |
| **Omni (compositing / edición)** | Omni animando motion graphics ENCIMA de un clip real ya grabado (skill `omni-reels`) | Animaciones/motion graphics ricos y orgánicos "estilo AE" DENTRO del propio video del avatar, con poco esfuerzo | Generativo: puede tocar voz/personaje si el prompt no es benigno + time-based; sale 720p → upscalar |
| **CapCut** | Edición humana | Montaje final, ritmo fino, capa de realismo, música/ducking | Manual |
| *(futuro)* APIs Kie/APImart | Generativa por API (curso AvatarHype) | Volumen barato de UGC ads | Por integrar |

> ⚠️ **Omni tiene DOS usos distintos:** (1) **generar** footage nuevo (avatar hablando, escenas) — lo de siempre; (2) **editar/compositar** gráficos sobre footage que YA existe — la skill `omni-reels`. La fila de arriba es el uso de edición.

## 🎬 Rutas de EDICIÓN / montaje del reel (cómo se arma la pieza final)

Tres formas de montar el reel; se eligen por pieza y se pueden **combinar**:

| Ruta | Los gráficos los pone… | Fuerte | Cuándo |
|---|---|---|---|
| **Remotion `ReelAssembly`** | el código (determinista) | control total, timing al frame, marca exacta, 0 riesgo de regenerar, gratis | b-rolls de datos, texto/marca, ensamblado reproducible |
| **Omni compositing** (`omni-reels`) | Omni, generativo sobre el clip | motion graphics ricos/orgánicos DENTRO del clip del avatar, poco esfuerzo | animaciones vivas encima del talking-head cuando el "estilo AE" aporta más que el control exacto |
| **CapCut** | edición humana | ritmo fino, capa de realismo, música | montaje/retoque final a mano |

> No compiten: p. ej. **Omni** para animar gráficos orgánicos sobre un clip + **Remotion** para los b-rolls de datos (#11) y el cierre de marca (#99) + **CapCut** para el pulido final.

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
| Animaciones / motion graphics DENTRO del clip del avatar | **Omni compositing** | omni-reels |
| UGC ads de producto | **Omni/Flow** (+ APIs a futuro) | avatarhype |
| Exploración de un look/estilo nuevo | **Flow** primero (rápido); si se adopta como marca → portar a **Remotion** (exacto y repetible) | crear-estilo-broll |

## Reglas del router
1. **Declarar la herramienta por pieza** en el plan de producción de cada reel (columna "Herramienta"), con el porqué si no es obvio.
2. **Nunca texto/números importantes en generativa**: si un b-roll de Flow necesita un dato exacto, el dato va en Remotion/CapCut encima, o la pieza entera pasa a Remotion.
3. **Marca = código**: todo elemento de identidad repetible (glifo, intro, cierre, lower third) se hace UNA vez en Remotion y se reutiliza. La marca no se regenera, se renderiza.
4. **Explorar en Flow, industrializar en Remotion**: la generativa es el laboratorio; lo que se vuelve estándar de marca se programa.
5. Si una pieza falla 2+ veces en una herramienta, el router evalúa la otra (o el híbrido) antes de insistir.

## Estado
- Omni/Flow (generar): ✅ operativo (manual, sin API).
- Omni compositing (editar, `omni-reels`): ✅ operativo (manual) — ruta de edición
  documentada; faltan en el repo sus helpers (`scripts/reel_cutter.py`, `reference/`).
- Remotion: ✅ operativo — piloto pasado; #11/#12/#13/#99 portados y compo
  `ReelAssembly` renderizando el reel-003 completo (Fase 3).
- CapCut: ✅ operativo (Ale/Mayra).
