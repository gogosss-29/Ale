# Agentes de IA en WhatsApp con N8N

> Ruta: 🔴 Grabaciones › Agentes de IA en WhatsApp con N8N

**🎬 Vídeo (74.2 min):** https://www.youtube.com/watch?v=o80aBm-8qOA

**📎 Recursos:**
- Agente WhatsApp n8n

---

Permite conectar WhatsApp Business con N8N mediante Evolution API para crear agentes de IA capaces de responder, procesar mensajes, tomar acciones, centralizar datos en Airtable y automatizar flujos reales en negocios sin intervención humana.

---

# **Línea de tiempo de intervenciones**

**[****00:00****] Franco – Introducción a la sesión**  
Contexto para nuevos miembros, explicación del formato de los viernes y presentación del tema principal: agentes de IA en WhatsApp. Explica por qué son útiles para atención, leads y procesos internos.

**[****01:03****] Franco – Qué son los agentes de IA por WhatsApp y por qué importan**  
Describe el valor de usar IA en conversaciones: soporte, atención, ventas y trabajo interno. Introduce el caso práctico que se revisará.

**[****02:20****] Franco – Presentación de N8N y estructura del flujo**  
Muestra N8N y explica las tres grandes partes del flujo: recepción de mensaje, procesamiento y agente de IA.

**[****03:25****] Franco – Qué se necesita para montar el agente**  
Explica los tres componentes clave: Airtable como base de datos, Evolution API para WhatsApp y N8N como núcleo del agente.

**[****04:51****] Franco – Cómo se integra WhatsApp → Evolution → N8N → Airtable**  
Conecta las piezas conceptualmente y describe el rol concreto de cada software dentro del sistema completo.

**[****07:52****] Franco – Preguntas: baneos, plantillas, riesgos y warm-up de números**  
Aclaración sobre baneo de WhatsApp, uso de números nuevos, cómo warmear, riesgos de mensajes outbound y diferencias entre WhatsApp Business y Meta/API.

**[****14:00****] Franco – Inicio del análisis del flujo paso a paso**  
Explica cómo se recibe el mensaje mediante webhook, cómo se formatea y por qué se filtra la información dependiendo del tipo de contenido.

**[****17:48****] Franco – El sistema de espera y buffer de mensajes**  
Explica por qué un agente debe esperar antes de responder, cómo se acumulan mensajes y cómo se combinan antes de enviarlos al agente de IA.

**[****21:03****] Franco – Cómo se almacenan mensajes en Airtable**  
Detalle del mecanismo: guardar, comparar timestamps, juntar mensajes y limpiar el buffer después de procesar.

**[****23:55****] Franco – Cómo se tratan textos, audios e imágenes**  
Explica cómo se normaliza cada tipo para que el agente siempre reciba texto procesable.

**[****24:55****] Franco – Sección del agente de IA: cómo funciona internamente**  
Revisa el system prompt, objetivo, límites, memoria, herramientas disponibles y cómo se conecta a Airtable.

**[****27:01****] Franco – Uso de memoria dentro del agente**  
Define qué es, para qué sirve, límites y configuración recomendada según volumen.

**[****30:03****] Franco – Limpieza de caracteres y naturalidad de respuestas**  
Explica cómo se eliminan signos poco naturales y cómo eso mejora el realismo del agente.

**[****34:01****] Franco – Configuración de Supabase para memorias avanzadas**  
Explica cómo pasar de la memoria básica de N8N a una memoria robusta para cientos de conversaciones diarias.

**[****36:00****] Franco – Testeo del flujo en vivo**  
Envía mensajes reales desde su teléfono, muestra ejecución completa y analiza cada nodo funcionando en tiempo real.

**[****42:00****] Franco – Consultoría del agente con ejemplo real**  
Ejemplo de conversación del agente detectando problemas y ofreciendo automatizaciones.

**[****46:00****] Ana – Consulta sobre automatizar negocio multinivel**  
Franco explica cómo empezar: identificar tareas repetitivas, nutrir leads, mensajes automáticos y procesos de venta.

**[****53:05****] Franco – Cómo funcionan los subagentes y comunicación interna**  
Explica cuándo usar varios agentes, cómo se llaman entre ellos y por qué mejora el rendimiento separar funciones.

**[****57:20****] Franco – Cómo evitar alucinaciones (guardrails)**  
Muestra cómo agregar un agente verificador que corrige mensajes problemáticos antes de enviarlos al usuario.

**[****1:03:41****] Franco – Preguntas técnicas: enviar mensajes, riesgos, cobros y seguimiento**  
Aclara diferencias entre mensajes inbound/outbound, riesgos de spam y recomendaciones para uso seguro.

**[****1:07:00****] Jua & Carlos – Contexto de infraestructura y tutoriales**  
Explican dónde están los tutoriales para instalar N8N, Evolution API y Airtable, y cómo partir desde cero.

**[****1:12:00****] Jua – Invitación a onboarding y sesiones de preguntas**  
Resumen de sesiones de la semana: lunes onboarding, martes Q&A con Franco, oportunidades de aprender y participar.

**[****1:13:25****] Franco – Cierre y próximos pasos**  
Anuncia que la plantilla será publicada en Skool, junto con contenido y explicación adicional.
