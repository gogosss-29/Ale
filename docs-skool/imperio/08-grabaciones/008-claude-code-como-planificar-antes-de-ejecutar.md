# Claude Code: cómo planificar antes de ejecutar

> Ruta: 🔴 Grabaciones › Claude Code: cómo planificar antes de ejecutar

**🎬 Vídeo (58.9 min):** https://www.youtube.com/watch?v=n0Br3HBRVR4

---

**Problemas que resuelve la sesión 1 de Mayo:** Cómo usar Claude Code con planificación real antes de ejecutar, cómo conectar N8N con Claude a través de MCP y skills, y cómo resolver problemas de login y configuración inicial para quienes recién arrancan.

---

**Intervenciones**

**[****00:00****] Juan – Automatización de cuentas a pagar en agencia de marketing** Comparte el caso de una agencia con presencia en España, México y Estados Unidos donde todo el proceso de AP (accounts payable) es manual: descarga de facturas por mail, registro en Excel, renombrado de archivos, seguimiento de pagos. Intentó automatizar con Power Automate y Claude, con resultados parciales. El flujo creaba la pestaña correcta pero sin datos. Solución: avanzar hacia N8N como herramienta principal. Recomendación de arrancar por un proceso acotado, sin criterio humano necesario, y automatizarlo primero antes de escalar.

**[****05:10****] Franco – Framework para encarar la automatización desde cero** Explica por qué el error más común es querer automatizar todo de golpe. Propone identificar un proceso concreto, mapearlo en pasos y automatizar solo los pasos mecánicos primero. El criterio del usuario entra después. Recalca la importancia de aprender gestión de contexto en Claude Code: separar la sesión de planificación (Opus) de la sesión de ejecución (Sonnet).

**[****13:30****] Franco – Cómo usar Claude Code bien desde el principio** Explica la diferencia entre usar Claude como chat versus Claude Code. Introduce el concepto de planificación con subagentes antes de ejecutar. Muestra cómo decirle a Claude que investigue cada paso del plan para anticipar problemas antes de que aparezcan en la ejecución.

**[****19:00****] Pablo – Diferencia entre skills y MCP para N8N** Pregunta sobre el funcionamiento de la skill de N8N y en qué se diferencia del MCP. Actualmente genera JSON desde Claude y lo importa manualmente a N8N. Solución: las skills le enseñan al modelo cómo funciona N8N y qué hacer. El MCP es la conexión directa que le permite actuar. Juntos se complementan: uno entiende, el otro ejecuta. Carlos agrega que el nuevo SDK nativo de N8N hace que Claude genere flujos en código real, no en JSON, lo que reduce errores.

**[****26:00****] Daniel – Problema de login de Claude Code en Visual Studio Code** No puede completar la autenticación porque el sistema abre el navegador equivocado (Firefox sin sesión iniciada, en lugar de Chrome donde tiene la cuenta). Solución en vivo: iniciar sesión en [Claude.ai](http://Claude.ai) desde Firefox, volver a intentar la autenticación desde VS Code. Una vez con sesión activa en el navegador correcto, el flujo de autorización se completa sin problemas.

**[****38:00****] Franco – Planificación real con Claude Code: caso LinkedIn Sales Navigator** Muestra en pantalla su proceso de esta mañana. Partió de un contexto de negocio cargado en Obsidian y le pidió a Claude que leyera todo, planificara y creara subagentes para investigar cada punto antes de ejecutar. El resultado fue un plan de casi 400 líneas que sirve de base para una sesión autónoma nocturna. Clave: usar Opus para planificar, guardar un brief compacto, y abrir una sesión nueva limpia para ejecutar. Concepto central: preparar a Claude como se prepara a una persona antes de que salga a trabajar sola.

**[****52:00****] Carlos – Pregunta sobre LinkedIn Sales Navigator y Playwright** Consulta sobre cómo se complementan ambas herramientas para un cliente que quiere hacer outreach automatizado por DM. Respuesta: Sales Navigator filtra y arma listas de prospectos. Playwright navega LinkedIn por ellos y ejecuta las acciones. Advertencia: LinkedIn aplica shadow ban rápido con automatizaciones en masa, hay que tener cuidado.

**[****57:30****] Cierre** Franco resume la importancia de la planificación como inversión que reduce tokens y errores en la ejecución. Daniel agradece la ayuda con el login desde Montevideo. Sesión cerrada con invitación a la próxima del martes.
