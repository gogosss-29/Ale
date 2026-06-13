# 🔌 4. Conectar Evolution a N8N

> Ruta: Agentes de WhatsApp › 🔌 4. Conectar Evolution a N8N

**🎬 Vídeo (3.7 min):** https://www.loom.com/share/6bb46c79908c40a2bb11765b58b8d9a5

**📎 Recursos:**
- Agente Whatsapp n8n Imperio

---

En este módulo conectamos tu número de WhatsApp Business con n8n usando Evolution. Esta es la parte que permite que cada mensaje que recibas en WhatsApp llegue directamente al agente.

El proceso es simple:

1. Creamos una **nueva instancia en Evolution** (es donde se vincula tu número).
2. Abrimos WhatsApp Business en el celular y escaneamos el **código QR** que aparece en Evolution (esto conecta tu número a la plataforma).
3. Vamos a n8n, creamos un workflow nuevo y **importamos el archivo** que te damos en el curso.
4. Dentro del flujo, copiamos la URL del **webhook** y la pegamos en la sección de eventos de Evolution.
5. Activamos la opción para que todos los mensajes entrantes se envíen a ese webhook.

Con estos pasos, tu WhatsApp queda conectado a n8n y listo para que el agente reciba y procese mensajes de inmediato. Una vez configurado esto, pasamos al siguiente paso para enlazar Airtable.
