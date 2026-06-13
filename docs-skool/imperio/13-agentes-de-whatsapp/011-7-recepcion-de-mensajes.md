# ✉️ 7. Recepción de Mensajes

> Ruta: Agentes de WhatsApp › ✉️ 7. Recepción de Mensajes

**🎬 Vídeo (6.6 min):** https://www.loom.com/share/14eb5c7689894ae39039cd014b79dcb0

---

En este módulo entendemos cómo funciona el primer bloque del agente: **el punto exacto donde llega cada mensaje de WhatsApp** y cómo lo procesamos para que el flujo siga funcionando de manera ordenada, estable y sin errores.

Todo comienza con un **webhook**, que recibe la información cruda enviada desde WhatsApp. Aquí vemos en tiempo real quién escribió, desde qué número, qué mensaje llegó y qué datos adicionales acompañan esa interacción. Esta visibilidad es clave para depurar, testear y mejorar tu agente.

Luego, almacenamos dos datos esenciales:

- **La instancia** (el número de WhatsApp conectado)
- **El remoteJID** (el número del usuario que escribió)

Guardar esta información permite usar un **solo flujo conectado a múltiples números**, y también filtrar ejecuciones por teléfono al momento de revisar logs en n8n. Esto te ahorra horas cuando necesitas encontrar errores o depurar respuestas.

Como WhatsApp y Evolution pueden enviar el número de teléfono en diferentes campos, añadimos un pequeño bloque de código que **unifica y estandariza el número**, evitando fallas futuras y asegurando que tu agente responda siempre al usuario correcto.

También incorporamos una **función interna de reseteo**: si el usuario (o tú en modo test) envía `/reset`, el sistema detecta el comando, borra la memoria del agente, elimina el registro del cliente en Airtable y deja todo listo para comenzar una nueva prueba. Esta herramienta acelera mucho el desarrollo, porque elimina la necesidad de borrar datos manualmente.

Finalmente, el módulo revisa si el usuario existe en la base de datos y si está activo.

- Si está activo → el flujo continúa.
- Si no está activo → el mensaje no se procesa.

Esta validación es fundamental para proteger tu sistema, evitar respuestas no deseadas y mantener un orden perfecto en la gestión de clientes.

Con este módulo entiendes y estructuras **la entrada oficial de mensajes al agente**, garantizando orden, estabilidad y control total sobre quién escribe y cómo se procesa cada mensaje antes de avanzar al resto del flujo.
