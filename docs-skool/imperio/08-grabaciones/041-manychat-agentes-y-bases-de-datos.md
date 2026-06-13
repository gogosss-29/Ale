# ManyChat + Agentes y Bases de Datos

> Ruta: 🔴 Grabaciones › ManyChat + Agentes y Bases de Datos

**🎬 Vídeo (71.4 min):** https://www.youtube.com/watch?v=vPhPOOO45sM

---

Explica paso a paso cómo usar **ManyChat** más allá de sus funciones básicas, integrándolo con bases de datos y agentes de IA para WhatsApp e Instagram. Se abordan problemas comunes como la gestión de múltiples mensajes, buffers de espera, sincronización de respuestas, handoff a humanos y pricing de este tipo de proyectos.

---

### 🕒 **Cronología de intervenciones:**

**00:00 – Fran – Introducción a la sesión**  
Presenta la dinámica del viernes (22 de agosto de 2025) y el foco en ManyChat: usos simples, integración con IA y cómo llevarlo más allá de sus funciones básicas.

**02:06 – Fran – Qué es ManyChat y su enfoque inicial**  
Explica el objetivo de ManyChat: simplificar automatizaciones en WhatsApp/Instagram y ser una herramienta accesible para creadores de contenido.

**06:49 – Fran – Ejemplos de automatizaciones simples**  
Muestra casos prácticos de triggers en historias de Instagram que responden con links o lead magnets.

**10:09 – Henry – Uso de ManyChat en ventas**  
Comparte su experiencia en procesos B2C e infoproductos, destacando su utilidad para equipos de ventas y organización de bandejas.

**11:47 – Víctor – Implementación real de un agente de IA en ManyChat**  
Expone cómo logró conectar ManyChat con Make para responder en WhatsApp con un agente IA, pero consulta cómo mostrar las respuestas guardadas en Google Sheets.

**16:09 – Fran – Explicación gráfica del flujo en Miro**  
Detalla la lógica de buffers de espera, agrupación de mensajes, integración con bases de datos externas (AirTable/Sheets) y activación de agentes IA vía HTTP.

**29:22 – Fran – Revisión del flujo completo**  
Recapitula el proceso: mensaje entrante → almacenamiento en BD → buffer de espera → activación de IA → guardado de respuesta → entrega al usuario → reinicio del ciclo.

**32:11 – Jorge – Duda sobre tiempos y fallos de respuesta**  
Pregunta qué pasa si la IA tarda más de lo esperado o no responde. Fran explica la importancia de configurar tiempos adecuados y filtros para evitar respuestas duplicadas.

**34:57 – Víctor – Problema con celdas en Google Sheets**  
Consulta cómo guardar múltiples conversaciones. Fran muestra la estructura ideal de BD en Sheets/AirTable con columnas (número, threadID, mensajes, respuesta).

**46:12 – Fran – Cómo mostrar la respuesta en ManyChat**  
Explica cómo mapear la respuesta desde Sheets/AirTable a un campo personalizado en ManyChat y devolverla al usuario.

**49:06 – Henry – Problema de mensajes secuenciales**  
Pregunta qué pasa si un usuario envía un mensaje adicional mientras la IA procesa. Fran explica cómo manejarlo con buffers y procesamientos paralelos.

**51:05 – Henry – Factores clave de implementación**  
Subraya tres puntos: tiempos de respuesta no inmediatos, pruebas de duración de procesos y monitoreo de conversaciones fallidas.

**56:13 – Fran – Pausar automatizaciones en ManyChat**  
Muestra cómo evitar que diferentes flujos de ManyChat se solapen, usando la función “pausar automatizaciones” y gestionando triggers con etiquetas.

**1:00:06 – Henry – Experiencia en lanzamiento masivo con ManyChat**  
Cuenta un caso donde un bot mal configurado generó caos en un lanzamiento por Instagram. Fran responde sobre errores comunes en handoff y precios de estos proyectos.

**1:07:02 – Víctor – Aprendizaje y estancamiento**  
Comparte su dificultad para avanzar con recursos dispersos. Pregunta si habrá entrenamientos específicos de ManyChat en Imperio Digital. Fran y Juaco confirman que están planificando un taller dedicado.

**1:10:24 – Víctor – Aporte a la comunidad**  
Se compromete a compartir su módulo de Make + ManyChat como recurso para otros miembros.

**1:10:31 – Roma – Consulta final sobre bases de datos**  
Pregunta si AirTable ofrece plantillas listas. Fran aclara que deben crearse manualmente.

**1:11:03 – Cierre – Fran**  
Cierra la sesión destacando el valor del intercambio, la importancia de experimentar y el soporte continuo de la comunidad.
