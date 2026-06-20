# 3 señales de que tu negocio no está estructurado
Marca: Cerebro · Educativo (info+experiencia+resolución) · ~49s · 9:16 · Estado: APROBADO (contenido)
Ángulo y sustancia: aportados por Ale. Escenario sugerido: estudio naranja (ref-01.jpg).

## 1 · GUIÓN COMPLETO (avatar · voz propia) — secciones de 10s

[0:00–0:10] **HOOK** — "Hay tres señales claras de que un negocio no está estructurado. Te las muestro una por una." *(17 · 6,1s)*
[0:10–0:20] **SEÑAL 1** — "La primera: el conocimiento vive en la cabeza de las personas, no en el negocio. Si mañana esa persona importante no está, nadie sabe cómo seguir." *(26 · 9,3s)*
[0:20–0:30] **SEÑAL 2** — "La segunda: no se trabaja sobre objetivos, se lleva el día a día. No hay objetivos propios planificados en un plan de acción." *(23 · 8,2s)*
[0:30–0:40] **SEÑAL 2** — "Y sin objetivos propios, dependés solo del contexto externo: si a la economía del país le va bien, te va bien. Si no, no." *(24 · 8,6s)*
[0:40–0:50] **SEÑAL 3** — "La tercera: no sabés si tu negocio gana o solo factura. Sin tus números, manejás por intuición. Y la intuición miente." *(21 · 7,5s)*
[0:50–1:00] **CIERRE** — "Antes de crecer, hay que entender. Conocer de verdad tu propio negocio es el camino inicial para crecer." *(18 · 6,4s)*
[1:00–1:10] **CTA** — "Seguime que te ayudo con tu negocio." *(7 · 2,5s)*

## 2 · Locución SIN COMAS (para Omni)
```
S1  Hay tres señales claras de que un negocio no está estructurado te las muestro una por una
S2  La primera el conocimiento vive en la cabeza de las personas no en el negocio si mañana esa persona importante no está nadie sabe cómo seguir
S3  La segunda no se trabaja sobre objetivos se lleva el día a día no hay objetivos propios planificados en un plan de acción
S4  Y sin objetivos propios dependés solo del contexto externo si a la economía del país le va bien te va bien si no no
S5  La tercera no sabés si tu negocio gana o solo factura sin tus números manejás por intuición y la intuición miente
S6  Antes de crecer hay que entender conocer de verdad tu propio negocio es el camino inicial para crecer
S7  Seguime que te ayudo con tu negocio
```

## 3 · PROMPTS DE AVATAR (escenario naranja · frontal de estudio · ref-01.jpg)

**Plantilla maestra (FIJA en los 7 clips):**
```
A hyper-realistic 9:16 vertical video. Clean studio look, photorealistic, natural real skin (not over-polished).
[CHARACTER] The exact same man from the provided reference image. Identity, face, teeth, skin, hair, body and outfit must match the reference perfectly. Do not beautify, slim or alter him.
[ENVIRONMENT] Sitting on the wooden-top metal bar stool against a smooth solid orange seamless studio background, exactly like the reference image. Centered, headroom above.
[HUMAN MOTION] Subtle natural motion: breathing, small head movements, restrained hand gestures, non-repetitive micro-movements. Calm, not stiff.
[LANGUAGE] Authentic Argentine Spanish (Río de la Plata accent), natural rhythm. Not Spain Spanish, not neutral Latin.
[TONE] Calm, authoritative, educational. Not selling, not performing.
[BEHAVIOUR] Starts slightly mid-thought, blinks, small pauses. Relaxed, mostly closed mouth — minimal teeth, no wide opening, no smile.
[CAMERA] Fixed frontal camera at eye level, straight on, tripod. No selfie, no handheld, no extreme angles. Framing: [FRAMING].
[ACTION] [ACTION]
[LIGHTING] Soft even studio light, natural skin, soft shadows.
[AUDIO] Clean natural voice, quiet room tone, subtle breathing, no music.
[NEGATIVE] beauty filter, perfect white teeth, plastic skin, ad-like polish, exaggerated gestures, robotic delivery, flicker, Spain accent, neutral latino accent, wide open mouth, teeth-baring, big toothy smile, changing the orange background, changing the stool, selfie arm.
[SCRIPT] "[SCRIPT]"
```
Cargá `ref-01.jpg` en cada clip. Como es un solo ambiente, también podés usar Modo A ("continua la grabación") para los clips 2-7.

**⚠️ DURACIÓN POR CLIP (generá en esta duración, NO 10s por defecto):**
C1 HOOK 17pal → **6s** · C2 SEÑAL 1 26pal → **8s** · C3 SEÑAL 2 23pal → **8s** · C4 SEÑAL 2 24pal → **8s** · C5 SEÑAL 3 21pal → **8s** · C6 CIERRE 18pal → **6s** · C7 CTA 7pal → **4s**. (Si un clip sale apurado o repite, ver la regla de buckets en `director-avatar-omni.md`.)

| # · Función | [FRAMING] | [ACTION] | [SCRIPT] (sin comas) |
|---|---|---|---|
| 1 · HOOK | medium-close | mira fijo, gesto contenido con una mano | Hay tres señales claras de que un negocio no está estructurado te las muestro una por una |
| 2 · SEÑAL 1 | medium | gesto explicativo con una mano | La primera el conocimiento vive en la cabeza de las personas no en el negocio si mañana esa persona importante no está nadie sabe cómo seguir |
| 3 · SEÑAL 2 | medium | marca "la segunda" con la mano | La segunda no se trabaja sobre objetivos se lleva el día a día no hay objetivos propios planificados en un plan de acción |
| 4 · SEÑAL 2 | medium-close | gesto firme, mirada directa | Y sin objetivos propios dependés solo del contexto externo si a la economía del país le va bien te va bien si no no |
| 5 · SEÑAL 3 | close | mirada firme, sentencioso en "la intuición miente" | La tercera no sabés si tu negocio gana o solo factura sin tus números manejás por intuición y la intuición miente |
| 6 · CIERRE | medium-close | gesto abierto, más calmo | Antes de crecer hay que entender conocer de verdad tu propio negocio es el camino inicial para crecer |
| 7 · CTA | medium | leve apertura de manos invitando | Seguime que te ayudo con tu negocio |

## 4 · B-rolls + música
- B-rolls (~50%): Señal 1 → conocimiento encerrado (caja/llave, #05) · Señal 2 → brújula/horizonte sin rumbo (#05) · Señal 3 → **informativo** (Estado de Resultados / "ganar vs facturar", #06). Detalle de estilos: `../../.claude/skills/cerebro-guiones/references/brolls-biblioteca.md`.
- Música: brief Suno/Udio (cinematic minimal, ducking bajo la voz).

