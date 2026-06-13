# 👀Encuentra Leads con APIFY y Personaliza Mails

> Ruta: Automatizaciones Make › 👀Encuentra Leads con APIFY y Personaliza Mails

**🎬 Vídeo (42.9 min):** https://www.youtube.com/watch?v=FH_7kHsFfG0

**📎 Recursos:**
- Leads_Automatico_Apify_GoogleMaps

---

### Cómo Crear un Sistema para Encontrar Clientes por ubicación, Personalizar Correos y Ahorrar Tiempo

Imagina tener un sistema que haga el trabajo pesado por ti. Busca a tus clientes ideales, les envía correos personalizados y organiza todo automáticamente en un solo lugar. Con las herramientas correctas como Apify, Make, Google Sheets y OpenAI, puedes automatizar todo este proceso en minutos.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/312f5fab0a5c42f18c2aa782953abc9b493354380bb142a28e4c0612f709e55d-md.png)

Te voy a explicar cómo funciona y cómo configurarlo paso a paso.

---

### Qué hace este sistema

1. Encuentra clientes automáticamente en Google Maps según tus criterios, por ejemplo, "veterinarias en Santiago".
2. Detecta correos válidos para asegurarte de contactar a las personas correctas.
3. Personaliza correos electrónicos usando inteligencia artificial para que parezcan escritos personalizados para cada cliente (hacemos un scraping de la informacion de su pagina).
4. Organiza toda la información en Google Sheets para que tengas un registro claro de todo.
5. Envía correos automáticos a cada uno.

---

### Cómo configurarlo paso a paso

**Paso 1. Busca negocios con Apify**  
  
El primer módulo usa Apify para hacer una búsqueda en Google Maps. Este paso recopila datos básicos como el nombre del negocio, dirección, teléfono y sitio web. Es ideal si buscas negocios como “restaurantes en Providencia” o “tiendas de ropa en [barrio]”. Un actor lo que hace es un agente que ejecuta una accion en especifico.  
  
**Entraremos a **[**apify.com**](http://apify.com)

y bajo "actors" buscaremos el "google maps extractor"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/08ab534b0d264924bcc137a99d2c44fa3909e50b663741419ed9d55927edd746)

Le daremos a "create task" para que se quede guardado en nuestra bibliotecta de actores

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4b57c0fc5b2b40ae890e831e6754e83a69b038317c7e4c1f9b60bc6a5e80dfda)

Luego, usaremos el módulo de "**Run an Actor**, Apify" en Make y le copiaremos el siguiente json

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/29454967dcbe49d18f30634cb9e8d753e21ee267c42a4cb9b066ca5f217ad314)

> {
> 
>     "language": "en",
> 
>     "locationQuery": "New York, USA",
> 
>     "maxCrawledPlacesPerSearch": 50,
> 
>     "searchStringsArray": [
> 
>         "restaurant"
> 
>     ],
> 
>     "skipClosedPlaces": false
> 
> }

También lo puedes encontrar si apretas "json" justo al lado de la opcion de correr al actor de manera manual.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8661cb1c48154858b58575b159eff978f74ac90c01a6450bb09bf555c12829fe)

**Paso 2. Agrega un tiempo de espera en Make o "sleep" (Sleep)**  
Introduce un retardo de 45 segundos para asegurarte de que Apify tenga tiempo suficiente para terminar la búsqueda. Esto asegura que los datos estén listos antes de pasar al siguiente paso.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/72b1afd978614448adf1f049f63848223e1ebae4892b40dca34561de79cd3f9c)

**Paso 3. Extrae la información con Apify (Get Dataset Items)**  
Recoge toda la información en formato JSON. Esto incluye los datos básicos del negocio, que se usarán en los pasos posteriores.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7165f9f32de04252ac8a7191240beb66de807ccfca4e48c8af9dc39b0042cc1f)

Bajo Dataset ID le pondremos "defaultDataSetId" para que nos tome el ID en específico de la accion que le acabamos de pedir al actor que ejecute.

**Paso 4. Encuentra correos con Anymail Finder**  
Este módulo filtra los datos y detecta los correos electrónicos válidos asociados con los negocios. Asegúrate de que sean correos activos y relacionados directamente con las empresas.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ba1f327d24094149a21caeb7eb398ccefa4e1656a4f6424ca0c82889dc982618)

> ProTip: Puedes crearte una cuanta de free trial por 3 días y de 600 créditos anuales, y te darán los 600. Pero el Free Trial te dejará hacer 250 llamados a la API. Por eso, puedes ejecutarla por 3 días, por ejemplo y mandas todos los correos que querías mandar. Luego te creas otra cuenta y pones la respectiva API key nuevamente. La API la encuentras bajo al sección "API" de Anymail Finder

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/eb4f3c1f9d404c4193a4a7247f3c2037415301841f73410a8600ac320064bcba-md.png)

**Paso 5. Busca la información de su página con Perplexity (Create a Chat Completion, Perplexity)**  
Utiliza Perplexity para extraer más información del sitio web del negocio. Esto incluye servicios ofrecidos, ubicación exacta o cualquier detalle que pueda ayudar a personalizar mejor los correos luego con OpenAI. Asegúrate de usar un modelo que sea "online"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8c480f3dda6e4ece9cf1f461e609a6f07f6290a3c1524bae87e2936bad101c31)

> Analiza la información del negocio, considerando su pagina web {{[2.website](http://2.website)}}, su ubicación {{2.state}} y su nombre {{2.title}} y consigue su mail de contacto si existe
> 
> Dame output de lo que hacen, y hazlo tambien enfocado en los procesos, audiencia, que hacen, programas, etc.

**Paso 6. Redacta correos personalizados con OpenAI (Create a chat completion) o "message an assistant" si tienes un asistente personalizado**  
Con la ayuda de GPT, este módulo genera correos electrónicos personalizados basados en la información recopilada. Por ejemplo:  
“Hola [Nombre del Propietario], notamos que [Nombre del Negocio] está creciendo en [Ubicación]. Nos encantaría hablar sobre cómo [Propuesta] puede ayudar a tu negocio a [Beneficio].”

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/eba83b19bd8c4139907fec2964feff8aef8b05df6e934f69b8db59e69d1b6f2a)

Te dejo el prompt que utilicé...   
  
**#Asegurate de cambiarle las variables**

> Tienes una agencia de autoamatizaciones con IA. En base a eso hazle una propuesta comercial (tu output en HTML) que se aplique al siguiente negocio especifico.
> 
> Nombre Empresa: {{2.title}}
> 
> Calle: {{2.street}}, {{2.city}}
> 
> Aqui hay un poco mas de info sobre la empresa: "{{6.choices[].message.content}}"
> 
> Crea un cuerpo de email personalizado en HTML para ofrecer tus servicios con el objetivo de agendar una llamada con el propietario de la empresa. Solo el cuerpo del email sin asunto. (no incluyas los simbolos (```) Puntos importantes:
> 
> Obtén información relevante de la empresa a partir de la siguiente información para personalizar el email
> 
>  
> 
> Pueden agendar una llamada en el siguiente enlace https://calendly.com o contestar el email con disponibilidad para agendar una llamada.
> 
> El cliente encontrará adjunto el catálogo de productos.
> 
> Sé extremadamente persuasivo utilizando los sesgos de la escasez, sesgo de prueba social y sesgo de autoridad.
> 
> Este negocio está en {{2.state}}en la zona de {{2.neighborhood}}. Utilízalo para la prueba social.
> 
> El nombre de mi empresa es Imperio Digital
> 
> Responde solo con el texto del cuerpo del correo electrónico en formato html. 
> 
> No añadas asunto.
> 
> No añadas variables vacías, solo utiliza las variables sobre las que tengas información.
> 
> Tu nombre es Benjamin Cordero, tu empresa es Imperio Digital, y estas en Av. Vitacura 1050
> 
> No incluyas campos a rellenar entre parentesis o corchetes, solo infrmacion relevante. 
> 
> Hazlo lo mas personal y mas humano posible, estas en Chile no seas tan formal, sino más casual.
> 
> # No uses los símbolos (*) ni (**)
> 
> # No uses el símbolo (`) ni incluyas (```html)
> 
> # No uses el símbolo de exclamación anterior (¡)
> 
> ## Hazlo y escríbelo de manera muy casual, un poco más informal y no uses símbolos anteriores de pregunta (¿).
> 
> Este será el mail final que se enviará.
> 
> ##Haz el output en formato HTML, es decir usaras line breaks <br> </br> de ser necesario
> 
> No incluyas "```html" al principio del código, solo dame el código HTML con los <p>
> 
> ##IMPORTANTE: El formato en output HTML y con muchos line breaks para que se vea más decente y ordenado.

**Paso 7. Organiza todo en Google Sheets (add new row, Google Sheets)**  
Toda la información se guarda automáticamente en una hoja de Google Sheets. Esto te permite llevar un control claro de los negocios contactados, los correos enviados y el seguimiento pendiente.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c80467a738114c519fd4828ae6bffe22d06c8d3da29a4bdaa67ab32090d05d1d)

**Paso 8. Envía los correos con Microsoft 365 Email o Gmail o tu correo de preferencia**  
Finalmente, el módulo de Microsoft 365 Email envía los correos directamente a los prospectos. Todo ocurre en automático, lo que elimina la necesidad de enviar correos manualmente.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f8975f87aa4646de9d95c228d224fecadc6575f3f7e4429db47b8b1d0580587e)

---

### Por qué este sistema te puede ayudar

Este flujo no solo automatiza tareas repetitivas, también asegura que cada prospecto reciba un correo personalizado que capture su atención. Es rápido, eficiente y funciona tanto para 10 como para 1000 prospectos al mismo tiempo.

---

### Para quién es este sistema

- Para emprendedores que quieren más clientes, pero no tienen tiempo para buscarlos manualmente.
- Para agencias y freelancers que necesitan optimizar su generación de prospectos.
- Para negocios que buscan escalar y automatizar tareas repetitivas sin contratar más personal.

---

### Cómo empezar

1. Regístrate gratis en Apify en este [enlace](http://apify.com).
2. Crea tu cuenta en Make en este [enlace](http://bencorde.com/make).
3. Descarga el blueprint del sistema aquí abajo y súbelo a Make.
