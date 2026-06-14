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

## 🎙️ Transcripción

a lo largo del tiempo he creado muchas automatizaciones que involucran la creación de imágenes esta que te crea contenido automáticamente y te lo publica en cuatro redes sociales distintas esta que te toma una noticia y te la adapta para publicarlo en las redes sociales esta que te crea libros personalizados para enviárselos después a clientes potenciales e incluso esta que te crea por completo un blog de wordpress y nos Crea una imagen relacionada al artículo pero todos tienen un mismo problema y es que las imágenes se nota muchas veces que son hechas con Inteligencia artificial Pero qué si te digo que he encontrado una forma para crear imágenes hiper realistas incluso de ti mismo y que no solo eso sino que las puedes meter dentro de tus automatizaciones porque Claro en el pasado hemos creado imágenes y nos dan cosas como estas pero algo pasa que toda la gente sabe que esto es hecho con iga Pero si te presentase un modelo que te crea imágenes como estas o incluso estas la cosa realmente cambiaría ahora que si te dijera que no tienes que generar un prom cada vez que lo haces sino que con una misma automatización podemos hacer 10 20 incluso 50 generaciones a menos de 3 centavos cada una Bueno eso es lo que vamos a ver hoy día vamos a aprender a vincular un modelo de Inteligencia artificial que es actualmente el más avanzado en generación de imágenes en mi opinión que se llama flux dev Lora y vamos a aprender Cómo podemos conectar Este modelo directamente a make para hacer absolutamente lo que queramos sea mandar un mail con una imagen imágen en específico sea publicar en distintas redes sociales imágenes hiperrealistas o incluso si quieres generar cientos y cientos de imágenes tuyas hechas con Inteligencia artificial y el potencial de esto es realmente enorme o sea podemos adaptar y entrenar modelos de Inteligencia artificial con fotos de un objeto en específico como esta taza por ejemplo y podemos crear cientos de imágenes extremadamente realistas con solamente un clic y después directamente vendérselo a alguien por ejemplo eliminándolas a un fotógrafo y obteniendo resultados de literalmente lo que ellos quieran y este es un servicio que se podría vender fácilmente en cientos de dólares Así que ahora sí antes de comenzar si no sabes quién soy Mi nombre es Benjamín Cordero y soy cofundador de la comunidad de imperio digital una comunidad donde nos dedicamos a ahorrar tiempo mediante automatizaciones sea porque las quieres implementar en tu negocio o porque las quieres vender tenemos decenas de automatizaciones listas para descargar e importar Y que comiences a usarlas ya y no solo eso porque también es un espacio donde vamos resolviendo tus dudas donde vamos conectando entre miembros y donde tendrás acceso a llamadas semanales con expertos en automatizaciones y lo mejor de todo es que puedes entrar a probar imperio digital por 7 días completamente gratis Si antes del día 7 sientes que la comunidad no es para ti puedes cancelar Y no se te va a cobrar absolutamente nada Ahora sí vamos acá antes de explicarte el paso a paso de cómo armarlo déjame mostrarte cómo funciona lo que vamos a hacer acá es vamos a recibir un webhook o un disparador instantáneo esto lo que va a hacer es nos va a generar un código en json que va a llamar directamente a nuestro modelo de Inteligencia artificial en replicate replicate es una plataforma que usamos para arrendar espacio en la nube o computing Power fuerza de computación entonces cada imagen por ejemplo se demora 20 segundos en hacer y nosotros estamos pagando esos 20 segundos que está corriendo el modelo de Inteligencia artificial cree una interfaz extremadamente simple con bolt para crear nuestra propia imagen Esto no es necesario pero creí que se iba a ver mejor Entonces si es que yo le pongo Ben corde en la torre ifel vamos a generar la imagen y va a empezar a correr la automatización si no sabes dónde estamos esta plataforma se llama make y es un lugar donde podemos conectar más de 10,000 aplicaciones y comenzar a crear trabajos y flujos automatizados de trabajo entonces aquí lo que hizo fue creó el código que es una plantilla que te voy a entregar que no tienes que hacer absolutamente nada mandó a crear la imagen como podemos ver aquí fue creada hace 44 segundos y después nos actualizó directamente Ben corde en la torre ifel si es que abrimos la imagen está directamente acá y después desde acá podemos hacer absolutamente lo que queramos si quisiéramos publicarla en instagram simplemente abriría Instagram nos vamos acá y le daríamos a crear una foto seleccionaríamos el URL que es este de acá y le crearíamos algún caption en específico le damos a Ok y ahora si corrier esta automatización se subiría a nuestro instag Instagram ahora sí te voy a explicar el paso a paso pero antes déjame comentarte que puedes importar esta automatización y solamente tienes que hacer un paso y cambiarle un parámetro si es que la quieres importar y correr por tu cuenta si es que nos vamos a las automatizaciones dentro de imperio digital vas a encontrar esta parte que aparece acá de crea imágenes con flux Lora si es que bajamos a la parte de más abajo aquí Te dejé una guía super detallada de cómo son los pasos que tienes que hacer que las vas a ver exactamente aquí en este video pero puedes descarg directamente la automatización si le das a descargar puedes irte a crear un nuevo escenario en make aprietas los tres puntitos le das a importar eliges el archivo le das a guardar y se te va a abrir exactamente lo que hicimos y lo único que tendrías que hacer en este caso sería irte al webhook crear un nuevo webhook vamos a ver todo esto pero creas el nuevo webhook le das Ok y le reemplazas este código de acá con tu apy de replicate que la puedes encontrar aquí en apy tokens y en crear token literalmente copias el token lo reemplazas acá y le das a Okay haces Exactamente lo mismo aquí reemplazas el token y le das a Okay ahora si guardamos y le mandamos alguna señal o algo en específico para que empiece a correr la automatización va a estar 100% funcional Así que sí Ese es el atajo si es que no quieres armar toda la automatización paso a paso pero también Creo que es super importante que vayamos entendiendo qué es lo que estamos Armando en el caso de que queramos ir haciéndoles modificaciones Así que lo que voy a hacer es voy a crear todo esto desde cero y te voy a mostrar Cómo podemos crear todo esto lo primero que vamos a hacer es Vamos a entrar a make.com y vamos a crear un nuevo escenario una vez que estemos acá vamos a apretar esta opción que sale webhook un webhook es un disparador instantáneo vamos a elegir custom webhook es decir cuando nosotros recibimos algún tipo de información en el webhook se va a desencadenar la automatización Por ejemplo si es que yo decidiera crear una interfaz donde mando información a un webhook va a mandar la Data como Data estructurada por ejemplo benen corde en la torre ifel cada vez que le voy a generar va a mandar la información al webhook pero Benja Cómo creamos esta interfaz de acá te voy a mostrar muy rápidamente Cómo lo podemos hacer Nos iremos a bol.com y acá dentro de imperio digital Recuerda que puedes entrar completamente gratis y te vas a encontrar todos estos prompts te dejé un prompt en específico que puedes copiar y pegar acá para crear nuestra propia aplicación con Inteligencia artificial esto es Crea una interfaz moderna minimalista bla bla bla permite al usuario escribir qué imagen quiene generar y si es que bajamos bajamos bajamos bajamos bajamos al final sale quiero que mandes el input del usuario como Data estructurada al siguiente webhook y este es el webhook que le vamos a poner si es que nosotros le damos aquí a agregar y le pongo como nombre flux Lora Ben corde B3 puedes ponerle Cualquier nombre pero esto me gusta siempre referenciarlo copiamos esto y le damos a Okay podemos irnos acá y decir que queremos que nos mande la Data estructurada directamente a el escenario de make Okay entonces si es que le doy a correr esta aplicación lo que va a empezar a hacer es nos va a empezar a armar toda una interfaz que después podemos Dejar Pública incluso para que el usuario o para que tú directamente puedas empezar a enviarle la información Ahora hay otros métodos más simples si quisiera podría armar la automatización que cada 15 minutos me genere una nueva imagen o que me genere 20 imágenes de una cada vez que le doy correr y que estas imágenes sean generados con charg PT o podemos crear un Google sheets con 20 estilos de imágenes distintas que queremos crear y que vaya generando una a una Pero en fin esa es una parte de los triggers y si quieres entender bien Cómo funcionan los triggers recomiendo que entres aquí al classroom te vayas a make desde cero y veas el capítulo de Los disparadores o los triggers que es un módulo guiado por uno de nuestros expertos en automatización Fran y aquí está la porque literalmente lo que antes nos hubiese demorado mucho tiempo en programar por nuestra cuenta hoy día lo podemos programar completamente gratis con herramientas de Inteligencia artificial como bt y aquí podemos ver que nos acaba de crear la interfaz así de simple verdad siendo x o un prom libre vamos a poner quiero que Ben corde esté bueno elijamos esa opción enseñando automatizaciones en una pizarra y ahora si es que le damos a correr al escenario de make deberíamos generar la imagen enseñando automatizaciones en una pizarra y deberíamos recibir el prom bencor enseñando automatizaciones en una pizarra o sea está funcionando después lo que tenemos que hacer es tenemos que mandarle algún tipo de señal o darle un contexto a flux Verdad que es el modelo de Inteligencia artificial que vamos a usar de Oye necesito que me crees a Ben corde enseñando sobre automatizaciones en una pizarra Porque si es que entramos a replic.com y buscamos flux de flora que es el modelo que vamos a usar y nos vamos acá podemos ver que hay una serie de parámetros que nosotros en teoría deberíamos usar ya por ejemplo si le pongo vencor demand teaching automation sina whiteboard elijo el ratio verdad uno a uno si Quiero la imagen cuadrado 169 si la quiero horizontal y le pido que me genere tres imágenes asociados a mi Lora y le doy a correr me comenzará a generar imágenes directamente de Benjamín Cordero enseñando automatizaciones en una pizarra como podemos ver aquí estoy primero mostrá unos robots después por alguna razón estoy doble Y nuevamente estoy viendo robots acá ahora la pregunta es Cómo podemos hacer para rellenar todos estos datos de manera automática Y eso es exactamente lo que te voy a mostrar ahora pero antes decirte que si es que no entiendes nada de lo que está pasando y por qué sabe la Inteligencia artificial quién soy No te preocupes porque también tengo un video paso a paso de cómo podemos entrenar la Inteligencia artificial con nuestra cara de hecho si que entras a recursos acá dentro imperio digital hay un video de crea imágenes de ti mismo donde te enseño cómo hacer un Lora o un low rank adaptation que es el momento donde a una Inteligencia artificial le modificamos una pequeña parte para enseñarle quién somos o cuál es el objeto con el que lo queremos entrenar si quisiéramos entrenarlo con la taza le subirías 20 imágenes de la taza y le diríamos esto es una taza Pero esto es una taza en específico le pondríamos alguna especie de keyw doble palabra clave en este caso yo lo que hice fue entrenarlo aquí como pueden ver con 20 imágenes de mí mismo y le puse el nombre de Ben corde Entonces ahora cada vez que le pido algo de Ben corde va a saber exactamente quién soy pero este mismo video también lo puedes encontrar dentro de imperio digital si es que quieres la guía paso a paso y si es que no también lo puedes encontrar publicado en mi canal de YouTube el video se llama crea imágenes tuyas hiperrealistas cona Pero ahora sí volviendo acá Cómo podemos rellenar este prom verdad Cuál es el Lora y demás Bueno aquí es donde vamos a usar char gpt si es que bajamos acá todo esto también te lo dejé publicado en la guía vas a encontrar este promt que aparece aquí este también te lo voy a dejar publicado en la descripción del video pero si es que analizamos este prom que aparece acá le decimos Necesito el output en formato json de lo siguiente de la versión del prompt en específico del hf Lora que sea en este formato bla bla bla bla bla bla Entonces al crear esto lo que estamos haciendo es le estamos mandando directamente toda esta información en específico a el modelo que queremos hacerle el llamado a Así que lo vamos a copiar esto que está acá Así tal cual y vamos a agregar un nuevo módulo de Open Ai Vamos a ponerle create a completion y si es que es primera vez que haces esto quizás vas a tener que conectarle la ap Key que lo puedes hacer acá en agregar y puedes buscar la ap Ke en playground openen vamos a elegir cualquier modelo para este caso voy a elegir el o uno mini que es uno de los más económicos Agregar un nuevo mensaje y en el roll lo voy a elegir como usuario Recuerda que no tienes que hacer todo esto si es que quieres importarlo directamente Pero también es importante que conozcas lo que estamos haciendo Entonces vamos a pegar aquí el contenido y aquí toma nota porque si lo pegamos con control V se va a ver así de desordenado pero si es que lo pegamos con control shift y b corta vamos a ver que va a estar en formato mucho más ordenado Okay después estas variables no van a aparecer en negro nosotros queremos que nos aparezcan en rosadito Porque no tenemos ninguna conectada Así que la voy a eliminar y la voy a volver a apretar Y nuevamente haré lo mismo acá la elimino y la vuelvo a apretar aquí lo que sí vas a tener que cambiar en el caso de que quieras imágenes tuyas personalizadas vas a tener que cambiar tu hf Lora que es este que está acá en el caso de que no quieras generar imágenes tuyas o no tengas un modelo entrenado simplemente puedes eliminarle la parte que aparece aquí después le vamos a dar a Ok y cuando generemos el resultado vamos a ver que nos va a sacar literalmente esto que está acá porque le pedimos que el output sea esto le vamos a dar okay Y este va a ser el módulo donde vamos a crear el Jason después lo que tenemos que hacer es tenemos que mandarle una señal al modelo de flux en replicate para que sepa que tiene que generar la imagen para eso vamos a usar un módulo de make a request de htt le vamos a hacer puntitos y esta parte es importante vamos a usar este módulo dos veces la primera vamos a hacer un post es decir necesitamos mandarles la información ya o sea post y la segunda es vamos a hacer un get es decir necesitamos traer información en términos s simples Por así decirlo vamos a ir acá y vamos a poner post en el URL vamos a pegarle el URL que te dejé aquí que es apir replicate p1 lo vamos a pegar pero si quieres encontrarlo directamente puedes irte aquí arriba y nos vamos donde sale Api una vez que estemos acá vamos a apretar http y copiamos este link que aparece acá lo copiamos y lo pegamos después necesitamos agregar un header y necesitamos ponerle de título authorization esta parte es muy importante y esta es la que vas a tener que reemplazar en el caso de que importes la automatización porque este es el Api que tú vas a tener y el Api es personal o sea cualquier persona que puede entrar o cualquier persona que tenga el acceso de este número de la Api va a poder empezar a generar imágenes con tus créditos y no queremos que pase eso así que vamos a mantenerlo completamente privado para este caso te lo voy a mostrar para que sepas cómo hacerlo pero volveremos a replicate apretaremos nuestro perfil y vamos a apretar Api tokens vamos a crear una nueva Api token que en este caso es la que ya creé anteriormente pero si quisiera volver a crearlo lo voy a crear con make flux versión dos y le voy a dar a crear token vamos a copiar este token que está acá y lo vamos a pegar bajo autoriz pero es importante que antes le escribamos Beer espacio y después pongamos la llave La razón por la que le agregamos Beer es porque Beer es portador en inglés ya o sea este es el portador de la llave es decir la persona que tiene esta llave puede prácticamente hacer lo que quiera en replicate Por así decirlo después vamos a bajar y en Body type le vamos a poner raw vamos a elegir el content type y vamos a poner Jason ya que previamente creamos un Jason que es lo que le estamos mandando en request content necesitamos darle el resultado de el output que nos dio chat gpt Entonces le voy a poner el resultado y en par response Vamos a ponerle que sí para que nos dé las respuestas parcial es decir separadas en Campos individuales le vamos a dar a okay Y este va a ser el módulo que va a ser make a request post es decir va a ser el módulo donde le decimos Oye gérvas en general se demoraban alrededor de 20 segundos 30 segundos en ser generadas pero a veces puede tomar un poquito más como en este caso por ejemplo que tomó 40 segundos porque generamos cuatro imágenes Así que lo que tenemos que hacer es antes de devolver la imagen y decirle Oye esta es la imagen necesitamos ponerle un pequeño timer de un slip un slip lo que va a hacer es va a pausar la automatización por un cierto número de tiempo para este caso le voy a poner 50 segundos y le voy a dar a Okay si bien habrían otras formas de poder verificar que ya se hizo la imagen como hacer una verificación anterior y si es que ya está lista que pase al siguiente paso mejor mantengamoslo un poco más simple y le ponemos un slip de 50 segundos ahora lo que tenemos que hacer es una vez que publicamos la información necesitamos recuperarla ya porque ahora si es que yo ejecuto Esta automatización que está acá y le doy a correr y después me voy a bt y le digo quiero que Ben corde esté en la torre de Pisa creo que se escribía así Y le doy a generar imagen y me voy acá vamos a ver que recibimos que Ben corde esté en la torre de Pisa va a crear el Jason y va a mandar el Jason directamente acá si es que abrimos replicate en este momento y actualizamos la página podemos ver que efectivamente acaba de recibir la señal hace de 6 segundos y está generándose podemos ver que la Fuente es directamente desde la Api antes hicimos dos generaciones directamente con la web y podemos ver que se demoró 23 segundos en crear Ya ahora si es que abrimos la imagen podemos ver que aquí estoy en la torre de Pisa excelente imagen pero en fin podemos ver que ya fue creada entonces podemos verificar que está funcionando después vamos a esperar 40 50 segundos para este caso le puse 50 porque me da igual esperar 10 segundos más y después tenemos que descargar la imagen Es decir recuperarlo Y para eso lo que vamos a hacer es vamos a crear un módulo Exactamente igual al que hicimos anteriormente pero en vez de que sea post va a ser get Así que en vez de crearlo de nuevo simplemente lo voy a clonar y lo voy a tirar aquí al ladito le voy a cambiar el nombre y este va a ser el get y va a ser Oye Ahora dame la imagen verdad Ahora recuperemos la imagen le voy a hacer clic acá y le voy a cambiar el método de post a get la URL la vamos a eliminar y vamos a ponerle la URL que aparece acá anteriormente vamos a irnos a URL y le vamos a poner la URL del get Okay Esto es para poder vincular que necesitamos sacar la información de El previo que mandamos verdad De este otro módulo que está a la izquierda después vamos a dejar el Beer lo vamos a dejar Exactamente igual y en el request content lo vamos a eliminar después le vamos a dar a okay y Listo ya después deberíamos ser capaces de recuperar la imagen que acabamos de crear Pero qué quiero hacer después quiero agregarlo a un Google sheets por ejemplo aquí las opciones ya son infinitas si quisiera agregarlo en Google sheets lo vincularía a un Google sheet le pondría agregar una nueva fila elegiría el sheet y después diría que lo quiero poner acá por ejemplo en el sheet name lo vamos a poner acá en la hoja uno en el prom vamos a poner el promt y después en la imagen tendría tenamos que poner el resultado por qué no nos aparece la imagen en este momento porque no hemos corrido ninguna vez la automatización si quisiéramos que nos aparezca la imagen tenemos que ejecutar la automatización una vez más así que le voy a dar a guardar voy a correr la automatización y va a ser benen corde jugando ajedrez por ejemplo le voy a dar a generar imagen y podemos ver que se está desencadenando toda la automatización nuevamente está creándolo Jason Verdad que es este que está acá si lo podemos ver acá abrimos el contenido nos creó directamente el código que es lo que mandamos que queremos una imagen en formato 169 etcétera Nos mandó a crear la imagen eso significa que si es que actualizo acá el replicate está efectivamente en estado de corriendo que fue creado hace 17 segundos y que ya se creó la imagen por lo que ahora es simplemente está esperando porque le dijimos Oye espera 50 segundos para asegurarnos de que la imagen ya esté lista y esté creada después esperó los 50 segundos como podemos ver acá y si es que abrimos el link acá abrimos el output vemos la Data volvemos a abrir el output podemos ver que tenemos un link y si es que abro el link en una nueva pestaña podemos ver que ahí estoy jugando ajedrez Okay Entonces ahora lo que podemos hacer es directamente vincular la imagen acá a que se actualice bajo el output bajo la imagen generada verdad Data output y la imagen generada le voy a dar okay Y aquí las opciones ya son infinitas O sea si quisiera podría mandármelo por mail podría crear un mensaje acá ponerle Aquí tienes tu imagen mandarle la imagen acá image source es igual al output que nos aparece acá Cerramos el paréntesis y mandármelo directamente a mi correo por ejemplo le damos a Okay y le damos a guardar ahora Si volvemos a correr la automatización venc de escalando una roca generar la imagen va a empezar a crearse todo nuevamente entonces Acaba de terminar de generar verdad Entonces nos acaba de mandar esto directamente al correo y si es que abrimos el correo podemos ver que Benja Aquí tienes tu imagen que voy a estar directamente escalando acá una roca ya entonces es s super interesante podemos hacer lo que queramos desde acá si quisiera podríamos publicarlo en instagram en Facebook o en alguna red social también si quisiera podría irme acá y podría decirle necesito agregar un espacio donde el usuario ponga un email que vamos a mandarlo directamente a la misma Data al mismo webhook bolt me empieza a hacer su interfaz y empieza a hacer el código me actualiza la interfaz y ahora sí le digo quiero a benc Core dando una charla Ted y le pongo directamente mi correo vamos a ver que voy a recibir ahora dos variables una que es prompt y otro que es el email verdad porque ahora se separa y si quisiera podría reemplazar acá el email por la variable del input que acabamos de crear que era el email okay Y ahora tenemos prácticamente una aplicación funcionando que si le doy a correr y vuelvo a pedírselo en específico vamos a pedirle nuevamente la misma ven corde dando una charla Ted Y que me la mande a este correo y le doy a generar imagen y si le damos a enviar vamos a ver que aquí está creando el Jason que nos va a crear un prom mucho más elaborado verdad si es que nos vamos al resultado vamos a ver benen corde haciendo una charla test dando no sé qué no sé qué estoy vestido con esto bla bla bla bla bla bla Y esto es lo que le está mandando directamente acá y ahora se lo va a mandar no directamente a mi mail sino a al mail que pusimos acá ya que sería este correo electrónico si yo le pongo juan@gmail.com se lo va a mandar a juan@gmail.com entonces podemos ver que ahora me sale que se acaba de mandar aquí y si es que me voy a mi correo vamos a ver Benjamín Cordero aquí tienes tu imagen y me acaba de crear dando una charla Ted Okay s super interesante se ve una imagen que está como con movimiento Pero en fin se entiende el punto nosotros podemos comenzar a adaptar este prompt absolutamente como queramos verdad y le podemos decir que haga ciertas prácticas dentro de imperio digital obviamente tdg Cuáles Creo yo que son las mejores prácticas Al momento de hacer un prom verdad con distintos ejemplos como esta esta esta y en fin También tenemos miembros de imperio digital que han hecho sus propias imágenes como a gusto por ejemplo que creó estas tremendas imágenes siguiendo el paso a paso del tutorial También tenemos a Rodrigo que creó varias imágenes suyas y recuerda que todas estos recursos puedes verlos dentro de imperio digital y puedes aprovecharlos y probarlos completamente gratis por los primeros 7 días Si sientes que no es para ti puedes cancelar Y no se te va a cobrar absolutamente nada y desde aquí las opciones son Realmente infinitas Entonces esto que acabamos de crear lo podemos implementar en cualquier automatización simplemente basta con copiar estas cuatro partes que están acá copiarlas y pegarlas y aquí tenemos los módulos que reemplazarían al módulo que usábamos previamente que era de generate an image ya entonces yo literalmente puedo dejar una automatización Armada donde cada vez que necesite generar una imagen entre y copie esto y lo pegue y se va a aplicar déjame mostrarte en un caso de uso práctico si es que yo me voy a crear un nuevo escenario e importo alguna de las automatizaciones que están en imperio digital por ejemplo abro automatizaciones me voy a esta automatización que crea contenido para distintas redes sociales en base a noticias en tiempo real bajo al máximo y voy acá donde sale Descargar la automatización le doy a descargar y me voy a este nuevo escenario aprieto los tres puntitos e importo la automatización desde acá se me va a cargar directamente la automatización Ahora vas a ver que tenemos un módulo que es el de generar una imagen entonces lo que nosotros podríamos hacer en teoría es desconectar este módulo y reemplazar ese módulo por estos cuatro módulos que aparecen acá voy a apretar control c voy a apretar control v y los voy a correr directamente acá voy a correr esto los voy a poner acá voy a juntar esto y después los voy a conectar y ahora podemos ver que sí tenemos a diferencia de este un automatización más completa que está generando resultados más realistas este ya lo puedo eliminar y después para conectarlo le diría crea un Jason a partir de la siguiente noticia que vendría siendo el título y el resumen de la noticia le voy a dar a Okay y listo aquí me debería generar directamente la noticia vamos a hacer la prueba Vamos a darle unlink unlink por ejemplo si es que me voy a crear un nuevo feed le pongo en temas tecnología le doy a guardar el feed copio el nuevo feed lo reemplazo acá y le doy a Okay selecciono el foto URL acá y ejecuto esta automatización completa lo que va a empezar a pasar ahora es que cada vez que haya una nueva publicación de la categoría de tecnología en específico vamos a subir un post a Instagram verdad porque ya mandamos a hacer la imagen relacionada a la noticia verdad que esto vendría siendo una noticia que salió hace 40 minutos de que Android tiene siete nuevos emojis que es la noticia que está acá que la podemos abrir acá y podemos visualizarla en tiempo real lo que estaría haciendo esta automatización es crearnos directamente la imagen porque ya le mandamos la imagen acá a replicate y que nos generó esta imagen relacionada a la noticia verdad y esto lo podemos ir en el fondo adaptando directamente si es que queremos solo imágenes hiperrealistas o si es que queremos solo imágenes de algún estilo lo podemos adaptar como queramos Pero esto es realmente lo importante que siempre vamos a poder reemplazar directamente estos cuatro módulos por la función de generar una imagen que usábamos previamente y en automatizaciones previas estoy volviéndolo a correr para ver qué imagen nos generaba nuevamente ya que la noticia era relacionado a esto y nos generó esta imagen que está acá que está mucho mucho mejor que la anterior me asegurémonos sean fotorrealistas así que si abrimos acá vemos el output vamos a la Data y vamos nuevamente al output podemos ver que aquí está el link ahora si quisiera subir esta imagen simplemente me bastaría con conectarlo a Instagram y elegir el foto URL que nos acaba de dar Y podemos dejar corri Endo esta automatización por ejemplo para que haga una noticia cada no sé te invento 120 minutos por ejemplo Así que en fin sin más que decir Espero que les sirva recuerden lo importante acá es que identifiquen esto que estos cuatro módulos que están acá una vez que los crean los pueden copiar y los pueden usar en absolutamente cualquier automatización okay Y también recuerda que te dejé aquí una guía paso a paso de todo lo que tienes que hacer de todos los pasos que tienes que seguir en el caso de que quieras volver algún paso en específico Y por último Recuerda que también tenemos el recurso acá para que aprendas a crear imágenes con Inteligencia artificial entrenadas directamente con tu modelo hiperrealistas también lo puedes encontrar directamente en el canal de YouTube y también mencionarte que puedes entrar a Imperio digital a probar por 7 días completamente gratis ya somos casi 500 miembros y todos muy apasionados por las automatizaciones y por la inteligencia oficial Así que si no quieres quedarte atrás y quieres conectar con gente que está con un mismo Norte imperio digital es el lugar para ti Además del acceso a soporte de las reuniones semanales que tenemos y en fin sin más que decir Espero que tengas mucho mucho éxito que te funcione esta automatización porque realmente es un Game changer Y si te interesa el mundo de las automatizaciones recomiendo que veas el resto de los videos aquí al final de este video te voy a dejar Cómo puedes acceder a ver el video de cómo entrenar una ia o un modelo flux Lora o low rank adaptation con imágenes de tu cara mucho éxito y feliz automatización
