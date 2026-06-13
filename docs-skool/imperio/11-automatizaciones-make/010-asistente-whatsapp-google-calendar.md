# ❤️ Asistente Whatsapp + Google Calendar

> Ruta: Automatizaciones Make › ❤️ Asistente Whatsapp + Google Calendar

**🎬 Vídeo (45.6 min):** https://www.youtube.com/watch?v=CvL95akto8Y

**📎 Recursos:**
- Whatsapp + Google Calendar v2

---

El otro día vi una publicidad de una app que se conectaba a **WhatsApp** y actuaba como un asistente virtual: podía **agendar eventos, revisar tu calendario y enviarte recordatorios**. Me llamó la atención porque, aunque suena increíble, **crear algo así es más fácil de lo que parece**.

Así que me puse a construirlo. En **dos horas**, ya tenía listo un sistema que hacía lo mismo. En este post te voy a explicar **cómo funciona** y cómo tú también puedes construirlo desde cero.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9209247781e146398f46e7413f3a273fc2ed76b46a5c4b43bbb014b142bff562-md.png)

---

### **Cómo Funciona la Automatización**

Básicamente, cada vez que le mandas un mensaje o un audio al asistente de WhatsApp, este puede hacer tres cosas:

✅ **Agendar un evento** en tu calendario con solo decírselo.  
🔍 **Revisar tu disponibilidad** y decirte qué eventos tienes en el día.  
🗑️ **Eliminar eventos existentes** con una simple instrucción.

Lo interesante es que este sistema **no solo entiende lo que le pides**, sino que **toma acciones reales** por ti. Se conecta con **WhatsApp Cloud API**, transcribe audios, interpreta la intención con inteligencia artificial y actualiza tu calendario en **Google Calendar**.

---

### **¿Por qué es Importante Aprender Esto?**

Cada día usamos WhatsApp para coordinar reuniones, revisar pendientes y recordar eventos. Con una automatización como esta, **te olvidas de hacerlo manualmente** y dejas que un sistema lo haga por ti.

Además, esto no se limita solo a eventos: **puedes adaptarlo para responder clientes, registrar pedidos o incluso generar reportes**. El punto es que **WhatsApp puede ser mucho más que solo una app de mensajería si lo conectas con las herramientas correctas**.

Si quieres aprender a conectar **WhatsApp Cloud API** y empezar a crear tu propio asistente automatizado, en la comunidad de **Imperio Digital** tenemos un **tutorial paso a paso** donde te explicamos cómo hacerlo.

[👉 ](https://www.skool.com/imperio-digital/classroom/7efa4739?md=435d257c707d4860b5c9768830d7c33b)[**Accede al tutorial aquí**](https://www.skool.com/imperio-digital/classroom/7efa4739?md=435d257c707d4860b5c9768830d7c33b)[ 🚀](https://www.skool.com/imperio-digital/classroom/7efa4739?md=435d257c707d4860b5c9768830d7c33b)

Esto no es el futuro, **es lo que puedes hacer hoy mismo**.

PROMPT Mencionado para el Text-To-Structured-Data

> Recuerda que HOY es "{{now}}"
> 
> Eres mi asistente personal encargado de extraer la info clave y devolverla como datos estructurados. Tienes tres funciones:
> 
> 1. **agendar_eventos:** Recibes fecha de inicio, nombre y duración del evento. Devuelve: 
> 
>    - nombre_evento
> 
>    - fecha_inicio
> 
>    - duracion
> 
> 2. **revisar_eventos:** Recibes fecha_inicio y fecha_termino. Devuelve:
> 
>    - fecha_inicio
> 
>    - fecha_termino
> 
> 3. **eliminar_evento:** Recibes fecha_inicio, fecha_termino y dos palabras clave. Devuelve:
> 
>    - fecha_inicio
> 
>    - fecha_termino
> 
>    - palabra_clave
> 
> ##Considera que la fecha actual es: {{now}}, por lo que si te dicen "mañana" o "en una semana", haz tus respectivos cálculos.
