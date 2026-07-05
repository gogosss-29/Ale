# 🗂️ 2. Crear base de Airtable

> Ruta: Agentes de WhatsApp › 🗂️ 2. Crear base de Airtable

**🎬 Vídeo (4.6 min):** https://www.loom.com/share/9e6e2ef73394421c8effce9ba95d997e

---

En este módulo armamos la base de datos que el agente necesita para funcionar. Lo hacemos desde cero, paso a paso, para que puedas replicarla sin complicación.

Creamos una base nueva en Airtable y añadimos dos tablas:

1. **clients (usuarios)**  
Aquí guardamos la información básica de cada persona que interactúa con tu agente (nombre, teléfono, estado activo o inactivo, descripción del negocio y posibles soluciones que la IA va generando).  
Cada campo se crea manualmente para que coincida exactamente con lo que el flujo necesita.
2. **messageBuffer (mensajes agrupados)**  
Esta tabla almacena los mensajes que llegan seguidos en pocos segundos (por ejemplo, cuando una persona envía tres o cuatro mensajes de corrido).  
Incluye un ID automático, la vinculación al usuario, el mensaje, la fecha de creación y el estado (recibido o procesado).

La idea de este módulo es que dejes lista la estructura que permite que tu agente recuerde quién es cada usuario y procese los mensajes en orden. Una vez creada esta base, ya puedes avanzar al siguiente paso.  
  
Plantilla: [https://airtable.com/appPB4o0PQvjgYCjp/shrLGFxAxDTxponVv](https://airtable.com/appPB4o0PQvjgYCjp/shrLGFxAxDTxponVv)

## 🎙️ Transcripción

Primero y principal, vamos a arrancar por tener, justamente, todo lo que necesitamos, que es, en un principio, esta base de Airtable. Vamos a crear una nueva base de Airtable cuando vamos a, por ejemplo, Airtable.com le van a dar a crear una nueva base, desde cero, en la en el workspace que tengan ustedes, crear una nueva base desde cero y acá vamos a poner ¡Hasta la próxima! dos tablas, una tabla va a ser messageBuffer y la otra tabla va va a ser clients. Ahora nosotros lo que tenemos que hacer es replicar específicamente todo esto, si? vamos a ir campo por campo lo voy a dejar acá en guardado para que puedan hacerlo luego en esta, no? que tiene esta descripción No les puedo compartir esto específicamente, así que lo van a tener que crear uno por uno. Primero, el primer campo de la tabla. tabla clients, tenemos que poner esta configuración con este nombre user-id, autonumber, después ¡Un beso! campo de texto, tienen que crear un nuevo campo, le ponen name, guardar, ¿cómo hacen para crear nuevos campos? van acá, ponen acá por ejemplo sería en este caso escriben pongo por ejemplo si yo quiero crear acá este campo que es name, name y single line text es el tipo, voy acá escribo single line text y acá le pongo name y así vamos creando todos los campos porque tiene que quedar, tiene que quedar igual a esto, tenemos este campo, el campo de phone que es de tipo numérico tipo número, nombre phone, status, que tenemos activo o inactivo porque este agente específicamente tenemos que cargarle usuarios, luego tenemos un campo de long text que es business description este campo que se hace automáticamente, luego tenemos un campo de fórmula que tenemos esto acá. y otro campo de posibles soluciones que nos va a llenar el agente de IE, que es lo mismo. Y por otro lado tenemos, tenemos la otra tabla que es bastante más simple, tenemos lo mismo ID con un autonumber, una vinculación acá que es tenemos que, que esto es un poquito, lleva un poquito más de tiempo hacerlo, son unos segundos más, que para poder hacerlo lo que tenemos que hacer es esperar. esto, vamos a ir acá, ponemos link to another record Lo conectamos a clientes, le ponemos User ID, a mi no me va a dejar entonces le tengo que poner 2 y acá apagamos. Hagamos esto y le ponemos skip y listo. Ya queda esta tabla, ahí se me creó un registro. borramos acá, borro este registro, seguimos con el resto de los campos, un campo de mensaje Un mensaje de long text, luego tenemos lo mismo el created time, de esta forma, un record ID que es exactamente lo igual y el status que el status de estos mensajes es diferente es recibido y procesado esto es una tabla para los mensajes fragmentados que nos mandan tres o cuatro mensajes en un par de segundos. Una vez que tenemos ya toda esta tabla, ya tenemos la base de RTT. para poder seguir con el resto de las cosas.
