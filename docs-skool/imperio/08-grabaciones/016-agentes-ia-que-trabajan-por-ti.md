# Agentes IA que trabajan por ti

> Ruta: 🔴 Grabaciones › Agentes IA que trabajan por ti

**🎬 Vídeo (58.9 min):** https://www.youtube.com/watch?v=bQeDq6eptQg

---

**Problemas que resuelve:** Cómo estructurar agentes de IA especializados en Discord con acceso a backups de N8N, cómo manejar sistemas de agenda con múltiples recursos usando lógica de round robin, y cómo construir un SaaS funcional con vibe coding integrando generación de imágenes, billing con Stripe y validación con IA.

---

**Intervenciones**

**[00:00] Tomás – Agentes especializados en Discord con acceso a GitHub** Comparte el setup de su equipo: dos agentes en Discord (Claudio y Gandalf), cada uno con rol específico. Gandalf está especializado en N8N, tiene acceso a backups de GitHub con 430 flujos y resolvió un problema de producción un viernes a la noche en 15 minutos. Detalla cómo el agente aprendió solo el límite de caracteres de Discord y lo incorporó a su memoria.

**[08:40] Franco – Configuración de permisos y conexión con AirTable** Explica cómo conectar agentes a AirTable mediante token con permisos limitados (solo lectura) como buena práctica de seguridad. Comenta el plan de conectar Gandalf a Anthropic y los riesgos de darle acceso directo al VPS principal en esta etapa.

**[09:28] Franco y Tomás – Canales de voz en Discord con OpenClow** Intercambio sobre la posibilidad de habilitar canales de voz para agentes en Discord, con la aclaración de que requiere actualización y configuración específica.

**[11:21] Bloque abierto – Ideas y dudas de la comunidad** Franco abre el espacio para elegir entre resolver dudas (modo martes) o explorar instalaciones de OpenClow. Se abre la sesión a preguntas.

**[12:10] Juaco – Gestión de campañas de Meta Ads desde Claude Code** Comenta el video de Benja sobre control de campañas de meta ads desde Claude Code. Pregunta cómo manejar generación automática de creativos con Nanobanana para imagen y video.

**[14:18] Franco – Generación de carruseles con agente + Nanobanana** Explica cómo entrena a su agente de OpenClow para generar carruseles con identidad de marca consistente, usando fotos de referencia del creador. El agente pide contexto, genera las imágenes y las sube a Mission Control con copy y hashtags listos.

**[16:22] Franco – Generación de video: límites y arquitectura** Aclara que Nanobanana genera imágenes, no video. Para video se requiere modelo como Veo o HeyGen. Para videos largos, recomienda usar FFMPEG como microservicio en VPS que pegue clips cortos y entregue el video final montado.

**[18:29] Tomás – Caso de cliente: reutilización de contenido existente** Describe el proyecto de automatizar la generación de nuevo contenido a partir de 250 videos ya subidos de una clienta coach, sin intervención manual.

**[23:55] Nuevo participante – Workflow de clonación de avatar con HeyGen** Primer ingreso a la sesión. Comparte que tiene clientes con avatar clonado y flujo de scraping + reformulación de contenido con output listo para editar. Ofrece compartir el workflow.

**[25:23] Franco – Cómo entregar proyectos con OpenClow o Antigravity** Responde pregunta de Octavio. Para OpenClow: se configura en el VPS del cliente, se entrega video y manual de usuario. Los cambios futuros se cobran mensualmente. Para Antigravity: se entregan skills y archivos preconfigurados que ayuden al cliente a desarrollar.

**[27:33] Florencia – Agente WhatsApp recepcionista + outbound para clínica** Consulta si usar el mismo número de WhatsApp del cliente (ya usado por la recepcionista) o crear uno nuevo para el agente. También pregunta cómo manejar inbound y outbound en el mismo número.

Solución: con WhiteCloud (API oficial) no hay riesgo de bloqueo haciendo inbound y outbound en el mismo número. El foco debe estar en el UX: quién lee las conversaciones derivadas, cómo se segmentan los chats y cómo se notifica al humano cuando la IA deriva.

**[31:52] Anónimo – Cómo detectar si un número fue baneado en Evolution** Pregunta cómo identificar un baneo. Respuesta: Evolution tira error HTTP (400 o 500) y el mensaje directamente no se envía. WhiteCloud además envía un mail de notificación.

**[33:23] Lucas – Sistema de turnos para barbería con múltiples barberos** Ex barbero que quiere automatizar los turnos de una barbería con 4 o 5 barberos. Consulta cómo manejar la asignación y la agenda por barbero.

Solución: usar [cal.com](http://cal.com) o Calendly como base. Para el round robin, mantener una tabla externa en N8N con registro del último barbero asignado. Cada vez que entra un nuevo turno, el flujo consulta la tabla, detecta a quién le toca y lo asigna. Lógica pura, sin depender de funciones nativas de la herramienta de calendario.

**[39:15] Ricardo (vía chat) – Comparativa de modelos: Anthropic vs Open AI vs Minimax** Consulta sobre costos y rendimiento. Franco explica: Open AI por defecto para agentes por costo, Anthropic cuando el agente falla o necesita mejor razonamiento lógico, Minimax para consultas simples y baratas. Carlos agrega que Codex le resolvió un problema de Stripe que Opus 4.6 no logró.

**[43:57] Ricardo (vía chat) – Web app para descarga de adjuntos de Gmail** Comenta que tiene una web que descarga adjuntos de correos no leídos por etiqueta, pero no identifica los que fallaron y no puede desconectar el flujo correctamente.

Solución sugerida: para uso interno, reemplazar la web app por una interfaz de AirTable con botón que dispare un webhook para encender/apagar el workflow. Para vender, mantener el formato web pero resolver la lógica de estado con flags en N8N.

**[48:32] Carlos – Demo en vivo: Renderly, SaaS de virtual staging** Muestra la aplicación terminada construida 100% con Claude Code. Incluye: panel admin con MRR y churn, validación de imágenes con IA antes de procesarlas, estilos precargados y custom description, generación en 2K y 4K, video walkthrough de habitaciones, marca de agua configurable por tier, comparación lado a lado y billing completo con Stripe. Tardó 4 días para el MVP y una semana más para la versión 2 con auditoría de seguridad, rate limits y force para las APIs.

**[57:27] Franco – Cómo manejar costos de API en un SaaS** Carlos responde: usa Kie como capa intermedia (más barato que consumir Google directamente), autorrecarga para no tener caídas, modelos fallback para imagen y video, y rate limits por IP (3 imágenes por minuto, 10 por hora).

**[58:30] Cierre** Franco destaca el trabajo de Carlos como ejemplo concreto de lo que se puede construir con vibe coding. Cierra invitando a seguir el martes.
