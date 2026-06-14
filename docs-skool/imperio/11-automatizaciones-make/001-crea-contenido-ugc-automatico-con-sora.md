# 📽️ Crea Contenido UGC automático con Sora

> Ruta: Automatizaciones Make › 📽️ Crea Contenido UGC automático con Sora

**🎬 Vídeo (32.3 min):** https://youtu.be/PcXe9oej_z4

**📎 Recursos:**
- Plantilla UGC Automatizacion Make

---

Hoy les traigo una automatización que quedó **realmente brutal**.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cf06738f38c14e27a717112c3d3a4e4e15f459dcf4154e6594b25d88d6d584eb-md.png)

Con esta automatización puedes generar **videos UGC completos** (persona hablando del producto, tono natural, estilo “review honesta”) usando **solo una foto**.  
  
No necesitas actores, micrófonos, cámaras ni edición.

La interfaz está hecha en **Bolt** y la automatización corre completa en **Make** usando **Sora** como motor de video.

El flujo es:  
**subes imagen → Make procesa → Sora genera → recibes video listo para descargar**.  
Todo eso, 100% automático.

---

# 🔧 Cómo funciona:

## 1. Interfaz en Bolt

Creamos una app simple con el** prompt que te dejo al final**, donde ingresas:

- Nombre del producto
- Imagen
- Descripción
- Info adicional (tono, emoción, contexto)

Apenas presionas **“Generar video”**, Bolt envía todo a Make vía webhook.

---

## 2. Webhook en Make

Make recibe los cuatro parámetros y genera un `video_id` para trackear toda la generación.

Todo queda registrado en un Google Sheets.

---

## 3. Procesamiento de imagen

Make hace tres tareas clave:

- **Descargar la foto**
- **Redimensionarla a 720×1280** (formato UGC vertical)
- **Convertirla a PNG** para evitar errores en Sora

Esto deja la imagen lista para usar como input del modelo.

---

## 4. Generación de video con Sora

Make llama al modelo **Sora 2** (o Sora 2 Pro si quieres más fidelidad).

Le pasa:

- El texto del prompt
- La imagen procesada
- Las variables del usuario
- La duración del video

El modelo genera un video UGC corto, ideal para anuncios o pruebas de creativos.

---

## 5. Subida y conversión

Cuando Sora termina:

- Subimos el video al Drive
- Creamos un link compartible
- (Opcional) Convertimos el archivo con CloudConvert a MP4 limpio
- Guardamos todo en Sheets

---

## 6. Retorno a Bolt

Make le devuelve a Bolt:

- `video_id`
- `status: completed`
- `url` del video listo
- `download_url`
- `thumbnail_url`

Bolt refresca la interfaz y muestra el **video final listo para reproducir**.

---

# 🧩 Prompt de Bolt.new (para replicar la interfaz)

```
Crea una aplicación llamada "UGC Imperial" con un tema oscuro elegante (fondo gris casi negro #0F0F11, texto blanco, acentos violeta #7C4DFF).

Esta app permite generar videos UGC publicitarios conectándose al webhook de Make:

https://hook.us1.make.com/b9p5guwrnhlw4u5h9t8bw72sks7lkyxb

Diseño general minimalista, moderno y rápido.

Todos los campos deben tener bordes redondeados y fondo gris oscuro (#1C1C1E).

---

INTERFAZ EN ESPAÑOL - DISEÑO SIMPLIFICADO:

- Sin sidebar ni menús laterales

- Header simple con logo "UGC Imperial"

- Una sola pantalla: "Crear Video UGC"

---

FORMULARIO PRINCIPAL:

Título: "Crear Video UGC"

Subtítulo: "Describe el concepto de tu video y qué quieres crear..."

Campos (todos con placeholders en español):

1. Nombre del Producto → campo de texto

2. Imagen del Producto → campo de texto (URL input)

3. Descripción → campo textarea

4. Información Adicional → campo de texto (opcional)

Botón principal: "Generar Video" (color violeta #7C4DFF)

---

FUNCIONALIDAD DEL WEBHOOK:

Al presionar "Generar Video", enviar datos como JSON al webhook con esta estructura:

{

  "product_name": "...",

  "product_image": "...",

  "description": "...",

  "additional_information": "...",

  "status": "create"

}

IMPORTANTE: Incluir status: "create" en la primera llamada junto con toda la información.

---

PANTALLA DE CARGA:

Después de enviar el formulario:

- Mostrar pantalla de carga elegante con:

  * Spinner grande morado girando

  * Mensaje: "Generando Tu Video"

  * Animación de puntos rebotando

  * Botón rojo "Cancelar Generación" (por si acaso)

Sistema de detección:

1. Suscripción realtime a la base de datos para detectar cambios instantáneos

2. Polling cada 3 segundos como respaldo para verificar si el video está listo

---

WEBHOOK RESPONSE - ENDPOINT:

Crear un Edge Function en:

https://[tu-proyecto].supabase.co/functions/v1/video-webhook

Que reciba esta estructura cuando Make termine de procesar:

{

  "video_id": "uuid-del-video",

  "status": "completed",

  "video_url": "url-para-visualizar",

  "download_url": "url-para-descargar",

  "thumbnail_url": "url-del-thumbnail-opcional"

}

---

PANTALLA DE VIDEO COMPLETADO:

Diseño de dos columnas:

LADO IZQUIERDO:

- Reproductor de video integrado

  * Si es Google Drive: usar iframe con formato /preview

  * Si es link directo: usar <video> tag HTML5 con controles nativos

- Nombre del producto debajo

- Descripción del producto

LADO DERECHO:

- Ícono de confirmación verde grande

- Título: "¡Video Generado!"

- Sección destacada "Link de Descarga" con emoji 🎬

- Link del video en recuadro verde con borde, clickeable y copiable

- Botones de acción:

  * "Abrir Video" (verde - abre video_url en nueva pestaña)

  * "Descargar" (azul - descarga usando download_url)

  * "Generar Otro Video" (violeta - vuelve al formulario)

---

GALERÍA DE VIDEOS GENERADOS:

Debajo del formulario, mostrar cuadrícula de videos previos.

Cada tarjeta incluye:

- Miniatura del video (thumbnail_url)

- Nombre del producto

- Estado: "Completado" o "En Progreso"

- Fecha y hora de creación

- Botones: "Descargar", "Abrir", "Eliminar"

Diseño: tarjetas color #1C1C1E, texto blanco, acentos violetas.

---

BASE DE DATOS (Supabase/Bolt Database):

Tabla: generated_videos

Campos:

- id (uuid, primary key)

- product_name (text)

- product_image (text, url)

- description (text)

- additional_information (text, nullable)

- status (text: 'in_progress' | 'completed')

- video_url (text, nullable) → para visualizar

- download_url (text, nullable) → para descargar

- thumbnail_url (text, nullable)

- created_at (timestamp)

Configurar:

- Row Level Security policies para acceso público

- Realtime subscription habilitada

- Edge Function para recibir webhooks sin autenticación JWT

---

ESTILO VISUAL COMPLETO:

Colores:

- Fondo principal: #0F0F11

- Campos/tarjetas: #1C1C1E

- Bordes: #2E2E33

- Texto: #FFFFFF (blanco)

- Acentos principales: #7C4DFF (violeta)

- Acento secundario: verde para confirmaciones

- Acento terciario: azul para acciones secundarias

- Cancelar/eliminar: rojo

Efectos:

- Bordes redondeados en todos los elementos

- Padding amplio y diseño aireado

- Transiciones suaves (0.3s) en hover

- Sombras sutiles en tarjetas

- Animaciones de loading fluidas

---

FLUJO COMPLETO DE USUARIO:

1. Usuario completa formulario → Click "Generar Video"

2. Se crea registro en BD con status: 'in_progress'

3. Se envía data al webhook de Make con status: "create"

4. Aparece pantalla de carga con spinner y botón cancelar

5. Sistema verifica cada 3 segundos + realtime subscription

6. Cuando Make responde con status: "completed":

   - Se actualiza BD con video_url y download_url

   - Sistema detecta el cambio automáticamente

   - Muestra pantalla de video completado

7. Usuario ve el video, puede descargarlo o abrirlo

8. Click "Generar Otro Video" → vuelve al formulario

9. Videos anteriores aparecen en la galería abajo

---

TECNOLOGÍAS:

- React + TypeScript + Vite

- Supabase/Bolt Database (PostgreSQL + Realtime)

- Supabase Edge Functions (Deno)

- Tailwind CSS para estilos

- Detección automática de tipo de video (Drive vs directo)

---

IMPORTANTE - DETALLES TÉCNICOS:

1. El video_url es para visualización (puede ser iframe de Drive o video directo)

2. El download_url es específicamente para descargar (webContentLink de Google Drive)

3. Convertir automáticamente links de Google Drive:

   - De: https://drive.google.com/uc?id=XXX&export=download

   - A: https://drive.google.com/file/d/XXX/preview

4. Implementar doble sistema de detección:

   - Realtime subscription para cambios instantáneos

   - Polling cada 3 segundos como respaldo

5. Link de descarga debe mostrarse destacado en recuadro verde con emoji 🎬

6. Todos los textos de la interfaz deben estar en español

```

---

# 🎥 Prompt de Sora (UGC)

```
Rol:

Eres un creador de videos UGC especializado en producir anuncios cortos y auténticos que se sientan como reseñas reales de usuarios.

Tarea:

Una persona sentada en una habitación acogedora sostiene el producto (de la imagen).

Nombre del producto: {{2.product_name}}.

Descripción del producto: {{2.description}}

Habla directamente a la cámara con tono natural, como si realmente usara el producto.

Sonríe, muestra el producto cerca de la cámara y comenta lo útil y estiloso que es.

Luz natural, estilo de video grabado con el celular en mano, duración aproximada de 10 segundos, con vibra de anuncio UGC realista.

Idioma: Español (neutral, natural y cotidiano).

Info adicional: {{2.additional_information}}

```

---

# 🚀 ¿Por qué esta automatización es tan poderosa?

Porque te permite:

- Crear UGC sin grabar nada
- Generar decenas o cientos de variaciones en minutos
- Venderlo como servicio a clientes
- Montar una **mini SaaS** con un MVP real
- Ahorrar costos gigantes en producción
- Testear ángulos creativos de manera rápida y barata

Esto es velocidad, volumen y escalabilidad.  
  
Justo lo que piden hoy las campañas.  
  
#Recuerda que puedes descargar la plantilla aquí abajo.

## 🎙️ Transcripción

Esta automatización que estás viendo en pantalla es una brutalidad. El contenido UGC o el user generated content clarísima. Estamos viendo a las marcas más grandes cada vez apalancarse más en el contenido que es creado por los mismos usuarios de los productos en específico. Esta automatización que estás viendo en pantalla literalmente se encarga de eso. Para el final de este video vas a ser capaz de replicarla y armarla completamente por tu cuenta. Oigan, miren esto. Es mi Kindle y de verdad estoy encantado. Es superligero, la batería me dura semanas y aquí tengo todos mis libros, se ve elegante, cabe en cualquier bolso. Este es mi Kindle y de verdad me tiene encantada. Es superligero, la batería dura un montón y puedo llevar todos mis libros conmigo sin llenar la mochila. Además, se ve elegante y funciona. Es realmente una brutalidad. Y déjame mostrarte rápidamente cómo funciona. Construimos una interfaz que también te voy a dar el prom para que lo hagas, que es esta de acá. La construimos en Bolt. Simplemente le pedimos el nombre del producto, la imagen del producto, la descripción y cualquier información adicional que queramos. y se va a desencadenar esta automatización detrás, que vendría siendo un llamado en específico, después mandándole una señal a Sora, el modelo de Open AI de generación de video y después devolviendo esa imagen. Veamos cómo se vería, ¿no? Es que esto es realmente genial. Entonces, mira, vamos a asumir que tenemos esta imagen en específico. Okay, vamos a copiar la imagen de la lata y nos vamos a ir acá a nuestra interfaz. Voy a pegar la imagen del producto y le voy a poner lata liquid test. Vamos a describirlo y vamos a ponerle esto es una lata de agua. Información adicional. ¿Okay? Y le vamos a dar a generar video. Vamos a correr la automatización para mostrarte cómo funcionaría antes de mostrarte el paso a paso. Nuevamente toda esta interfaz la creamos solamente con un prompt que también te lo voy a entregar. Okay, como podemos ver, recibió el webhook, está creando el video ID en específico, está extrayendo la imagen que le acabamos de dar y la está pasando al formato que necesitamos. Después lo que está haciendo es creando el video con Sora 2 en específico. Se creó el video, luego se subió al Drive y se está pasando a MP4 y nos creó directamente el video acá. Y si es que lo abrimos se vería algo así. Este es mi nuevo crush de hidratación, Liquid Death. Sí, es agua, pero viene en esta lata que parece de cerveza. Y bueno, como esto podemos crear literalmente la cantidad que queramos. Por ejemplo, aquí simplemente le subí esta imagen de el Kindle y me creó este video. Oigan, miren, esto, es mi Kindle y de verdad estoy encantado. Es superligero, la batería me dura semanas y aquí tengo todos mis libros, se ve elegante, cabe en cualquier bolso. Oigan, miren esto. Es el nuevo libro de Alex Ormosi. Se llama 100. Money Models. Llevo dos días leyéndolo y ya me ha dado un par de ideas buenísimas para mi negocio. Además, vieron lo bonito que está. o incluso este que le subió una foto distorsionada de un libro y me creó este review en específico. Oigan, miren, lo que me acaba de llegar, es el nuevo libro de Alex Ormosi. Se llama 100M Money Models. Lo empecé ayer y ya me tiene lleno de ideas para hacer dinero. Así lo podemos hacer con literalmente lo que nos imaginemos. ¿Okay? Y ahora te voy a mostrar literalmente todo todo el paso a paso para que tú también puedas hacerlo. Pero recuerda que si estás en la comunidad de Imperio Digital, puedes descargar exactamente esta plantilla para que no tengas que armar todo desde cero. Recuerda que puedes irte acá, irte al Classroom, apretar en automatizaciones, bajar, bajar, bajar, buscar la automatización que estamos buscando, que es esta, darle clic acá, darle a descargar y crear un nuevo escenario, darle a importar, elegir el archivo, guardar y vo, ya tienes la automatización lista para usar. Simplemente tienes que reemplazarle un par de variables, que sería el webhook que aparece acá, y conectar tu cuenta de Google, absolutamente nada más. Ah, y bueno, también la cuenta es HRGPT, pero en fin, ahora sí vamos a armar todo el sistema paso a paso. Es importante que entiendas que este sistema consta de dos partes. Primero, la automatización que está en el backend, que es la automatización de make, que estás viendo justamente acá. Y segundo, tienes la interfaz, que es la cual estoy interactuando en que vendría siendo esta de acá. ¿Okay? Esto lo creamos en una plataforma que se llama Bolt New. Alternativamente puedes usar lovable, puedes usar V0, cualquiera que sea con vibe coding o Vipompting para armar este tipo de interfaces va a funcionar bien. Lo personal a mí me gusta Bolt new porque me acostumbré, pero lo también te debería funcionar bien. Entonces, lo primero que vamos a hacer es vamos a crear un nuevo escenario en make.com. Vamos a irnos aquí al escenario y vamos a darle a crear escenario. Una vez que estemos acá va a empezar la magia. Previamente vimos que necesitábamos recibir el webhook para luego extraer la imagen que recibimos, pasarlo al formato que necesitábamos, crear o mandar a crear el video, subirlo al drive y luego convertirlo a MP4 para devolver la información, ¿correcto? Esto lo vamos a armar paso a paso para que entiendas cómo lo podemos ir haciendo. Un webhook es un disparador instantáneo y lo que va a hacer esto es recibir que desde la plataforma de Volt le mandamos una señal al webhook para desencadenar la automatización. ¿Okay? Así que aquí nos vamos a ir a custom webhook, es un trigger instantáneo y le vamos a dar a crear. El nombre del webhook va a ser UGC Webhook versión 2. Lo voy a poner y le vamos a dar a guardar. Y lo que va a estar haciendo esto directamente va a ser recibir la información. Este es el webhook. Y le voy a cambiar acá el nombre porque este va a ser recibir información. ¿Okay? ¿Cómo verificamos si esto está funcionando? Vamos a darle acá, vamos a abrirlo y vamos a apretar el link directamente. Y si es que se ejecuta el escenario, una vez que lo recibimos aquí es que está funcionando correctamente. Okay. Y esta va a ser entonces la versión 3 del contenido UGC. Esto es importante porque puedes armar esto y transformarlo en una SAS. O sea, tú puedes llegar a las empresas y decirle, "Okay, mira, te voy a generar UGC específicamente para tus productos", ¿verdad? Quizás no tiene la mejor fidelidad en términos de cómo es el producto, porque lo estamos haciendo solo con una imagen, pero es bastante bastante buena. Si quisiéramos llevarlo a otro nivel, probablemente entrenaríamos un Lora para sacar las imágenes en específico, pero esto funciona increíble. Yo estoy realmente impactado. Entonces, recibimos la información y necesitamos agregarlo a un Google Sheets en específico. Para eso creé este Google Sheets que está acá, que tiene el video ID, el video uno y el video 2 o video ID. Y esto va a ser al final el URL y el video 2, que van a ser los dos URL en específico. Vamos a irnos acá y vamos a apretar el más y vamos a irnos a Google Sheets. ¿Qué es lo que queremos hacer? Queremos agregar un nuevo row y queremos agregar una nueva fila. Entonces vamos a buscar acá el add new o el add a row en específico. Vamos a elegir spreadshe ID que elegimos. Vamos a conectar previamente nuestra cuenta de Google si es que no lo hemos hecho y vamos a buscar cuál es el sheets en específico que estamos armando. [música] Para este caso es el versión 2 UGC contenido, que es este sheets que acabamos de crear acá. Vamos a irnos al sheet name. Vamos a poner sheet name 1 y vamos a reemplazar con las variables que queremos. Aquí tenemos que poner la información del webhook que recibimos. Aquí tenemos que empezar a poner los links, pero el vídeo ID todavía no lo tenemos. Entonces, lo que vamos a hacer es vamos a dejar un place holder o vamos a dejar algo para saber que después tenemos que rellenar ese algo acá y le vamos a dar a guardar y guardar. Entonces, acá va a ser trackar video. Okay, ya tenemos lo primero armado. Mandamos el webhook o mandamos la señal en específico para desencadenar la automatización. Pero, ¿cómo sabemos específicamente qué es lo que queremos mandar? Bueno, necesitamos entrar a Bolt New y promptear la interfaz que vimos previamente. ¿Recuerdas que acá creamos que tenemos el nombre del producto, la imagen del producto, la descripción y la información adicional? Bueno, necesitamos mandar esos cuatro parámetros a volt. Entonces, entraríamos a Volt y le diríamos, "Créame una interfaz que mande cuatro variables como data estructurada al siguiente webhook, ¿verdad? Y el webhook lo ponemos acá, recibir información. Copiamos el webhook y lo pegamos acá. La plataforma va o la aplicación, el rol es que mande un formulario y después se devuelva y se visualice la imagen, etcétera. Todo eso lo tenemos que promptear directamente para tu facilidad. Hice este prompt acá, también te lo dejé en Imperio que puedes llegar, copiar y pegar. Lo único que tienes que reemplazar es el webhook. Pero aquí tenemos crea una aplicación llamada UGC Imperial, etcétera. Tenemos hasta los tonos. paréntesis, todo este prom lo armé con charpt. Ya. Entonces, nos vamos a ir acá y vamos a pegar todo esto. La única cosa que tenemos que cambiar en este flujo va a ser el webhook. Entonces, el webhook al que queremos mandar la información va a ser reemplazado justo acá. Esta app te permite crear videos UGC y vamos a reemplazar este por nuestro nuevo webhook, que vendría siendo este de acá. Okay, ahí sí. http hookmake rpi. Verificamos. HTTP Hookmake RPI. Perfecto. Y ahora vamos a darle a construir y vamos a dejar que Bolt haga su magia y ejecute la interfaz. Y después de unos momentos podemos ver que ya nos creó la interfaz. Tenemos aquí el create database, el babase, el video completion screen con el reproductor entre medio Everything Works. Eso es lo que vamos a ver. Y ahora debería estar cargando y no sé por qué no está apareciendo. Voy a ponerle no visualizo nada. Vamos a darle. Okay. Y ahora sí le pusimos no visualizo nada, literalmente después del prompt y me creó la bolt Database. Okay, aquí tenemos todo imperial. Literalmente tenemos ya todo lo que necesitamos. Entonces acá, por ejemplo, si es que yo le pongo nombre, le pongo link, le pongo descripción y le pongo info adicional y le ponemos a generar video. Vamos a vamos a irnos antes, vamos a guardar y vamos a correr la automatización. una vez para recibir la información y le pongo generar video, mandar un URL link.com. Ahí sí me agregó hasta el filtro generando tu video. Vamos a ver que recibimos directamente la información acá en el webhook. ¿Qué es lo que recibimos? El video ID, el product name, el product image, la descripción y la información en estado de crear. Brutal. Ahora hagamos la automatización que está detrás. Aquí lo que necesitamos hacer es empezar a trackar los videos en específico. Entonces, acá en el video, a, ¿qué es lo que vamos a poner? Bueno, el video ID, exactamente, que vendría siendo este ID en específico para cada generación. Después tenemos que recibir la imagen, ¿verdad? Porque aquí vamos a mandar una imagen en específico. Bueno, este le voy a dar a cancelar generación porque ya no sirve. Eh, mandar una imagen en específico, pero lo que tenemos que hacer después es descargar esa imagen y pasarla en formato que sí podamos trabajar acá. Para ello vamos a irnos acá al más, vamos a poner http y vamos a darle a get a [música] file, que es downloads a file from a given URL. El URL que queremos descargar en este caso vendría siendo no ese sino el product image. Vamos a darle a guardar y esto lo que va a hacer es un módulo HTTP que va a descargar la imagen y tenerla en un formato que queremos trabajar. Ahora las imágenes se van a presentar en muchos formatos distintos, ya tanto en tamaño como en JPG, PNG, etcétera. Entonces vamos a usar un módulo de make que es el image. Vamos a partir, tenemos que usar el resize y el convert. Vamos a partir con el resize y vamos a pasarlo al formato que queremos. Si queremos vertical, lo vamos a hacer en 10280 por 680. Y si queremos en horizontal, lo vamos a hacer, no sé, en 1020 por 1080, dependiendo de tus intereses. Para este caso, lo que queremos hacer es trabajar con Sora. Entonces, déjame revisar rápido cuáles son las proporciones de Sora que nos permite trabajar. Esto no es necesario que lo hagan ahora. Open AI, generate a video. Acá elegimos el modelo. Para este caso voy a elegir el Sora 2, da igual, Sora 2 Pro. y quiero ver las resoluciones con las que trabajamos. Entonces, bueno, ahí está. Tenemos estas dos opciones, 720 * 10280 o 1280 * 720. Si es que lo quiero en vertical va a ser 720 * 10280, ¿verdad? Entonces acá vamos a hacer, quiero cambiar las dimensiones de mi imagen a y ya en específico 720 * 1080, ¿verdad? 720 de ancho por 1280 de largo de alto, perdón. Vamos a darle a guardar y después queremos cambiar el formato. Vamos a usar nuevamente el image y le vamos a poner el converta format de la imagen. La queremos trabajar en PNG porque podemos recibir de todo. Entonces aquí va a ser cambiar tamaño y aquí va a ser cambiar formato de la imagen. Genial. Y ahora que la tenemos en un formato que sí nos acomoda a trabajar, podemos llamar a el modelo de Sora en específico. Vamos a irnos a Open AI, vamos a apretar acá y vamos a buscar el generate a Vídeo. Si es que no has conectado a tu cuenta de Open AI, puedes ir aquí a donde sale agregar, entrar a platform. Openai API keys, pegar la API ke y vas a poder usar el modelo de Sora. Okay, prompt. Necesito que me generes un video UGC del siguiente producto, ¿verdad? Eres un experto en UGC y así, pero podemos empezar. ¿Qué producto en específico? Bueno, el nombre del producto. ¿Cuál es la descripción del producto? La descripción. Okay, esto también. Recuerden que el prompt lo pueden ir refinando para fines prácticos. Voy a copiar el que ya creé, que es este. Eres un creador de videos UGC especializado, el nombre del producto, habla directamente a la cámara, etcétera. De hecho, también voy a aprovechar de dejárselos aquí publicados en Imperio para que puedan usarlo. Esto vendría siendo acá. Se los voy a dejar acá, perdón. Ahí sí. Y se los voy a guardar. Perfecto. Y vamos a usar este mismo prompt. Okay. Prompt. Eres un creador de videos UGC, user generated content especializado en producir anuncios curtos y auténticos. Una persona sentada en una habitación acoger sostiene el producto de la imagen. Nombre del producto. Bueno, la variable que recibimos. Nombre. La descripción del producto es la descripción. Info adicional. Información adicional. Perfecto. Vamos a darle a guardar. Ah, bueno, esta parte también es importante. Tenemos dos modelos acá, Sora 2 y Sora 2 Pro. El Solora 2 Pro es más caro y es más lento. El Solora 2 funciona bastante bien. El único problema que tengo con el Sora 2, con esta automatización en específico, es que a veces se demora tanto que no hacemos un sistema de verificación como, okay, esperar a que se termine de generar, sino que espero que se termine dentro de esta automatización. Es un pequeño detalle técnico, pero si quisiéramos mejorar esto más, te voy a mostrar al final del video cómo podemos hacerlo. Okay, vamos a generar el video de 4 segundos para que sea más rápido. Después lo podemos cambiar a ocho 4 segundos con esta imagen en específico y esperar a que el video se genere. Sí. Okay, vamos a usar el sola dos y vamos a guardar. Esto va a ser acá generar video. Okay, hasta ahí verifiquemos que todo está funcionando. Vamos a darle a correr una vez y vamos a volver a mandar información. Aquí tengo una serie de imágenes, por ejemplo, ya aquí saqué un tablet online, una imagen de un tablet chino que vendría siendo esta. Y vamos a abrir la imagen y vamos a copiar la imagen. Vamos a entrar a Volt y le vamos a poner acá puede ser un Amazon Kindle, ¿ya? O no sé, para que no se seque va a ser un tablet que le permite al usuario leer, ¿verdad? Información adicional. A ver si queremos meter algo más en el prompt. Vamos a correr la automatización esta de acá y vamos a generar el video. Generando tu video. Perfecto. Se descargó la imagen, se cambió el tamaño de la imagen, se cambió el formato y se va a generar el video. Todavía no se va a visualizar nada acá porque no hemos devuelto una respuesta. Tenemos el webhook trigger que recibe una respuesta, se desencadena toda la automatización, así porque lo están viendo al revés, se desencadena toda la automatización y al final esperamos un Webhook response o un get, un http get, que en español significa queremos saber que terminó la automatización, queremos saber que se terminó de ejecutar y que me devuelva información. ¿Qué información me va a devolver? La información que voy a visualizar acá en el video. Y después de unos minutos podemos ver que ya está creado. Vamos a verlo acá. Vamos a irnos al video en específico, video ID y ya lo creamos. Rol, ¿verdad? El nombre de producto, tablet para leer, etcétera. Y ahora tenemos toda esta data de video que no podemos hacer nada con. ¿Por qué? Porque en este formato no lo podemos trabajar. Y aquí lo podemos trabajar de muchas formas. Podemos descargar directamente la imagen, pero en este caso quiero subirlo a un drive porque me gusta centralizar mis imágenes en algún lugar. Entonces vamos a apretar el más, vamos a buscar drive y vamos a buscar el upload a file. Esto va a ser subir un archivo. ¿Dónde lo vamos a subir? A esta cuenta. ¿A qué carpeta elijamos? De la cuenta. New folder. Vamos a poner vencord school. Da igual. ¿Y qué es lo que vamos a subir? Bueno, el archivo que acabamos de generar con Sora. Vamos a darle a guardar. Y esto es subir al drive. El siguiente paso va a ser descargarlo o conseguir un link compartible para que todos puedan tener acceso a eso, porque a veces cuando subimos las cosas al Drive no son necesariamente públicas. Nuevamente Google Drive, había uno que era como Sharlink, get a share link. Sí, efectivamente. ¿Y de qué queremos el share link? Bueno, del File ID o el archivo que acabamos de subir. Vamos a bajar y vamos a darle a guardar. El email address no tenemos que poner nada. Ah, me lo pide porque en tipo tiene que ser anyone para que cualquier persona con el link al final pueda trabajar. Ahí sí. Entonces, File ID, ponemos este que está acá, tipo anyone, guardar. Y esto va a ser link compartible, así de simple. Okay, tenemos el link para descargar, tenemos el link para subir. Ahora lo que necesitamos hacer es pasarlo a MP4 porque quiero poder visualizarlo. Para eso vamos a usar esta parte, es opcional, a mí me gusta. Vamos a usar una herramienta que se llama cloud convert para pasarlo de este formato en específico a MP4 paréntesis. Aquí lo que podemos hacer también si es que te gusta es actualizar el row, ¿verdad? Que va a ser como eh eh update a row en específico. Eh, ¿qué queremos hacer? Poner que el video ya fue creado, no todavía subido, pero sí creado. Entonces, iremos a nuestro spreadshet idico de acá. Sheet name, row number, bueno, el mismo que acabamos de crear, que sería este de acá. Y vamos a actualizar acá el video uno, que vamos a poner el link que es compartible. Okay, ese link deberíamos encontrarlo, si no me equivoco, acá el link. Okay, vamos a guardarlo y esto va a ser actualizar sheet. Perfecto. Ahora sí vamos a convertirlo en un formato que nos guste. Voy a usar cloud convert, ¿verdad? y voy a darle a convert key. Simplemente entra a cloud convertale API Key y creo que tienes como o $10 gratis. El input file va a ser el input de el file que acabamos de conseguir, que es el web content link, que file from URL. Y vamos a buscar acá web content link. ¿Qué formato es? Bueno, no sé que me va a llegar, pero quiero que me lo pase a MP4 file name, ¿cómo se va a llamar? mismo ID o no va a llamarse el videoid.mp4 por ponerle algún nombre. Okay, guardar y esto va a convertir el video. Y finalmente lo que queremos hacer es devolver el video. Para ello vamos a hacer un http. Vamos a poner un makeup request y aquí dentro del maker request puede sonar terrorífico, pero realmente no lo es. Prácticamente el único módulo que vas a usar es el file y el request. El maker request tiene dos opciones, que es el get o el post. Generalmente, generalmente, no siempre, pero generalmente, el get es para traer información y el post es para mandar información. Nosotros queremos mandar información. Ahora, ¿a dónde queremos mandarla? A nuestra interfaz que está justamente acá. Entonces, aquí le voy a decir ahora quiero mandar información de vuelta a través de un make a request o a través de un post request. Dame el link para mandarla a Aquí probablemente te va a mandar un link de la database porque por mientras que carga esto, Bolt lo que hace es tiene muchas integraciones, entre ellas tiene las bases de datos como suabase, si no me equivoco es la que usa acá. Esta base de datos lo que tenemos que hacer es registrarlo en algún lugar porque después necesitamos tener memoria de lo que se ha estado generando, ¿verdad? Aquí no se ha generado nada porque todavía no sabe nada que ha recibido de vuelta. Entonces, el post, el suabase que vamos a mandar es este de acá y lo que tenemos que mandar es esto. Entonces, vamos a irnos acá, vamos a copiar, vamos a a URL y vamos a pegar este video. ¿Qué vamos a hacer? Post, que es lo que vamos a mandar, un row Jason en específico. ¿Por qué Jason? Porque esto es lo que nos pidió, formato del post request este Jason. Vamos a copiar este Jason ahora y nos vamos a ir acá al request content y lo vamos a pegar. Y aquí empezamos a reemplazar. Video ID. Bueno, ¿cuál es el video ID? este que acabamos de generar acá, el status vamos a devolver completed. El URL va a ser el URL que acabamos de crear en Cloud Convert, que es el temporary URL de acá. Y el download URL va a ser el que hicimos acá de Drive, que vendría siendo el web content link de acá y el thumbnail URL. Esto es opcional, pero creo que siempre le le da un toque, ¿verdad? Vamos a ponerle el product image. Vamos a guardar. Y esto lo que va a hacer es devolver un HTTP. Okay, vamos a guardar. Vamos a darle a correr. Veamos cómo funciona. Si es que funciona, sería genial. Sería genial si funciona la primera. Y vamos a hacer la prueba con Okay, este mismo tablet. Tenemos el link de la imagen. Copy image address. Vamos a entrar acá. Imagen del producto. ¿Dónde quedó esto? Bueno, Amazon Kindle. Descripción, un tablet para leer, información adicional y vamos a generar el video. Estamos generando el video. Debimos haber recibido esto acá. Me gusta porque es como una carrera de caballo. Y arranca el webhook, se pone a trackar el video. El HTTP descarga la imagen y cambia el tamaño. Cambia el formato porque no nos va a aceptar cualquier formato y necesitamos PNG. Eh, solo está generando los videos, está consumiendo tokens en específico para generar los videos. Hay un hay un video muy bueno de los N8N Builders, no sé si lo han visto, que es este de acá. Por mientras que carga esto, que es genial, que genial que se llama en en Arena. Justamente acá. Es genial. Genial, porque lo que hacen esto es como justamente tenéis una persona que está narrando así como te ponen un desafío y tenía dos personas intentando de resolver las automatizaciones. Es lo más ñoño que existe en el planeta, pero es increíble. Recomendadísimo ese video. Y aquí podemos ver los pasos que se acaban de completar. Bueno, aquí tuvimos un error, pero verifiquemos que el resto está funcionando bien y después diagnosticamos este error en específico. Okay, link compartible, subir al drive. Vamos a ver, vamos a buscar el link compartible, que es este de acá, el web content link. Vamos a abrirlo y veamos qué es lo que pasa. Nos da descargar el video y si abrimos el video, miren, esto es mi Kner, es superligero, la batería dura días y ya perfecto, funciona. Entonces, hasta acá está todo increíble. El único problema está en cuando estamos devolviendo el request http que nos dijo IP address not valid. Esto vendría siendo el IP address que acabamos de llamar, que es este que aparece arriba. Entonces, si es que ahora vuelvo, voy a copiar este error, voy a volver a volt y voy a decirle make en el fondo me tiró un error que va a ser el IP address. ¿Por qué? Porque intentamos de copiar este IP address en específico que es este, pero al parecer no lo está recibiendo. Será porque quizás no está creado en el B Database, en el Supase en específico, este link que está acá o quizás es algún error en cómo lo entregó. Verifiquemos. Ahora vamos a volver a copiar esto. Vamos a verificar si es que está bien. Parece que era un error de autentificación o autenticación. Lo vamos a pegar. No cambió nada. Y vamos a darle a guardar. Intentemos de ejecutar solamente este módulo. A a a. Y vamos a mandar un link en específico. Y bueno, copiamos acá el error, lo pegamos acá y después me reconoció justamente, mira, e le pedimos el link, probamos el link, me dijo, "No, y ahora me reconoció, mira, déjame verificar la URL." Ah, ahí está el problema. Te di la URL incorrecta. Entonces, ahora volvamos acá, copiemos esto y peguémoslo. Ahora sí vamos a darle a guardar y verifiquemos si es que esto funciona esta vez. Vamos a correr este módulo a a link link. Verifiquemos que esto funciona. Y ahora sí me debería quizás mandar un error 500, pero ya sabemos que se está ejecutando. Verifiquemos si es que esto funciona o no. Efectivamente, error 500 internal server error está funcionando. ¿Por qué no estoy el error? Porque como no llamamos a ningún video en específico, no logró reconocerlo, pero cuando se desencadee en el flujo debería funcionar. Okay, verifiquemos que esto funciona. Ahora sí que sí, eh, vamos a guardar esto. Vamos a correrlo y ejecutarlo una vez más nuevamente. Vamos a volver a rellenar todo y le vamos a poner acá Amazon Kindle. Vamos a ponerle el esto. Copiar image. Pegar la imagen, tablet para leer, información adicional. Ahí podríamos ponerle lo que queramos, o sea, algo oscuro, o sea, como o la persona tiene que estar muy emocionada. Es como una ventanita para poder tear un poco más como en lo que estás buscando en específico. Y ahora sí debería completarse esto que está acá. Se generó el video. Ahora se está convirtiendo el video. Seguimos convirtiendo el video y efectivamente se devolvió de manera completa el request acá. Ahora si es que vemos acá nos va a salir completado y que podemos descargarlo directamente. ¿Por qué? Porque esto se va a quedar cargando todo el rato hasta que no reciba este request de vuelta. Después podemos seguir promteando para santa un poco más de tiempo antes de hacer el time out y haz una revisión periódica si recibiste algo al URL de vuelta. Hazla cada 5 segundos, algo así. Y aquí le vamos a poner enter. Y quiero que se visualice una vez que termine de cargar la generación. Ah, bueno, no me había dado cuenta, pero ya estaba funcionando eso y aquí tengo para descargarlo directamente. No me había dado cuenta, pero ya estaba funcionando y le promé para hacer literalmente lo que ya estaba haciendo. Así que voy a cancelar el mensaje. Eh, podemos abrir este, podemos ver el video, podemos encontrarlo acá. Okay, ahora recordemos que lo está generando de 4 segundos. Si es que quiero abrir el video, lo abrimos ahí. Si es que quiero descargarlo, ¿verdad? Aparece acá. Y si es que quiero generar otro video, vuelvo al inicio. Realmente increíble. Y así de simple creamos una aplicación. Ahora, si quisiera hacer esto un poquito más largo, iría acá a la parte de Sora, me iría los segundos, me iría los 8 segundos, le daría guardar y lo dejaría corriendo. Esto lo dejaría así y lo dejaría prendido para que cada vez que se ejecute esto pase. Lo que voy a hacer es nuevamente ir acá. Voy a exportar esta plantilla en específico. Voy a irme acá y te la voy a subir a Imperio Digital para que la puedas llegar eh implementar. Y vamos a reemplazar esta de acá porque esta tiene un poquito más de notas. Creo que está buena. Agregar file en específico y es la versión 3. Le voy a poner plantilla UGC automatización make. Vamos a guardarlo. Y listo. Así de simple ya está funcionando. ¿Recuerdas que antes te dije que podías llegar a un máximo tiempo de time out? Bueno, eso también tiene una solución. Ahora, yo estuve probando con el modelo Sora 2, funciona bien, pero si es que quiero hacerlo de 12 segundos y quiero usar el Sora 2 Pro, se me va a demorar mucho tiempo y si es que hay un módulo de make que está ejecutándose por más de 5 minutos, se va a pausar. Entonces, no queremos que eso pase. La alternativa que te recomiendo es separar esto en dos escenarios. ¿Okay? Esto lo vamos a separar acá. Mira, escenario número uno, escenario número dos. Esto funcionaría así. le cambiarías acá en el generar video, bajarías y le dirías, "Espera que el video sea generado." Y le pones "No." Y en otro escenario, que esto lo copias y lo pegas en otro escenario, puedes irte acá al Open AI, te vas al watch Video jobs y le pones el límite de videos en específico. Por ejemplo, uno desde, no tengo idea, manually y podemos hacer cualquiera, no sé, desde el penúltimo video que hicimos y lo conectamos acá. ¿Qué va a hacer esto? que si es que tenemos una ejecución de un video que es muy largo alcance a generarse y no se interrumpa. El flujo de automatización es genial, es genial, muy práctico, muy útil, te puede servir mucho si es que quieres llevar esto a otro nivel. En fin, creo que se entiende el punto. Se entiende el punto. ¿Hacia dónde va est? Podría quedarme hablando y mejorando esto muchísimo, muchísimo, porque lo encuentro muy interesante la cantidad de marcas que pueden llegar y pagar por esto y no es algo caro. Ah, yo me acuerdo que estuve probando, por ejemplo, aquí en distintos modelos, si no conoces Replicate, Replicator, una página que te permite probar modelos de inteligencia artificial e además integrarlo en tus automatizaciones, por lo que es realmente genial. Estuve probando hace un tiempo con Beo BO3 y es carísimo, es carísimo. Cada video me acuerdo que me salía alrededor de, no tengo idea, $, algo así, ya. Era muy muy caro. Aquí lo puedo buscar. Veo acá o el 3.1 mejor, pero me acuerdo que era muy caro, muy caro. ¿Dónde está el pricing? Acá. V o 0.2 por output video en este caso, pero como estamos generando con audio es 0.4. Sora lo está generando en 0.1. Es decir, 10 centavos el segundo. Esto si es que llegamos y hacemos unos cálculos rápidos y no me falla mi matemática. Si creamos, no tengo idea. Hoy día, por ejemplo, con los ads, esto está valiendo más que nunca, como sacar cantidad. Y cada video de 12 segundos nos saldría 1.2 si queremos crear, no tengo idea, 100 videos. O sea, imagínate todo lo que te costaría conseguir 100 videos distintos de UGC para un producto o alguien hablando de algo. Aquí lo podemos hacer por 120 y tenemos para probar 100 ángulos distintos en ads, en campañas, en literalmente lo que queramos. Genial, genial. Si quisieras vender este servicio de imágenes, lo que te recomendaría es que hagas un lora o hagas un flux training. Por ahí debería aparecer. Eh, yo tengo entrenado directamente mi modelo de Lora, que lo puedes encontrar acá, que es mi modelo acá. Vencorde, vencorde 3 y cada vez que entro y le pido una imagen mía, me la hace. ¿Por qué? Porque entrené, hizo un low rank adaptation de mi cara. Entonces, todos los videos, todos los thumbnails que veis, todas las cosas las hago directamente con esto, esto que está acá. ¿Por qué? Porque sabe quién es Ben Cordero, man Superman. Yo bajo acá, le ajusto los parámetros, quiero cuatro outputs, le esto, eh, pum, correr y me empieza a generar esto. Lo interesante es que acá, como ves, tenemos el Jason y si tiene Jason es automatizable. Lo mismo si es que tiene HTTP y ajustamos los parámetros acá. Pero creo que me estoy desviando un poco del tema. Lo que quería ir con esto era que podemos hacer entrenamientos, por ejemplo, de productos. Yo este lo entrené con 40 fotos mías, pero podemos hacer un entrenamiento con cinco fotos de un producto en específico y empezar a sacarle campañas y venderle campañas a marcas de los productos según la estacionalidad que están. Por ejemplo, campañas para Halloween, campañas para Año Nuevo, Navidad, etcétera, y las podemos sacar en tiempo récord. Eso fue una de las cosas que vimos ahora en el evento de Tijuana que organizamos los avatars, específicamente los fake avatars o los deep fakes que eran geniales. Y así de simple estamos usando Fluxlora para crear imágenes mías. Genial. Encuentro que me veo bastante guapo. Ah, me hace harta harta harta justicia. Mira ahí el Benja Superman. Así que nada, nada, espero ahí que te sirva. Esta automatización nuevamente te la voy a dejar publicada aquí dentro de Imperio Digital si es que quieres aprender de automatizaciones en comunidad más activa de automatizaciones con inteligencia artificial entre Imperio Digital prueba somos más de 600 miembros es realmente brutal brutal y aquí compartimos todos con una estrategia que tenemos en común o un objetivo que tenemos en común que es ahorrar tiempo con estrategias que funcionan tenemos la sección del Classroom donde puedes llegar a implementar las automatizaciones además de muchos muchos cursos que puedes encontrar acá sesiones en vivo con expertos, con el mismo equipo, soporte y una comunidad que te está acompañando en todo el proceso, o sea, porque quieres automatizar tu empresa, porque quieres crear una SAS en específico en base a una automatización o porque quieres vender automatizaciones como servicio. Ahora sí, sin más que decir, espero que te haya servido esta maravillosa automatización y nos vemos en una próxima.
