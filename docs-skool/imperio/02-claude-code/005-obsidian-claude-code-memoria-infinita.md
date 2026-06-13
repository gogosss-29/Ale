# Obsidian + Claude Code = Memoria Infinita

> Ruta: Claude Code › Obsidian + Claude Code = Memoria Infinita

**🎬 Vídeo (33.5 min):** https://youtu.be/p5YgvC6yzCs

---

🧠 GUÍA DE IMPLEMENTACIÓN → LLM Wiki con Claude Code + Obsidian

Acá está todo lo que necesitas para tener tu propia memoria infinita funcionando en menos de 30 minutos, aunque nunca hayas usado Obsidian antes.

📺 Video tutorial completo: [https://youtu.be/p5YgvC6yzCs](https://youtu.be/p5YgvC6yzCs)

━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 QUÉ VAS A ARMAR

Un sistema donde Claude Code consulta y actualiza una wiki propia (archivos markdown interconectados como Wikipedia) antes de responderte. Sin RAG. Sin vectorización. Sin pagar infraestructura.

La misma carpeta funciona con Claude Code, OpenClaw, Manus, Genspark, o cualquier agente que lea archivos. 100% portable.

━━━━━━━━━━━━━━━━━━━━━━━━━━

🛠️ SETUP PASO A PASO

1. Descarga Obsidian

Entra a [https://obsidian.md](https://obsidian.md) y descarga la versión para tu sistema operativo. Cuando te pregunte por la cuenta de pago, dale en "continuar con versión gratuita". No la necesitas.

2. Crea tu primer Vault

Abre Obsidian → "Crear nuevo Vault" → ponle un nombre (ej: "mi-wiki") → elige una ubicación en tu computador donde quieras guardar los archivos → dale "Crear".

3. Abre esa misma carpeta en Claude Code

Aquí está la magia. Abre VS Code (o Cursor, Antigravity, donde uses Claude Code) y abre la MISMA carpeta que creaste como Vault. Las dos apps trabajan sobre los mismos archivos en tiempo real.

4. Copia la estructura de Karpathy

Ve al repo oficial (link abajo), copia el contenido del README, y pégalo en Claude Code con este prompt:

"Necesito que mantengas mi wiki organizada siguiendo esta estructura: [pega el README]. Crea el [CLAUDE.md](http://CLAUDE.md) con las reglas, el index, el log y las carpetas raw/ y wiki/."

5. Empieza a poblar

Ya tienes el sistema. Ahora le pasas fuentes (transcripciones, documentos, ideas, lo que sea) y Claude Code las clasifica automáticamente.

━━━━━━━━━━━━━━━━━━━━━━━━━━

🔗 RECURSOS OFICIALES

📄 LLM Wiki de Andrej Karpathy (GitHub)

El repo original con la estructura y las instrucciones. Cópialo y úsalo como base:

[https://github.com/karpathy/llm-wiki](https://github.com/karpathy/llm-wiki)

📄 Obsidian (descarga)

La app que visualiza tu wiki como grafo interconectado:

[https://obsidian.md](https://obsidian.md)

📄 Obsidian Clipper (Chrome Extension)

Plugin para mandar contenido desde Chrome directo a tu wiki. Útil para guardar tweets, artículos, papers:

[https://chromewebstore.google.com/detail/obsidian-web-clipper/cnjifjpddelmedmihgijeibhnjfabmlf](https://chromewebstore.google.com/detail/obsidian-web-clipper/cnjifjpddelmedmihgijeibhnjfabmlf)

📄 Plugins oficiales de Obsidian

Para extender funcionalidad (MCP, AI agents, sync, etc.):

[https://obsidian.md/plugins](https://obsidian.md/plugins)

📄 Tweet original de Karpathy

El post que lo popularizó:

[https://x.com/karpathy](https://x.com/karpathy)

━━━━━━━━━━━━━━━━━━━━━━━━━━

🧩 ESTRUCTURA DE ARCHIVOS

Cuando termines el setup, tu carpeta va a verse así:

/mi-wiki

├── [CLAUDE.md](http://CLAUDE.md)       → Las reglas del sistema (el alma)

├── [index.md](http://index.md)        → El mapa principal (lo primero que lee la IA)

├── [log.md](http://log.md)          → Registro de cambios

├── raw/            → Fuentes crudas sin clasificar

└── wiki/

    ├── conceptos/  → Ideas clave

    ├── entidades/  → Personas, empresas, herramientas

    ├── fuentes/    → Artículos, videos, papers

    └── sintesis/   → Resúmenes generados

Cada archivo markdown puede linkear a otros con [[nombre-archivo]]. Así se construyen las relaciones que ves en el grafo de Obsidian.

━━━━━━━━━━━━━━━━━━━━━━━━━━

⚙️ LAS 4 OPERACIONES BÁSICAS

Cuando hables con Claude Code sobre tu wiki, estos son los 4 comandos que vas a usar todo el tiempo:

INGEST → "Digiere este archivo y clasifícalo"

Para agregar una fuente nueva. Claude crea la página, la categoriza, le pone tags y la linkea con lo existente.

QUERY → "Busca en la wiki qué sabemos sobre X"

Para consultar. Claude navega desde el index hasta encontrar lo relevante.

LINT → "Revisa archivos huérfanos y conéctalos"

Mantenimiento. Toma archivos sin relaciones y los integra al grafo.

BULK INGEST → "Procesa todos estos archivos a la vez"

Para poblar rápido cuando tienes muchas fuentes iniciales.

━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 CASOS DE USO CON EJEMPLOS REALES

1. Base de conocimiento de tu negocio

Qué guardar: propuestas enviadas, precios cerrados, objeciones de clientes, casos de éxito.

Ejemplo: "Claude, un lead me pidió propuesta para automatizar su WhatsApp. Busca en la wiki propuestas similares y sus precios antes de redactar."

2. Memoria de código

Qué guardar: decisiones de arquitectura, bugs resueltos y sus soluciones, convenciones del equipo.

Ejemplo: "Tengo el mismo error de CORS que ya solucionamos antes. Revisa la wiki y dime cómo lo arreglamos la vez pasada."

3. CRM liviano

Qué guardar: resúmenes de calls, notas de prospectos, follow-ups pendientes.

Ejemplo: "¿Qué me dijo Juan de ACME en nuestra última call? ¿Qué acordamos como próximo paso?"

4. Content OS

Qué guardar: transcripciones de videos, hooks que funcionaron, patrones de thumbnails ganadores.

Ejemplo: "Basándote en los patrones de mis 10 videos con más views, sugiéreme 3 ideas para mi próximo video."

5. Cerebro de equipo

Qué guardar: procesos, SOPs, decisiones importantes, aprendizajes.

Funciona bien si sincronizas la carpeta con Google Drive, iCloud o Dropbox para que todo el equipo contribuya.

6. Segunda memoria personal

Qué guardar: notas de libros, insights de podcasts, conversaciones importantes, ideas.

Ejemplo: "¿Qué patrones conectan mis notas sobre liderazgo con lo que leí de psicología cognitiva?"

━━━━━━━━━━━━━━━━━━━━━━━━━━

✍️ PROMPTS LISTOS PARA COPIAR

Prompt 1: Setup inicial

"Voy a crear una wiki personal siguiendo el formato LLM Wiki de Karpathy. Crea la estructura base: [CLAUDE.md](http://CLAUDE.md) con las reglas del sistema, [index.md](http://index.md) como mapa principal, [log.md](http://log.md) para registro, y las carpetas raw/ y wiki/ (con subcarpetas conceptos, entidades, fuentes y síntesis). Usa markdown y links estilo [[nombre-archivo]] para las relaciones."

Prompt 2: Ingesta de una fuente nueva

"Ingiere este contenido en la wiki: [pega contenido o URL]. Clasifícalo en la categoría correcta, créale tags, extrae los conceptos clave, y linkea con archivos existentes que tengan relación. Actualiza el index y el log."

Prompt 3: Consulta profunda

"Busca en la wiki todo lo relacionado con [tema]. Empieza desde el index, navega las conexiones relevantes, y dame un resumen con los archivos fuente que consultaste."

Prompt 4: Sugerencia basada en patrones

"Analiza los archivos en wiki/fuentes/ y dime qué patrones se repiten en [X]. Crea un archivo de síntesis con los hallazgos."

Prompt 5: Mantenimiento (lint)

"Revisa todos los archivos de la wiki y encuentra los que están huérfanos (sin links entrantes o salientes). Propón conexiones con archivos existentes y aplícalas después de mi aprobación."

Prompt 6: Bulk ingest

"Toma todos los archivos que están en raw/ y clasifícalos. Créales su página en wiki/, extráeles conceptos clave, y linkéalos con los archivos existentes. Hazlo uno por uno y al final actualiza el index."

━━━━━━━━━━━━━━━━━━━━━━━━━━

🔌 PLUGINS RECOMENDADOS DE OBSIDIAN

Dentro de Obsidian ve a Configuración → Community Plugins → Browse. Estos son los que más valor agregan:

Obsidian Web Clipper

Para mandar contenido desde Chrome directo a tu wiki. Funciona con tweets, artículos, papers.

MCP Tools

Conecta tu Vault con servidores MCP para que otros agentes lean tu wiki directamente.

Dataview

Convierte tu wiki en una base de datos consultable. Útil para dashboards.

Templater

Plantillas automáticas para que cada archivo nuevo siga una estructura consistente.

Smart Connections

Sugiere relaciones entre archivos usando embeddings. Complementa bien el sistema de links manuales.

Git

Sincroniza tu Vault con GitHub para backup y trabajo en equipo.

━━━━━━━━━━━━━━━━━━━━━━━━━━

🚨 TROUBLESHOOTING COMÚN

"Claude Code no ve los archivos de mi Vault"

Asegúrate de abrir la MISMA carpeta raíz del Vault en VS Code. No una subcarpeta. Si abriste una subcarpeta por error, cierra y abre la raíz.

"Los links [[nombre]] no se ven como enlaces"

Obsidian los renderiza en modo "Reading View". Cambia el modo con Ctrl/Cmd + E. En modo "Edit" se ven como texto plano.

"Claude clasifica mal las fuentes"

Edita el [CLAUDE.md](http://CLAUDE.md) con reglas más específicas. Ejemplo: "Los archivos que mencionen clientes van a wiki/entidades/clientes/. Los que mencionen herramientas van a wiki/entidades/herramientas/."

"Mi grafo está caótico, con nodos sueltos"

Corre el prompt de lint. Claude va a conectar los archivos huérfanos con el resto. Hazlo cada 1-2 semanas como mantenimiento.

"Obsidian tarda mucho en abrir"

Si tienes miles de archivos, desactiva plugins que no uses. Los plugins de sync en tiempo real son los que más pesan.

"Se me borró el [CLAUDE.md](http://CLAUDE.md) por accidente"

Obsidian tiene "File Recovery" activo por defecto. Ve a Configuración → Core Plugins → File Recovery y recupéralo de las versiones guardadas.

"Quiero usar mi wiki con OpenClaw en vez de Claude Code"

Simplemente abre la misma carpeta con OpenClaw. El [CLAUDE.md](http://CLAUDE.md) se lee igual (OpenClaw respeta ese archivo). Si usas otro agente, copia el contenido de [CLAUDE.md](http://CLAUDE.md) a [AGENTS.md](http://AGENTS.md) o [GEMINI.md](http://GEMINI.md) según corresponda.

━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 PRÓXIMOS PASOS

1. Mira el video completo si no lo has hecho: [https://youtu.be/p5YgvC6yzCs](https://youtu.be/p5YgvC6yzCs)

2. Arma tu wiki vacía siguiendo el setup de esta guía (30 min max)

3. Elige UN caso de uso de la lista y empieza por ahí. No intentes todo a la vez.

4. En 1 semana, corre el prompt de lint para ver cómo creció tu grafo.

5. Trae tus dudas a las sesiones en vivo de Claude Code → martes y viernes.

━━━━━━━━━━━━━━━━━━━━━━━━━━
