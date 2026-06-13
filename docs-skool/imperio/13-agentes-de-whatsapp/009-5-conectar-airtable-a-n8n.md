# 🔗 5. Conectar Airtable a N8N

> Ruta: Agentes de WhatsApp › 🔗 5. Conectar Airtable a N8N

**🎬 Vídeo (8.2 min):** https://www.loom.com/share/99ac500e0ab643b3bfe29afc14fe14ab

---

En este módulo conectamos Airtable con n8n para que el agente pueda leer y escribir información en tu base de datos. Esta conexión es clave, porque sin ella el agente no podría recordar usuarios, guardar mensajes ni mantener el contexto de la conversación.

El proceso es sencillo:

1. Creamos una **credencial OAuth** en Airtable (desde el Builder Hub).
2. Copiamos la URL de redirección que nos da n8n y la usamos para registrar la integración.
3. Generamos el client ID y el client secret, y los pegamos en n8n para completar la conexión.
4. Una vez creada la credencial, seleccionamos la base correcta y cada tabla en los nodos de Airtable dentro del flujo.
5. Revisamos que todos los nombres coincidan exactamente (si cambian los nombres de tablas o campos, el flujo no funciona).

Con esto, Airtable queda completamente sincronizado con n8n y con Evolution.  
Tu agente ahora puede recordar a quién está hablando, qué se dijo y cuál es el estado de cada conversación.

Además, dejamos preparado un formulario simple para agregar usuarios nuevos a la base (nombre, teléfono y estado activo), que es lo único que necesitas para habilitar a alguien y permitirle conversar con la IA.

Una vez configurado esto, ya tenemos todo conectado y listo para la prueba en vivo.
