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

## 🎙️ Transcripción

hoy vamos a construir un sistema en los próximos minutos que literalmente va a transformar la manera en la que usas chat gpt te puedo afirmar con seguridad que más del 99% de las personas no conoce esta función de charat gpt y sigue usándolo de la misma manera tradicional dándole una instrucción esperando una respuesta e iterando sobre esa respuesta Pero qué Si te dijera que chat gpt puede hacer mucho más que eso descubrí una forma en la que podemos conectarlo a más de 10,000 aplicaciones para que ejecute acciones en tiempo real por nosotros imagina que puedes pedirle a char gbt que haga casi cualquier cosa que te puedas imaginar desde crear y publicar contenido en tus redes sociales de forma automática hasta agendar reuniones generando links personalizados mandándose elos a la persona en un correo electrónico y luego agendá solo en tu calendario y hoy te voy a mostrar Cómo lograr esto en pocos pasos este tutorial es superrápido de configurar y para el final de este video vas a poder tener tu propio ya personalizado o tu asistente que te ejecute literalmente casi cualquier cosa que te puedes imaginar y déjame mostrarte cómo funciona si es que entro acá a chat gpt voy a tener una conversación regular con chat gpt si es que entro acá a chat gpt puedo decirle algo por el estilo de Necesito que me agendes una reunión con Max para mañana a las 4 de una duración de 45 minutos y se la mandes al mail Benja Cordero 00@gmail.com me va a preguntar si es que los detalles están bien me va a preguntar la hora duración 35 minutos se lo voy a mandar y yo le voy a poner que sí envíaselo y lo que está haciendo en este momento es me está creando un link único personalizado de Google Meet y se lo va a mandar al mail con la invitación Le voy a dar a confirmar acá y me dice la reunión con Max ha sido agendada exitosamente para las 4 y se ha enviado la invitación al correo X ahora si es que entramos a mi correo podemos ver que efectivamente Acabo de recibir la invitación con el link personalizado de el Google Meet y ahí me pueden ver intentando unirme a la reunión pero no solo eso porque imagínate ahora lo quiero agendar en mi calendario puedo volver acá y le puedo decir Oye ahora necesito que lo agregues a mi calendario y le voy a dar enter nuevamente me va a confirmar los detalles y yo le voy a confirmar los detalles y le voy a poner Sí una vez que le voy a confirmar me va a decir la reunión con Max ha sido agregada a tu calendario todo el éxito y si es que entramos al calendario podemos ver que efectivamente me agendó la reunión con Max de 4 a 445 y déjame mostrarte un Incluso un poco más extremo supongamos que Acabo de recibir esta boleta que está acá que no tengo idea lo que aparece y como yo soy de es organizado necesito organizar todo en un Google sheets entonces comienzo a centralizar todos mis costos todos mis gastos directamente acá lo que puedo hacer es entrar directamente a chat gbt y puedo decirle Oye mira tengo esta imagen me acaba de llegar Necesito que me pases toda la Data de esta imagen directamente a el Google sheets para poder ir centralizando mis gastos lo lo que voy a hacer es tomarlo desde el celular y voy a abrir la aplicación de chat gpt y le voy a subir exactamente esta foto si es que vemos acá voy a seleccionar la foto la voy a subir y voy a activar el dictado de voz y le voy a decir Oye necesito que me pases toda la información de esta boleta que recibí y la organices en mi Google sheet acorde a las variables que aparecen ahí Necesito que me incluyas el precio el producto el nombre bueno y todas las cosas que que necesito organizar dentro del sheets y aquí tenemos abierta directamente la conversación con chat gbt y una vez que se lo mando me va a hacer exactamente lo mismo nosotros podemos ver aquí en el celular que me sacó toda la información necesaria me pregunta si es que confirmo que estos son los datos correctos para ingresar al Google sheets le voy a poner sí Y como por arte de magia podemos ver cómo se acaba de agregar al Google sheets efectivamente confirmemos que es la misma información que compramos wooden blogs que tenemos el email que es mik Trade research y que gastamos 46 cont 38 efectivamente gastamos 46 con 38 no sé quién se va a gastar 46 comprando bloques de madera pero lo que voy es que esta herramienta funciona y ahora quizás te estás preguntando cómo funciona Okay Mira por ponerlo en términos muy simple te voy a mostrar todo esto paso a paso pero por ponerlo en términos muy simples los que estamos haciendo acá es cada vez que le pedimos una acción en específica a char gbt estamos mandándole una acción en específico a make y si no conoces lo que es make make es una plataforma forma que te permite conectar más de 10.000 aplicaciones y te permite crear flujos de automatización o flujos de trabajo A partir de un gatillante es decir cuando recibe una información se empieza a desencadenar una serie de automatizaciones que vienen después por ejemplo en este caso en este flujo de trabajo tenemos que cuando recibimos cierta información cree un link de un Google Meet en específico y después mando un mail en Outlook Así que si es que le doy a correr por ejemplo y supongamos que lo tengo activo y le digo créame otra reunión con Pedro ahora y mándamela al mail Benja Cordero 00 para mañana a las 11 de la mañana aquí me va a volver a confirmar lo mismo reunión con Pedro le voy a poner que sí estoy de acuerdo con esta duración y me va a mandar la Data directamente a make cuando le doy a confirmar podemos ver en tiempo real que estamos recibiendo esta Data del webhook Así que lo que está haciendo make es le está mandando toda esta Data que acabamos de crear y la está absorbiendo directamente aquí en este flujo podemos ver que se tomó la reunión con Pedro que acaba de crear un link en específico y que luego lo mandó directamente a benj Cordero 00@gmail.com y si es que dentro a mi mail podemos ver que tenemos aquí el nuevo link de trabajo y antes de mostrarte Cómo armar todo este proceso paso a paso te quería comentar que te acabo de publicar una guía en imperio digital si es que entras aquí donde sale automatizaciones y bajas vas a encontrar esta parte que sale ao automatiza tareas desde chat gbt donde te explico todo el paso a paso de cómo lo hacemos y tienes publicada una serie de automatizaciones y mucho contenido que puedes comenzar a implementar desde hoy además tenemos llamadas con expertos de manera semanal y una comunidad activa que está siempre dispuesta a ayudar y que compartimos un interés en común que es la Inteligencia artificial y las automatizaciones Así que ahora sí sin más que decir vamos a armar esta automatización lo primero que vamos a hacer es Tenemos que tener esto tenemos que crear lo que se conoce como un web Hook en make y crear esto realmente es s s simple una vez que entremos a make que es esta plataforma que conecta todas las aplicaciones y podemos crear estos flujos y sistemas de trabajo nos vamos a ir a donde sale crear nuevo escenario una vez que estemos acá vamos a tener que elegir cuál es el gatillante Y qué es lo que va a pasar después de que se llame ese gatillante imagina que yo toco el timbre cuando yo toco el timbre alguien va a abrir la puerta si es que yo nunca toco el timbre nadie va a ir a la puerta entonces lo que queremos hacer es necesitamos avisarle a make que alguien está tocando el timbre y para eso usamos lo que es un disparador instantáneo o También conocido por su nombre más elegante que es un webhook bueno para crear este webhook o este disparador instantáneo lo que vamos a hacer es vamos a apretar este más que aparece acá vamos a buscar la palabra webhook y vamos a elegir esta opción que sale custom webhook una vez que estemos acá le vamos a apretar a agregar o add aquí y te recomiendo que le pongas un nombre relativamente simple y lo que tenía pensado hacer era armar esta automatización primero para hacer que nos organice directamente las boletas y nuestros gastos y nuestros costos directamente en un sheet centralizado después vamos a crear otra automatización pero vamos a comenzar con esta entonces para este webhook lo que voy a hacer es le voy a poner el nombre webhook rayita cálculo rayita boletas y le voy a dar a guardar y lo que tenemos acá este link que aparece acá es el link que nos va a ser de interés como podemos ver este link tiene dos partes tenemos la primera parte que es el link y la segunda parte que es el id vamos a necesitar los dos para continuar con esta automatización ahora que tenemos este timbre ahora que podemos llamar a esta automatización lo que querríamos hacer es básicamente no lo hagan todavía pero para mostrarles es agregar una nueva línea en el Google sheets con la información de cada uno de estos verdad Pero de dónde sacamos esa información bueno queremos sacarlo de la conversación que tenemos con chat gpt para eso lo que vamos a hacer es vamos a crear un asistente personalizado de chat gpt necesitas una cuenta de chat gpt Plus Sí necesitas una Porque necesitamos crear un asistente personalizado y a la fecha Sí necesitas un acceso a gpt plus para crear esta automatización entonces lo que vamos a hacer Vamos a entrar directamente a charg PT y nos vamos a ir donde sale explorar gpt si es que no sabes lo que es un gpt personalizado es un gpt que cumple una función en específico y que ha sido entrenado con alguna función en específico sea distinto contexto un PDF etcétera nos vamos a ir acá donde sale crear y vamos a crear nuestro gpt aquí le vamos a poner el nombre y la función que queremos que tenga este chat gpt aquí para hacértelo aún más fácil te lo dejé publicado en imperio digital si tenemos toda esta guía que aquí te explico todo el paso a paso podemos ver que te puse el prompt o la instrucción base que queremos entonces la voy a copiar y para que te hagas una idea esto es eres un asistente personal automatizar tareas para Benja Tu misión es interpretar Cuál es el webhook que estamos llamando bla bla bla bla bla bla y después me confirmas los detalles y la envías al sistema s simple este prom lo pueden encontrar en imperio digital Ah y en imperio digital también tiene un periodo de prueba de 7 días entonces también si lo que te interesa es realmente ver esta automatización puedes entrar por s días completamente gratis y si es que cancelas antes de los 7 días no se te va a cobrar absolutamente nada Pero estoy seguro que una vez que entres no te vas a querer ir así que lo que vamos a hacer es vamos a copiar todo esto nuevamente y nos vamos a ir a charg bt y lo vamos a pegar aquí lo que voy a hacer es le voy a poner asistente y jarvis versión 3 y obviamente que le voy a poner un corazoncito y lo vamos a crear aquí le puse descripción Esto me permitirá mandarle acciones a make Porque esa es la función que nosotros vamos a hacer le voy a habilitar las capacidades y le voy a dar a crear voy a seleccionar que solo yo lo puedo ver porque en el fondo No quiero que nadie más tenga acceso si es que quisiera que alguien más tenga acceso le pondría que la gente con el link puede verlo y estando ya acá podemos ver y darnos cuenta de que ya tenemos el gpt activo pero todavía no le podemos mandar ninguna acción por qué porque no hemos establecido la comunicación entre char gpt y entre make lo que queremos hacer es hacer que este asistente que está acá pueda comunicarse con este escenario que acabamos de crear Así que lo que voy a hacer es voy a habilitar la conexión entre estos dos así que nuevamente iré a explorar los gpt abriré mi gpt y voy a editar el gpt que acabamos de crear voy a irme donde aparece las acciones y le voy a dar a crear una nueva acción y aquí es donde le vamos a hacer la conexión entre el make y el chat gpt en teoría en esta parte tenemos que agregarle código Pero descubrí en internet que existe un gpt personalizado que te crea específicamente este código con la conexión en específico para que tú no tengas que escribir absolutamente ninguna línea de código Así que esto realmente no puede ser más simple en la descripción te voy a dejar un gpt personalizado que te ayuda a escribir este código y también lo puedes encontrar en la guía de imperio digital si es que nos vamos a este link que aparece acá y lo abrimos en una nueva pestaña nos va a aparecer Alo algo así Crea una integración webhook entre make y chat gpt cuando apretemos este botón vamos a tener que pedir la ayuda a que nos cree el código Pero esto es s simple y es realmente muy pero muy guiado nos dice que tenemos que conectar el URL y que tenemos que mandarles el ID si es que volvemos a nuestra conexión en m recuerda podemos tomar el URL del webhook completo aquí lo vamos a copiar o le vamos a poner copi address y vamos a volver acá cuando lo peguemos Vamos a darnos cuenta que aquí tenemos el URL que es esta parte de acá y este es el ID o sea todo esto es el ID y todo esto es el URL Entonces yo le voy a poner acá que el URL es este y que el ID es este le voy a poner enter y después me va a seguir ayudando a crear esta acción Okay y aquí me pidió dos cosas la primera Cuáles son los campos que nosotros queremos y la segunda es que me gustaría automatizar con este webhook cuando nos vamos acá podemos ver que tenemos tenemos una serie de datos que nosotros necesitamos Como por ejemplo tenemos la fecha tenemos en este caso el nombre tenemos el cuánto gastamos tenemos el mail de contacto y así Y estos son los datos que nosotros necesitamos entonces lo que voy a hacer es copiar estos datos y voy a pegarlos acá y le voy a poner los datos que necesito son estos y los voy a pegar acá en este caso lo que necesito es la fecha el número de orden el producto el nombre cuánto gasté y el mail y después le vamos a explicar cuál es la labor en específico Para qué lo estamos programando nuevamente también te lo dejé publicado en chat gpt y en este caso Us necesito crear un gpt personalizado que envíe los datos a make a través de un webhook para que los pase a un Google sheets luego analizar las boletas y tomar la información de las variables las variables o los fields que necesitamos extraer específicamente son y este prompt lo que voy a hacer es copiarlo y pegarlo y bueno Aquí le voy a reemplazar que están arriba recordemos que es igual que tener una conversación con cualquier chat gpt le podemos hacer preguntas solamente que al final de todo nos va a dar el código Ah y paréntesis esta descripción la pueden hacer absolutamente para lo que ustedes quieran Okay entonces aquí podemos ver que nos está empezando a crear el código nos está creando un esquema de Open Ai que el esquema es lo que nosotros vamos a publicar justamente acá recuerdan que cuando editamos el chat gbt podemos crear una nueva acción bueno Esta es la acción que nosotros vamos a crear Okay este esquema que nos está creando justamente acá basado en los detalles que nosotros le dimos Ahora sí podemos subir podemos copiar el código y podemos pegarlo directamente acá como podemos ver aquí tenemos las acciones que están disponibles para hacer que es mandar la Data dentro de los métodos tenemos dos principales que es el get y que es el post El get es cuando tú extraes información y el post es cuando tú publicas información Okay en este caso lo que queremos hacer es publicar información Porque queremos mandarla directamente al make para poder trabajar con esa información después Aquí abajito tenemos las políticas de privacidad aquí recomiendo que pongan las políticas de make estas las pueden encontrar si es que buscan make privacy policy y abren el link que aparece acá Este de aquí y Listo Ya lo tenemos listo esto debería estar funcionando y si es que le doy a actualizar ya debería estar funcionando y debería estar mandando absolutamente toda la Data que nosotros queramos y le pidamos a make me voy a ir acá donde sale ver gpt y aquí tenemos nuestra conversación con el asistente jarvis versión 3 vamos a hacer el mismo ejercicio de antes y le vamos a mandar la misma boleta que le mandamos anteriormente le voy a poner Necesito que me extraigas esta Data y lo mandes a make a través de un webhook la razón por la que le estoy escribiendo esto es simplemente para verificar que esto está funcionando Okay voy a eliminar este módulo porque lo volveremos a crear después y le voy a dar a correr ahora podemos ver que va a estar cargando infinitamente porque no ha recibido nada de información pero si es que yo me voy acá y le digo Necesito que me extraigas Data y lo mandes a través de un webhook podemos ver que charg PT me va a decir perfecto Esta es la Data que extraí quieres que le mande esta información al webhook de make yo le voy a poner sí Y podemos ver que está ejecutando la acción y una vez que le de a confirmar debería aparecerme esta información acá si es que le voy a confirmar podemos ver que efectivamente acabamos de recibirla y Estas son las variables que recibimos primero la fecha después el orden El número de orden después el producto después el nombre cuánto gastamos y el mail Y a partir de esto es que podremos empezar a generar información y crear la automatización que sigue entonces supongamos que quiero actualizarlo en un Google sheets nos vamos a ir acá a Google sheets vamos a agregar una nueva fila Porque queremos que se vayan agregando por cada nuevo gasto y voy a seleccionar este mismo que está acá que es el cálculo expenses invoice voy a apretar el spreadsheet ID y entre todos estos vamos a elegir el que aparece acá vamos a apretar la hoja uno que vendría siendo esta hoja que aparece abajo y vamos a reemplazar las variables en la nueva fila por ejemplo fecha queremos la fecha en la orden que vendría siendo esta orden de acá queremos Que aparezca el order ID en el producto el producto en el nombre queremos Que aparezca el nombre en cuanto se gasto ponemos esto el neto no se lo pedí pero lo que podríamos hacer podría hacer algo por el estilo de en esta casilla vamos a tener eh No sé esto menos el valor del total por el impuesto que vendría siendo 0.19 por ejemplo mi invento no sé si es que el impuesto es del 19 por Pero esto no es un curso de contabilidad esto es un video de automatizaciones Así que no lo voy a poner así que ya el neto me lo voy a saltar y en el total voy a dejar nuevamente el total gastado y el mail de contacto vamos a poner el mail le vamos a dar okay Y ahora si es que corremos esta automatización nuevamente podemos darle a correr y podemos decirle vuelve a darme los datos o quizás podemos poner otra boleta a ver veamos esta que aparece aquí ahora hagámosla con esta esta es otra boleta x que encontré por ahí y Bueno aquí tenemos la boleta que tenemos dos ems que son efectivamente ent el ítem uno y el ítem dos no aparece fecha en esta boleta así que me puso no hay fecha específica Qué mala boleta que elegí pero bueno en fin me dijo faltan algunos datos puedes proporcionar la fecha supongamos que esto fue ayer y el email del cliente supongamos que es email @client comom y esto también es super interesante porque va a ir pidiéndome digamos ciertos datos que faltan y después me los va a confirmar entonces aquí tenemos la hoja de información confirmada quieres confirmar estos datos sí me pasó el ayer a que sea literalmente el 11 del 6 hoy día estamos al 11 del 7 eh las fechas me gusta trabajarlas al revés por un tema de comodidad dentro de make y aquí nos dicen la información ha sido enviada exitosamente al webhook de make y si es que vemos acá podemos ver que efectivamente tenemos el item mundos el nombre email cliente etcétera y que se acaba de actualizar el Google sheets y si es que entramos acá efectivamente podemos ver que se actualizó el Google sheets con el nuevo luego que le acabamos de subir y bueno acabamos de configurar chat gpt para que haga una acción Pero qué pasa si queremos que el mismo asistente haga dos o haga tres o cco 10 20 incluso cientos Bueno lo que vamos a hacer es vamos a agregarle un nuevo webhook porque claro lo tenemos configurado para que ejecute este escenario de acá pero si queremos que haga más cosas necesitamos configurar otro escenario con un webhook distinto para dejar corriendo esta automatización simplemente le daré acá y voy a guardar la automatización y le voy a poner chat gbt a sheets versión 3 Ahora sí guardaré y Volveré atrás y me iré a los escenarios volveré a crear un nuevo escenario y voy a crear otro webhook me iré donde sale custom webhook agregaré un nuevo webhook y lo que quiero crear ahora es un webhook que me pase la Data es de ch gbt y que me agende una reunión verdad Entonces qué es lo que voy a necesitar para una reunión Voy a necesitar el mail a cual se lo vamos a mandar voy a necesitar la hora a la que vamos a crear la reunión Voy a necesitar el nombre del evento y muchas otras cosas así que le voy a poner webhook reunión Meet versión 3 y este va a ser el nombre del webhook que le vamos a poner y aquí lo tenemos creado en un escenario completamente distinto para agregarle esta nueva acción lo que tenemos que hacer es volver a la conversación de antes y decirle Oye necesito crear un nuevo webhook que sea adicional al que me diste es decir Necesito que lo integres en tu código y para tu conveniencia también te cree el prompt específico en este caso para chat gpt si es que bajamos bajamos bajamos recordemos que tenemos esta guía donde te muestro todo el paso a paso de literalmente lo que hicimos en este video y aquí está el promt Oye ya tenemos esta función Necesito agregarle un nuevo webhook que ahora se desencadene y se envía cuando necesite crear una nueva reunión con alguien el link del webhook es este el ID es este los eventos que necesito registrar son el nombre del evento Cuándo empieza el evento Cuánto dura el evento cuándo termina y el mail Entonces le voy a copiar esto que está acá por fines prácticos y se lo voy a pegar directamente Okay ahora necesito ponerle la información de mi webhook verdad de este nuevo webhook o este nuevo disparador que se va a desencadenar Y eso es realmente lo que acabamos de crear entonces volveremos acá voy a pegar el link del webhook y el ID es este que aparece acá incluido La Barrita entonces nuevamente lo voy a pegar Respecto a los eventos aquí podemos registrar absolutamente los eventos que nosotros queramos como necesitamos agendar una reunión Necesito el nombre del evento cuando empieza esto es importante que quiero que esté el formato en mes después día y después año cuánto va a durar el evento y cuándo va a terminar el evento verdad que esto lo podemos sacar básicamente de la información de la duración y por lo mismo le puse la fecha más la duración de la reunión y el mail o sea son estos cuatro eventos que va a crear 1 2 3 cu cinco eventos que va a crear 1 2 3 4 5 le voy a dar a enviar y listo aquí me está creando y me está sobre escribiendo el código que creamos anteriormente si nos vamos acá a los G es me voy a mi gpt y me voy a editar el jarvis podemos ver que si apretamos las acciones tenemos este código que es el que pegamos anteriormente Bueno ahora lo que está haciendo chat gbt es me está creando otro código que es el mismo código de antes más el nuevo código de la otra acción que va a hacer así que lo que tenemos que hacer es sobre escribirlo por eso es super importante que usemos la misma conversación que creamos para crear el webhook anterior Pero esta vez le digamos Oye necesito agregar este evento y aquí me lo creó con los cinco eventos que es el nombre fecha duración fecha y el mail que son los eventos que vamos a recibir aquí en make voy a subir y voy a copiar este código que aparece acá Volveré acá a editar el gbt de nuestro asistente yarvis y aquí podemos ver que mira tenemos una acción Verdad que es Send order Data que es la que acabamos de crear para que nos pase la Data al Google sheets y si es que yo selecciono todo esto lo borro y pego el nuevo código vamos a ver que vamos a tener ahora dos acciones la primera que es pasar la Data al Google sheets y la segunda que es crear una reunión Entonces qué va a pasar cuando tengamos la conversación con este gpt personalizado y el gpt interprete que tú quieres hacer alguna de estas dos acciones va a llamar el webhook si es que tu mensaje tiene una intención de pasar la Data de una boleta y pasarla al Google sheets va a ser este primer webhook que está acá si es que te ve la intención de agendar y crear el link de una reunión para mandárselo a alguien por mail va a crear o va a llamar este webhook directamente que aparece acá Así que te voy a mostrar ahora cómo funciona le voy a dar a actualizar y le voy a dar a ver gpt si es que entro a este webhook y le doy a correr que es el nuevo que acabamos de crear le voy a cambiar el nombre y le voy a poner agenda reunión Meet y le voy a guardar y le digo necesito agendar una reunión con Pedro para mañana a las 6 de la tarde de 45 minutos y se la mandes a al mail Pedro @pedro comom lo que va a hacer acá es me va a recopilar esa Data verdad me va a confirmar que el nombre del evento reunión con Pedro está la fecha de inicio bla bla bla lo voy a poner sí está correcto y me va a comenzar a ejecutar la acción verdad en este caso estamos esperando a que se ejecute la acción y si le voy a confirmar me va a decir que la reunión con Pedro ha sido agendada exitosamente es decir que le mandó exitosamente la señal a make.com y efectivamente podemos ver que la recibimos acá nos aparece el check Y si apretamos la nube que aparece acá o la burbujita podemos ver que ya tenemos las variables reunión con Pedro fecha de inicio duración fecha de término bla bla bla y desde aquí podemos armar la automatización como la armarías como en cualquier automatización de make arrastramos un nuevo módulo que es lo primero que queremos hacer queremos crear un evento de un Google Meet Entonces vamos a buscar Google Meet y le vamos a dar a create meeting es decir crear una reunión cuando estamos acá vamos a conectar nuestro calendario vamos a poner el nombre del evento de la variable que acabamos de recibir cuando empieza que sería el 11 el 08 el 2024 a las 18 horas y cuando termina que sería a las 18:45 horas ahí podemos ver que acaba de crear el evento y le vamos a dar a Okay qué queremos hacer Cuál es el próximo paso lógico lo que queremos a hacer es enviarle un mensaje verdad Así que vamos a ir a Outlook o Gmail o mail o absolutamente lo que sea que uses yo en lo personal uso Outlook por un tema de comodidad y nos vamos a ir donde sale crear y enviar un mensaje en el asunto le voy a poner poner lo que quiera le podemos poner evento o le podemos poner el nombre del evento como reunión con Pedro después en el contenido le voy a poner Hola aquí te mando el link de el nombre del evento que es desde fecha de inicio hasta fecha de término y le voy a poner punto te dejo el link aquí y aquí es donde vamos a a buscar el link de la reunión que en teoría se acaba de crear acá es decir queremos mandarle el hangout link es decir el link donde nos vamos a conectar después nos vamos a ir a quién queremos enviárselo verdad Y si recordamos también le pedimos la variable del email el desde que mail da igual y le voy a poner a Okay ahora le voy a dar a correr y nuevamente Si es que le vengo a decir vuelve a crearlo Pero esta vez mándale el mail a y le pongo mi correo electrónico vamos a ver que esto va a cambiar y va a volver a ocurrir pero me lo va a mandar a mi mail si Confirmamos podemos ver que acabamos de recibir el webhook acaba de crear la reunión nos creó este link personalizado y acabamos de recibir el mail verdad o en teoría acabamos de recibir el mail y solamente para confirmar si es que entro acá efectivamente Acabo de recibir reunión con Pedro hola aquí te mando el link de reunión con Pedro que es desde Hasta te dejo el link aquí y el Google Meet que está funci and así que así es como tú armas tu propio asistente personalizado para hacer absolutamente lo que quieras y quiero comentarte que esto que acabas de ver es solamente el inicio Por qué Porque existe un mundo de automatizaciones y sistemas que podemos crear para nuestra conveniencia en lo personal hay muy pocas tareas muy pocas y cuando te digo pocas es pocas que no he conseguido automatizar si es que tenemos el conocimiento técnico de hecho todas las automatizaciones que que ves que tengo publicadas en imperio digital como esta automatización para crear contenido y publicarlo automáticamente en distintas redes sociales o esta para crear ebooks personalizados para cada persona e incluso esta para encontrar leads en específico pueden ser desencadenadas desde chat gbt Así que realmente esto es muy muy útil y si entendemos Cómo combinar las automatizaciones con la Inteligencia artificial no tengo dudas de de que en el futuro vas a poder ser mucho más productivo y estas mismas soluciones que hoy día te pueden estar funcionando a ti puedes comenzar también a venderlas o usarlas para escalar tu propio negocio y justamente de eso se trata imperio digital imperio digital es una comunidad donde somos fanáticos de las automatizaciones de la Inteligencia artificial pero sobre todo de aprender a ahorrar tiempo con las cosas que Realmente funcionan ya somos más de 200 miembros y estamos teniendo llamadas semanales en vivo con expertos en automatización y también distintas sesiones de preguntas y respuestas además si te estás enfrentando algún problema en esta automatización puedes directamente publicarla el Imperio digital y alguno de nuestros especialistas o incluso alguno de los cracks que están dentro de la comunidad van a poder ayudarte y lo mejor de todo es que puedes probar absolutamente sin riesgo porque acabamos de habilitar una opción de 7 días gratuitos es decir si entras los primeros 7 días y sientes que la comunidad no es para ti puedes cancelar Sin costo alguno Pero estoy seguro que que cuando entres vas a realmente quedar fascinado o fascinada porque es el espacio del cual me habría encantado ser parte antes así que sin más que decir te invito a que entres conozcas imperio digital sin riesgo alguno y te hagas parte de lo que potencialmente va a ser la comunidad más grande de automatizaciones hispanohablante y queríamos aprovechar de felicitar a los miembros de imperio digital que llegaron a nivel cuatro en el mes de octubre que es Alejandro de edmark Rubén García de Pitágoras trading que tiene su canal Vicente rabaj guus J los di and partners Juan marquez aitor Vergara También conocido como vergar ator y a Andrés García que nos manda todo desde San Salvador de jujui Argentina felicidades por haber llegado al nivel cuatro en imperio digital cuéntame qué te pareció este video en los comentarios si no te has suscrito al Canal recomiendo que te suscribas porque aquí hablamos de las cosas que funci Estoy seguro que te va a encantar este video que aparece aquí chao
