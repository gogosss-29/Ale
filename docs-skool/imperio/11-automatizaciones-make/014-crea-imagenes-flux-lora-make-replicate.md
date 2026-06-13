# 🔥Crea Imágenes FLUX LoRA + Make + Replicate

> Ruta: Automatizaciones Make › 🔥Crea Imágenes FLUX LoRA + Make + Replicate

**🎬 Vídeo (30.3 min):** https://youtu.be/lEEfaFbhW-Y

**📎 Recursos:**
- FLUX LoRA + Make

---

**En esta guía,** aprenderás cómo configurar una automatización completa para generar imágenes hiperrealistas utilizando [Make.com](http://Make.com) y modelos avanzados de inteligencia artificial alojados en Replicate, como un FLUX LoRA Dev. Este proceso te permitirá crear imágenes personalizadas de altísima calidad con solo unos clics y llevar tu creatividad o tus proyectos al siguiente nivel.

Hasta ahora, en **Imperio Digital** hemos utilizado el módulo de **Generate Image de DALL-E 3** en numerosas automatizaciones con resultados increíbles. Sin embargo, hoy damos un paso más allá al implementar un método que utiliza un modelo mucho más avanzado y con resultados significativamente mejores. Lo mejor de todo es que este sistema es súper práctico: basta con copiar y pegar los 4 módulos principales directamente en cualquiera de tus automatizaciones para comenzar a utilizarlo de inmediato.

**Este es un auténtico game-changer** para todos los que buscan generar contenido visual de calidad profesional de manera eficiente y escalable. Te recomiendo que no te pierdas esta guía, ya que cambiará la forma en que trabajas con imágenes en tus flujos de automatización.   
-----------------------------------------------------------

Primero crearemos un nuevo escenario en [Make.com](http://Make.com) y crearemos un nuevo Custom Webhook. (Si no quieres armar la automatizacion paso a paso, puedes importar el escenari oque aparece al final de esta guía y luego creas el nuevo webhook).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6bbe2c504602474190ec085cad1e784c7d726172f99d42f4b9fc35c46094d4a9)

Lo copiaremos

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2495ba71b380418c863d2d738c7b83eeac467ca448c645aab5df5c8da52dc0af)

Luego entraremos a [bolt.new](http://bolt.new) y le daremos el siguiente prompt y reemplazaras el final de lwebhook y le agregarás el URL que copiamos previamente.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1df50f5c8d8f4f09868cdb1fdab094dac7d96fc8f0524c048f8c4f6e3da0ea13)

> Create a modern, minimalist, and dynamic interface for generating AI-based images from a prompt, ensuring the entire interface is in Spanish. The interface should have two main options:
> 
> Free Prompt: Allows the user to type in what image they want to generate.
> 
> Pre-designed Option: A specific selection called “BenCorde haciendo X” (e.g., "BenCorde teaching automations" or "BenCorde climbing a mountain"), where users can still type freely into the text input.
> 
> Structure and Design:
> 
> Header:
> 
> A striking title like "Crea tu imagen con FLUX LoRA."
> 
> Prompt Field:
> 
> A text box with a friendly placeholder: "Describe tu imagen ideal aquí…"
> 
> Action Button:
> 
> A visible and modern button labeled "Generar Imagen."
> 
> Pre-designed Section:
> 
> A secondary, highlighted option with a selector or alternative button to pick “BenCorde haciendo X.”
> 
> Dynamism and Movement:
> 
> Add micro-interactions when hovering over buttons and fields (e.g., soft and subtle hover effects).
> 
> Include a modern loading animation (spinner or progress bar) while the prompt is sent to the webhook.
> 
> Highlight successful prompt submission with a brief message like "Imagen enviada al servidor."
> 
> Style:
> 
> Typography: Modern sans-serif.
> 
> Color Palette: Minimalist (white, black, and a soft accent like blue or gray).
> 
> Spacing: Generous to prevent visual overload.
> 
> Data Structure (Webhooks):
> 
> The prompt data should be sent in a JSON format, where the input field is labeled "prompt".
> 
> The JSON structure should be sent to the following webhook:
> 
> [INSERT WEBHOOK HERE]
> 
> In summary, I need an interface with the specified style and features, where the user input field sends structured data labeled as "prompt" to the webhook. All text and UI elements should be in Spanish.

Esto me generó el siguiente resultado:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/eb783fd7239a4687bcde1222b0bfc53af28eed58c8004da79daf3a45f73dc0f1-md.png)

Luego, correremos el escenario en Make

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cd3fc62a349147b29e4a0c4813ae381464dac7ccb51f4eb2b53883dc53a4ef17)

y mandaremos la información en la interfaz de bolt

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b27307f4187f4d02aeb749a982724c71589bd13505ac4aa0baefc0a353260d87-md.png)

para verificar que estamos recibiendo la informacion en el escenario

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/95fa9416750540c58762d90ec6269e126ee3caa2a7f742e2b001b51d4ee31932)

Ahora si podemos comenzar a armar la automatizacion... (recuerda que puedes importarla, pero igual te mostrare el paso a paso aquí)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/bd379ccf8edc43c0b58be80d95489898d262dfc49d114eea9ca9e057bed9d80b-md.png)

La imagen de arriba es lo que queremos llegar a... así que lo primero que agregaremos es un "create a chat completion" de OpenAI 

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/87c2ae963c5a4436a6556acd193a2caa3b9bf82257e8485a80e3786280fbfb62)

y le pegaremos el siguiente prompt (está escrito abajo):  
  
TIP: Pegarlo con CTRL + SHIFT + V para mantener el formato

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5eeeea7644c646dab70337a35b4e8c530979af702cf1447fbba010357e48fcae)

Aquí debemos reemplazar las variables en negro, por la nueva variable que recibimos en el webhook para que se pueda hacer sola:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/df5b91fd8cf84319873cce4cb670312a15c3f11b21e54b259e7885feabf95961)

TIP: Pegarlo con CTRL + SHIFT + V para mantener el formato

> "prompt" variable example for the input "superman": Bencordero as Superman, his red cape billowing behind him. He flies over a city, the sun casting a golden glow on the horizon. His face shows unwavering determination as he prepares to save the world, embodying strength and heroism in his classic blue and red suit.
> 
> The prompt always will start with the keyword "bencorde" if it is mentioned in the user input prompt. If bencorde is not mentioned, do not include "bencorde" it in the prompt.
> 
> The user asked for a prompt with the input: {{9.prompt}}
> 
> I need JSON Output for the following.
> 
> ###Do NOT include the symbol "`" or "```json" or "```" on the output.
> 
> Your output should be the following JSON Prompt:
> 
> {
> 
>   "version": "091495765fa5ef2725a175a57b276ec30dc9d39c22d30410f2ede68a3eab66b3",  "input": {
> 
>     "prompt": " (replace this parenthesis with a generated prompt of bencorde (if mentioned) related to: {{9.prompt}}) ",
> 
>     "hf_lora": "bencorde3/bencorde3",
> 
>     "num_outputs": 1,
> 
>     "aspect_ratio": "16:9",
> 
>     "output_format": "png",
> 
>     "guidance_scale": 3.5,
> 
>     "output_quality": 100,
> 
>     "num_inference_steps": 28
> 
>   }
> 
> }

Nota: Si este prompt no te funciona, quizás tendrás que cambiar la "version", que ya te mostraré más adelante en esta guía donde puedes sacarla

Nota 2: Puedes ajustar los parámetros del final como el numero de inference steps, el output si lo quieres en .jpg o el aspect ratio a 1:1 si lo quieres cuadrado, por ejemplo

Nota 3: Si quieres ponerlo con imágenes de tu cara, puedes ajustarle el valor "hf_lora" a el modelo de IA que tengas entrenado con tu cara y reemplazar todos los "bencorde" por el keyword que le tengas asociado al entrenamiento. El mio personal es "bencorde3/bencorde3" Si no conoces o no tienes un LoRA entrenado, puedes hacerlo viendo [esta guía de aquí](https://www.skool.com/imperio-digital/classroom/7efa4739?md=f9cd03c1b1ef4d02b273547b82d83a94)

Luego reemplazamos las variables para que nos salga en rosado, no en negro

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7cce0f41585847cba8bdd2e6f441581054d6a421f448426ea7969a997acc425c)

Luego agregaremos el modulo de Make a Request en HTTP

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/92791f9dff56425b88cc2fcd5a42d28405c39a7f4aca413a9f55ceef8324e244)

Y para encontrar tus propios campos, entraremos a nuestro modelo de Replicate LoRA (si no has visto o no has entrenado tu modelo, puedes hacerlo siguiendo estos pasos de [esta guía de aquí](https://www.skool.com/imperio-digital/classroom/7efa4739?md=f9cd03c1b1ef4d02b273547b82d83a94))

Entraremos a Replicate y lo primero que buscaremos será nuestra API Key. Para ello iremos a [Replicate.com ](http://Replicate.com)y buscaremos "API Tokens" arriba a la izquierda

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f296d7b2b5ae4a019fddd1eaf7868cd5d067c3cbb441487aaa32bc3c3b3ee40e)

Crearemos un nuevo Token

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1dd1c1ba128742479db920a99a277aba9e1d482167884af6a9726adbe8248f53)

Y crearemos un "Item" en Headers y lo pegaremos en nuestro módulo Make a Request seguido de "Bearer" (Bearer es el portador de la llave, quiere decir que cualquier accion o persona que tenga la llave podrá generar imágenes, por lo que es super importante que no la compartas). 

En Name le pondrás "Authorization" 

En Value le pondrás "Bearer [tu api key]"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/dc167bc67ddc4c95879aabbb09d732f823ebba3cb3d34e2f8a199b0dc99597e1)

Luego debemos irnos al modelo que queremos usar, para este caso usaremos el [FLUX Dev LoRA](https://replicate.com/lucataco/flux-dev-lora), pero la lógica para cualqueir modelo de IA en Replicate es la misma.  
  
Buscaremos el modelo que estemos buscando, para este caso

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6951c7b4cd164dd4880ac229ccd499dda09684d3693d4d9693e8425984fe554c-md.png)

Y nos iremos a API y HTTP:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/bf00f79e634c4fb2853f0548bb04e6b1edbf9599a4f844c7b950eada1c404172)

Aquí nos aparecerá el siguiente código, que es el mismo dependiendo de la versión que tengamos

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7cd0a689f87346d69a727bba136c1450c5ddc6566e2d423f82182fc4e06b8cb6-md.png)

Tendremos que copiar el siguiente URL

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0fb6e097a33c4e0783f75bbec8ced1569182eabdfefb4dc0be177d6941d873be)

Que es este mismo que está aquí abajito (te lo podría haber dado, pero prefiero que sepas donde buscar la info, ya que podría salir una nueva versión en el futuro y en el prompt inicial que le dimos a OpenAI, hay una parte que sale "Version". Asegúrate que el version es el mismo número que aparece aquí)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3cc27df0903745c5a52cff1009c5cb373f26bd30f3a94247915b822cc81c5558)

con el que pusimos en el prompt de OpenAI

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/75cf7310677244d68b1abdc663ea3d18e8ebf9ff665b4c1fa794c2905d0fd6e2)

para evitar errores futuros.

Retomando, volveremos al modulo de Make a Request HTTP

[https://api.replicate.com/v1/predictions](https://api.replicate.com/v1/predictions) (Esto va en URL)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/51d19c11f29b420a9ca9a7b3c9fe80d385823df4ab994bf2bd89bc2c2bef9e37)

Luego en Body Type le pondremos "Raw" y luego "JSON"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d8f52df31b50477aa2e52b1157e5b1d8f376b11afc1145c8b84ba9a24ad889c4)

Finalmente en el request content, pondremos el resultado de OpenAI

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/fc52c296dfbe4e5d9e4d9111070919c006e6c8bb9dfb4c95acc3ea3164fe7cec)

y en "Parse Response", le pondremos "Yes"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e15cb4c609f44d8c89b839261427981692d236cf73c64fbb9a4fb85636d40850)

Y por último, SUPER importante, tenemos que tener el request en "POST"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5582c9f5bf3d490ca1465af08515b108570bffd181fc4efeb3f1aa5999a45364)

Dandonos algo así

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b71cc521a8ee48a9a651a0f193906b6ff9f4c2013c3845ea91c6994a6bcd338e)

Lo que hicimos aquí fue hacer el llamado "POST" a mandarle la señal a Replicate. Si corremos solo esta autoamtización hasta aquí, nos comenzará a generar la imagen.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/bce3b0f48dde4d94953b499bd6e7fdc645bd5ef9b6204fde9f439ea0462449fa)

Verificaremos que está funcionando dandole a "Run Once" a la automatizacion y enviando un nuevo webhook o señal, que debería comenzar a ejecutarse en Replicate. Le damos a Run Once

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8328665dc6c44504bdafea0fb0b8cf5bcb7de33e9e1e43a3830ca42012a9d525-md.png)

Mandamos la señal en Replicate

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e6c5587c226141b59a2c4cae9baabc5c472c8f039d494bc4901f29e2045a5ea7)

Y deberia aparecernos el escenario así

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d425ded2e2934b9499a67643c445e7ef8acd8c4e00294959a69eb8b9fbca7e46)

y si entramos a Replicate debería habernos comenzado a generar la imagen

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f325a797c38e4ad2a4af29893cbe20b26bb607c2dd164986a4e7845e26645eb6)

Dándonos algo así...

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f4cce3a6983749d3ab00b8fbf3826f16e1a38825a7a441129b645e0153e248d0)

Pero la mayoria de las generaciones toman alrededor de 20 a 30 segundos como pueden ver

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0910bb12c3ca469b8be623f1c8bde38b657d79b0ad7649959569431aa5321c21)

por lo que tenemos que poner un moduolo "sleep" de 50 segundos, para asegurarnos que se alcance a generar antes de poder descargar la imagen

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8e0b20cc6ba34a989f07910af3b879d1fc90d5fe38ab406aa4c6bdbefe00b61a)

 que pausará la automatizacion por 50 segundos

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0abb4b366941413d9be628d4ec8b6f544ad8a46fc5834264865bd9f62731668f)

Luego, tenemos que extraer la información con otro módulo de Make a Request HTTP, pero por términos de simpleza y no rellenar todo de nuevo, duplicaremos el que ya hicimos con "clone"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b21c764765d5451e9a3ae5b9c00b5b18eeca66d8635d482887b6d0c83c486fbc)

Ahora le ajustaremos un par de cosas... Primero eliminaremos el URL y le podnremos el del URL que generamos anteriormente bajo "Data, URL's, get" (nota: si no te aparece, tienes que correr la automatizacion una vez antes)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2172c41f291a4cf7a01c5f5cc6d739aef09f3e15c5b54cdd9ace498725f99cac)

Luego, le cambiaremos el "Method" a "GET", ya que no queremos subir informacion, sino que queremos extraer informacion.

Bajo "Request Content" le eliminaremos lo anterior y lo dejaremos vacío... y nos debería quedar algo así

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/54bd6884d03e43feb65077d23fd1f7659686723abe7f4ed281f14aa1fae0fd57)

Ahora finalmente, si le damos a correr escenario, debería devolvernos el link. Hagamos la prueba, le dare a "Run Once" al Make, y mandare otro input.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e555c3a55b4647c1840f7323a3f45073397856abb8b341588db2c85aef0b4abb)

Y leugo en el resultado tras correr toda la automatizacion, abrimos "OUTPUT, Data, output y vemos el "1", habrá un link

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8fef5b3537d64e9e85d8f96e746183113ed1f784ed3d4b748bf18b3444aa4f7e)

Y si lo abrimos...

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3ed5aef070fe41beacd139db3e634c157621f39b96064e36856b4c80732171eb)

podemos ver la imagen que fue generada.

Ahora, podemos hacer lo que queramos con estas imagenes. Subirla a Instagram, animarlas con Runway, mandarla a un mail o lo que gustes. El límite es tuyo. Pero por fines prácticos, queremos visualziarlo en un Google Sheets.

Primero agregaré la info a un Google Sheets, por lo que pondré "Add a Row" en Google Sheets

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c47baab1f92447fc94a77a17faff3facad8166af6735481380e8ce9c7297659e)

y seleccionaré el spreadsheet ID

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/64a03dee262745959dce216c832a26894a5c18af483a491a8300dd7a8fefd594)

Bajo Prompt le pondré el prompt inicial

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5c6f6accb0824f928449d4345a972702dedc2b7550b1400489dcc9c4640ecefd)

y bajo Imagen le pondré el URL le pondré el output URL, (que solo lo podrás ver si vuelves a ejectuar la automatización completa), pero está bajo "Data, output, 1".

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/765ba124dddc4e72956f3361def76f4cf09638d72bed4d06a2dd94bee724824d)

Ahora guardaré, y cada vez que corra la automatización, se agregará nuevamente a un a un Sheets

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/55092700c9b54e8183b8aaa8088ffd5f42671f6b5234438badc17e5e0b03a365)

Asegúrate de dejar activa la automatización dando click aquí

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/fef784b89cf748429497200ee2c17797c55012d609e94f309f4c5f205fb40608)

También recuerda que peudes importar la automatización directamente desde aquí abajo.
