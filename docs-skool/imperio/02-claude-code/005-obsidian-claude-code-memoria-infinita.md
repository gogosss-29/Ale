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

## 🎙️ Transcripción

Lo que acabamos de armar es literalmente una memoria infinita. Lo que estás viendo son 88 de mis videos de YouTube organizados en un sistema que se construye solo. Cada uno de estos puntos es un video y cada línea entre videos es una conexión o relación entre herramientas, conceptos, etcétera. Por ejemplo, este de acá en mi video de OpenCloud versus Cloud Code. Y como vemos está conectado a OpenClow aquí y conectado a Cloud Code acá. Y si es que lo aprieto, vamos a ver que me puede referenciar a los otros videos, cómo está estructurado, etcétera. Volviendo acá, por ejemplo, fíjate como Cloud Code está conectado a cada uno de los videos y de los conceptos. Por ejemplo, este de gente en 18 minutos también tocamos OpenCloud. Entonces, se conecta para acá, también se conecta a, no tengo idea, Mac Mini. Macmini se conecta a cómo usar Openclor que el 99% de las personas. Open Close se relaciona a agentes IA y así constantemente, pero eso no es lo más loco porque yo puedo preguntar qué patrones se repiten en los videos que mejor le fue en los últimos meses y me responde y me crea un archivo tipo el ecosistema tecnológico, la llegada de OpenCloud, la tesis de la economía de tokens, ¿verdad?, que se correlaciona justamente con cuándo empezó el spike de los videos de YouTube. O le puedo decir, estoy pensando en hacer un video sobre agentes y la economía de tokens. en algún video toqué esto y va a entrar y va a consultar dentro de todo este arsenal al final de archivos y me va a decir, "Sí, ya lo tocaste exactamente acá, pero no he hecho esta conexión explícitamente, por ejemplo." Y esto que estás viendo se llama un llm wiki popularizado por Andres Carpaty en este tweet que hizo acá. Andre Carpaty es uno de los grandes conocidos, tiene más de 18,0000es de views solamente esta publicación de Twitter y lo puedes descargar directamente desde esta librería que es completamente gratis y pública. Lo que estás viendo también en esta aplicación es una interfaz que se llama Obsidian, que nos ayuda a ordenar los archivos Markdown de una manera que se correlacionan entre sí. Y quizás te estás preguntando un par de cosas, ¿cómo funciona esto? ¿Reemplaza esto al rack? ¿Qué casos de uso le puedo dar? ¿Cómo lo populamos? ¿Cómo sacó los videos? Y todo eso te lo voy a responder en este video, además de mostrarte paso a paso cómo podemos montar un sistema como este, que podemos usar perfectamente en aplicaciones como estilo chatbots, cómo lo conectamos con distintos agentes y cómo podemos empezar a aplicarlo para tus proyectos para que de esta manera tu negocio, tu canal, lo que sea, tenga una memoria consistente que no se olvide de las cosas y no pase un periodo de compactación donde se olvida todo lo anterior. Y para el final de este video vas a poder tener corriendo el tuyo paso a paso y explicado de la manera más simple y clara posible. Pero antes de comenzar te agradecería mucho si me dejas un like en este video, no solamente porque apoyas al canal, sino porque también le dices a YouTube y tu algoritmo que este tipo de videos te interesan. Ahora sí, vamos manos a la obra. El sistema de lo que estás viendo, puede parecer terrorífico, pero realmente no lo es. ¿Recuerdas cuando entrábamos, por ejemplo, a wikipedia.com y buscamos, no sé, cualquier cosa, Cloud Code, cómo se van correlacionando distintos archivos a distintos lugares. Por ejemplo, entramos acá y de cloud entramos a Large Language Models y de Large Language Models entramos a Natural Language Processing y de acá a acá y vamos abriendo distintas aplicaciones o distintas páginas constantemente. Bueno, la lógica aquí es exactamente la misma. Yo voy a abrir algo. Acá tengo un índice que es el índice principal y vamos a empezar a hacer correlaciones entre los archivos. De esta manera, cuando la inteligencia artificial busca algo, sabe que puede llegar a otro lugar. Por ejemplo, vamos a volver a los agentes IA en 18 minutos. Lo vamos a conectar a, no tengo idea, MSP. Dentro de MSP podemos ir a Cloud Code. Dentro de Cloud Code vamos a ir a por qué dejé de usar N8N. Dentro de acá voy a N8N. Y en fin, creo que se entiende el punto. Y toda esta idea nace de Andrés Carpaty, que fue el cofundador de Open AI, que también lanzó muchas cosas y dio origen a lo que es el vibe coding. Si le interesa esa historia, tengo un video explícito donde hice un miniocumental de vibe coding y es una de las personas que más sabe inteligencia artificial en todo el planeta. Y la idea es bastante simple. La mayoría de las personas usan inteligencia artificial como si fuese un rag. Es decir, subes un PDF, la IA busca algún pedacito relevante, te da una respuesta y funciona. Pero cada vez que empiezas de nuevo, la IA empieza desde cero. No hay acumulación, no hay memoria, no hay contexto persistente entre conversaciones o incluso entre agentes. Esto soluciona exactamente eso. Lo que Carpati propone es diferente porque en vez de estar buscando los documentos crudos cada vez, el modelo construye y mantiene una especie de wiki como Wikipedia, un conjunto de archivos markdown que están interconectados entre sí para saber qué camino seguir y no gastar infinitos tokens buscando todo que probablemente ni siquiera vas a encontrar. Y la arquitectura la puedes encontrar acá en tres principales capas. Tenemos las fuentes crúas, que vendrían siendo como los archivos en su esencia más básica, es decir, artículos, papeles, imágenes, data, pero todo esto sin clasificar. Después tenemos la wiki, que vendría siendo este directorio de ll, es decir, archivos markdown que están y que se crean a partir de estos archivos bases. Aquí es donde tienes estos archivos al costado, que vendrían siendo la wiki, justamente los que están acá, páginas de conceptos, por ejemplo, entidades, fuentes, síntesis, etcétera. Y cada vez que agregas algo nuevo, el LLM no solamente lo guarda, sino que lo archiva, lo procesa y lo etiqueta. y eso es lo potente, empieza a crear estas relaciones entre los archivos. Y tercero, tenemos el esquema, que en nuestro caso va a ser un Cloud MD en específico, porque estamos usando cloud code para hacerle las preguntas a directamente Obsidian. Recordemos que podemos usar cualquier agente, puedes estar usando Manus, Jenspark, puede estar usando cloud code, OpenClo, lo que sea, pero va a funcionar igual. Y lo interesante es que Carpat incluso decía que él pensaba que necesitaba un rag, pero después se dio cuenta que este sistema podía funcionar bastante bien porque la es muy bueno leyendo los índices. Si te fijas acá tenemos toda la estructura de las carpetas, es decir, tenemos el wiki y tenemos el raw, que vendrían siendo las dos cosas principales, pero aquí tenemos una parte que sale el índice. El índice vendría siendo la primera página y es la página principal que viene a crear todo y a correlacionar todo. Es decir, aquí están los archivos de todo y cada vez que le hacemos una pregunta a la inteligencia artificial, lo que va a hacer es empezar a construir una especie de camino. Supongamos que le quiero hacer una pregunta de oye, ¿en qué video hice no tengo idea, algo de OpenCl? Lo que va a hacer es va a entrar al índice y va a empezar a crear correlaciones. Entonces, voy a buscar acá OpenCh. Okay, te explico OpenCloud. Y ya pasamos de tener los 88 archivos que teníamos a seccionarlo a 1 2 3 4 5 6 7. Y es mucho más fácil buscar en esos siete que en los otros al final, ¿eh? O en los 88 archivos completamente. Esa es un poco la lógica de la estructura que está acá. El log vendría siendo como los loges, es decir, cada vez que se va cambiando algo, va quedando registrado acá. Y aquí tenemos los raw, que aquí vendría siendo los crudos, por así decirlo, que no han sido catalogados aún o que ya fueron catalogados, pero mantiene las fuentes principales. Ya esta es la estructura, no es nada más que eso, no es nada más complejo que lo que estás viendo acá. Y de hecho, si es que entro al buscador y me voy acá a la carpeta donde tengo esto, que en este caso sería agentes, después sería content creator, y me voy al Obsidian Bolt, vamos a ver que tenemos aquí la misma estructura, contenido de YouTube, contenido YouTube, index, index, log raw, ¿verdad? y wiki, que es donde estábamos creando las cosas, conceptos, síntesis, videos, etcétera. Pero lo lindo que tiene al final Obsidian es que tiene esto y que lo podemos visualizar de una manera mucho más visual. Déjame explicarte un poco de por qué esto es realmente importante que lo entiendas, pero antes me voy a tomar un gel porque no he almorzado y ya son las 3:30 de la tarde. Estaba todo el día jugando con esto. Oh. Okay, déjame mostrarte ahora porque es importante. Tradicionalmente cuando queríamos armar este tipo de archivos lo que hacíamos era armábamos un rack, es decir, un retrieval augmented generation, donde tomábamos los documentos de acá, los pasábamos, los vectorizábamos, es decir, los transformábamos en números y ecuaciones matemáticas para poder armar correlaciones entre los archivos para que la IA lo pueda entender. Después hacíamos un proceso de chanking, que es esto de acá, que lo separábamos y lo subseccionábamos en distintos, por así decirlo, chanks o pedazos. Entonces, un PDF quedaba cortado en la cantidad de pedazos que tú querías, después pasaba al LM y después recién te da la respuesta. Funciona bien, sobre todo cuando queremos usar cosas a escala, pero al final puede ser un poco más complejo, es más difícil mantenerlo actualizado y es todo un sistema que lo más importante es que te cuesta dinero. Segundo, cuando le hacemos una pregunta a un rag, empieza a traer ciertas preguntas que tienen o cierto contenido que tiene relevancia porque tienen una similaridad semántica, por así decirlo. decir que los vectores en sí se parecen a lo que estás preguntando y claro puede funcionar en muchas ocasiones, pero a veces no. Este formato lo que propone es leer el índice. Cada vez que hacemos una pregunta empieza a navegar, llega a los puntos y llega y te da una respuesta. De hecho, un usuario logró compactar y procesar 383 archivos, lo que le llevó a ahorrar un 95% por cada token o por cada query que hacía. Y lo tercero y lo que también encuentro que es muy valioso, sobre todo para gente que está todo el día cambiando de inteligencias artificiales, de agentes de Open Cloud Cloud Code, es que es portátil. O sea, yo puedo tener esta carpeta y abrirla con OpenClow, puedo tener la misma carpeta y abrirla con Cloud Code. Puedo trabajar con la misma carpeta y pasársela a Cowork de Cloud o literalmente lo que sea y puede trabajar con ella. Puede trabajar en manus, puede trabajar en Genspark, puede hacer literalmente lo que sea. Y lo útil y lo impactante y lo importante de esto es que podemos crear estas bases sin tener que estar pagando por un RAC porque Obsidian es completamente gratuito. Así que te voy a mostrar cómo lo estoy usando y cómo lo estoy haciendo yo todo paso a paso. Este que está acá es mi Obsidian. Antes de crearlo paso a paso, tenemos un índice, que es lo que une literalmente todo. Si es que me voy al costado, vamos a encontrar el índice y vamos a ver que están los grandes puntos unidos directamente. Cada uno de estos puntos después se une a otro de los puntos y la idea es evitar como archivos sueltos que no están vinculados a nada porque nunca vamos a llegar realmente a ellos. Si no, si es que entro a un video específico, por ejemplo este de acá, voy a ver un resumen ejecutivo, voy a ver la estructura del video, el hooky, la apertura y temas clave que estoy tocando acá. ¿Okay? Es bastante sencillo, una manera en la que puede eh entenderlo e interpretarlo sin sobrepoblar de información. Lo que está bastante bueno es que después siempre voy a poder volver a los archivos originales. Entonces, si es que necesito profundizar por alguna razón en algo que no está en este resumen ejecutivo, lo que hace acá es referenciar las distintas fuentes. Así que si abro el wiki y abro las fuentes o me voy a los ROSS, van a salir mis transcripciones acá. Y aquí tengo cada una de las transcripciones de los videos de YouTube. Y esto no lo hice yo, sino que lo saqué con Cloud Code y ya te voy a mostrar exactamente cómo hacerlo. Pero lo mejor es cuando le pedimos este tipo de cosas, tipo, ¿por qué les está yendo bien a ciertos videos? Y me hizo el análisis de los patrones, de los hooks, las tendencias en las duraciones, etcétera, todo lo que está acá para poder verlo y podemos tener una conversación con nuestros archivos. ¿Okay? Eso vendría siendo los archivos que estás viendo o los archivos que están detrás, los Markdown. Pero también hay un par de archivos más que son importantes de entender, sobre todo este que es el cloud. El cloud.md es el alma de todos los agentes de inteligencia artificial. En otros agentes tiene otros nombres como gemini.m agents.m en cloudscloud.md. Y este es el archivo al final, el cloud MD, el que le dice, "Oye, cuando recibas una fuente tienes que hacer esto." Define cómo el LM se comporta sobre la wiki, etcétera, etcétera, etcétera. Lo genial es que si es que ahora llego y abro otro agente en específico, por ejemplo, open, creo un nuevo una nueva carpeta que va a ser carpeta de prueba. abro la nueva carpeta y simplemente le digo, "Oye, te acabo de pegar acá el volt de Obsidian, es decir, la información de Obsidian. Necesito que la interpretes y que la crees. Vamos a ver que eh funciona y que está entendiéndola. Esto lo hacemos con rayita init, le hacemos play y vamos a ver que está empezando a comprender y a entender qué es lo que hay en cada uno de los archivos y crear el cloud.md. Pero ahora sí te voy a mostrar literalmente todo paso a paso, cómo lo podemos armar, incluso si es que nunca has usado este tipo de herramientas. Así que si me sigues, vamos a aprender a crear un Bolt, correrlo en Cloud Code, escribir el prompt e importar nuestras primeras fuentes. Lo primero que vamos a hacer es vamos a ir a obsidian.md y vamos a irnos a descargar y vamos a descargar para nuestro sistema operativo. Una vez que te lo descargas, te va a preguntar si es que quieres crearte una cuenta de pago o no. Dale que no. Eh, solamente creo que te sirve si es que quieres sincronizar cosas entre archivos, pero realmente no es necesario. Continúa con la versión gratuita. Después ve si te sirve la versión de pago. Yo sigo en la gratuita y está perfecto. Y vamos a irnos a crear un nuevo Volt, dónde está acá. Crear un nuevo Volt o crear una nueva bóveda. Vamos a darle a crear. Vamos a ponerle un nombre y este va a ser, por ejemplo, no sé, contenido de YouTube. Vamos a elegir una ubicación para esto. Voy a crearlo aquí en una nueva carpeta para que no se contamine eh de por sí. contenido de videos de YouTube versión 2 y le vamos a dar a abrir. Le voy a dar a crear acá y se va a inicializar una nueva bodea. Aquí tenemos crea una nota de algo, crea un enlace o prueba el importador. Cuando esté listo, borra esta nota y aprópiese de la bóveda. Si abrimos el importador, tenemos distintas maneras en las que podemos empezar a importar información. Tenemos Notion, Apple Notes, Evernee, Apple Journal, Craft, Bear, etcétera. Para este caso, lo que queremos hacer es vincularlo con Cloud Code porque necesitamos empezar a sacar información de distintos lados. Y recordemos que Cloud Code tiene acceso a MCP, por lo que hace mucho más fácil importar información directamente. Pero bastante sencillo para mostrarte algo. Cuando creamos un nuevo enlace, este va a ser el enlace uno. Vamos a ver cómo se relaciona con el enlace uno. Queremos crear un vínculo con el enlace dos. Entonces, acá en la bienvenida tenemos el enlace uno, que vendría siendo este. Y si es que abrimos acá la carpeta de bienvenida, como estamos referenciando el enlace uno justo acá, están conectados. Si es que no referenciáramos el enlace uno o directamente lo eliminamos, por ejemplo, no debería estar apareciéndonos acá porque no existe conexión. ¿Okay? bastante sencillo, así es como funciona. Eh, y lo que estamos visualizando acá, es decir, la carpeta Markdown o el archivo Markdown bienvenida y el archivo Markdown enlace son simplemente otra manera de estar visualizando lo que está acá. Obsidian Bolt, videos 2 y estos dos archivos, ¿verdad? Un archivo Markdown que es bienvenida y un enlace que es el otro archivo Markdown. Okay, Benja, ¿cómo puedo ahora empezar a importar distintas cosas? Aquí es donde ocurre la magia. Como estamos trabajando en archivos a nivel de elfinder, es decir, acá podemos trabajar a nivel de Cloud Code. Entonces, vamos a abrir Cloud Code. Y estas son las únicas dos aplicaciones que necesitamos usar. Obsidian para visualizar esto y Cloud Code para conversar con nuestra base de datos o con nuestra wiki. A mí me gusta usar Cloud Code en VS Code, pero puedes usarlo dentro de cloud. Por ejemplo, si te vas acá y buscas code, puedes tener la conversación acá, puedes hacerlo en Antigravity, puedes hacerlo en BS Code, donde sea, todo va a funcionar exactamente igual. Para este caso, vamos a irnos a PS Code y vamos a abrir una nueva carpeta. La carpeta que tenemos que abrir es la carpeta que creamos previamente, ¿ya? Así que nos vamos a ir a BST en este caso, que es donde tengo las cosas, tengo los agentes, dentro de los agentes, tengo el content creator y esta es la carpeta de prueba que estamos trabajando con. Okay, esta es la carpeta con la que vamos a trabajar. Obsidian Bolt, contenido videos de YouTube. Y si te fijas, aquí tenemos las eh carpetas con los archivos que son los que estamos trabajando. Vamos a abrir la carpeta que habíamos creado, es decir, el volt que habíamos creado previamente. Vamos a cerrar acá y vamos a entablar una conversación con Cloud Code. Si es que no te aparece acá, tienes que irte a las extensiones, instalar Cloud Code y podemos tener la conversación. O así se hace al menos en BS Code. Si es que vamos acá y le preguntamos qué es lo que ves, aquí nos va a decir directamente qué es lo que estás viendo, es decir, qué hay en los archivos. Veo un workspace con dos directorios de trabajo. Déjame explorar que hay en ellos y va a revisarlos y vamos a ver que no hay mucho más, ¿verdad? Son dos archivos bastante sencillos y bastante básicos. Lo que vamos a hacer es vamos a empezar a poblarlo. Para ello vamos a irnos acá a el GitHub de Carpaty de ll Wiki y vamos a copiar todo esto. Puedes también darle el link y le dices cómo vamos a instalar esto. Puedes también copiarlo manualmente, puedes copiar el row, puedes hacerlo como gustes. Para este caso lo voy a copiar y le voy a decir, vamos a crear un agente. Necesito que mantenga todos mis videos de YouTube organizados. Aquí le vamos a poner las cosas de el GitHub que acabamos de copiar y le vamos a decir crea el cloud.md con las reglas, el index, el log y las carpetas. Mi canal de YouTube es este de acá. Lo vamos a pegar que vendría siendo este. Le vamos a dar a enter y vamos a ver cómo se empieza a crear el cloud.md. Ahora no tenemos nada. Va a empezar a sacar las cosas, las transcripciones quizás, o eso es lo que quiero que empiece a hacer. Y este es el siguiente paso al final porque mira, está empezando a crear los archivos. Está creando el Obsidian, está creando el RAW, está creando el wiki, que aquí tenemos las series, las temas, los videos, etcétera, y va a empezar a vincularlos acá. Okay, si es que visualizamos acá, mientras está trabajando el VS Code y sigue trabajando, podemos ver cómo se empiezan a crear las distintas cosas. Entonces, tenemos aquí el bienvenido, el cloud, el log, el index y podemos ver cómo se empieza a crear el wiki, que vendría siendo las cosas clasificadas, y el RAW, que vendrían siendo las cosas crúas. Cada vez que nosotros agregamos algo nuevo se va a ir a RAW a menos de que sea clasificado por la inteligencia artificial o manualmente o lo que sea. ¿Ya? Entonces, aquí tenemos el cloud. Está empezando a armarse el cloud MD. Voy a volver acá. Voy a volver al VS Code. Vamos a ver. Okay, vamos al siguiente paso. Necesito una URL de YouTube, necesito una transcripción copiada o un título. Así quedó estructurado esto. Tenemos el cloud MD, que es como las reglas o el system prompt. Tenemos el RAW, que son las fuentes crúas, y tenemos la wiki, que ya es clasificado. Aquí tenemos dos formas de empezar, o en verdad tenemos muchas formas de empezar a popular de información. Para este caso, lo más práctico sería que le diga, "Haz un scraping de mis videos de YouTube y saca las transcripciones." Pero te voy a mostrar también otro método que te puede funcionar, que es con este plugin, que si buscamos acá, Obsidian Clipper, vamos a actualizar y vamos a agregar esto a Chrome. Esto es exactamente lo que está viendo acá y es una manera de mandar archivos. Por ejemplo, supongamos que me gustó este tweet de, no sé, a ver, vámonos acá. Quiero meter el post de Carpati, que vendría estando acá, quiero mandarlo. Entonces, voy a apretar el link que está aquí y puedo ponerle agregar a Obsidian. Aquí le puedo cambiar cosas si quiero. Eh, supongamos que me sirve como para ir guardando contenido, cachá, o lo que sea. Pum, listo. Agregar obsidian. Si es que aprieto acá, puedo guardarlo o copiar o directamente agregar a Obsidian. Vamos a abrir Obsidian. Se agregó Obsidian. Y listo. ¿Dónde quedó esto? Mira, tenemos esto que está acá que se está referenciando. Está en los tags, que son los clippings y lo podemos encontrar en los que acabamos de crear, que vendría siendo los clippings, ¿ya? O sea, directamente los de acá. Alternativamente, también los podemos mandar a los raw si es que apretamos aquí y le ponemos que no vaya a clipping, sino que queremos que vaya a raw y aquí se agregó y se metió acá. Ya, eso es un poco la estructura y lo importante que tenemos que entender que está actualizando. Vamos a popularlo con un poco más de información. ¿Por qué te quiero mostrar ese método? Porque primero si es que quieres meter algo rápido funciona bastante bien, pero el que me interesa que aprendas es el de Cloud Code porque es el más importante. Entonces ha un scraping de mi video de YouTube y saca las transcripciones. ¿Por qué quiero esto? Porque Cloud Code es lo que podemos conectar a todos. Lo podemos conectar vía MSP a nuestros archivos de Drive, lo podemos conectar a los formularios que nos van llegando, a distintas fuentes de información, los podemos conectar incluso a Pinecone o a distintos vector bases o lo que queramos. Entonces es muy potente para mantener actualizado y tener esto de una manera organizada y tener una conversación con nuestros archivos que no alucine ya o que alucine mucho menos porque tiene una ruta predefinida, determinada y que es una genialidad. O sea, la cantidad de casos de usos que se me ocurre son muchísimos. Por ejemplo, para e-commerce puedes empezar a crear un índice con los distintos productos, con las preguntas, ¿verdad? Eh, puedes crear este chatbot que después puede tener una conversación con estos archivos y te va dando información. Eh, es una genialidad todo lo que se puede hacer. O sea, podemos vincular hasta esto con los Cloud Agents, que es una actualización, un lanzamiento que tuvieron hace un par de días y puede buscar las fuentes directamente de Obsidian, porque también se puede conectar por MSP en el caso de que quieras. Sigamos con esta parte, vamos a ver cómo populamos esto. Está descargando las transcripciones de los 85 videos. Y si te fijas, ya tenemos la estructura básica creada. Tenemos el index, ¿verdad?, que va a ser el canal, tenemos los videos, tenemos los temas, tenemos las series, las personas, los analytics, pero esto es lo que se va a empezar a modificar. Ahora, mientras tanto, podemos ver acá que tenemos el archivo Cloud MD, que vendría siendo como el system prompt. Esto siempre me gusta que esté a la izquierda. Y tenemos acá, este es un wiki personal mantenido por un agente LM para organizar el contenido de X. Okay, este vendría siendo el cloud.md, bastante sencillo, obviamente se puede optimizar, pero eh no es el fin de este video. El fin de este video es que entiendas que son las cosas que se pueden hacer, que se puede armar con Obsidian y que desplguemos este proyecto juntos. Y bueno, podemos ver cómo empieza ahora a popular con las transcripciones. De hecho, si es que abrimos uno, tenemos aquí un transcript. Eh, después podemos volver acá, tenemos distintos transcript, pero está todo caótico y no está nada ordenado. Lo tenemos todo por distintos lados. Mira, fíjate acá. No tenemos correlaciones, no tenemos absolutamente nada, simplemente tenemos muchos puntos en distintos lugares. Y es por eso que tenemos cuatro operaciones que podemos tener o conversaciones que podemos relacionarnos con cuando usamos obsidian. Tenemos el ingest, tenemos el query, tenemos el lint y tenemos el bulk ingest. El ingest viene siendo cada vez que creamos una nueva cosa. Es como digérelo, digérelo, interprétalo, clasifícalo, categorízalo, créale las tags, hazle literalmente todo, crea su página, creo, actualiza temas, etcétera. Después tenemos el querer que es para consultar directamente. Si quisiéramos, por ejemplo, después hacer un chatbot, podríamos hacerlo con esto. eh desplegamos esto y le ponemos como lo desplegamos a un agente, lo conectamos con los archivos y directamente le decimos y lo transformamos en un chatbot como, ¿dónde puedo encontrar esto? O no sé, puedo hacer un chatbot de mis videos de YouTube, por ejemplo, y es como, ¿dónde pillo un video que haga esto y te redirecciona un video de YouTube? Podría ser. O alternativamente también puedo hablarle yo en esta interfaz a Cloud Code para buscar ciertas cosas. Después tenemos Lint, que es algo clave, que es una especie de mantenimiento donde va a tomar todos los archivos guachos o los archivos que están solitarios que no tienen relación alguna, porque por ejemplo aquí podemos ver que ya está empezando a categorizar alguna, como que está el trabajo que está haciendo ahora, pero va a tomar todos los archivos que no tienen alguna conexión con algo y los va a directamente marginar o los va a conectar con algo. Mira cómo se empieza a conectar esto. Char GPT se eh conecta con estos dos videos, por ejemplo. Después Open Ai se conecta con este video. Son videos bastante antiguos, lo que es una es una genialidad. De hecho, esto era cuando estaban los plugins de Char GBT, que es genialidad. Eh, pero si es que nos vamos acá, voy a volver a Obsidian, podemos ver cómo sigue trabajando. Aquí estamos teniendo la conversación con Cloud Code y tenemos el bulk inest, que es para procesar también muchos archivos de una, que es lo que está corriendo y es lo que está ejecutando ahora en este preciso momento. No lo digo yo, sino que si es que abrimos el llm wiki, que es lo que copiamos, tenemos las opciones acá, ingesty lint, ¿okay? Y bulking Jest vendría siendo como lo mismo, pero lo mismo que el Injest, pero con más archivos. Voy a dejar trabajando esto y te voy a dejar un timelapse de esta parte para que veas cómo se van construyendo las relaciones mientras voy a buscar una barrita para comer algo. Y después de un ratito podemos ver cómo empieza a popular los temas. Acá está creando los distintas categorías, agentes cloud code, WhatsApp, ¿verdad? Está creando y agregando los distintos temas. Justamente acá podemos empezar a ver cómo se construyen las correlaciones entre ellos. Por ejemplo, acá si es que abro los temas, puedo abrir chat GPT y me dice todos los que están acá, Cloud Code, ¿verdad? Eh, no tengo idea. El curso de Cloud Code, que es el curso que lanzamos y nos tira todas las cosas acá. Lo importante es que también tiene la referencia a el lugar anterior y tenemos aquí las distintas redes que se van creando y cómo se van relacionando entre sí. Tenemos el índice, que recordemos que es la lo más importante y es lo primero que se navega directamente y el índice es lo que está correlacionando todo el resto de las cosas. Por ejemplo, acá supongamos que me voy a make.com y también tenemos crea un año de contenido con Canva Master GPT más make o si nos vamos acá a make.com tenemos no tengo idea, eh, automatización o la automatización de la facturación. Si nos vamos acá al URL nos manda al link de el video en específico que habíamos subido y en fin, es realmente una genialidad. Aquí lo tenemos todo visualmente y si te fijas también está todo aquí publicado dentro de nuestro find o de nuestra carpeta o nuestro folder. Tenemos todos los archivos acá, raw, ¿verdad? Tenemos los clippings, que es lo que habíamos creado previamente, tenemos los transcript, tenemos el wiki y aquí tenemos las categorías con los distintos temas, por ejemplo, cloud code. Y una última cosa, si es que te vas aquí a Obsidian, puedes buscar los plugins oficiales de Obsidian para empezar a hacer las sincronizaciones. Puedes buscar Obsidian Plugins y te vas a la página oficial de los plugins, que vendrían siendo estos que están acá. Y tenemos muchas cosas como para conectarlo con Discord, el LM Dogs, PDF, tu Image, AI agents. Eh, tienes algunos que están bien interesantes e incluso si es que buscan MCP, podemos ver que aquí tenemos el MCP tool para poder conectarlo con distintos MSPs, con los plugins de Obsidian directamente. Entonces, reemplaza esto el rag y la respuesta es depende de la situación. Mira, si tienes muchos documentos y quieres manejar una escala que es excesivamente grande, el RAC sigue siendo tu mejor opción, pero para el 90% de los casos estoy seguro de que este sistema te va a funcionar bastante bien. Así que si tienes cientos de documentos, que es como el caso de las mayorías de las personas, esto debería funcionarte bastante bien e incluso te podría funcionar mejor porque tiene relaciones entre los archivos como directas y no inferidas en base a chunks. decir que el modelo sabe exactamente dónde buscar porque hay un índice y una correlación que va buscando y un camino claro que va siguiendo. Para que te hagas una idea, Carpa dice que en 100 artículos con medio millón de palabras funciona excelente. En este caso vimos 88 artículos, tenemos más de 100 páginas generadas y honestamente responde al tiro. Ahora, si ya estás en el punto de que pasas a tener cientos de miles de documentos, quizás millones de documentos, no lo sé, que es un caso muy enterprise o de empresas a una gran escala, ahí sí quizás te sigue conviniendo tener un RAC, es decir, montar un RAC tradicional con vector bases con su infraestructura tradicional que pueda navegar los archivos de manera más ordenada, por lo menos a esa escala, porque seamos honestos, imagínate esto mismo que acabas de ver acá, es decir, esto, pero con cientos de millones de archivos, sería realmente un caos. Así que si estás armando un chatbot que estás buscando que refiera productos, un organizador de contenido para YouTube, una base de conocimientos para tus clientes o para tu equipo, eh referencias a distintos archivos o quieres centralizar tu memoria para poder pasarla y usarla en distintos tipos de agentes, esta es tu mejor opción. Piénsalo así. Esto es como un RAC, pero en vez de estar buscando por similaridad de datos, está buscando y buscando referencias entre relaciones dentro de la wiki, es decir, relaciones directas. Lo que acabamos de armar es literalmente una memoria infinita. No es una exageración, la única limitante que estás teniendo es cuánta memoria tienes en tu espacio y siendo archivos de texto, la verdad es que probablemente es bastante. Son literalmente archivos de texto que se relacionan entre sí. Es la misma lógica que llevamos usando por más de 20 años con Wikipedia, pero en vez de que miles de voluntarios tengan que estar manteniendo esto eh, sin ser pagado, sin ser remunerado y completamente a muy buena voluntad, lo hace un agente de inteligencia artificial y puedes tener tu propia wiki completamente privada. Te dejo el kiss de Carpati abajo en la descripción para que lo uses y si te gustó este video, no sabes todo lo que me sirve que me dejes un humilde like. No solamente porque me ayudas a mí y al canal, sino porque también le dices a YouTube que este tipo de videos te interesan y te empieza a recomendar más cosas pulentas como esta. Así que eh te agradecería mucho si me dejas el like y si te interesa el mundo de las automatizaciones y de la inteligencia artificial, te invito a darte una vuelta por Imperio Digital, un lugar donde estamos construyendo todo el día. Tenemos cuatro sesiones en vivo. Todas las semanas estamos subiendo bastantes cosas y al final hacemos de las automatizaciones y la inteligencia artificial algo entretenido. Si te interesa, el link está abajo en la descripción y te voy a dejar dos videos acá. Uno es un curso completo de Cloud Code de más de 3 horas. Es el curso gratuito en español más completo que hay en este momento y otro es un video de YouTube que te va a recomendar YouTube que cree que te podría gustar. Dicho eso, espero que te haya servido esto y ya nos vemos.
