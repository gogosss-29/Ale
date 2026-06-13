# Lleva los GPTs al siguiente nivel

> Ruta: Mentalidad IA › Lleva los GPTs al siguiente nivel

**🎬 Vídeo (31.2 min):** https://www.youtube.com/watch?v=t9hgwrzyZg8

---

Supercarga ChatGPT con [Make.com](https://bencorde.com/make): Guía Paso a Paso para Automatizar Tareas desde ChatGPT

En este tutorial, aprenderás a utilizar [Make.com](https://bencorde.com/make) para convertir a ChatGPT en una herramienta potente y automatizada, capaz de realizar tareas como realizar llamadas, extraer datos de documentos, crear tareas, y mucho más.   
  
Sigue esta guía para configurar cada paso de forma detallada, y ve el video de arriba para hacerlo aun más simple

---

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c56f3cba993e4f72851cf6e0342f555199e2324cd24b4ebdb602f3dc370cbda2-md.png)

### Introducción

El objetivo es explicar cómo transformar ChatGPT en un sistema automatizado usando [Make.com,](https://bencorde.com/make) conectándolo a múltiples aplicaciones para realizar tareas automáticas. Este sistema te permitirá, por ejemplo, agendar reuniones y enviar mails, extraer datos de un archivo como una boleta (imagen o PDF) y organizarlos en hojas de cálculo o crear eventos y agregarlos a tu calendar y literalmente lo que te imagines.

---

## Casos de Uso

Para mostrar la versatilidad de ChatGPT y [Make.com,](https://bencorde.com/make) veremos tres casos de uso:

1. Extraer datos de un PDF y añadirlos a una base de datos.
2. Agendar una reunión de meet y enviársela a un mail en específico
3. Agregar eventos en un Google Calendar
4. **Y literalmente casi lo que sea que te imagines posible...**

## Configuración del Sistema

Para que este sistema funcione, necesitas:

1. **ChatGPT Plus**: Para acceder a las funciones avanzadas necesarias para la automatización.
2. [**Make.com**](https://bencorde.com/make): La plataforma de automatización que conectará a ChatGPT con aplicaciones externas.

### Conceptos Básicos de [Make.com](https://bencorde.com/make)

[Make.com](https://bencorde.com/make) permite automatizar flujos de trabajo mediante *triggers* (disparadores) y *actions* (acciones). Un trigger inicia el flujo de trabajo, y la acción es la tarea que se completa. En este caso, el trigger será la orden que envías a ChatGPT y que activa un webhook en [Make.com](https://bencorde.com/make).

---

## En síntesis lo que haremos es

Configurar ChatGPT como un asistente de automatización:

1. **Configurar el ChatGPT Personalizado**: Crea un asistente personal dentro de ChatGPT que pueda seguir tus instrucciones específicas para tareas específicas en Make
2. Crear una (o varias) automatización(es) de Make que serán disparadas desde ChatGPT dentro del mismo GPT personalizado a través de un webhook (si suena complejo, pero es mucho mas simple de lo que crees).

---

## Configuración del Webhook en [Make.com](https://bencorde.com/make)

Un *webhook* permite que [Make.com ](https://bencorde.com/make)reciba información enviada por ChatGPT, lo que desencadena el flujo de trabajo deseado. Este proceso es esencial para que la automatización funcione, ya que cada vez que ChatGPT envíe un comando específico, el webhook capturará esos datos y activará la secuencia de acciones en [Make.com.](https://bencorde.com/make)

### 1. Crear un Nuevo Escenario en[ Make.com](https://bencorde.com/make)

- Inicia sesión en tu cuenta de [Make.com.](https://bencorde.com/make)
- En el menú principal, haz clic en la pestaña **Escenarios**.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5f5af8f15a9b4601846ad3daa301417922a30c15964847908c15f2479a860b44)

- Selecciona **Nuevo Escenario**. Un escenario en [Make.com ](https://bencorde.com/make)es el flujo de trabajo que define qué acciones se realizarán una vez que el webhook reciba la información. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d8776ed4894a400aa31eea6137ad62643a6383452a06411992449cd17fe5e859)

### 2. Seleccionar Webhooks como Disparador del Escenario

- Dentro del nuevo escenario, haz clic en el gran ícono de **+** en el centro de la pantalla.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1027b4d856e2486badacce5cc26313b0ab9003d1278d41058a3cf9857d5ae30c)

- Aparecerá un menú de opciones. Busca y selecciona **Webhooks** como el disparador (trigger) de este escenario.
- Luego, selecciona **Custom Webhook** (Webhook Personalizado) para configurar uno que se ajuste a tus necesidades específicas.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/150a71f34001499cb69fd939371fb21cf502c2c2494c4f8eb6b991675f23c805-md.png)

### 3. Crear un Nuevo Webhook y Nombrarlo

- Haz clic en **Agregar un Webhook** o **Crear nuevo Webhook**.
- Aparecerá un cuadro donde podrás introducir un nombre descriptivo. **Dale un nombre único y claro** al webhook, como "webhook-extraccion-datos-boleta". Esto es importante para identificar los distintos flujos de trabajo en el futuro.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4a838128106542b4a55994483ee07189c1bffe9d55204e90ace72aa7bfe8e822)

- Una vez nombrado, [Make.com](http://Make.com) generará automáticamente una URL única para el webhook.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5badcd5779004c4b99d60b400507935bf413cc325c1440b0a390274e53fe21b4)

### 4. Copiar la URL del Webhook para su Uso en ChatGPT

- Una vez creado el webhook, copia la URL que aparece. Esta URL es la dirección donde [Make.com](http://Make.com) recibirá los datos de ChatGPT.
- **Verás dos partes, una con el link y otra con el ID** (el ID es lo que sigue después del /)

Por ejemplo el webhook completo es 

> [https://hook.us1.make.com/3s5puvxno2eogo8u5ue9jjrcz3gqor27](https://hook.us1.make.com/3s5puvxno2eogo8u5ue9jjrcz3gqor27)

Donde el link es: [https://hook.us1.make.com](https://hook.us1.make.com/3s5puvxno2eogo8u5ue9jjrcz3gqor27)  
Y el ID es: [/3s5puvxno2eogo8u5ue9jjrcz3gqor27](https://hook.us1.make.com/3s5puvxno2eogo8u5ue9jjrcz3gqor27)

### 5. Configurar la URL del Webhook en ChatGPT Personalizado

- Entra al siguiente [GPT personalizado](https://chatgpt.com/g/g-qaZZZqxzt-create-make-com-webhook-integration) que te ayudará a construir el "OpenAI Schema", que es el código que deberemos incluirle al GPT personalizado para que ejecute y mande las acciones al escenario de Make.  
  
Link: [https://chatgpt.com/g/g-qaZZZqxzt-create-make-com-webhook-integration](https://chatgpt.com/g/g-qaZZZqxzt-create-make-com-webhook-integration)

- Abre el GPT personalizado y ve a la configuración o al esquema donde estás creando tu asistente personalizado.
- Haz clic en el botón predeterminado

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/fb082af72eaa4deaace8c16f6c300d12f8567a93b5964c128c836caf3783200a)

- En el área correspondiente, **pega la URL del webhook**. Esto permite que cuando le pidas a ChatGPT realizar una tarea (como extraer datos de un PDF o crear una tarea), enviará la información necesaria directamente a la URL del webhook en [Make.com](http://Make.com).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a39c68762e0f4973921a8320ed0591cd2d9b0b381b974d7493b57ea45da43416-md.png)

Luego nos pedirá que digamos cual es la acción que queremos que ejecute y cuales son las variables que queremos enviar a Make.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0f6840331e7c4ebb9e6e8ede781015afa5e24abaffa643e7b7758e0bb077f9b5-md.png)

Si queremos que extraiga datos de una boleta y que los pase a un excel, lo que haremos es decirle eso exactamente, y cuales son las variables que queremos extraer. Para fines prácticos usaremos: Fecha | Order ID | Producto Nombre | Total Gastado | Mail de contacto  


![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ccb9cd06bb054432a00ac474bcc95f1e3436f06c351d44ef9f16cafa13055414)

> Prompt utilizado: 
> 
> Necesito crear un gpt personalizado que envie los datos a make a traves de un webhook pero que los pase a un google sheets luego de analizar las boletas y tomar la informacion de las variables. Las variables o fields que necesitamos extraer específciamente son:
> 
> fecha
> 
> order_id
> 
> producto_nombre
> 
> total_gastado
> 
> mail

Luego nos responderá con el siguiente mensaje:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/083b333f26c84974b62b5c699ea9b9d378e00707f3274be5b72a3116726d1a58-md.png)

Y esta es la parte importante... porque nos dará el codigo del OpenAI Schema:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7eb9837bdd2d476b94227d36e33691b09fcecb50541645de85460d94a04938bb)

Código que copiaremos y pegaremos en el siguiente paso.

---

## Creación del Esquema de OpenAI

El esquema de OpenAI es un conjunto de instrucciones que permite a ChatGPT interpretar y estructurar la información de forma precisa, facilitando así su procesamiento y enviarlo a [Make.com](http://Make.com). Este paso es necesario cuando queremos que ChatGPT extraiga y organice datos específicos (por ejemplo, de un PDF de una boleta) y los envíe al webhook configurado en [Make.com](http://Make.com).

### ¿Qué es el Esquema de OpenAI?

Un esquema en OpenAI define cómo debe ChatGPT extraer y formatear los datos. Esto se realiza mediante un bloque de código JSON que actúa como una guía, permitiendo a ChatGPT identificar cada campo relevante (como "número de factura", "fecha", "total", etc.) y estructurarlo de forma adecuada para su envío.

### Crearemos el ChatGPT Personalizado, nuestro propio "Jarvis"

Para este paso, necesitaremos al cuenta de ChatGPT Plus. Crearemos un GPT personalizado y le daremos la instrucción que encontremos necesaria.  
  
Entraremos a ChatGPT y nos iremos a la sección de arriba a la izquierda que aparece "Explore GPT's"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/787d67cdca394752879f5c7b58037330d27ab4ae7f974e5d9729b408aefcffd7)

Iremos arriba donde sale "Create"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6efd645540724ac2a05b11ae1d7bbac67110f9537f6e4baaac6c4ba76b27adf8-md.png)

Rellenaremos el GPT con la informacion que necesitamos. Nota, esto lo peudes adaptar dependiendo de la funciones que quieres que realice, pero esta es la base.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3c23d57b94a94b2c9e2092f05e45002c5fa732a5bb4d40d3b73e66bd0075e507-md.png)

> Instruccion: Eres un asistente personal y ejecutivo muy útil, automatizando tareas para tu cliente, Benja. El objetivo es procesar sus tareas, enviando los resultados a varios webhooks que se recibirán en Make.com, los cuales luego se procesarán para realizar otras tareas y devolver un resultado que necesitas escribirle al usuario. Aquí están las reglas:
> 
> Primero, asegúrate de que todo el código requerido esté presente para que el webhook funcione.
> 
> Segundo, si falta algo, no envíes los resultados; en su lugar, haz un seguimiento para pedir la información faltante que aún no has recibido.
> 
> Tercero, si agregas información adicional (por ejemplo, si tu usuario te pide crear una publicación en un blog y tú la creas), pregunta si desea que también envíes esa información al webhook. Si dicen que sí, envíala; si dicen que no, no envíes los adicionales, solo envía la información que te proporcionó el usuario.
> 
> Cuarto, las palabras "enviar", "procesar", "crear", "automatizar", "hacer", "completar" u otras palabras similares se utilizan para indicarte que envíes los datos al webhook adecuado en Make.com.
> 
> ****Siempre confirma con el usuario los detalles de la reunión antes de enviarla al sistema. Confirmame las variables que crearás y te confirmaré con un "Sí" o un "No" antes de enviar el webhook.
> 
> **** LAS RESPUESTAS TIENEN QUE ESTAR EN EL FORMATO MM/DD/YYYY
> 
> Nota: Estamos en el 2024, para que no sigas agendando las cosas para el 2023. ESTAMOS EN EL 2024

---

Luego le daremos a donde sale "Create a new action"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/08e7f0f6a7e04fa1a9378ca4120352406aa7b4a6721b4f5391ab015762d5f8ea)

Y aquí le pegaremos el código json que nos dio el GPT en el paso anterior

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/40b24ff9b24f4a5ea45b567e256e73708739859e1a05430f84878d74b9eca977-md.png)

Nota: Abajo tienes que poner el "privacy policy" que es 

```
https://www.make.com/en/privacy-notice
```

Le daremos a "Create"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a1838824c7e4404aa7458eb6aae636b0ea5254378895447bbff725a0ac18da92)

y eligiremos la opción de "Only Me" para no comaprtir el GPT con nadie más y que nadie más tenga acceso a nuestro webhook (si quieres compartirlo con el equipo, puedes poner comaprtir con el link)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0daad5f3fed048b3a674e94730e7984c12fbcd8a02ac4165bfb99020218cae86)

Ya tendremos nuestro Jarvis "operativo"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cd981cd621ae4b86b22af42ba15e2af51c9c53c5714b4fb99d48e0c15949c962-md.png)

## Verificar que funciona

Para verificar que funciona, habilitaremos el "run once" del escenario de Make e intentaremos enviarle informacion.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/981dc7ff3d0f4ea9a5d6a86e6d8eb819da9c5a048fea4136a0f00a239b5bdbe9-md.png)

Para enviarle info le pediremos a chatgpt que nos mande informacion por ejemplo, de una boleta (puedes probar con esta misma imagen)

![sales-services-invoice-07.jpg](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d06b06294c3b47afad02093ff76eede8677a58034cc645d29698dfaaffcfe0a3-md.jpg)

Entraremos al GPT personalizado "Jarvis", y le subiremos la data y le pediremos que nos mande la info a Make para verificar que funciona.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4edfad96061945648eed394ddab0699c759ca4a559de4b58a714f89cc9faa09c-md.png)

Cuando apretemos "Confirm" debería aparecernos algo así en Make, donde tendremos la data que nos es relevante.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ee83593526994252b540bfd73a7de2bff71566e2d8a0463f9910d9f54e779043-md.png)

## Integración con Google Sheets:

De aquí en adelante, ya las opciones son infintias. Pasaremos los datos automaticamente a un Google Sheets.

- Crea un google sheets donde pasaremos la informacion.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1c3a1de6d5e44f78acf01a438329dfa49c9bf250a52f4154a652d639eabf6eaa)

**Configura Google Sheets en **[**Make.com**](http://Make.com): Añade Google Sheets a [Make.com](http://Make.com) y selecciona el "add a row"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b7634eaed5a64e35b4bfbebc87f4aea0ceee9ceab41840c99c3b8b6be709ca0e)

Mapea los datos recibidos del webhook a las columnas de tu hoja de cálculo.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/246356cd874a4ff28f25e06f97ca455bc8e100b42e5c4b7e96538cbaa96bb865-md.png)

**Prueba el Flujo**: Dale a "Run Once" abajo a la izquierda y envía datos de prueba desde ChatGPT y verifica que se guarden en la hoja de Google Sheets.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2cf447dd553f492b8c12e3f9bade9220db7385b43507453eb791939e4fa7f0c9)

---

## Otros Casos de Uso en [Make.com](http://Make.com)

Bueno, en el próximo módulo vamos a ver cómo agregar otros casos de uso y configurarlos para que se ejecuten en distintos webhooks desde la misma conversación. Es importante destacar que esto es un "trigger", o sea, desde acá podemos enviar la data que queramos y hacer absolutamente [cualquier automatización en ](https://www.skool.com/imperio-digital/classroom/a65de4cd?md=a64bbf02c8104dcba446f67fb720fd24)[*Imperio Digital*](https://www.skool.com/imperio-digital/classroom/a65de4cd?md=a64bbf02c8104dcba446f67fb720fd24)[.](https://www.skool.com/imperio-digital/classroom/a65de4cd?md=a64bbf02c8104dcba446f67fb720fd24) Porque esa es justamente la idea: lo que estamos creando aquí es un disparador automático. Todo lo que has visto en el módulo de automatización del [classroom ](https://www.skool.com/imperio-digital/classroom/a65de4cd?md=a64bbf02c8104dcba446f67fb720fd24)se puede aplicar aquí.

Para fines prácticos, vamos a agregar una función que nos permita agendar una nueva reunión en Google Meet, crear un enlace único y luego enviar un correo con toda la información de la reunión.

Aquí puedes conectar literalmente con más de 10,000 aplicaciones en [Make.com](http://Make.com), dándote infinitas opciones para crear flujos personalizados y automatizados.

---

## Añadir Más Rutas y Automatizaciones a ChatGPT

Si quieres que ChatGPT realice múltiples tareas, añade nuevas rutas:

- Crearemos un nuevo webhook en un **nuevo escenario**, que será llamado en el caso que se detecte la intención de "crear una nueva reunion y enviarle un mail de confirmacion" ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/19de7ab058314e54ba259414cac491d9f45b4dc77c964667b9fb36a39b98de42) **Editar el ChatGPT Personalizado**: Necesitaremos modificar el codigo nuevamente con el [GPT que nos ayudo a armar el "OpenAI Schema"](https://chatgpt.com/g/g-qaZZZqxzt-create-make-com-webhook-integration) inicial y decirle **en la misma conversacion** (prompt): > Oye, ya tenemos esta funcion, necesito agregarle un nuevo webhook que ahora se desencadene y se envie a make cuando necesite crear una nueva reunion con alguien, y que se la mandemos al mail  
>   
> El link del webhook es: [https://hook.us1.make.com](https://hook.us1.make.com/f37g8gvrkj7v7r6mohmxcrn97dkdivzw)  
> Y el ID es: [/f37g8gvrkj7v7r6mohmxcrn97dkdivzw](https://hook.us1.make.com/f37g8gvrkj7v7r6mohmxcrn97dkdivzw)  
>   
> Los eventos que necesito registrar son:  
>   
> nombre_evento  
>   
> fecha_inicio (en formato MM/DD/YYYY HH:mm)
> 
> duracion  
>   
> fecha_termino (en formato MM/DD/YYYY HH:mm + la duración de la reunion)
> 
> mail Nota: Estos eventos son variables que creamos que puedes adaptar para cada caso que necesites. Puedes crear absolutamente lo que quieras

A lo que procederá a modificarte nuevamente el código, código que reemplazaremos en el OpenAI Schema de nuestro Jarvis.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d3e6eb7c763b46bcac12e4311643bc03d5c01ba0927d450ab5bf1ed1a51ae186)

Nos iremos nuevamente a "My GPT's" a reemplazar el código, por ende iremos a "Edit GPT"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/916cbb193dbb447d90887ac58f693c39ad168a8a314b486197ab2989702e2c52-md.png)

Abriremos la acción que creamos previamente

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/50f462e6a58a4eca9d73dc2e10d113e51fd4f1114ad44d8caef21d4a31751f02)

Copiaremos y reemplazaremos el código COMPLETO, ya que este nuevo codigo incluye las dos funciones, tanto la del sheets como la de la reunion.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ac77dc86cec948749d6932dacaed8406253b41fd16da4ba890a628a3da4fb768)

Podemos confirmar que hay dos webhooks y dos acciones que se ejectuaran en cada situacion deseada si nos vamos abajo y vemos las "available actions"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/394b4fb3deee488493153aa132d8aee4eb83b3fba6ed47788f8b38501507ac69)

Cada una de estas se desencadenará en caso de que se vea la intención de llamar alguna de estas.

## Construir el proceso del segundo escenario de Make

Volveremos a abrir el escenario donde tenemos el webhook y continuaremos la automatizacion en Make. Agregaré un modulo de "crear una nueva reunion"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f1973d0293cf4df8a5db8506bab5d1f6678b8be7a09041cbaf3728d2cb7a521d-md.png)

Le dare a correr una vez para que el webhook me tome las variables que quiero trabajar con, así que habilitaré el "run once"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5b194a28fead48e7afbc89fb375f95a6b6ead72bd0fa4eb2ae2d0997b1cddc65)

y luego le mandare la data desde ChatGPT

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/216d7d2a0f8046d4ba001af2dbd303486f5d656fd0094728a7cb328cf141b551)

Y podemos verificar que ya está funcionando:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d6eb84ebbb934451a9fa09f4307a1e4f32469185b6884db2ad4be66b354453f3-md.png)

Ahora solo tenemos que crear el flujo y reemplazar las variables.  
Le agregaré el "enviar un mail desde outlook"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/32e05a3cbd8e44d987177f359a6e97cb3a98d86b92bf4bd6b36de03f5b2ad023-md.png)

Reemplazamos las variables en cada uno de estos, por ejemplo en el google meet sería algo así:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/80789888b27a49b68c1bed3f18e5214f94267523387f444881f6eb94105f5775-md.png)

Y en el outlook algo así:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e18ec63081c548d6bf70f1dce18d3cece6fe9707c2e947adab47ac18254d2f88-md.png)

Ahora si guardamos y activamos la automatizacion:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c36dc21a387b44279dfc079897cc6f693af794bea6784d28b8915a067dca5d7a-md.png)

y le volvemos a escribir lo mismo a ChatGPT"Necesito que me crees una reunion con Benja para mañana a las 16:00 hrs, debe durar 45 minutos y quiero mandarsela al mail [becord00@gmail.com](mailto:becord00@gmail.com)"  
  
ChatGPT nos dirá:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4ef77450ce5c4284ad3b50cc40d59ffa7818516d6aca4171860dca7742d62b84)

Y recibiremos un mail así:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/51f9db9b23a342c69a65ba3e38f3a7881f8f1d32446e43bd96f627188287abdf-md.png)

---

Este sistema permite automatizar tareas complejas usando ChatGPT y [Make.com](http://Make.com), lo que ahorra tiempo y esfuerzo en la gestión de tareas y datos. Con una inversión pequeña, puedes crear un asistente virtual que maneje llamadas, gestione documentos, y organice tu equipo de trabajo en segundos.
