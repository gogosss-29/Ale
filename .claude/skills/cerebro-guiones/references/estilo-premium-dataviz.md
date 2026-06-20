# 📊 Estilo Cerebro — Premium Data Motion (estándar nuevo de B-rolls)

> **La dinámica nueva.** Reemplaza el enfoque editorial estático (#05/#06) como
> **default**. Validado por Ale (prompts reales que funcionaron en Flow/Veo). Principio:
> el **dato/concepto, con TEXTO, ES el contenido** — informa, aporta y engancha. Calidad
> broadcast. Los estilos viejos quedan como secundarios (metáfora pura sin dato).

## Filosofía
- **El texto/número aporta valor** (no decora). Por eso, a diferencia del sistema viejo,
  acá el texto SÍ va en el render. Cada b-roll enseña un dato.
- **Producción de alto nivel:** motion graphics tipo After Effects, cámara con movimiento,
  multi-etapa, ritmo punchy. Nada estático ni "plano".
- **Claridad financiera:** verde = positivo, rojo = negativo/alerta. Lectura instantánea.

## FIRMA FIJA (se repite en todos los b-rolls del estilo)
- **[STYLE base]:** `Vertical 9:16 premium After Effects mixed-media motion graphics, 24fps, [DUR]s, broadcast quality. Editorial design-studio aesthetic, camera movement, parallax, soft shadows, subtle film grain, shallow depth of field.`
- **Fondo:** grid claro tipo cutting-mat `#EDEDED` con sombras gobo en movimiento y viñeta leve. Props reales opcionales (chinche rojo, clip).
- **Tipografía:** sans-serif **bold, negro tinta `#111111`**, kinética, español, palabras EXACTAS.
- **Paleta:** grid `#EDEDED`/`#FFFFFF` · negro `#111111` · **verde `#1FB85B`** (positivo/ingreso) · **rojo `#E2352B`** (alerta/egreso/costo) · *opcional acento amarillo marca*.
- **Animación:** multi-etapa, cámara (dolly-in / pan / whip-pan) + parallax, números/barras que crecen con easing + motion blur, ritmo punchy.
- **Audio:** sin voz; clicks UI, golpe de bajo, whooshes, beeps/ticks, synth cálido.
- **NEGATIVE base:** `No dark neon-only scene, no vintage sepia, no messy clutter, no static single-pose animation, no slow boring motion, no low-res look, no voiceover, no narration, no human speech.`

## VARIABLE (lo único que cambia por pieza)
1. **Layout** (elegir patrón abajo) · 2. **Dato/concepto** · 3. **Texto exacto en pantalla** · 4. **Duración** (según el dato, ver buckets).

## 4 patrones (layouts)
- **P1 · Panel KPI / Card glass** — tablero "TU NEGOCIO" o card con un dato grande. (hooks, "no conocés tus números", una métrica). → ej. V1.
- **P2 · Chart 3D + línea de tendencia** — barras ingreso/egreso, saldo descendente, alerta. (evolución temporal, liquidez, facturación vs ganancia). → ej. V2.
- **P3 · Comparativa de cards** — A vs B con números y barra de margen, gana el mejor. (precio/costo/margen, opciones). → ej. V3.
- **P4 · Ranking / lista** — lista ordenada con métricas por ítem (clientes, productos). (rankings, "el 20% que deja el 80%").

## Reglas
1. **Texto exacto y corto** en `[TEXT ON SCREEN]`. **NO** meter códigos hex en el texto (Veo los "imprime"): el color va solo en `[COLOR PALETTE]`.
2. **Duración = el dato** (ver buckets 4/6/8/10s en `director-avatar-omni.md`). Una idea por b-roll.
3. **Verde/rojo** solo para el significado financiero (no decorativo).
4. Para **dato/número → este estilo**. Para **metáfora pura sin dato** → #05/#06 (secundarios).
5. B-roll informativo: el dato tiene que ser **real** (de Ale) o un ejemplo claramente ilustrativo; sin números inventados como si fueran reales.

---

## Prompts validados (referencia / copiar-pegar)

### V1 · Panel KPI "TU NEGOCIO" (P1, 4s)
```
[STYLE]: Vertical 9:16 premium After Effects mixed-media motion graphics, 24fps, 4 seconds, broadcast quality. Editorial design-studio aesthetic: clean light grid surface, real props, floating glass UI panel, bold kinetic typography, camera movement, parallax, soft shadows, subtle film grain, shallow depth of field.
[BACKGROUND]: Soft grey-white cutting-mat grid #EDEDED with gentle moving drop shadows and a faint vignette. A red pushpin and a paperclip rest at the edges as real props.
[MAIN ELEMENT]: A floating frosted-glass dashboard panel titled "TU NEGOCIO" with five KPI cards in a column: "MARGEN", "FLUJO DE CAJA", "RENTABILIDAD", "CLIENTES", "MARKETING". Every value field is empty, showing a blinking red "?" instead of a number. At the end a red ribbon blindfold sweeps across the whole panel.
[ANIMATION]: Multi-stage. Camera dolly-in toward the panel with parallax. The five KPI cards drop in one by one with realistic shadows and a soft bounce. Each "?" blinks red. At the end a red blindfold ribbon whips across the panel. Punchy rhythm, motion blur on entries.
[TEXT ON SCREEN]: Bold modern sans-serif, ink-black #111111 labels, blinking red "?" values, Spanish. Title "TU NEGOCIO".
[COLOR PALETTE]: Grid grey-white #EDEDED / #FFFFFF, ink black #111111, alert red #E2352B.
[MOOD]: Premium, editorial, tense setup, flying blind without data.
[AUDIO]: NO voice, NO narration. Deep bass hit on the dolly-in, crisp UI clicks as cards drop, blinking digital beeps, a sharp whoosh on the blindfold sweep. Warm punchy synth.
[NEGATIVE]: No dark neon-only scene, no vintage sepia, no messy clutter, no static single-pose animation, no slow boring motion, no low-res look, no voiceover, no narration, no human speech.
```

### V2 · Chart 3D + alerta de liquidez (P2, 6s)
```
[STYLE]: Vertical 9:16 premium After Effects mixed-media motion graphics, 24fps, 6 seconds, broadcast quality. Editorial design-studio aesthetic, light grid surface, 3D bar chart, kinetic typography, camera movement, parallax, soft shadows, subtle grain, shallow depth of field.
[BACKGROUND]: Soft grey-white cutting-mat grid #EDEDED with gentle moving shadows, faint vignette.
[MAIN ELEMENT]: A 3D monthly chart across six months (ENE to JUN). For each month a green "ingreso" bar up and a red "egreso" bar down. A glowing balance line "SALDO" runs across the top of the bars, descending month by month until it crosses zero into red around month four, where a kinetic "⚠ ALERTA DE LIQUIDEZ" badge snaps in.
[ANIMATION]: Multi-stage. Camera pans left-to-right following the months as bars grow with easing and realistic shadows. The saldo line draws itself descending. When it crosses into red the camera pushes in and the "⚠ ALERTA" badge slams in with a light-streak and a small shake. Punchy.
[TEXT ON SCREEN]: Bold sans-serif kinetic, Spanish: "ENE FEB MAR ABR MAY JUN", "INGRESOS", "EGRESOS", "SALDO", "⚠ ALERTA DE LIQUIDEZ".
[COLOR PALETTE]: Grid grey-white #EDEDED / #FFFFFF, ink black #111111, ingreso green #1FB85B, egreso/alert red #E2352B.
[MOOD]: Premium, data-driven, rising tension toward the alert.
[AUDIO]: NO voice, NO narration. Rhythmic UI ticks as bars grow, a descending tone as the line falls, a sharp impact and alarm-like digital beep on the alert. Deep bass, warm synth.
[NEGATIVE]: No dark neon-only scene, no vintage sepia, no messy clutter, no static single-pose animation, no slow boring motion, no low-res look, no voiceover, no narration, no human speech.
```

### V3 · Comparativa de margen A vs B (P3, 6s)
```
[STYLE]: Vertical 9:16 premium After Effects mixed-media motion graphics, 24fps, 6 seconds, broadcast quality. Editorial design-studio aesthetic: clean light grid surface, floating glass UI cards, bold kinetic typography and numbers, camera movement, parallax, soft shadows, subtle grain, shallow depth of field.
[BACKGROUND]: Soft grey-white cutting-mat grid #EDEDED with gentle moving shadows and faint vignette.
[MAIN ELEMENT]: Two product cards side by side, "PRODUCTO A" and "PRODUCTO B". STAGE 1: card A shows "Precio $1.000" then "− Costo $600" then a green margin bar fills to "MARGEN $400 (40%)". STAGE 2: camera whips to card B with "Precio $1.500 − Costo $1.200" and a shorter green bar "MARGEN $300 (20%)". STAGE 3: both cards align, card A glows green with a check, highlighted as the one that contributes more.
[ANIMATION]: Numbers fly in with motion blur and snap. The subtraction animates, the margin bar fills with easing. Camera whip-pan between A and B, then pulls back to compare both with parallax. Card A pulses green with a check mark. Punchy, rhythmic.
[TEXT ON SCREEN]: Bold sans-serif kinetic numbers, Spanish: "PRODUCTO A", "Precio $1.000", "Costo $600", "MARGEN $400 (40%)", "PRODUCTO B", "$1.500", "$1.200", "MARGEN $300 (20%)".
[COLOR PALETTE]: Grid grey-white #EDEDED / #FFFFFF, ink black #111111, positive green #1FB85B, cost red #E2352B.
[MOOD]: Premium, financial clarity, satisfying reveal.
[AUDIO]: NO voice, NO narration. Crisp UI ticks as numbers count, a bass hit when the margin fills, whoosh on the whip, satisfying snap and a positive chime on card A. Warm synth.
[NEGATIVE]: No dark neon-only scene, no vintage sepia, no messy clutter, no static single-pose animation, no slow boring motion, no low-res look, no voiceover, no narration, no human speech.
```

> Para un b-roll nuevo: elegí patrón (P1-P4), copiá el V correspondiente y cambiá solo
> `[MAIN ELEMENT]` + `[TEXT ON SCREEN]` con el dato/concepto. La firma (fondo, paleta,
> animación, audio, negative) se mantiene.
