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

## 🎙️ Transcripción

Probablemente has visto este tipo de videos que están virales en las redes sociales. Este mismo que tiene millones y millones de views. Déjame decirte que no necesitas ser un programador o un diseñador elite para poder llegar y hacer este tipo de videos que estás viendo acá, porque hoy día te voy a mostrar cómo armamos un sistema completamente automatizado, que es capaz de generar este tipo de videos que estás viendo en pantalla. Y no solo generarlo, sino que crearlo todo, desde la imagen hasta la animación, hasta la música. hasta el texto y subirlos a las distintas plataformas como Instagram reels o incluso YouTube Shorts si quisieras. Y lo que armamos juntos es un sistema que con chat GPT creamos los promps para armar las imágenes, luego animamos con Cley, creamos música con otra inteligencia artificial llamada Music F y después se sube directamente a Instagram. Todo sin que tú tengas que intervenir manualmente ninguna vez. De hecho, ya hay personas que están creando este mismo tipo de automatizaciones en aplicaciones para el celular, como podemos ver justo aquí, y que están cobrando mensualidades de 30, $0 mensuales y tienen miles y miles de descargas. ¿Okay? Esto es realmente una locura y es literalmente la misma automatización que te voy a mostrar. Ahora, este sistema lo puedes dejar publicando contenido por literalmente el tiempo que quieras y con la frecuencia que tú quieras. Y antes de mostrártelo, veamos cómo funciona. Simplemente tú escribes la idea de tu video acá, es decir, un objeto en específico, y lo que va a hacer este sistema es literalmente crearte todo el contenido. Chat GBT crea los promps visuales, luego Cllink anima esa imagen que te acaba de dar, luego se crea la música y se combina y se sube a tu Instagram. Esto es realmente una locura y lo mejor es que puedes comenzar a aplicarla hoy mismo porque te voy a dar absolutamente todo para que lo puedas hacer. Vamos a escribir una lista de objetos o de ideas que queremos que nuestro video sea sobre. Por ejemplo, vamos a hacerlo de un macetero para plantas, una taza de café y una hamburguesa. Aquí podemos crear la lista con la cantidad de objetos que literalmente queramos. Si somos muy flojos, podemos incluso pedirle a Chat GPT que nos genere una lista de objetos relacionadas al nicho en específico, al que quieran lanzarlo. Después le vamos a dar a ejecutar y lo que va a hacer es nos va a tomar la primera fila que aparece acá que tenga un cero, es decir, en este caso un macetero. Va a revisar directamente y nos va a empezar a crear el prom de la imagen. Luego nos genera la imagen y le acaba de mandar la imagen para generar a el modelo de Google de Imagine 3 o imagen 3. Si es que abrimos esto y vemos exactamente qué es lo que nos dio, vamos a ver que la imagen es esta que está aquí y tenemos actualmente los pequeños trabajadores trabajando en el más macetero, pero todavía nos falta darle vida y eso es lo que sigue justo acá. Lo que estamos haciendo acá, estamos descargando la imagen y con char GPT estamos creando el prompt con el que vamos a animar el video. Luego nos vamos a ir a la parte que sale generar video, que vendría siendo este de acá, y va a mandarle una señal a Cling. Clmente, en mi opinión, es lo mejor que hay para animar videos. Sí, puede ser un poco costoso. Cada generación está bajo el dólar de toda esta automatización, pero saca resultados muy muy buenos. Entonces estamos haciendo el llamado a cling en este caso y estamos creando el prompt de la música y el prompt de el caption del Instagram. Luego de unos segundos podemos ver que acabamos de recibir directamente acá que se terminó de generar el video, porque recordemos aquí lo mandamos a generar y acá se acaba de terminar de generar, es decir, está completado. Luego vamos a extraer toda la información que se trajo directamente de lo que se generó previamente, es decir, el link que nos dio acá. Y ahora estamos creando la música. Esto es realmente una maravilla. Estamos creando la música completamente con inteligencia artificial usando un programa que se llama Music Fight con el prompt que creamos antes, que era justamente este de aquí. Aquí nos acaba de crear la música, como podemos ver acá. Este es el archivo de la música y luego se está combinando la música con el video en una aplicación que se llama Segmine usando un modelo de combinación de videos con audio. Una vez que se haya combinado el video, lo vamos a subir a Dropbox, nos va a crear el link y se va a publicar automáticamente en Instagram. Si es que entramos a Instagram, esta es una cuenta con la que estuve probando, con la que estuve jugando y lo voy a actualizar y actualmente no se ha publicado, pero apenas se termine esto se va a publicar en Instagram. Y podemos ver que se acaba de terminar de publicar y ahora sí, si es que actualizo esto, debería aparecernos acá justamente el video. Esto está realmente genial. la había probado, había armado otro tipo de videos como este o incluso este. Y esto es realmente una locura porque podemos empezar a armarlo con la continuidad y la frecuencia que nosotros queramos, simplemente cambiándole este pequeño parámetro de acá. Es decir, quiero que se publique y se cree un video cada 15 minutos o quiero que sea una vez por día o quiero que sea ciertos días en específico de la semana, ¿verdad? Si quisiera subir, no tengo idea, seis o cierta cantidad con cierta frecuencia, simplemente le cambiaría este parámetro que está acá. Ahora sí, vamos a ver cómo funciona esto, pero antes déjame decirte que no vas a tener que armar todo paso a paso porque todas estas plantillas las tengo publicadas en Imperio Digital. Imperio Digital es una comunidad donde puedes aprender de automatizaciones e inteligencia artificial con estrategias que funcionan. Entonces, si es que entramos a Imperio Digital, nos vamos al Classroom y nos vamos a las automatizaciones, podemos bajar, bajar, bajar y vamos a ver la parte que sale crear los reels con Cling. Aquí también te dejé una guía detallada con todos los promps, con todas las cosas que vamos a usar. Y si bajas al máximo, al máximo, al máximo, vas a poder encontrar que justo al final de todo esto están estos dos escenarios. Y basta con darle clic, descargar, luego darle clic y descargar. Nuevamente, darle a crear un nuevo escenario, apretar los tres puntitos e importar el blueprint. Vamos acá, le damos a guardar y te va a aparecer exactamente así el primer escenario y hacemos exactamente lo mismo con el segundo escenario. Y simplemente desde este punto hay que cambiarle un par de variables, hay que conectar tu cuenta de Google, tus App Keys. App key es la llave que usas para extraer y conectarte con distintos servicios y nada más. Ya, o sea, son una serie de pasos ss sencillos que te los dejé publicados justamente acá al final, que es el cómo importarla junto a el paso a paso de todo lo que hay que hacer si es que quisieras hacerlo de cero. Ahora sí te voy a mostrar cómo funciona. Es importante que entendamos que existen dos escenarios. Tenemos el escenario uno, que es el que nos crea el reel directamente, es decir, el reel más todos los promps. Y tenemos el escenario dos, que es el que literalmente nos sube el reel y nos combina lo que es la música con el video. Este escenario se va a ejecutar solamente cuando se haya terminado de generar el video. Es decir, primero vamos a mandar a hacer el video, es decir, va a comunicarse con el servidor a través de Freepix, se va a comunicar con Cllink y le va a decir, "Oye, mándame a hacer el video. Vamos a esperar un ratito y una vez que esté listo, es decir, en un transcurso generalmente de 4 o 5 minutos, se va a ejecutar el segundo escenario a través de lo que se conoce como un webhook." ¿Okay? Entonces, mientras se está creando el video, se mandó a hacer, va a esperar y cuando se termine de hacer y el estado pase de en proceso a completado, se va a ejecutar el segundo escenario que está acá. Okay, ahora sí que sí vamos a ver cómo funciona este escenario. Lo primero que vamos a hacer es vamos a entrar acá y vamos a importar el primer blueprint, ¿ya? O también puedes ir copiándolo porque te voy a ir mostrando todo paso a paso, pero vamos a importar el primer blueprint. Y esto lo vamos a hacer con la función de search rose. Search rows vendría siendo esta que aparece justamente aquí. Este es el trigger y esto es lo que va a gatillar el primer escenario. O sea, es la primera cosa que se va a ejecutar cada vez que le demos run o cada vez que elijamos una frecuencia en específico. Vamos a agregarle un filtro y el filtro va a ser cuando la condición es igual a cero, es decir, cuando no se ha publicado, no se ha subido. Vamos a tomar uno, ¿verdad? uno que está acá de esta fila o esta columna que aparece acá. En este caso vamos a tomar este que nos aparece aquí porque es el primero que sale con cero. Lo que vamos a hacer después es vamos a crear el prompt para poder generar la imagen. Cabe destacar que esto no es una automatización que hice 100% yo, sino que hay otro creador de contenido que sí armó una automatización super parecida, pero yo le hice bastantes cambios y le hice una especie de modificación a todo el contexto que está acá. Este prompt para crear la imagen si es un prompt que creó él directamente. Así que gracias Mohamed y es esto que está acá. Imagina que hay pequeños trabajadores que están haciendo esto. Queremos que el output sea en formato Jason y que lo hagas de la idea del video que está acá, es decir, de esta idea del cup of coffee o de la taza de café. Luego le damos un ejemplo de output que estamos buscando y que la respuesta sea en formato Jason. Ya, esto no tiene que ser 100% así, no es completamente necesario, pero sí funciona bastante bien. La salida puede ser de texto y no va a haber absolutamente ningún problema, pero este prompt que acabamos de crear acá a través del create a completion también, por supuesto, te lo dejé publicado aquí, ¿okay? Que es este mismo que podemos llegar y copiar. Luego vamos a mandar a generar la imagen a través de Freepck usando el modelo de imagen 3. Paréntesis, si es que no has conectado tu cuenta de Open AI, puedes hacerlo yéndote a agregar aquí arriba y pegando la API Key. Esta API Key la puedes encontrar en exactamente platform. Openai y yéndote a API Keys aquí, ¿okay? Le das a crear nueva llave secreta y le das a entrar y agregar acá. Vamos a hacer exactamente lo mismo para Freepic. ¿Okay? Freepic es la plataforma que vamos a usar para conectarnos con distintos modelos de inteligencia artificial. Queremos conectarnos con imagen tres, que es el que nos ayuda a crear las imágenes, que es el modelo de Google. Y nos queremos conectar con Cling, que es el que vamos a usar para generar los videos y darle vida o animar estas imágenes. Y las dos las vamos a hacer a través de Freepic. Aquí arribita te dejé también los links, te los voy a dejar en la descripción, pero si apretamos acá Freepck AI, vamos a poder crearnos una cuenta o entrar con una cuenta en específico. Si nos vamos acá al App Home, podemos apretar el get free API key. Una vez que estemos acá, podemos crear nuestra API y hacemos la conexión. justamente acá nos vamos a agregar, le ponemos un nombre y pegamos la API Key y listo. Después aquí, bueno, todo esto ya va a estar preconfigurado, pero igual te voy a decir exactamente lo que hay que poner. En el URL tendríamos que hacer el llamado porque estamos haciendo un request a un modelo en específico. En este caso, ¿qué estamos haciendo el request? A Imagine 3. Podría ser Imagen 4 si es que está disponible acá, pero esta es la lógica. Okay, te dejé el link acá justamente de imagen 3 nuevamente, pero lo puedes encontrar en freepic. com documentación y es esta info que está acá, text to image, imagen 3 y simplemente la pegamos acá. Vamos a hacer un método post, es decir, vamos a mandarle una información y que le vamos a mandar, bueno, esto que está acá, el prompt que generamos previamente. Vamos a esperar unos segundos porque le mandamos hacer la imagen, pero no se generan instantáneamente. Entonces, vamos a esperar 15 segundos a esperar a que tengamos una respuesta y después vamos a extraer la imagen que está acá. ¿Cómo la vamos a extraer? Bueno, vamos a usar el mismo URL que pusimos antes, pero vamos a agregarle el Task ID. Cada vez que se genera una imagen o se manda hacer algo en específico, se crea lo que se conoce como un Task ID. Task ID es un identificador único para cada solicitud que le hacemos a los distintos modelos. Entonces, le vamos a poner acá nuevamente el mismo URL de antes, no hay que ponerle.com. etcétera, porque al haber hecho esta identificación así ya viene prehecho. Si es que estuviésemos haciendo un make request o un get file o absolutamente lo que sea, un módulo HTTP sí tendríamos que ponerlo, pero como hicimos la conexión así no tenemos que hacerlo y tampoco tenemos que poner la API porque ya hicimos la conexión previamente. Entonces ahora vamos a usar un método get para extraer la imagen. Esto nos va a dar el output, que vendría siendo la imagen que acabamos de generar, que para este caso fue justamente esta que está acá. El siguiente paso es descargar la imagen para que podamos usarla, porque en el fondo generamos la imagen, pero muchas veces la imagen queda en la nube y necesitamos pasarlo a un formato en el que podamos usar y que podamos tener como URL. El siguiente paso es el que está acá y es crear el prompt del video del re. Entonces el prom va a ser el mismo también. Nuevamente te lo dejé acá, pero Benja, no me hagas entrar a tu comunidad para tener las cosas tranqui. Puedes entrar 7 días completamente gratis y no se te va a cobrar absolutamente nada. O sea, literalmente puedes entrar, descargarte toda esta información y después salirte y nunca más nos vamos a volver a ver. Pero si quieres puedes quedarte también y puedes empezar a conectar y ver estrategias que funcionan con gente que le ha resultado en una comunidad que actualmente tiene más de 900 miembros y que todos estamos con un mismo objetivo, que es ahorrar tiempo con estrategias que funcionan. Entonces, te dejé justamente este prompt que está acá. ¿Okay? Entonces, el prompt básicamente te dice como, "Oye, esta es la imagen con la que trabajamos. Necesito crear un video o una motion o un movimiento para este video. Okay, quiero que tu output sea en esto, es decir, que sea en formato Jason. Y esta es la imagen con la que trabajaremos. ¿Qué imagen? Ah, el geta file que conseguimos antes, que era la imagen que descargamos previamente, que es esta de acá. ¿Por qué le damos la imagen? porque tiene que entender un poco de qué es la imagen y de qué es el contexto para poder crear el video. Luego aquí hay un ejemplo de un pequeño output de cómo sería y está la respuesta que la queremos en Jason. Ya, nuevamente puede ser en texto, no hay problema si es en texto. Nos gustan las respuestas en Jason porque nos encanta trabajar con Jason porque es un poco más ordenado. Y le vamos a dar a guardar. Luego viene la parte de crear la estructura Jason para poder hacer el llamado en específico. Ya aquí lo que estamos haciendo es estamos estructurando parte de la data que estábamos teniendo antes para poder hacer el llamado a mandar a hacer el video, porque eventualmente vamos a tener que hacer un oye, necesito que me crees un video en específico que tenga estas características, pero ¿cómo podemos pasar eso a variables? Bueno, con este módulo que está justo antes que es el crear estructura Jason para Freepck, específicamente. Toda esta información la puedes encontrar justamente acá y es el cómo lo vamos a crear. Esta parte sí vas a tener que hacerla tú, que es si es que recién importaste en la plantilla que vamos a ver. Esta parte no se va a importar porque necesitamos crear una data estructurada en específico. Para eso lo que vamos a hacer es vamos a irnos a agregar, vamos a generar una nueva data estructurada, te lo voy a poner acá y vamos a agregar cuatro íems en específico. ¿Qué ítems? Bueno, veamos cuáles son los ítems con los que tenemos que trabajar. Primero la imagen, después el prom, después la duración, etcétera, pero no lo queremos agregar así porque no tendríamos que poner todo esto. Entonces, en vez de agregarlo directamente ítem a íem, lo que vamos a hacer es vamos a irnos a generar. Vamos a irnos acá y vamos a pegar exactamente esto que está aquí. Vamos a copiar el código y lo vamos a pegar en sample data. Una vez que estemos acá, le vamos a dar a generar. Cuando le das a generar, te debería salir algo así, ¿okay? Pero si por alguna razón no te funcionó ese código que está ahí, simplemente puedes irte nuevamente a agregar, lo vamos a hacer video dos y le vamos a dar a adem. ¿Qué vamos a agregar? Bueno, primero la imagen, requerido, sí, después vamos a hacer lo mismo con el prompt, ¿verdad? tipo texto requerido. Sí. Después vamos a hacer lo mismo con duración. Después con la escala CFG, que en el fondo vendría siendo como qué tanto quieres que o qué tan fiel quieres que sea la imagen al texto, el texto a la imagen. Puedes jugar con ese parámetro. Después puedes ir con el webhook URL y después con el negative prom que vendría siendo literalmente como su nombre dice el opuesto del prom que funciona superb. Una vez que estemos acá, vamos a empezar a reemplazar las variables que teníamos previamente, que vendría siendo acá el body data generated. Aquí tenemos la imagen, ¿verdad? El URL. Aquí tenemos el prompt que acabamos de crear, la duración, que es lo que estamos buscando, y en fin. Okay, vamos a rellenar todos estos datos justamente acá. Y esta parte es super importante porque si estás importando la automatización, necesitamos ejecutar el segundo escenario. ¿Recuerdas? El segundo escenario solamente se va a ejecutar una vez que se termine de generar el video. El video se demora 4 o 5 minutos en ejecutarse, por eso no armamos todo en el mismo escenario. Entonces, el webhook URL, que es el que está acá, vamos a tener que ponerlo con el segundo escenario que importamos, que vendría siendo este de acá, ¿okay? O sea, importas el segundo escenario, copias el webhook y lo pegas literalmente acá. No te preocupes porque igual vamos a volver a esta parte, pero es super importante que sepas eso. Y después tenemos el prom negativo. Le vamos a dar a guardar. Y ahora sí podemos irnos a la parte de generar el video. Vamos a abrir un make an apicol, vamos a generar la parte del Freepic o la parte de hacer el llamado, mejor dicho, a Clink Pro y vamos a hacer un método post, es decir, le vamos a mandar información. ¿Qué información le vamos a mandar? Bueno, esta que acabamos de generar acá, esta que tuvimos que estructurar, que eran muchas cosas, que era la imagen, el prom, en la duración, qué tan fiel quieres que sea esto, el webrl, etcétera, ¿ya? O sea, literalmente todas las cosas que mandamos acá se las vamos a mandar estructurados de una manera en específico, que es todo lo que está acá. Vamos a mandarle esto y le vamos a hacer el post y vamos a seleccionar el Jason Stream, que es lo que acabamos de hacer, que vendría siendo la imagen y todas esas cosas. Arriba en la parte de URL vamos a poner Clink Pro. Y bueno, puedes estar viendo este video más adelante y puede haber un mejor modelo e o una nueva versión de Clink. Y para ver eso, simplemente puedes entrar acá a la documentación de Freepck y te puedes ir a la parte que sale video Generation API. Actualmente estamos usando el Clint Pro 1.6, pero este es el URL que necesitamos. Entonces, si es que llegamos y lo copiamos, podemos volver acá y volvemos a literalmente a pegarlo acá. ¿Okay? ¿Por qué razón no estamos usando el appreep.com? Porque ya hicimos la conexión previamente eh a través de la conexión cuando pusimos agregar. Si estuviésemos usando un modelo HTTP o un request http, sí tendríamos que usar el link, pero como no lo estamos haciendo, para este caso no es necesario. Entonces, le vamos a dar a guardar y vamos a pasar al siguiente paso, que es crear el prom de la música. Aquí tenemos esto que está acá que va a ser un mensaje. Usamos el modelo 4.1 mini, pero en verdad podríamos usar literalmente cualquiera, o sea, es crear un pront. En este caso prefiero usar uno más económico, no más. Y tenemos acá el contenido que le vamos a poner, que es el video script. Esta parte es importante, este es el image. Vamos a seleccionar acá el http get a file que acabamos de generar para darle contexto de cuál es la imagen. Podríamos mapearla también, pero creo que el get file funciona bien y es más simple. Después vamos a crear el caption de Instagram. ¿Recuerdas que cuando subimos esto hay un caption que aparece acá? Bueno, aquí vamos a directamente crear el caption de Instagram. Ahora el caption está en inglés, pero podríamos hacerlo en español, en inglés, en lo que queramos. Ya esto al final la idea es poder hacerlo lo más genérico posible o ahí depende de la estrategia que quieras seguir. Si quieres elegir un nicho en específico o quieres empezar a monetizar después algún tipo de cuenta en PIN. Okay, le vamos a dar a guardar y vamos a el último paso de la primera automatización. En este paso es s super importante. Una vez que se ejecute todo esto, recordamos que mandamos hacer el video, pero necesitamos después recuperar ese video. Bueno, para eso vamos a usar lo que se conoce como el data store o la memoria interna de Me. Vamos a crear un data store en específico. Okay, para eso vamos a irnos acá y probablemente no tengas un data store creado o quizás sí, pero vamos a guardar las variables con las que queremos trabajar en el futuro. ¿Por qué? Porque cuando trabajemos con esta segunda automatización, necesitamos decir como, oye, ya, ¿cuáles son las variables con las que tengo que trabajar? Ah, ya, mira, necesito el ID del video que mandamos a crear, que nos lo dio acá, una vez que se manda, que vendría siendo justamente este de acá. ¿Qué más necesitamos? Bueno, todos los proms que creamos. Creamos el prom de la música, creamos el prom del caption, pero todavía no mandamos a hacer la música, todavía no subimos el caption, por eso los vamos a guardar en una fila. Para hacer eso, nos vamos a ir a agregar y vamos a crear una nueva data structure. Aquí le podemos poner reels 2, da igual, y vamos a crear una nueva data structure. ¿Cómo lo vamos a hacer? Bueno, pongámoslo acá. Data estructurada, tiny workers reels. Le podemos poner lo que queramos. Agregar íem. ¿Qué es lo que queremos guardar? Ah, ya, el ID del video, ¿verdad? ¿Qué más queremos guardar? Queremos guardar el prom de la música. Podemos ponerle descripciones si es que es necesario. ¿Qué más queremos guardar? Queremos guardar el caption del Instagram. Queremos guardar el número de la fila. Ya, así se entiende. Okay, vamos a darle aquí a guardar en este caso y le vamos a poner cuánta data storage queremos que llegue a usar. Como estamos guardando puro texto, da igual, lo puedes dejar en uno y te aseguro que no vas a llegar a cumplirlo. Además que generalmente tenemos super poco storage en make, así que puedes dejarlo en uno. Okay, una vez estando acá, va a ser esto y empezamos a asociarlos. Efectivamente, el music prompt vendría siendo este prompt que está acá, el caption de Instagram vendría siendo este que está acá. Y en fin, voy a volver al original para no tener que remapear las variables. Y listo. Una vez que tengamos todo esto, toda la primera parte de la automatización va a estar lista, es decir, buscar el reel, generar la imagen, mandar hacer la imagen, esperar, extraer la imagen que creó, descargar la imagen que creó y crear los proms, el prom del reel, del video, de la música y el caption de Instagram y mandar a hacer el video. Una vez que mandamos a hacer el video, vamos a ver que de hecho, si es que entramos justamente acá, mandamos a hacer el video al principio de esta grabación que fue a las 6:57, pero se demoró 5 minutos, 6 minutos en generar el video y ahí recién mandó una señal para que se ejecute el resto de la automatización. Entonces, una vez que recién estuvo completado, se empezó a ejecutar el resto de la automatización, ¿okay? es decir, buscar la información, extraer la información, crear la música, descansar, combinar los videos y en fin, ahí vamos a ver esta automatización y vamos a abrirla. Vamos a asumir que importaste esta automatización apretando los tres puntitos y aquí sí hay que agregar un par de variables más. Lo primero que vamos a hacer es vamos a crear un nuevo webhook. ¿Qué webhook vamos a usar? Bueno, puedes usar uno ya existente o puedes crear uno nuevo. Recomiendo que crees uno nuevo. Le das a agregar y vamos a copiar este webhook. Luego vamos a volver a la automatización anterior y vamos a reemplazarlo acá. Esta parte super importante porque si no nunca le va a avisar que ya se terminó de crear el video. Porque recordemos esta segunda automatización que estamos viendo acá es para subir y compilar el reel. La primera es para crear los promps y mandar a generar el video. Entonces, acá volvemos y asumiendo que se terminó de generar el video, vamos a pasar al segundo paso, que es buscar la información que guardamos previamente. Si es que apretamos el M que aparece acá y nos vamos a las datas stores o a donde guardamos la data en make, podemos abrirlo y podemos ver todas las generaciones que hemos hecho. En este último caso, que es el que acabamos de hacer, era este que está acá. guardamos el ID del video, guardamos el prompt de la música y guardamos la información o el caption que queríamos usar. Entonces, lo que tenemos que hacer es extraera, tenemos que buscar. ¿Y qué vamos a buscar? Bueno, el ID del video en específico, ya porque se llamó a este webhook, mira, vamos a correrlo una vez nuevamente para este que está acá, que es cup of coffee, y lo volvimos a mandar al webhook, que aparece acá. De hecho, acabamos de esperar unos minutos y efectivamente acabamos de ver que lo recibimos en el segundo escenario. ¿Qué recibimos? Bueno, le mandamos a hacer una taza de café. Abrimos esto, podemos ver que la imagen ya fue generada y la podemos abrir y la podemos revisar justo acá, que en mi opinión está genial, genial. Y efectivamente ahora está haciéndonos todo el otro proceso. Y en fin, se subió nuevamente al Instagram, lo podemos revisar. Acá tenemos la imagen de los trabajadores acá en la taza de café que está buenísimo, buenísimo. En fin, ahora sí, ¿cómo funcionó este proceso? Bueno, le mandó la señal al webhook que hicimos y aquí le pusimos un filtro. ¿Cuál es el filtro? Que cuando el estatus sea completado, es decir, que se mande una señal al webhook con el estatus completado, pase a los siguientes pasos. ¿Por qué es tan clave esto? Porque muchas veces vamos a ver si es que abrimos otras automatizaciones que se mandan dos señales, una por ejemplo a las actualicemos esta página 48 y otro a las 54. Pero, ¿qué pasó acá? Mandamos una señal, pero le mandamos una señal de que estaba en proceso, de que estaba en construcción, ya que el estatus, si lo podemos ver acá, estaba in progress y nosotros no queremos seguir con la automatización si es que no está listo, porque no tendríamos con qué video trabajar. Así que por eso mismo ponemos un filtro acá que es si es que el estatus está completado. Pasemos al siguiente paso. ¿Cuál es el siguiente paso? Bueno, extraigamos toda la información que guardamos previamente en la automatización número uno, es decir, todo lo que guardamos en la data store, que vendría siendo el ID del video, el número de fila, el prompt y el caption. Vamos a poner un search record. Vamos a extraer todos esos parámetros, pero solamente del Task ID que sea el específico que mandamos. Por eso ponemos otro filtro acá. en el search y cuando lo extraemos todos estos parámetros nos va a devolver los mismos que guardamos previamente. El siguiente paso es crear la música y para eso vamos a usar una aplicación que se llama Music F. Existen distintas aplicaciones, podemos usar Suno, podemos usar Music F, en fin, esta funciona bastante bien en lo personal tienes eh incluso créditos gratis que puedes usar y Music F es esta de acá. De hecho, justamente también acá te dejo el link, eh, también me voy a encargar de dejar todo en la descripción, pero tenemos el API de Music F. Si es que entramos acá, podemos ir a probarlo gratis, nos podemos ir a la parte que sale API y podemos crear nuestro API. Okay, vamos a poner el app de Music File y vamos a hacer un request en específico. Como no hicimos conexión nativa, vamos a tener que escribir este header que es authorization y pegar nuestra API key. Vamos a ponerle Jason. ¿Y qué es lo que vamos a crear? Bueno, el prom de música que creamos previamente que lo guardamos en el data store. ¿Cuánto queremos que dure? Bueno, la duración en específico que va a ser 10 segundos, porque eso es lo que le pedimos que dure el video. Después vamos a hacer el llamado acá. Eh, vamos a darle a guardar parcial la respuesta. Guardamos y aquí podemos ver que se generó efectivamente nuestra música, nuestra canción. Este es el file URL. De hecho, podemos ir acá y en teoría podemos escuchar y descargar la canción que acabamos de crear. Después, el siguiente paso es combinar el video con la música directamente que acabamos de crear. Descansamos 15 segundos para que haya una pausa entre medio del video. Y el video que generamos es este generated. Este es el que recuperamos. Si es que lo abrimos acá, vamos a poder visualizarlo, que es literalmente el que subimos a Instagram, pero sin música. Entonces, acá lo que vamos a hacer es vamos a recuperar este video y lo vamos a combinar en un solo video con el audio que generamos. ¿Cómo vamos a hacer eso? Bueno, vamos a usar una herramienta que se llama segmin, que te permite conectarte a distintos modelos de inteligencia artificial. Y en este caso vamos a hacer un merge audio y vídeo, es decir, una combinación de video y audio que te genera un solo video de vuelta. Vamos a irnos acá. Voy a bajar y vamos a cloudsegmin.com. Puedes buscar segmino. Y vamos a crear una nueva API key. Dentro de segmin. Podemos empezar a crear distintos workflows. Es super entretenido. Podemos jugar con distintos modelos de IA. Ya, o sea, hay varios varios playground entretenidos de de todas maneras es algo interesante si te quieres meter, pero lo que vamos a buscar es segment vídeo audio en específico, si es que no quieres apretar el link. Vamos a irnos acá, vamos a abrirlo y vamos a darle acá a la parte que sale API. Aquí tenemos toda la información de lo que nos pide, ¿verdad? que sabemos que es un X apik key, un input audio y toda la data que necesitamos, pero para este caso es simplemente get your AP key. Vamos a crear, vamos a copiar nuestra API Key y la vamos a poner justo donde sale X key, que es esta de acá. Una vez que estemos acá, vamos a ponerle el request content, que es el input vídeo y el input audio. Es decir, queremos mezclar estos dos en uno, fusión. función y listo. O sea, una vez que está todo esto acá, eh, ya no necesitamos nada más. Jason Input y este también se demora un poco, se puede demorar un minuto o algo así, pero este es muchas veces uno de los modelos que te puede o uno de los llamados API que te puede presentar problemas. Entonces, por eso lo mejor que podemos hacer es crear un error handler. Un error handler lo que hace es romper, ¿verdad?, o manejar los errores que tenemos en las automatizaciones de distintas maneras. Por ejemplo, si le agrego un error handler acá, podemos parar una automatización, podemos eh hacer un commit, es decir, que siga la automatización sin importar lo que pase, ignorar los errores y es s super útil para las automatizaciones. ¿Okay? Para este caso vamos a crear un error handler que es un break. El break va a ser cuántas veces lo vamos a intentar. E después lo que vamos a hacer es subirlo a Dropbox directamente, que vamos a subir, bueno, el video que nos acaba de generar. Vamos a usar el módulo upload file y vamos a elegir una carpeta en específico. Cuando hagamos la conexión de Dropbox es super intuitiva, te va a pedir un par de cosas, pero en general funciona s super bien. Si es que tienes algún problema con los scopes, puedes resolverlo acá directamente. O sea, hemos tenido personas que han tenido problemas con los scopes, que son los permisos, de qué tanta información o qué tantos permisos le podemos dar a Dropbox. Y ese problema ya lo resolvimos justamente aquí. ¿Okay? Eh, puede ser que te pase, puede ser que no, pero en el caso de que te ocurra, lo tenemos publicado ahí en la sección de preguntas. Entonces, ¿qué vamos a subir? Bueno, el nombre del video, ¿verdad? El ID.m4. ¿Y qué es lo que vamos a subir? La data que acabamos de recibir de el makeup request, ya del llamado que hicimos a segmind para el modelo. Después lo que tenemos que hacer es poner un link de create o update a share link, que vendría siendo el path display que acabamos de crear. Esto en el fondo, la razón por la que hacemos esto es porque subimos datas, subimos números y los subimos al Dropbox, pero todavía necesitamos un URL que sea como descargable, algo que nos funcione para que Instagram sí lo pueda realmente usar y entender. ¿Okay? Entonces, vamos a ponerle el pad display, ya con este acá, create update a share link y finalmente lo vamos a publicar en Instagram. Esto es literalmente agregar Instagram y crear un reel, que vendría siendo esto de acá. ¿Qué es lo que vamos a crear? Bueno, o qué es lo que vamos a subir? El vídeo URL de la descarga que acabamos de crear en el módulo anterior, es decir, este de acá. Entonces, vamos a usar ese caption acá y si quisiéramos podríamos ponerle una portada en específico, que podría ser si quisiéramos, no sé, la portada de la imagen que acabamos de crear, ¿verdad? Que vendría siendo esta de acá. eh no lo vamos a hacer porque para qué y después podemos elegir si es que lo queremos compartir en nuestro inicio o no. Para este caso le voy a poner que sí porque si no no nos aparecería en el feed y solamente en los reels. Okay, finalmente vamos a actualizar el estado a listo con el update a road, es decir que cuando se termina de ejecutar esto se va a cambiar del cer ala. ¿Para qué? para que la próxima vez que ejecutemos la automatización, la primera, pueda buscar el primer cero y no nos vuelva a subir la misma publicación una y otra y otra vez. Entonces, aquí ya tenemos todos los pasos listos. Si te llegó a presentar algún problema o algo, publícalo en la comunidad, feliz de acompañarte y ayudarte en lo que podamos. Un problema que podéis tener acá también es eh si es que no te está mandando la información al webhook, puedes ir directamente editar la data structure y poner tu webhook además acá, ¿okay? Eso también puede ser si es que no se llega a mandar la información. Recordemos que se va a llamar a ese webhook cada vez que haya un cambio en el estado de la creación del video. Es decir, si está creándose, va a llamar al webhook, si es que está en proceso, va a llamar al webhook, si es que está creado y está completado, va a llamar al webhook. ¿Okay? Y ahora si es que quisiera dejar esta automatización corriendo al 100%. Bueno, lo primero que haría sería guardar la automatización. Por favor, háganse el hábito de guardar las automatizaciones y vamos a darle a dejar corriendo al segundo escenario. Okay, el segundo escenario siempre tiene que estar activo. El primer escenario, este que está acá, es el que vamos a elegir que se haga. Supongamos que quiero que cada 15 minutos se ejecute el escenario, pero ahora solamente tengo uno, entonces y quiero crear un poco más. Voy a entrar a HRGPT y literalmente le voy a decir, créame una lista de objetos para abajo. Si tienes un nicho en específico, puedes ponerle el nicho si quieres hacer objetos de, no sé, solamente de tecnología, hace solamente de tecnologías, pero en fin. Aquí nos acaba de crear una lista con 120 objetos y los vamos a seguir. Y vamos a seguir para aquí abajo. Voy a pegarlos acá y le voy a decir, "Dámelos en una tabla porque me los pegó como con un pequeño espacio." Los voy a copiar, los voy a pegar acá. Voy a eliminar esto y voy a poner puros ceros hacia abajo. Ya. Para definir el estado de que no se han subido. Me intriga este que es el Rubik Cube. Quiero ver qué pasa. Y lo vamos a poner acá en vez de Burger. Y lo vamos a dejar en cero. Y ahora sí, si quisiera dejarlo publicando, no sé, creamos 120, pero si quisiera subir cuatro por día, podría ser algo como que se suba cada 360 minutos, por ejemplo, y que se active el escenario. Y si es que vemos acá, el escenario se está ejecutando exactamente en este momento y se va a seguir ejecutando cada 6 horas, es decir, por un mes completo, ya que tenemos 120, se va a subir cuatro reels diarios cada 6 horas religiosamente. ¿Okay? Y aquí podemos ver que se subió el reel ya después de 5 minutos. Vamos a ponerle audio. Y bueno, no sé por qué hay explosiones, pero está genial, genial. Y esto lo va a ser para cada uno de las cosas. Ya recuerda, lo puedes anicharr, puedes hacer absolutamente lo que quieras y son solamente estas dos automatizaciones que están acá. Ya, esto es super power, es superpotente. De hecho, de hecho está justamente metido en el celular y vi que existen eh páginas que directamente están cobrando mensualidades de más de $40 para crear este tipo de videos, ¿ya? y es eh tiene más de 400 ratings, es decir, debe tener miles y miles de descarga y te cobran mensualidades de $40 por hacer exactamente y literalmente lo que acabas de ver en la automatización que te acabo de mostrar. Así que sí, ahora, sin más que decir, eh si quieres descargarte estas plantillas, puedes entrar a Imperio Digital. Actualmente tenemos una prueba gratuita de 7 días, es decir, puedes entrar, probar completamente gratis por 7 días y si sientes que es para ti, te puedes quedar y si no, cancelas antes del día 7 y no se te va a cobrar absolutamente nada. Imperio Digital es la comunidad donde tenemos automatizaciones, hablamos de inteligencia artificial, tenemos Meli que se acaba de juntar con otro miembro de la comunidad y ahora están armando negocios juntos. Esto es realmente una locura. Okay. Si entramos al Classroom tenemos las automatizaciones, que son muchas automatizaciones que hemos ido armando en conjunto con los blueprints, cómo crear aplicaciones con inteligencia artificial e incluso cómo podemos prospectar y redactar propuestas personalizadas. No solo eso, porque también tenemos todas las semanas una sesión de preguntas y respuestas, otra sesión de automatiza con Fran y muchas, muchas otras cosas que recomiendo que no te lo pierdas si es que quieres tomarte en serio esto de las automatizaciones. Yo voy a dejar corriendo esta automatización que te acabo de mostrar. La voy a dejar corriendo a ver qué pasa con esa cuenta de Instagram. Pero en fin, espero que lo puedas aprovechar. Y ahora sí, sin más que decir, te deseo mucho éxito y una muy feliz automatización. YouTube recomienda que veas este video que está acá.
