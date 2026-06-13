# ⛏️Crea Reels Virales | Kling AI + ChatGPT

> Ruta: Automatizaciones Make › ⛏️Crea Reels Virales | Kling AI + ChatGPT

**🎬 Vídeo (39.0 min):** https://youtu.be/pS74O0EvY-c

**📎 Recursos:**
- 1. Crear Prompts + Reel.json
- 2. Subir + Compilar Reel.json

---

En esta guía vas a aprender a montar un sistema **completo** en [Make.com ](http://bencorde.com/make)que:

1. **Crea** un Reel totalmente automatizado (imagen, video, música y caption).
2. **Sube** ese Reel a tu cuenta de Instagram Business y actualiza el estado en tu Google Sheet.

Todo parte de una hoja de Google Sheets donde introduces el tema (por ejemplo, “café” o “planta de hoja”) y, sin intervención manual, obtienes un Reel listo para publicar.

---

### **Visión general de las dos automatizaciones**

- **Escenario 1 (“Crear Reel”)**: ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9d04a21e85b1454ca5f5218321745c5fb7153ace21ae48d0bc30bc44044b65ac-md.png) 1. Lee el siguiente tema pendiente en Google Sheets.
2. Genera prompts con ChatGPT para imagen, video, música y caption.
3. Llama a Freepik/Kling para crear la imagen y el video.
4. Guarda en DataStore los parámetros necesarios.
- **Escenario 2 (“Subir Reel”)**  ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/85e51676bec44310b6ef593f68f4db23ead1d0901fdc48fea9a7e2936a271c6f-md.png) 1. Se dispara cuando termina la generación del video (webhook) en Freepik (Kling).
2. Recupera datos del DataStore.
3. Genera la pista de audio con MusicFy.
4. Combina audio y video con Segmind.
5. Sube el archivo a Dropbox y obtiene enlace.
6. Publica en Instagram Business y marca como “Done” la fila en Google Sheets.

---

## ¿Qué usaremos?

- [**Make.com**](http://make.com) – plataforma donde armamos ambos escenarios (Plan Pro gratis 30 días con tu link de referidos).
- [**Google Sheets**](https://workspace.google.com/products/sheets/) – hoja con las ideas que dispara el flujo → columnas **Idea Video**, **Creado**, **Subido**.
- [**Freepik API **](https://www.freepik.com/developers/dashboard/api-key)**– **[**Imagen3 **](https://docs.freepik.com/api-reference/text-to-image/imagen3/post-imagen3)**& **[**Kling**](https://docs.freepik.com/api-reference/image-to-video/kling-pro/post-kling-pro) – genera la imagen 9:16 y el video CGI.
- [**OpenAI Platform**](https://platform.openai.com/docs/overview) – crea los prompts para imagen, video y música (modelos `o4-mini` y `gpt-4o-latest`).
- [**Musicfy API**](https://create.musicfy.lol/) – compone la música de fondo a partir de texto (cuota gratuita diaria).
- [**Segmind API **](https://www.segmind.com/models/video-audio-merge/api)**– video-audio merge** – fusiona el MP4 sin complicaciones.
- [**Dropbox API**](https://www.dropbox.com/developers/documentation/http/documentation) – aloja el archivo final y devuelve el link descargable.

Más a detalle...

## 1. Escenario 1: Crear el Reel

1. **Disparador: Google Sheets → SearchRows** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a030326fce284883b1c42b2123a0bf23bfed57b012a94c29adcd8c939f067e05) - Filtra la hoja “Reels” buscando la primera fila con estado “0” (pendiente). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c3a1e3ef9b3d40c483cbb6c4a040677b730f936a464342f1a541c8b5d22f5705)
2. **ChatGPT:  Create a Chat Completion (Crear prompt de imagen)** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2ce66b434a0849a5a901a49de48a6cbea16ada4ebfb647298995a10b53a6d95b) - Módulo `openai-gpt:CreateCompletion` (o4-mini).
- Mensaje sistema orientado a prompts cinematográficos macro con personajes en miniatura. > You are an imaginative and detail-oriented prompt engineer specializing in creating cinematic and whimsical image prompts. Your outputs should be structured, vivid, and tailored for high-quality image generation in a macro photography style. All scenes should feature toy-sized characters (like miniature chefs, workers, or animals) interacting with real-world objects as if they’re giant environments. Use storytelling elements and focus on realism, charm, and creativity.Note: Many tiny workers should be there.  
>   
> Create a whimsical and detailed macro photography-style image prompt based on the topic: {{73.`0`}}  
>   
> Expected JSON output :
> 
> {"prompt":""}   
>   
> Example output:
> 
> {
> 
> "prompt":"A whimsical and detailed miniature scene showing tiny toy chefs making a giant pizza. The setting is a kitchen counter turned into a pizza factory. Miniature workers in chef hats and aprons use toy-sized cooking tools: rolling pins, paint rollers for spreading dough, tiny buckets of tomato sauce, and ladders to reach toppings like giant olives, pepperoni slices, and basil leaves. One chef is shredding cheese with a huge grater, while another uses a blowtorch to melt cheese. Construction cones and scaffolding surround the pizza as if it’s a worksite. Warm lighting, shallow depth of field, cinematic realism, macro photography style."
> 
> }
3. **Freepik: (Make an API Call) Generar imagen** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/338d1f0844d8412980a66e3b3701ecef0d9ea9bf782a4479a05e30637598a9ab) - Llamada a `/v1/ai/text-to-image/imagen3` con el prompt generado, ratio 9:16.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0caffc3baa0244119ec320ee2ed39e14e250cdf1c70c4b6aa22a2c7b32246e07)

Nota: Tienes que hacer una conexión antes, que la puedes hacer en

> {
> 
>   "prompt": "{{47.result.prompt}}",
> 
> "num_images": 1,
> 
> "aspect_ratio": "social_story_9_16"
> 
> }

1. **Tools: Sleep (Delay de 15 s)** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b0ce15202f2d47f8b8179c80156373d5ac2263bbc88b48b882a0235d8b26acfa-md.png)

- Pausa para que Freepik complete la tarea.

1. **Freepik: Obtener URL de imagen** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/29a0ec000ff94f0c841f4d6625f4b9916f57b6b96f2143449f6bf9b970a51835-md.png)

- `GET /v1/ai/text-to-image/imagen3/{task_id}` ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/047e558404bd40dc899eeb12ac8d900c22f2db3fde914c08b218685a38c50780)

1. **HTTP: Get a File (Descargar Imagen)** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b4c7d678c9214d0db9e57e8b350da558c4f14990765c40e4ae43e04629db0f84-md.png)

- Módulo `http:ActionGetFile` para bajar la imagen.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5640be37c9614568a508f8c9726bb37233b8eaba76a54c20a11d421a1f474277)

1. **ChatGPT: Crear prompt de video** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a932624607954b41b3abb36be95090cd6b7c24ed056d4a3a955441dcdcd92611-md.png)

- Módulo `openai-gpt-3:CreateCompletion` (chatgpt-4o-latest). **Prompt 1** > You are a creative video prompt generator. Your task is to analyze an image and create a whimsical, cinematic video animation prompt.  
> 
> The prompt should describe camera movement (including rotating shots), fast-paced actions of tiny toy-like characters, dynamic environment effects, and ambient sound design.  
> 
> The tone must be magical, playful, and visually immersive—perfect for a short animated video in tools like Kling, Runway, or Sora.
> 
> Strict Note: 
> 
> 1. All characters should appear to be working very fast and efficiently, not slow or idle. Their poses and actions should suggest speed, urgency, or rapid coordination — as if everything is moving in a high-efficiency, fast-paced system.
> 
> 2. This is a 10s Video Script
> 
> 3. Keap The prompt Lite and short and includes all the information as well.
> 
> Expected JSON output :
> 
> {"prompt":""}

**Prompt 2:**

> Example output:
> 
> {
> 
> "prompt":"A whimsical, fast-paced animation featuring tiny toy chefs working quickly on a massive pizza. The scene begins with a rotating camera orbiting the pizza surface, revealing multiple layers of activity.  
> 
> Miniature chefs run up and down ladders, rapidly spread tomato sauce using toy paint rollers, and quickly place huge pepperoni slices. Others zipline between platforms or operate toy forklifts carrying basil leaves and cheese chunks.  
> 
> The camera spins slowly around the scene, then dips down for low-angle shots and dramatic close-ups of melting cheese and sizzling toppings. Steam rises as the cheese bubbles and browns.  
> 
> The animation is lively and energetic, with fast but smooth character movement and lots of background action. Cooking sounds (sizzling, chopping, splattering) blend with whimsical, upbeat music to enhance the pace and mood.  
> 
> Cinematic lighting, shallow depth of field, and warm tones bring the magical kitchen factory to life."
> 
> }

- Usa la imagen descargada como input y genera un prompt ligero y dinámico para un video de 10 s.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/adf8f11515ac4e5b9dbbecede3d46740ae2768dd384b4f3794815384b8f78cb4)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/bd26fa7804004374bd2750f585d39cfd95174e82c0454a3fad9ac9e21935b41c)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a48577a8a6a84fdd98473c406227243acc9988d1dc4947c789c11f238ec0b97c)

1. **Create JSON: (Data Structure) Estructura para video** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/429f2b76c22e477cac9332e0043b5cd5b8ffb128287243b6bb91fa9b513b61e2-md.png)

Luego le daremos a "ADD"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0aab26dca03b465bb00d7a4e79c364ab95f9be4db82c40ca958a452f7dd5a2ee)

Y luego le daremos a "Generate"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b94bd2d3531e45b8a0e119b000ef21e538e8234d846e4932a2bde6c11417867c)

Y en sample data

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/792477024f1d4b18a74e756e5c9c7150e2ed1cccfcab4c82a0e6452f353eab33)

pegaremos el siguiente código:

> {
> 
>   "image": "[https://cdn-magnific.freepik.com/imagen3_c4bf833a-6346-42be-a500-c0d1c6ca0594_0.png?token=exp=1747223397~hmac=8af1a3824046ae1edfbbb23d21e301950e300b6c5959db6f5eb75ddb86b99102](https://cdn-magnific.freepik.com/imagen3_c4bf833a-6346-42be-a500-c0d1c6ca0594_0.png?token=exp=1747223397~hmac=8af1a3824046ae1edfbbb23d21e301950e300b6c5959db6f5eb75ddb86b99102)",
> 
>   "prompt": "A magical, high-speed animation showing tiny construction workers repairing a giant shattered smartphone screen. The camera swoops in from above, then rotates tightly around the impact site where workers in hard hats jackhammer through cracks, sparks flying. Others rapidly sweep debris while a crane swings a glowing microchip into place like a steel beam. On scaffolding, a crew welds lightning-speed data lines as blueprints flap in the wind. Dust swirls and spotlight beams pierce through ambient toolkit clatter and whirring drills. Everything buzzes with playful urgency in this fantastical tech repair zone.",
> 
>   "duration": "10",
> 
>   "cfg_scale": 0.7,
> 
>   "webhook_url": "[https://hook.eu1.make.com/il4y15dem4fuijtbag17xhv9h4vc33yp](https://hook.eu1.make.com/il4y15dem4fuijtbag17xhv9h4vc33yp)",
> 
>   "negative_prompt": "low resolution, blurry, dull colors, bad lighting, overexposed, underexposed, noisy background, unnatural motion, stiff animation, unappealing characters, messy composition, incorrect proportions, poorly rendered textures, jerky camera movement, awkward transitions, inconsistent lighting, lack of depth, no background details, flat lighting, chaotic scene, broken physics, pixelation, distorted faces, ugly colors, cluttered frame, unrealistic shadows, low frame rate, bad sound quality, missing sound effects, out-of-focus elements, boring composition, oversaturated colors, glitch effects"
> 
> }

`json:CreateJSON` monta el cuerpo con imagen, prompt, duración, escala, negative_prompt y webhook. (Aquí tienes que cambiar tu webhook)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/29f994a344714302a5882d64bd7a4c7808fd05d60f2a4e5dbb0ed8fc3a32d2a0)

Abajo en el negative prompt pegaremos:

> low resolution, blurry, dull colors, bad lighting, overexposed, underexposed, noisy background, unnatural motion, stiff animation, unappealing characters, messy composition, incorrect proportions, poorly rendered textures, jerky camera movement, awkward transitions, inconsistent lighting, lack of depth, no background details, flat lighting, chaotic scene, broken physics, pixelation, distorted faces, ugly colors, cluttered frame, unrealistic shadows, low frame rate, bad sound quality, missing sound effects, out-of-focus elements, boring composition, oversaturated colors, glitch effects

1. **Freepik: Make an API Call (Generar video con Kling)** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a69d1601d87a4986bb96bd918783d47009f400a304584720804abde46592fafe-md.png)

- POST a `/v1/ai/image-to-video/kling-pro` usando el JSON anterior. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/922c015081b2466e848b59f125537f3219b9e01d2d9c4f7780d8bd71e44f6709) Y seleccionaremos la variable que creamos anteriormente.

1. **ChatGPT: Create a Completion (Música): **Crea prompt para MusicFy basado en el script y la imagen. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/065ff6a2fe9e49c6831ca0c6bba168a4756a3caf4dbb451daf40c47517a20055-md.png) > PROMPT MUSICA:   
>   
> You have to create a music prompt for generating background music using Musicfy for a 10-second video. The video will be created using Kling AI. Based on the provided image and the video script, generate a background music prompt that matches the mood, pace, and surreal visual style of the scene.
> 
> The music must enhance the fast-paced, cinematic, and dreamlike atmosphere of the video.
> 
> The characters in the scene are moving very fast and efficiently, so the music should reflect that energy.
> 
> Include references to instrumentation, tempo, mood, and any sound effects or genre influences (e.g., whimsical strings, glitchy synths, cartoon sound design, orchestral hits, lo-fi beats, etc.).  
>   
> Your output will be only be the music prompt in a loop if possible, the 10 second should end in a loop that syncs with the beginning of the beat.  
>   
> Video Script : {{50.result.prompt}} ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/119fb139987e43ffadf4df802aa62f32114fa6e7f9b547ea9f1e5b4c41337077)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/75fac601cef642abb8f3ff274487ab8910cf608410534886b75d44139657b9fb)

1. **ChatGPT: Create a Completion (Caption)** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6e8110e11f7449e79673b748c33f85677a260fc9ce9b416a9b6ce4c028a3caf9-md.png) >  You have to create a short, attention-grabbing Instagram caption (under 150 characters) that matches the vibe of the video — surreal, funny, satisfying, or weirdly cool — and encourages viewer engagement.
> 
> for a 10-second video
> 
> Your output will ONLY be the caption.  
>   
> Video Script : {{50.result.prompt}}  
>   
> {{[46.body.data](http://46.body.data).generated[]}} ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ad434c088e7f4c49a133cef64c2eeaa707c0962f8a8146bd8c9a6cd1ae90da8f)   
`gpt-4.1-mini` genera un caption corto (<150 car.) para Instagram.
2. **DataStore: AddRecord**

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6d438fb06ae040f0b3ddd82c33335ca0faafbc428410407ea069b087c3b19fee-md.png)

- Guarda en el DataStore “Ad Reels” el ID de video, prompt de música, caption y número de fila.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3542c83111944a0c8b1b0d8428d77841a8dbb88921c04ac5882a77ef297a0c0b)

Es probable que tengas que tengas que crear una Data Store y Data Structure antes aqui  


![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5b9df2c69bed43ef931f366d460641aae3a0ece5e1034e498f6154935577f5c9)

Le das a "Add Item"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b1aa6fcde0c54ed8a1aee52ef0502e092816ecf02a1d45c3b36e6f4845da998d)

Y vas agregando los items manualmente, ID Video, Prompt Musica, Caption, Numero Fila.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/35ddc21d773243b3b2ca2786ff3b23cc31c6e6dfa44c4af19320fa647dd2ad38)

Le das a "Save"

Y con esto el primer escenario ha generado **todas** las piezas necesarias y las ha almacenado para la siguiente fase.

---

Ahora tendremos que esperar unos minutos a que se genere el video, que tiende a tomarse entre 3 a 6 minutos (en mi experiencia). Una vez que esté lsito, se mandará un webhook al webhook que reemplazamos previamente, cuando cambie al status "COMPLETE"

---

## 2. Escenario 2: Subir el Reel

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/28cc229ac35949d7bc03b8bbee497d880755925221b7444eb59aafe2a5f63245-md.png)

1. **Disparador: Custom Webhook** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/64e35c9cd4a7422f8b6ed62b7170f383c788f639a682413d8639fbdd9dadb6a4) - Crearás un nuevo webhook (es el webhook que tenemos que reemplazar en el custom JSON de la automatizacion 1). **Se activa cuando Freepik/Kling notifica que el video está listo.** 1.5 **Filtro** ante "Completed": Se activará el filtro cuand oel estado de la generación del video esté **"COMPLETED"** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/82b082004f8c43799fc18e5ad42d2d5db6d32697f65349eaae862cac4d279176)
2. **DataStore: SearchRecord** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8846cc8490ae471e9ee7563d2d23c2f8667052911db74a53b7ac360258b046cc-md.png) - Busca en el datastore específico la información que guardamos previamente en el registro, filtraremos cuyo ID de video (task_id) coincida con el recibido en el webhook.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d3c7a0dfb85a4b878f2e251fb155edf9fb12493d2a7340748604c42c3cc7b96d)

1. **HTTP: Make a Request (MusicFy: Generar música)** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/57f67e1878504a008eee42d77d1616ff2750091cc20d4ae9ad16e9743b259e25-md.png)

- `http:ActionSendData` POST a `https://api.musicfy.lol/v1/generate-music` con el prompt guardado.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2007fe0b14f84f359dc276464b58c6c4b3872676379444f7b518964354509cfe)

Nota: Tienes que crearte la [API de MusicFY ](https://musicfy.lol/api)e incluirla y pegarla bajo "Authorization"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3e7e24945ad04bdda16a4d5852a9ad46902f252a37c7472e97dd9da8bf7d04ed-md.png)

Y bajo el requested content, pegaremos el prompt de aquí.

> {
> 
>   "prompt": "{{9.data.`Prompt Musica`}}",
> 
>   "duration": 10
> 
> }

- Permite 10 s para producir la pista.

1. **Tools: Sleep (Delay de 15 s)** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/75405a1a643142ef85e46e45114a97e8c8310b778a144979b36bc296b9299464-md.png)

- Asegura que MusicFy termine la generación.

1. **HTTP: Maque a Request (Segmind: Combinar video y música)** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3b7a415713424d26bd975ec974523bd1faaf80837826478a8a95392279b0b4c6-md.png)

- `http:ActionSendData` a `https://api.segmind.com/v1/video-audio-merge` con URLs de video y audio.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/35586d7a825b42b8a2b6246acf6cf14ec90c988a5b60402ea515b1e05880b1ed)

Es importante que rellenemos el x-api-key con nuestra PROPIA api key que podemos generar en [https://cloud.segmind.com/console/api-keys](https://cloud.segmind.com/console/api-keys)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/10e3cdf25e224841b197f63abc6188463322db7e8b5e44fcac60511525a0c23e-md.png)

apretando "get your api-key".

1. **Dropbox: Upload a File ** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/74fbec9eeb034a6eab8c6d77e48f1f14db22b7067e5b42ddadb4417e6843ab6b-md.png)

- Sube el MP4 resultante al path elegido, usando un UUID.mp4 como nombre y la data que sacamos previamente del video combinado

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/77fcc8b0eb5a47b18c891095e21112b1c9317d509f18409a940f64219dbfaa02)

1. **Error Handler** (Break)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/dfbea802528b4349b6fe5d12e2709313a0ff8a35c2754d30958deec12e095bd2)

Agregaremos un error handler especificamente "Break" por si hay algun problema en esta parte de la automatizacion, que es la que mas te podría presentar problemas.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8a16d13c18fd426cbadd56fa6f0cfd1c121b9a257fe84f9f896475e29d73d7c6)

1. **Dropbox: Create/Update Share Link** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6b9e417c55004f53a2164eab79d21fc90496e267b6b3412e8a49a04a5b9344d3-md.png)

- Obtiene un enlace público de descarga.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c983ba509fbb4ad0bf78302c796f0d9c50ef4a6857654eb1bdbc1fc56be8bdad)

1. **Instagram Business: Crear Reel** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cc2c75a31c3c4f1b9a54394d0d7870e16569e2c999d04635914a8869b1cf876e-md.png)

- Módulo “Create a reel post” mapea el enlace de Dropbox y el caption.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2b3c964548f747199d243e3ea8b3a2824a369df55c0e41548852ee706e986c64)

1. **Google Sheets: Update a Row** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7756ab79635f41448a37d1895ccf4ae8bdb172c07cdd457ba85af3bf18fb64cc-md.png)

- Marca la fila correspondiente como “1” (Done) para no volver a procesarla.
- Especifica el URL

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/671d6cd68dfc47da8080e3ec701b222d3c769fb59719460590f0e363cfaba89d)

Al terminar, tu Reel está **en vivo** en Instagram y tu hoja de cálculo refleja que ya está subido.

---

Puedes importar directamente los blueprints en Make, o construir el flujo desde cero siguiendo la lógica anterior.  
Si tienes dudas sobre parámetros específicos, revisa los JSONs que te adjunto, y usa los ejemplos de prompt como base para tus pruebas.

---

#### Cómo Importarla

Con estos **dos escenarios** en [Make.com](http://Make.com) obtienes un pipeline que, desde un simple tema en Google Sheets, genera un Reel completo y lo publica automáticamente. 🚀

1. Copia/pega los blueprints JSON en tu cuenta de [Make.com](http://Make.com).
2. Conecta tus cuentas: Google, OpenAI, Freepik, MusicFy, Segmind, Dropbox e Instagram Business.
3. Reemplaza el Webhook por el webhook del segundo escenario que creaste (en el JSON Structured)
4. Crea la Data Structured dandole a "Generate"
5. Ejecuta el escenario 1 y observa cómo crea el Reel.
6. Todo lo demás ocurre en segundo plano con el escenario 2.

Listo! Ahora puedes producir contenido **viral** en piloto automático sin invertir horas en edición manual.
