# Mandá 1000 mensajes sin que te baneen

> Ruta: 🔴 Grabaciones › Mandá 1000 mensajes sin que te baneen

**🎬 Vídeo (58.9 min):** https://www.youtube.com/watch?v=5UIrC_nJv2o

---

**Problemas que resuelve la sesión 3 de Abril:** Cómo automatizar envíos masivos de WhatsApp sin banear la cuenta, cómo construir agentes de IA replicables para múltiples clientes desde un solo flujo, y cuándo usar Playwright para automatizar acciones en plataformas sin API.

---

**Intervenciones**

**[****00:00****] Agustín — Automatización de WhatsApp para empresa de construcción** Tiene 1.000 contactos en un listado y quiere mandar 30 mensajes diarios para limpiar la base y capturar mails. Busca un sistema que lo haga solo, sin riesgo de baneo.

Solución: conectar WhatsApp Business a WhiteCloud, crear una plantilla aprobada por Meta y lanzar campañas masivas directamente desde la plataforma. Para casos más complejos, integrar con N8N. No hace falta N8N si el objetivo es solo envío masivo con plantilla.

**[****09:33****] Agustín — Agente de voz para registrar entradas y salidas** Quiere mandar mensajes de voz a WhatsApp diciendo "hoy gasté tanto" y que el agente lo cargue automáticamente en un Excel con tabla dinámica, por categorías (personal, empresa, efectivo, transferencia).

Solución: usar N8N con un agente de IA conectado a WhatsApp via WhiteCloud. También se menciona OpenClaw como alternativa más autónoma para este tipo de caso.

**[****13:00****] Agustín — ¿Cómo instalar N8N de forma económica?** El cupón de descuento de Hostinger no le funciona desde Argentina.

Solución: el cupón aplica desde otros países (México, Europa). Usar VPN para activarlo o verificar si aplica al pago anual.

**[****15:45****] Juaco — Recomendación adicional: OpenClaw** Sugiere revisar la sección de OpenClaw en Bytecoding para el caso del agente contable. Aclara que hay capas de seguridad documentadas en el curso y que el equipo lo tiene corriendo sin problemas en producción.

**[****20:08****] Juaco — Agentes replicables para e-commerce (caso de su hermana)** Su hermana tiene una agencia de marketing y quiere ofrecer un agente de atención al cliente como demo a tiendas online. El agente ya fue armado con scraping de la tienda, knowledge base en Supabase y configuración automática del tono, mensaje de bienvenida y avatares de cliente.

Duda: cómo pasarlo a producción para que la agencia pueda dar de alta nuevos clientes sin intervención técnica.

Solución (Franco): todos los agentes apuntan al mismo webhook. El payload lleva un slug que identifica el negocio. N8N busca el registro en la base de datos, inyecta el prompt variable y devuelve la respuesta como webhook response. Para pasar a producción solo hay que incrustar un HTML estándar que cambia el slug. El proceso de alta queda a cargo del panel en Vercel, con un toggle demo/producción.

**[****34:11****] Juaco — ¿OpenClaw para agentes de atención al cliente con acciones complejas?** Pregunta si tiene sentido usar OpenClaw para un agente que necesite agendar citas en plataformas sin API.

Solución (Franco): no, es overkit y difícil de contener con 20+ conversaciones activas. Mejor alternativa: armar un scraper en N8N y llamarlo como tool en el flujo del agente. Si hay una parte específica que requiere razonamiento variable, ahí sí meter OpenClaw de forma acotada.

**[****38:34****] Franco y Juaco — ¿Qué es Playwright y para qué sirve?** Se explica en contexto luego de que Juaco menciona que lo usa en Cloud Code via MCP.

Playwright permite controlar un navegador de forma programática desde N8N, Claude Code, Cloudbot o cualquier herramienta compatible. Sirve para llenar formularios, navegar webs sin API, hacer QA automatizado (testeo de flujos de usuario), verificar links rotos y pasar captchas. Consume muchos tokens en la primera acción, pero aprende rápido y las siguientes son más eficientes.

**[****43:00****] Daniel — Chatwoot: ¿vale la pena?** Un participante pregunta si Chatwoot es buena opción para conectar chatbot, WhatsApp, Instagram y redes sociales en un cliente que quiere todo integrado.

Respuesta: sí, especialmente si el cliente quiere self-hostear. Tiene macros que permiten activar webhooks con una etiqueta. Carlos Domínguez tiene experiencia documentada con esta herramienta. Franco la usó con Evolution API y tuvo fricciones, pero reconoce que puede ser un problema de setup.

**[****49:42****] Shen — Seguridad en aplicaciones hechas con Claude** Pregunta cómo proteger la información de clientes en apps construidas con IA, especialmente en etapas tempranas.

Respuesta (Franco): si estás validando, no te sobre-compliques con seguridad. Confiar en los servicios cloud es lo que hace la mayoría. A medida que crece la base de clientes y aparecen requerimientos de compliance, ahí escalar las capas de seguridad.

Respuesta (Daniel): para una red local pequeña, lo básico es un router Cisco configurado con firewall, control de puertos y registro de accesos. Un SSL wildcard si hay subdominios. El ISP ya puede ofrecer algo, pero no es suficiente para tener visibilidad real de quién entra y qué pide.

**[****57:19****] Alejandro — Go High Level con Claude Code** Quiere montar en Go High Level un sistema para entrenadores con pipeline, citas, seguimiento y métricas.

Respuesta: sí se puede conectar Go High Level con Claude Code via MCP. Hay contenido en camino en el Classroom específicamente sobre eso.
