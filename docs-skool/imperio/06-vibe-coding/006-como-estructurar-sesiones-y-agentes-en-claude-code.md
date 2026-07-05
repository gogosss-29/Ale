# Cómo estructurar sesiones y agentes en Claude Code

> Ruta: Vibe-Coding › Cómo estructurar sesiones y agentes en Claude Code

---

**Problemas que resuelve la sesión del 6 de Mayo: **Cuándo usar caché y hand-off entre sesiones de Claude Code, cómo estructurar documentos guía (Cloud.md, Blueprint, Roadmap, Task) sin generar ruido o alucinaciones, y cómo trabajar en paralelo múltiples proyectos con agentes (OpenClow vs. Hermes) aprovechando Obsidian como segundo cerebro conectado.

---

**Intervenciones**

**[00:00] Carlos – Anuncio: Anthropic duplica los límites de Claude** Comparte en vivo que Anthropic anunció una asociación con Starling que duplica el consumo de tokens cada 5 horas para planes Pro y Max, y elimina las restricciones de hora pico a partir del día de la sesión.

**[01:30] Carlos – Dinámica de la sesión** Propone formato de preguntas abiertas donde cada miembro comparte su caso, comparte pantalla y lo resuelven en conjunto. Ganó por votación: *Mejores prácticas de Claude Code*.

**[04:00] Joaco – Pregunta inicial: continuidad de sesiones y gestión de contexto** Plantea el tema central: cuándo conviene continuar una sesión con `/continue` o `cloud resume`, cuándo arrancar nueva, y cómo impacta en el consumo de tokens.

**[08:00] Carlos – Caché de prompt y lógica de sprints** Explica que si respondés en menos de 5 minutos el caché de prompt sigue activo, evitando que el modelo tenga que releer todo el contexto. Recomienda organizar el trabajo en sprints (una tarea acotada, trabajada de corrido) para maximizar este beneficio.

**[10:00] Carlos – Hand-off vs. sesión nueva vs. clear compact** Muestra su configuración de agente que genera automáticamente un documento `handoff.md` al cerrar un sprint. Explica cuándo usar hand-off (tareas relacionadas aunque distintas), cuándo arrancar sesión limpia (tareas sin vínculo), y cuándo hacer compact.

**[16:00] Carlos – Modos Plan y Build: Opus para planear, Sonnet para construir** Muestra cómo activar el modo plan para que Opus diseñe el plan y, al aprobarlo, cambie automáticamente a Sonnet para la construcción, reduciendo costos sin perder calidad de razonamiento.

**[17:30] Joaco – Diferencia entre Blueprint, Roadmap, Plan y Task** Consulta sobre los distintos documentos guía. Carlos responde: Blueprint es la biblia del proyecto, de la que se derivan en cascada Roadmap → Plan → Task. Mientras más desfase entre ellos, mayor riesgo de alucinaciones.

**[29:00] Pablo Valenzuela – Dónde vive el Cloud.md** Carlos aclara: existe un `CLAUDE.md` a nivel usuario (afecta todas las sesiones de todas las apps de Claude) y uno por proyecto (en la carpeta raíz). Recomienda que el de usuario solo contenga contexto general: quién sos, en qué lenguaje querés que te hablen, cuál es tu wiki.

**[31:00] Carlos – Obsidian como segundo cerebro conectado a Claude** Muestra su configuración: `CLAUDE.md` global apunta al índice de su vault de Obsidian. Claude entiende que existe ese contexto y lo consulta solo cuando es relevante, sin consumir tokens innecesarios en cada sesión.

**[36:00] Carlos – Cómo mantener actualizado el Wiki automáticamente** Describe su pipeline nocturno: un script a las 8:50 pm genera la nota diaria con LittleBird (app que escucha pantalla y audio), otro a las 9:50 pm procesa los JSON de Claude Code y genera un resumen de sesiones. Todo se ingesta en Obsidian vía Claude Code.

**[43:00] Eduardo – Cloud.md y estructura de agentes en un proyecto web** Comparte que su `CLAUDE.md` referencia una carpeta de agentes. Carlos valida la estructura y recomienda mantener el `CLAUDE.md` bajo 250 líneas, delegando detalle a un archivo `agents.md` separado.

**[48:00] Carlos – La Forja: framework para construir proyectos con Claude Code** Presenta La Forja, su framework open source (pago único, $75 con descuento). Cubre planeación, análisis de mercado, proyecciones financieras y construcción paso a paso. Incluye integración nativa con Claude Design para tokens de marca.

**[55:00] Dean – Cómo combinar La Forja con Claude Design** Consulta cómo usar los dos sin romper el flujo. Carlos muestra que La Forja tiene el comando `/design` integrado: primero usás `/landing`, y cuando el agente pregunta si tenés un diseño en Claude Design, le pasás la URL. El agente lo lee y aplica los tokens automáticamente.

**[57:00] Carlos – Coolify como alternativa a EasyPanel en VPS** Responde a José Luis (Venezuela) que instaló EasyPanel con problemas de acceso. Recomienda Coolify (gratuito, más potente, con MCP nativo para instalar stacks desde Claude Code). Instruye a resetear el VPS desde Hostinger y recomenzar limpio.

**[1:09:00] Carlos y Leandro – OpenClow vs. Hermes: dos agentes, roles distintos** Leandro comparte su experiencia corriendo ambos en el mismo VPS. Hermes es más conversacional, tiene memoria nativa (mem0), genera vídeos directamente orquestando herramientas. OpenClow es más operativo y robusto para tareas complejas. Carlos muestra en vivo un Reel generado 100% por Hermes usando su sistema de clonación de voz y edición automática.

**[1:38:00] David (España) – Seguridad en app web con backend PHP** Consulta sobre cómo auditar una app antes de publicarla. Carlos da tres pasos: (1) verificar que no haya API keys expuestas en el front, (2) configurar correctamente CORS, (3) hacer auditoría de seguridad con Codex generando un `audit.md` en una sesión y aplicando mejoras en otra sesión separada.

**[1:44:00] Cierre** Carlos comparte que Benja publicó un nuevo video sobre conexión de MCP con Claude Code y HikesField. Joaco cierra con invitación a la sesión de bienvenida del jueves.
