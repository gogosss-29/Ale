# 🎬 Sistema Creador de Guiones

> Documentación completa del método para crear guiones de reels de la consultora Cerebro y la marca personal Mia. Diseñada para que cualquier IA o persona pueda replicar el sistema sin contexto previo. Es la página hermana del **🎬 Sistema Creador de B-Rolls** y se engancha con ella en la última estación.

---

## 🎯 Qué hace este sistema

Convierte un **tema + un ángulo crudo** en un **guion estructurado en escenas de 10 segundos**, listo para grabar con avatar real y para alimentar el sistema de B-rolls de Google Flow. Garantiza que cada guion salga consistente con el embudo (TOFU/MOFU/BOFU), con el tono de la marca y con la velocidad real de locución del avatar — sin tener que re-explicar la lógica cada vez.

El sistema NO escribe guiones de cero. Ale aporta el ángulo o el concepto; el sistema lo estructura y lo refina.

---

## 🗂️ Cómo navegar este sistema

1. **Contexto y tono** → quién es el usuario, para qué marca, con qué voz
2. **Pipeline de 6 estaciones** → el flujo de trabajo de punta a punta con sus gates
3. **Framework de objetivo (TOFU/MOFU/BOFU)** → la receta estructural según el momento del embudo
4. **Plantilla canónica de guion** → la estructura fija de escenas de 10s
5. **Marcado de B-rolls** → cómo se reparte avatar/B-roll y cómo se conecta con el sistema de Flow
6. **Reglas inmutables** → lo que no se rompe nunca
7. **Banco de hooks y ángulos** → de dónde salen los temas

---

## 1. Contexto y tono

**Marcas:**
- **Cerebro · Consultora IA** — consultora de crecimiento para pymes argentinas (datos + IA + marketing + profesionalización). Conversión comercial vía ads.
- **Mia (@alexanderwitenko)** — marca personal 100% educativa. Construye audiencia y autoridad orgánica. Mia nunca menciona Cerebro.

**Voz (vale para las dos):**
- Español argentino coloquial, trato de "vos".
- Calmo y autoritario, **nunca confrontativo ni condescendiente**. El que mira es dueño de un negocio: se le habla como par.
- Educativo, no vendedor. "Observación educada" antes que hot take.
- Anclado en la realidad pyme real, no en jerga corporativa traducida.
- **Sin estadísticas inventadas.** Si no hay fuente real (ej. CACE), se usa un claim suave basado en experiencia.

---

## 2. Pipeline de 6 estaciones

Cada estación tiene un gate: no se avanza hasta cerrarla. Cada guion guarda **en qué estación quedó**, para retomar sin repetir contexto.

**Estación 1 — TEMA**
Fuente: la página de Notion *Ideas y Ángulos de Contenido* o *Biblioteca de Contenido*, o lo trae Ale.
Salida: tema + ángulo crudo (la bajada concreta, el punto de vista).

**Estación 2 — OBJETIVO**
Se elige TOFU, MOFU o BOFU. Esto **carga automáticamente la receta** de la sección 3 (arco, densidad, tipo de CTA).

**Estación 3 — DESARROLLO**
Ale da el ángulo. El sistema propone la **estructura de escenas** (qué pasa en cada bloque de 10s) en borrador, sin redacción fina todavía. Ale aprueba o corrige el esqueleto.

**Estación 4 — GUION (narración del avatar)**
El avatar narra el guion completo con la voz del usuario. Se redacta la narración entera, dividida en secciones de 10s (~19–26 palabras cada una). El avatar habla de punta a punta: no hay secciones sin narración.

**Estación 5 — PRODUCCIÓN DE AVATAR (Omni)** · agente *Director de Avatar*
Cada bloque de 10s de narración se convierte en un prompt para **Omni** (el avatar se genera en secuencias de 10s con la voz/dialecto del usuario). El Director de Avatar suma el toolkit cinematográfico: tipo de plano y lente, movimiento de cámara, acción del avatar, ambiente, transición, ritmo y acto — todo alineado al objetivo (anuncio IG). Respeta el formato real de Omni: los datos fijos (avatar `@alexander.witenko`, 40% más bronceado, dialecto, 9:16, ritmo, línea de cierre) van **solo en la primera secuencia**; las continuaciones arrancan con "Continua la grabación…" y solo dicen lo que cambia. Detalle completo en el doc *Director de Avatar (Omni)*.

**Estación 6 — PISTA DE B-ROLLS**
Los B-rolls son una capa que se monta **en edición, encima de la narración** — no reemplazan al avatar. Se arma una lista aparte: cada B-roll indica en qué momento entra (mm:ss), cuánto dura (4 o 6s) y el estilo sugerido. Apuntar a que **~50% del timeline** quede cubierto por B-roll; el resto muestra al avatar.

**Estación 7 — PROMPTS FLOW (B-rolls)**
Las entradas de la pista de B-rolls pasan al **Sistema Creador de B-Rolls** (plantilla de 8 bloques) para generar los prompts de Google Flow.

---

## 3. Framework de objetivo — recetas TOFU / MOFU / BOFU

Cada objetivo impone una estructura. No se mezclan.

### 🔵 TOFU — atraer (público frío, no te conoce)

- **Meta:** que alguien que no te conoce pare, se sienta identificado y aprenda algo.
- **Hook (0–3s):** dolor reconocible o dato fuerte. Ej: *"Hay un tipo de cansancio que no se cura durmiendo."*
- **Arco:** hook → escena compartida / dolor → reframe ("no es tu culpa, es estructura") → enseñanza → cierre con esperanza.
- **CTA:** suave. *"Seguime que te ayudo a estructurar tu negocio."*
- **Densidad:** media. Más narrativo y emocional que técnico.
- **Duración típica:** 45–90s.
- **Ratio sugerido:** puede inclinarse a más avatar (la conexión importa más que el dato).
- **Ejemplos tuyos:** *El error de apagar incendios*, *El cansancio que no se cura durmiendo*, *5 datos que tenés que saber*.

### 🟡 MOFU — considerar (ya te sigue, está evaluando)

- **Meta:** mostrar cómo pensás y cómo trabajás para que te consideren.
- **Hook (0–3s):** promesa de método. Ej: *"Así desarrollamos una estrategia para una hamburguesería."*
- **Arco:** hook → pasos o pilares numerados → caso concreto con números reales → por qué funciona → cierre con criterio.
- **CTA:** palabra clave en comentarios. *"Comentá ESTRUCTURA / delivery y te paso la info."*
- **Densidad:** alta. Técnica, con números, enumeraciones.
- **Duración típica:** 60–100s.
- **Ratio sugerido:** 50/50 (hay mucho concepto abstracto que cubrir con B-roll).
- **Ejemplos tuyos:** *Cómo auditamos*, *Estrategia de ads — caso hamburguesería*, *3 fundamentos financieros*.

### 🟢 BOFU — convertir (ya te considera, listo para dar el paso)

- **Meta:** que el que ya te considera dé el paso.
- **Hook (0–3s):** resultado, prueba o pregunta de calificación. Ej: *"Esto vemos cuando auditamos un negocio."*
- **Arco:** hook → qué hacemos exactamente → resultado / transformación → qué te dejamos → CTA directo.
- **CTA:** directo. *"¿Querés saber cómo está tu empresa hoy? Escribinos."*
- **Densidad:** media-alta, concreta, orientada a la oferta.
- **Duración típica:** 45–70s.
- **Ratio sugerido:** 50/50.
- **Ejemplos tuyos:** *Cómo auditamos* (cierre comercial), casos reales.

---

## 4. Plantilla canónica de guion

El entregable son **tres bloques separados**: el guion (narración del avatar), la pista de B-rolls y los prompts de Flow. Nunca se mezclan narración y B-roll en una misma línea.

```
# [TÍTULO DEL GUION]
Objetivo: [TOFU / MOFU / BOFU]   ·   Duración total: [NNs]   ·   Formato: 9:16
Palabra clave de activación (si aplica): [PALABRA]

## 1 · GUIÓN COMPLETO (avatar · voz propia) — secciones de 10s
[0:00–0:10] "..."
[0:10–0:20] "..."
[0:20–0:30] "..."
( …el avatar narra el 100%, ~19–26 palabras por sección… )

## 2 · GUIÓN DE B-ROLLS (entran en edición)
| #  | Entra | Dura | Qué se muestra |
| BR1 | 0:11 | 6s  | [descripción + estilo sugerido] |
| BR2 | 0:31 | 6s  | [descripción + estilo sugerido] |
Textos en pantalla: [mm:ss "TEXTO" · …]

## 3 · PROMPTS DE B-ROLLS (Flow)
[un prompt de 8 bloques por cada B-roll]
```

**Funciones narrativas (en la narración):** HOOK (primera sección), CONTEXTO/CASO, GIRO o revelación, PUNCH (frase citeable), CTA (última sección).

**Regla de locución:** ~19–26 palabras por sección de 10s. Conceptos cortos pegados pueden ir más densos; frases con énfasis (una palabra clave fuerte), más cortas.

**Locución para Omni:** cuando la locución se pasa al avatar en Omni, va **sin comas** (puntos solo si son muy necesarios), porque Omni estira las pausas en cada signo de puntuación. La versión con puntuación normal queda solo para lectura humana.

---

## 5. Pista de B-rolls (conexión con el sistema de Flow)

- Los B-rolls se montan **en edición sobre la narración**: el avatar narra el 100%, el B-roll tapa la imagen en ciertos momentos.
- **Target ~50% del timeline cubierto por B-roll;** el resto muestra al avatar. El video respira con el avatar.
- Cada B-roll lleva: **momento de entrada (mm:ss)**, **duración (4 o 6 segundos)**, descripción del momento cubrible y **estilo sugerido** de la Biblioteca de Estilos.
- Buenos candidatos a B-roll: metáfora visual fuerte, concepto abstracto que se aclara con imagen, enumeraciones (1-2-3), transiciones, hooks que necesitan retención.
- Las escenas B-ROLL se exportan a la estación 6 y entran en la **Plantilla Maestra de 8 bloques** del Sistema Creador de B-Rolls. Ahí se resuelven STYLE, BACKGROUND, MAIN ELEMENT, ANIMATION, TEXT ON SCREEN, COLOR PALETTE, MOOD, AUDIO, NEGATIVE.
- Recordatorio del sistema de B-rolls: prompts de 1.800–3.000 caracteres, sin voz, 9:16, y si se repite estilo dentro del video, variar al menos 3 de las 5 variables.

---

## 6. Reglas inmutables

1. **El avatar narra el guion completo** con la voz propia, en secciones de 10s (~19–26 palabras). Los B-rolls se suman después en edición.
2. **Arco obligatorio según objetivo** (sección 3). No se improvisa la estructura.
3. **Español argentino**, tono calmo y autoritario, nunca confrontativo ni condescendiente.
4. **Vertical 9:16** siempre.
5. **~50% del timeline cubierto por B-roll**, el resto muestra al avatar.
6. **B-rolls de 4 o 6 segundos**, nunca se cubre el 100% del video.
7. **Sin estadísticas inventadas.** Claims con fuente real o suavizados por experiencia.
8. **Hook en los primeros 3 segundos**; **CTA siempre con acción clara**.
9. **El sistema no escribe de cero:** Ale aporta el ángulo, el sistema estructura y refina.
10. **Mia nunca es comercial.** Si el guion es para Mia, no menciona Cerebro ni vende.

---

## 7. Banco de hooks y ángulos

Fuente principal: página de Notion **Ideas y Ángulos de Contenido** (`3435f724-2166-812e-9682-ddfe2a8ff85b`) y **Biblioteca de Contenido** (`3435f724-2166-818f-934e-e8edaa6a171f`).

Patrones de hook que ya funcionaron:
- **Dato fuerte con fuente:** *"En los últimos 3 años, 3,2 millones de argentinos compraron por primera vez en un e-commerce."*
- **Dolor reconocible:** *"Hay un tipo de cansancio que no se cura durmiendo."*
- **Promesa de método:** *"Así desarrollamos una estrategia de marketing para una hamburguesería. Te lo cuento en un minuto."*
- **Pregunta de calificación:** *"Si no podés responder estas tres preguntas en menos de un minuto, estás trabajando a ciegas."*
- **Mirada desde adentro:** *"Esto vemos cuando auditamos un negocio."*

---

*Sistemas hermanos: 🎬 Sistema Creador de B-Rolls.*
*Última actualización: junio 2026.*
