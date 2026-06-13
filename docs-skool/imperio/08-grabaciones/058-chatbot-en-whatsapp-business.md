# Chatbot en WhatsApp Business

> Ruta: 🔴 Grabaciones › Chatbot en WhatsApp Business

**🎬 Vídeo (58.1 min):** https://www.youtube.com/watch?v=ftg6-5Ej830

**📎 Recursos:**
- Escenarios JSON

---

En esta sesión de **Automatiza con Fran**, cubrimos en detalle la integración de **Wapi, Relevance y Make** para la implementación de un chatbot en **WhatsApp Business**. El objetivo fue explicar cómo aprovechar al máximo estas plataformas **automatizando la comunicación con clientes, gestionando etiquetas y asegurando una transición fluida entre IA y agentes humanos**.

#### **Puntos clave de la sesión:**

1. **Introducción al sistema:** - Uso de **Wapi** para gestionar los mensajes en WhatsApp Business.
- Conexión con **Relevance AI** para la generación de respuestas con inteligencia artificial.
- Implementación en **Make** para la automatización de procesos y estructuración de datos.
2. **Manejo de etiquetas para clasificación de chats:** - Se explicó la importancia de **etiquetar nuevas conversaciones** para evitar que el bot interactúe con contactos previos.
- Se introdujo la **etiqueta “IA In”** para indicar nuevas interacciones con clientes potenciales.
- Se explicó el **proceso de handoff** para derivar conversaciones a un humano cuando sea necesario, asignando la etiqueta "Derivado a humano".
3. **Optimización del flujo de conversación:** - Se implementó una estrategia para **manejar múltiples mensajes consecutivos** y evitar que el chatbot se active varias veces.
- Se usó un delay de **60 segundos** para **concatenar mensajes y enviarlos a la IA como una sola consulta**.
- Explicación de cómo almacenar y recuperar conversaciones en la **Data Store de Make** para mejorar la gestión de los chats.
4. **Manejo de diferentes tipos de mensajes:** - **Texto:** Flujo estándar de procesamiento y respuesta.
- **Audios:** Uso de la API de OpenAI (Whisper) para convertirlos en texto antes de enviarlos a la IA.
- **Imágenes:** Uso de **GPT-4 Vision** para describir imágenes enviadas por los usuarios.
5. **Optimización y pruebas del sistema:** - Explicación sobre cómo **realizar pruebas seguras** antes de implementar la automatización con clientes.
- Uso de filtros en Make para evitar errores y garantizar una ejecución fluida.
- Estrategias para dividir procesos largos en varios escenarios y optimizar el uso de operaciones en Make.
6. **Preguntas y respuestas de la comunidad:** - Cómo manejar chats derivados a humanos y la posibilidad de devolverlos al chatbot.
- Estrategias para reducir el consumo de ejecuciones en Make y evitar que los procesos se detengan por límites de tiempo.
- Implementación de soluciones escalables para sistemas con miles de mensajes o registros.

### **Conclusión:**

Esta sesión fue un recorrido avanzado por la creación de un **chatbot potente en WhatsApp Business**, combinando múltiples herramientas de automatización e inteligencia artificial. La estrategia presentada permite **gestionar clientes de forma eficiente, automatizar respuestas y mejorar la experiencia del usuario** sin perder control humano cuando sea necesario.
