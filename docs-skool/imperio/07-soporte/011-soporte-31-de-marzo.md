# Soporte - 31 de Marzo

> Ruta: 🛠️ Soporte › Soporte - 31 de Marzo

**🎬 Vídeo (63.8 min):** https://www.youtube.com/watch?v=jbqUZxByFE4

---

**Problemas que resuelve:** Cómo reducir costos de API en Anthropic hasta un 90%, cómo implementar prompt caching con proxy en N8N, y cómo gestionar el contexto de forma eficiente en Claude Code.

---

**Intervenciones**

**[00:00] Franco – Contexto de la sesión** Introduce la dinámica de preguntas y respuestas del martes. Menciona el momento tecnológico actual con Claude Code y Clawdbot como herramientas de punta.

**[03:00] Franco – Qué es el prompt caching y por qué importa** Explica que el caché control es un parámetro de la API de Anthropic que permite guardar bloques del prompt para que las llamadas repetidas cuesten hasta un 90% menos. Presenta el caso real de un agente que pasó de gastar $180/mes a $30/mes aplicando esta técnica.

**[08:30] Franco – Cómo funciona el caché control (diagrama)** Muestra visualmente la estructura de un llamado HTTP a Anthropic: system prompt, user prompt, historial de conversación y tools. Explica qué parte del llamado se puede cachear y qué diferencia hay entre TTL de 5 minutos (1.25x el costo inicial) y 1 hora (2x), con llamadas posteriores al 10% del costo original.

**[15:00] Franco – Por qué N8N no lo permite nativamente y cómo solucionarlo** N8N no expone el parámetro cache_control en sus nodos nativos de Anthropic. La solución: desarrollar un proxy en Node.js con Claude Code (5 minutos de trabajo) que intercepta el llamado, le agrega el parámetro y lo reenvía a Anthropic. Pasos: desarrollar el proxy → alojarlo en un VPS con seguridad → cambiar la URL de la credencial de Anthropic en N8N.

**[24:00] Carlos – Context managing en Claude Code: el enfoque equivalente** Explica que en Claude Code el mecanismo análogo es el manejo del contexto: mantener un [CLAUDE.md](http://CLAUDE.md) conciso (200-300 líneas), no cargar skills innecesarios, y usar hooks que interceptan los requests antes de enviarlos para limpiar y reducir la información. El flag `/model opus plan` hace que Opus planifique y Sonnet ejecute, reduciendo hasta 5x el consumo.

**[36:00] Daniel – Aclaración sobre el objetivo del proxy** Pregunta si el proxy engaña a Anthropic sobre el origen del llamado. Franco aclara: el proxy en este caso solo agrega el parámetro cache_control, no cambia IPs ni evade rate limits. Son funciones diferentes aunque ambas se implementen con proxies.

**[47:00] Franco y Carlos – Síntesis: dos métodos, mismo objetivo** Cache control (para APIs y N8N): misma información, pero Anthropic la cobra más barato porque ya la procesó. Context managing (para Claude Code): se le manda menos información desde el inicio. Ambos reducen costos, en contextos distintos.

**[55:00] David – Estructura de directorios en Claude Code** Consulta cómo organizar carpetas en OneDrive para múltiples proyectos y líneas de negocio. Carlos responde: lo clave es tener una carpeta por proyecto con su propio [CLAUDE.md](http://CLAUDE.md). Claude Code solo ve la carpeta donde fue abierto, pero puede leer otras si se le indica explícitamente. El punto `.claude` es una carpeta oculta de configuración interna, no debe usarse para proyectos.

**[1:03:28] Cierre** Franco cierra invitando a la sesión del viernes y a la de Carlos del miércoles.
