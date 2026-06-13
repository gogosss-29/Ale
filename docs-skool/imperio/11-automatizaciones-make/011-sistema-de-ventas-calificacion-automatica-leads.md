# 👑Sistema de Ventas Calificación Automatica Leads

> Ruta: Automatizaciones Make › 👑Sistema de Ventas Calificación Automatica Leads

**🎬 Vídeo (45.2 min):** https://www.youtube.com/watch?v=6I780zheHzU

**📎 Recursos:**
- Calificacion_Leads_Plantilla_v4

---

Sí... es cansador hablar con leads que no califican.   
  
Este sistema te ahorra tiempo, automatiza el proceso de calificación y te ayuda a cerrar más ventas… incluso mientras duermes (+ blueprint descargable)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e4e374d8edf447fa81a64a137bc4513276c59854f9094802a3cf8e49b6dffa69-md.png)

### 🚀 ¿Qué hace este sistema?

Califica automáticamente a tus leads (clientes potenciales) en tres categorías:

- **Muy calificado**
- **Calificado**
- **No calificado**

En base a esa clasificación:

- Envía un email personalizado según su clasificación
- Notifica a distintos miembros de tu equipo comercial en Slack según su clasificación
- Registra todo en un CRM (AirTable)
- Le envía un WhatsApp al lead para agendar una reunión
- Si el lead *no* califica, le ofrece una alternativa como un downsell (por ejemplo, acceso a un low ticket)

### 🧠 ¿Cómo funciona?

1. El lead rellena un formulario (puedes usar [Fillout.com](http://Fillout.com) o Google Forms).
2. [Make.com](http://Make.com) detecta la nueva respuesta y envía los datos a ChatGPT.
3. ChatGPT interpreta las respuestas y clasifica el lead según su urgencia, presupuesto, necesidad y otros factores.
4. Según esa calificación, se ejecuta uno de tres flujos: - Muy calificado → Correo + Slack al equipo A + WhatsApp para agendar
- Calificado → Correo + Slack al equipo B
- No calificado → Email de downsell (acceso a Imperio Digital)

### 🛠 Herramientas que usamos

- [**Make.com**](http://Make.com): El motor de automatización
- **Fillout** (o Google Forms, Typeform, etc.): Para capturar leads
- **OpenAI / ChatGPT**: Para interpretar y calificar a los leads
- **AirTable**: Actúa como CRM y registro central
- **Slack**: Notificaciones automáticas al equipo comercial
- **WhatsApp Business Cloud**: Mensajes automatizados para agendar llamadas

### 🔥 ¿Por qué es tan poderoso?

- Filtra automáticamente a los leads que no te hacen perder el tiempo.
- Ofrece una ruta de conversión para cada tipo de lead (no los pierdes).
- Ahorra horas de seguimiento manual y mejora tu eficiencia comercial.
- Se puede implementar en **menos de una hora**.
- Es personalizable al 100%.

Este sistema está disponible como plantilla descargable al final de esta publicación.

---

Prompt: Transform Text to Structured Data *(este es el prompt que modificaremos según los parámetros que nosotros queramos usar para clasificar al lead)*

> Califica el siguiente lead en:
> 
> Muy Calificado
> 
> Calificado
> 
> No Calificado
> 
> 1. **Determina el nivel de calificación del lead.**
> 
> Toma como referencia las siguientes preguntas que le hice en el formulario:
> 
> ¿Tienes otros procesos que te gustaría automatizar? {{37.answers.ceyL}}
> 
> ¿Que proceso en tu negocio te esta generando mas problemas o consume mas tiempo? {{37.answers.qmij}}
> 
> Que tan urgente es resolver este problema? (3 opciones: Urgente necesito una solucion ahora, Importante pero puede esperar, no es prioridad estoy buscando opciones) Este es clave en la respuesta para la calificacion. La respuesta fue:{{37.answers.xeAu}}
> 
> Cuentanos un poco sobre tu negocio: {{37.answers.`5XPY`}}
> 
> Tienes presupuest oestimado para esta solcuion? (USD) (5 opciones, menos de $750, entre $750 y $1500, entre $1500 y $3000, entre $3000 y $5000, más de $5000 si el ROI es alto), este es lo mas importante para determinar la calificacion, si elige menos de 1500, no aplica, si es entre 1500 y 3000, califica, y si es 3000 o más, es muy calificado 
> 
> La respuesta que nos dio fue: {{37.answers.kECK}}
> 
> ¿Cómo manejas actualmente este proceso? {{37.answers.`3TsV`}}
> 
> ¿Cuál es tu correo? {{[37.answers.dvR](http://37.answers.dvR)9}}
> 
> ¿Cual es tu nombre? {{37.answers.hj8E}}
> 
> ¿Cuantas personas trabajan en tu empresa? {{37.answers.`124E`}}
> 
> ¿Cuál es tu sitio web?{{37.answers.teJb}}
> 
> Tambien generaremos el diminutivo del nombre como confianza con la persona, tipo si el nombre es "Benjamin Cordero", le pondremos "Benja", si es "Maximiliano", es "Max". Recuerda que le estamos escribiendo a "{{37.answers.hj8E}}"
> 
> Tambien sacaremos cual es el mayor problema que estan teniendo en 1 a 5 palabras, mientras menos mejor.
> 
> Tambien pasaremos el celular y le quitaremos el +. Por ejemplo de +56912345678 lo pasamos a 56912345678

Prompt Asistente:

> Crea un correo electrónico personalizado para enviar a los leads que han llenado un formulario para obtener soluciones personalizadas aplicadas a su empresa. Ajusta el tono y el contenido del correo basándote en su nivel de calificación: **"Muy Calificado"**, **"Calificado"** o **"No Calificado"**.
> 
> - **"Muy Calificado":** Haz que sea muy personal y elogioso, mencionando aspectos positivos del negocio del negocio. Explica que se le ha enviado una invitación a un llamado con el dueño del negocio, Benja en el siguiente link: [https://calendly.com/becord00/nivel-6-sesion-1-1](https://calendly.com/becord00/nivel-6-sesion-1-1)
> 
> - **"Calificado":** Haz el correo formal e informa que se le ha enviado un link para que agende una llamada con Juan, jefe de Ventas: [https://calendly.com/becord00/nivel-6-sesion-1-1](https://calendly.com/becord00/nivel-6-sesion-1-1)
> 
> - **"No Calificado":** Explica que actualmente no es un buen momento para recibir consultoría pero que se le invita a unirse a una comunidad llamada Imperio Digital donde enseñamos las bases de automatizaciones y puedes aprender como construimos estos sistemas mas "Do it Yourself" o "Done with you" el link es [www.skool.com/imperio-digital](http://www.skool.com/imperio-digital) . Puedes probar por siete dias gratis
> 
> ---
> 
> # Steps
> 
> 1. **Determina el nivel de calificación del lead.**
> 
> 2. **Prepara el email.**
> 
>    - **Muy Calificado:** tono muy personal, menciona la reunión con Benja. [https://calendly.com/becord00/nivel-6-sesion-1-1](https://calendly.com/becord00/nivel-6-sesion-1-1) 
> 
>    - **Calificado:** Haz el correo formal e informa que se le ha enviado un link para que agende una llamada con Juan, jefe de Ventas: [https://calendly.com/becord00/nivel-6-sesion-1-1](https://calendly.com/becord00/nivel-6-sesion-1-1) .
> 
>    - **No Calificado:** menciona que no es el mejor momento y ofrécele la suscripción y unirse a nuestra comunidad llamada "Imperio Digital" que enseñamos a como puedes construir este tipo de soluciones etc, también personalizado.

Prompt Redactar Emails

> ##Redacta el cuerpo del email segun su nivel de calificacion que es: {{38.Calificacion}} 
> 
> ##Sigue las instrucciones de tu prompt system.
> 
> Haz los parrafos cortos, como de una o dos lineas máximo, para que sea mas legible
> 
> Toma como referencia las siguientes preguntas que le hice en el formulario:
> 
> ¿Tienes otros procesos que te gustaría automatizar? {{37.answers.ceyL}}
> 
> ¿Que proceso en tu negocio te esta generando mas problemas o consume mas tiempo? {{37.answers.qmij}}
> 
> Que tan urgente es resolver este problema? (3 opciones: Urgente necesito una solucion ahora, Importante pero puede esperar, no es prioridad estoy buscando opciones) Este es clave en la respuesta para la calificacion. La respuesta fue:{{37.answers.xeAu}}
> 
> Cuentanos un poco sobre tu negocio: {{37.answers.`5XPY`}}
> 
> Tienes presupuest oestimado para esta solcuion? (USD) (5 opciones, menos de $750, entre $750 y $1500, entre $1500 y $3000, entre $3000 y $5000, más de $5000 si el ROI es alto), este es de los mas clave para determinar la calificacion: 
> 
> Respuesta: {{37.answers.kECK}}
> 
> ¿Cómo manejas actualmente este proceso? {{37.answers.`3TsV`}}
> 
> ¿Cuál es tu correo? {{[37.answers.dvR](http://37.answers.dvR)9}}
> 
> ¿Cual es tu nombre? {{37.answers.hj8E}}, pero nos dirijiremos a el como "{{38.nombre_confianza}}"
> 
> ¿Cuantas personas trabajan en tu empresa? {{37.answers.`124E`}}
> 
> ¿Cuál es tu sitio web?{{37.answers.teJb}}
> 
> ###Importante:
> 
> Si es lead es:
> 
> Muy Calificado: Invítalo a una llamada con el dueño del negocio en el siguiente link: [https://calendly.com/...](https://calendly.com/becord00/nivel-6-sesion-1-1)
> 
> Calificado: Invítalo a una llamada con Juan en Ventas en el siguiente link: [https://calendly.com/becord00/...](https://calendly.com/becord00/nivel-6-sesion-1-1)
> 
> No Calificado: No califica para la solucion, pero invítalo a unirse a la comunidad para que aprenda a crear este tipo de sistemas en [www.skool.com/imperio-digital](http://www.skool.com/imperio-digital) 
> 
> Recuerda que le estamos redactando el cuerpo del correo a un lead {{38.Calificacion}}
> 
> #El output debe ser en HTML y OMITE escribir "```html" o (```html) o usar el símbolo ` en cualquier parte del texto.
> 
> #Si no tienes alguna variable como nombre, cargo, nombre empresa, etc no lo incluyas.
> 
> Mi nombre es Benja, Cofundador de Imperio Digital, mi contacto es +569 1234 5678
> 
> El correo debe ser preciso al grano, personalizado y NO muy extenso, mas bien corto y tratarlo como "{{38.nombre_confianza}}", escribe con confianza y recuerda que eres de chile, por lo que haremos que escribes como una persona.
> 
> NO menciones su "nivel de calificacion"
> 
> No uses símbolos de exclamación anteriores "¡" ¡ ni ¿ "¿"
