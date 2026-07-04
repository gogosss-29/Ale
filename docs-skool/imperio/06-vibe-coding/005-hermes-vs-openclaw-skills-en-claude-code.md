# Hermes vs OpenClaw + Skills en Claude Code

> Ruta: Vibe-Coding › Hermes vs OpenClaw + Skills en Claude Code

---

**Problemas que resuelve la sesión del 13 de Mayo: **Cómo migrar de OpenClaw a Hermes, cómo estructurar Skills a nivel usuario y proyecto en Claude Code, y cómo conectar agentes autónomos a infraestructura local o en VPS para mayor control y estabilidad.

---

**Intervenciones**

**[****00:00****] Joaco & Benjamín – Novedades de Imperio Digital** Anuncian el concurso "1.000 miembros, 1.000 sistemas" con premio de $100 USD. Presentan el nuevo buscador semántico con RAG y vectorización en Pinecone dentro del OS agéntico de la comunidad, que incluye roadmap gamificado y guía personalizada de recursos.

**[****10:49****] Carlos – Contexto y agenda de la sesión** Introduce el tema central: comparativa entre OpenClow y Hermes. Comparte que ya lleva una semana con Hermes corriendo en Mac Mini junto a Claude Code y OpenClow, conectados vía MCP local.

**[****11:45****] Carlos – ¿Qué es Hermes y en qué se diferencia de OpenClow?** Explica que Hermes es desarrollado por Neus Research como evolución de OpenClow. Diferencias clave: mejor sistema de memoria persistente nativo, auto-mejora basada en feedback, dashboard visual propio, app de escritorio, y alertas interactivas de permiso antes de ejecutar comandos (similar a human-in-the-loop). Carlos lo corre con DeepSeek V3 Pro vía OpenRouter por $10/mes y lo prefiere sobre OpenClow por velocidad y calidad de respuestas.

**[****18:33****] Arturo – Consulta sobre hardware y configuración** Pregunta sobre qué Mac Mini comprar para correr agentes. Carlos aclara que para solo correr OpenClow o Hermes cualquier equipo es suficiente; los modelos locales requieren mínimo 32 GB de RAM. Arturo comparte que usa Claude Code con Gemini 4 vía API gratuita como LLM.

**[****22:00****] Carlos – Infraestructura recomendada: OpenClow + Hermes + Claude Code** Muestra cómo conectar los tres en la misma máquina vía MCP local, permitiendo que Hermes o OpenClow deleguen tareas a agentes especializados de Claude Code sin duplicar trabajo.

**[****28:45****] Carlos – Seguridad en Hermes** Confirma que las capas de seguridad son idénticas a OpenClow: Tailscale, cierre de puertos, usuarios no-root. La ventaja de Hermes es que pide autorización nativa desde Discord antes de ejecutar cualquier comando nuevo.

**[****31:10****] Max – Consulta para recién llegado** Pregunta por dónde empezar. Carlos recomienda comenzar con Claude Code antes de tocar Hermes u OpenClow, para entender el motor antes de orquestar desde afuera.

**[****38:26****] Arturo – Asistente financiero personal** Presenta la idea de un asistente que rastree inversiones, cripto y gastos desde el teléfono. Carlos recomienda Claude Code + PostgreSQL en local + deploy por Docker + agente con permisos de lectura/escritura controlados por tabla.

**[****43:10****] Ronald – Problema con gateway y Tailscale en VPS** No puede abrir el dashboard de OpenClow. Carlos diagnostica el error: el gateway está en modo LAN en lugar de BIND/Loopback, que es el necesario para funcionar con Tailscale. Recomienda abrir Claude Code desde la carpeta raíz de OpenClow para hacer el troubleshooting directamente sobre los archivos de configuración.

**[****56:00****] Carlos – Skills: estructura, niveles y buenas prácticas** Explica la diferencia entre Skills a nivel usuario (disponibles en todos los proyectos) y a nivel proyecto (disponibles solo en esa carpeta). Recomienda no instalar Skills genéricas sin adaptarlas, y usar un índice para gestionar bibliotecas grandes sin saturar el contexto. Muestra además cómo pasar de Markdown a HTML para mejor legibilidad humana, con sincronización automática entre ambos formatos.

**[****01:04:45****] Cris – Primera sesión: dudas sobre Skills** Pregunta cuántas Skills se pueden cargar y cuál es el límite. Carlos explica la lógica de tokens y contexto, y por qué instalar demasiadas Skills o MCPs puede degradar el rendimiento del agente.

**[****01:13:40****] Joaco & Carlos – Skills vs Prompts y venta de Skills** Distinguen que una Skill es un prompt estructurado e invocable. Carlos confirma que sí es posible monetizar Skills empaquetadas con agentes y configuraciones, que es parte de lo que ofrece en la Forja.

**[****01:33:15****] Leo – Flujo de trabajo real para landing pages con clientes** Consulta sobre errores al subir imágenes en Claude Design y qué herramienta usar. Carlos recomienda evitar Claude Design para proyectos con mucho contenido y trabajar directamente en Claude Code con Next.js, usando el repositorio gratuito "Forja Landing". Destaca que Hostinger ya permite deploy directo desde GitHub con dominio propio en un clic.

**[****01:47:35****] Carlos – GPTs personalizados: ¿todavía tienen mercado?** Confirma que sí, especialmente para adultos no técnicos que ya usan ChatGPT y no están listos para Claude Code. Es un nicho válido para un perfil de cliente específico.

**[****01:49:00****] Carlos – Design tokens y consistencia visual en apps** Muestra su sistema de showcase/UI kit local que le permite mantener paleta, tipografía y componentes consistentes a lo largo de toda una aplicación. Un solo cambio en el token se propaga automáticamente a toda la app.

**[****01:52:50****] Lester – ¿Claude Desktop o IDE para empezar?** Carlos recomienda empezar por Claude Desktop, que ya incluye conexión SSH a VPS. Para usuarios avanzados, IDEs como Cursor o Antigravity agregan extensiones, previsualizaciones y herramientas como Codex integrado.

**[****01:56:27****] Cierre** Joaco agradece la participación récord (37 conectados), anuncia sesión de bienvenida el jueves y próximo Bytecoding el miércoles siguiente.
