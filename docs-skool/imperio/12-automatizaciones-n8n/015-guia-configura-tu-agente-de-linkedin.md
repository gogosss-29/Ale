# 👑 [GUIA] Configura tu Agente de LinkedIn

> Ruta: Automatizaciones n8n › 👑 [GUIA] Configura tu Agente de LinkedIn

**🎬 Vídeo (17.0 min):** https://www.loom.com/share/219866bc26964cb689e61f60c64f56a2

**📎 Recursos:**
- Linkedin Agente Auténtico
- [Plantilla Sheets](https://docs.google.com/spreadsheets/d/1VLehRMvAzDgUiU2DipNCeYqVykxMbM6wUSuqFqJxG6U/edit?usp=sharing)

---

## Guía Técnica: Cómo instalar y configurar tu Agente de LinkedIn en n8n (Paso a Paso)

Si llegaste acá, es porque seguramente ya viste cómo funciona este Agente de IA para LinkedIn y los resultados que puede darte. Si aún no ves la "magia" o la lógica detrás de esta automatización, te recomiendo partir por el video principal donde te explico el concepto completo: 👉 [https://www.skool.com/imperio-digital/classroom/8e2ffdbc?md=9e04d92c52a44093a8df35d2cfcccfd4](https://www.skool.com/imperio-digital/classroom/8e2ffdbc?md=9e04d92c52a44093a8df35d2cfcccfd4)

Ahora sí, vamos a lo técnico. En este post vamos a ensuciarnos las manos. Te voy a guiar clic a clic para importar la plantilla, conectar las APIs y dejar a tu agente listo para entrevistarte mañana mismo.

Vamos directo al grano.

---

### Paso 1: Importar la Plantilla y la Base de Datos

Lo primero es tener la estructura lista. Vamos a necesitar dos cosas: el "cerebro" (n8n) y la "memoria" (Google Sheets).

1. **En n8n:** Descarga el archivo JSON de la plantilla (lo tienes en la descripción del video) e impórtalo en un nuevo workflow. Verás que aparecen tres etapas: Contexto, Preguntas Diarias y Generación de Contenido.  [https://docs.google.com/spreadsheets/d/1VLehRMvAzDgUiU2DipNCeYqVykxMbM6wUSuqFqJxG6U/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1VLehRMvAzDgUiU2DipNCeYqVykxMbM6wUSuqFqJxG6U/edit?usp=sharing)
2. **En Google Sheets:** Duplica la plantilla que te compartí. - Dale a "Archivo" > "Hacer una copia".
- Guárdala en tu Drive. Esta hoja es clave porque aquí se guardará tu información.

---

### Paso 2: Crear y Conectar el Bot de Telegram

Telegram será tu interfaz de usuario. Aquí es donde el agente te hablará.

1. Abre Telegram y busca a **@BotFather**.
2. Escribe el comando `/newbot`.
3. Ponle un nombre (ej: `Agente LinkedIn V3`) y un usuario (debe terminar en `bot`, ej: `BenjaLinkedin_bot`).
4. BotFather te dará un **Access Token**. Cópialo.
5. **En n8n:** Ve a las credenciales de Telegram y pega ese token.

**⚠️ Truco para el Chat ID:** Para que el bot sepa que eres tú, necesitas tu Chat ID.

- En el nodo de Telegram (Trigger), dale a "Listen for Event".
- Ve a tu nuevo bot en Telegram y escríbele "Hola".
- En n8n verás que llega la data. Busca el campo `chat.id` (es un número largo) y cópialo.
- Pega ese número en todos los nodos de Telegram donde te pida "Chat ID".

---

### Paso 3: Conectar Google Sheets

Esta parte es vital. Aunque importes la plantilla, n8n no sabe cuál es *tu* hoja de cálculo.

1. Abre cada nodo de Google Sheets en el workflow (son varios: guardar contexto, leer tópicos, guardar post).
2. Conecta tu cuenta de Google.
3. **Importante:** En el campo "Document", selecciona tu copia de la hoja que creamos en el Paso 1.
4. Asegúrate de mapear la hoja correcta (`Context`, `Questions` o `Content`) en cada nodo según corresponda.

> **Ojo:** Haz esto con calma en cada nodo. Si te saltas uno, la automatización fallará porque no encontrará dónde escribir.

---

### Paso 4: Conectar la Inteligencia (OpenRouter y Replicate)

Ahora démosle cerebro y ojos a esto.

**Para el Texto (OpenRouter):**

1. En los nodos de "AI Agent", conecta tu credencial de OpenRouter.
2. Elige el modelo que prefieras. Yo uso **GPT-5.2** (o GPT-4o) para la redacción final porque escribe mejor, y modelos más ligeros (como Flash o GPT-4 mini) para tareas simples como generar preguntas.

**Para las Imágenes (Replicate - Opcional):** Si quieres que genere fotos tuyas:

1. Ve a , crea tu cuenta y busca tu API Token.
2. Pégalo en el nodo `HTTP Request` de n8n (Authentication: Header Auth).
3. **El Prompt Visual:** En el cuerpo de la solicitud (Body), verás un enlace a una imagen. **Cámbialo por una foto tuya real** que tengas alojada en internet (puedes subirla a imgbb o similar y copiar el link directo). Esto sirve para que el modelo "Nano Banana" sepa cómo es tu cara y tu ropa.

---

### Paso 5: Prueba de Fuego

Ya está todo conectado. Hora de probarlo.

**1. Generar Contexto:** Ejecuta la primera parte del workflow manualmente. El bot te pedirá en Telegram: "¿Quién eres?".

- **IMPORTANTE:** En Telegram, mantén presionado el mensaje de la pregunta y selecciona **RESPONDER**. Si no respondes sobre el mensaje, el bot no sabrá a qué te refieres.
- Mándale un audio de 1 o 2 minutos contando tu vida, tu negocio y tus gustos.
- Revisa el Google Sheet: Si ves que la pestaña "Context" se llenó con tus datos, ¡funciona!

**2. Pregunta Diaria:** Simula el trigger de "Preguntas Diarias". Te debería llegar una pregunta aleatoria basada en tus temas (ej: "¿Cuál fue tu mayor error al vender?").

- Responde con un audio (usando la función "Responder").
- Espera unos segundos... y deberías ver en tu Sheet el post redactado y (si lo activaste) la imagen generada.

---

### ¿Listo para automatizar?

Parece técnico al principio, pero una vez que haces estas conexiones, no tienes que volver a tocarlas. Tu único trabajo será responder un audio mientras te tomas el café.

Recuerda que si quieres entender la estrategia de contenido detrás de esto y por qué lo estructuramos así, tienes el video completo aquí:

## 🎙️ Transcripción

Ok, familia, a continuación les voy a mostrar cómo hacemos la importación y la conexión de la gente del Inquien, eh, realmente interesante, te voy a mostrar el paso a paso, vamos directo al grano. Cuando entra en perro digital te vas a encontrar con algo así obviamente mucho más bonito, vamos a descargar a la gente, eh, este de la gente directamente, vamos a crear todo desde cero de nuevo, todo esto por fines de, eh, vamos a guardarlo, ok, por en ese caso, todo esto con fines de mostrarte cómo lo importamos directamente desde 0. Entonces, vamos a crear el curflow, vamos a darle los tres puntidos y vamos a importar los dos para que que funcionan, lo vamos a hacer todo desde 0, voy a sumir que no tienes absolutamente nada, ¿ok? Cuando lo importemos, se va a importar algo así, segundo paso de lo que tenemos que hacer es tenemos que duplicar la plantilla de Drive que les deje acá, esta plantilla acá. Entonces, esta plantilla vamos a llegar, vamos a hacer una copia. Ok, hacer una copia y va a hacer copio contenido federal, no sé, igual. Ok, teniendo esto, ya tenemos las dos cosas que necesitamos y las dos plantillas importadas. Tenemos las tres etapas que son las de juntar el contexto, tenemos la de las preguntas diarias y tenemos la de general contenido basado en tu respuesta. Vamos a juntar el contexto primero. Para juntar el contexto, lo que tenemos que hacer es entrar a Telegram, vamos a entrar acá previamente y vamos a buscar la conversación con botfader si es que no tienes botfader puede buscar botfader Telegram enter launch botfader cuando le deja launch start bot se le va a abrir exactamente esto, una vez que esté acá le vas a decir new bot, le vas a poner un nombre le vamos a poner v3 agente linkadin bot y después vamos a copiar esto, este access token lo vamos a copiar y lo vamos a pegar acá, vamos a ir nos acá vamos a darle a crear una nueva función, vamos a conectar la gente, oops va a ser versión 3 bot vamos a conectar a la gente y vamos a darle a guardar que estemos acá va a estar guardado vamos a poner red bot y vamos a ejecutar este paso en específico este paso te va a decir que tenemos que chequear nuestros parámetros ok ya perfecto eso es lo primero que tenemos que hacer es crear la credencial luego vamos a empezar a reemplazar la credencial en cada uno de estos, entonces tenemos acá B3 bot en específico y lo reemplazamos, después acá download voice, vamos a reemplazarlo con B3 bot, después donde más lo tenemos aquí arriba, vamos a reemplazarlo con B3 bot, y eso lo vamos a hacer con todos y una vez que ya no hay más, debería estar funcionando esto. ¿Por qué no funciona todavía? Porque tenemos que reemplazar el chat IDP pero ya te explico cómo hacemos esto. Vamos a edificarse que esto está funcionando, voy a cerrar esto acá, y voy a irme acá donde sale V3 agente y le vamos a dar a Start. Ok, vamos a agregar un nuevo nuevo y este nuevo se llama Telegram. Telegram, vamos a buscar los triggers y vamos a esperar wait for a message, un message en específico acá, betrez bot y le vamos a dar a execute step, ahora sí, oops, vamos a ejecutar el step, vamos a irnos acá y le vamos a poner, pero vamos a ver si escuchamos el evento y perfecto, lo escuchamos, esta idea en específico es el que tenemos que buscar, es from id, acá, vamos a darle ahora aquí y lo que queremos buscar es reemplazar los chat ID ok entonces chat ID este lo vamos a reemplazar vamos a reemplazarlo también aquí no si no acá en el sender and reply de que queremos que llegue bueno del chat ID en específico y lo vamos a reemplazar, download voice, esto debería estar bien, si está bien, perfecto, merge it feels, aquí no tenemos que reemplazar nada, aquí tampoco, ok, listo ya no tenemos que reemplazar nada más, entonces ahora lo que vamos a hacer es vamos a hacer el envío del audio ya pero antes necesitamos mapear específicamente cuáles son los cheats que vamos a sacar entonces vamos a abrir cada uno de los cheats y los vamos a poner nuevamente tenemos los cheats tenemos acá los get rose y necesitamos buscar el contexto el contexto está por acá Max está intentando pasar por abajo de la cámara si y tenemos que reemplazar cada uno vamos a conectar nuestra cuenta de Google cheats acá en cada uno de las partes que sale cheats entonces vamos preguntas diaria, sheets, vamos a poner contexto y vamos a poner context, ya importante, acá vamos a tener que cambiar y poner el copy of contenido, entonces probablemente tenemos que volver a hacer todo, así que ahora sí, context y lo vamos a cambiar, después vamos a hacer lo mismo, acá en sheets, ya, esta parte importante que le hagan, porque incluso si es que tiene el mismo nombre puede ser que cambia, entonces acá, si te fijas acá, tenemos el context de nuevo y tenemos que buscar el copy of tag y buscamos el context perfecto vamos a hacerlo mismo ahora en el get context que es cambiar copy y context perfecto y después el save context que lo vamos a poner acá copy y vamos a dejar el context y finalmente el update, vamos acá, cambiamos nuevamente el copy of contenido, perfecto y acá en el save vamos a hacer lo mismo copy of contenido y perfecto, ahora vamos a guardar, dicho esto y hecho esto ya debería estar hecha la conexión de Gullsheets y la conexión con Telegram, es decir que por lo menos hasta acá debería estar funcionando bien. Vamos a hacer primero la primera parte en específico, antes de terminar con el resto de la conexión. Entonces vamos a comenzar por acá, vamos a verificarse que está todo funcionando, bueno, vamos a también conectar los modelos en específico por si acaso porque en el momento de importar lo puede ser que no los tengas conectados ya así que vamos a ir al primer agente de día y vamos a conectar el modelo de OpenRouter con el modelo que tú quieras, este caso voy a usar la Gemini 3 Flash, después vamos a hacer lo mismo con el otro AI Agent, acá voy a usar gbt5.2 y después acá también voy usar gpt 5.2 y en el long post también voy a usar gpt 5.2, ok? vamos a aprovechar de hacer esta conexión de una en verdad para después ya no tener que volver a hacer nada para este vamos a hacer el 4.1 y esta es la parte de generar la imagen, toda esta parte copiamos la hagamos exactamente igual como lo estoy haciendo y después te voy a explicar un poco mejor cómo funciona pero hagamos las conexiones de una, htdbrequest lo único que tienes que modificar acá es que va a parecer algo así vamos a irnos a buscar nuestra API de Replicate para ello vamos a ir a Replicate.com acá vamos a irnos aquí arriba vamos a buscar a Pitocans en a Pitocans vamos a dar la crear vamos a copiar el a Pitocans y lo vamos a pegar acá vamos a apretar acá y vamos a crear una nueva creensión, pegar, ver, y le damos. En esa parte vamos a asegurar de borrar lo que ya acabamos a mostrar, pero bueno, después vamos a estar acá en el prompt y en el prompt vamos a cambiar la imagen que nosotros tenemos de nosotros mismos. Para este caso la imagen es esta, que yo la voy a copiar, la subida imhp.com y la reemplazo aquí, ok. Dicho y hecho esto, ya tenemos nuestro, nuestra parte conectada, en específico a la nueva nana y después tenemos que acá, no tenemos que hacer nada más porque estuve está conectado, entonces dicho esto y hecho esto vamos a partir con la automatización. la primera parte es ejecutar el workflow y responder las preguntas, entonces le voy a ejecutar y vamos a ver qué vamos a recibir una serie de preguntas, vamos a que voy a contestar las y voy a decir aquí recibir un mensaje de telegram voy a entrar acá y este es el V3, ahora sí esta parte es muy importante cuando respondan estas preguntas van a tener que mantener apretado acá y poner con testar a las preguntas, verdad que no estoy con la cámara acá, reply y después mandan el audio, ya, porque si no, no les va a identificar y no va a saber qué pregunta está respondiendo, no va a saber si es de contexto o las que te llegan diariamente, etcétera. Vamos a hacer esta versión super super corta ya que la hice un poco más largo en el video, pero en fin, mi nombre es Benjamin Cordero, soy cofundador de una comunidad que se llama Imperial, me gustan los perros, me gustan las automatizaciones, las comunidades de automatizaciones de inteligencia artificial, me gusta el café, me gusta la escala, me gusta viajar, me gusta hacer de borte, me gusta conocer cosas nuevas, me gusta, las automatizaciones con N8N, la inteligencia artificial, me gusta ir a eventos, me gusta saber de fiesta, me gusta la música rock, me gusta, en fin, hay creo que queda bastante claro, mi audiencia es personas no técnicas y técnicas que quieren automatizar su negocio mediante automatizaciones con inteligencia artificial, tanto para aplicarla en su negocio o para venderlas a terceros como un servicio. Lo voy a dar a esta parte importante, antes de darle a Enter, voy a asegurar de que estemos recibiendo la información, lo voy a dar a ejecutar acá y ahora sí le voy a mandar el audio. Ahora está esperando un trigger y acabo de mandar el audio. Y recibimos el audio, estamos transcribiendo el audio, estamos descargando la voz, transcribiendo el audio en específico, y ahora se fue por arriba, así que si es que me voy acá y me voy al contexto, vamos a ver que se debería empezar a actualizar en 3, 2, 1, todavía no se actualiza, se está morando un poco la gente, pero en fin de estar haciendo un buen trabajo y listo, ahí se debería actualizar, vemos que se actualiza acá y me da todo el contexto, y me empieza a crear los tópicos con los que vamos a trabajar, ok? dicho y hecho esto podemos pasar a la segunda fase diariamente ya quedó el contexto listo, ok? entonces diariamente me va a empezar a mandar las preguntas por telegram que son, oye, que son las cosas que te interesan en base a esto podemos ver acá que tenemos varias listas de tópicos entonces supongamos que dieron las 4 pm y se corre esta automatización se ejecuta, empieza a sacar cierta información específico, empieza a generarme las preguntas, saca uno de los 20 tópicos que me escribaba acá, música roca, eventos, perros, café, automatización, etcétera y toma cuatro específicos todos los días. Aquí tomo ejecución de automatizaciones, conocer cosas nuevas y vida nocturna, ok? Y me empieza a llegar acá en el celular como distintas automatizaciones y distintas cosas. ¿Qué es lo ideal que más disfrutas para salir de fiesta y como el liger es el lugar ideal para pasar una noche, de rock, ¿qué pasa abortumente en momentos justo antes de adelante para ejecutar un proceso crítico? ¿Cuál ha sido el descubrimiento experiencia más reciente que te ha sacado por completo de tu zona de confort? ¿Cuál es el derro más común que es cuando alguien intenta vender automatizaciones con ellas sin tener experiencia abrevia? Suponcamos que quiero responder esta última. Voy a la responder acá, voy a darle el audio, recordemos seleccionar esto y decir, uno de los errores más comunes que vean las personas es no quantificar cuánto es el roi que te va a dar esta automatización en concreto. La gente y los dueños de negocio toman decisiones en base a el roi esperado y en base a esto deciencias que un inversión que están dispuesto a ser o no. Entonces el hecho de no quantificar metricamente cuántas horas está ahorrando, cuánto dinero está ahorrando directamente al momento de implementar una automatización específica es un error común que veo en la gente que está partiendo en el mundo de las automatizaciones. Ok, ahora sí, vamos a darle ejecutad el workflow justamente acá en específico esperando el trigger voy a mandar acá la respuesta y vamos a ver qué se está enviando la voz ok se está enviando está empezando a crear la publicación está mandando la publicación corta en específico está también creando la publicación larga en paralelo y recordemos que todo esto se va a actualizar en tiempo real ya para este caso va a crear la imagen también, recordemos que podemos usar un panco de imágenes en el caso de que no queramos crear las imágenes con dano banana porque dice que no te ves bien o que tienes algo que no eres exactamente igual nuevamente, yo soy participé de que lo que importa es la intención no directamente el, como el sí es que me veo bien o no, estamos en el link y no estamos en Tinder y dicho esto ya empieza a crear la automatización, se manda acá, empieza a crear la imagen, podemos ver que se mandó la imagen, se está procesando toda esta imagen, tenemos el ID, podemos ver que sigue procesando y que acaba de terminar, acaba de terminar y aquí está mostrando y está creándome una imagen en específico, bien concreta, no es la imagen favorita, pero en fin, da igual. Este problem lo puede ir modificando, pero está bastante buena, o sea, creo que me parezco bastante en un par de años más, quizás, pero en fin, aquí por aquí va la idea de la automatización que estamos implementando. Aquí no despera, se lo buse en un minuto. Esto es importante, porque necesitamos esperar que se complede el minuto antes de extraer específico que es lo que vamos a hacer. Y ahora sí que entramos acá y entramos al contenido podemos ver que el ron número uno al vender automarizaciones conías sin experiencia es este hablas de locura y no hay cuánto dinero bruce he visto demasiada gente intentar vender world free de automarizaciones como si fuera un gadget pero el dueño de negocio se le está pensando esto me deja más plata vamos a perderme los tiempos y si no cuantificas el rollo ok perfecto con esto en específico ya lo tenemos listo podemos entrar podemos copiarlo podemos pegarlo, podemos ver la imagen que quedó acá, aquí, acá, y listo, ahí tenemos la imagen que la descargamos, la copiamos y la ponemos el link. Lo interesante, esto es que puedes decir cualquier cosa que se te venga, la mente estas preguntas son, literalmente, una guía que después te van a dar, pero puedes empezar a compartir experiencias un poco más personales y puedes empezar a crear contenido un poco más auténtico escapando de todo el ruido que existe de contenido, GPT, crea claramente con Dali y esos postos riles en el link en que uno es el 80% de las publicaciones, así que dicho esto, este fue el paso a paso de cómo implementar esta plantilla, paso a paso de todo. O sea, como vemos, no es muy difícil, no es muy difícil, esta sección en azul ya no se vuelve a hacer, a menos que quieras actualizar el contexto. Las preguntas diarias van a ejecutarse de manera como dice su nombre diaria ok y si quieres ir actualizando el contexto también lo puedes hacer si es que no crees hacer la parte de generar las imágenes te la puedes saltar conectando este modulo hasta acá y ahí tienes ya la automatización de el agente de cómo funciona esto lo voy a eliminar de cómo funcionaría y cómo lo conectamos paso a paso para crear contenido que no suena y te tira a distancia kilómetros de distancia, este contenido fue hecho con IA.
