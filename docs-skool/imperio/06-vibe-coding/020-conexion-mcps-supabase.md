# 🤓 Conexión MCPs + Supabase

> Ruta: Vibe-Coding › 🤓 Conexión MCPs + Supabase

**🎬 Vídeo (36.0 min):** https://youtu.be/7ppKLr2mfBA

---

## Parte II. Supabase + MCP. Conexiones dinámicas en Antigravity y qué viene en el siguiente video

Antes de seguir construyendo, aquí hacemos una pausa estratégica para entender dos piezas que te van a ahorrar horas:

1. **Qué es Supabase y por qué lo usamos en este proyecto**
2. **Qué es MCP (Model Context Protocol) y por qué conectarlo a Antigravity cambia el juego**

Luego hacemos la parte práctica: conectar **GitHub, Supabase, Vercel y n8n** a Antigravity, cada uno con un método distinto. La idea es que entiendas que no hay una sola forma “correcta”. Hay varias, y tú eliges según el caso.

Al final, te explico qué haremos en el siguiente video.

## 1. Qué es Supabase (en simple y sin humo)

Supabase es una alternativa open-source a Firebase basada en **PostgreSQL**. Piénsalo como un backend completo en una caja:

- **Base de datos relacional (Postgres)**
- **Auth listo** (email, social login, teléfono, etc.)
- **Storage** (archivos, imágenes, PDFs)
- **APIs auto-generadas** (para leer/escribir datos sin montar servidor propio)
- Edge Functions si luego quieres lógica server-side

### Por qué lo usamos aquí

En este proyecto Supabase tiene dos roles claros:

1. **Guardar datos**: clientes, diagnósticos, cotizaciones, correos enviados
2. **Habilitar acciones**: auth y operaciones que requieren backend real

## 2. Cuándo sí y cuándo no usar Supabase

### Sí usarlo cuando:

- Necesitas guardar data de usuarios
- Quieres login real y sesiones
- Tienes relaciones (uno a muchos) como: - Un cliente . muchos diagnósticos
- Un diagnóstico . muchas cotizaciones
- Una cotización . muchos correos enviados
- Quieres lanzar rápido un MVP con backend incluido

### No usarlo cuando:

- Tu app es 100% estática (landing sin datos)
- Todo es almacenamiento local sin usuarios
- Tienes lógica backend ultra compleja y necesitas arquitectura propia

## 3. La parte importante. Relaciones en base de datos

Este proyecto usa relaciones reales, no “listas sueltas”:

- **Clientes** . Diagnósticos (1 a N)
- **Diagnósticos** . Cotizaciones (1 a N)
- **Cotizaciones** . Emails enviados (1 a N)

Esto es lo que hace que luego puedas:

- consultar historial
- filtrar
- auditar
- tener trazabilidad  
Sin volverte loco.

## 4. Qué es MCP y por qué te ahorra tiempo

MCP (Model Context Protocol) es un estándar abierto creado por Anthropic para conectar modelos de IA con herramientas y datos, tipo “USB universal”.

La diferencia práctica:

- Sin MCP: tú escribes integraciones a mano, APIs, headers, body, errores, etc.
- Con MCP: el modelo ya sabe cómo hablar con la herramienta, tú pides en lenguaje humano.

MCP reduce fricción. Punto.

## 5. Qué MCPs vamos a conectar en este curso

Para este proyecto conectamos:

- **GitHub MCP**: leer repos, archivos, buscar código, issues, PRs
- **Supabase MCP**: ver proyectos, manejar DB, tablas, auth, etc.
- **Vercel MCP**: deploy, logs, proyectos, env vars (con CLI y sesión)
- **n8n MCP**: listar workflows, ejecutar, buscar, etc.

La meta es que Antigravity pueda:

- leer tu PRD y código en GitHub
- crear y ajustar DB en Supabase
- ayudarte a deployar en Vercel
- crear o integrar flujos en n8n  
Todo desde el chat.

## 6. Conectando MCPs en Antigravity (lo práctico del video)

### A) GitHub (nativo, pero ojo con Docker)

Antigravity trae GitHub “preconfigurado”, pero a veces lo intenta correr via Docker.

Aquí mostramos la forma pro:

- Instalas GitHub MCP
- Generas un **Personal Access Token (classic)** en GitHub
- Si te lo pone como Docker, editas el JSON y lo conviertes a **npx**
- Guardas y refrescas

Buenas prácticas del token:

- Expira en pocos días si es demo
- Scope solo lo necesario (repo, workflows, hooks, etc.)
- Nada de permisos innecesarios

Luego haces el test obligado:

- “Listame mis repos” para confirmar que sí hay acceso real

### B) Supabase (nativo y directo)

Supabase sí es plug-and-play:

- Generas **Supabase Personal Access Token**
- Lo pegas en Antigravity
- Confirmas que aparece en Tools
- Test rápido: “Confirma que puedes ver mi proyecto”

### C) Vercel (no viene nativo. se conecta manual)

Aquí enseñamos otra ruta:

- Vercel MCP no aparece preconfigurado
- Buscamos documentación oficial del MCP (mcp server + npx)
- Pegamos config manual en el JSON
- Si ya estabas logueado, puede que no te pida token
- Si quieres forzar el onboarding para el tutorial: - `npx vercel login`
- te manda a `vercel.com/devices`
- autorizas y listo

Esto es importante porque mucha gente cree que “si no pidió token. no conectó”. No. Puede usar sesión local.

### D) n8n (no nativo. se configura por repo oficial)

Aquí hacemos algo que te sirve para cualquier herramienta:

- Buscamos el MCP oficial de n8n en GitHub
- Le pedimos al agente que lo clone, lo lea y nos devuelva el config exacto
- Rellenamos: - URL de n8n
- API key de n8n (creada en settings)
- Guardamos, refrescamos y probamos: - “Listame mis workflows”

Si te lista tus flows, ya está.

## 7. Regla de oro del módulo

Cada vez que conectes un MCP:

1. conéctalo
2. refresca
3. haz una prueba real (listar repos, listar workflows, ver proyecto)

Si no pruebas, vas a perder tiempo después y no vas a saber si el bug era tu app o la conexión.

## 8. Qué sigue. Próximo video (win rápida)

En el siguiente video hacemos una “win” rápida de 0 a 100:

- Construimos un clon de **Linktree**
- Mobile-first
- Deploy a Vercel
- Te quedas con una URL pública
- Lo puedes poner en Instagram, TikTok, donde sea
- Sin pagar Linktree

Después de esa win, regresamos al proceso completo para construir una app más grande con el flujo completo y deploy final.

## 🎙️ Transcripción

Perfecto. Entonces, para este punto ya debes tener antigravity conectado. Antes de continuar vamos a hacer dos cosas. Vamos a ver primero qué es Supabase y qué es el protocolo MSP, porque vamos a tener que conectarlo eh para que sea más fácil. No es obligatorio, pero créeme te va a ahorrar muchísimo tiempo conectar los MSP. Vamos primero a empezar con qué es Supabase. Supase lo vamos a utilizar para el proyecto porque nos va a servir de dos cosas. Nos va a servir para tener nuestras tablas, donde vamos a tener nuestros clientes, las cotizaciones, etcétera, que lo vamos a ver en unos segundos. Y también su pav sirve como un back en tas service para poder realizar ciertas acciones u operaciones, así como para la parte de la autenticación que lo vemos en el último video. Entonces vamos a explicar. generé esta pequeña presentación que de hecho la generé con Google AI Studio y vamos a ver eh lo que es Supabas. Dice Supas for Builders, aprende a dominar la alternativa open source a Firebase basada en Postgress SQL para tus proyectos del mundo real. Okay. Si estás viendo esto, muy probablemente ya sabes algo de N8N y a lo mejor ya tienes Postgress configurado para tu memoria. Quiero que sepas que Supas es open source, utiliza postg SQL y o puede ser que también tengas alguna vector store ya creada con Supace directamente. Entonces, ¿qué es upabase? Es como tener un backend completo en una C. Dice, para tu aplicación no es magia, es simplemente postgre SQL vitaminado para desarrolladores modernos. Imagina Firebase, lo conoce Firebase es de Google, pero si el vendor locking, por eso comentaba lo de Google y con el poder absoluto del lenguaje SQL, vamos a poder tener base de datos relacionales, vamos a poder tener autentificaciones listas por correo, por teléfono, por email, utilizando tu Apple ID, utilizando tu número de teléfono, muchas opciones para poderte conectar. IP res autogenerada, ¿qué quiere decir? que su pavis te puede crear lo que se llaman edge functions, que te permite hacer llamados como si tuvieras una tal cual una API, como cuando llamamos a generar imágenes con no banana o algo así y sincronización en tiempo real que está pasando y tamb manejo de caché de nuestros usuarios. ¿Okay? ¿Cuál es el superperer de Superabase? Lo que les comentaba, la base de datos, tenemos postgress SQL puro, consultas potentes y es escalable. ¿Qué quiere decir? Puedes empezar con tu cuenta gratuita. Conforme va aumentando tu número de usuarios, en teoría tendrías que ir aumentando tu facturación y vas aumentando eh su pavisabis, que es lo que te va a ir dando mayor usuarios, mayor caché, mayor request por segundo, etcétera. Pues la segundo para lo que se usa mucho es la parte de la autenticación, lo que te comenté social login, que quiere decir que inición de sesiones y tu almacenamiento. Tú pavisamente es un storage, puedes subir imágenes, PDFs, puedes poner URL públicas, pockets privados, etcétera. ¿Okay? ¿Cuándo sí y cuándo no usar su pavase? Eso es muy importante. No todos tus proyectos en antigravity, no todos tus proyectos no code van a necesitar supace. Entonces, vamos a ver cuándo sí y cuándo no. ¿Cuándo sí usa suabase? Cuando quieres guardar datos de usuarios, cuando quieres tener un login que el usuario inicia sesión, entonces necesitas guardar su user ID, la fecha en la que creó su cuenta o su usuario, su contraseña a lo mejor en hash protegida, etcétera, cuando tienes que tener una base de datos relacionales, que eso es genial para postgres, lo vamos a ver más adelante, pero a lo mejor tienes una base, una tabla de usuarios y los usuarios pueden tener, en el caso de la aplicación que vas a construir más adelante o unas de las que vamos a construir, puedes tener cotizaciones. Entonces, un usuario puede tener muchas cotizaciones, pero una cotización solo puede ser de un usuario. Eso se refiere con relacionadas y es muy rápido desplegar, por eso es para prototipos rápidos para MVPs. En minutos ya tienes todo listo porque es su propio backend, por el nombre lo dice, es un backend service. cuando no necesitas usarla, cuando solamente quieres hacer almacenamiento local, caché de tu browser, apps 100% estáticas, una landing page que no captures información de usuario, que solamente muestres información o que los redireccionas a otro lado, no necesitas su pais para nada. Y eh lógica backen ultra compleja ya para un nivel mucho mayor. Suis a lo mejor se te quedaría corto, lo mejor es que tengas tú tu propio servidor backend con el textac, la tecnología. que tú quieras. Okay. En este caso, ¿qué vamos a hacer nosotros para el proyecto que vamos a utilizar subas? Vamos a tener nuestra tabla de clientes. ¿Por qué la necesitamos? Una, porque vamos a poder mantener la información de contacto. Dos, para nuestro pipeline de ventas y para poder enviar coticiones por email. Una tabla, imagínense como si tuvieras un Excel y esos son tus encabezados del Excel, tus headers, tus columnas. Una tabla va a tener diferentes campos. En este caso va a ser un campo de ID tipo UID, que es un identificar único, como si tuviéramos en Air Table una tabla que tienes tu identificar único, tu campo de nombre, que en este caso era texto, tu campo de email y tu campo de estatus. Y más o menos un ejemplo de cómo se vería la tabla, eh, tal cual en su país. Este código no es real, pero más o menos es como un ejemplo, ¿no? Tenemos la tabla de diagnósticos que es para almacenar respuestas. Esto esto va a ser más sentido cuando vayamos más adelante y veamos toda la parte de las tablas y al momento que las implementemos directamente en los próximos videos lo vas a ver. Tus tablas de cotizaciones igual con su ID, su token público y las tablas de correos enviados. ¿Okay? Una vez que definimos todas esas tablas, vamos a ver cuestiones de seguridad. R level security te permite definir quién ve directamente quién quién ve qué y directamente en el motor de base de datos. No todos pueden tener accesos. Para políticas de MVP podemos hacer una lectura, una lectura pública por token o podemos hacer que eh sea anónimo que en este caso de MVP para una prueba pues no pasa absolutamente absolutamente nada, ¿no? ¿Cómo [carraspeo] vamos a hacer? Tenemos el wizard completo, luego guardamos el cliente, la I hace el diagnóstico, generamos la cotización, enviamos el email en 8N y compartimos el enlace. Ese va a ser flujo de acción donde Supace entra en cada una de estas partes. Okay, eso es lo que les mencionaba de las relaciones. Tenemos clientes que se relaciona a diagnósticos uno a N. N tómela como uno a muchos. ¿Por qué? Porque un cliente puede tener muchos diagnósticos, ¿okay? Luego tenemos diagnósticos que se relacionan uno muchos con cotizaciones porque cada diagnóstico puede tener diferentes cotizaciones y cada cotización puis haber mandado diferentes correos. Entonces, todo esto son relaciones uno a muchos, uno a muchos, uno a muchos. Okay, en este caso es un poquito de de código, no lo van a tener que ustedes escribir. Todo esto lo hace antigravity por ustedes. Okay, perfecto. Entonces, ya quedó claro que supase nos sirve para las generar las tablas. Velo como si fueran tal cual tus tablas de table, donde tienes tus campos, qué nombre, qué correo, que una fórmula, etcétera. Y ahora vamos a hablar acerca de lo que es el model context. Protocol o MCP, seguro lo has visto en varios lados. Muchos dicen que es la evolución de las APIs, de las API y este fue un estándar abierto que actúa como un puerto USB universal para conectar modelos de guías con tus datos y herramientas locales. API era como para conectar esta herramienta con esta herramienta y MSP vo conectar esta herramienta con tus modelos de inteligencia artificial. ¿Okay? ¿Quién y por qué? Fue creado por Antropic. Como saben, Antropic es el padre de Clot, que es otro LLM como Chagpt, como Gemini, Grock, etcétera. Eh, fue presentado como un estándar abierto para la industria. ¿Qué quiere decir? Que se lo abrieron a todos, ¿no? No se lo dejaron nada más para ellos. Eh, dice, "Adiós a las integraciones AdHot. Básicamente permite que un modelo use la misma herramienta sin importar si está en Cloud Desktop, cursor, tu propio servidor, etcétera. Y la IA ya no sabe, ya no solo sabe cosas, sino que ahora puede ver, tocar y tus sistemas. Por ejemplo, si tuviéramos una conexión por API de GitHu, tú le puedes decir, "Okay, con este endpo vas a ver y vas a ir a buscar qué repostorios existen. Con ese otro point vas a ir y vas a buscar los comentarios que tengan mis repositorios y así ahorita con un MCP le dices, mira, tú tienes acceso a todo esto. Casi que yo te pida algo, ve qué puedes llamar y cuándo lo puedes llamar y tú encárgate de darme la respuesta." Entonces, la idea es estandarizar las aplicaciones, eh, estandarizar cómo las aplicaciones proporcionan datos a los modelos de lenguaje, eliminando la fricción de de construir conectores personalizados y una y otra vez. ¿Cuántas veces no les ha pasado que están trabajando en NHN y que están haciendo, no sé, el el workflow de carruceres virales, ¿no? Muchas personas se dieron topes con ese y cuando hacían el llamado a la API eh les regresaba eh, no sé, eh un código de error o les daba error y les decía que no se podía conectar o decía que el body estaba incorrecto, etcétera. Entonces, básicamente MSP se quita todo eso porque ya tiene toda la documentación, sabe cómo funciona. Entonces, tú con palabras humanas le puedes decir, "Necesito que vayas y que me descargues una imagen." Y ya se va a encargar, ya sabrá él cómo lo hace. Y tú no tienes que preocuparte por esa parte, esa parte técnica porque ya se genera ese protocolo, ya se pusieron de acuerdo cómo se van a comunicar. Okay. ¿Qué vamos a integrar para el proyecto? El GitHub de MCP, que te permite leer archivos y repositorios completos, crear y gestionar issues y pull request y buscar código a través de múltiples repositorios. Okay, como ya lo hablábamos, GitHCP es un control de versiones. Lo vamos a poder hacer todo directamente desde chat pidiéndole a la gente, ve y dime qué puedes ver en este repositorio. Ve y haz un commit. Ve y haz un push. Ve y haz un pull. No voy a entrar ahorita en detalles muy técnicos de qué es un push, qué es un pull y todo lo que vamos a ver en Gitcop. Lo tocaremos un poco más adelante en el curso, pero muy por la superficie. Podría ser todo un curso completo de manejo de Gitcoup, pero bueno, no es el caso. Vamos a utilizar Versel. Versel, como ya abrimos en la introducción, es donde vamos a hacer el deploy. ¿Okay? ¿Qué es deploy? Básicamente decir que mi app es pública y cualquiera con la URL dinámica que me genere, todo el mundo puede acceder y puede ver mi aplicación. Claro, si yo quiero, porque tú la puedes limitar. Este puede no solo hacer deploy, sino puede leer, listar los proyectos, como dice aquí, ¿por qué fallé mi último deploy? ¿Qué fue lo que pasó? ¿Qué te mandó Versel en su lock? ¿Qué te dijo que tienes que cambiar? Puedes editar variables de entorno, muchas otras otras cosas. Esa es otra cosa que vamos a conectar. N8N. Vamos a conectar el MCP de N8N. No tiene mucho que salió. Vamos a ver cómo obtener tu eh URL que te pide, cómo obtener tu API key, cómo conectarlo con H N. No tiene soporte nativo antigravity, pero nosotros vamos a conectarlo manualmente al igual que con Versel. Versel tampoco tiene soporte nativo, pero nosotros lo vamos a conectar. Y obviamente vamos a conectar Supase con eh Antigravity a través de el protocolo MSP. Entonces Antigravity tiene activo MSP y GitHub. ¿Okay? ¿Qué hay quiere decir que está nativo? Lo vamos a ver en unos minutos que tú literal te vas antigravity, le das eh conectar, simplemente te pid token y listo, ya se conectó, no te no te descaste absolutamente nada más. Y ahorita como vamos a ver con Versel y con eh lo que es N8N tenemos que copiar un cachito de código que es muy sencillo. Y ya una vez que hace eso se sincroniza y tal cual en la interfaz gráfica de Antigravity vas a ver lo mismo para Supase, para N8N, para GitHub, para Versel, vas a poder prender y apagar qué pueden hacer, qué tienen acceso y todo eso. pasa por crear tablas, leer tablas, crear los logins, autentificación, todo eso directamente con el MSP de Supase. Entonces, como les comentaba, que vamos a ver en el video en el ecosistema. Nosotros le pedimos algo a nuestra gente, en este caso puede ser eh Clotini, lo que estemos usando en antigravity. Va y se conecta las herramientas que necesitemos y nos regresa la respuesta. dice, "Listo, ya me conecté o me dijo esta información o ya hice esto que tú necesitabas." Okay, entonces sin más preámbulo, vámonos a Antigravity y vamos a conectar las diferentes herramientas. ¿Okay? Ya que estamos en Antigravity, ya viste cómo entrar a a Antigravity, lo vimos en el video anterior. Aquí está nuestra consola. Así es como como iniciamos. Y lo primero que vamos a hacer es conectar GitHop, que para mí es lo más eh importante. Entonces, ya que está aquí en Antigravity, aquí en la parte de arriba le vamos a dar en los tres puntos, le vamos a dar en donde dice MSP Servers y aquí nos va a listar todos los servidores MSP que ya vienen preconfigurados, la conexión, digamos, con Antigravity. Entonces, nosotros vamos a escribir gitube. Simplemente le vamos a dar un click y aquí arriba le vamos a dar donde dice instalar. Nos va a pedir un token para poderlo conectar. Okay. Entonces, para esto nos vamos a ir a GitHub que para esta tú ya deberías de tener tu cuenta de GitHub. Entonces, vámonos para GithitHop. Okay, le vas a dar aquí en tu usuario, le vas a dar donde dice settings. Ya que estamos en settings, le vamos a dar hasta abajo donde dice developer settings. Después, ya que estamos aquí, nos vamos a ir a personal access tokens, tokens clásicos. Aquí ya tengo varios que estaba probando, pero vamos a hacer desde cero. Vamos a generar un nuevo token. Obviamente de nuevo nos aseguramos que sea clásico. Nos va a pedir en este caso si lo tienes configurado, un 12FA o algo así que confirmes vía correo. Entonces a mí me tendrá que llegar un código a mi correo. Simplemente lo voy a copiar y lo voy a pegar para confirmar que si soy yo la persona que está intentando acceder. Entonces vamos a ponerle demo imperio digital. Queremos que expire 30 días, 60 días, 90 días. Custom no expire. En ese caso, yo lo voy a hacer 7 días simplemente para cuestiones de prueba. ¿Qué queremos hacer? Queremos darle acceso al repo completo. Estos son los scopes, como cuando conectas ah, no sé, Google Cloud que te tienes que meter y decirle, "Okay, quiero que tengas acceso a Google Sheets, quiero que tengas acceso a esto." Como cuando conectas Air Table, ¿no? Quiero que puedas leer las tablas, quiero que puedas leer la base completa, quiero que puedas leer mis webhots, es exactamente lo mismo. Entonces, les damos acceso a Repo, le damos acceso a Workflow, le damos acceso a packages. No queremos que elimine nada, no necesitamos darle acceso de control de admin control. Eh, le damos, no necesitamos darle acceso a la publicy, le damos acceso al repo hooksi, al gificaciones también. Usuari, no necesitamos darle nada. Discusiones, enterprise, audit lock, cpaces, copilot, no lo necesitamos. Configeraciones de red no lo necesistamos. Proyecto, sí. Y de ahí ya no necesitamos nada más. Y le vamos a dar generar token. Okay, ya que le damos generar token, copiamos este token, nos regresamos antigravity, lo pegamos y le damos guardar. Okay. Muy probablemente cuando les dé guardar le va a dar este error. ¿Por qué? Porque Antigravity intenta eh configurar Github a través de Docker. Okay. Docker es, digamos, como un manejador de paquetes. Lo voy a poner en palabras sencillas. De hecho, si están utilizando Easy Panel, Easy Panel utiliza Docker, que son como los para más bien los contenedores. Nosotros no nos sirve tener el GitHub con Docker, no es que no nos sirva, si no es demasiado complicado y para este caso no lo necesitamos. Así que, ¿qué es lo que vamos a hacer? Vamos a configurarlo nosotros manualmente para que no intente conectarse a través de Docker. ¿Okay? Entonces, ¿qué es lo que vamos a hacer? Nos vamos a ir de nuevo a Manage MCP Servers. Ya que estamos aquí, nos vamos a ir donde dice view Rock Config y nos va a tirar toda la configuración de el MSP server de Git. En este caso, aquí está el token que nosotros acabamos de generar. Aquí está el la dirección, etcétera. Y si se fijan, aquí dice que es comando docker y esos son los argumentos. Okay. Esto no nos sirve o no para lo que queremos. Entonces tenemos de dos. Podemos hacerlo con Antigravity o lo podemos buscar en Google. Así que yo digo que la hagamos con Antigravity. Vamos a darle para atrás a los agentes y vamos a decirle, estoy configurando el MSP de GitHop, pero me sale como si fuera un Docker. Me puedes dar el código Jason para configurar el MSP de GitHub, pero con NPX. Ahí está. Vamos a mandar. Vamos a ver qué nos dice. Ahí está. Listo, aquí nos está dando el código, simplemente nos dice que reemplazas tu token aquí y que tengo que reemplazar esto. Entonces, ya tenemos aquí mp servers, MCP servers, githupando argumentos, variable de entorno, personal token. Entonces, simplemente vamos a sustituir lo que nos pide. En lugar de GitHook MSP Server, vamos a escribir GitHub y borramos todo lo demás y lo dejamos como tal. Comando no es docker, sería npx. npx argumentos no lleva ron básicamente no lleva nada de esto. Y la e la cambiamos por y no lleva tampoco esto. Y nos está pidiendo que pongamos esto. Lo pegamos. Después tenemos la cerramos el corchete m token, etcétera. Vamos a ver si sí es cierto. Le vamos a guardar. Nos vamos a regresar a manch MCP. Le damos refrescar y vemos que ya está configurado Github 26 dice que tenemos acceso a todo esto. Nosotros podemos apagar dependiendo de lo que necesitemos. En este caso, no lo apagues. No, no, no te va a afectar en nada. Así que vamos a hacer una prueba. Acabo de configurar mi MCP de GitHop. Puedes verificar que efectivamente está funcionando la conexión. No sé, haz un get repositories o algo para que yo vea que sí puedes tener acceso a mi GitHub. Vamos a pedirle que nos confirme que efectivamente está funcionando GitHub. Después de que configuramos el MSP dice perfecto. Voy a verificar la conexión. y dice, "Excelente, la conexión de MSP de GFU está funcionando perfectamente y eso es lo que pudo tener acceso. Así que perfecto, ya terminamos con Kitoup. Ahora vamos a conectar la otra que estábamos hablando que es muy importante que es suabase. Entonces escribimos suabase que en este caso también tiene nativa, y vamos a darle donde dice instalar. nos va a pedir el superabase access token. Okay, diceabase personal access token. Si ustedes le dan aquí en la flechita, los va a mandar directamente a la página donde pueden generar el access token de su le voy a dar eh me está pidiendo aquí que vuelve a iniciar sesión. Entonces vamos a iniciar sesión. Yo tengo mi Supase conectado con mi GitHub. Si yo les recomiendo que lo hagan de esa manera, es lo más fácil porque así utilizan una sola cosa para conectar y lo mismo para ver sell como vimos en el video anterior. Entonces nos están mandando directamente aquí a los Acens token. Vamos a darle donde dice generate new token. Vamos a ponerle demo imperio digital y vamos a decirle que 7 días generamos el token. Lo copiamos. Vamos de vuelta antigravity, lo pegamos, le damos guardar y si nos vamos a configurar, nos vamos a tools, vemos que ya todo eso está conectado. Y si nos vamos a manage NCP servers, le damos view rock config, vemos que ya está aquí suabase con el modo, el comando npx que es igual que tenemos como tenemos Gitu. Entonces, vámonos de regreso con nuestra gente y vamos a decirle, "Okay, genial. Fíjate que también acabo de conectar el MCP de Supase. ¿Me puedes confirmar que tienes acceso para ver mi proyecto? Eso es simplemente como buena práctica que cada vez que conectes algo pedirle a tu agente confirmar que efectivamente tenga acceso. Entonces me dice, "Excelente, la acción con el MCPS Pav también está funcionando perfectamente. Puedo acceder, puedo ver que es es tu proyecto, bla bla bla bla bla." Entonces ya lamos dos de dos. Okay, entonces ya que conectamos, vamos a hacer lo mismo para Versel, como veíamos, si me voy aquí directamente a MCP Servers, yo busco Versel, no existe, no viene nativamente, así que vamos a conectarlo, pero vamos a hacer una forma diferente. En lugar de pedirle aquí a la guía vamos a a ir a buscar la documentación oficial, vamos a ir de vuelta a Manage MCP Servers, ya lo tenemos aquí, view config para que nos abra el Jason y vámonos a Google. y pongamos MCP Server Verscel NPX. Y siempre te recomiendo que visites o verifiques la documentación oficial. Aquí donde dice todas las plataformas no sale eh como tal antigravity, pero puedes usar Gemini Code Assistant o lo que es Gemini CLI, si te fijas, exactamente el mismo. Entonces vamos a copiar. Como estábamos viendo antes, ¿no? Necesitamos de donde dice MCP server, necesitamos a partir del nombre. Sería de Versel hasta aquí porque esta está cerrando esta. Entonces vamos a copiar, nos vamos a Antigravity, estamos en nuestro Jason, le ponemos una coma aquí para abrir uno nuevo y le damos pegar. Okay, fij en este caso no nos pidió nuestro token, no hemos generado ninguna conexión, así que lo más seguro es que cuando le demos guardar nos pida que de alguna forma que hagamos uno outdo mi file, me regreso mis MSPs y refresco. Aquí me dice Versel y vamos a darle que está todo esto. Vamos a darle configurar. Está mandando para acá, así que le vamos a pedir a la gente, acabo de conectar manualmente el MSP de Versel, es decir, editando el MSP Config de Jason. Puedes verificar si ya hay conexión. Es que no me pidió mi token. Ah, le voy a dar acceso a el archivo. Dice que no me pidó el token porque probablemente había una sección global, ya había iniciado sesión anteriormente con el CI de Versel, Versel login en tu terminal con el comando npx MCP remote puede estar utilizando esas credenciales cacheadas. Confir remota al usar protocolo de forma transparente y detecto sesión activa en el sistema. Okay, entonces como tenía abierto en el sistema Versel, me lo detectó, pero vamos a ver si podemos forzarlo para que quede en el video. Okay. ¿Cómo hago un logout de Versel para volver a hacer un login? Es que estoy grabando un video, un tutorial. Vamos a ver qué nos dice. Quiero forzar que me piden esa sesión para que ustedes vieran cómo se vea la primera vez cuando lo conecten. ¿Qué hay que mostrar en tu video? Cuando vuelvesas a ejecutar esto, verás lo siguiente. Determinate un enlace para abrir el navegador tepizar la conexión de tu cuenta. Vamos a copiar esto. Si no saben cómo abrir el la consola, le dan aquí arriba en el icono donde dice togle panel y la abren. Y aquí vamos a darle un logout. Dice que comando not found. Entonces, npxel logout. Okay, dice que no estoy logueado, entonces vamos a darle un login y me dice visitversel.com device y voy a copiar esto. Le doy enter, me va a abrir el browser y este es el código, así que le voy a dar que permito la conexión. Satisfactorio. Regresamos y me dice que estoy conectado. Así que ya saben, configuren su aquí el el MSP, le dan NPX Versel login, les va a salir esto para que vayan y autorice. pueden hacer de esta manera, ya no necesar el token porque con este comando de Versel, ya que tengan el MCP puede generar esa conexión. En mi caso, como yo me salí y volví a entrar para guardar para grabar este video, me por eso me salió, pero tal cual usen ese comando y les va a salir. Y por último, vámonos a configurar N8N. Si nos vamos para acá y vámonos a MCP Servers, otra vez buscamos N8N, vemos que no existe. Okay, entonces vamos a hacer un recap en dónde nos quedamos. Ya tenemos GitHub, Supasel para conectar N8N. Si nos vamos aquí para ver nuestros agentes, cerrar esto nuevo, le doy aquí en MCP Servers y si buscamos en 8N, como hemos visto, no viene predeterminado. Así que les voy a enseñar otra manera diferente de conectarlo. Vámonos a nuestro navegador y vamos a poner NHN MCP Server y vamos a la documentación oficial. Aquí nos dice cómo configurarlo, el acceso, las llaves, los workflows, todo usando o outando el access token, lo que podemos hacer, etcétera. Y los argumentos, todo lo que le tenemos que decir. Esa es una manera en la que la podemos conectar tal cual, pero ¿qué les parece si vemos una manera diferente? Vámonos a GitHop y vamos a buscar el MCP oficial de N8N en GitHub. Entonces, sé que no parecía el oficial, pero es este que está aquí. Lo abrimos y nos vamos para abajo. Vamos a encontrar el RMI, que prácticamente es muy parecido a lo que tenemos en directamente en la página oficial de N8N. Okay, nos está diciendo todos los argumentos, qué podemos hacer, eh, etcétera, ¿no? Entonces, obviamente vamos a hacerlo de una manera mucho más sencilla para que no tengan que leer toda la documentación o no tengan ustedes que ir y y decirle a la interprétame esto. Todo mira, aquí dice antigravity nos va a mandar directamente para acá. ¿Cómo lo podemos hacer? tu URL de producción, npm install GN8 NMCP. Si nosotros le damos este argumento no los puedo instalar, pero volvemos a lo mismo. Les quiero enseñar otra forma diferente de conectarlo. Vamos a copiar. Entonces, un vámonos de vuelta. Tenemos dos opciones, lo copiamos directamente de aquí o le damos en esta flechita y nos da todo esto. Vamos a copiarlo. Vámonos a Antigravity. Abrimos un nuevo agente. Vamos a ponerle tres prolog. Pegamos, ¿no? Esto y vamos a decirle, te estoy dejando el enlace oficial de GitHub del MCP de N8N. Quiero que clones este repositorio localmente en esta carpeta y que lo ejecutes, lo leas y me des la configuración local. Dime dónde poner mis credenciales y mi URL para que el MCP esté funcionando. Y lo mandamos. Vamos a darle un tiempo para que piense. Y me está pidiendo permiso para correr el comando. Le damos que sí. Como ven, les está enseñando varias formas en las que pueden configurar diferentes MCPs directamente con token, con autenticación o out poniéndolo manualmente el que ya viene por defecto, etcétera, por si les toca en su momento configurar diferentes MCPs, tengan todas las opciones posibles. Voy a ponerle pausa en lo que corre todo esto y regreso ahorita ya que me termine. Listo, ya terminó. Dice, "Listo, he completado la instalación. ¿Dónde poner tus credenciales? Tal cual aquí. Entonces vamos a darle refresh. No sale en MCP, obviamente no está configurado, así que vamos a darle view R config. Y aquí nos está pidiendo que pongamos nuestras credenciales. Dice, "Pon aquí tu URL y pon aquí tu AP." Okay, perfecto. Entonces, vámonos a mi N8N. Tengo dos opciones. Puedo tomar mi URL directamente de aquí o la URL que me da Easy Panel. Vamos a ver cuál de las dos me acepta. Vamos a copiar esto. Vámonos de vuelta Antigravity. La cambiamos aquí y me borré esto. Vámonos a generar una AP key. Aquí abajo en settings. NHNI. Creamos una demo imperio 2 7 días, no tocamos nada de los scopes, lo dejamos como está así. La copiamos regresamos ante Gravity, sustituimos esto y le damos file, le damos save. Nos regresamos a manage y le damos refresh. Okay, al parecer ya está bien, me sale todo en azul, todo prendido, así que como siempre hagamos una prueba. ¿Me puedes listar los workflows que tengo en N8N? Vamos a ver qué nos dice. Okay. Editar imágenes. Ag edición Telegram. Catalí Sistem Gener imágenes. Chat bote guapi con K gente WhatsApp de P digital. [resoplido] Okay, perfecto. Entonces sabemos que está funcionando perfectamente. No vamos a crear ahorita el el Hello World. lo vamos a hacer más adelante. Entonces, ya ahorita está todo conectado. Vamos a recapitular de nuevo. Conectamos Supabase, GitHub, Percel y NHN. Cada uno de una manera distinta. Todos llegamos al mismo objetivo. Y qué sigue, vamos a continuar. Antes de eh seguir con esta serie de videos, aquí vamos a hacer una bifurcación. Vamos a partir. El siguiente video después de este curso que vean va a ser una vez que ya tenemos configurado el MSP, ya tenemos configurado Antigravity, vamos a hacer una win rápida. Quiero que en el siguiente video de 0 a 100 hagamos una aplicación con deploy en Versel. ¿Qué vamos a hacer? Vamos a hacer un clon de Link Tree para que puedan tener su Link Tree sin tener que pagar para sus redes sociales y lo vamos a hacer deploy a Verel. van a obtener el dominio para que lo puedan empezar a usar, lo pueden empezar a compartir, lo pueden empezar a poner en sus perfiles de TikTok, de Instagram, en cualquier red social que tengan y no tengan que pagar link directamente. Vamos a hacer eso en el siguiente video, una win super rápido y después de eso continuamos con el proceso completo para hacer una aplicación desde cero con la de con el deploy final. Nos vemos en el siguiente
