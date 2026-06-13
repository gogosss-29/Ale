# Tu agente programa solo mientras duermes

> Ruta: Vibe-Coding › Tu agente programa solo mientras duermes

---

**Problemas que resuelve la sesión 3 de Junio:** Cómo escalar una app personal a un SaaS multitenante, cómo orquestar agentes Hermes + Claude Code desde Telegram para desarrollo asíncrono, y cómo elegir entre N8N, código puro o Claude Cowork según el nivel del proyecto.

---

**Intervenciones**

**[****00:00****] Joaco & Carlos – Apertura y concurso de la comunidad** Dan la bienvenida a la sesión miscelánea del 3 de junio. Comentan el cierre del concurso comunitario y destacan el nivel general de los proyectos presentados: no solo ideas sino aplicaciones reales construidas en semanas.

**[****02:37****] Flor Vallejo – Big Workschooler: app para familias unschoolers** Comparte su proyecto ganador del concurso: una web app construida en una semana para documentar el aprendizaje informal de sus hijos durante un viaje por Europa en autocaravana. La app incluye diario de viajes, perfiles por hijo, tracking de hábitos, biblioteca de recursos con indexación de PDFs, recuerdos de viaje geolocalizados y reportes generados por IA con recomendaciones mensuales.

Problema inicial: no había forma de demostrar lo que hacían como familia. Solución: una plataforma completamente funcional, desplegada con su propio dominio, optimizada con Cloudflare, que indexa libros de Santillana y permite búsquedas semánticas por tema.

**[****08:11****] Carlos – Análisis técnico del proyecto de Flor** Destaca la calidad visual y de rendimiento de la app, comparable a productos comerciales. Explica el concepto de multi-tenancy (de single tenant a permitir múltiples familias con sus propios accesos), la importancia de separar repositorios de app y landing page, y cómo gestionar el despliegue de nuevas funcionalidades sin romper la versión en producción. Propone una sesión futura sobre este flujo de trabajo.

**[****20:15****] Carlos – OCR con GLM y búsqueda semántica en libros** Explica cómo indexar PDFs con cursiva mediante el modelo OCR de ZhipuAI (GLM OCR), líder en benchmarks y 16.000 veces más barato que GPT-3.5 para esta tarea. El flujo: subir PDFs a Drive → procesar con GLM OCR → guardar chunks con referencias de página en Supabase → consultar con búsqueda vectorial desde la app.

**[****25:00****] Carlos & Iván – Multi-tenancy y sincronización de hogares** Aclaran la diferencia entre varios usuarios dentro de un hogar (relación de tabla en Supabase con Realtime) versus multi-tenancy real (múltiples familias con sus propios espacios). Recomiendan usar Realtime de Supabase para sincronizar cambios entre usuarios del mismo hogar.

**[****28:00****] Iván Risso – Dónde comprar dominios** Pregunta sobre Godaddy vs Cloudflare vs Hostinger. Carlos recomienda Hostinger por la integración nativa entre VPS, deploy y dominios en un solo panel. Cloudflare y Namecheap son más baratos. Godaddy es más caro pero tiene integraciones automáticas con muchas plataformas.

**[****34:00****] Óscar Oyarzo – Cómo conecta lo público con lo local en la app de Flor** Pregunta cómo funciona la biblioteca si los PDFs son locales. Flor aclara: los libros viven en OneDrive y se indexan solo cuando ella los sube con un enlace. Cada familia cargaría su propio material. No hay libros compartidos ni almacenados públicamente en la app.

**[****41:45****] Daniel (Montevideo) – CRM conectado a Mercado Libre** Comparte que logró instalar Hermes, OpenClow y DeepSeek en Ubuntu siguiendo sesiones anteriores. Consulta sobre cómo construir un CRM para gestionar inventario, ventas, comisiones y márgenes conectado a Mercado Libre.

Solución de Carlos: primero documentar en detalle qué datos entran, cuáles salen y qué pasa en cada evento de compra. Luego cruzar ese plan con la documentación oficial de [developers.mercadolibre.com](http://developers.mercadolibre.com) y pasárselo a Claude Code junto con el Excel actual. Como punto de partida más accesible: usar Claude Cowork para analizar el Excel existente y automatizar cálculos directamente desde ahí.

**[****58:00****] Joaco – Plugins de Anthropic para pequeños negocios** Muestra los plugins de Claude (Small Business, entre otros): paquetes de Skills + conectores preconfigurados instalables desde la interfaz de chat. Permite activar Skills como "Monday Brief" (resumen semanal conectado a calendario y correo) o "Invoice Chase" (seguimiento de facturas pendientes). Útil como punto de entrada antes de llegar a Claude Code.

**[****1:02:00****] Joaco – Automatic: orquestación Hermes + Claude Code desde Telegram** Muestra su proyecto de chatbots automáticos para negocios. Un agente Hermes llamado Matic tiene acceso al repositorio en Vercel y a Claude Code en el VPS. Desde Telegram, Joaco le pide nuevas funcionalidades, Matic las desarrolla, crea ramas en Github y espera aprobación para el merge. El CRM operativo está en Notion, actualizado una vez por día. Un cliente activo (clínica de fertilidad) tiene el chatbot integrado en su web y WhatsApp con agendamiento conectado a [Cal.com](http://Cal.com).

Problema del día: Joaco agotó el tier gratuito de Gemini Embeddings (1.000 llamadas diarias) al pedirle a Matic que procesara todas las tiendas durante la noche.

**[****1:17:30****] Carlos – Cómo funciona la orquestación de agentes** Hermes no escribe el código directamente: orquesta, le pide a Claude Code que ejecute, recibe confirmación y notifica al usuario. Diferencia entre los tres tipos de agentes: local (en Claude Code), en N8N (nodo de agente con system prompt), y en producción para terceros (código puro, managed agents de Anthropic, o Legends SDK).

**[****1:23:00****] Agustín – Perplexity MCP + Claude y búsqueda en tiempo real** Carlos recomienda Perplexity para búsquedas en tiempo real (especialmente fuente social y Reddit) y Context7 para documentación técnica de plataformas. Para búsqueda en tiempo real también recomienda Exa AI de Groq.

**[****1:38:00****] Agustín – Autonomía del agente para desarrollar y desplegar** Carlos explica cómo dar permisos granulares: configurar un PAT de Github con scopes limitados, crear un usuario Github específico para el agente y definir hasta qué punto puede actuar (solo PR, sin merge a main). Recomienda conectar Sentry para que el agente detecte errores en producción y los trabaje con o sin intervención humana según el nivel de confianza definido.

**[****1:43:00****] Agustín – Agente como interfaz para clientes que no saben qué necesitan** Carlos advierte: si el cliente no sabe lo que necesita, un agente no puede resolverlo solo. Propone una capa intermedia: un agente con Skills de relevamiento que documente las ideas del cliente para que un humano las interprete y decida. Hermes permite crear grupos de Telegram con múltiples usuarios, filtrar quién puede interactuar con el agente y definir dónde se documenta cada conversación.

**[****1:47:00****] Iván – Cómo migrar un agente de N8N a código puro con Forge** Carlos indica: crear una carpeta nueva, correr forge init en consola, darle acceso a la carpeta del agente existente y pedirle el plan de migración. No contaminar el proyecto operativo.

**[****1:49:00****] Cierre** Joaco y Carlos cierran felicitando a Flor y anunciando próxima sesión sobre el flujo de desarrollo de nuevas funcionalidades en apps ya en producción.  
  
  
**Resumen:**  
Esta sesión se centró en la presentación y celebración del proyecto ganador del concurso comunitario, desarrollado por Flor.   
Flor presentó su aplicación web «Lechuza», diseñada para documentar y hacer seguimiento del aprendizaje informal de sus hijos en un entorno homeschooler/unschooler, que desarrolló en una semana con la ayuda de Claude y Forsch.   
La aplicación permite registrar actividades, hábitos, viajes y generar informes sobre el progreso académico de los niños utilizando inteligencia artificial para indexar el contenido de los libros de texto. Los participantes elogiaron a Flor por su evolución técnica y el nivel de calidad del proyecto desarrollado.   
La sesión también incluyó discusiones técnicas sobre desarrollo web, configuración de dominios, gestión de GitHub y la implementación de agentes como Hermes y OpenCloud para automatizar tareas de desarrollo. Carlos y otros miembros de la comunidad compartieron consejos sobre buenas prácticas para la creación de aplicaciones web y la gestión de proyectos en producción.
