# 🚀 6. Prueba en vivo

> Ruta: Agentes de WhatsApp › 🚀 6. Prueba en vivo

**🎬 Vídeo (7.8 min):** https://www.loom.com/share/b0f217816566440ebcdd1c84e2c5c508

---

En este módulo probamos el agente en tiempo real para confirmar que todo el sistema está funcionando. Cargamos un usuario nuevo en Airtable, activamos el flujo en n8n y enviamos un mensaje desde otro número de WhatsApp para ver cómo responde el agente.

Vas a ver paso a paso cómo:

1. El mensaje entra por Evolution y llega al webhook.
2. n8n procesa la información, identifica al usuario y agrupa los mensajes si llegan seguidos.
3. El agente de IA analiza el contexto (en este caso un negocio real como una panadería) y comienza a responder de forma natural.
4. La conversación fluye, el agente recuerda lo que se dijo, hace preguntas y propone soluciones basadas en la información del usuario.

También mostramos qué ocurre si llega un mensaje de alguien que no está en la base (el sistema lo filtra de forma automática). Esto permite que el agente solo responda a usuarios habilitados.

Lo importante de este módulo es que ves todo funcionando en unos minutos. La lógica, la espera de mensajes, la memoria, las respuestas y la dinámica completa ya están listas. A partir de aquí puedes cambiar el “cerebro” del agente y adaptarlo a tu propio negocio o al de tus clientes sin modificar la estructura principal.
