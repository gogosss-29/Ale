# 📋 Sistema Avatar IA — Documento operativo (listo para Notion)

> **Propósito:** punto de entrada único para que **cualquier IA o persona** se conecte,
> entienda el sistema y lo use de inmediato. Documento autocontenido. Las fuentes
> completas viven en el repo `gogosss-29/Ale` (carpetas `docs/`, `avatarhype/`, `cerebro/`).
>
> _Pega este documento en Notion como página principal del proyecto "Sistema Avatar IA"._

---

## 1. Qué es este sistema
Producir **avatares de IA hiperrealistas que hablan**, para anuncios de e-commerce y
contenido (UGC, podcast, voz en off, dualcast, image-ads). Objetivo: realismo que pasa
desapercibido, al menor coste posible.

**Principio del curso:** la diferencia entre un anuncio que revienta y uno mediocre está
en **el ángulo + el guion (la creatividad)**, no en el modelo de vídeo. No depender de una
sola herramienta.

## 2. Dos rutas (decisión estratégica pendiente)
| Ruta | Herramientas | Fuerte en | Coste |
|---|---|---|---|
| **A — Curso (AvatarHype)** | Kie.ai / APImart → Veo 3.1, **Omni Flash**, GPT Image 2; ElevenLabs; CapCut | Volumen barato, muchos formatos, prompts probados | ~0,07–0,16 €/clip · 0,012 €/img |
| **B — Higgsfield** (lo ejecutado aquí) | Higgsfield Soul + voz + Seedance/Veo | Identidad consistente (digital twin), todo integrado | mayor, plan Plus |

> **Recomendación:** Higgsfield (B) para fijar la **identidad/Soul** y para el vídeo hablado
> de Alexander; ruta del curso (A) para **producir volumen** de anuncios barato. Se pueden
> combinar. Decidir al estandarizar el pipeline.

## 3. El flujo de 6 pasos (vale para ambas rutas)
```
1. ÁNGULO + GUION   → producto → público, pain points, ángulo, guion (agente GPT del curso)
2. INSPIRACIÓN      → Pinterest/TikTok/IG (captura de un avatar/escena real)
3. IMÁGENES         → GPT Image 2 / Nano Banana Pro (ruta A) · Soul v2 (ruta B)
4. VÍDEO            → Veo 3.1 / Omni Flash (ruta A) · Seedance/Veo + audio (ruta B)
5. EDICIÓN          → CapCut: cortar, entrelazar, música, textos, CAPA DE REALISMO
6. PUBLICAR
```

### Capa de realismo en CapCut (aplicar SIEMPRE) — ajuste de color del curso
```
Temperatura: -3 · Tinte: +2 · Saturación: -6 · Exposición: -3 · Contraste: +12
Highlights: -35 · Sombras: -18 · Fade: +6
```

## 4. Prompts clave (copy-paste)

### 4.1 Plantilla maestra de vídeo (14 bloques resumidos) — ruta A (Veo/Omni)
```
A hyper-realistic 9:16 handheld iPhone front-camera selfie video.

[CHARACTER] The exact same [man/woman] from the reference images. Identity, face, skin
texture, hair, outfit must match perfectly.
[GOAL] Maximum realism. Real casual UGC selfie, not AI-generated.
[ENVIRONMENT] [lugar, luz, hora, fondo; luz natural imperfecta, no cinematográfico]
[ACTION] [1 acción principal + 1 microacción] while speaking naturally to camera.
[HUMAN MOTION] natural: slight vertical bounce, sway, shoulder movement, inconsistent
micro-movements, breathing affecting motion/speech.
[LANGUAGE] authentic Castilian Spanish from Spain, natural rhythm, slight hesitations,
informal cadence. Not Latin American Spanish. Fillers: "a ver…", "es que…".
[TONE] [calm / confident / casual / not selling / not performing]
[SCRIPT] "[guion corto, para 8 s]"
[BEHAVIOUR] starts mid-thought, blinks, brief glance away, small pauses, subtle facial motion.
[CAMERA] handheld iPhone selfie, off-center, natural micro-shake, minor autofocus shifts,
rolling shutter, no stabilization.
[LIGHTING] natural daylight only, slight exposure changes, soft uneven shadows.
[AUDIO] raw phone microphone, light ambient noise, natural breathing, no music.
[NEGATIVE] studio lighting, beauty filter, perfect skin, ad-like polish, exaggerated
gestures, robotic delivery, over-sharpening, artificial background, unnatural motion, flicker.
[START/END FRAME] [si hay 2 referencias, describe la transición]
```
> Versión completa con explicación bloque a bloque: `docs/recursos-prompts/plantilla_prompts_veo_3_1.md`

### 4.2 Prompts de imagen (referencia visual)
```
CAMBIAR AVATAR:   make this woman/man a different one, [descripción, outfit...]
REEMPLAZAR FONDO: replace the guy from file 1 with the guy from file 2 wearing the same
                  outfit as file 2, he is talking to camera gesticulating
PLANO CERCANO:    A closer view of this same image shows less countertop. He's talking to
                  the camera, you can see his teeth well
PODCAST (2º avatar): Flip the image horizontally  /  looking to the right side of the frame
```

### 4.3 Prompt del vídeo hablado en Higgsfield (ruta B, el de Alexander)
```
The man speaks directly to the camera in a natural, relaxed way, lips perfectly
synchronized with the provided voice audio, subtle natural head movements and blinking,
soft neutral indoor lighting, steady camera, realistic
```
> Más plantillas: `docs/recursos-prompts/` (ads_imagen, trends_virales_ads).

## 5. Truco del español de España
Los modelos tiran a inglés/español latino. Forzar peninsular con el bloque [LANGUAGE] +
una palabra muy de España al inicio del guion ("joder", "tía") que luego se corta en edición.
Con **Omni Flash** (Vol. 4) ya casi no hace falta y permite acentos LATAM (argentino, etc.).

## 6. Activos vivos de Alexander (Higgsfield)
| Elemento | ID |
|---|---|
| Soul "Alexander v2" (USAR) | `9ffc9c16-eeb2-465d-b2b5-03a7b14a227d` |
| Retrato base v2 | `43c9b6e8-e08c-47af-b8b7-94b61bae1b2e` |
| Voz clip 12 s | `41bd653e-a16f-4089-baea-60cbcfba1d18` |
| Voz completa 3:27 | `efc51158-010b-4a2f-ae28-a9b1d4026f90` |

Generar imagen: `generate_image` model `soul_2` + `soul_id`. Vídeo: `generate_video`
model `seedance_2_0`, start_image=retrato, audio=clip 12 s, 9:16, 12 s, 720p.

## 7. Mapa del repo (fuente de verdad)
- `docs/SISTEMA-AVATARHYPE.md` — sistema completo del curso (leer entero).
- `docs/recursos-prompts/` — todas las bibliotecas de prompts.
- `docs/transcripciones/` — 4 lecciones transcritas (referencia).
- `avatarhype/` — pipeline en Python para automatizar.
- `cerebro/` — este brain (índice, playbook, activos, estado).

## 8. Enlaces del curso
- Kie.ai · APImart (`apimart.ai`) — marketplaces de APIs baratas.
- Agentes GPT propios (en `docs/notas-lecciones/` y `docs/SISTEMA-AVATARHYPE.md §4`).
- Biblioteca del alumno: `avatarhype.online/alumnos`.

## 9. Estado y próximos pasos
- ✅ Soul v2, voz, retratos, curso documentado, cerebro en repo.
- 🔜 Generar el vídeo hablado (en sesión interactiva: `generate_video` se aprueba ahí).
- 🔜 Decidir ruta A/B/combinada y **automatizar el pipeline** (n8n + APIs + Higgsfield),
  ver `docs/SISTEMA-AVATARHYPE.md §5`.

---
## Cómo se conecta una IA a este sistema
1. Leer este documento entero (resumen operativo).
2. Para profundizar: leer `docs/SISTEMA-AVATARHYPE.md` y los prompts en `docs/recursos-prompts/`.
3. Para ejecutar con la identidad de Alexander: usar los IDs de la sección 6 con el conector
   Higgsfield. Generar vídeo requiere sesión interactiva (aprobación).
4. Tras cada avance, actualizar `cerebro/04-estado.md` (y este doc si cambia el sistema).
