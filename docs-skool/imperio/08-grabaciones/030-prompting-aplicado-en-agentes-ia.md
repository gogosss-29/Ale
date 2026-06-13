# Prompting Aplicado en Agentes IA

> Ruta: 🔴 Grabaciones › Prompting Aplicado en Agentes IA

**🎬 Vídeo (63.0 min):** https://www.youtube.com/watch?v=2IRDfLoEPwg

---

**[00:01] Contexto de la sesión y objetivo**  
Introducción a la sesión de viernes y explicación del enfoque: prompting aplicado y debugging en un caso real ya próximo a producción.

**[01:13] Caso real: agente IA para inmobiliaria**  
Presentación del agente que atiende consultas por WhatsApp: compra, alquiler temporario, alquiler convencional, tasaciones y administración.

**[02:49] Metodología de testeo de flujos**  
Uso de un listado simple de flujos a testear con estados (pendiente / aprobado) para organizar pruebas antes de producción.

**[06:53] Primer bug detectado (flujo incorrecto)**  
El agente interpreta una propiedad en venta como alquiler. Se identifica que el error proviene de la lógica y el scraping, no de la IA.

**[08:25] Error por formato de números (precio)**  
Problemas causados por puntos y comas en precios. Ajuste de prompt para devolver solo números enteros y evitar errores de evaluación.

**[12:39] Decisión estratégica: cuándo no corregir en vivo**  
Se explica cuándo conviene anotar un bug y seguir avanzando con otros flujos para no frenar el proceso de testeo.

**[13:01] Flujo de compra sin link**  
El agente hace preguntas clave (zona, tipo y presupuesto) y deriva correctamente al asesor humano según las reglas del cliente.

**[15:10] Uso de memoria y user tags**  
Cómo se guarda la intención del usuario (compra, alquiler, etc.) en la base de datos y se reutiliza como lógica de prompting.

**[16:26] Subagentes silenciosos**  
Explicación del subagente de compra que no conversa con el usuario, sino que decide lógica y acciones internas.

**[18:28] Ajustes de saludo y tono**  
Corrección de respuestas genéricas para mantener una presentación clara y consistente del agente desde el primer mensaje.

**[23:10] Prompt dinámico según estado del usuario**  
Simplificación del prompt cuando la intención ya está definida, descargando contexto innecesario al agente.

**[28:01] Guardarrails y filtros de respuesta**  
Uso de filtros externos para eliminar saludos repetidos, agradecimientos innecesarios y repeticiones (eco).

**[29:53] Flujo de alquiler temporario con link**  
Testeo de propiedad con scraping en tiempo real, validación de precios mínimos y reglas por ambiente.

**[33:02] Error de UX: preguntas mal ordenadas**  
El agente pregunta duración del alquiler antes de resolver dudas del usuario. Se detecta un problema estructural de prompt.

**[36:57] Manejo de límites (mínimo 3 meses)**  
Cómo comunicar restricciones sin sonar cortante y manteniendo un tono humano y empático.

**[40:06] Problema en el curado del mensaje**  
Un guardarrail elimina información clave por detectar falso eco. Se identifica el error en la expresión lógica.

**[44:00] Corrección del detector de eco**  
Ajuste para evaluar solo el último mensaje del usuario y no toda la conversación.

**[48:00] Ajuste fino de tono**  
Separación entre respuesta del subagente, agente principal y mensaje final, agregando una capa de reformulación empática.

**[50:10] Reescritura del flujo con link definido**  
Reordenamiento del prompt: primero obtener información, luego informar y recién después calificar.

**[55:36] Error técnico en derivación (Round Robin)**  
Fallo por mala referencia de arrays en n8n. Explicación del concepto de Round Robin para asignar leads.

**[57:14] Fix en expresiones de n8n**  
Corrección usando `first` en lugar de `item` para evitar errores al seleccionar asesores.

**[1:00:00] Mejora visible del tono del agente**  
El agente responde de forma más natural, menos robótica y con mejor secuencia conversacional.

**[1:02:18] Cierre y aprendizajes clave**  
Importancia del testeo exhaustivo, prompts descargados, lógica clara y debugging real antes de producción.
