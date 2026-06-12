# Sistema AvatarHype — Anuncios UGC con IA para E-commerce

> Documento maestro. Resume y reconstruye el sistema completo enseñado en el curso
> **AvatarHype™ Academy — "Todos los formatos IA (menos animado)"** (4 volúmenes).
> Es la base sobre la que vamos a construir el sistema más grande.

---

## 0. Qué es esto y para qué sirve

AvatarHype enseña a producir **anuncios de e-commerce con avatares de IA hiperrealistas**
(UGC, podcast, voz en off, dualcast e imagen) por **la ruta más barata del mercado**,
evitando las herramientas "premium" que se comen el margen (HeyGen, Arcads, Veed, etc.).

La tesis central del curso, repetida en cada volumen:

> **"El UGC con IA no va sobre una herramienta concreta. La diferencia entre un anuncio que
> revienta y uno mediocre está únicamente en la creatividad (el ángulo + el guion), no en el
> modelo de vídeo."**

Y la segunda idea clave: **no depender de una sola herramienta ni de un solo modelo.** Se monta
un sistema con varias "rutas" intercambiables, de forma que si una API se satura o un modelo se
cierra (le pasó a Sora), se salta a otra sin quedarse bloqueado.

**Resultado objetivo:** clips de vídeo realistas a **0,07–0,16 € por clip** (vs. 2–4 € en la ruta
oficial), e imágenes a **0,012 € por imagen**, suficientemente buenos para pasar desapercibidos
ante el 90 % de la audiencia.

---

## 1. El stack de herramientas (las "rutas")

El sistema usa **marketplaces de APIs** chinos que revenden acceso a los modelos de IA punteros
mucho más barato que las plataformas oficiales. Esa es toda la "magia" del coste.

| Capa | Herramienta | Para qué | Coste aprox. |
|---|---|---|---|
| **Marketplace API 1** | **Kie.ai** | Vídeo (Sora 2) e imagen, muy barato | Sora 2: ~0,15 € / 15 s |
| **Marketplace API 2** | **APImart** (apimart.ai) | Vídeo (Veo 3.1, Omni Flash, Kling) e imagen (GPT Image 2, Nano Banana Pro) | Veo 3.1: ~0,07–0,08 € / 8 s · GPT Image 2: ~0,012 €/img |
| **Imagen** | **Nano Banana Pro** (en APImart/Kie) | Generar avatares, productos, frames | barato |
| **Imagen (ruta económica)** | **GPT Image 2** (en APImart) | Avatares/escenas, 90 img por 1 € | 0,012 €/img |
| **Voz en off** | **ElevenLabs** | Audio narrado para UGC voice-over | — |
| **Edición** | **CapCut** (escritorio) | Montaje, capa de realismo, subtítulos | gratis (algunas funciones pro) |
| **Subtítulos premium** | **Captions** (app móvil) | Subtítulos estilo anuncio | ~pago mensual, opcional |
| **Música / SFX** | **Epidemic Sound** (30 días gratis) + biblioteca propia AvatarHype | Música sin copyright y efectos | gratis 30 d |
| **Inspiración / referencias** | **Pinterest, TikTok, Instagram** | Encontrar avatares, escenas, trends | gratis |
| **Frames de trends** | descargador de TikTok + **frame extractor** | Sacar frames de un trend viral para recrearlo | gratis |
| **Generación de prompts** | **Agentes GPT propios de AvatarHype** (custom GPTs) | Crear prompts y guiones estructurados | ChatGPT |

> ⚠️ **Nota de actualización (del propio curso):** Sora cerró oficialmente. El Volumen 1 (que lo
> usaba) quedó obsoleto en esa parte. El contenido **más actual es el Volumen 3/4** (modelo
> **Omni Flash** de Google + formato **Dualcast**). Cuando se replique, priorizar la ruta Veo
> 3.1 / Omni Flash sobre Sora.

### Modelos de vídeo por orden cronológico en el curso
1. **Sora 2** (Vol. 1) — ❌ descontinuado.
2. **Veo 3.1 / Veo 3.1 Fast** (Vol. 1–2) — el caballo de batalla durante meses.
3. **Kling v3** (Vol. 2) — alternativa, algo más cara, buen lip-sync (máx. 5 s).
4. **Omni Flash** (Gemini Omni, familia Google) (Vol. 3/4) — **el más reciente y mejor**. Clips de
   4/6/8/10 s al mismo coste que 8 s. Mucho mejor con el español de España.

---

## 2. El flujo de trabajo central (válido para todos los formatos)

Todos los formatos comparten el mismo esqueleto de 6 pasos:

```
1. ÁNGULO + GUION   → agente de scripts (producto → público, pain points, ángulo, guion)
2. INSPIRACIÓN      → Pinterest / TikTok / Instagram (captura de pantalla de un avatar/escena real)
3. IMÁGENES         → GPT Image 2 / Nano Banana Pro (avatar, producto, frames inicial y final)
4. VÍDEO            → Veo 3.1 / Omni Flash (prompt = cámara + microacción + guion + voz + acento)
5. EDICIÓN          → CapCut (cortar, entrelazar, música, SFX, textos, capa de realismo)
6. PUBLICAR         → anuncio listo
```

### 2.1 El "Método 6C" y la estructura de prompt
El curso estructura cada prompt de vídeo en bloques. Los agentes GPT propios automatizan esto,
pero la estructura manual (de la plantilla Veo, ver `docs/recursos-prompts/plantilla_prompts_veo_3_1.md`)
es:

1. **Formato y tipo** — `9:16, iPhone front-camera selfie, handheld, hyper-realistic UGC, not cinematic`
2. **Identidad del personaje** — "la misma persona de las imágenes de referencia, identidad/cara/piel/pelo/outfit idénticos"
3. **Entorno** — lugar, hora, luz, ambiente
4. **Acción principal** — 1 acción + 1 microacción (no meter 5 acciones en 8 s)
5. **Física humana** — definir qué es "natural": microshake, respiración, rebote, movimientos no repetitivos
6. **Idioma y forma de hablar** — forzar español de España con muletillas ("a ver…", "es que…")
7. **Tono emocional** — calm / confident / casual / not selling / not performing
8. **Script** — corto, fácil de pronunciar, pensado para 8 s
9. **Comportamiento** — empieza hablando mid-thought, parpadea, pausas, mira fuera de cámara
10. **Cámara** — handheld, off-center, autofocus shifts, rolling shutter, no stabilization
11. **Luz** — luz natural, exposición que cambia, sombras suaves (la luz perfecta mata el UGC)
12. **Audio** — micrófono crudo de iPhone, ruido ambiente, respiración, sin música
13. **Negative prompt** — studio lighting, beauty filter, perfect skin, ad-like polish, robotic delivery…
14. **Start frame / End frame** — si hay referencias, guía la transición entre los dos estados

> **Truco del español de España:** los modelos se entrenan con mucho más inglés y español latino.
> Para forzar acento peninsular: usar el bloque de idioma + meter una palabra muy de España al
> inicio del guion ("joder", "tía", "tío") que luego se corta en edición. Con **Omni Flash** (Vol. 4)
> esto ya casi no hace falta y se pueden hacer acentos argentino/colombiano/mexicano.

### 2.2 La "capa de realismo" en CapCut (clave, se aplica SIEMPRE)
Después de generar los clips, el toque que hace que parezcan reales. Dos ajustes documentados:

**Ajuste Vol. 1 (rápido):**
- Disposición/temperatura: ~ +3 · Contraste: −7 · Partículas: 10 % · Motion blur: 20 % (clip a clip)

**Ajuste Vol. 2 (ajuste de color personalizado, el bueno):**
```
Temperatura: -3 · Tinte: +2 · Saturación: -6 · Exposición: -3 · Contraste: +12
Highlights: -35 · Sombras: -18 · Fade: +6
```
Se guarda como "ajuste personalizado" en CapCut y se reaplica a todos los vídeos.

---

## 3. Los formatos (qué enseña cada volumen)

### Volumen 1 — Formatos base (con Sora 2, ahora obsoleto)
Introduce el sistema y dos rutas:
- **Ruta 1 (Sora 2 en Kie):** vídeo de 15 s por imagen→vídeo, 0,15 €. Concepto de *success rate*
  (la API se satura algunos días → te vas a otra ruta).
- **Ruta 2 (Veo 3.1 en APImart):** clips de 8 s a 0,07–0,08 €, uniéndolos en edición. Más control
  porque se le dan **primer frame y último frame** (generados antes con Nano Banana Pro).
- Enseña además: **anuncios con trends virales** (descargar un TikTok trend, sacar frames, recrearlos
  con IA, animar antes/después) y **anuncios en imagen** con Nano Banana Pro (before/after + testimonio).

### Volumen 2 — UGC sin Sora: Podcast, UGC tradicional, UGC voz en off
- Ruta principal: **Veo 3.1 a 0,08 € / 8 s** + imágenes con **GPT Image 2 a 0,012 €** (sustituye a
  Nano Banana Pro por coste: 90 img/€ vs 7 img/€).
- **3 formatos detallados:**
  - **Podcast:** dos avatares (uno se genera y el otro se "voltea" con `Flip the image horizontally`),
    cámara estática, se entrelazan clips cortos en edición para simular conversación natural.
  - **UGC tradicional:** un avatar habla a cámara, con imágenes superpuestas (periódico, comparativas).
  - **UGC voz en off:** se genera el audio con **ElevenLabs** y se montan varios clips por encima.
- Introduce los **dos agentes GPT propios**: el de **scripts 3 formatos** (producto → 3 guiones) y el
  de **prompts método 6C** (captura de Pinterest → prompt estructurado).
- Logo de podcast generado con GPT Image 2 + quitar fondo, como marca de agua.

### Volumen 3 — Ads en Imagen v2 (agente automatizado)
- Un **agente GPT "Ads Creative Generator"**: le das el producto, hace análisis estratégico
  (nicho, avatar, pain points, ángulos), le das paleta de colores + mercado, y devuelve **7+ prompts
  listos** para image-ads en distintos formatos:
  - Comparativa · Before/After · Testimonial · Problema-solución · Fake-news · Advertorial · Reddit ·
    WhatsApp · Timeline de progreso · Oferta · Características de producto.
- Generación en **GPT Image 2** (resolución 2K, aspect ratio 4:5 para post o 9:16 para story).

### Volumen 4 — Modelo nuevo (Omni Flash) + formato Dualcast
- **Cambio de modelo:** de Veo 3.1 → **Omni Flash** (Gemini). Salto de calidad grande, mismo coste,
  clips de 4/6/8/10 s, mejor español de España y acentos LATAM.
- **Biblioteca de prompts unificada** (hospedada en `avatarhype.online/alumnos`): cámara, microacciones,
  movimientos de cámara, idioma/acentos, voces, formatos. Se mantiene abierta en una pestaña y se copia/pega.
- **Microacciones / migeneraciones** (gestos que dan realismo): ajustarse la gorra, beber café antes de
  hablar, tocarse el pelo, señalar arriba-izquierda/derecha (para superponer una imagen), reírse, asentir.
- **Movimientos de cámara:** plano fijo, zoom lento/rápido, móvil en mano con temblor, retroceso que
  revela entorno, seguimiento al caminar.
- **Formato nuevo DUALCAST:** dos personas a cámara hablando e interactuando entre ellas y con la
  audiencia. Dos prompts base: "habla la persona izquierda, la derecha asiente" y viceversa. Se generan
  clips cortos y se entrelazan en edición (limitación: los cortes se notan un poco, pero pasa para el 90 %).

---

## 4. Mapa de recursos extraídos (en este repo)

| Carpeta / archivo | Contenido |
|---|---|
| `docs/transcripciones/` | Transcripción completa (subtítulos ES oficiales) de los 4 vídeos |
| `docs/notas-lecciones/` | Notas escritas de cada lección, con todos los links |
| `docs/recursos-prompts/plantilla_prompts_veo_3_1.md` | Plantilla maestra de prompt de vídeo (14 bloques) + plantilla copiable |
| `docs/recursos-prompts/prompts_referencia_visual.md` | Prompts para cambiar avatar, reemplazar fondo, plano cercano, podcast (flip) |
| `docs/recursos-prompts/ads_imagen.md` | Plantillas de image-ads (testimonial + before/after) con ejemplos |
| `docs/recursos-prompts/trends_virales_ads.md` | Flujo completo de un trend viral: antes/después/producto + animación |
| `docs/recursos-prompts/mini_biblioteca_prompts_sora.md` | Biblioteca de prompts Sora (Vol.1, modelo obsoleto, valor histórico) |

### Enlaces del curso (de las notas de cada lección)
**Herramientas (afiliados del autor):**
- Kie.ai — `https://kie.ai?ref=5ec19ff01c88163e62f1bf8b90bfc2fa`
- APImart — `https://apimart.ai/register?aff=avatarhype`
- Epidemic Sound — `https://share.epidemicsound.com/r1xj4g`

**Agentes GPT propios (requieren ChatGPT):**
- Agente método 6C (prompts) — `https://chatgpt.com/g/g-6975edfa30b8819183d350d8b87358d4-avatarhypetm-prompts-metodo-6c`
- Agente Scripts 3 Formatos — `https://chatgpt.com/g/g-6a022e72bb388191abaebb6302f759d7-scripts-que-convierten`
- Agente de prompts (compartido) — `https://chatgpt.com/share/69cfeabd-793c-83e9-a471-9a40f914bd99`

**Recursos del alumno:**
- Biblioteca de prompts y música — `https://avatarhype.online/alumnos`
- Recopilación de música (Drive) — `https://drive.google.com/drive/folders/1GJMPIDjaFQUUlMetrhxxhd8LVQAYbXbi`
- PDF ejemplos de conversión en imagen — `https://drive.google.com/file/d/1NPyoddNlK4BagSPkx8QPzszzFPfrzFvJ/view`

---

## 5. Hacia la replicación / automatización (próximos pasos)

Este curso es **manual** (mucho copiar/pegar entre Pinterest → ChatGPT → APImart → CapCut). El
"sistema más grande" que vamos a construir puede **automatizar este pipeline**. Notas para esa fase:

- **Las APIs son accesibles programáticamente.** Kie y APImart exponen endpoints REST. Se puede
  orquestar `producto → guion → imágenes → vídeo → ensamblado` sin tocar las webs manualmente.
- **Los agentes GPT propios** se pueden replicar como prompts de sistema + llamadas a la API de un LLM
  (los guiones y la generación de prompts es lo que más valor aporta y es 100 % automatizable).
- **n8n** (conectado en este entorno) es el candidato natural para orquestar el flujo end-to-end:
  webhook con el producto → nodo LLM (guion + prompts) → nodo HTTP (APImart vídeo/imagen) → ensamblado.
- **Higgsfield** (también conectado) cubre generación de imagen/vídeo/audio y podría sustituir o
  complementar las rutas de APImart según coste/calidad.
- **La "capa de realismo" y el ensamblado** (CapCut) es la parte menos automatizada; se puede replicar
  con ffmpeg (curvas de color equivalentes + concat de clips + audio).

> **Estado:** sistema aprendido y documentado por completo. Listo para diseñar la versión automatizada
> cuando demos la señal de continuar.
