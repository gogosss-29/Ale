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

## 🎙️ Transcripción

imagínate tener un sistema que haga todo el levantamiento pesado por ti es decir que busque clientes potenciales redacte propuestas personalizadas y realmente puedas dedicarle el tiempo a conversar sobre una propuesta que ya le mandaste y no gastes realmente el tiempo en prar el video que te voy a mostrar ahora es probablemente uno de los videos más importantes que vas a ver en mucho tiempo si es que sabes aplicarlo correctamente y para el final de este video vas a poder tener este sistema funcionando al 100% si sigue paso a paso te voy a mostrar rápidamente Cómo funciona este sistema Okay lo primero que vemos es nos encontramos con una plataforma como esta y el sistema yo lo adapté tú lo puedes adaptar como quieras pero lo adapté para eh crear un itinerario e ir buscando hoteles es decir alojamiento restauranes y actividades a cambio de ofrecer tu servicio ya o sea está pensado digamos para un freelancer que quiere viajar y recorrer el mundo ofreciendo sus servicios de fotografía edición de videos eh páginas web absolutamente lo que sea okay Entonces yo entro acá directamente le pongo los destinos la ciudad y el país y cuántas noches me quiero quedar por ejemplo me quiero quedar del 29 al 31 y me quiero quedar en España específicamente en Madrid Y quiero mandarle un mail personalizado a 10 hoteles a 10 restaurantes y 10 tours en específico Okay después le voy a poner otro destino que ya no quiero quedarme en España y supongamos que me quiero ir a no sé Argentina ya entonces voy a poner Argentina y la ciudad me quiero ir a bueno Buenos Aires y me quiero quedar el del 2 al 7 de febrero por ejemplo voy a redactar un mail personalizado a 10 hoteles a 10 restaurantes y 10 tours en específico le voy a decir que le puedo ofrecer servicios de fotografía y edición de reels estilo blog para publicidades en meta y le voy a decir que mi portafolio de Instagram es @ben corde ya Este es un ejemplo práctico Pero tú lo puedes personalizar absolutamente para lo que quieras y una vez que enviemos el formulario directamente se va a ejecutar Esta automatización que está detrás que ya te voy a explicar cómo funciona pero si le damos a correr vamos a poder ir viendo el paso a paso Entonces ahora le voy a dar a enviar solicitud y podemos ver que se está comenzando a ejecutar directamente la automatización y aquí Se confirmó que se mandaron los datos y comenzará a buscar en específico en España en Madrid 10 hoteles 10 restaurantes 10 actividades y le va a redactar una propuesta personalizada para cada uno de ellos porque este sistema no solamente te consigue los datos el contacto y el mail de esos lugares sino que también descarga la información de su página web y lo personaliza y le redacta una propuesta personalizada de Porque tú eres la mejor opción para ofrecer este servicio entonces lo que está haciendo el sistema en este momento es descargase conseguir directamente los hoteles que es lo primero que va a conseguir si es que abrimos acá vamos a poder ver que consiguió directamente el Hostal Madrid después el Newton Hostal después el Hostal Tati el safe State Madrid y así nos consiguió los 10 directamente lo que está haciendo ahora el sistema es descargando y consiguiendo los mails para poder redactar les directamente la propuesta a cada uno de ellos podemos ver que aquí nos consiguió por ejemplo uno de los mails y ahora lo que está haciendo el sistema es descargándose la información que está pública en su página web y podamos redactar una propuesta más personalizada por ejemplo Aquí vemos que le dijimos analízame la información del negocio considera su página web y si es que vemos el resultado acá nos va a decir eh se encuentra en el barrio centro de Madrid verdad tiene las noches de DJ noches de cine tiene un rooftop Esto es lo que hacen etcétera después Aquí directamente le está redactando el correo electrónico que vendría siendo Hola Me llamo de jamin cordeo conocido en instagram como voy a estar en Madrid del 29 al 31 de enero y ofrezco mis servicios de fotografía y edición de reels estilo blog además puedo crear videos estéticos en mi portafolio junto van a poder encontrar no sé qué me encantaría agendar una llamada contáctenme al número eh espero tener la oportunidad de colaborar con ustedes aquí podemos ver que efectivamente Se está enviando el correo electrónico y desp pues está tabulando todo en un Google sheets ya para poder tener registro de lo que estamos haciendo y de las cosas que hemos enviado y de las cosas que no y ahora si es que empieza a abrir mi mail vamos a ver que estoy empezando a recibir los correos electrónicos Hola voy a estar el perfecto Oye voy a estar el para Madrid central eh propuesta para el hotel Triana propuesta para el hostel Madrid y así lo va a hacer con los 10 hoteles que conseguimos y después lo va a hacer con los 10 restaurantes y después lo va a hacer con las 10 actividades y de esta manera podemos viajar prácticamente gratis verdad A cambio de nuestros servicios por el mundo Entonces en esta misma plataforma que te voy a mostrar también cómo la podemos crear con un simple prompt vamos a poder ver cómo nos podemos armar un itinerario completo Ya esto es una idea de uso práctico para que se imaginen cómo lo podemos hacer pero en realidad esto lo puedes aplicar para lo que sea sea que tienen una agencia de marketing y quieren conseguir clientes sea que tienen una agencia de automatizaciones sea que quieres ofrecer tus servicios de páginas web sea que absolutamente lo que sea que vendas tú lo puedes personalizar acá directamente ya así que aquí podemos ver que ya terminó de enviar directamente todos los hoteles recibimos los correos y esto es interesante porque buscamos 10 correos electrónicos le pedimos 10 pero solamente logró encontrar cinco ya entonces por eso también a veces ponemos un número un poco más alto porque necesita cumplir las condiciones de que tengan página web y que tengan un un mail disponible para que nosotros le podamos redactar el mail como podemos ver acá para redactar el mail es un simple pront como podemos ver aquí abrimos y le dije Eres un freelancer experto en edición de videos eh tu fecha aproximada sería la fecha que pusimos acá justo aquí Eh Necesito que le escribas a la empresa te dejo un poco más de contexto sobre la empresa y ahí está toda la información que logramos sacar y le redactamos este mail a cambio de alojamiento para los restorantes va a ser exactamente lo mismo Pero va a ser a cambio de tres comidas o de cuatro comidas o absolutamente lo que tú quieras que le vamos a grabar los videos estéticos verdad o le hablamos de cualquier servicio en fin ahí podemos ver que ya estamos comenzando a recibir directamente los correos electrónicos entonces aquí está mi propuesta sencilla cambio de cuatro comidas completas en taramara les ofrezco mi expertise para crear contenido visual bla bla bla bla bla bla y finalmente se está ejecutando ahora lo mismo pero para las actividades para los tours ya esta automatización nuevamente está pensada para un freelancer o un creador de contenido que quiere viajar por el mundo eh sin la necesidad de pagar alojamiento y pagar las actividades ya pero pueden aplicarlo absolutamente a lo que sea solo que me gusta hacerlo con un caso de uso práctico de hecho sería interesante si es que pruebo esta misma automatización y veo si es que es posible realmente hacerlo pero yo me imagino que sí porque eh todos los hoteles o todos los lugares siempre están buscando eh potenciar un poquito su marketing y empiezan a crear más tipo de contenido orgánico y este tipo de propuestas son propuestas que yo también recibo directamente okay Así que como podemos ver acá ya se terminó de ejecutar toda la parte de los restaurantes Y en este momento están las actividades y si abrimos el mail comenzaríamos a recibir nuevamente las propuestas que vamos a estar mandando y una vez que terminó por completo con todo lo de Madrid ahora como le pusimos dos ubicaciones va a comenzar con lo de Buenos Aires entonces amente va a empezar a buscar 10 hoteles en Buenos Aires 10 restauranes 10 actividades y va a empezar a mandarle un mensaje personalizado a cada una de ellas según la información que tienen disponible en su página web Ya esto es realmente Una mina de oro y si te quedas hasta el final de este video vas a aprender a construir este sistema completamente por tu cuenta sea porque quieres ofrecer tus servicios o tener tus servicios y publicitar losos o quieres venderle esta automatización a alguien más porque sabemos que gr parte y gran dificultad de las cosas en general o de la mayoría de los negocios es conseguir leads Así que si tú le puedes decir a alguien que le consigues clientes potenciales en frío y aplicas esta automatización que te voy a dar y te voy a dar la opción que directamente te la descargues la importes y la comiences a usar sin duda es algo que se le puede sacar mucho mucho dinero ya pensemos también en los clientes potenciales que son altísimos o de altísimo valor como todo lo que son los inmobiliarios como todos los que venden tiet más alto también es un área de potencial de uso s super interesante Okay si es que seguimos viendo los correos seguimos recibiendo los correos electrónicos Pero esta vez de Buenos Aires Ahora sí voy a pausar esta automatización para que no siga corriendo porque te voy a enseñar Cómo podemos empezar a armarla le voy a dar a stop y ahora vamos a lo que nos convoca vamos a armar esta automatización paso a paso pero antes si no me conoces Mi nombre es Benjamín Cordero y soy cofundador de la comunidad de school imperio digital una comunidad donde nos dedicamos a ahorrar tiempo mediante soluciones y automatizaciones que funcionan en este momento ya somos más de 700 miembros que están metidos dentro de la comunidad y todos exactamente con el mismo fin Si es que entras acá en p digital vas a poder ver todas las plantillas que nosotros tenemos y toda la actividad y todas las automatizaciones que hemos ido Armando directamente importables y descargables también tenemos varios recursos cursos de agentes de Inteligencia artificial Y tenemos sesiones en vivo Todas las semanas y comentarte que también tenemos un periodo de prueba de 7 días por si quieres entrar a probar la comunidad ver lo que hay aprovechar los recursos que están dentro puedes entrar completamente gratis por 7 días sin compromiso siempre y cuando canceles antes del día 7 Pero estoy seguro que una vez que entres te vas a querer quedar adentro Ahora sí vamos a armar esta automatización nuevamente por completo Si es que no conoces Qué es esta aplicación esta aplicación es make y es un lugar donde podemos crear flujos de trabajo completamente automatizados y podemos conectar más de 10,000 aplicaciones directamente entre sí Así que si no quieres armar toda esta automatización si es que entras directamente al classroom te vas a las automatizaciones y buscas Esta que está acá de prospecta y reacta propuestas personalizadas vas a encontrar una guía paso a paso con todo lo que vamos a ver en este momento y si es que bajas hasta el fondo vas a poder descargarte la plantilla de la automatización que vamos a armar Así que si entras acá a make.com aprietas los tres puntitos y le das a importar plantilla vas a poder usar esta plantilla que es esta de acá y se te va a cargar absolutamente todo pero igual te voy a mostrar paso a paso cómo lo podemos armar okay Así que ahora sí vamos a entrar a make.com y vamos a crear un nuevo escenario Una vez estando acá vamos a crear un nuevo webhook y vamos a mandar un custom webhook un webhook lo que va a hacer en el fondo es recibir Data desde un formulario o desde la aplicación que vamos a crear y vamos a trabajar con esa información directamente Okay entonces vamos a crear un nuevo webhook y le vamos a poner solo Travel versión 3 solo traveler porque esta es una aplicación que estamos Armando para viaje verdad le vamos a dar a guardar y aquí tenemos el webhook listo para recibir la información Okay después lo que vamos a hacer es vamos vamos a crear una interfaz directamente en b. neww entraremos a bolne y si no conoces bolt bolt es una aplicación que nos permite crear aplicaciones en base a texto es decir le digo Oye créame una aplicación de una interfaz de viajes donde rellenan un formulario y después mandas toda la información a x o al webp o al disparador instent ario para hacertelo aún más fácil te deje un prom listo que podemos comenzar a usar en bolt que es quiero que cree una aplicación que se llama esto que tenga estas páginas bla bla bla bla bla bla bla bla bla voy a copiar y pegar Esto justamente acá y le voy a decir quiero que le mandes la Data como Data estructurada al siguiente webcom y aquí es donde copiaremos esto y lo pegaré directamente Ahora sí si le damos enter Bol va a empezar a construir directamente la interfaz en la que nosotros vamos a trabajar ya que es esta misma interfaz que vte al principio del video que la construimos solamente con un plon Es realmente brutal y si no han usado bolt recomiendo que empiecen a probarlo Porque funciona superb para armar aplicaciones de una manera superrápida y todo con lenguaje natural como podemos ver acá se está empezando a armar la página tomamos matecito mientras espera y después de unos 30 segundos aproximadamente nos acaba de crear esta página que está acá tenemos mis viajes tenemos explorar destino bueno toda esta parte está en desarrollo Pero tenemos la parte de mis viajes que es lo importante tenemos un inicio que es superlindo y mis viajes que aparece aquí después si es que hay algo que me gustaría hacer en específico que sea un cambio podemos decírselo directamente acá por ejemplo quiero que cuando apretamos enviar plan de viaje aparezca globos en la pantalla le voy a dar Okay y y esto quiero que también lo tengan en cuenta porque el lenguaje de programación del futuro es el lenguaje natural este tipo de aplicación lo demuestran más que nunca o sea ha pasado muy poco tiempo desde el lanzamiento de los llm a un nivel global como chas gpt y esto solamente demuestra de que cada vez es menos necesario realmente saber programar pero sí es muy importante saber y conocer los sistemas de cómo funciona detrás todo esto Entonces esto lo que está haciendo es crearnos una página que le está mandando una señal a una automatización que se va a desencadenar es decir está mandando información a lo que se conoce como un webhook o un disparador instantáneo que es lo que nos recibe directamente la información y es la información con la que vamos a trabajar y como podemos ver ya se acaba de hacer el cambio aquí podríamos decirle lo que sea o sea cambiar el color eh agreg nuevos espacios para el formulario y en fin volveremos aquí a la aplicación y le vamos a dar a guardar y le vamos a dar a correr lo que está esperando mica ahora es recibir un webcup de la aplicación en Sí así que vamos a hacer la prueba y le voy voy a poner Santiago Chile la fecha de inicio desde el 29 hasta el 31 y quiero que contacte a cinco hoteles cinco restauranes y cinco actividades le voy a dar a enviar plan de viaje y ahí nos aparecieron algunos globitos Verdad que es lo que le pedimos pero lo importante lo que tenemos que verificar es si efectivamente recibimos la información aquí en el webhook y si es que abrimos vamos a ver que recibimos Santiago Chile eh la fecha la fecha cinco hoteles cinco restaurantes y cinco actividades Okay ahora sí podemos comenzar a armar nuestra automatización ya eh si no quieres armar toda esta automatización paso a paso Este es el momento en el que puedes importarla la otra automatización y simplemente cambiarle el webhook y reemplazar un par de variables pero también te voy a mostrar paso a paso cómo lo hacemos la automatización que vamos a armar es esta de acá tenemos tres partes se las voy a mostrar se me terrorifica pero no es tan terrorífica porque es la misma automatización que se repite tres veces así que lo que vamos a hacer es vamos a armar solamente una línea que vendría siendo esta de acá y esta de acá después la vamos a copiar y la vamos a pegar directamente tres veces la línea de arriba es para los hoteles o el alojamiento la línea del medio es para los restaurantes y la línea de más abajo es para las actividades y lo único que va a cambiar en estas tres es esto que está acá el redactar correo electrónico Por qué Porque le vamos a decir estamos contactando a un hotel y quiero que ofrezcas tus servicios a cambio de alojo después en el del restaurant estamos contactando un restaurant quiero que pidas cuatro comidas A cambio de y eh En las actividades estamos contactando a un centro de actividades quiero que le pidas una actividad en específico a cambio de un video etcétera Okay entonces vamos a armar una vez esto y después lo vamos a duplicar tres veces vamos a partir con lo primero que es tenemos los destinations acá es decir la información que acabamos de recibir lo primero que vamos a hacer es vamos a irnos a Flow control y vamos a agregar un iterator Porque queremos trabajarlos en grupos y que cada ciudad sea su propio grupo Así que vamos a apretar destinations acá y le vamos a dar a guardar si es que quieres aprender un poquito más de cómo funcionan los iteradores Y por qué estoy haciendo esto en la comunidad tenemos un curso que se llama make desde cero y puedes abrir exactamente este que está acá que es el procesamiento de listas iterator y puedes aprender un poquito más de cómo funciona entonces una vez que lo apretamos le vamos a dar a guardar y después tenemos que crear un router y este router lo que va a hacer es separarnos la automatización en tres posibles caminos para arriba si es que es hoteles para el medio si es que es restaurantes y para abajo si es que es actividades recordemos que esto lo podemos adaptar absolutamente como nosotros queramos pero para este caso lo vamos a hacer a así lo primero que tenemos que hacer es tenemos que hacer un llamado a una aplicación que se llama apify apify va a ejecutar lo que se conoce como un actor y va a conseguirnos directamente los leads en una ubicación en específico que estamos buscando apify la puedes encontrar en apy.com Y si que entras acá a los actores vas a ver que tenemos una tienda de muchos actores que nos sirven para scrapear datos o para conseguir datos de algo en específico tenemos para Buscar en Facebook para buscar en Instagram para Google Maps verdad Y nosotros vamos a usar Exactamente eso ya vamos a usar Google Maps extractor Por qué no Google Maps imail extractor Porque queremos conseguir primero la ubicación y después vamos a usar otra herramienta que se llama enail finder para conseguir los mails con mayor precisión que esta otra Google Maps extractor nos va a permitir conseguir directamente los negocios por ejemplo si es que yo estoy buscando un hotel en Santiago Chile Y le doy a correr actor lo que va a hacer acá va a ser directamente encontrarme estos 10 hoteles que están acá y si bien los podemos exportar lo que queremos hacer realmente es trabajarlos de una manera más automatizada entonces aquí tenemos todos los hoteles que nos los filtró por la ubicación Santiago Chile podemos ser super específico podemos poner barrios podemos poner comunas en el caso de que quisiéramos pero para este caso lo voy a dejar Más general para que nos aparezca el actor vamos a volver acá y vamos a darle a create task una vez que le demos a create task le vamos a poner un un nombre y le vamos a dar a continuar la razón por la que estamos haciendo esto es porque queremos que nos aparezca justo acá y una vez que hicimos eso vamos a buscar la Tas vamos a abrir a brif y vamos a darle a Run an actor es decir correr un actor en específico Qué actor vamos a correr el que acabamos de agregar justamente aquí esto se conocen como los actores Okay después cuando nos pide el input Jason es exactamente esto que está acá es qué es lo que quieres Buscar dónde quieres buscarlo y cuántos quieres buscar json es un código que nos sirve para ordenar variables Entonces nosotros lo podemos hacer de manera manual o de manera automatizada con el Jason Entonces el Jason vamos a apretar este botoncito que aparece acá y vamos a copiar esto que aparece y lo vamos a pegar acá con control shift B Por qué no control V porque si lo peg en control V nos aparece así y si es que lo pego con control shift y v nos aparece en orden pero yo no quiero Quiero buscar necesariamente en Santiago de Chile No yo quiero buscar en la variable de la ciudad que es la variable que mandamos Acá está acá y quiero buscarlo en la variable país que vendría siendo la variable de acá país y la voy a seleccionar Cuántos Quiero buscar ahora Estamos trabajando con hoteles verdad Entonces el número de los hoteles que yo rellené en el formulario y qué es lo que quiero buscar Okay hotel eso está perfecto le voy a dar a guardar y una vez que corre esta automatización Así tal cual lo que va a hacer es hacer el llamado a este rand verdad o a este actor en específico antes cuando corrimos la automatización Se demoró alrededor de 30 segundos en darnos los resultados Así que lo que vamos a hacer es vamos a poner un módulo de slip o de delay de 30 segundos le vamos a poner slip le vamos a poner 45 segundos Para estar seguros Entonces vamos a ando aquí recibimos la info del formulario reagrupando la información hacemos llamado al actor espera 45 segundos y después vamos a recuperar la información ya porque hicimos el llamado y ahora tenemos que recuperar la información que nos devolvió Así que nos vamos a ir a get dataset items el dataset ID vamos a buscar el default dataset ID que es este que aparece aquí en el límite de Cuántos vamos a recuperar va a ser el número de hoteles que nosotros queríamos y aquí sí le podemos dar a guardar y Aquí vamos a recuperar la info ahora si yo le doy a guardar a esta automatización Y le vuelvo a dar a correr puedo volver hacer exactamente el envío de este formulario que ahí se acaba de hacer enviar plan de viaje y si es que abro la automatización podemos ver que efectivamente Recibió la información que es el destino Santiago Chile bla bla bla y que se fue a hacer el llamado al actor podemos verificar que lo hizo si es que nos vamos a apify y nos vamos a Run podemos verificar que efectivamente acaba de hacer el llamado al actor y si es que abrimos la información vamos a ver que aquí tenemos el hotel barrio Hostal catedral ot del patio y en fin ya es decir que acabamos de hacer el llamado esperó y después nos devolvió toda la información de los hoteles el hotel un hotel 2 hotel 3 hotel 4atro y hotel 5 okay ya tenemos toda la información y las páginas web de los hoteles que queremos contactar lo que vamos a hacer ahora es conseguirnos su correo electrónico con una aplicación que se llama Any mail finder mi recomendación con Any mail finder es que te crees una cuenta en el plan anual ya pero te suscribas a los 3 días gratis y ahí te vas creando distintas cuentas en el caso de que no quieras realmente pagarlo Eh pero en tres días deberías poder contactar muchos lads Y si ya realmente decides que es algo y un sistema que quieres seguir usando ahí puedes evaluar la opción de pagarlo pero lo puedes probar completamente gratis al igual que apify que funciona gratis hasta los 5 una vez que nos creemos la cuenta en an email finder vamos a abrir la sección que sale Api y vamos a crear una Api key y ahora lo que tenemos que hacer es Buscar directamente el mail en base a un dominio Así que vamos a buscar el email finder y vamos a poner search for companies emails es decir Buscar los mails de la empresa vamos a buscar según El dominio y El dominio que nosotros estamos buscando es El dominio que nos quedó en específico donde sale Website Por qué nos aparece en blanco Porque si es que vamos acá vamos a ver que no logró conseguir una Website en este caso es decir no logró conseguir una página web Así que no vamos a ser capaces de conseguir el mail de ese lugar en específico Okay le voy a dar a guardar y ahora si es que corremos la automatización no vamos a tener una página web que buscar entonces la automatización puede presentar fallas Cómo arreglamos esto le decimos Oye quiero que avances al módulo de anime Fer solamente si es que tienes una Website entonces acá vamos a irnos a los filtros y vamos a agregar un nuevo filtro nuevamente Si es que te interesa aprender más sobre los filtros puedes ver el módulo de filtros y condiciones en el curso de make desde cero pero básicamente el filtro como dice su nombre es filtra Eh si es que se cumple un requisito que pase por este camino y si es que no se cumple un requisito que no pase por el camino ya eso es a muy grandes rasgos entonces acá es si es que tienen página web es decir si es que Website existe quiero que sigas avanzando si es que no existe la página web no quiero que sigas avanzando Okay entonces acá lo voy a renombrar y Esto va a ser conseguir email Así que vamos a darle a guardar y ahora sí si es que vuelvo a correr la automatización y vuelvo a enviar esto vamos a ver que efectivamente acaba de hacer el llamado nuevamente va a esperar los 45 segundo es decir que puedo servirme otro mate y como podemos ver efectivamente está corriendo ya o sea recuperó la información directamente nos devolvió los cinco hoteles que estábamos buscando y aquí comenzó a filtrar de si es que tienen página web entonces podemos ver que el uno no tiene página web pero el do 3 cu y c sí tienen página web esto lo podemos comprobar acá que el uno no tiene Pero el 2 3 cu sí tienen página web entonces logramos Conseguir tres páginas de los cinco después intentamos de sacar los correos electrónicos como podemos ver acá y los vamos recuperando Okay Cuál sería el paso siguiente si es que ya tenemos la página web Y tenemos el correo electrónico necesitamos Descargar la información de la página web para poder hacerle una propuesta mucho más personaliz Ada a la persona okay Para eso tenemos muchos métodos pero vamos a usar una de mis herramientas favoritas que es perplexity que nos permite directamente Buscar en la página web y descargar la información como si estuviésemos hablando con un chatbot Okay entonces vamos a abrir y vamos a arrastrar un nuevo módulo vamos a buscar el módulo de perplexity y vamos a poner a create a chat completion vamos a elegir algún modelo que sea online ya para que tenga acceso online y en el rol vamos a elegir usuario y en el mensaje vamos a decirle Necesito que analices la información de esta página web tanto Qué productos ofrecen como sus servicios lo más detallado posible sobre lo que hace básicamente extrae todo aquí le vo a poner página web y vamos a ponerle Website que es decir la página que acabamos de recuperar de todas maneras este pron lo dejé puesto un poquito más abajo si es que seguimos bajando acá bajamos bajamos llegamos a la parte de perplexity es analiza la información del negocio Okay máximo de tokens le voy a dar 1000 y le vamos a dar a guardar entonces acá estamos descargando la info del negocio No está cargando directamente pero se entiende Cuál es el paso que sigue ahora sí si es que ya tenemos el correo y ya tenemos la información del negocio necesitamos redactar el mail pero aquí también se puede presentar un problema que es que podemos tener una página web verdad Y podemos intentar de buscar su mail en base a la página web pero a veces no está disponible el correo Entonces vamos a poner un pequeño filtro acá entre conseguir el mail y descargar la información del negocio porque tampoco queremos Descargar la información del negocio si es que no tenemos el correo electrónico al cual le vamos a escribir Entonces vamos a agregar un nuevo filtro y esto es si existe correo ya es decir si es que el email existe le vamos a dar a guardar ahí Pasas a perplexity y ahora recién podemos redactar el correo con Open Ai lo vamos a redactar con Open Ai y vamos a darle a create a chat completion justamente con esta versión que aparece aquí si tienen un asistente también podemos escribirle directamente con el asistente Y si ya tienes conectada tu cuenta de openi a make.com vas a poder seguir haciendo Este paso que está acá si no has conectado tu cuenta de perplexity lo puedes hacer yéndote a agregar y copiando la a piki y pegándola esta la puedes encontrar en perplexity comom o perplexity mejor dicho te vas a la tuerca y te vas donde sale apic te vas a generar apik la copias y la pegas directamente aquí ya no es necesario tener perplexity Pro para esto pero sí es necesario que de cargues créditos lo mismo vamos a hacer en openi Vamos a darle agreg y vamos a pegar nuestra apq acá esta apq la puedes encontrar en platform open.com Si te vas al dashboard y te vas acá donde sale apis le vas a dar a crear una nueva llave secreta y la pegas exactamente aquí okay Aquí vamos a elegir el modelo que nosotros más queramos o el modelo que queramos usar para mí el o1 mini funciona perfectamente Y esta es la parte más importante de todo porque aquí es donde ya ya tenemos toda la información y aquí depende completamente de tu habilidad de pronte el mail que le vamos a mandar Entonces le voy a agregar un nuevo mensaje que va a ser de usuario el contenido del mensaje va a ser algo como Necesito que le redactes un correo electrónico a este hotel ofreciendo tu servicio de X a cambio de alojamiento Necesito que te reacte un correo bla bla bla bla bla bla ofreciendo una página web el servicio o la aplicación que tú le quieras dar ya para este caso va a ser eh videos a cambio de alojamiento en el contenido del texto vamos a irnos acá y yo te dejé un pront un poquito más acá que puedes literalmente copiar y pegar Pero lo importante es que el resultado esté en formato html ya porque si no e nos va a aparecer todo el texto escrito en una línea en el mail y queremos que salga en formato de párrafos ya entonces el prom que le pusa acá es eres un freelancer bla bla bla te dejo detaller de mi servicio y aquí tenemos que comenzar a rellenar las variables Entonces tu fecha aproximada de llegada será el 29 de enero y saldrás el 31 de enero el nombre de la empresa es el título de la empresa y se encuentra ubicado en esta parte de acá aquí te dejo un poco más de contexto sobre la empresa que es el resultado que nos va a dar perplexity esta parte importante haz el output en formato html es decir usarás párrafos para separar los párrafos en el cuerpo del mensaje Okay le vamos a dar a guardar ya tenemos todo reemplazado y le vamos a dar a guardar entonces este va a ser redactar el correo y finalmente el último paso va a ser mandarle el correo electrónico a el hotel ya para eso vamos a irnos acá vamos a agregar un nuevo módulo y podemos usar el módulo de Gmail de mandar un mail yo en lo personal Prefiero usar Outlook Eh así que hacer create y enviar un mensaje en Outlook también lo puedes hacer en gmail y en la propuesta o el asunto le voy a poner propuesta y le voy a poner el título el contenido que va a ir adentro va a ser el resultado de redactar el correo Y a quién se lo vamos a mandar Bueno se lo vamos a mandar al email que acabamos de conseguir Okay le vamos a dar a guardar en este caso y este va a ser el enviar propuesta personalizada Aquí también es importante le puedes agregar un attachment verdad con tus servicios etcétera También lo puedes hacer y finalmente Como me gusta mantener un orden más o menos de las cosas que voy haciendo vamos a ir dejando todo en un Google sheets para ello vamos a buscar gole sheets y vamos a apretarle al a a brow esto es lo que hace es agregar una fila directamente en el Google sheets por cada nueva entrada vamos a elegir el spread sheet ID que va a ser acá lista leads les voy a mostrar spread sheet ID para que se hagan una idea un poco de lo que vamos a estar viendo y de cómo se va a ir agregando Pero esto es netamente para poder tener un trackeo Okay aquí tenemos todo tenemos a qui le escribimos dónde es el mensaje y el mail s simple y cada vez que mandemos un nuevo correo se va a ir agregando directamente aquí Entonces como podemos ver ya he hecho varias pruebas he conseguido más de 70 correos porque yo poco a poco haciéndolo y probando esta automatización y haciéndole modificaciones Así que se van a ir agregando Ahí lo vamos a poner en la hoja uno y vamos a partir aquí le vamos a poner el título donde quedan le voy a poner la dirección cuál es el cuerpo del mail que le acabamos de mandar Este acá cuál es el correo que acabamos de mandárselo a este que está acá y cuál es el URL o la página que conseguimos bueno es la web site que aparece aquí okay le vamos a dar a guardar y listo la automatización ya está funcionando no hay nada más que le tengamos que hacer para que funcione la parte del Hotel hagamos la prueba antes de duplicarlo verdad y ponerlo tres veces porque lo que vamos a hacer después es copiarlo y pegarlo y lo vamos a poner justo acá y nuevamente acá Okay pero comprobemos que esto está funcionando como no quiero mandarle los correos electrónicos de propuestas que no voy a cumplir voy a reemplazar este campo acá por mi correo electrónico directamente Okay entonces va a ser acá guardar guardar y le vamos a dar a correr automatización nuevamente volveré a bolt y esta vez le vamos a pedir 10 hoteles directamente enviar plan de viaje nos aparece los Globos es decir que se mandó y está corriendo toda la automatización ya vamos a ir viendo paso a paso Qué es lo que está haciendo sé que lo hemos visto pero a veces es importante vol a entender todo el flujo aquí estamos recibiendo la información la estamos reagrupando y reordenando y estamos haciendo el llamado al actor ya es decir Estamos buscando la información ahora estamos esperando 45 segundos para asegurarnos de que efectivamente se terminó de scrapear o de conseguir toda la Data de Google Maps de los negocios a los que vamos a contactar y después estamos recuperando directamente esa información ya la información que incluye la ubicación el nombre del negocio las páginas etcétera después empezamos a conseguir el mail directamente si es que tiene página web conseguimos el mail y si es que tiene mail o logramos conseguir un mail empezamos a descargar la información del negocio si es que descargamos la información del negocio vamos a redactar el correo electrónico y si es que redactamos el correo electrónico vamos a mandarlo y se va a archivar esto lo podemos comprobar justamente acá que se acaba de agregar que es esto que está aquí Okay Eh podemos confirmarlo también si es que entramos al mail actualizamos el correo electrónico vamos a ver queé recibimos aquí directamente Espero que este mensaje se encuentre bien soy un apasionado bla bla bla bla bla bla en fin podemos decir que la automatización está funcionando como podemos ver acá el output nos dio directamente 10 grupos distintos Entonces se va a empezar a ejecutar 10 veces uno para cada uno de ellos Okay Eh sabemos que está funcionando Así que lo voy a pausar y podemos ver que está funcionando porque seguimos recibiendo los correos electrónicos Así que ahora lo que vamos a hacer es vamos a volver acá y vamos a crearlo también para los restaorantes y lo vamos a volver a crear para las actividades pero esta parte ya es mucho más simple porque ya está funcionando todo el sistema de una así que vamos a directamente seleccionar todo esto voy a eliminar este módulo eliminar este módulo y lo voy a volver a pegar acá y lo volveré a pegar acá voy a apretar este botoncito mágico que es auto alinear nuevamente y Listo Ya ahora solamente tenemos que reemplazar un par de variables y va a quedar perfecto lo primero que vamos a hacer es necesitamos definir que cuando recibimos los hoteles se vaya para arriba cuando recibimos los restaurantes se vaya por el medio y cuando recibimos los tours o las actividades se vaya por abajo para ello vamos a hacer clic derecho y vamos a agregar un Fil si es hotel le vamos a poner es decir cuando hotel existe va a irse por arriba después le vamos a poner otro filtro que es si es restaurant es decir si es que restaurant existe se va a ir por acá y después le vamos a poner si es tour es decir si es que actividad existe se va a ir por abajo y la razón por la que estamos haciendo esto porque queremos realmente trabajar cada uno por sí solo Okay vamos a hacer el llamado al actor después antes lo teníamos puesto con ciudad país y hoteles ahora Necesitamos hacerle unos pequeños ajustes ciudad país pero ya no queremos el número de hoteles sino que queremos el número de restaurantes y no queremos Buscar Hotel sino que queremos Buscar restaurant le voy a dar a guardar y voy a hacer lo mismo aquí abajo no quiero Buscar hoteles sino que quiero buscar actividades y no quiero buscar hotel sino que quiero buscar tour nuevamente esperaremos 45 segundos recuperaremos la info Pero esta vez el límite no va a ser de los hoteles sino que va a ser de el número de restaurant y no va a ser de los hoteles sino que va a ser el número de actividades ya o sea cambiamos este cambiamos este cambiamos este cambiamos este y ahora conseguir el mail va a quedar Exactamente igual lo mismo acá Descargar la información del negocio va a ser igual lo mismo acá pero este si es importante de que cambie por qué Porque queremos redactar el correo y antes en el prom decíamos que queremos cambiarlo Porque queríamos alojo verdad o queríamos alojamiento ahora para el caso del restaurant no queremos alojamiento sino que queremos cambiarle y pedirles comida entonces ofreces tus servicios a cambio de cuatro comidas completas o lo que tú quieras te dejo más detalles bla bla bla tu fecha esto no sé qué no sé qué no sé qué encontrarás perfecto y eso es todo lo que tenemos que cambiar ya podemos darle el contexto que nosotros queramos para ir haciend le voy a dar a guardar y voy a hacer lo mismo para los tours abriré esto y le pondremos que ofrezco ofrecemos nuestros servicios a cambio de un tour completo x que incluye piezas listas para publicitar bla bla bla bla bla bla y guardar Ahora sí si es que le damos a guardar la automatización Ya está lista y lista para correr hagamos la prueba Okay vamos a ir acá le vamos a dar a guardar y le vamos a dar a correr si es que entro aquí a directamente Vamos a ponerle Santiago quiero contactar no sé ocho hoteles ocho restaurantes y ocho actividades y quiero Agregar un nuevo destino que sea eh No sé Montevideo en Uruguay quiero quedarme allá Desde el dos hasta no sé el o por ejemplo y y quiero contactar digamos lo mismo 88888 si es que está corriendo la automatización le voy a dar a enviar plan de viaje listo se acaba de mandar y podemos ver que recibimos aquí los destinos el primero que es Santiago de Chile y el segundo que es Montevideo que Lo separó en dos grandes grupos ya correrá primero todo esto es decir toda la automatización de las tres líneas en específico línea por línea y después volverá y va a correr todas las de Uruguay ya de montevido en específico Así que ahora tenemos que esperar tenemos que verificar vamos a abrir nuestra lista que hasta el momento nos quedamos aquí justo acá solo voy a pintar para poner la referencia y vamos a esperar un par de minutitos A ver cuántos mails va a enviar y vamos a analizar un poco los números y aquí acabo de pausar la automatización Pero podemos ver que efectivamente se mandaron muchos correos electrónicos que vendrían siendo todos estos de acá después los de abajo si es que entramos a mi correo electrónico vamos a ver todos los mails que recibimos y cada uno era una propuesta personalizada ya ahí seguimos recibiendo que vendría siendo este de acá que son los de Montevideo directamente planeo estar por acá eh después tenemos este después tenemos las otras de acá y todas estas son propuestas personalizadas que directamente recibimos para cada uno o que mandamos para cada uno de ellos est esta esta esta Entonces es s super interesante porque toda la parte de conseguir el alojo o conseguir estos leads o conseguir este restaurant o cualquiera sea eh la industria que estamos buscando la podemos externalizar a este sistema y recuerda que este sistema puedes literalmente descargarlo copiarlo y empezar a implementarlo desde hoy Entonces es s super interesante y en el caso de que queramos dejar corriendo este sistema podemos darle a Run once es decir correr una vez o podemos dejarlo prendido aquí mismo para que cada vez que recibimos un web hooko cada vez que enviamos este formulario que está acá se empiece a ejecutar si apretamos este botoncito arriba la derecha que aparece deploy vamos a dejar este formulario activo y corriendo para que lo podamos usar simplemente entrando al link que nos van a dar entonces apretaría acá y tenemos el formulario que está funcionando acá si nos vamos dentro de mis viajes Okay s super interesante Recuerda que puedes entrar el perod digital puedes descargarte la plantilla después si quieres te puedes salir Pero si quieres realmente sacarle el máximo provecho al mundo de las automatizaciones que de los agentes para enfrentar digamos este 2025 y está dentro de la ola o mantenerte al tanto de lo que está pasando y los sistemas que podemos armar con Inteligencia artificial recomiendo que entres pruebes esos s días gr gratis y después decidas Digamos si es que te quieres quedar o te quieres salir de la comunidad de imperio digital Recuerda que también tenemos clases en vivo absolutamente Todas las semanas si es que subimos acá vamos a encontrar la sección del calendario y vamos a tener secciones en vivo donde podemos ir resolviendo dudas donde vamos a ir Armando automatizaciones exclusivas y puedes Navegar todo el contenido que está en imperio digital probando esos siete días gratis así que sin más que dec Espero que este sistema te funcione recuerda está todo publicado acá si es que quieres entrar e importar la plantilla puedes hacerlo pero también siento que es importante que vayamos conociendo Cómo armamos estos sistemas Cómo funcionan estos sistemas y en fin Recuerda que esto también lo puedes personalizar absolutamente como tú quieras o sea sea que tienes una agencia y quieres conseguir clientes sea que quieres buscar eh influencers sea que quieres buscar restauranes quieres buscar clínicas dentales absolutamente lo que quieras puedes comenzar a aplicar este sistema desde ya así que sin más que decir se deseo mucho mucho éxito que te sirva si te gustó este video recomiendo que te suscribas al Canal porque vamos subiendo muchos videos de este estilo y también recomiendo que veas los otros videos que vamos subiendo porque quizás hay alguna automatización que te puede interesar de hecho según YouTube esta automatización que aparece acá te puede interesar bastante así que sin más que decir Te deseo lo mejor ya nos vemos [Música]
