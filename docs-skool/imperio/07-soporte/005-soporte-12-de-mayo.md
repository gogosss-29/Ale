# Soporte - 12 de Mayo

> Ruta: 🛠️ Soporte › Soporte - 12 de Mayo

**🎬 Vídeo (59.7 min):** https://www.youtube.com/watch?v=msmBWZ6ATVE

---

**Problemas que resuelve:** Cómo conectar un agente de WhatsApp cuando Meta bloquea o demora la verificación del portfolio comercial, cómo usar WhatsApp coexistencia para automatizar sin perder el número activo, cómo procesar videos de walkthroughs técnicos para extraer transcripciones, timestamps y screenshots automatizados, y cómo arrancar con automatizaciones sin validar primero el método de negocio.

---

**Intervenciones**

**[01:20] Glenda – Chatbot bloqueado por verificación de Meta** Tiene todo el flujo armado y probado, pero no puede activarlo porque Meta lleva más de una semana revisando el portfolio comercial sin aprobarlo. Twilio tampoco es opción porque no tiene cobertura en España.

Solución: usar un BSP (Business Solution Provider) como Whitecloud, que actúa como intermediario entre el usuario y Meta. Permite crear un nuevo portfolio empresarial desde su plataforma y conectar el número directamente, sin depender de que Meta apruebe la cuenta anterior. En muchos casos el proceso tarda minutos.

**[12:45] León – WhatsApp personal para automatizaciones y número de empresa compartido** Quiere usar su WhatsApp personal como canal de automatización y también integrar un número de empresa donde un humano siga pudiendo atender.

Solución: Whitecloud permite conectar números por coexistencia. El bot automatiza respuestas y el agente humano puede seguir usando el mismo número desde la app normal de WhatsApp.

**[16:00] León – Supabase self-hosted vs cloud con MCP e Inforge** Pregunta si la versión cloud de Supabase limita la conexión MCP frente a una versión self-hosted.

Solución: es indiferente. El MCP y el CLI de Inforge se conectan a la URL del host sin importar dónde esté montado. Con Inforge funciona mejor el CLI que el MCP.

**[18:00] Flor – La Forja sobre Claude Code: qué es y cómo arranca** Recibió créditos en la comunidad y quiere invertirlos en La Forja. Pregunta si puede traer un proyecto de Codex y qué pasa si se quedó sin créditos de Claude.

Solución: La Forja es un arnés que vive encima de Claude Code e incluye skills, hooks y agentes especializados para construir MVPs desde cero contemplando diseño, seguridad y escalabilidad. No está pensada para Codex porque la arquitectura es exclusiva de Claude. Hay un plugin oficial para correr Codex dentro de Claude Code si se agotan los créditos propios.

**[24:25] Daniel – Walkthrough con lentes Meta: transcripción, timestamps y screenshots automáticos** Empresa HVAC documenta obras con lentes de grabación. Hoy anotan en papel y se les olvida todo. Quieren grabar el recorrido y que automáticamente se genere un resumen por sección con fotos del video.

Solución: es viable. La recomendación técnica fue usar FFMPEG (librería liviana que corre en cualquier servidor) combinado con MLX Whisper para extraer la transcripción con timestamps. Con esos datos se extraen frames en los momentos donde el técnico menciona algo relevante. Lo clave es normalizar el protocolo de grabación: que todos los walkthroughs empiecen desde el mismo punto y sigan el mismo recorrido (ej. planta baja a alta, en sentido horario) para que los timestamps sean coherentes entre grabaciones. No es necesario usar palabras clave para segmentar: el timestamp ya hace esa función.

**[47:30] Ricardo – Por dónde empezar siendo nuevo en la comunidad** Acaba de unirse, quiere agentizar su e-commerce con su esposa y no sabe por dónde arrancar.

Recomendación: no automatizar un método que todavía no se sabe si funciona. Primero validar el proceso a mano, y solo entonces automatizar. Para aprender, hay sesiones de automatización los lunes y jueves con Juaco. Claude es la herramienta base recomendada para arrancar.

**[43:45 / 51:50] Glenda – Continuación: sitio web y error en Meta** Al avanzar con Whitecloud, Meta le rechaza la URL del sitio web por temas de formato (www, https, barra final). También tiene activado Brave con VPN, lo que genera bloqueos adicionales.

Solución: usar Chrome sin VPN para este tipo de procesos. Si Meta sigue rechazando el sitio web, la opción es marcarlo como "mi empresa no tiene sitio web" y continuar igual. El campo es opcional.

**[57:40] Cierre – Calendario de School en iCal** Pregunta sobre cómo sincronizar el calendario de Skool con iCal.

Respuesta: desde el calendario del Classroom hay un botón para agregar eventos al calendario personal. Por ahora es evento por evento, pero se puede poner repetición para replicar la misma sesión hacia adelante. Están trabajando en un link centralizado que sincronice todos los eventos automáticamente.
