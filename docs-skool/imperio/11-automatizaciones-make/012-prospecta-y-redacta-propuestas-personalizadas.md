# ✈️Prospecta y Redacta Propuestas Personalizadas

> Ruta: Automatizaciones Make › ✈️Prospecta y Redacta Propuestas Personalizadas

**🎬 Vídeo (45.1 min):** https://www.youtube.com/watch?v=XYQX-A3sh9c&feature=youtu.be

**📎 Recursos:**
- Prospecta y Redacta Propuestas

---

## Imagina poder automatizar todo tu proceso de prospección y cierre de clientes, sin perder horas buscando contactos y redactando propuestas.

Pero veámoslo en un caso práctico... Imaginemos que viajamos por el mundo sin pagar por alojamiento, comidas o experiencias. Gracias a la automatización, ahora puedes **conseguir noches gratis en hoteles, comidas en restaurantes y acceso a tours turísticos**, simplemente ofreciendo tus habilidades a cambio.

Desde **fotografía, gestión de redes sociales, diseño web, creación de contenido** y más, puedes presentar propuestas irresistibles que se adapten a las necesidades de cada negocio, **de forma completamente automatizada!**

**LO MEJOR: **Es personalizable para lo que tu quieras... esto nuevamente... es solo un caso de uso práctico.

---

### **¿Cómo funciona esta automatización?**

Utilizando herramientas, hemos creado un flujo de trabajo que permite **buscar, personalizar y enviar propuestas automáticamente**, ahorrando tiempo y aumentando las probabilidades de éxito.

1. **Definir el objetivo y crear una interfaz con **[**Bolt.new**](http://Bolt.new) - Un formulario sencillo donde defines qué tipo de negocio quieres contactar: hoteles, restaurantes o tours, y qué servicio puedes ofrecer a cambio. Puedes usar un formulario de manera alternativa.
2. **Buscar alojamientos, restaurantes y tours con **[**Apify.com**](http://Apify.com) - Extraemos datos clave de cientos de negocios en el destino elegido, incluyendo nombre, ubicación y categoría, todo de forma automatizada.
3. **Encontrar los correos con AnyMail Finder** - Identificamos los emails de contacto de los negocios seleccionados para asegurarte de que tu propuesta llegue a la persona indicada.
4. **Personalizar la propuesta con Perplexity** - Extraemos información clave de las páginas web de cada negocio para hacer que tu oferta sea relevante y atractiva.
5. **Redacción automatizada con OpenAI** - La IA redacta un correo profesional y persuasivo, adaptado a cada negocio, destacando cómo tu servicio puede beneficiarles.
6. **Envío automático con Outlook o Gmail** - Todos los correos se envían automáticamente sin que tengas que intervenir, maximizando tu alcance con el mínimo esfuerzo.

---

### **¿Por qué esta automatización es una solución perfecta?**

- **Propuestas personalizadas en segundos:** Adaptadas a cada negocio para aumentar tus oportunidades de éxito.
- **Ahorro de tiempo:** Dejas de buscar manualmente y enviar correos uno por uno.
- **Alta escalabilidad:** Puedes contactar decenas o cientos de negocios en minutos.
- **Mayor tasa de respuesta:** Gracias a la personalización y al enfoque estratégico de la propuesta.

---

### **¿Qué puedes ofrecer a cambio de estos servicios gratuitos?**

- Contenido visual de alta calidad (fotografía y video).
- Gestión de redes sociales y estrategias de marketing.
- Optimización de su página web y SEO.
- Publicidad digital para atraer más clientes.
- Creación de reseñas en plataformas de viaje y blogs.
- Básicamente lo que quieras...

---

Lo primero que haremos será crear una interfaz en bolt.new

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/604e1844869b4892ac6aba736bb8106d7f194a4e116b46b6b60f5c2c4bdf3eaa)

Le pondremos este prompt de aquí abajo, adaptado a lo que gustes (puedes pulir tu propio prompt con ChatGPT y pedirle que lo adapte para lo que quieres).

> "I want you to create a web application called **"Viaja Gratis Bencorde"**, which helps users plan their trips for free by exchanging their services for accommodation, food, and activities. The entire interface must be in Spanish, with a simple and futuristic design. Here is the detailed project specification:
> 
> **Objectives:**  
> Create a web application that allows users to input their travel plans and connect with hotels, restaurants, and activity providers in exchange for services. The target audience includes budget travelers and digital nomads looking for affordable ways to explore new destinations.
> 
> **Menu:**
> 
> 1. **Inicio** (Home)
> 2. **Mis viajes** (My Trips)
> 3. **Explorar destinos** (Explore Destinations)
> 4. **Configuración** (Settings)
> 5. **Ayuda** (Help)
> 
> **Front-Office:**
> 
> - The interface must be fully in Spanish with a clean and futuristic design.
> - A responsive and intuitive layout for desktop and mobile devices.
> - A dynamic form that adapts based on user selections: - Users select the number of destinations they plan to visit.
> - Based on the selected number, fields appear to input details for each destination (e.g., "Ciudad 1, Fecha 1, Pais 1"; "Ciudad 2, Fecha 2, Pais 2").
> - Options to specify the number of hotels, restaurants, and activities to contact per destination.
> - Inline validation to guide users while filling out the form.
> - A progress indicator to show the completion status of the form.
> - A confirmation page that summarizes all user inputs before submission.
> 
> **Note:**  
> Ensure that all form elements and buttons are fully functional and interactive before finalizing the implementation."

Luego de tener la interfaz creada, vamos a crear nuestro escenario en Make, y crearemos un nuevo "Custom Webhook"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/393f5c4c8b2b46cc92cdd7ced90be26f3f3ae30abc324e85974a655d8519c904)

Copiaremos el nuevo webhook generado

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4a984bcd446a4e1e943c540998728036b57c8a9dd66b48ceb7f7587c250c2701)

Y volveremos a [bolt.new](http://bolt.new) y le mandaremos el siguiente prompt (donde reemplazaremos el link del webhook)

> ##IMPORTANT: We will send all the data as structured data to the following webhook: [https://hook.us1.make.com/6u1wq42mtvjcflbjzfw3aqawkeqjv1cc](https://hook.us1.make.com/6u1wq42mtvjcflbjzfw3aqawkeqjv1cc)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9b5689f7230e4ecba33c2bdc57edf03e7d798b33359c48ac81ee20c2ec334a16-md.png)

Le daremos a "Run once" en Make para poder recibir las variables

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8626f2d02fa24f1fac680671b96e236655c6483d2d6c4dd482cbeff21bdce7ff)

rellenaremos el formulario de bolt y le mandaremos la informacion para que la pueda recibir

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0506ed729a44412496ba72f696ec30fefe1d1d93b3c24f299d922aaea3996bc1)

Y deberíamos recibir algo así

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/184898c67daf41f5b4bbc0d20b1becd5b380d7b61250446d86a0c247923f72a1)

Luego como recibimos los datos en un solo bundle, tenemos que emplear el uso del "iterator" para separarlo en más bundles, ya que recibiremos data de hoteles, restaurantes y tours.

Buscaremos "Iterator" y seleccionaremos "destinos" o la variable madre que recibimos en el webhook

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7f22ab971e064262bb728a4b886f736a73f780154af84478a40540234e571c78)

Luego tenemos que crear 3 flujos, uno para hoteles, otro para restaurantes y otro para tours. Sin embargo los 3 cumplen la misma funcion, asi que haremos uno y los copiaremos y pegaremos, luego reemplazarmeos las variables. Comenzaremos por los hoteles. Buscaremos un "Router" y lo agregaremos

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/09fe979e996d4d4b8bc05c74a1f6d1f00dfd1d0f4a234757a2c6d45acd4d1950)

Buscaremos el modulo de APIFY de "Run an actor"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2febef50fa9840b4bc23b6f3a6761200271cb13e22a24f15a70d9e9ef5e172e9)

Buscaremos en Apify el "[Google Maps Extractor](https://console.apify.com/actors/2Mdma1N6Fd0y3QEjR/input)" y le daremos a "Create Task

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/54d4f8cd6d72420aa95e5f5666707b29c009f3942e174dc7be71fe22f8577da9)

Luego de hacer nuestra conexión con Apify, vamos a buscar el "Actor" que acabamos de crear... 

> Nota: Si necesitas más contexto de como funcionan los actores, puedes [ver esta guía ](https://www.skool.com/imperio-digital/classroom/a65de4cd?md=80d7cfd967084a2683741533d53f0ec4)que lo explico paso a paso

Volveremos a Apify y seleccionaremos la opción que sale "JSON"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d79d3b804b7f4c768211d15136afe678f410a8a4fa6d40e093d40f0ff9d7b725)

Copiaremos ese código y lo pegaremos en Apify. (tip, pégalo con CTRL + Shift + V para que se copie y pegue con el formato correcto)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/549549de151848b5b1023e0101a9f2e088ef38dfc250472995b5ef1a6a3ca33f)

Luego reemplazaremos las variables de "ciudad" , "pais" y "numhoteles" por las variables que acabamos de mandar en el formulario. (Usaremos solo numHoteles y luego para las otras lo cambiaremos a restaurantes, etc, o lo que busquemos)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1e5c410c06514c7b9c97911350c32ced200adfcdc5ca45e09227f25ef628ed5e)

También cambiarás el tipo de negocio al que estas buscando, por ejemplo hotel, hostal, habitacion, etc. Para este caso lo dejaré en "Hotel"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/31a6483ac8804f399e83f4f1dba79dafd7be734cb9b6448a886b66ec675d2b08)

Luego tenemos que hacer una "pausa" de 45 segundos para que se termine de ejectuar el actor. Para ello usaremos el modulo "sleep" 

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8af0be994fd54f9590c41750daf3d49655955b3caaa34a7da774d640e92ac96a)

Luego buscaremos en Apify el "Get Dataset Items", para recuperar la informacion que acabamos de mandar a buscar al actor

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a84a4a3944b84f19b6bb47c1bd50ed0562df82ccb3c7427abf0e94aef4dfef80)

Bajo el "Dataset ID", pondremos el "DefaultDatasetId" 

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1ec8112370544df2ab8bac41aa32253058576f0636c64038a2e816ec4842a098)

Y en el límite le pondremos el número de hoteles que queremos recuperar

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3d421356b9ec4d9f8ff272bddad087bf305f8248575047a8ac4f53504cb0b867)

Luego tenemos que extraer el mail al que le enviaremos la propuesta personalizada, para ello usaremos una app que se llama [Anymail Finder](https://newapp.anymailfinder.com/).  
  
Nota: Puedes crearte una prueba gratuita y usarlo por 3 días, y crearte múltiples cuentas. 

Iremos a la API y habilitaremos la API. Luego la copiaremos y pegaremos en Make

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/62aee78477044c1d93c9d8ae6620cead5d9fa27178a64be680e0b639aee588f9)

Usaremos el modulo "Search for a Company's Email"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/520e8a09df804c42b28870d31acaa4d47396d511e8274885b9c1e32e58ca1eb3)

Y bajo "domain" necesitamos poner el dominio que acabamos de extraer, pero aun no lo tenemos. Es por eso que correremos la automatizacion y ejecutaremos el formulario, para poder tener la variable con la que vamos a trabajar.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ad7b689bf22340a8a7b853268d9f5d12c7f70b22aea04441ab8bad498ae50c16)

Correr automatizacion

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e1e1c6a56505468484b5e8e12f614c68ca1b9f91fefa4a6b80e7f4fc11814c1c-md.png)

Esto nos permitira poder trabajar con la variable "website"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/014208c9548d47d3b514a317826f0eea046e184f96684d65ad1886b02f90d568)

Abriremos anymail finder y seleccionaremos la variable "website"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/bade3149146d4dcba1954bc98e8c17bf6c12ae6b8cb84a2097328979645f285e)

(*opcional*) Luego para personalizar aun mas la propuesta, usaremos Perplexity AI para sacar más informacion de su sitio web. Agregaremos el módulo de Perplexity y "Create a Completion"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/22eba5b271ff4502bf3b52893acc33211014e23e2db4457989baf844e45f5545)

Nos aseguraremos de usar algun modelo "online"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/91d8ad3914c345e1b3ea8be2516d4743c9c37831e0b7418fac92ab511b195b43)

A continuacion te dejaré el prompt que utilicé:

> Analiza la información del negocio, considerando su pagina web {{[8.website](http://8.website)}}, su ubicación {{8.address}} y su nombre {{8.title}} y consigue su mail de contacto si existeDame output de lo que hacen incluyendo sus actividades principales

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/bda6a5c1420349479fa2f8e88436f33f63bcc75e6a7e41a2a958c5502ab605db)

Luego le personalizaremos el correo con el modulo OpenAI (o LLM a tu elección). Usare el modulo de "Create a chat completion", pero si tienes un asistente entrenado puedes usar el "Message an assistant"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/53e263f85a3540b9a8cd0c00c9cb12fd003df43796744e20b5f701370336ac12)

A continuación te dejo el prompt que utilicé, es importante porque tenemos que tener si o si el resultado en HTML para que cumpla un mejor formato y más legible. Reemplaza las variables que debas reemplazar

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6e254f8c2f8f4d9ba4ae39b23aa6d4fbb443273348624a93afe9f9fb4a20916d)

Este es el prompt que utilicé: 

> Eres un freelancer experto en edicion de video, le redactars un mail a la siguiente empresa ofreciendo tus servicios a cambio de alojamiento, que incluye piezas listas para publicitar en plataformas como meta ads o facebook y videos estéticos subidos en colaboracion. Te dejo mas detalles de mis servicios: redactaras piezas de contenido publicitarias y editaras videos para que puedan usar para promocionar su lugar y haras estilo vlog natural y profesional.
> 
> Tu fecha aproximada de llegada seria {{3.fechaLlegada}} y salida {{3.fechaSalida}}
> 
> ##tu output en HTML que se aplique al siguiente negocio especifico y hazlo super personal y natural, escrito muy natural y muy empatico y personalizado con los datos que tienes de su negocio.
> 
> Nombre Empresa: {{8.title}}
> 
> Calle: {{8.address}}
> 
> Aqui hay un poco mas de info sobre la empresa: {{11.choices[].message.content}}
> 
> Crea un cuerpo de email personalizado en HTML para ofrecer tus servicios con el objetivo de agendar una llamada con el propietario de la empresa. Solo el cuerpo del email sin asunto. (no incluyas los simbolos (```) Puntos importantes:
> 
> Obtén información relevante de la empresa a partir de la siguiente información para personalizar el email
> 
>  
> 
> El encontrarán adjuntos a este mail mi portafolio. Me llamo Benjamin Cordero, conocido en Instagram como @bencorde ( [instagram.com/bencorde](http://instagram.com/bencorde) )
> 
> Sé extremadamente persuasivo utilizando los sesgos de la escasez, sesgo de prueba social y sesgo de autoridad. pero con leve flexibilidad, di que estas por la zona en ese tiempo.
> 
> Responde solo con el texto del cuerpo del correo electrónico en formato html. 
> 
> No añadas asunto.
> 
> No añadas variables vacías, solo utiliza las variables sobre las que tengas información.
> 
> Tu nombre es Benjamin Cordero
> 
> te pueden contactar a este mail o al whatsapp +569 90002748
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
> ##Haz el output en formato HTML, es decir usaras <p> </p> de ser necesario
> 
> No incluyas "```html" al principio del código, solo dame el código HTML con los <p>
> 
> ##IMPORTANTE: El formato en output HTML y con <p> </p> para que se vea más decente y ordenado.

Enviaremos el correo electrónico. Para este caso utilizaré "Outlook", pero puedes usar Gmail o el correo de tu conveniencia

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2cf1c5ecb6eb4bf89e3847f201c50b333ae7e934de50403497c9524d29c9c1e1)

En "Subject" o "asunto" le podnremos el asunto, por ejemplo "Propuesta para [empresa]", en "Body Content" Le pondremos el resultado de ChatGPT "Result", y en Recipients, le pondremos "email". Le daremos a guardar.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4e703419dc8647e1b23568acc30df4ae1713e264b9f343329cd4fd0a039f2632)

*OPCIONAL: Agregar los mails a un sheets para llevar contabilidad de los emails enviados. Add New Rows*

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5665db577d004b91bf72b00a59e3d2896c35680ae15f4b0193c6799f36819e47)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4773e0bd3d284ccc9562c645bee02e64d5896d7eb6d546bea0eb686815ae63a3)

*Y luego los agregarás a un sheets cada variable en un mismo "row" o fila.*

La automatización se verá algo así

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1f124d5aaea443d69d2d97c1e714b136d6498a932bc94ec28ec549935a9fa54e-md.png)

Pero ahora nos faltan dos pasos clave antes de duplicarla. Primero, necesitamos solo filtrar para que cuando conseguimos una pagina web, pasar a extraer los datos en perplexity (asi la automatizacion no nos tira errores) y segundo solo redactar un mail si es que encontramos un mail (asi no nos itra errores) y porque en el fondo no queremos redactar un mail si no logramos encontrar a quien mandárselo. Para esto usaremos los "filtros",

Entre "Get Dataset (APIFY)" y "Anymail Finder"  haremos click derecho y pondremos un filtro

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/25580698cfe04ce3881b8ff154016ae78cdf28c0982e4d6880cc880959baa83b)

El filtro será... "Si existe página web, avanza. Si no, no avances". 

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/498dd79134a646eb9a185286fe17fa93d1c88121ff584d3883bc2799d642490f)

Haremos lo mismo con el mail, entre Anymail Finder y Perplexity

"Si el correo existe, avanza. Si no, no avances".

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8f591e756fe1444f9365b951d36dbd56b7b90e8da7e041ea8ea93b15de6ffdeb)

Ahora nos mandaremos un correo de prueba, le daremos a correr autoamtizacion y reemplazaré el correo electrónico al que lo mandamos por el mio, a modo de prueba

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7be1edddeabe4b2694ac6e0e5891cfe3da411f23e45b4e78b9476c963e73d605)

Le daré a guardar y "Run once" y volveré a enviar el formulario.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/688998ed92c4454d84bb31e9dcdaaef140197a748f1c41248d50e7b475540541)

Al correrlo debería aparecer algo así, y recibir el correo electrónico así.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/043590b75911408399d348059a91ae0bffddb984aed84ccda38a2248552a223b)

Ahora... Necesitamos hacer lo mismo para los restaurantes y turismo.

Así que seleccionaremos toda la automatizacion desde el "Router" a la derecha (sosteniendo SHIFT + Seleccion)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/37694770e5e44a28a170589ed4c8c3e78ba4f6d50cc1464b9f90497a92123c37)

Copiaremos y pegaremos 3 veces

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1626dc195d214e838715708df4952ab8a97a9c4153a24d698c4405175ca6e6e3)

Luego tendremos que poner los filtros... Para que se vaya a hoteles tenemos que hacerlo SOLO si es hoteles lo que piden. Asi que iremos a filtros

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f3911cd982a044a986b8d08dca98ebc9f322c56055bc47b4850846108d22f1c4)

Y se cumplira solamente si el numHoteles existe, es decir si hay numero en hoteles.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/084b20492e394c71aa79d5ebd424e4068633c58318124e27bdab9f0c454626b1-md.png)

Haremos lo mismo para la segunda, que es solo restaurantes

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0377a2c76bac46c0979938371fad7ecc06b9fb2cde0a457cb2cc78f9bfbd7d06)

Solo si existe restaurantes

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5859ff8c82924e8bac8b0808467036664c61c1b94ee64280b286dc6f8d415b38-md.png)

Y lo mismo para Tours

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a91e747247e84ac1b5c39a302396beba3e0247f220fa4e5ea1ef346e691053c6)

Luego tenemos que reemplazar el llamado al actor en cada uno... primero haremos el del restaurant. Aqui haremos dos cambios importantes, el primero es cambiarle el "numHoteles" a "numRestaurantes" , y segundo, cambiaremos el "hoteles" a "restaurant"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d83620e92b7c4d01ae85afb6f9a192a5ee1ba705c263475abc9f77e9e7368b30)

Luego haremos lo mismo en "tour"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8f3e7a4ec03b4116a5f024ec99d8da1172b4aff3ab2946f58e071850d5305353)

Finalmente modificaremos el prompt de Redactar Correo Personalizado para que se adapte a cada uno. Primero el de restaurantes, que le cambié el "system prompt" para que se adapte a intercambiarle los servicios a un restorán.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/117211a5bc9747ac88f5d03b738e9710cc21f904a2bb4fbea5032f6cf6d079e5)

Esto fue lo que le cambié

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0ed9dad2df934aa1873da740e75d4d0e58eb3ec3dfcf4bd29f8ca6791372bb59)

Y después lo mismo en "tours" o "actividades"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/80190ab0dbe84862a1cf7ceb658e527d93048c975beb456aa3790b203e6b8994)

Dale a "Guardar" Y corre la automatización enviandop nuevamente el formulario, agregando la cantidad de ciudades y lugares que quieras.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7087ed5c7f0e469c9f7dc15d66299aa5c021839171494f2289bcfdf6cb7c0bcd-md.png)

Ahí comenzarás a enviar y recibir las distintas propuestas

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d0827781bf9040a2b9caa7582e9e5cd0b669141b74af4e8ca23bdbefb68d6c4b-md.png)

Recuerda que peudes importar todo este blueprint descargándolo abajo, apretando los 3 puntitos en make y eligiendo "import blueprint".

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/54d23569004f4bcd9f79a79283aa5c3593a20c70fa4b4367ba6ad1acf5776b3e)
