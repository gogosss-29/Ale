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
