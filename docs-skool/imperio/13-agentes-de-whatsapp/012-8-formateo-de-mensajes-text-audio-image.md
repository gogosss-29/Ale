# 🧩 8. Formateo de mensajes (text, audio, image)

> Ruta: Agentes de WhatsApp › 🧩 8. Formateo de mensajes (text, audio, image)

**🎬 Vídeo (4.4 min):** https://www.loom.com/share/3adafa2d2b7e4981a249de10e0e05829

---

En este módulo tomamos cualquier mensaje que envíe el usuario —texto, audio o imagen— y lo convertimos en información limpia y lista para que la IA la procese. Esta etapa es clave: evita errores y asegura que el agente entienda exactamente lo que recibió.

Primero identificamos al usuario y verificamos si corresponde responderle. Luego, según el tipo de mensaje que llega desde Evolution, el flujo sigue una de tres rutas:

**1. Texto**  
El caso más simple. Tomamos el mensaje y lo pasamos directo como *input*, sin transformaciones adicionales.

**2. Audio**  
Aquí el proceso es automático: se descarga el archivo, se convierte, se envía a GPT para transcripción y se guarda el texto final como *input*. Todo ocurre en segundos.

**3. Imagen**  
Descargamos la foto, la analizamos con GPT mediante un prompt diseñado para obtener descripciones útiles y, si el usuario escribió un caption, también se integra al *input*.

---

## **Un solo destino: input**

Aunque existan rutas distintas, todas terminan en la misma variable. Esto:

- evita condicionales repetidas,
- mantiene el sistema más simple,
- y permite que cualquier módulo downstream use siempre `$.json.input` sin preocuparse por el origen del mensaje.

Gracias a esto, el agente puede responder igual de bien a un texto, una nota de voz o una imagen.

---

## **Qué aporta este módulo**

- Aceptas cualquier tipo de mensaje sin romper el flujo.
- Conviertes audio e imágenes en texto útil.
- Mantienes una estructura estándar y fácil de escalar.
- Entregas datos limpios a la siguiente etapa, donde la IA interpreta y responde.

En resumen: este módulo prepara todo para que tu agente entienda al usuario sin importar el formato y mantenga una conversación fluida desde el primer mensaje.
