---
name: guion-cerebro
description: >-
  Convierte un tema + ángulo crudo en un guion de reel estructurado para las
  marcas Cerebro (consultora IA) y Mia (marca personal de Alexander Witenko).
  Segmenta la narración en bloques de 10s (2,8 pal/seg), aplica el arco
  TOFU/MOFU/BOFU y entrega 3 bloques separados: guion (narración), pista de
  B-rolls y handoff a los prompts. Úsala cuando Ale pida "armar un guion",
  "hacer un reel", "guion para Cerebro/Mia" o traiga un ángulo/idea para
  convertir en video. NO escribe de cero: Ale aporta el ángulo, la skill lo
  estructura y lo refina.
---

# 🎬 Guion Cerebro — Estación 1→4 del Sistema Creador de Guiones

> Esta skill automatiza el método documentado por Alexander (Notion: "Sistema
> Creador de Guiones"). Es la fuente de verdad operativa. Skills hermanas:
> `director-avatar` (Estación 5: prompts del avatar) y `brolls-cerebro`
> (Estaciones 6-7: pista y prompts de Flow). El orquestador `reel-cerebro` las
> encadena.

## Principio fundamental
La skill NO inventa el contenido: **Ale aporta el ángulo o el concepto; la skill
lo estructura, lo segmenta y lo refina.** Nunca se improvisa la estructura ni se
inventan estadísticas.

## Contexto y tono (vale para las dos marcas)
- **Cerebro · Consultora IA** — consultora de crecimiento para pymes argentinas
  (datos + IA + marketing + profesionalización). Conversión comercial vía ads.
- **Mia (@alexanderwitenko)** — marca personal 100% educativa, autoridad
  orgánica. **Mia nunca menciona Cerebro ni es comercial.**

**Voz:** español argentino coloquial, trato de "vos". Calmo y autoritario,
nunca confrontativo ni condescendiente (se le habla al que mira como un par).
Educativo, no vendedor ("observación educada" antes que hot take). Anclado en la
realidad pyme, sin jerga corporativa. **Sin estadísticas inventadas:** si no hay
fuente real (ej. CACE), claim suave basado en experiencia.

## Pipeline (estaciones que cubre esta skill)
Cada paso tiene un gate: no se avanza sin confirmar.

**Estación 1 — TEMA.** Fuente: banco "Ideas y Ángulos de Contenido" /
"Biblioteca de Contenido" en Notion, o lo trae Ale. Salida: tema + ángulo crudo.
→ Si Ale no da ángulo, ofrecer 3 del banco y que elija. No avanzar sin ángulo.

**Estación 2 — OBJETIVO.** Elegir TOFU, MOFU o BOFU (ver framework abajo).
Cargar su receta: arco, densidad, duración, CTA y ratio avatar/b-roll.

**Estación 3 — DESARROLLO.** Proponer el esqueleto de escenas en borrador
(funciones narrativas: HOOK → CONTEXTO/CASO → GIRO → PUNCH → CTA). **Ale aprueba
el esqueleto antes de escribir la narración.**

**Estación 4 — GUION (narración).** Escribir la narración completa, de punta a
punta, y segmentarla en bloques de 10s con el motor determinístico.

Al terminar, hacer el handoff a `director-avatar` y `brolls-cerebro`.

## Framework de objetivo — TOFU / MOFU / BOFU
No se mezclan. Cada objetivo impone su estructura.

### 🔵 TOFU — atraer (público frío)
- **Meta:** que alguien que no te conoce pare, se identifique y aprenda algo.
- **Hook:** dolor reconocible o dato fuerte.
- **Arco:** hook → dolor → reframe ("no es tu culpa, es estructura") → enseñanza
  → cierre con esperanza.
- **CTA:** suave ("seguime que te ayudo a estructurar tu negocio").
- **Densidad:** media, narrativo/emocional. **Duración:** 45–90s.
  **Ratio:** puede inclinarse a más avatar.

### 🟡 MOFU — considerar (ya te sigue)
- **Meta:** mostrar cómo pensás y trabajás.
- **Hook:** promesa de método.
- **Arco:** hook → pasos numerados → caso con números reales → por qué funciona
  → cierre con criterio.
- **CTA:** palabra clave en comentarios.
- **Densidad:** alta, técnica. **Duración:** 60–100s. **Ratio:** 50/50.

### 🟢 BOFU — convertir (listo para dar el paso)
- **Meta:** que dé el paso.
- **Hook:** resultado, prueba o pregunta de calificación.
- **Arco:** hook → qué hacemos → resultado → qué te dejamos → CTA directo.
- **CTA:** directo ("¿querés saber cómo está tu empresa hoy? Escribinos").
- **Densidad:** media-alta. **Duración:** 45–70s. **Ratio:** 50/50.

## Motor de segmentación a bloques de 10s (determinístico, no a ojo)
1. Ritmo de referencia: **2,8 palabras/segundo** (~168 wpm).
2. Tope duro: **10s = 28 palabras**. NUNCA se supera.
3. Ventana objetivo: **6–10s (17–28 palabras)**.
4. Cortar en **límite de frase**; si una frase supera 28 palabras, cortar en el
   **conector** más cercano (y, pero, porque, entonces, así que…).
5. Mostrar siempre la **duración estimada** de cada bloque = palabras ÷ 2,8.
6. **Palabras intactas:** reestructurar a 10s nunca es reescribir el guion.

## Multiplicador de Ángulo (módulo opcional, upstream)
Un ángulo fuerte es una cantera, no una piedra. Si Ale lo pide, exprimir el
mismo núcleo en varias piezas variando 3 ejes, sin re-derivar el insight:
- **Arista:** dolor · dato · caso · mito a refutar · pregunta de calificación ·
  contraste antes/después.
- **Formato:** reel largo · reel corto · carrusel · post de texto (el largo se
  produce una vez y de ahí se derivan los cortos).
- **Objetivo:** el mismo insight en TOFU, MOFU y BOFU.
Salida: un "plan de racimo" (qué piezas, qué arista, qué formato, qué objetivo,
orden de publicación). Cada pieza debe agregar valor propio (no recortar la misma).

## Plantilla canónica de salida (3 bloques SEPARADOS)
Nunca se mezclan narración y B-roll en una misma línea.

```
# [TÍTULO]
Marca: [Cerebro/Mia] · Objetivo: [TOFU/MOFU/BOFU] · Duración: [NNs] · Formato: 9:16

## 1 · GUIÓN COMPLETO (avatar · voz propia) — secciones de 10s
[0:00–0:10] "..."   (NN palabras · ~N,Ns)
[0:10–0:20] "..."   (NN palabras · ~N,Ns)
...

## 2 · GUIÓN DE B-ROLLS (entran en edición)
BRn | entra mm:ss | dura 4/6s | qué se muestra + estilo
Textos en pantalla: [mm:ss "TEXTO"]

## 3 · HANDOFF
- Locución sin comas por sección → skill `director-avatar` (prompts del avatar).
- Entradas de B-roll → skill `brolls-cerebro` (prompts de Flow, 8 bloques).
```

**Funciones narrativas:** HOOK (primera sección, gancho en los primeros 3s),
CONTEXTO/CASO, GIRO, PUNCH (frase citeable), CTA (última, con acción clara).

**Locución para el avatar (Omni/Veo):** la versión que va al generador se pasa
**sin comas** (puntos solo si son muy necesarios), porque el motor estira las
pausas en cada signo. La versión con puntuación normal queda para lectura humana
y para los textos en pantalla.

## 10 reglas inmutables (no se rompen nunca)
1. El avatar narra el guion completo con la voz propia, en secciones de 10s. Los
   B-rolls se suman en edición.
2. Arco obligatorio según objetivo. No se improvisa la estructura.
3. Español argentino, tono calmo y autoritario.
4. Vertical 9:16 siempre.
5. ~50% del timeline cubierto por B-roll; el resto muestra al avatar.
6. B-rolls de 4 o 6 segundos; nunca se cubre el 100%.
7. Sin estadísticas inventadas.
8. Hook en los primeros 3s; CTA siempre con acción clara.
9. La skill no escribe de cero: Ale aporta el ángulo.
10. Mia nunca es comercial.

## Banco de hooks que ya funcionaron
Dato fuerte con fuente · dolor reconocible · promesa de método · pregunta de
calificación · mirada desde adentro.

## Anti-patrones
- Mezclar objetivos (TOFU vendiendo, BOFU sin CTA). · Bloques de >28 palabras. ·
- Inventar datos/porcentajes. · Narración que el B-roll repite literal (el B-roll
  debe sumar info, prueba o emoción, no decorar). · Tono de vendedor o de gurú.

## Recuperación
Si un bloque queda largo → re-segmentar en el conector, no reescribir. Si el
ángulo es débil → volver a Estación 1 y pedir/elegir otro. Si Ale no aprueba el
esqueleto → iterar la Estación 3, no saltar a narración.
