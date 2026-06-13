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
