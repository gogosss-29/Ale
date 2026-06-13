# 🌐Crea Extensiones de Chrome con IA

> Ruta: Automatizaciones Make › 🌐Crea Extensiones de Chrome con IA

**🎬 Vídeo (24.1 min):** https://www.youtube.com/watch?v=4Zf5s_dLIuY

**📎 Recursos:**
- El Justiciero - Plantilla Make

---

En este video vamos a ver cómo crear, paso a paso, una extensión de Google Chrome conectada a Inteligencia Artificial y automatizaciones externas… sin saber programar.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/fad77ce74212472f93255f60140a7434ef26e39522dc484cb904ca5cb4483596-md.png)

Usaremos ChatGPT para generar todo el código y Make para procesar la información en tiempo real, permitiéndote:

- Ejecutar automatizaciones en el **backend** directamente desde tu navegador.
- Conectar la extensión con cualquier flujo en Make, N8N o Zapier.
- Armar literalmente lo que quieras: asistentes, verificadores, resúmenes automáticos, alertas, integraciones personalizadas, etc.
- Personalizar mensajes, diseño y funciones en segundos.

Para este caso vamos a armar un sistema que, al seleccionar un texto en cualquier página web, lo envía a una automatización en Make, lo analiza con IA y devuelve si es real o falso, junto con una breve explicación y un porcentaje de certeza.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3054a8af2fbf46b4bfd02058f50503fe74c73da4dc5d44a48296ee5b94fdcefd-md.png)

Este es solo un ejemplo, y es bastante simple: desde aquí puedes adaptarlo para tareas repetitivas, sistemas internos o incluso productos listos para vender y publicar en la Chrome Web Store. 

Literalmente puedes crear cualqueir extensión de cualqueir automatización que hemos visto en este último año.

💡 **Potencial:** Crear herramientas internas para tu equipo, asistentes personales de IA, verificadores de datos en tiempo real o extensiones de productividad que trabajen mientras estás browsing.  
  
No creo que lo necesites, pero si llegas a quererlo aquí abajo te dejo el escenario de Make y el prompt utilizado.

> Eres un verificador automático de texto. Recibes un fragmento de texto plano y debes responder únicamente con “REAL” si el contenido es auténtico o “NO REAL” si parece falso. Necesito que después me des una breve explicacion de por qué y comiences toda respuesta con "El Justiciero dice que esto es... REAL/FALSO (dependiendo del contexto). Tambien daras una probabilidad de certeza, entre 0% y 100% según que tan confiado estas de tu respuesta. Ten criterio y no seas amarillo, toma decisiones.
> 
> El texto a verificar es: {{`1`}}
