# 📄Facturación Automática ChatGPT + Sheets + Make

> Ruta: Automatizaciones Make › 📄Facturación Automática ChatGPT + Sheets + Make

**🎬 Vídeo (49.5 min):** https://www.youtube.com/watch?v=c_VVCadaOx0

**📎 Recursos:**
- Sheets Factura Automatica
- Docs Factura Automatica Plantilla
- JSON Make Factura Automatica

---

Imagina esto: acabas de cerrar una venta, y en lugar de perder tiempo generando manualmente una factura, un sistema lo hace todo por ti, la crea, la registra y la manda por correo. Así es como funciona este flujo automatizado que hemos armado en Imperio Digital usando ChatGPT y Make.

Todo comienza con un mensaje sencillo. Por ejemplo, le dices a ChatGPT: *"Crea una factura para Benjamín Cordero por 3 manzanas a $590, 4 pepinos a $680 y 5 plátanos a $1,100, luego mandasela al mail"* ChatGPT interpreta los datos y los envía mediante un webhook a Make. Este webhook es el disparador que pone en marcha todo el sistema.

Primero, Make verifica si el cliente ya existe en tu base de datos. Si no está, lo crea automáticamente, incluyendo todos los detalles como nombre, dirección y correo electrónico. Luego, se generan los datos de la factura, se rellenan en una plantilla en Google Docs y se calculan los totales de forma precisa. Todo esto pasa en segundos, sin que tú tengas que hacer nada.

La factura se guarda en PDF, organizada dentro de una carpeta en Google Drive. Si el cliente ya tiene una carpeta, el sistema la usa; si no, crea una nueva automáticamente. Para cerrar el ciclo, la factura se envía directamente al correo del cliente, y tú puedes recibir una copia para asegurarte de que todo está en orden.

Este sistema no solo te ahorra tiempo, sino que elimina errores y centraliza todo el proceso. Y si quieres llevarlo un paso más allá, puedes personalizar cada detalle: desde agregar más datos del cliente hasta conectarlo con otras herramientas que uses en tu negocio.

Puedes descargar esta configuración lista para usar, adaptarla en minutos y comenzar a operar con ella hoy mismo.   
  
El objetivo es simple: eliminar las tareas repetitivas para que puedas concentrarte en lo que realmente importa.  
  
------------------------------------------  
Prompt para OpenAI (GPT Personalizado):

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ebf9a47ffb6d4965a7c5a2a34bb22442e15ca65484744a5bbb767543ce05e65c-md.png)

Description:   
  
Eres un asistente diseñado para ayudar a crear, enviar y generar facturas de manera eficiente. Tu objetivo es clasificar en una de las tres categorías principales: crear_cliente, crear_item o crear_factura, además de la data estructurada que lo acompaña a cada categoria.

  
System Prompt

```
Visión:
Eres un asistente diseñado para ayudar a crear, enviar y generar facturas de manera eficiente. Tu principal objetivo es procesar solicitudes relacionadas con la gestión de clientes, ítems y facturas, asegurándote de clasificar cada operación en una de las tres categorías principales: crear_cliente, crear_item o crear_factura. Además, debes recopilar toda la información requerida según la categoría seleccionada y confirmar con el usuario antes de enviar los datos al webhook como un JSON completo que contenga tanto la clasificación como los datos estructurados.

Rol y Propósito
Clasificar la intención del usuario:
Identifica si la solicitud corresponde a crear_cliente, crear_item o crear_factura.
Recopilar y validar datos:
Solicita toda la información necesaria según la categoría seleccionada.
Valida que todos los campos requeridos estén completos y correctamente formateados.
Generar JSON estructurado:
Crea un objeto JSON que combine la clasificación (clasificacion) y los datos recolectados, estructurados según el esquema predefinido.
Confirmar antes de enviar:
Antes de enviar los datos al webhook, presenta al usuario el JSON generado para confirmar que toda la información es correcta.
Enviar al webhook:
Solo envía el JSON al webhook si el usuario confirma explícitamente que los datos son correctos.
Estructura del Webhook General y Clasificaciones
Clasificación: crear_cliente
Objetivo: Registrar un nuevo cliente en la base de datos.
Datos requeridos: Nombre del cliente, calle, ciudad, país y email.
Data estructurada:
json
Copy code
{
  "clasificacion": "crear_cliente",
  "nombre_cliente": "string",
  "calle": "string",
  "ciudad": "string",
  "pais": "string",
  "email": "string"
}
Clasificación: crear_item
Objetivo: Registrar un nuevo ítem para futuras facturas.
Datos requeridos: Nombre del ítem, descripción y precio.
Data estructurada:
json
Copy code
{
  "clasificacion": "crear_item",
  "nombre_item": "string",
  "descripcion": "string",
  "precio": "number"
}
Clasificación: crear_factura
Objetivo: Generar una factura combinando información de clientes e ítems registrados previamente.

Datos requeridos:

Nombre del cliente.
Descripción del proyecto.
Ítems seleccionados (nombre, cantidad y precio).
Fecha de entrega.
Fecha actual.
Número total de ítems distintos.
Separación de los ítems en nombre_itemX, cantidadX y precioX (hasta 6 ítems).
Data estructurada:

json
Copy code
{
  "clasificacion": "crear_factura",
  "cliente": {
    "nombre": "string"
  },
  "descripcion_proyecto": "string",
  "items_distintos": "integer",
  "nombre_item1": "string",
  "cantidad1": "integer",
  "precio1": "number",
  "nombre_item2": "string",
  "cantidad2": "integer",
  "precio2": "number",
  "nombre_item3": "string",
  "cantidad3": "integer",
  "precio3": "number",
  "nombre_item4": "string",
  "cantidad4": "integer",
  "precio4": "number",
  "nombre_item5": "string",
  "cantidad5": "integer",
  "precio5": "number",
  "nombre_item6": "string",
  "cantidad6": "integer",
  "precio6": "number",
  "fecha_entrega": "DD/MM/AAAA",
  "fecha_actual": "DD/MM/AAAA"
}
Proceso de Clasificación Automática
Recepción de la solicitud: El usuario describe su intención.
Identificación de la categoría: El asistente determina si la solicitud corresponde a crear_cliente, crear_item o crear_factura.
Recopilación y validación de datos:
Valida que todos los campos requeridos estén completos y correctamente formateados.
Si es crear_factura:
Calcula el número de items_distintos basado en los nombres de los ítems proporcionados.
Separa los ítems en campos individuales (nombre_itemX, cantidadX, precioX) hasta un máximo de 6.
Completa los campos faltantes con valores predeterminados ("0" para nombres y 0 para cantidades y precios).
Generación del JSON estructurado: Crea el JSON que incluye la clasificación y los datos completos.
Confirmación del usuario: Presenta el JSON al usuario con un mensaje claro:
"Aquí están los datos que se enviarán al webhook. Por favor, confirma si todo está correcto:"
Envío al webhook: Solo envía el JSON si el usuario responde afirmativamente.
Ejemplo de JSON Generado
Usuario: Quiero generar una factura.
Asistente: Aquí está el JSON estructurado con los datos proporcionados:

json
Copy code
{
  "clasificacion": "crear_factura",
  "cliente": {
    "nombre": "Juan Perez"
  },
  "descripcion_proyecto": "Compra de equipos",
  "items_distintos": 2,
  "nombre_item1": "Laptop",
  "cantidad1": 2,
  "precio1": 1200,
  "nombre_item2": "Mouse",
  "cantidad2": 3,
  "precio2": 50,
  "nombre_item3": "0",
  "cantidad3": 0,
  "precio3": 0,
  "nombre_item4": "0",
  "cantidad4": 0,
  "precio4": 0,
  "nombre_item5": "0",
  "cantidad5": 0,
  "precio5": 0,
  "nombre_item6": "0",
  "cantidad6": 0,
  "precio6": 0,
  "fecha_entrega": "2024-12-31",
  "fecha_actual": "2024-12-24"
}
Asistente: ¿Deseas confirmar y enviar esta información al webhook? (Responde con "Sí" para enviar o indica si deseas corregir algo).
```

OpenAI Schema:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b94bf311d5d3481c93044b50f5ffd84c084036cb88944e47806787b8519cb5e7-md.png)

Schema:

```
{
  "openapi": "3.1.0",
  "info": {
    "title": "Gestión de Clientes, Ítems y Facturas",
    "version": "1.0.0",
    "description": "API para la creación y gestión de clientes, ítems y facturas utilizando un webhook de Make.com."
  },
  "servers": [
    {
      "url": "https://hook.us1.make.com",
      "description": "Make.com Webhook Base URL"
    }
  ],
  "paths": {
    "/npcsl5y43z6i5obwhhvm9537xun1yg1r": {
      "post": {
        "summary": "Procesar solicitudes para crear clientes, ítems y facturas",
        "description": "Webhook general que clasifica y procesa solicitudes en tres categorías: crear_cliente, crear_item y crear_factura.",
        "operationId": "procesar_solicitud",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "clasificacion": {
                    "type": "string",
                    "enum": ["crear_cliente", "crear_item", "crear_factura"],
                    "description": "Tipo de operación a realizar (crear_cliente, crear_item o crear_factura)."
                  },
                  "nombre_cliente": { "type": "string" },
                  "calle": { "type": "string" },
                  "ciudad": { "type": "string" },
                  "pais": { "type": "string" },
                  "email": { "type": "string", "format": "email" },
                  "nombre_item": { "type": "string" },
                  "descripcion": { "type": "string" },
                  "precio": { "type": "number" },
                  "cliente": {
                    "type": "object",
                    "properties": {
                      "nombre": { "type": "string" }
                    },
                    "description": "Solo se incluye el nombre del cliente para la creación de facturas."
                  },
                  "descripcion_proyecto": { "type": "string" },
                  "items_distintos": {
                    "type": "integer",
                    "description": "Cantidad de ítems distintos solicitados en la factura.",
                    "minimum": 1
                  },
                  "nombre_item1": { "type": "string", "default": "0" },
                  "cantidad1": { "type": "integer", "default": 0 },
                  "precio1": { "type": "number", "default": 0 },
                  "nombre_item2": { "type": "string", "default": "0" },
                  "cantidad2": { "type": "integer", "default": 0 },
                  "precio2": { "type": "number", "default": 0 },
                  "nombre_item3": { "type": "string", "default": "0" },
                  "cantidad3": { "type": "integer", "default": 0 },
                  "precio3": { "type": "number", "default": 0 },
                  "nombre_item4": { "type": "string", "default": "0" },
                  "cantidad4": { "type": "integer", "default": 0 },
                  "precio4": { "type": "number", "default": 0 },
                  "nombre_item5": { "type": "string", "default": "0" },
                  "cantidad5": { "type": "integer", "default": 0 },
                  "precio5": { "type": "number", "default": 0 },
                  "nombre_item6": { "type": "string", "default": "0" },
                  "cantidad6": { "type": "integer", "default": 0 },
                  "precio6": { "type": "number", "default": 0 },
                  "fecha_entrega": { "type": "string", "format": "date" },
                  "fecha_actual": { "type": "string", "format": "date" }
                },
                "oneOf": [
                  {
                    "required": ["clasificacion", "nombre_cliente", "calle", "ciudad", "pais", "email"],
                    "description": "Requisitos para crear_cliente."
                  },
                  {
                    "required": ["clasificacion", "nombre_item", "descripcion", "precio"],
                    "description": "Requisitos para crear_item."
                  },
                  {
                    "required": [
                      "clasificacion",
                      "cliente",
                      "descripcion_proyecto",
                      "items_distintos",
                      "nombre_item1",
                      "cantidad1",
                      "precio1",
                      "nombre_item2",
                      "cantidad2",
                      "precio2",
                      "nombre_item3",
                      "cantidad3",
                      "precio3",
                      "nombre_item4",
                      "cantidad4",
                      "precio4",
                      "nombre_item5",
                      "cantidad5",
                      "precio5",
                      "nombre_item6",
                      "cantidad6",
                      "precio6",
                      "fecha_entrega",
                      "fecha_actual"
                    ],
                    "description": "Requisitos para crear_factura."
                  }
                ]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Solicitud procesada correctamente",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "status": { "type": "string", "example": "success" },
                    "message": { "type": "string" },
                    "data": { "type": "object" }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Error en los datos proporcionados",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "status": { "type": "string", "example": "error" },
                    "message": { "type": "string" }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}

```

Links de Interés:  
  
Link Sheets (crear copia) [https://docs.google.com/spreadsheets/d/1cE4m3GS328ENx1wOIWiR-zofeIItmxSCeJ_vHuwJg9I/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1cE4m3GS328ENx1wOIWiR-zofeIItmxSCeJ_vHuwJg9I/edit?usp=sharing)

Link Custom GPT [chatgpt.com/g/g-qaZZZqxzt-create-make-com-webhook-integration](http://chatgpt.com/g/g-qaZZZqxzt-create-make-com-webhook-integration)

Link Plantilla Docs: [https://docs.google.com/document/d/1ttljMyZra9ImLARw7_MMEKEgNgJVu4ZmOFOrwgVS2eo/edit?usp=sharing](https://docs.google.com/document/d/1ttljMyZra9ImLARw7_MMEKEgNgJVu4ZmOFOrwgVS2eo/edit?usp=sharing)

## 🎙️ Transcripción

sabemos que lo último que queremos hacer después de un largo día de trabajo es mandar la factura a ese cliente que acabamos de cerrar o a múltiples clientes que vamos cerrando en el camino pero qué Si te dijera que voy a mostrarte un sistema que te va a permitir nunca más tener que hacer una factura de manera manual y si sigues con cuidado el paso a paso para el final de este video vas a poder implementarlo directamente por tu cuenta y no solo eso porque también te voy a dar una manera en la que puedes descargar y comenzar a implementar este sistema desde de hoy Déjame mostrarte en un ejemplo cómo funciona Necesito que le emitas y le mandes al correo a Benjamín Cordero la facturación de la venta de tres manzanas a 590 cada una cuatro pepinos a 680 cada uno cinco plátanos a 1100 cada uno y el costo de envío que fueron de 3,990 pes aquí podemos ver que Acabo de recibir en el celular exactamente esto y le voy a poner a enviar me va a confirmar los detalles de la factura Benjamín Cordero manzanas unidades costo de envío y después me va a pedir verificar los artículos que están acá yo lo voy a poner si es correcto le voy a dar enviar y en el momento que le voy a confirmar va a empezar a correr directamente el sistema que está acá va a buscar en mi lista de clientes en este momento Si es que hay un cliente que se llama Benjamín Cordero y va a tomar todos los datos del mismo cliente y una vez que le doy a enviar el sistema va a empezar a correr lo primero que va a hacer es va a buscar en nuestra base de datos si es que hay algún cliente que se llama Benjamín Cordero después va a agregar todo esto a la base de datos de la factura que va a ser exactamente aquí ya hice muchas pruebas por eso se puede ver directamente más arriba después directamente nos va a crear la factura en base a una plantilla cuya plantilla está acá y también te la voy a dar para que te la descargues después va a descargar el documento y en Drive va a empezar a organizarlo si es que ya hay una carpeta que tiene el nombre de Benjamín Cordero la va a meter directamente adentro de la carpeta pero si es que no hay una carpeta que se llama Benjamín Cordero y hay un nuevo cliente porque es un nuevo Cliente va a crear la carpeta después la va a subir y va a enviar directamente al correo electrónico la factura que acabamos de crear De hecho si es que entro a mi correo electrónico vamos a ver que aquí está la factura de Benjamín cordero con la fecha de vencimiento y si es que la abrimos efectivamente tenemos las Manzanas al precio unitario por tres los pepinos por cuatro los plátanos y el costo de envío en total y la facturación por 13980 toda la matemática está hecha directamente en el sistema y te voy a mostrar paso a paso más la automatización para que la descargues y la importes directamente Pero qué pasa si es que todavía no tenemos los datos del cliente bueno eso también está pensado porque como podemos ver acá tenemos dos caminos uno que es crear cliente y el otro que es Buscar el cliente Entonces si es que yo vuelvo a entrar al mismo sistema y le mando un audio de voz diciendo Oye necesito crear un nuevo cliente me lo va a crear por ejemplo le voy a poner necesito crear un nuevo nuevo cliente Voy a conversar en este caso estoy hablando directamente con charg bt y me va a pedir los datos que yo necesito para que lo metamos a la plantilla de los clientes para este caso le voy a decir invéntame todo y me va a confirmar Juan Pérez calle falsa ciudad fantasía email Juan Pérez @gmail o @example y le voy a poner sí está correcto una vez que le dé a confirmar acá se me va a agregar automáticamente aquí en la planilla ahora después en otro momento si es que abro una nueva conversación por ejemplo y le digo créame una factura a Juan Pérez por la venta de dos manzanas a 390 pesos o 490 pesos cuya factura pense mañana por ejemplo me va a directamente confirmar los datos le voy a decir sí está correcto lo verifico acá y le envío los datos va a empezar a correr nuevamente la automatización y va a buscar acá en este caso los datos de Juan Pérez que es calle falsa ciudad fantasía país y imaginario luego me va a crear el documento va a descargar el documento lo busca en Drive verifica como no tiene carpeta y es un nuevo cliente crea la nueva carpeta y lo sube y ahora si es que vuelvo acá y actualizo el Google Drive se me va a haber creado una nueva carpeta con Juan Pérez y si es que la abrimos vamos a ver que aquí está rellena literalmente con toda la información del cliente y que recibimos el correo electrónico directamente en nuestra bandeja de entrada as es que lo abrimos acá vemos el correo adjunto y aquí está y lo mejor de todo es que todo esto fue hecho de manera completamente automática y bueno lo que te voy a mostrar ahora es Cómo podemos Conectar a char gbt directamente a make pero si quieres más detalle en eso tengo un video que te lo voy a dejar acá y si te estás preguntando qué es make make es una aplicación que te permite crear flujos de trabajo completamente automatizados conectando más de 10,000 aplicaciones entre sí Y si no quieres armar toda esta automatización y la quieres incluir directamente en tus flujos de trabajo también lo puedes hacer si es que eres miembro de imperio digital Simplemente tienes que ir a crear un nuevo escenario entrar acá a Imperio digital descargarte La automatización que es esta que aparece acá ponerle Descargar y después Volver al nuevo escenario apretar los tres puntitos y darle a importar seleccionar elegir el archivo darle a guardar y voilá la automatización ya va a estar importada y lo único que tienes que hacer es reemplazar un par de variables Y si te estás preguntando qué es imperio digital bueno imperio digital es una comunidad donde lo que hacemos Es ahorrar tiempo mediante automatizaciones ya somos más de 500 miembros y todos estamos con un mismo objetivo en común ahorrar tiempo con automatizaciones que funcionan aquí es donde puedes descargar literalmente todos los recursos e importar todas las automatizaciones que hemos armado y donde tendrás acceso a clases semanales con expertos en automatizaciones para mostrar lo que está funcionando también tendrás acceso a soporte por si es que estás teniendo algún problema en tus automatizaciones y acceso a una comunidad donde puedes ir publicando los problemas que que vas teniendo las victorias las dudas y vamos todos creciendo con un mismo Norte y lo mejor de todo es que puedes entrar a probar completamente gratis ya que habilitamos la opción de probar por 7 días gratis y si te gusta Te quedas y si no y cancelas antes del día 7 no se te va a cobrar absolutamente nada Así que ahora sí vamos a lo que nos compete vamos a armar esta automatización completa paso a paso por lo que si te quedas hasta el final del video deberías ser capaz de armarla también por tu cuenta pero lo que quiero que sepas es que también el nivel de personalización que uno puede adaptar y crear y modificar en este sistema está Solamente limitado por tu mente ya que por ejemplo si quisiéramos hacer el proceso de facturación automática a un mismo cliente cada 30 días podemos modificarlo si quisiéramos agregarle algo que se conecte a otra base de datos como nuestros ems o los productos ya listos también lo podemos hacer y si quisiéramos hacer un sistema de verificación para no mandarle directamente la factura sino recibirla yo confirmarla y después volverla a mandar también se puede hacer y todo este sistema tiene dos grandes partes que vamos a ver la primera es cómo conectamos a char gpt y cómo hacemos que chat gpt envíe esta señal y la segunda es la automatización en Sí para ambos casos te voy a dejar plantillas para que puedas literalmente copiar y pegar y comiences a operar hoy mismo de todas maneras si quieres profundizar un poco más en la parte de la integración de charg PT con make también te dejé este video preparado con un poco más de detalle del paso a paso de cómo lo podemos hacer pero ahora te voy a mostrar la versión rápida y la versión corta para pasar a la automatización lo primero que vamos a hacer es vamos a crear un escenario en make esta aplicación que nos conecta más de 10,000 aplicaciones y nos ayuda a crear flujos de trabajos automatizados vamos a irnos a crear un nuevo escenario y vamos a buscar la opción de un webhook vamos a elegir custom webhook y un webhook es un disparador instantáneo que cuando recibe información recibe la información como Data estructurada es decir desencadena una automatización a partir de los parámetros que recibió Entonces vamos a irnos a agregar y vamos a crear un nuevo webhook en este caso le voy a poner webhook factura versión 3 porque es la tercera vez que lo creo le voy a dar a guardar y vamos a darle a Okay después lo que vamos a hacer es vamos a crear un gpt personalizado para que directamente se comunique con este webhook y que le podamos mandar la información como Data estructurada por ejemplo el nombre de la persona si queremos crear un nuevo cliente nombre mail ciudad etcétera o si queremos crear una nueva factura Cuáles son los ítems que nos pidió Cuáles son los montos etcétera Así que para ello vamos a entrar a chgt comom para crear un gpt personalizado si es necesario la versión Plus o Superior y nos vamos a ir acá arriba a la derecha donde sale my gpt vamos a seleccionar un crear un gpt y le vamos a poner el nombre que queramos para este caso le voy a poner asistente de facturas versión 3 aquí en las instrucciones lo que vamos vamos a hacer es le vamos a dar una instrucción que entienda que tiene que mandar cierta Data cuando nosotros se la pedimos en las instrucciones también le podemos alimentar con contexto con todo lo que queramos para que sea realmente nuestro asistente pero yo te preparé una instrucción que puedes literalmente copiar y pegar si es que entras al School vamos a ver acá que tenemos la descripción eres un asistente diseñado para ayudar crear y enviar facturas de manera eficiente tienes que clasificar en una de las categorías principales que es o crear cliente o crear ítem o crear factura que vamos a ver que va a ser exactamente las mismas que están acá clientes facturas o items te voy a mostrar ahora cómo crear los clientes y crear las facturas pero si quisieras llevarla un paso más allá podríamos también crearlo y centralizar los items acá entonces dependiendo de la intención que tú tengas de si quieres crear un cliente o quieres crear una factura va a reconocer y va a mandar cierta Data específica que te va a pedir Así que vamos a copiar todo lo que está acá y lo vamos a pegar acá después de que lo copiemos y lo peguemos tenemos que ejecutar lo que se llama una acción Si vemos acá tenemos tres acciones principales que es crear ítem crear factura y crear cliente y todo eso vamos a mandarle la señal directamente a este webhook que acabamos de crear Entonces cuando chat gbt reconozca alguna de estas tres intenciones que es o crear un cliente o crear un ítem o crear una factura va a desencadenar lo que se llama una acción y la acción que está acá va a ser directamente este prompt que te dejé acá o este código Jason que te dejé acá que lo vamos a copiar y lo vamos a pegar y se va a ver algo así abajo en políticas de privacidad Le vamos a poner este link que está acá que lo puedes encontrar buscando make privacy policy le das a enter y copias el privacy notice que aparece acá que está acá luego le d a dar a crear si quieres solamente tú tener acceso le pones a un limit y si quieres que toda persona con el link tenga acceso le pones cualquiera con el link Entonces el gpt ya está creado pero no está mandándole la información al webhook del escenario que acabamos de crear específicamente así que tenemos que modificar directamente eso vamos a entrar acá y vamos a copiar este webhook que aparece aquí para editar el gpt nos vamos a ir a my gpt y vamos a apretar esta versión que aparece acá edit gpt dentro de las acciones vamos a modificarle Hacia dónde queremos mandar la información entonces lo que acabamos de copiar es esto de acá que es esto de exactamente aquí la parte de la izquierda tendrás que copiarla y tendrás que reemplazarla aquí la vas a copiar y la vas a pegar y le eliminas La Barrita después la parte de la izquierda es el id específico del webhook es decir todo lo que está desde La Barrita hacia la derecha que vendría siendo esto de acá y esto lo vas a reemplazar directamente en el path en esta parte que aparece acá lo vas a copiar y lo vas a pegar acá y ahí lo que acabamos de hacer es reemplazar en este mismo prom hacia donde vamos a mandar la información okay Y ahora sí le podemos dar a actualizar ahora si por alguna razón quieres hacerle una modificación en específica a esta parte que está acá es decir quieres agregarle un nuevo campo como el número de teléfono por ejemplo puedes irte acá y te deje un gpt que te cumple Exactamente esa función que es este gpt que aparece acá y le puedes decir algo por el estilo de copiar todo esto y decirle en crear cliente Verdad que es la primera función que nosotros vamos a ver Necesito que pidas un campo más como Data estructurada que es teléfono le voy a poner aplícalo en la misma jerarquía y adáptate el open Ai schema Entonces le voy a dar enter y esto es lo lindo porque nosotros no tenemos que realmente programar nada entonces aquí podemos ver que efectivamente si empezamos a bajar me va a crear un nuevo campo que es número de teléfono del cliente y si es que yo copiara este campo que aparece acá y lo pegara acá me empezaría a hacer el cambio y después le pediría directamente que ahora adáptate el System prompt del gpt personalizado para que me incluya el número de teléfono en crear cliente y Le copio y le pego el System prompt que son las instrucciones que va a cumplir el gpt y después haría Exactamente lo mismo copiaría este código que está acá Una vez que se termine y después lo pegaría directamente acá y listo el gpt personalizado ya está creado de hecho si me voy acá me voy a my gbts y voy al asistente de facturas ya podemos empezar a pedirle los datos por ejemplo digámosle que quiero crear un cliente le doy a enter y después me va a pedir todos los datos de El cliente el nombre del cliente la cle la ciudad le voy a decir invéntale los por fines prácticos pero aquí nosotros podríamos mandarle directamente en el audio y después me confirma si es que está correcto le voy a decir sí está correcto aquí podemos ver que quiere ejecutar una acción y lo que quiere hacer es hablar con el webhook que está directamente en make ahora si es que yo le doy a guardar Y le doy a correr el escenario y le pongo confirmar podemos ver que acabamos de recibir directamente la función de crear cliente Carlos García venida a las flores Ciudad de México etcétera Okay entonces ya recibimos la información directamente en make ahora tenemos que pensarlo lógicamente teníamos la opción de crear cliente o de crear factura para este caso Comencemos con la rama de crear cliente vamos a agregar un nuevo módulo y vamos a elegir el módulo de router esto nos permite verificar si es que es crear clientes que se vaya para arriba y si es que es crear factura que se vaya para abajo vamos a irnos acá y tenemos que adaptar verdad y sincronizar directamente esta base de clientes tú puedes crear tu propio Google sheets por ejemplo si te vas acá y le pones nueva hoja de cálculo y aquí le pones todos los datos que quieres como no cliente ciudad calle etcétera y que se vaya rellenando para abajo Por fin es prácticos también te lo dejé directamente acá que si nos vamos al link de sheets puedes irte a archivo y crear una copia lo voy a poner facturas automáticas versión 3 y le puedo ir a crear una copia para este caso voy a eliminar todo voy a irme a las facturas voy a eliminar todo voy a irme a los ems Y también voy a eliminar todo y ahora sí tenemos facturas automáticas versión 3 y lo que tenemos que hacer en este caso es agregar una nueva fila verdad porque si vimos la información acá y necesitamos crear el cliente Porque después tenemos que sacar los datos de este cliente para poder emitirla la factura Porque necesitamos sus datos entonces voy a irme acá voy a irme a Google sheets y voy a ponerle agregar una fila o add Arrow vamos a elegir el spreadsheet ID y vamos a buscar facturas automáticas versión 3 dentro de las hojas tenemos tres hojas que son estas que están aquí abajito clientes facturas o ems y como vamos a crear un nuevo cliente quiero ponerlo en cliente en el nombre que Quiero poner el nombre del cliente Carlos García en calle Quiero poner la calle en la ciudad vamos a poner la ciudad en el país vamos a poner el país y en el mail vamos a poner el email en el estado quiero que sea creado porque acabamos de crear el cliente le voy a dar a okay Ahora qué pasa si es que le doy a correr una automatización primero va a correr para arriba y después va a correr para abajo pero yo no quiero que me cree un nuevo cliente Si es que vamos a crear una factura para un cliente ya existente entonces aquí es donde entran los famosos filtros Okay los filtros van a decidir si es que yo me voy para arriba o me voy para abajo si es que se cumplen ciertas condiciones entonces voy a hacer clic acá voy a ponerle crear un filtro y le voy a poner acá si es crear cliente quiero que pase por acá y el otro es si es crear factura recuerda acá que lo clasificamos como crear cliente se va para arriba y si es crear factura se va a ir para abajo entonces nuevamente Si es crear cliente es decir si crear cliente es igual indiferente de la mayúscula o minúscula a crear y un bajo cliente Okay te vas a ir para arriba si es que es el otro que era crear factura si es crear factura que la clasificación es crear factura es igual a crear factura se va a ir para abajo entonces en este caso como recibimos que es crear cliente se va a ir directamente a crear cliente verdad pero no va a pasar por la línea de abajo porque crear cliente no es igual a crear factura no sé si se entiende la lógica de todas maneras si es que quieres entender un poquito mejor toda la parte de los filtros dentro de la comunidad de imperio digital en el classroom tenemos un curso que se llama make desde cero y aquí cubrimos todos los conceptos básicos para crear flujos de automatizaciones que son guiados por Fran nuestro experto en automatizaciones y aquí tenemos justamente un módulo específico de los filtros y condiciones que te pueden ayudar a entender bastante mejor cómo funciona y cómo creamos estos flujos de trabajo automatizados okay Pero ahora sí Entonces si es que ahora guardo el escenario le pongo un nombre factura automática versión 3 vuelvo a guardar Y le doy a correr puedo decirle a charg bt vuelve a crearme el mismo cliente Mira Me dice no es posible crear un cliente duplicado le voy a decir Envíame los datos de nuevo aquí está ejecutando la acción vamos a confirmar y ahora podemos ver que acabamos de recibir el cliente verdad crear cliente Carlos García etcétera Y si nos vamos a nuestra base de datos podemos ver que el nombre Carlos García Ciudad de México México mail ya está creado Okay entonces una vez que ya creamos este sistema tenemos que pasar a la segunda opción verdad Porque si en este momento yo le digo a charg PT Oye créame una factura chat gbt lo que va a hacer es perfecto Te voy a mandar los datos de la creación de factura te voy a pedir todas las cosas pero no sé qué hacer después de hecho hagamos la prueba si es que yo me voy acá supongamos que me voy a un nuevo chat de dentro del mismo asistente le digo créame una factura para Carlos García de una manzana a 790 que vence mañana me va a crear directamente los datos venta de manzana una precio etcétera mandar la información Sí y si es que le voy a correr la automatización acá y decido mandarle los datos efectivamente vamos a ver que recibimos todos los datos verdad el nombre del cliente venta de manzanas manzana precio y se fue para abajo y no se F fue para arriba porque identificó que era crear factura Y no era crear cliente Okay ahora si queremos crear una factura Necesitamos saber los datos del cliente verdad y Aquí vamos a usar una función que se llama Search Rose es una función de Google sheet que nos permite entrelazar distintos o distintas hojas o distintos sheets o bases de datos entonces lo que queremos hacer acá es queremos reemplazar toda esta base de datos directamente pero la queremos reemplazar con la información que está en esta otra base de datos ya entonces si es que nos vamos acá y nos vamos a Google sheets vamos a encontrar la función de Search Row es decir Buscar filas vamos a elegir el spreadsheet ID que es directamente la misma que estamos trabajando y vamos a elegir la parte de clientes lo que estamos haciendo acá es estamos extrayendo la información de un cliente en específico si bajamos acá podemos poner que el nombre sea igual a el nombre que acabamos de mandar entonces solamente va a sacar el nombre o los datos de esa fila en específico en este caso de cuánto es el límite que nosotros queremos como se lo estamos creando un cliente le voy a poner uno y ahora sí si es que le doy a guardar y a correr automatización nuevamente entro acá y le digo vuelve a enviar los datos que son los datos de crear factura vamos a confirmar y vamos a ver que recibimos la información y acabamos de buscar los Rose ya es decir extraemos la información de facturación que es el nombre la calle de la ciudad del país etcétera Okay entonces voy a ir nombrando esto y esto va a ser acá el nombre arriba es directamente crear cliente verdad y aquí es Buscar cliente y le doy a Okay el siguiente paso que tenemos que hacer es actualizar en esta planilla que aparece acá de facturas los datos de la factura verdad Porque queremos en un lugar centralizar toda la información que vamos mandando Entonces vamos a ponerle nuevamente agregar una nueva fila para esta nueva factura que vamos a emitir vamos a elegir nuevamente el spreadsheet ID facturas automáticas Pero esta vez lo queremos incluir en facturas esta parte es si es que contiene encabezados la respuesta es Sí y Aquí vamos a poner el nombre verdad o el número perdón de la factura aquí podemos crear distintos sistemas para tener nuestra propia facturación pero a mí me gusta crear esta opción que se llama timestamp Por qué Porque nunca van a ver dos timestamp distintos en distintas ocasiones para que se hagan una idea es un par parámetro que cada vez que pasa un segundo se va creando un nuevo número y se va sumando un nuevo número desde 1970 entonces en 1970 el timestamp debe haber sido no sé 60 Segundos desde el primer minuto pero hoy día Ya estamos por los números super super grande en resumen es una métrica que me gusta usar a mí en este tipo de ocasiones Okay después en la fecha de Misión lo que vamos a hacer es vamos a empezar a reemplazar ciertas variables con la información que ya recibimos verdad la fecha de emisión es la fecha que mandamos directamente desde el webhook verdad que la recibimos acá que es la fecha actual y la vamos a reemplazar acá vamos a bajar y vamos a poner fecha actual en cliente Cuál es el cliente que vamos a trabajar con si subimos tenemos la información del cliente la calle la ciudad etcétera la fecha de vencimiento es cuando vence la factura verdad que Esto va a ser la fecha de entrega en este caso puede ser fecha de entrega puede ser fecha de vencimiento absolutamente como quieras Recuerda que esta plantilla la puedes personalizar a tu gusto la descripción voy a poner la descripción del proyecto que es la venta de una manzana y vamos a empezar a reemplazar las variables verdad cantidad Cuál es la cantidad del primer ítem cantidad Uno cuál es el ítem manzana Cuál es el precio 790 vamos a hacer lo mismo en el dos cantidad dos nombre em dos precio em dos después en el tres cantidad 3 precio 3 nombre item tres y precio tres después cantidad cuatro nombre item cuatro y precio de cuatro después cantidad cinco precio cinco y nombre ítem 5co y finalmente cantidad 6 precio 6 y nombre ítem 6 y esta parte es super interesante porque podemos empezar a hacer ecuaciones matemáticas okay Si queremos calcular el total necesitamos multiplicar todos los ítems Entonces nos vamos a ir acá y vamos a ponerle cantidad uno vamos a buscar acá vamos a poner por y le vamos a poner precio uno verdad que tenemos que hacer después sumar y nos vamos a hacer lo mismo con la cantidad dos esto lo voy a copiar por precio 2 más cantidad 3 por precio 3 más y así sucesivamente cantidad uno por precio 1 más cantidad 2 por precio 2 más cantidad 3 por precio tres y así sucesivamente esta planilla que armamos funciona hasta seis ems pero si quisiéramos podríamos extenderla hasta la cantidad que queramos ya recordemos que yo les estoy enseñando la base pero después la podemos personalizar absolutamente como queramos Y por qué es lindo paréntesis todo esto también porque las automatizaciones siento que las armamos porque estamos buscando ahorrar tiempo verdad ahorrar tiempo para hacer las cosas que realmente nos gustan hacer o sea no creo que tenemos que automatizar todo en nuestra vida sino que tenemos que automatizar el proceso y las tareas tediosas que nos toman más tiempo verdad si yo disfruto hacer un actividad no tengo por qué automatizar esa actividad puedo hacerla y puedo disfrutarla pero si es que no disfruto el crear una boleta o emitir una boleta o enviar las boletas o la facturación etcétera crear este tipo de sistemas realmente ayudan sea porque los quieres implementar en tu negocio porque los quieres vender y creo que ese es el propósito también que tenemos en imperio digital poder ahorrar tiempo para tener tiempo para hacer las cosas que realmente nos gustan Okay ahora sí si es que volvemos acá vamos a ver que tenemos todo y después le vamos a dar a Okay ya y esto de acá va a ser el nombre le voy a poner agregar a sheets factura le voy a dar OK le voy a dar a guardar y vamos a ver si es que está todo funcionando Okay nuevamente Volveré acá y le diré vuelve a enviar los datos recordemos que estamos mandando estos datos que están acá si le doy a confirmar va a empezar a correr por acá como es crear factura se va a ir por abajo va a actualizar esto y podemos ver que tenemos la descripción etcétera etcétera etcétera etcétera Y tenemos el total acá paréntesis esta fecha de Misión debería aparecern como fecha ahí Sí por eso no nos está apareciendo y nos esta saliendo de otra manera era porque no esta bien puesta la tabla okay Así que acá formato número y nos vamos a ir a fecha y puedes poner el formato que más te acomode Ahora sí podemos ver que efectivamente lo está haciendo acá Cuál es el siguiente paso necesitamos crear el documento ya necesitamos crear la factura Y si bien recuerdas yo te dejé una plantilla creada acá Tú la puedes adaptar como quieras esta plantilla Lo lindo de esta plantilla es que tú puedes subir cualquier docs cualquier cosa y si es que pones las cosas entre estos corchetes que aparecen acá lo va a tomar como variables directamente en el json entonces van a ser distintas variables que podemos ir reemplazando por ejemplo el ítem uno que en este caso era manzana con el precio unitario van a ser directamente variables esta plantilla que está acá también te la dejé acá la puedes descargar como documento acá o puedes irte a justamente acá se te va a abrir esto te vas a archivo y le das a crear una copia y la guardas ya Entonces tenemos esto acá Aquí también tú puedes cambiar estas cosas que ya están por default si le haces doble clic acá puedes guardarlo y cambiarlo como quieras en fin esta plantilla la creé para que la uses y la modifiques absolutamente como quieras por ejemplo acá ni siquiera la actualicé los términos y condiciones Pero esto es lo importante dentro de la plantilla tenemos nombre calle ciudad país y esto se va a rellenar con los datos de El cliente verdad estos que están acá Así que si volvemos acá y nos vamos al make Podemos agregar el nuevo módulo que es crear un documento Entonces vamos a buscar acá vamos a abrir Google docs y vamos a poner create a document from a template crear una plantilla desde un documento vamos a ir acá y vamos a buscar el document id para este caso es el que tú duplicase que es factura de plantilla y acá podemos ver que están todos los valores que podemos reemplazar por ejemplo factura número que es el valor que aparece acá factura número eh ítem uno nombre verdad es ítem uno nombre que está acá y en fin y Aquí vamos a empezar a reemplazarlos la factura número aquí partirían rellenando el ítem uno nombre verdad que serían todas estas cosas de acá nombre ítem así que tenemos que rellenar directamente los datos del documento que estamos creando Y si bien podríamos elegir acá directamente el timestamp va a pasar algo si es que pasa más de un segundo entre que agrega los datos de la factura y crea el documento el timestamp va a ser distinto Así que si bien Esto podría funcionar también podría causarnos problemas así que lo que vamos a hacer es vamos a volver atrás y vamos a agregar un paso justo antes voy a correr esto directamente para los lados y voy a darle a desconectar una vez que estemos acá vamos a crear una nueva variable y esto también le puede servir mucho en sus automatizaciones y la variable va a ser literalmente el número de la factura Así que vamos a irnos a Tools y vamos a poner set variable la variable va a ser número de factura verdad y el valor de la variable va a ser el timestamp Así que nos vamos a ir acá en el calendario y vamos a poner el timestamp Ahora sí podremos trabajar con esta variable en futuros pasos la vamos a conectar y acá en vez de ponerle el timestamp Vamos a ponerle el número de factura le vamos a dar okay Y ahora sí podemos Volver al Google docs y podemos seleccionar el número de factura vamos a volver a seleccionar el documento y vamos a elegir factura plantilla vamos a irnos al número de factura y vamos a poner el número de factura Y ahora sí podemos empezar a rellenar el resto de los datos por ejemplo la fecha de hoy que es la fecha actual la fecha de vencimiento la fecha de entrega el item uno va a ser manzana Aquí también te dejé uno que es la descripción por si es que quisieras agregarle una descripción personalizada que también se la puedes mandar a chat gbt pero para este caso le voy a poner el mismo nombre del ítem después la cantidad uno y el precio uno para el ítem uno total vamos a hacer la cantidad del ítem uno por el precio del ítem uno verdad y vamos a hacer exactamente lo mismo para el resto recordemos que estas variables que estamos rellenando acá son las variables que vamos a rellenar de la factura Entonces en este caso el ítem uno nombre ítem cantidad y todo esto ítem uno total es todo lo que acabamos de rellenar Así que Volveré acá y vamos a seguir vamos a poner el nombre del ítem dos en la descripción Vamos a ponerle nuevamente el nombre en la cantidad Vamos a ponerle cantidad del item do en el precio de el ítem dos vamos a ponerle el precio del dos y el total del ítem dos va a ser cantidad 2 por precio 2 recordemos nuevamente las funciones tenemos que ponerle la función de acá de multiplicación porque si no no lo va a tomar vamos a hacer exactamente lo mismo con el ítem 3 nombre ítem 3 cantidad ítem 3 precio ítem 3 cantidad por precio lo mismo con el ítem 4 lo mismo con el ítem 5 cantidad ítem 5 precio ítem 5 cantidad C por precio cco y finalmente lo mismo con el ítem seis nombre ítem seis cantidad del ítem seis precio del ítem seis y cantidad por precio después la factura del total va a tener que ser literalmente la misma que creamos antes verdad que en vez de tener que ir a buscarlo atrás simplemente podemos darle un título rápidamente como factura Y el número de la factura buscarle una nueva ubicación que en este caso va a ser alguna carpeta de Drive si es que nosotros entramos aquí al Drive podemos irnos a nuestra unidad a crear una nueva carpeta y le puedo poner facturas versión 3 y este es el lugar donde se van a guardar directamente todas las facturas irnos acá si no te aparece puedes apretar este icono que aparece acá para actualizar y elegimos las facturas versión 3 le damos okay Y ahora sí antes de seguir rellenando todo recordemos que teníamos la parte que sale factura total pero esa multiplicación ya la hicimos anteriormente en la parte de acá de agregar a sheets Entonces yo puedo bajar puedo copiar todo esto darle Okay volver acá y directamente pegar la facturación total acá que sería la cantidad uno por el precio uno cantidad dos por el precio de dos y todo esto sumado en nombre vamos a bajar y vamos a sacar los datos que extraí o que logramos extraer anteriormente acá en la parte de Buscar cliente Así que si me voy a la derecha vamos a tener el nombre la calle la ciudad el país y el email ahora sí le puedo dar a OK recordemos Que todas estas cosas que rellenamos son directamente las cosas que estn acá verdad nombre calle ciudad país para que se genere en el nuevo documento Así que este módulo que acabamos de crear es crear factura le voy a dar okay Y si es que ahora corremos esta automatización le voy a dar a guardar le voy a dar a correr y hacemos la prueba me debería generar directamente Una factura y guardarla en esta carpeta de Drive que está acá Así que hagamos la prueba créame una factura para Carlos García de la venta de dos manzanas y tres peras a 590 y 750 respectivamente le voy a dar a subir y ahora debería empezar a mandarnos la información una vez que le confirmemos vamos a leer esto vamos a verificar que efectivamente está bien y le voy a decir sí confirmo va a empezar a ejecutar la acción y va a confirmar ahora debería empezar a crear directamente esto y nos debería empezar a crear la factura si es que vemos a acá efectivamente nos acaba de crear la segunda factura es decir actualizó todo lo que está acá y nos creó la factura Ahora sí es que abrimos el Drive vamos a ver que la va a haber creado y aparece justamente aquí okay Ahora el paso siguiente que queremos hacer es no le queremos mandar la factura directamente en un Drive verdad O si quisiéramos mandarla por mail o si quisiéramos hacer cualquier cosa necesitamos trabajarlo en un formato más cómodo Así que lo que vamos a hacer es vamos a descargarla como PDF vamos a abrir un una nueva parte que sale Google docs y vamos a buscar acá descargar un documento o Download a document en el document ID lo que tenemos que hacer es tenemos que poner directamente el documento que nos aparece aquí que es este que está acá que está en el output bundle y document ID Así que vamos a descargar exactamente este documento y le vamos a dar a map y vamos a seleccionar la variable para este caso es el primero que aparece acá que es document ID después vamos a elegir el formato y Me acomoda trabajarlo en PDF y le voy a dar a Okay este de acá transforma a PDF y ahora sí vamos a estar descargando y teniendo los archivos directamente en PDF esta parte también es super interesante y les va a ayudar mucho en la organización y es que dónde queremos guardar esto verdad porque aquí tenemos una carpeta que sale facturas Pero yo lo que quiero hacer es quiero identificar si es que hay una carpeta creada con el nombre o si es que no hay una carpeta creada con el nombre y en función de eso quiero que okay cree una nueva carpeta o me lo guarde en alguna carpeta de El cliente Esto es para que podamos ir centralizando en un mismo lugar todas las facturas que le emitimos al mismo cliente Okay y lo que vamos a hacer acá es primero vamos a buscar en Drive si es que existe una carpeta así entonces vamos a buscar acá en Drive vamos a poner Buscar más y vamos a buscar la opción de Search files and folders es decir Buscar carpetas o archivos dónde es que queremos Buscar Esto bueno en la carpeta que acabamos de crear que es versión 3 en retrieve lo que queremos Buscar es si existe la carpeta verdad Así que vamos a elegir folders y vamos a buscar entre los nombres de las carpetas y los archivos Cuál es la carpeta que estamos buscando Bueno vamos a buscar exactamente la carpeta con el nombre del cliente y el nombre lo tenemos en varios lugares para este caso voy a elegir el nombre que está acá en Buscar cliente Quiero buscar un nombre que contenga el nombre y en el límite va a ser un máximo resultado okay Okay entonces esto que está acá es Buscar carpeta y después tenemos dos rutas la primera es si es que no existe una carpeta con el nombre del cliente Quiero crear una nueva carpeta y guardarla acá la segunda ruta alternativa es si es que existe una carpeta con el nombre del cliente quiero meter este mismo archivo A esa carpeta Entonces vamos a usar el famoso router que nos separa la ruta y la automatización en dos caminos partamos con el primero Quiero crear una carpeta en el caso de que no exista Okay entonces dónde Quiero crear la carpeta acá en facturas versión 3 cómo quiero que se llame la carpeta Ah el nombre del cliente verdad y le voy a dar a okay Y esto que está acá es crear carpeta cliente y después la ruta alternativa es si es que ya existe la carpeta la encontramos acá donde sale Buscar carpeta verdad entonces lo que quiero hacer es subir el archivo a la carpeta que ya existe Cuál es la carpeta que ya existe Ah sí el folder ID o el file ID que es el que encontramos directamente aquí verdad Y qué es lo que queremos subir a el documento el PDF que acabamos de crear Así que le voy a dar okay Y esto sería subir a carpeta existente Entonces tenemos la opción de crear una carpeta de cliente o subir una carpeta que ya existe pero si creamos la carpeta después lo que tenemos que hacer es subirla entonces me voy a ir acá y le voy a subir el archivo para este caso simplemente puedo clonar este archivo verdad y puedo tirarlo acá y reemplazar el parámetro a el último folder ID es decir al crear carpeta cliente y ponerle el folder ID le voy a dar Okay Y le voy a dar a guardar Ahora nos estamos enfrentando la situación de que tenemos que aplicar un filtro Por qué Porque necesitamos verificar si es que la carpeta no existe que se vaya por arriba y si la carpeta existe que se vaya por abajo entonces lo que voy a hacer acá es directamente desconectar esto voy a guardar y voy a correr la automatización una vez por qué corremos la automatización Porque necesitamos muchas veces que nos den los parámetros por ejemplo de El Buscar carpeta en este caso necesitamos los parámetros para poder trabajar con ellos así que correré la automatización y le voy a decir vuelve a crearlo y nos va a mandar nuevamente la misma opción de Carlos García vamos a confirmarlo y podemos ver que está ejecutándose toda la automatización no está creando la factura en documento la está transformando a PDF y aquí me dio Carlos García Ahora sí puedo volver a conectarlo y puedo empezar a crear los condicionales el primero es si es que la carpeta no existe quiero crearla así que nos vamos a ir acá vamos a crear un filtro y voy a ponerle si carpeta no existe verdad que esto sería si es que el nombre de la carpeta en este caso está vacío es igual a no existe pasa para arriba y después el segundo caso sería si carpeta existe Es decir que el nombre es igual a indiferente de mayúscula o minúscula el nombre del cliente queremos que suba a la carpeta existente Verdad que es esta carpeta que generamos anteriormente ahora sí le puedo dar Okay le puedo dar a guardar y vamos a abrir la carpeta nuevamente vamos a irnos a facturas B3 Y si le doy a correr a la automatización y empiezo a vuelve a enviarlo Y le doy a confirmar a la automatización vamos a ver que se empieza a ejecutar por dónde debería irse si es que la carpeta no existe bueno debería irse por arriba y efectivamente me acaba de crear la carpeta y debería habérmelo subido y si es que abro ahora la carpeta que está acá Carlos García vamos a ver que ahí está la factura número X por el total de 3430 bla bla bla bla Ahora qué pasa si vuelvo a correr la automatización se debería ir por arriba o por abajo veamos vamos a guardar voy a darle nuevamente a correr y le voy a decir ahora vuelve a crearlo pero agrégale una sandía a $1,000 vamos a generar la nueva estructura vamos a confirmar lo vamos a leer Está correcto Sí vamos a darle a confirmar y podemos ver que en este momento me está mandando la nueva señal pero le agregó una sandía Entonces ahora está creando la factura está transformándolo PDF buscó la carpeta y ahora se fue por abajo verdad por qué Porque buscó la carpeta y vio que la carpeta de Carlos García que está acá ya existía Por ende si es que la carpeta ya existe la vamos a subir a la carpeta que ya existe verdad si es que abrimos aquí la factura podemos ver que está la nueva cotización digamos o la nueva factura con la sandía incluida y aquí ya las opciones son Realmente infinitas O sea si quieres puedes mandártelo a ti directamente para que tú lo revises y después lo mandes o puedes crear algún condicional para apretar un botón en Excel y ponerle lo Acabo de revisar me gustó Mándalo pero por fines prácticos lo que vamos a hacer es vamos a mandarlo por correo electrónico okay Así que nos vamos a ir acá vamos a buscar Outlook o Gmail o el que sea que uses vamos a crear y enviar un mensaje y en el sujeto le voy a poner factura número y voy a ponerle el número de la factura le voy a poner Aquí está tu factura Carlos García con vencimiento del fecha da igual en Quién lo va a recibir vamos a poner y vamos a bajar y vamos a poner el campo de el email verdad que lo conseguimos acá previamente cuando hicimos la función de Search Rose en el nombre le voy a poner nombre y si quisiera agregarme a mí como con copia porque yo quiero estar al tanto o Quiero agregar a mi contador o Quiero agregar absolutamente a cualquier persona también lo voy a hacer por ejemplo yo voy a poner uno de los correos que tengo y quiero recibirlo directamente yo con copia vamos a bajar y en el attachment Vamos a ponerle el PDF que acabamos de crear le voy a dar a Okay voy a poner enviar mail por ejemplo y voy a clonarlo y lo voy a subir acá ahora le daré a Okay guardar y voy a a auto alinear completamente la automatización de nuevo y vamos a correrlo una vez más a ver si es que esto está funcionando créame una nueva factura para Carlos García pero de un Iphone a 790,000 voy a generar la nueva factura aquí lo que está haciendo está mandando la Data Entonces al final lo único que tenemos que hacer es verificar si es que esto está correcto que debería estar correcto y lo voy a poner sí está comenzando a ejecutar la acción y lo Confirmamos una vez que estemos acá se va a empezar a armar toda la automatización nuevamente está creando la factura está transformándolo un PDF está subiéndolo a la carpeta y después está enviándolo al mail se envió al mail Carlos García verdad y me lo envió con copia a uno de mis correos y si es que yo entro acá me acaba de librar el celular por lo que significa que me llegó factura bla bla bla bla bla Aquí está tu factura Y esta es la copia que me llegó tenemos el total Tenemos aquí los datos del destinatario y en fin desde aquí las opciones son Realmente infinita o sea podemos armar no sé alguna automatización para que cada los días 4 de octubre se mande la misma facturación a no sé qué etcétera podemos hacer muchas muchas cosas desde acá Esto está recién comenzando si quisiéramos podríamos extraer verdad los datos agregarle esta columna de ítems y pedirle que extraiga los datos de ciertos ítems en específico e podemos hacer muchas cosas y esto es recién el inicio o sea el potencial que tiene esta automatización de ser vendida a distintos clientes o a distintas personas personas o directamente implementada en tu línea de negocio es altísima altísima porque no sé por ejemplo esta misma automatización en vez de hablar por chat gpt yo puedo conectar a un celular de WhatsApp para decir Oye voy a mandar un audio transcríbelo la señora que tiene un minimarket que quiere hacer una boleta a X cuál es el canal que más usa es directamente WhatsApp Entonces qué pasa si es que este webhook verdad lo recibimos desde una señal de WhatsApp No desde charg bt verdad o lo interpretamos con Inteligencia artificial las opciones son Realmente infinitas ya bueno en el fondo quiero que sepan que esta solución No la van a encontrar en ningún otro lado verdad porque nosotros somos capaces de crear y la idea también de enseñar automatizaciones y de empezar a automatizar es que podamos empezar a crear este tipo de automatizaciones personalizadas hechas a la medida de la persona y que podamos vendérselas a gente para que ellas o ellos puedan empezar a ahorrar tiempo o para que tú puedas empezar a ahorrar tiempo y para que todos en el fondo empecemos a ganar Okay también demás está decir que bueno esta automatización te la voy a dejar directamente publicada acá si es que entras al classroom dentro de imperio digital vas a encontrarte con muchas ventanas como estas tenemos cursos tenemos grabaciones de las sesiones en vivo pero si te vas aquí a las automatizaciones vas a encontrar un a automatización que se llama facturación automática que es donde te dejé todos los prompts directamente publicados y todos los recursos que vamos a usar Recuerda que puedes apretar este botón de acá el Jason puedes darle a descargar y si es que te vas a crear un nuevo escenario es decir te vienes acá y le das a crear nuevo escenario puedes apretar los tres puntitos e importar la plantilla le das a guardar y se te va a abrir absolutamente todo lo que hicimos Qué es lo único que tendrías que hacer Tienes que venirte Acá tienes que irte al webhook tienes tienes que agregar un nuevo webhook verdad crear un nuevo webhook y este es el que reemplazas en el open Ai schema que hicimos anteriormente luego sincronizas tu propia base de datos reemplazas las variables y le vinculas tus propias cuentas y listo esta automatización está corriendo pero deja le quiero hacer un cambio porque quiero agregarle eh No sé que le pida el teléfono o Quiero agregarle la parte de un nuevo em Bueno también puedes hacer eso directamente acá sin necesidad de codificar nada porque aquí tenemos un custom gpt que le podemos ir pidiendo variaciones del Jason que está en el open skema y sé que quizás no entendiste mucho esas palabras o que puede sonar un poco complicado pero es realmente más fácil de lo que crees Por qué Porque este código que está acá que es la acción que nosotros ejecutamos puedes llegar y decirle algo tan simple como Oye Necesito mandar una nueva Data y que me pidas una nueva Data directamente en chat gpt que es el teléfono verdad o la comuna o no sé lo que quieras o si quieres crear un nuevo em verdad o quieres crear una nueva acción puedes irte acá y puedes ponerle Esta es la acción de crear ítem verdad le pones las condiciones y el crear ítem por ejemplo es agregar una nueva fila directamente en el spreadsheet ID de facturas automáticas y ponerle ems verdad entonces aquí nos va a ir creando y el ítem que vamos recibiendo es cuando recibimos la información desde el gatillador instantáneo y después podemos hacer que ya no tenemos que darle necesariamente los precios de cada producto sino que puede cada producto tener una descripción y tener un precio y que esté asociado aquí en la ventana o en la plantilla de los ítems Así que podríamos hacer todo el proceso de facturación mucho más personalizado Así que si eres de esas personas que te interesa aprender a automatizar o quieres crear este tipo de soluciones recomiendo que entres a probar imperio digital hoy día tenemos la opción de 7 días completamente gratis para que entres a probar el link está en la descripción y si sientes que no es para ti no tienes que pagar absolutamente nada si es que cancelas antes del día 7 incluso puedes entrar en peri digital descargarte la plantilla empezar a usarla y después decides si te quedas porque vas a ahorrar bastante tiempo pero también siento que es importante que entendamos lo que estamos haciendo porque claro yo te podría dar todas las plantillas y podría decirte Oye importa esto haz esto haz esto haz esto pero si es que no te muestro el proceso de cómo lo estamos haciendo realmente las opciones a personalizarlo más a tu medida son Realmente bajas y si quieres aprender también un poco más acerca de Cómo podemos hablar con este gpt y Cómo podemos pedirle literalmente lo que queramos a char gpt tenemos este video que se llama automatiza tareas desde char gpt y la razón por la que lo cubrí tan rápido es porque te dejo todo explicado aquí con una guía Cómo es el proceso de mandar la información directamente a char gbt este video también lo puedes encontrar en YouTube y se llama conecta todo a chat gpt también mencionarte que tenemos clases en vivo Todas las semanas con Fran nuestro experto en automatizaciones dos veces a la semana semana por medio también hay clases conmigo y que puedes publicar absolutamente cualquier tipo de duda dentro de imperio digital Así que sí ahora sin más que decir Espero que esta automatización que esté acá la puedas armar la puedas modificar y puedas sacarle realmente el máximo provecho porque recordemos las automatizaciones no las tenemos y no las hacemos Porque queremos ahorrar tiempo en todo nosotros tenemos que automatizar las cosas que no realmente nos gustan hacer o las cosas que no nos gustan tanto hacer Mejor dicho para qué Para que tengamos el tiempo de hacer las cosas que nos gustan hacer y automatizar las cosas que no nos gustan hacer y esa es nuestra meta dentro del imperio digital Ahora sí sin más que decir te deseo mucho éxito y recomiendo también que veas alguno de los otros videos feliz [Música] automatización i
