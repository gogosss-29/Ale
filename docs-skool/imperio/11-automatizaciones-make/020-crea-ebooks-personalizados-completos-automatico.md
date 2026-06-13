# 📕Crea Ebooks Personalizados Completos Automático

> Ruta: Automatizaciones Make › 📕Crea Ebooks Personalizados Completos Automático

**🎬 Vídeo (37.6 min):** https://youtu.be/nzvG_8xvdlM

**📎 Recursos:**
- Ebooks_Personalizados_Make_Autom

---

Esta automatización conecta la entrada de datos de un **Google Forms** para crear un eBook personalizado de principio a fin. A continuación, te detallo el flujo completo:

1. **Entrada de Google Forms**: El usuario completa un formulario en Google Forms donde proporciona detalles clave como el título del libro, descripción, número de capítulos y nivel de lectura deseado.
2. **Esquema del Libro con OpenAI**: Los datos del formulario se envían al módulo de **OpenAI**, que genera un esquema inicial del eBook basado en la información proporcionada.
3. **Generación de Capítulos por Bucle**: Se activa un bucle en [Make.com](http://Make.com) que, utilizando OpenAI, genera cada capítulo uno por uno. Durante este proceso: - **Almacena el Capítulo**: Cada capítulo generado se guarda temporalmente en una variable.
- **Acumula los Capítulos**: Los capítulos se van agregando a una variable acumulativa, con saltos de línea para mantener la estructura.
4. **Filtro de Finalización**: Un filtro verifica que se hayan generado todos los capítulos solicitados antes de proceder. Esto asegura que la automatización no continúe hasta que todos los capítulos estén listos.
5. **Conversión de Markdown a HTML**: Una vez finalizados todos los capítulos, el contenido acumulado se convierte a HTML para darle la estructura adecuada.
6. **Conversión de HTML a PDF**: El HTML generado se transforma en un PDF profesional listo para ser enviado.
7. **Envío del eBook al Correo Electrónico**: El PDF final se envía automáticamente al correo electrónico que el usuario proporcionó en el formulario, completando así todo el ciclo de la automatización.

**Resultado**: El usuario recibe un eBook personalizado directamente en su bandeja de entrada, basado en la información específica que proporcionó en el formulario inicial.  


---

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/03b5ad26abb74685b25384ee293a36d8ebcde3a6f5c3498fafb5dc521f83507a-md.png)

  
Escribir un libro es una estrategia poderosa para construir autoridad y posicionarte como un experto en cualquier nicho o industria. Además, los eBooks son una excelente herramienta como **lead magnets**, lo que te permite captar leads cualificados de forma efectiva. En esta guía, te mostraré paso a paso cómo configurar una automatización que te permitirá crear un eBook personalizado con solo un clic.

> Nota: Al final de esta guía, podrás descargar un archivo .json con todas las configuraciones y variables pre-cargadas para importar directamente en Make.com. Solo necesitarás dirigirte a la opción "Import Blueprint" en Make.com, subir el archivo .json, ¡y tendrás toda la automatización lista para comenzar a generar tus eBooks personalizados! 

> Además, si quieres saber más sobre cómo utilizar los eBooks como lead magnets, te recomiendo revisar nuestro módulo "**Crea, Conecta, Convierte**" [aquí](https://www.skool.com/imperio-digital/classroom/4fbd6ff6?md=96cb28d1b9a14fea85b1227bd2502119).

**Esta es solo la base:** Desde esta configuración, podrás expandir la automatización para generar audiolibros, videos de YouTube y mucho más. Aprender a configurar esta base es fundamental para dominar formatos más extensos en el futuro y llevar tus habilidades en automatización al siguiente nivel.

---

### **Beneficios de Utilizar eBooks en Tu Estrategia de Negocios**

Existen dos formas principales en las que un eBook puede ayudarte a escalar tu negocio:

1. **Venta en Amazon o Kindle**: Publicar un libro en plataformas como Amazon o Kindle no solo genera ingresos adicionales, sino que también posiciona tu marca como un referente en tu industria. Esto refuerza tu autoridad y te ayuda a destacarte como experto.
2. **Lead Magnet Personalizado**: Ofrecer un eBook como lead magnet es una forma efectiva de captar leads cualificados. Con la tecnología actual, puedes personalizar cada eBook según la información proporcionada por cada lead, haciendo que el contenido sea relevante y atractivo para cada individuo, como lo vimos en [Crea, Conecta & Convierte](https://www.skool.com/imperio-digital/classroom/4fbd6ff6?md=96cb28d1b9a14fea85b1227bd2502119)

Por ejemplo, si eres un entrenador personal, podrías utilizar un formulario para capturar datos como el peso inicial de una persona, su peso objetivo, edad y sus metas específicas (ya sea perder grasa, ganar músculo, o mejorar la resistencia). Con esta información, la automatización generará un eBook único adaptado a las necesidades de cada cliente, lo que no solo añade valor, sino que también mejora la conversión en tu funnel.

### **Paso a Paso: Configuración de la Automatización para Crear eBooks Personalizados**

Vamos a detallar el proceso completo para crear esta automatización utilizando herramientas accesibles para cualquiera en la comunidad de Imperio Digital. Aquí tienes una guía detallada basada en los módulos que se utilizarán en la automatización:

#### **Paso 1: Configuración del Formulario en Google Forms**

El primer paso consiste en crear un formulario que recolecte toda la información necesaria para personalizar el eBook. Aquí puedes personalizar los campos como prefieras, ajustándolos a la información específica que necesitas para cada tipo de lead o cliente. En este caso, para fines prácticos, yo he seleccionado las preguntas que considero más relevantes para crear un plan personalizado.

1. **Accede a Google Forms**: Inicia sesión en tu cuenta de Google y crea un formulario en blanco desde Google Forms. Nombra este formulario como "Automatización eBook".
2. **Campos Necesarios**: Aquí incluye todos los campos que peudas considerar relevantes como variables para lograr una mayor personalizacion, pero asegúrate de incluir estos tres: - **Correo Electrónico** del destinatario para enviar el eBook finalizado.
- **Nombre:** para personalizarlo aun más.
- **Número de Capítulos** que quieren incluir en su eBook.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/01260fd2ce7246db82b0704b7e0e140cfb64a128702145a18025ccd36024e425-md.png)

Estos campos son solo una guía, y puedes ajustarlos según la información que consideres necesaria para personalizar cada eBook en tu caso particular. En este ejemplo, la información está enfocada en crear un **plan personalizado** para generar contenido relevante en un libro adaptado a cada usuario.

#### **Paso 2: Configuración de la Automatización en **[**Make.com**](http://Make.com)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b6400a9cb6f64286b4c157462d2c4edac93a481060c64bc8ac9eb7f126300571-md.png)

Para esta automatización, utilizaremos [**Make.com**](http://Make.com), una herramienta visual para crear flujos de trabajo automatizados:

1. **Crea un Nuevo Escenario**: Inicia sesión en [Make.com](http://Make.com) y crea un nuevo escenario desde cero. Esto te llevará a un lienzo en blanco donde podrás construir tu automatización paso a paso. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6e61c982665746d0aa920b9701edd5d6fc286fa237df402c8ebdf87c3fa02034)
2. **Configura el Disparador con Google Forms**: El primer módulo será Google Forms, configurado para "Watch Responses", lo que permitirá que la automatización se active cada vez que alguien complete el formulario. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c6b7af80f507490e8b00c3aa67034757aa0f0821ecbd4951b7048375209e820c) Busca el titulo que nombraste el formulario con, que le pusimos "Automatización eBook". Ponle el límite a 1, que será el máximo de respuestas que analizará cada vez que se ejecute la automatizacion (1 respuesta es una enviada del formulario, que peude tener muchas respuestas dentro) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7d5e618aa9974a9f8314de75d15e532c01216417da3040f79b741a26200e6689)
3. **Generación del Esquema del Libro con OpenAI**: Usa un módulo de OpenAI para crear un esquema del libro basado en las respuestas del formulario.  Aquí puedes usar "Create a chat completion" donde le pondremos el prompt, o si quieres hacerlo aun mas avanzado, puedes ponerle un "Message an assistant", para poder escribirel a un agente aun mas presonalizado si es que dominas el uso de los agentes o asistentes. Nota: Puedes aprender a usar los agentes en el módulo del classrom "[Agentes](https://www.skool.com/imperio-digital/classroom/a65de4cd?md=b03e9a24881b42f5a8ff85831305db4d)".  Para fines prácticos usaremos "Create a completion" ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/909586ae204043c7a756ccf9ae977258c23c45829556449390acefe9adf994a1-md.png) Configura el módulo para que extraiga información como el título, la descripción, el número de capítulos y el nivel de lectura, generando un esquema único para cada libro, y que termine con un Call to Action de tu servicio principal, para seguir avanzando en el embudo de venta. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/926db1eaacf542638fde57445e6a1bbd7040460e6c2145d49a3e3b7ef920cfe3) Este es el prompt que utilicé:  ```
Por favor, escribe un esquema para un eBook personalizado en base a la siguiente información: Objetivo principal: 
Lo que se quiere lograr: 
Número de días de deporte a la semana:
Tipo de ejercicio frecuente: 
Sexo:
Peso actual (en kg):
Peso ideal (en kg):
Altura:
Edad:
Restricciones alimentarias o preferencias:
Cantidad de capítulos: Al final del libro, incluye una sección bonus a la cantidad de capitulos sobre la posibilidad de obtener una asesoría personalizada para lograr los objetivos específicos de manera más detallada, que venda y ataque directamente los objetivos y presentando una situacion deseada, puede agendar su llamada gratis en www.bencorde.com
```

Aquí reemplazas e integras las variables en cada uno de ellos.

Luego le defines el máximo de tokens a 10.000

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/63e5e7225a5c4498b30a133be8ac2ddd534763440ce3489fad70cae4dd058db5-md.png)

#### **Paso 3: Creación de Capítulos por Medio de Bucles en **[**Make.com**](http://Make.com)

- Ahora, crearemos una variable que usaremos para poder "independizar" cada capítulo. Para esto iremos a un nuevo módulo y buscaremos "Set Variable" ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e71a612700eb4c3ba5b1295c7f2b7b220f94eed5f6074b76bb8ca3ff3b7b6ad0-md.png) Le pondremos el nombre "capitulos acumulativos" ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/94c9332c51f74efeb64b1f0c06cd829d94add0499b9b402e92dc833c11a2afc1)
- **Configura un Ciclo Repetitivo (Repeater)**: Agrega un módulo "Repeater" que te permitirá generar cada capítulo del eBook de manera individual, basándote en el número de capítulos que el usuario especificó en el formulario. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/38d7327291b64cd19bbdffb8d42de7561ecce81f57124d3ba998aff4e7b99328) Ahora que tenemos el repeater, tenemos que decidir cuantas veces se ejecutara. Para esto comenzaremos en 1, y lo haremos el máximo de veces que nos pidio el usuario, es decir, la cantidad de capitulos que nos pidieron. Porque esta secuencia de desatará en bucle la cantidad de veces que le pongamos. Para eso, le pondremos que vaya desde el 1, hasta el [Respuesta de capitulos solicitados], que lo podremos encontrar en la estrellita, bajo numero de capitulos, bajo textAnswers, bajo answers y elegimos Value. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c2ce8c424e004ef78353fe96eba640d88be0259a8658487a9752fb5e3f1e0c2e)
- **Almacena los Capítulos en Variables**: Ya creamos la opcion de "Set Variable", pero lo que haremos ahora es un "Get Variable", es decir usaremos la variable para almacenar el contenido de cada capítulo generado por el OpenAI, asegurándote de que cada capítulo esté bien organizado y listo para ser compilado en el eBook final. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ebb1d94eda034ba6b234a43e021669c166f827e01f84466da4d4dd3fe0b7fdde) Aquí le ESCRIBIREMOS (no eligiremos como variable), sino que escribiremos el mismo nombre de la variable que creamos anteriormente, en este caso, capitulos acumulativos. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c8d7204e8edb4d6a8b484fd4051dee4e858e41e59c1c4dadb4e997f21205a318)
- **Generación de Contenido Capítulo por Capítulo**: Utilizaremos nuevamente el módulo "Create a Completion" de OpenAI para generar el contenido de cada capítulo. Es importante configurar bien el prompt para que la IA produzca contenido coherente y relevante basado en la información recopilada. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1e83158d79d947f7b46cbeef392c63795ca40e17a5dd44008897377463966fb2) Aquí rellenaremos las variables que aparecen acá de la informacion que recolectamos, y nuevamente te dejaré el prompt que utilicé aquí abajito. Además le setearemos el Max Tokens a 10.000

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/92e031eb7ecd40eeaaa0801adbdea8c1110020cb64df4eefb50c9300c18dc590-md.png)

Prompt para capitulos

> Por favor, escribe el capítulo [CAPITULO] del siguiente eBook de fitness en un tono motivador y personalizado:
> 
> Recordemos que el libro personalizado para [NOMBRE] (nombre que usaremos en el contenido)
> 
> Objetivo principal:
> 
> Meta específica:
> 
> Frecuencia semanal diaria de ejercicio:
> 
> Tipo de ejercicio frecuente:  
>   
> Sexo:
> 
> Altura:
> 
> Peso actual kg:
> 
> peso deseado kg:
> 
> Edad:
> 
> Restricciones alimentarias:
> 
> Cantidad de capítulos:
> 
> Por favor, proporciona solo el capítulo como resultado, sin ningún otro comentario, en formato markdown. El título del capítulo debe comenzar con el número de capítulo y la meta principal en H2. El tono de voz debe ser similar al de Dan Koe. Al final del libro, incluye sutilmente una sugerencia para obtener una asesoría personalizada y lograr los objetivos en mayor detalle.  
>   
> Te dejo aqui el outline / esquema del ebook de donde debes sacar los capitulos: [RESULTADO]

- **Almacenar el Contenido del Capítulo en una Variable**: - Agrega un módulo "Set Variable" llamado **Capítulo**. Aquí es donde almacenarás el contenido generado del capítulo actual.  ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4b97aaa7967847eeb4de0b611e5bb7aeeea6cdd151e542a78b2b478db07be9e1) En el campo de "Variable Value", selecciona el contenido de "Message.Content" generado por el OpenAI (lo puedes encontrar bajo estrellita, choices, message, content) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a36679fe007b416ebb391561fa9a2f6f7571eb3290d74da4a3929f94bfc8f1eb)
- **Acumulación de Capítulos**: - Agrega otro módulo "Set Variable" llamado **Capítulos Acumulativos**.  ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3b9f0529bd67430dac95cac7b8021204a4c1e4a3f3e94471a3c277f7d15f1f65) Aquí, conectarás cada capítulo a la variable anterior, agregando un salto de línea (`newline`) entre capítulos para mantener la separación adecuada. Selecciona la variable acumulativa existente (como variable) y el contenido del capítulo generado anteriormente (la que creamos llamada capitulo).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d1ab18dbafa34953b4830c215259c5644c03fb471b5f498f963eeb3a3d81e104)

#### **Paso 4: Conversión del Contenido en un PDF Final**

1. **Markdown a HTML**: Usa un módulo de "Markdown to HTML" para convertir el contenido del libro en formato HTML. Esto es crucial para darle la estructura adecuada antes de convertirlo en PDF. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/fb4c78f728f24e6f9e8d3cdd04db9e563994d8e0640e435695d505aed3634c8a) Aquí le incluiremos "ebook personalizado para: [variable]". Esto será lo que aparecerá en el principio del PDF. Es decir, aquí es donde combinaremos TODOS los capitulos que ya hemos creado en bucle, el 1, 2, 3, y así...

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/15c42309a88d4579b85aed5249ef712e5002682ee0c84c0ba3e537de130e9f7b)

Esta parte es super importante, entre la acumulación de capítulos y la conversión de Markdown a HTML, hay un paso esencial: un filtro que asegura que la automatización se detenga correctamente cuando se hayan generado todos los capítulos solicitados.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2802831b97684d2c9dd4d91215994fa5c83cbc2d1c2d412abf3c93bb37a4249f)

#### **Configuración del Filtro**

1. **Conecta el Filtro**: Después de la acumulación de capítulos, añade un filtro entre "Set Variable" y "Markdown to HTML" (le tienes que hacer clic a la linea punteada) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9598c7c8b9284a2193a0579f10284db6e7811aaff50d4708926ae3ae00d1c2d8-md.png)
2. **Condición del Filtro**: Establece que `i` (el número de la iteración actual en el bucle) debe ser igual al **número de capítulos solicitados** por el usuario. Esto asegura que se han generado todos los capítulos. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2112fce86f294a7396b2fa6b18e2caeee8fc7966b93440d49a6e2ddf95128d8b)
3. **Acción**: Si `i` coincide con el número total de capítulos, la automatización continúa hacia la conversión de Markdown a HTML. Si no, el bucle sigue generando capítulos. En palabras simples, este filtro garantiza que la automatización no pase al siguiente paso hasta que todos los capítulos estén completos, asegurando que cada eBook esté perfectamente estructurado y listo para la conversión.  
 Siguiente paso: convertir el HTML a un PDF.

- **HTML a PDF con **[**PDF.co**](http://PDF.co): Convierte el HTML generado en un archivo PDF profesional utilizando el servicio [PDF.co](http://PDF.co). Este tiene una prueba gratuita de hasta 10.000 créditos (cada generación toma aproximadamente 10-20 créditos, por lo que tenemos para crear MUCHAS). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b987521480e844df8cce505ea0fc2958c659b6c92ea04968937a3b529cdfb574) Asegúrate de configurar bien el documento para que incluya encabezados, capítulos organizados y el formato adecuado. Aquí le pondremos el convert type "HTML to PDF" y en el input HTML le pondremos el siguiente código: > <!DOCTYPE html>
> 
> <html>
> 
> <head>
> 
> </head>
> 
> <body>
> 
> [VARIABLE HTML]
> 
> </body>
> 
> </html> Dándonos algo así: ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2e6f05b0c01c4e0bb2add000e3e7a7488d705afeb99b46159efd0d90b247d5e7-md.png) Nota: Hay que reemplazar la parte que sale [Variable HTML por el HTML que nos dio en el módulo anterior]   
Luego le daremos en las opciones de exportación, "Download a File" ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3db7fd6ce18d410a86f27d493f3ce0ed60dbcf8679c24b5fbfb036a0cfe5be6e)
- **Envío del eBook por Correo Electrónico**: Configura el envío automático del PDF utilizando el módulo de **Microsoft 365 Email (Outlook) ***(Podrías usar Gmail, pero a mi me acomoda más trabajar con Outlook)*. Buscaremos la opción de "Create and send a message". ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d561930d1a5b4703b449e3643f0850cc80f4fe6a2bc94b8189df03f4de741a3f)   
Este módulo enviará el eBook directamente a la dirección de correo especificada por el usuario en el formulario, completando así la automatización. Le rellenaremos en el subject el asunto que queremos que el mail tenga, con esta opción saldría algo como "Benja, aquí tienes tu eBook!" y en el body content le puedes poner lo que quieras también, que sería el cuerpo del email. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6702b124abb04bb69374071c70cab25312db8976a8284be593aeaa76a3fc6023) Luego configuraremos el remitente y el receptor. Para el receptor, incluiremos el mail que nos dieron en el cuesitonario: ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6a6bda2c970947e08346d5aababa6c93c4f4a0bea12a4f8ab8b9a8df75cd2a57) ...y luego esta parte es importante, porque incluiremos los "attachements" o los "adjuntos". Aquí tenemos que seleccionar el archivo "PDF.co" que creamos en el módulo anterior, así nos asewguramos de que se envie. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4356daad853d46919f9899b1ef144218f9aca34237d74ecfb19ae38321f04c50)

Y listo.  
  
Puedes probar la automatización activándola aquí, y rellenando un nuevo cuestionario para ver si funciona. Debería llegarte un PDF completo al email y a tus futuros clientes potenciales.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a8c82a5440214047a631f479c68a83e7f9ae69adb0684f0781daa01444b570aa)

La automatización se debería ver algo así

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/03b5ad26abb74685b25384ee293a36d8ebcde3a6f5c3498fafb5dc521f83507a-md.png)

  
**Paso 4: Escalando la Automatización para Nuevos Formatos**

Esta automatización es solo la base. Desde aquí, podrás crear procesos más avanzados para generar audiolibros, videos educativos para YouTube, y mucho más. Dominar esta configuración inicial te permitirá explorar nuevos formatos y adaptar la automatización para cubrir diferentes necesidades de contenido en el futuro.

### **La Revolución de la IA: GPT-40 Mini y la Reducción de Costos**

La tecnología de IA ha avanzado a pasos agigantados. OpenAI y su modelo **GPT-40 mini**, le permiten escribir entre 4 y 5 millones de caracteres por solo 60 centavos. Esta reducción de costos facilita la creación masiva de contenido de calidad, lo que abre nuevas posibilidades para los emprendedores digitales.

### **Conclusión: **

Implementar esta automatización en tu estrategia es un cambio radical que te permitirá ahorrar tiempo, ofrecer contenido de alto valor y capturar leads de manera efectiva. 

Recuerda que, al final de cada eBook personalizado, puedes incluir una invitación sutil para una **asesoría más detallada**, lo que te permitirá afianzar la relación con tus leads y guiarles hacia sus objetivos de manera más efectiva.

Espero que pongas en práctica esta automatización y observes el impacto positivo en tu negocio. ¡Es momento de aprovechar la tecnología y llevar tu emprendimiento al siguiente nivel!  


**Recuerda que puedes descargar e importar la automatizacion directamente descargando el archivo .json que aparece aquí abajito.**
