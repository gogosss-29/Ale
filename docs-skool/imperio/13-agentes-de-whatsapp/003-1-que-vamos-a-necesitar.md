# 🧩 1. Qué vamos a necesitar?

> Ruta: Agentes de WhatsApp › 🧩 1. Qué vamos a necesitar?

**🎬 Vídeo (3.3 min):** https://www.loom.com/share/4c4c3a0d91da48c4b9d95e5a3039c4ad

---

> NOTA: Si NO has instalado n8n, puedes hacerlo siguiendo el tutorial de [aquí](https://www.skool.com/imperio-digital/classroom/8e2ffdbc?md=2606db521b014a3e8034d5a992dbb6b3)[.](https://www.skool.com/imperio-digital/classroom/d32f4fc7?md=6a3fb77e9ac943418699065623a6ba15)

En este módulo revisamos las tres piezas que necesitas para que tu agente de IA funcione en WhatsApp. Todo es simple y modular. Lo único que usamos es:

1. **n8n (el cerebro)**  
Aquí se procesa todo: los mensajes, la lógica y la llamada a la IA. Puedes usarlo en tu propio servidor o en su versión cloud (ambas funcionan igual).
2. **Airtable (la memoria)**  
Es donde vamos a guardar una base de datos muy simple con la información de cada usuario y sus mensajes. Con el plan gratuito basta.
3. **Evolution (el puente hacia WhatsApp)**  
Es lo que conecta tu número de WhatsApp Business con n8n. Puedes instalarlo en tu servidor o usarlo en la versión cloud.

También explicamos, de forma rápida, cómo funciona la plantilla completa:  
Los mensajes que llegan por WhatsApp entran por un webhook, se agrupan unos segundos (para juntar mensajes seguidos), se procesan con un agente de IA (en este caso un consultor llamado Roberto) y luego se envía la respuesta de manera natural al usuario.

La idea de este módulo es que entiendas el paso a paso general antes de enchufar todo a tu propio número. En el siguiente video vemos exactamente cómo hacerlo.
