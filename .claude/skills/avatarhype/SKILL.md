---
name: avatarhype
description: >-
  Metodología EXACTA del curso AvatarHype™ para producir anuncios UGC con
  avatares de IA hiperrealistas para e-commerce, por la ruta barata (Kie.ai /
  APImart, Veo 3.1 / Omni Flash, GPT Image 2 / Nano Banana, ElevenLabs, CapCut).
  Cubre el flujo de 6 pasos, el método de prompt de 14 bloques ("6C"), los
  formatos (UGC, podcast, voz en off, dualcast, ads en imagen) y la capa de
  realismo. Úsala cuando se pidan anuncios UGC de producto, "estilo AvatarHype",
  ads con avatar de IA, o recrear un trend viral para vender.
---

# 🎯 AvatarHype — UGC ads con avatares de IA (método del curso)

> Porte fiel de **`docs/SISTEMA-AVATARHYPE.md`** (fuente de verdad elegida por Ale)
> y de los prompts verbatim en `docs/recursos-prompts/`. NO inventar pasos ni
> valores: si algo no está en esas fuentes, marcarlo. Para máxima exactitud de un
> prompt, abrir el archivo verbatim que se referencia en cada sección.

## Tesis central del curso (no olvidar nunca)
> "El UGC con IA no va sobre una herramienta concreta. La diferencia entre un
> anuncio que revienta y uno mediocre está únicamente en la **creatividad (ángulo
> + guion)**, no en el modelo de vídeo."

Segunda idea: **no depender de una sola herramienta/modelo.** Montar varias
"rutas" intercambiables; si una API se satura o un modelo cierra (le pasó a Sora),
saltar a otra. Objetivo de coste: **0,07–0,16 € por clip** de vídeo · **0,012 €**
por imagen.

## Stack / rutas (capas intercambiables)
| Capa | Herramienta | Para qué |
|---|---|---|
| Marketplace API 1 | **Kie.ai** | vídeo (Sora 2 ❌ cerrado) e imagen |
| Marketplace API 2 | **APImart** | vídeo (**Veo 3.1**, **Omni Flash**, Kling) e imagen (GPT Image 2, Nano Banana Pro) |
| Imagen económica | **GPT Image 2** | avatares/escenas/frames — ~90 img/€ (0,012 €) |
| Imagen calidad | **Nano Banana Pro** | avatares, productos, frames |
| Voz en off | **ElevenLabs** | audio narrado |
| Edición | **CapCut** | montaje + capa de realismo + subtítulos |
| Música/SFX | **Epidemic Sound** + biblioteca AvatarHype | sin copyright |
| Inspiración | **Pinterest / TikTok / Instagram** | avatares, escenas, trends |
| Frames de trend | descargador TikTok + frame extractor | recrear un trend |

**Modelo de vídeo recomendado (lo más actual):** **Omni Flash** (Gemini, Vol. 4) >
Veo 3.1. Mejor español de España + acentos LATAM, clips 4/6/8/10 s al mismo coste.
Sora 2 quedó obsoleto (Vol. 1).

## Flujo central de 6 pasos (vale para todos los formatos)
```
1. ÁNGULO + GUION  → producto → público, pain points, ángulo, guion
2. INSPIRACIÓN     → Pinterest/TikTok/IG (captura de un avatar/escena real)
3. IMÁGENES        → GPT Image 2 / Nano Banana (avatar, producto, frame inicial y final)
4. VÍDEO           → Veo 3.1 / Omni Flash (prompt 14 bloques = cámara+microacción+guion+voz+acento)
5. EDICIÓN         → CapCut (cortar, entrelazar, música, SFX, textos, capa de realismo)
6. PUBLICAR        → anuncio listo
```

## Método de prompt de VÍDEO — 14 bloques ("6C")
Estructura EXACTA (plantilla verbatim y copiable en
[`docs/recursos-prompts/plantilla_prompts_veo_3_1.md`](../../../docs/recursos-prompts/plantilla_prompts_veo_3_1.md)):
1. **Formato y tipo** — `9:16, iPhone front-camera selfie, handheld, hyper-realistic UGC, not cinematic`
2. **Identidad del personaje** — "the exact same person from the reference images; identity/face/skin texture/hair/outfit must match perfectly"
3. **Entorno** — lugar, hora, luz, ambiente (concreto)
4. **Acción principal** — 1 acción + 1 microacción (no 5 acciones en 8 s)
5. **Física humana** — definir qué es "natural": microshake, respiración, rebote vertical, sway, micro-movimientos no repetitivos
6. **Idioma y forma de hablar** — forzar español de España (filler "a ver…", "es que…"; "Not Latin American Spanish")
7. **Tono emocional** — calm / confident / casual / **not selling / not performing**
8. **Script** — corto, fácil de pronunciar, pensado para 8 s
9. **Comportamiento** — empieza mid-thought, parpadea, pausas, mira fuera de cámara, se recoloca
10. **Cámara** — handheld, off-center, autofocus shifts, rolling shutter, no stabilization
11. **Luz** — natural, exposición que cambia, sombras suaves (la luz perfecta mata el UGC)
12. **Audio** — micrófono crudo de iPhone, ruido ambiente, respiración, sin música
13. **Negative prompt** — studio lighting, beauty filter, perfect skin, ad-like polish, robotic delivery…
14. **Start frame / End frame** — si hay referencias, guía la transición entre los dos estados

> **Truco español de España:** bloque de idioma + meter una palabra muy de España
> al inicio ("joder", "tía", "tío") que se corta en edición. Con **Omni Flash** casi
> no hace falta y se pueden hacer acentos argentino/colombiano/mexicano.
> Prompts cortos de referencia (cambiar avatar, reemplazar fondo, plano cercano,
> talking-head, podcast flip) en
> [`docs/recursos-prompts/prompts_referencia_visual.md`](../../../docs/recursos-prompts/prompts_referencia_visual.md).

## Formatos (qué produce cada uno)
- **UGC tradicional:** un avatar habla a cámara + imágenes superpuestas (periódico, comparativas).
- **Podcast:** dos avatares (el 2º se genera con "Flip the image horizontally"), cámara estática, se entrelazan clips cortos en edición. Single speaker por clip.
- **UGC voz en off:** audio con **ElevenLabs** + varios clips montados encima.
- **Dualcast (Vol. 4):** dos personas a cámara interactuando; dos prompts base ("habla izquierda, derecha asiente" y viceversa); se entrelazan clips cortos.
- **Ads en imagen (Vol. 3):** GPT Image 2 (2K, 4:5 o 9:16). Formatos: Comparativa · Before/After · Testimonial · Problema-solución · Fake-news · Advertorial · Reddit · WhatsApp · Timeline · Oferta · Características. Plantillas verbatim (testimonial + before/after) en [`docs/recursos-prompts/ads_imagen.md`](../../../docs/recursos-prompts/ads_imagen.md).
- **Trends virales:** descargar un TikTok trend → sacar frames → recrearlos con IA → animar antes/después/producto. Flujo en [`docs/recursos-prompts/trends_virales_ads.md`](../../../docs/recursos-prompts/trends_virales_ads.md).

## Capa de realismo en CapCut (se aplica SIEMPRE, valores verbatim)
El toque que hace que parezcan reales. Guardar como "ajuste personalizado" y
reaplicar a todos los clips.

**Ajuste Vol. 1 (rápido):** Disposición/temperatura ~+3 · Contraste −7 · Partículas 10% · Motion blur 20% (clip a clip).

**Ajuste Vol. 2 (el bueno):**
```
Temperatura: -3 · Tinte: +2 · Saturación: -6 · Exposición: -3 · Contraste: +12
Highlights: -35 · Sombras: -18 · Fade: +6
```

## Agentes GPT propios del curso (referencia)
- Scripts 3 Formatos (producto → 3 guiones) · Prompts método 6C (captura Pinterest → prompt 14 bloques). Enlaces en `docs/SISTEMA-AVATARHYPE.md` §4.

## Reglas inmutables
1. La creatividad (ángulo+guion) manda sobre el modelo.
2. Siempre 9:16, look UGC NO cinematográfico, NO ad-like.
3. 1 acción + 1 microacción por clip de 8 s.
4. Definir "natural" explícitamente (física humana) — el fallo nº1 es el movimiento falso.
5. Idioma forzado (acento correcto); tono "not selling, not performing".
6. Negative prompt siempre. · Capa de realismo siempre.
7. Multi-ruta: si una API/modelo falla, saltar a otra (no quedarse bloqueado).

## Anti-patrones
Meter 5 acciones en 8 s · decir solo "natural" sin definirlo · luz de estudio /
piel perfecta / pulido de anuncio · acento latino cuando se pidió España · olvidar
el negative prompt o la capa de realismo · depender de un solo modelo.

## Notas honestas (entorno / fuentes)
- El curso es **manual** (Pinterest → ChatGPT → APImart → CapCut). La automatización
  (APIs REST, n8n, ffmpeg) es el "desarrollo propio" que vive en `avatarhype/` (Python),
  NO es el método del curso.
- Para detalles que solo se ven en los vídeos, consultar `docs/transcripciones/`.
- AvatarHype apunta a **anuncios UGC de producto** (e-commerce). Para reels
  educativos de Cerebro, el pipeline es el de las skills `*-cerebro`.
