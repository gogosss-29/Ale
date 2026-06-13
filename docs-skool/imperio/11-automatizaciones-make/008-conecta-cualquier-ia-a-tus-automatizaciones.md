# 📌Conecta Cualquier IA a tus Automatizaciones

> Ruta: Automatizaciones Make › 📌Conecta Cualquier IA a tus Automatizaciones

**🎬 Vídeo (32.4 min):** https://youtu.be/UVxh6GVqVyM

**📎 Recursos:**
- LoRA + Video + Audio.blueprint v3

---

### Replicate + Make (Flux LoRA + Kling + Audio)

### 1. ¿Qué hace exactamente esta automatización?

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cd1e581d989d4f7da49be42de5fd262ff8b244469b054c49aa6f86245bbc3c34-md.png)

1. **Recibe tu idea** (una frase dentro de `{ }`) mediante un Webhook.
2. **Genera cuatro prompts** (texto, video, audio y caption) con OpenAI.
3. **Crea la imagen** en Replicate usando tu LoRA.
4. **Anima la imagen** → video de 5 s en otro modelo de Replicate.
5. **Diseña el ambiente sonoro** sobre ese video.
6. **Publica el Reel** en tu cuenta de Instagram con el caption generado.

Todo el flujo corre dentro de Make; tarda ± 3‑4 minutos y queda 100 % hands‑off.

### 2. Visión general del flujo

1. **Custom Webhook (Make)** ― Recibe tu `{prompt}` al instante.
2. **Set Variables (Make)** ― Carga tu `api_replicate` para no hardcodear la key.
3. **Create Chat Completion (OpenAI o3-mini)** ― Devuelve 4 líneas (TEXT, VIDEO, AUDIO, CAPTION) en ≈ 5-10 s.
4. **Transform to Structured Data (OpenAI gpt-4o)** ― Separa cada línea en variables únicas (≈ 1-2 s).
5. **HTTP POST a Replicate (LoRA)** ― Genera la imagen vertical 9:16 (≈ 10-25 s).
6. **Sleep 15 s** ― Da tiempo a Replicate para renderizar.
7. **HTTP GET a Replicate** ― Recupera la URL de la imagen (≈ 1 s).
8. **HTTP POST a Replicate (Kling)** ― Convierte la imagen en video de 5 s (≈ 2-3 min).
9. **Sleep 180 s** ― Espera el render completo del video.
10. **HTTP GET a Replicate** ― Obtiene la URL del video (≈ 1 s).
11. **HTTP POST a Replicate (FX Audio)** ― Añade ambiente sonoro (≈ 15-20 s).
12. **Sleep 20 s** ― Espera el render con audio.
13. **HTTP GET a Replicate** ― Recupera la URL final (video + audio) (≈ 1 s).
14. **Create Reel Post (Instagram Graph API)** ― Publica el Reel con caption (≈ 5-10 s).

> En total: ~3-4 min y cero intervención manual.

*(Los bloques Sleep son necesarios porque Replicate responde primero con una URL “polling”; esperamos y luego consultamos ese endpoint.)*

---

### 3. El prompt maestro (Prompt Engineering)

El módulo **Generador de Prompts** envía este mensaje al modelo *o3‑mini*:

```
Eres Generador de Prompts Triple. El usuario te dará una sola frase entre llaves: "bencordero {{19.activity}}"

Devuélveme cuatro líneas, cada una ≤ 20 palabras, con este formato y sin ningún texto extra:
TEXT: ...
VIDEO: ...
AUDIO: ...
CAPTION: ...

– TEXT, VIDEO y AUDIO en inglés  
– CAPTION en español (humor ligero)  
– “bencordero” SIEMPRE es el sujeto  

Ejemplo de entrada: {bencordero epic climbing in Patagonia}
Ejemplo de salida: 

TEXT: bencordero climbing a huge granite spire at sunrise, cinematic
VIDEO: the climber with slow dolly zoom out showing vast Patagonian valley
AUDIO: windy sound, distant condors, gear jingling
CAPTION: Escalando egos y montañas… ambas igual de resbalosas 😅
```

---

### 4. Configuración de cada servicio

#### Replicate

- **Imagen** → tu propio modelo LoRA (`benjacord/bencorde`), resolución 9:16, `.webp`, 28 steps, `guidance_scale: 3`.
- **Video** → modelo `kwaivgi/kling‑v1.6‑standard` con la imagen como `start_image`, duración 5 s.
- **Audio** → modelo `62871f…` que toma el video final y añade FX.

> Asegúrate de guardar tu API Key en la variable **api_replicate** y no hardcodearla.

#### OpenAI

Usamos dos llamadas:

1. **o3‑mini** (chat) para creatividad rápida.
2. **gpt‑4o** para parsear la respuesta y devolver JSON limpio (TEXT, VIDEO, AUDIO, CAPTION).

#### Instagram Graph API

Necesitas un **Instagram business account** conectado a tu Facebook app. El módulo `CreateAReelPost` pide:

- `video_url` (del paso 13)
- `caption` (del prompt)
- `share_to_feed: true` para que aparezca también en tu feed.

---

### 5. Paso a paso para replicarlo

1. **Duplica** el escenario en tu cuenta de Make.
2. En **SetVariables** sustituye `api_replicate` con tu propia key y las variables necesarias.
3. Conecta tu **cuenta de OpenAI** (modelo o3‑mini y gpt‑4o).
4. Conecta tu **Facebook/Instagram** en el último módulo.
5. Activa el escenario en **instant mode**.
6. Espera ~4 min y revisa tu Instagram. 🎬

---

### 6. Consejos y mejoras

- **Reduce los tiempos de Sleep** si tu modelo corre más rápido; prueba y ajusta.
- **Sonido**: el modelo acepta descripciones creativas (e.g., “rain hitting neon signs, distant chatter”).
- **Batch mode**: activa “secuencial” en Make si quieres lanzar varios prompts en paralelo.
- **Logging**: conecta un módulo *Google Sheets* antes de publicar para guardar cada prompt y URL.

---
