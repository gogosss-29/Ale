# Claude Code, subagente, modelos y ahorro de tokens

> Ruta: 🔴 Grabaciones › Claude Code, subagente, modelos y ahorro de tokens

**🎬 Vídeo (67.3 min):** https://www.youtube.com/watch?v=4sTsuS0Zqq0

---

**Problemas que resuelve la sesión 17 de Abril:** Cómo estructurar subagentes en Claude Code sin inflar el consumo de tokens, cómo optimizar el uso de modelos por tarea y cómo testear agentes de WhatsApp antes de salir a producción.

---

**[****00:00****] Miguel – Agente trafficker digital con resultados incorrectos** Comparte que construyó un sistema multi-agente con un orquestador CEO y subagentes especializados (trafficker, diseñador, vendedor). El agente trafficker genera copies con errores de codificación, presupuestos mal configurados y creativos de baja calidad.

Solución: revisar que cada subagente tenga el modelo explícitamente definido en su [CLAUDE.md](http://CLAUDE.md). Si no se especifica, el subagente hereda el modelo del orquestador. Para tareas creativas, usar Sonnet u Opus según complejidad; para tareas simples, Haiku.

**[****10:00****] Carlos – Estructura de carpetas y contexto por cliente** Explica cómo organizar subagentes a nivel usuario versus nivel proyecto. Los subagentes a nivel usuario son invocables desde cualquier carpeta; los de proyecto viven solo en esa carpeta. Recomienda separar el contexto del cliente en un [CLAUDE.md](http://CLAUDE.md) corto (menos de 200 líneas) y una carpeta `/contexto` con markdowns adicionales. Muestra su flujo con Obsidian como wiki indexado por Claude Code.

**[****22:00****] Juan – WhatsApp BSP: ¿qué plataforma usar?** Consulta sobre JCloud como alternativa a Evolution API. Franco explica la diferencia entre API oficial (WhiteCloud como BSP Premier, sin riesgo de baneo pero con más restricciones) y API no oficial (Evolution, Waha, Ziper). Recomendación: API oficial para clientes, no oficial solo para uso interno donde el riesgo de baneo es aceptable.

**[****27:00****] Juaco – Ziper como alternativa a Evolution** Presenta Ziper como herramienta similar a Evolution, con soporte de coexistencia y conexión por QR. Lo tiene en producción para un bot propio con buenos resultados. Carlos agrega Waha como otra alternativa válida para pruebas internas.

**[****38:00****] Carlos – Certificación como Meta Tech Provider** Comparte que está en proceso de convertirse en proveedor técnico de Meta para hacer onboarding directo a la API oficial, eliminando la dependencia de BSPs como WhiteCloud.

**[****40:00****] Tips de optimización de tokens en Claude Code** Carlos y Franco comparten estrategias: usar rutinas para correr tareas a la 1 AM cuando los tokens son más baratos, hacer rewind en lugar de corregir en el siguiente mensaje, cancelar ejecuciones con Escape para evitar gastar tokens de output, y bajar el nivel de razonamiento cuando la tarea no lo requiere.

**[****51:00****] Tomás – Generación de thumbnails y testeo de agentes** Pregunta cómo crear thumbnails consistentes y cómo testear agentes antes de producción.

Solución thumbnails: subir imagen de referencia a Gemini, pedirle que la desglose en JSON por capas (colores, tipografía, layout, CTA), y usar ese JSON como prompt para Flux/Imagen3 Pro en plataformas como Hisfield o Freepick.

Solución testeo: usar trigger de chat en N8N en lugar de WhatsApp para testear el prompt del agente sin costos de mensajería. Para testear el flujo completo (manejo de audios, imágenes, reacciones), Carlos recomienda capturar los payloads reales con un número de prueba, guardarlos como JSON y simularlos desde un webhook interno desconectado de WhiteCloud.

**[****1:06:58****] Cierre** Franco resume: estructurar bien las carpetas, definir modelos por subagente y testear exhaustivamente antes de producción. Próxima sesión: martes.
