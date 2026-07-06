# Guion 001 — Sueldo extra invirtiendo: caso real $300M

Objetivo: **Conversión (CCC)** · Duración: ~85s · Formato: 9:16
Base: borrador de Ale (2026-07-06) + datos reales de Notion "cartera 300 millones"
Estado: **✅ APROBADO por Ale (2026-07-06)** — monto real $300M, cierre
opción A (directo). La opción B queda como alternativa si luego montan el
embudo de palabra clave.

> ⚠️ Único pendiente de producción: la **captura real de resultados**
> (la aportan Ale/Mati) para el bloque de 1:04.

## 1 · GUIÓN COMPLETO (Mati a cámara) — bloques de 10s

**[0:00–0:09] HOOK (24 palabras ≈ 8,6s)**
"300 millones de pesos para invertir. El objetivo: crear un sueldo y
conservar el capital. Te cuento cómo armé la cartera de este cliente."

**[0:09–0:18] LA PERSONA (24 palabras ≈ 8,6s)**
"Primero tengo que conocer a la persona. Nunca invirtió. La plata viene de
la venta de un departamento y de una indemnización por despido."

**[0:18–0:27] EMPATÍA (27 palabras ≈ 9,6s)**
"Nunca gestionó esta cantidad de plata y encima se quedó sin trabajo.
Imaginate el estrés. Pero tiene capital para salir adelante. No es la
situación de todos."

**[0:27–0:36] LA CARTERA, PARTE 1 (25 palabras ≈ 8,9s)**
"Entendiendo su situación le propuse esta cartera. 200 millones van a
conservar el capital: cuatro bonos del Estado con distintos vencimientos
que ajustan por inflación."

**[0:36–0:45] QUÉ ES UN BONO CER (26 palabras ≈ 9,3s)**
"O sea, le prestás plata al Estado y tu capital se actualiza todos los
meses con la inflación. Cuatro bonos distintos para diversificar y tener
flexibilidad."

**[0:45–0:54] LA CARTERA, PARTE 2 (26 palabras ≈ 9,3s)**
"Los otros 100 millones van a un fondo común de inversión con liquidez
diaria. De acá sale el sueldo todos los meses sin tocar los bonos."

**[0:54–1:04] LA METÁFORA (28 palabras = 10s)**
"Pensalo como un tanque de agua: el tanque principal son los bonos, que
crece con el tiempo. Y un tanque de uso diario de donde salen los gastos."

**[1:04–1:13] EL PUNCH + PRUEBA (25 palabras ≈ 8,9s)**
"¿Cuánto genera? No te lo puedo prometer de antemano. Lo que sí te puedo
mostrar: empezamos en abril de 2025 y estos fueron los resultados."
*(→ acá entra la CAPTURA REAL de resultados en pantalla)*

**[1:13–1:22] CIERRE — opción A, la del borrador de Ale (25 palabras ≈ 8,9s)**
"Hace 8 años que gestiono capital para empresas y personas. Si querés
sacarle más rendimiento a tu plata, nos conocemos y vemos qué podemos hacer."

**[1:13–1:22] CIERRE — opción B, variante CCC con palabra clave (24 palabras ≈ 8,6s)**
"Hace 8 años que gestiono capital para empresas y personas. Comentá CARTERA
y te muestro cómo se podría armar una para tu caso."

## 2 · GUIÓN DE B-ROLLS / GRÁFICOS (entran en edición)

| # | Entra | Dura | Qué se muestra | Tipo |
|---|---|---|---|---|
| BR1 | 0:03 | 4s | Card: "$300.000.000" + "objetivo: sueldo + conservar capital" | informativo (P1 KPI) |
| BR2 | 0:12 | 4s | Texto kinético: "venta de depto + indemnización" | texto (P3) |
| BR3 | 0:29 | 6s | Split: "$200M → 4 bonos CER (vencimientos escalonados)" | informativo (P3 comparativa) |
| BR4 | 0:47 | 6s | Card: "$100M → FCI liquidez diaria → retiro mensual" | informativo (P1) |
| BR5 | 0:55 | 6s | Animación tanque de agua: principal (bonos) + uso diario (FCI) | metáfora (generativo o motion graphic) |
| BR6 | 1:05 | 6s | **Captura real de resultados** (⚠️ la aporta Mati) + "abril 2025 → hoy" | informativo (prueba) |

Cierre (1:13→fin) limpio sobre Mati, sin B-roll.
Textos en pantalla: 0:05 "$300.000.000" · 0:30 "$200M bonos" · 0:47 "$100M FCI" · 1:06 "resultados reales".

## 3 · PROMPTS DE B-ROLLS — para OMNI (manual, texto en pantalla ✅)

> Plantilla maestra de 8 bloques (brolls-biblioteca) · estilo #11 Premium Data
> Motion · CON texto (Omni renderiza texto bien — dato de Ale 2026-07-06).
> Flujo: runbook reel-002 paso 3 — pegar en Flow/Omni, modo Fast, sin imagen
> de referencia, verificar que no meta voz. Duración BR1/BR2 = 4s, BR3/BR4/BR5 = 6s.

### BR1 · Card $300M (4s, entra 0:03)
```
[STYLE]: Vertical 9:16 premium After Effects mixed-media motion graphics, 24fps, 4 seconds, broadcast quality. Editorial design-studio aesthetic: clean light grid surface, floating frosted-glass UI card, bold kinetic typography, camera movement, parallax, soft shadows, subtle film grain, shallow depth of field.
[BACKGROUND]: Soft grey-white cutting-mat grid #EDEDED with gentle moving drop shadows and a faint vignette.
[MAIN ELEMENT]: CENTER: a large floating frosted-glass finance card with a huge bold number "$300.000.000". LOWER THIRD: two small glass chips side by side, left chip with a green check icon and the text "CREAR UN SUELDO", right chip with a green shield icon and the text "CONSERVAR EL CAPITAL".
[ANIMATION]: Punchy and front-loaded: the big number snaps in within the first 1.5 seconds with motion blur; camera slow dolly-in with parallax; the two chips pop in with soft bounce and realistic shadows; subtle floating idle at the end. Camera completely static at the end.
[TEXT ON SCREEN]: Bold modern sans-serif, ink-black #111111, Spanish, EXACT words only: "$300.000.000", "CREAR UN SUELDO", "CONSERVAR EL CAPITAL".
[COLOR PALETTE]: Grid grey-white #EDEDED / #FFFFFF, ink black #111111, positive green #1FB85B.
[MOOD]: Premium, editorial, confident financial clarity.
[AUDIO]: NO voice, NO narration, NO speech of any kind. Deep bass hit on the number landing, crisp UI clicks as chips pop, warm punchy synth bed.
[NEGATIVE]: No dark neon-only scene, no vintage sepia, no messy clutter, no static single-pose animation, no slow boring motion, no low-res look, no voiceover, no narration, no human speech, no misspelled words, no extra text, no logos.
```

### BR2 · Origen del capital (4s, entra 0:12)
```
[STYLE]: Vertical 9:16 premium After Effects motion graphics, 24fps, 4 seconds, broadcast quality. Editorial design-studio aesthetic: clean light grid surface, bold kinetic typography, camera movement, parallax, soft shadows, subtle film grain.
[BACKGROUND]: Soft grey-white cutting-mat grid #EDEDED with gentle moving shadows and faint vignette. A red pushpin at the top-left edge and a paperclip at the lower-right edge as real props.
[MAIN ELEMENT]: Kinetic typography sequence. UPPER: the words "VENTA DE UN DEPARTAMENTO" in bold ink-black type. BELOW IT: "+ INDEMNIZACIÓN" stamped beneath. LOWER: a thin ink-black horizontal line, and under it a small green chip with white text "CAPITAL PARA EMPEZAR".
[ANIMATION]: Punchy front-loaded kinetic type: first line slides in within the first 1.5 seconds; second line stamps in with impact and a slight controlled camera shake; the line draws itself left to right; the green chip pops with a soft scale bounce. Camera drifts with gentle parallax, then completely static at the end.
[TEXT ON SCREEN]: Bold modern sans-serif, ink-black #111111, Spanish, EXACT words only: "VENTA DE UN DEPARTAMENTO", "+ INDEMNIZACIÓN", "CAPITAL PARA EMPEZAR".
[COLOR PALETTE]: Grid grey-white #EDEDED / #FFFFFF, ink black #111111, green accent #1FB85B.
[MOOD]: Premium, editorial, a human story told with type.
[AUDIO]: NO voice, NO narration, NO speech of any kind. Paper slide whoosh on line one, stamp impact on line two, soft tick on the line draw, warm synth.
[NEGATIVE]: No dark neon-only scene, no vintage sepia, no messy clutter, no static single-pose animation, no slow boring motion, no low-res look, no voiceover, no narration, no human speech, no misspelled words, no extra text, no logos.
```

### BR3 · $200M en 4 bonos (6s, entra 0:29)
```
[STYLE]: Vertical 9:16 premium After Effects mixed-media motion graphics, 24fps, 6 seconds, broadcast quality. Editorial design-studio aesthetic: clean light grid surface, floating glass UI cards, bold kinetic typography and numbers, camera movement, parallax, soft shadows, subtle grain, shallow depth of field.
[BACKGROUND]: Soft grey-white cutting-mat grid #EDEDED with gently moving shadows and faint vignette.
[MAIN ELEMENT]: UPPER: a frosted-glass header card with the bold number "$200.000.000" and the label "BONOS DEL ESTADO" under it. CENTER: the header splits into four smaller glass cards in a 2x2 grid, each with a minimal bond-document icon and a different year tag ("2027", "2028", "2030", "2031" — placeholder years, confirm real maturities). LOWER: a green ribbon banner sweeps in with white bold text "AJUSTAN POR INFLACIÓN".
[ANIMATION]: Multi-stage, punchy, front-loaded: header lands within the first 1.5 seconds with a bass-synced impact; it splits into the four cards with snappy staggered pops and realistic shadows; camera push-in with parallax; ribbon sweeps in with a light streak. Camera completely static at the end.
[TEXT ON SCREEN]: Bold modern sans-serif, ink-black #111111, Spanish, EXACT words only: "$200.000.000", "BONOS DEL ESTADO", "2027", "2028", "2030", "2031", "AJUSTAN POR INFLACIÓN".
[COLOR PALETTE]: Grid grey-white #EDEDED / #FFFFFF, ink black #111111, positive green #1FB85B.
[MOOD]: Premium, data-driven, protective and solid.
[AUDIO]: NO voice, NO narration, NO speech of any kind. Bass hit on the header, crisp UI clicks on each card pop, whoosh on the ribbon sweep, warm synth.
[NEGATIVE]: No dark neon-only scene, no vintage sepia, no messy clutter, no static single-pose animation, no slow boring motion, no low-res look, no voiceover, no narration, no human speech, no misspelled words, no extra text, no logos.
```

### BR4 · $100M FCI → retiro mensual (6s, entra 0:47)
```
[STYLE]: Vertical 9:16 premium After Effects mixed-media motion graphics, 24fps, 6 seconds, broadcast quality. Editorial design-studio aesthetic: clean light grid surface, floating glass UI cards, bold kinetic typography, camera movement, parallax, soft shadows, subtle grain, shallow depth of field.
[BACKGROUND]: Soft grey-white cutting-mat grid #EDEDED with gentle moving shadows and faint vignette.
[MAIN ELEMENT]: UPPER: a frosted-glass card with the bold number "$100.000.000" and the label "FONDO COMÚN DE INVERSIÓN" under it. UPPER-RIGHT: a small rounded rectangular pill chip (NOT a casino chip) in green with white text "LIQUIDEZ DIARIA". CONNECTING THEM: a smooth green arrow flows downward from the card into a minimal flat green wallet icon, with three small golden coins pulsing along the arrow in a monthly rhythm. LOWER: a green rounded pill chip with white bold text "RETIRO MENSUAL".
[ANIMATION]: Punchy, front-loaded: card lands within the first 1.5 seconds with a bass hit and motion blur; the pill chip pops; the arrow draws downward with flowing green particles pulsing rhythmically; coins pulse on each beat; camera slow push-in with parallax. Camera completely static at the end.
[TEXT ON SCREEN]: Bold modern sans-serif, ink-black #111111, Spanish, EXACT words only: "$100.000.000", "FONDO COMÚN DE INVERSIÓN", "LIQUIDEZ DIARIA", "RETIRO MENSUAL".
[COLOR PALETTE]: Grid grey-white #EDEDED / #FFFFFF, ink black #111111, flow green #1FB85B, small golden coin accents.
[MOOD]: Premium, fluid, dependable monthly income.
[AUDIO]: NO voice, NO narration, NO speech of any kind. Bass hit on the card, UI click on the chip, soft rhythmic ticks as the coins pulse, warm synth.
[NEGATIVE]: No casino chips, no poker elements, no dark neon-only scene, no vintage sepia, no messy clutter, no static single-pose animation, no slow boring motion, no low-res look, no voiceover, no narration, no human speech, no misspelled words, no extra text, no logos.
```

### BR5 · Metáfora del tanque de agua (6s, entra 0:55)
```
[STYLE]: Vertical 9:16 premium 3D motion graphics, 24fps, 6 seconds, broadcast quality. Clean design-studio aesthetic: light studio background with subtle grid floor, glossy photorealistic 3D render, soft studio lighting, gentle camera movement, shallow depth of field, subtle film grain.
[BACKGROUND]: Soft grey-white studio with a faint cutting-mat grid floor #EDEDED, gentle shadows, faint vignette.
[MAIN ELEMENT]: A water-tank metaphor for a two-part portfolio. LEFT: a LARGE transparent main water tank with a floating ink-black label tag "BONOS", filled with calm clear blue water slowly rising. RIGHT: a SMALL daily-use tank with a floating label tag "FCI", connected to the main tank by a clean transparent pipe. LOWER-RIGHT: from the small tank a chrome tap pours a steady gentle stream into a drinking glass with a floating label tag "SUELDO" and a small green up-tick icon. IMPORTANT: all three label tags stay INSIDE the frame at all times, anchored near their object, never cropped by the frame edges.
[ANIMATION]: Camera slow push-in (minimal movement, keep all labels fully visible in frame). Water in the main tank rises subtly; the pipe pulses; the tap opens and the glass fills with a satisfying pour; the green tick pops at the end. Front-loaded: both tanks and all three labels fully visible within the first 1.5 seconds. Camera completely static at the end.
[TEXT ON SCREEN]: Bold modern sans-serif, ink-black #111111 on small white floating tags, Spanish, EXACT words only: "BONOS", "FCI", "SUELDO".
[COLOR PALETTE]: Grey-white studio #EDEDED / #FFFFFF, ink black #111111, clear blue water, one positive green accent #1FB85B.
[MOOD]: Premium, calm, ingenious clarity — income today without draining tomorrow.
[AUDIO]: NO voice, NO narration, NO speech of any kind. Soft water flow, gentle glass fill, a subtle click on the green tick, warm calm synth.
[NEGATIVE]: No cartoon style, no dark neon-only scene, no vintage sepia, no messy clutter, no cropped or cut-off labels, no slow boring motion, no low-res look, no voiceover, no narration, no human speech, no misspelled words, no extra text, no logos.
```

## 4 · Notas de producción
- Mati graba a cámara (registro de su video de las 3 carteras: didáctico,
  numerado, calmo). Gráficos: cards estilo Premium Data Motion, paleta
  financiera (verde/rojo) coherente con su feed.
- **Cumplimiento (regla de Ale 2026-07-06): NO se dan estimaciones de
  rendimiento** — ni en narración ni en gráficos. La única evidencia
  permitida son los **resultados reales ya ocurridos** (la captura). El
  punch se apoya en eso: "no te lo puedo prometer / te lo puedo mostrar".
- Nombres técnicos de los bonos (TXMJ0, TXMJ8, TMF27, T31Y7): NO se dicen
  en la narración (muy nicho); pueden ir en el gráfico BR3 como detalle.
