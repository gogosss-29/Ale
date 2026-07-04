# reel-003 · Prompts de Omni (edición por compositing)

> Método: skill `omni-reels`. Editar los 7 clips de avatar del reel-003 animando
> motion graphics ENCIMA, sin que Omni toque la voz ni el personaje.
> Reel: **"3 señales de que tu negocio no está estructurado"** · español argentino · 9:16.

## ⚠️ Tiempos
Los `~Xs` de cada prompt están **estimados del guion** (texto + duración real de
cada clip). Para clavarlos, correr `reel_cutter.py` sobre cada clip y tomar los
segundos de `segments.json` (necesita ffmpeg + faster-whisper; no disponible en el
entorno remoto). Si un gráfico cae 0.3–0.5 s corrido, ajustar el segundo.

---

## Plan maestro — sistema visual (FIJO en los 7 clips)

- **Composición:** el sujeto está **centrado** (sentado, fondo naranja). Por eso los
  gráficos van en la **banda superior** y en **lower-thirds**, **nunca sobre la cara
  ni el centro**. Pill de sección arriba-izquierda; título arriba; tags abajo.
- **Colores por NOMBRE (nunca hex):**
  - **gold / dorado** = pills y títulos de sección (marca Cerebro).
  - **alert red / rojo** = el problema o dolor de cada señal.
  - **bright green / verde** = la resolución (cierre).
  - texto **off-white**; acentos de fondo **charcoal/graphite**.
- **Física de animación:** entradas *ease-out-back* con overshoot, salidas *ease-in*,
  motion blur suave, glow tenue, glassmorphism leve. Diagramas que se dibujan solos.
- **Tokens recurrentes:** una pill de sección dorada, **UN** título por clip, un bug
  de marca **"CEREBRO"** chico que aparece en el hook y reaparece en el cierre/CTA.
- **Safe zones:** nada importante en el 10% superior ni el 15% inferior; nada sobre
  el rostro (centro del cuadro).
- **Cámara:** un lento push-in continuo del 3% en cada clip.

### Mapa de beats (un foco por clip)
| Clip | Dur | Foco único | Gráfico central |
|---|---|---|---|
| C1 HOOK | 6s | Enganchar | Título "3 SEÑALES" + bug de marca |
| C2 Señal 1 | 8s | Dependés de personas | Cabeza con el conocimiento adentro que se apaga |
| C3 Señal 2 | 8s | Sin objetivos | Diana vacía con "?" + camino sin rumbo |
| C4 Señal 2b | 8s | Dependés del contexto | Flecha "CONTEXTO" que zarandea el camino |
| C5 Señal 3 | 8s | ¿Ganás o facturás? | Barras FACTURACIÓN ↑ vs línea GANANCIA plana |
| C6 CIERRE | 6s | Resolución | Módulos que pasan a verde |
| C7 CTA | 4s | Seguime | Handle de marca + ícono seguir |

---

## Preámbulo benigno (encabeza TODOS los prompts)

```
This is my own video of myself that I want to enhance with motion-graphic overlays. Keep my original footage and its audio exactly as they are — do not modify the video of me, the background or the lighting, and do not change the sound of my voice or my speech in any way. Only add new graphics, titles and sound effects composited on top, like overlay layers in a video editor. Keep me visible the whole time.
```

---

## C1 · HOOK (6 s)
Locución: *"Hay tres señales claras de que un negocio no está estructurado, te las muestro una por una."*

```
This is my own video of myself that I want to enhance with motion-graphic overlays. Keep my original footage and its audio exactly as they are — do not modify the video of me, the background or the lighting, and do not change the sound of my voice or my speech in any way. Only add new graphics, titles and sound effects composited on top, like overlay layers in a video editor. Keep me visible the whole time.

Goal: a clean, premium opening beat for a vertical business/finance reel (9:16, 1080p) in Argentine Spanish. I am seated and centered, so keep all graphics in the upper band and lower third, never over my face or the center of the frame. Do not add subtitles. The only number allowed on screen is "3"; do not add any other numbers. Never display any color code, hex value or technical text on screen.

Style and timing: At ~0.4s fade in a small gold brand bug "CEREBRO" in the lower-left corner. At ~0.8s pop in a large gold title upper area "3 SEÑALES" (heavy condensed uppercase, ease-out-back overshoot, soft glow, one light-sweep). At ~2.2s slide a slim off-white subtitle under it "TU NEGOCIO NO ESTÁ ESTRUCTURADO". Camera: a slow continuous 3% push-in. Keep everything inside the safe zones.

Sound effects (added softly as separate quiet layers under my original voice, no music, without changing my voice): a soft whoosh at ~0.8s; a light tick at ~2.2s. Do not add any music.

Constraints: 9:16, 1080p, Argentine Spanish on-screen text with no spelling errors; keep my original video, background and voice unchanged and keep me visible throughout; the only on-screen text is "CEREBRO", "3 SEÑALES", "TU NEGOCIO NO ESTÁ ESTRUCTURADO".
```

---

## C2 · SEÑAL 1 (8 s)
Locución: *"La primera: el conocimiento vive en la cabeza de las personas, no en el negocio. Si mañana esa persona importante no está, nadie sabe cómo seguir."*

```
This is my own video of myself that I want to enhance with motion-graphic overlays. Keep my original footage and its audio exactly as they are — do not modify the video of me, the background or the lighting, and do not change the sound of my voice or my speech in any way. Only add new graphics, titles and sound effects composited on top, like overlay layers in a video editor. Keep me visible the whole time.

Goal: a clean, premium beat for a vertical business/finance reel (9:16, 1080p) in Argentine Spanish. I am seated and centered, so keep all graphics in the upper band and lower third, never over my face or the center of the frame. Do not add subtitles. Do not add any numbers. Never display any color code, hex value or technical text on screen.

Style and timing: At ~0.3s bring up a small gold pill upper-left "SEÑAL 1" (ease-out-back). At ~1.0s a gold title beside/under it "EL CONOCIMIENTO EN LAS CABEZAS" (heavy condensed uppercase, soft glow). At ~2.5s draw a clean off-white line-icon of a human head with small connected knowledge nodes inside it, upper-right, drawing itself on. At ~5.0s the head icon dims to charcoal and a single alert-red "?" appears over it (person gone, nobody knows). Camera: a slow continuous 3% push-in. Keep everything inside the safe zones.

Sound effects (added softly as separate quiet layers under my original voice, no music, without changing my voice): a soft pop at ~0.3s; a light draw-on sweep at ~2.5s; a subtle alert at ~5.0s. Do not add any music.

Constraints: 9:16, 1080p, Argentine Spanish on-screen text with no spelling errors; keep my original video, background and voice unchanged and keep me visible throughout; the only on-screen text is "SEÑAL 1", "EL CONOCIMIENTO EN LAS CABEZAS".
```

---

## C3 · SEÑAL 2 (8 s)
Locución: *"La segunda: no se trabaja sobre objetivos, se lleva el día a día. No hay objetivos propios planificados en un plan de acción."*

```
This is my own video of myself that I want to enhance with motion-graphic overlays. Keep my original footage and its audio exactly as they are — do not modify the video of me, the background or the lighting, and do not change the sound of my voice or my speech in any way. Only add new graphics, titles and sound effects composited on top, like overlay layers in a video editor. Keep me visible the whole time.

Goal: a clean, premium beat for a vertical business/finance reel (9:16, 1080p) in Argentine Spanish. I am seated and centered, so keep all graphics in the upper band and lower third, never over my face or the center of the frame. Do not add subtitles. Do not add any numbers. Never display any color code, hex value or technical text on screen.

Style and timing: At ~0.3s bring up a small gold pill upper-left "SEÑAL 2" (ease-out-back). At ~1.0s a gold title "SIN OBJETIVOS" (heavy condensed uppercase, soft glow). At ~2.5s draw an off-white dashed target/bullseye upper-right that is EMPTY, with a small alert-red "?" in its center (no goal set). At ~5.0s a thin off-white path line wanders left-to-right without direction, drifting up and down. Camera: a slow continuous 3% push-in. Keep everything inside the safe zones.

Sound effects (added softly as separate quiet layers under my original voice, no music, without changing my voice): a soft pop at ~0.3s; a light draw-on at ~2.5s; a subtle wobble as the path drifts at ~5.0s. Do not add any music.

Constraints: 9:16, 1080p, Argentine Spanish on-screen text with no spelling errors; keep my original video, background and voice unchanged and keep me visible throughout; the only on-screen text is "SEÑAL 2", "SIN OBJETIVOS".
```

---

## C4 · SEÑAL 2b (8 s)
Locución: *"Y sin objetivos propios, dependés solo del contexto externo: si a la economía del país le va bien, te va bien. Si no, no."*

```
This is my own video of myself that I want to enhance with motion-graphic overlays. Keep my original footage and its audio exactly as they are — do not modify the video of me, the background or the lighting, and do not change the sound of my voice or my speech in any way. Only add new graphics, titles and sound effects composited on top, like overlay layers in a video editor. Keep me visible the whole time.

Goal: a clean, premium beat for a vertical business/finance reel (9:16, 1080p) in Argentine Spanish. I am seated and centered, so keep all graphics in the upper band and lower third, never over my face or the center of the frame. Do not add subtitles. Do not add any numbers. Never display any color code, hex value or technical text on screen.

Style and timing: At ~0.3s keep a small gold pill upper-left "SEÑAL 2". At ~1.0s a bold gold line-arrow labeled "CONTEXTO" enters from the right edge and shoves a thin off-white path line upward, then downward, erratically (external force). At ~4.5s an alert-red tag snaps in lower area "A LA DERIVA" with motion blur. Camera: a slow continuous 3% push-in. Keep everything inside the safe zones.

Sound effects (added softly as separate quiet layers under my original voice, no music, without changing my voice): a whoosh as the CONTEXTO arrow shoves at ~1.0s; a snap on the tag at ~4.5s. Do not add any music.

Constraints: 9:16, 1080p, Argentine Spanish on-screen text with no spelling errors; keep my original video, background and voice unchanged and keep me visible throughout; the only on-screen text is "SEÑAL 2", "CONTEXTO", "A LA DERIVA".
```

---

## C5 · SEÑAL 3 (8 s)
Locución: *"La tercera: no sabés si tu negocio gana o solo factura, sin tus números manejás por intuición, y la intuición miente."*

```
This is my own video of myself that I want to enhance with motion-graphic overlays. Keep my original footage and its audio exactly as they are — do not modify the video of me, the background or the lighting, and do not change the sound of my voice or my speech in any way. Only add new graphics, titles and sound effects composited on top, like overlay layers in a video editor. Keep me visible the whole time.

Goal: a clean, premium beat for a vertical business/finance reel (9:16, 1080p) in Argentine Spanish. I am seated and centered, so keep all graphics in the upper band and lower third, never over my face or the center of the frame. Do not add subtitles. Do not add any numbers. Never display any color code, hex value or technical text on screen.

Style and timing: At ~0.3s bring up a small gold pill upper-left "SEÑAL 3" (ease-out-back). At ~1.0s a gold title "¿GANÁS O SOLO FACTURÁS?" (heavy condensed uppercase, soft glow). At ~2.5s in the upper-right, tall off-white bars labeled "FACTURACIÓN" rise quickly while a flat alert-red line labeled "GANANCIA" stays pinned near the bottom; a red arrow points to the gap. At ~5.5s an alert-red tag snaps in lower area "LA INTUICIÓN MIENTE". Camera: a slow continuous 3% push-in. Keep everything inside the safe zones.

Sound effects (added softly as separate quiet layers under my original voice, no music, without changing my voice): a soft pop at ~0.3s; rising ticks as the bars grow at ~2.5s; a snap on the tag at ~5.5s. Do not add any music.

Constraints: 9:16, 1080p, Argentine Spanish on-screen text with no spelling errors; keep my original video, background and voice unchanged and keep me visible throughout; the only on-screen text is "SEÑAL 3", "¿GANÁS O SOLO FACTURÁS?", "FACTURACIÓN", "GANANCIA", "LA INTUICIÓN MIENTE".
```

---

## C6 · CIERRE (6 s)
Locución: *"Antes de crecer, hay que entender. Conocer de verdad tu propio negocio es el camino inicial para crecer."*

```
This is my own video of myself that I want to enhance with motion-graphic overlays. Keep my original footage and its audio exactly as they are — do not modify the video of me, the background or the lighting, and do not change the sound of my voice or my speech in any way. Only add new graphics, titles and sound effects composited on top, like overlay layers in a video editor. Keep me visible the whole time.

Goal: a clean, premium resolution beat for a vertical business/finance reel (9:16, 1080p) in Argentine Spanish. I am seated and centered, so keep all graphics in the upper band and lower third, never over my face or the center of the frame. Do not add subtitles. Do not add any numbers. Never display any color code, hex value or technical text on screen.

Style and timing: At ~0.3s show three small off-white module chips in the upper band "EQUIPO", "OBJETIVOS", "NÚMEROS", each starting outlined in alert-red. Between ~0.6s and ~2.2s each chip turns bright green one by one (problem resolved). At ~2.5s a gold title appears "CONOCÉ TU NEGOCIO" (heavy condensed uppercase, soft glow). At ~4.0s the small gold brand bug "CEREBRO" fades in lower-left. Camera: a slow continuous 3% push-in. Keep everything inside the safe zones.

Sound effects (added softly as separate quiet layers under my original voice, no music, without changing my voice): a soft positive chime as each chip turns green (~0.6s, ~1.4s, ~2.2s); a gentle rise under the title at ~2.5s. Do not add any music.

Constraints: 9:16, 1080p, Argentine Spanish on-screen text with no spelling errors; keep my original video, background and voice unchanged and keep me visible throughout; the only on-screen text is "EQUIPO", "OBJETIVOS", "NÚMEROS", "CONOCÉ TU NEGOCIO", "CEREBRO".
```

---

## C7 · CTA (4 s)
Locución: *"Seguime que te ayudo con tu negocio."*

```
This is my own video of myself that I want to enhance with motion-graphic overlays. Keep my original footage and its audio exactly as they are — do not modify the video of me, the background or the lighting, and do not change the sound of my voice or my speech in any way. Only add new graphics, titles and sound effects composited on top, like overlay layers in a video editor. Keep me visible the whole time.

Goal: a clean, premium call-to-action beat for a vertical business/finance reel (9:16, 1080p) in Argentine Spanish. I am seated and centered, so keep all graphics in the upper band and lower third, never over my face or the center of the frame. Do not add subtitles. Do not add any numbers. Never display any color code, hex value or technical text on screen.

Style and timing: At ~0.3s bring up a gold pill in the lower third "SEGUIME" (ease-out-back overshoot, soft glow) next to a clean off-white "follow" plus-icon that pulses once at ~1.2s. At ~0.5s the small gold brand bug "CEREBRO" fades in lower-left. Camera: a slow continuous 3% push-in. Keep everything inside the safe zones.

Sound effects (added softly as separate quiet layers under my original voice, no music, without changing my voice): a soft pop at ~0.3s; a light UI blip on the follow-icon pulse at ~1.2s. Do not add any music.

Constraints: 9:16, 1080p, Argentine Spanish on-screen text with no spelling errors; keep my original video, background and voice unchanged and keep me visible throughout; the only on-screen text is "SEGUIME", "CEREBRO".
```

---

## Checklist antes de mandar a Omni (por clip)
- [ ] Preámbulo benigno arriba (sin "clone/lip-sync/bit-for-bit").
- [ ] Todos los cues por tiempo (cero "when I say"). Afinar los ~s con `segments.json`.
- [ ] Ningún código hex (colores por nombre).
- [ ] Lista blanca de texto + bloqueo de números no dichos (solo "3" en C1).
- [ ] "No music" (la música se suma al final).
- [ ] Tras generar: verificar voz (correlación banda 300–3400 Hz) y **upscalar** 720p→1080p.
