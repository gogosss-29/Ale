# Agentes de Make (Pt. 2)

> Ruta: 🔴 Grabaciones › Agentes de Make (Pt. 2)

**🎬 Vídeo (61.2 min):** https://www.youtube.com/watch?v=isOsKfmO--c

---

En esta edición de "Automatiza con Fran", Franco Ricci nos sumergió en el mundo de los agentes de IA dentro de Make, enfocándose en su implementación, personalización y uso eficiente para automatizar escenarios complejos y mejorar la interacción multicanal.

Durante la clase se trataron temas esenciales como:

---

**Adaptación de escenarios existentes con agentes de IA:**  
Franco explicó cómo transformar escenarios ya creados para que funcionen con agentes, destacando la importancia de utilizar la función “Run Scenario on demand” y configurar correctamente las variables de entrada. También se recalcó la relevancia de las descripciones claras en cada herramienta para que el agente pueda interpretarlas y usarlas de forma autónoma.

---

**Desarrollo de un sistema automatizado para agendar visitas:**  
Se mostró cómo crear un sistema completo para agendar visitas inmobiliarias, que incluye verificación de disponibilidad en calendario, recolección de datos (nombre, fecha, hora, email), y respuesta automatizada a través de WhatsApp. Además, se explicó cómo manejar errores y validar la coherencia de las respuestas.

---

**Herramientas "on demand" y nodo "Return output":**  
Se profundizó en el uso de herramientas que pueden ser invocadas dinámicamente por los agentes, y cómo estructurar sus salidas para que sean entendibles y accionables. Franco enfatizó que el nodo “Return output” es clave para el razonamiento del agente.

---

**Uso de un agente manager y agentes especializados:**  
Se discutió la arquitectura modular en la que un agente principal (manager) puede dirigir tareas a subagentes especializados según la necesidad del usuario. Esto permite escalar los sistemas sin sobrecargar un solo agente y mantener la claridad funcional.

---

**Implementación de lógica conversacional coherente:**  
Se presentó una estrategia para mantener conversaciones consistentes a lo largo del tiempo y en múltiples canales. Esto incluyó la búsqueda y almacenamiento de datos en Airtable, integración con WhatsApp y manejo de mensajes entrantes y salientes para identificar usuarios y mantener contexto.

---

**Desafíos y soluciones en persistencia de datos:**  
Franco abordó la necesidad de evitar búsquedas innecesarias dentro de un flujo conversacional. Se propusieron estrategias como almacenar información clave fuera del agente y utilizar Data Stores o bases como Airtable para recuperar datos de forma eficiente.

---

**Participación de la comunidad:**  
Miembros como Henry, Pedro y Joaquín compartieron dudas y experiencias relacionadas con proyectos de calendario, manejo de herramientas dentro de escenarios y persistencia de contexto. La conversación se enriqueció con preguntas sobre diseño modular, simplificación de escenarios y pruebas de herramientas individuales.

---

**Demostración práctica en vivo:**  
Franco presentó un asistente virtual funcional conectado a WhatsApp y Airtable, mostrando paso a paso cómo automatiza la atención, agenda eventos y mantiene consistencia en la conversación. También se adelantaron acciones futuras, como la creación de un curso sobre Airtable y la optimización de escenarios existentes como el de WhatsApp.
