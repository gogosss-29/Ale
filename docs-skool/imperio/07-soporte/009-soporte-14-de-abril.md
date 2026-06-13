# Soporte - 14 de Abril

> Ruta: 🛠️ Soporte › Soporte - 14 de Abril

**🎬 Vídeo (79.5 min):** https://www.youtube.com/watch?v=jzkbI8moX8A

---

**Problemas que resuelve:** Cómo automatizar tareas con scraping web usando Claude Code, cómo estructurar contexto y memoria en proyectos con Obsidian/LLM wiki, cómo organizar subagentes en Claude Code por proyectos y nivel de usuario, cuándo usar Claude Managed Agents vs Claude Code, y cómo construir agentes de seteo en Instagram para calificación de leads.

---

**Intervenciones**

**[****00:00****] Franco – Apertura y dinámica de la sesión** Explica el formato de preguntas y respuestas en vivo. La mecánica es libre: desmutear, levantar la mano o comentar. Se abre el espacio para que cada participante traiga obstáculos reales de desarrollo.

**[****01:28****] Gonzalo – Automatización de revisión judicial en Chile** Es abogado y necesita revisar diariamente un portal judicial estatal ([oficinajudicial.cl](http://oficinajudicial.cl)) que requiere login con clave única. Quiere automatizar la revisión de sus causas y recibir un resumen.

Solución: usar scraping con Playwright para simular navegación con credenciales, crear una skill en Claude Code con el método afinado, y ejecutarla de forma periódica (cron job). Recomendación: empezar con el plan $20 usando modo planificación antes de ejecutar, para no desperdiciar contexto.

**[****12:15****] Carlos – Bot de atención y calificación de leads para negocio de limpieza** Tiene un CRM conectado a WhatsApp, Facebook e Instagram. Necesita atender leads entrantes fuera de horario y calificar el 30% que realmente vale. Duda entre construirlo él solo o contratar a alguien.

Solución: dado que el negocio ya tiene publicidad frenada por falta de atención, lo más eficiente es contratar un proveedor dentro de la comunidad. Se lo orienta a publicar en la comunidad y se confirma que hay capacidad de desarrollo disponible.

**[****17:25****] Cristian – Análisis de conversaciones de WhatsApp para detectar patrones** Tiene una startup con tres números de WhatsApp Business (soporte, comercial y propio). Quiere conectar IA para analizar conversaciones e identificar patrones de comportamiento de leads y clientes.

Solución: primero conectar los números a Whacloud para externalizar y guardar conversaciones en tiempo real. Luego pasar las conversaciones a data estructurada (Excel con columnas por característica: tipo de reclamo, emoción, tiempo de resolución, etc.). Eso permite análisis cuantitativo y dashboards en lugar de opinología subjetiva.

**[****25:09****] David – Dónde concentrar el contexto del negocio para campañas de Meta y Google** Conectó Claude Code con Meta, Google y LinkedIn para automatizar campañas. No sabe dónde guardar toda la información de marca (colores, tipografía, tono) de forma que sea reutilizable y eficiente en tokens.

Solución: usar Obsidian como LLM wiki — una carpeta local con archivos markdown vinculados entre sí. Claude Code la toma como contexto disponible permanente. Permite conectar documentos, clientes, flujos y metas en una estructura de grafos que el modelo puede consultar. Recomendación: pasar el manual de marca de docx a markdown y cargarlo en la carpeta del proyecto.

**[****33:04****] Arturo – Cómo mejorar el uso de skills en Claude Code para un proyecto web** Está usando Claude Code + VS Code para construir un sitio web de casas modulares. Instaló skills de la comunidad pero no obtiene resultados precisos. Tiene docx, renders e imágenes pero no sabe cómo pasarlos bien al modelo.

Solución: los archivos docx no los lee bien el modelo; pasar todo a markdown usando Claude Desktop. El manual de marca también debe convertirse a MD con los códigos de color y tipografías. Las skills de Claude Chat no se comparten con Claude Code — hay que cargarlas directamente en la carpeta del proyecto en VS Code. Mejor aún: pedirle a Claude que adapte cada skill a las necesidades específicas del proyecto antes de instalarla.

**[****46:48****] Axel – Cómo hacer Claude Code proactivo y controlarlo desde Telegram** Quiere que Claude actúe sin que él lo inicie manualmente, y quiere controlarlo por Telegram aunque esté lejos o con el computador apagado.

Solución para proactividad: usar el comando `/schedule` en Claude Code (crea un cron job nativo) o usar Claude Managed Agents (CMA) para tareas que deben correr en la nube sin depender del computador. Para control remoto con computadora encendida: conectar un canal de Telegram o Discord al entorno local. Para el caso sin computadora: CMA es la opción, ya que vive en la infraestructura de Anthropic y se despliega como endpoint.

Concepto clave explicado: diferencia entre un agente generalista (contexto contaminado, ventana sucia) y un agente especializado (contexto limpio, un solo objetivo). Mientras más enfocado es el agente, mejor funciona. No siempre conviene tener un agente que lo haga todo.

Sobre automatización de Instagram: usar siempre la API oficial de Meta para publicar — evita riesgo de baneo y cumple todas las reglas.

**[****59:16****] Miguel – Un agente por cliente o un agente para todos los clientes** Trabaja con múltiples clientes en pauta publicitaria y quiere saber si conviene tener un agente trafficker por cliente o uno solo para todos.

Solución: lo que importa no es cuántos agentes sino que el contexto de cada cliente esté bien separado. Se puede tener un agente orquestador (el "CEO") que conoce el negocio general y llama a subagentes especializados (trafficker, desarrollador web, SEO) con contexto limpio cada vez. Los subagentes deben crearse a nivel usuario (no a nivel proyecto) para que estén disponibles en cualquier carpeta. Usar `/context` para monitorear qué está consumiendo la ventana y evitar que imágenes en memoria inflen el uso innecesariamente.

**[****1:10:40****] Rodrigo – Agente setter para calificación de leads en Instagram** Tiene un negocio de inversión inmobiliaria. Hoy usa setters humanos en Instagram para calificar leads y derivarlos a un closer vía Calendly/GHL. Quiere automatizar el 100% del seteo.

Solución: sí es completamente viable. El flujo recomendado es ManyChat → webhook → Make/N8N → Claude (Sonnet 4.6) con system prompt bien definido. El agente debe estar acotado al 95% de los casos — no intentar contemplar todos los edge cases. Incluir un handoff humano para casos que no puede resolver. Mientras más corto y definido sea el seteo, mejor funciona el modelo. Usar Claude Sonnet 4.6 para mantener el tono humano que requiere la venta de alto valor.
