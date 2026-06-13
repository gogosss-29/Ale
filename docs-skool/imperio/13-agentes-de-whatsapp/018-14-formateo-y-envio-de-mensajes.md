# 📤 14. Formateo y envío de mensajes

> Ruta: Agentes de WhatsApp › 📤 14. Formateo y envío de mensajes

**🎬 Vídeo (4.0 min):** https://www.loom.com/share/3d9ba7f021454a5fb15e9bb3c63792af

---

En este módulo cerramos el ciclo completo del agente.  
Aquí convertimos la respuesta generada por la IA en un mensaje limpio y listo para enviarse por WhatsApp mediante Evolution. Ya no procesamos entradas: preparamos la salida final que verá el usuario.

---

## **1. Limpieza de la respuesta de la IA**

Cuando el agente responde, el texto llega a la variable **output**.  
A veces la IA incluye caracteres extraños, saltos de línea innecesarios o símbolos que no se ven bien en WhatsApp.

Para evitarlo, usamos un nodo de formateo que:

- Detecta caracteres no deseados
- Los elimina automáticamente
- Devuelve un mensaje limpio y seguro

Pedirle a la IA "no uses X símbolo" no siempre funciona.  
La solución real es **sanear el mensaje antes de enviarlo**.

---

## **2. Espera controlada (opcional)**

Este paso no siempre es necesario, pero puede ser útil cuando:

- La IA genera respuestas largas
- Queremos evitar choques si llegan nuevos mensajes mientras se procesa
- Es necesario espaciar envíos para evitar bloqueos o parecer spam

Normalmente se dejan unos segundos, pero el nodo es totalmente opcional.

---

## **3. Envío final por WhatsApp**

El último paso es enviar el mensaje al usuario.  
Esto se hace mediante un POST al endpoint de Evolution:

- Se usa la URL del webhook
- Se envía el API key
- Se pasa el número del usuario (remoteJID + sufijo de WhatsApp)
- Se envía el texto limpio generado en el paso anterior

El sistema utiliza automáticamente:

- La instancia correcta
- El webhook inicial del flujo
- La variable **output_limpio** como contenido final

El usuario recibe la respuesta en segundos, como si estuviera conversando con una persona real.

---

## **Qué permite este módulo**

- Convertir la salida de la IA en un mensaje limpio y sin errores
- Enviar respuestas confiables a cualquier número de WhatsApp
- Controlar la cadencia de los mensajes cuando es necesario
- Completar el circuito del agente: mensaje entrante → procesamiento → inteligencia → mensaje saliente

Con esto, tu agente ya piensa, recuerda, decide, ejecuta… y ahora responde correctamente.  
Queda oficialmente listo para producción en WhatsApp utilizando n8n y Evolution.
