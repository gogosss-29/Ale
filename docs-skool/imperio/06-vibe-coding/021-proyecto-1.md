# 🏆  Proyecto 1

> Ruta: Vibe-Coding › 🏆  Proyecto 1

**🎬 Vídeo (? min):** https://youtu.be/d6mXu2tlevk

---

## Parte III. Primera win. Clon de Linktree en tiempo récord (repo listo para clonar)

En este módulo hacemos tu primera win real con Antigravity. La meta es simple. Pasar de idea a app pública en Vercel en menos de 30 minutos. Terminamos cerca de los 35. Sigue siendo una win.

Si quieres clonar la app ya terminada, aquí está el repositorio

```txt
https://github.com/agenciainsigniaia-oss/nova-bio-link.git

```

## Qué vas a construir

Un clon simple tipo Linktree para centralizar tus links y usarlo en tus redes:

- Foto y bio
- Botones a redes (LinkedIn, Instagram, Facebook, TikTok)
- CTA de “Recursos / Toolkit” y “Trabaja conmigo”
- Captura de email para leads (sin Supabase. MVP)
- Deploy público en Vercel

No usamos Supabase en este video porque no lo necesitas para un Linktree. Queremos velocidad.

## Tech stack del video

- Antigravity (orquestador)
- React + Vite + TypeScript
- Tailwind
- GitHub (para repo y versionado)
- Vercel (para deploy)
- n8n (para capturar emails por webhook)

Cuentas necesarias (todas pueden ser gratis):

- GitHub
- Vercel
- n8n (cloud o self-host)
- Antigravity

## Flujo del video (lo importante, sin relleno)

### 1) Prompt. Cero técnico

Le damos a Antigravity un prompt con:

- Estilo (neobrutalista)
- Marca ficticia (Alex Nova. Nova AI)
- Secciones (bio, links, CTA, footer)
- Objetivo (captar correos y centralizar redes)

Antigravity decide framework y estructura. Tú solo defines resultado.

### 2) Ver la app local sin complicarte

Cuando termina, corres:

- `npm run dev`  
y abres el [localhost](http://localhost).

Aquí es donde confirmas si el diseño ya está usable antes de moverle algo.

### 3) Truquito clave. “Ver lo que yo veo”

Le pides al agente que abra el navegador y vea tu app. Antigravity navega, hace scroll, prueba botones, rellena campos, toma screenshots. Esto acelera QA y cambios visuales.

Cambios que pedimos en el video:

- Efecto “flip” en la foto de perfil en escritorio
- En mobile, alternar imagen cada 2 segundos con animación
- Links reales para “descarga” y “trabaja conmigo”
- Actualizar URLs de redes

### 4) Captura de emails sin Supabase. Usando n8n

No hacemos base de datos. MVP.

Idea:

- El formulario manda el email a un **webhook de n8n**
- n8n recibe el payload
- Luego tú conectas lo que quieras. Gmail, Google Sheets, Airtable, CRM, newsletter, etc.

Workflow sugerido en n8n:

- Webhook trigger
- Validación mínima (email no vacío)
- Guardar o enviar a donde quieras
- Responder al front con confirmación

Nombre del escenario en el video:

- “Linktree lista de correos”

### 5) Buenas prácticas. GitHub como debes hacerlo

Cuando ya está funcionando:

- Crear repo
- Commit inicial
- Push
- README claro con: - cómo correr local
- qué hace la app
- dónde configurar el webhook de n8n
- qué variables se usan si aplica

Esto es parte del producto. No es opcional si lo vas a compartir o vender.

### 6) Deploy a Vercel desde Antigravity

Con el MCP de Vercel conectado, le pides:

- Crear proyecto
- Build
- Deploy
- Validación final en producción

Después pruebas:

- link público abre
- botones funcionan
- formulario dispara webhook
- n8n registra ejecución

## Qué aprendiste en esta win

- Cómo usar Antigravity para construir una app completa con un prompt
- Cómo hacer QA visual con navegador controlado por el agente
- Cómo resolver captación de leads sin backend pesado usando n8n
- Cómo cerrar el loop completo: repo + deploy + verificación

## Lo que viene después

En los siguientes videos ya entramos en modo serio:

- Supabase (tablas, relaciones, seguridad básica)
- Auth
- Integraciones con Gemini
- Variables de entorno en Vercel
- MVP listo para vender o usar en producción con mejores prácticas

##

## 🎙️ Transcripción

Perfecto. Entonces, ya que tenemos todo configurado y conectado, vamos a hacer tu primera win. Vamos a hacer lanzar algo rápido. Vamos a ser en tiempo récord. Voy a intentar no pausar este video a ver si logramos llevar una app dea a la app física deploy en menos de 30 minutos. Entonces, ya tenemos lo que es antigravity configurado. Sabemos cómo funcionan los agentes, los diferentes eh modelos que podemos utilizar. Ya conectamos los cuatro MCPs principales que vamos a usar. Entonces, ¿qué vamos a hacer ahorita? Vamos a construir un clon de link para que lo puedas hacer en tus redes sociales y que puedas utilizar eh puedas poner el lit magnets o contáctame, trabaja conmigo, etcétera. Algo muy sencillo. En este caso no vamos a usar Supas porque no necesitamos supace para esto que estamos haciendo. Así que vamos a hacer un deploy muy muy rápido. Vamos a darle un vamos a intentar que sea uno o dos proms a lo mucho. Vamos a darle todo directamente antigravity. Y de ahí hacemos el deploy a Ver. Entonces, ¿qué vamos a hacer en este caso? Esto, de hecho, esto lo creé con Google Studio justo para este este mini mini video del curso de la primera win. Dice, "Bienvenido builder antes de clonar el intrig usando antigravity en minutos. Un tutorial interactivo paso a paso para dominar la IA y el display modero." Vamos a empezar. Dice la gente y el PROM, dice, "Quiero crear un link minimalista con fondos degradado obscuro y botón alrededor es un ejemplo, ¿no? Dice subir imagen. Voy a escoger una imagen que yo tengo aquí y dice Protip usa imágenes claras de referencia para que la agente entienda tu identidad visual. Vamos a darle continuar. dice, vamos a darle agregar enlace, por ejemplo, tenemos Instagram, vamos a hacer que sea Facebook y yo me dice que aquí le pongo https 2.com y barra mi Facebook, el nombre que tengan ustedes, ¿no? Y digamos si qui hacer también TikTok, entonces vamos a ponerle TikTok. Eso es nada más una demo, no va a ser así la programación, pero es para que entiendan un poquito. Y sería https pun doble diagonal TikTok, mi perfil, ¿no? Por ejemplo, vamos a darle continuar y dice, "Configura tu enlace de email." Hola. Vamos a ponerle eh Imperio. Hola @ imperiodigital.com. Vamos a darle generar proyecto. Vamos a hacer un push to githup. Obviamente esto no hay una conexión de gh de para que vean lo poderoso lo que se puede crear con un solo. Esto es un solo promp. Lo que podemos crear con un solo prompt. Vamos a ir a deploy a Versel y listo. Así tenemos nuestro link que podemos utilizar, poner en nuestras redes sociales, etcétera. Entonces, ¿qué les pareció esto? Vámonos directo a Bueno, antes de irnos Antigravity, si no conoc tre, es esta plataforma muy famosa, seguro de visto en redes sociales algún creador de contenido, alguna empresa, sobre todo creador de contenido y ves, te metes a su perfil y dice mi linktri o mis redes y lo abres y te sale más o menos algo así, ¿no? mi canal de YouTube, mi cuenta de TikTok, Instagram o equipo de video, si tienen alguna cuenta de afiliados, más o menos esto. Obviamente hay gratuitos que te permiten hacer muy poquitas, si te fijas casi todos se parecen y está la versión de pago. Entonces, vamos a hacer un clon mucho más interactivo, mucho más bonito, vamos a hacer la menor cantidad de programas posibles. Ahora sí, hab dicho eso, vámonos a Antigravity. Estando en Antigravity, vamos a abrir nuestro agente directamente de acá. Vamos a darle nuevo a gente esta conversación. En este caso vamos a usar un prolog, vamos a usar el método planeación. Y yo ya tengo mi prompto. Lo hice con eh charge pt. Literalmente le dice, le dije, quiero crear un clon de Link Tree para utilizar en mis redes sociales como si fuera un influencer. Quiero que el estilo sea neobrutalista. Y le dice, le dije, inventa la marca, inventa el nombre del influencer, haz todo Domi para poder generar esto para un video. Literal es todo lo que elijt me dio un prompt. Se los voy a pegar aquí que más o menos es esto. Dice Bio Link page tipo Linkry, estilo neobrutalista, marca personal ficticia, contexto de la marca Alex Nova, marca Nova AI, influencer de automación y sistemas digitales. Objetivo captar correos con recursos de alto valor, centralizar redes sociales, etcétera. Les voy a dejar el prom aquí abajo del video por si lo quieren copiar, lo quieran adaptar con todas las diferentes secciones, sección uno, sección dos, sección tres, empezar hoy footer, todo es muy muy sencillito. Y vamos a darle enviar. Recuerden que voy a intentar no pausar el video para poder ver en tiempo real cuánto nos tardó hacer esta app de cero a deploy. Okay, está procesando. Usé el modo planear, entonces va a tardar un poquito más. Okay, ya creó las task, va a inicializar el proyecto de Vite, va a instalar las dependencias, va a limpiar un poco, va a empezar a trabajar con el diseño y el estilo. Le dije que sea neo brutalista. Mientras carga esto, les voy a enseñar, bueno, le voy a decir, vamos a leerlo rápido, ¿no? Diseño neobrutalista, colores, componentes, mi index, mi header y verificar el plan. Okay, poniendo que vamos a creer 100% lo que nos diga, todo va a salir bien. Vamos a darle proseguir. Mientras empieza a trabajar en esto, les voy a enseñar un poco qué es un diseño neobrutalista. Vitalismo, diseño gráfico es más o menos este estilo. Muchos cuadrados, letra grande, colores brillantes. Eso es el estilo neobrutalismo. Okay, vámonos de vuelta. Integravity dice que acepte para correr. Va a generar el proyecto. Está utilizando React y y Bitter. Vamos a empezar a darle que sí que empiece a frenear todo. Igual no voy a poner pausa, así que voy a intentar narrar. Vámonos a nuestros task. Okay, ya hizo esto. Bueno, está en progreso. El circulito que está en progreso y es lo que podemos ver aquí. Y va ahorita a iniciar el proyecto de BTE, que es lo que está haciendo. Va a instalar todas las dependencias que se necesite. Y ahora le dije, quiero que utilices esa tecnología. quiero que utilices eh este método. Yo nada más le dije, quiero este resultado y la ella está decidiendo en qué con qué framew, metodología, tecnología va a usar y todo. Yo le pude haber dicho, "Hazmelo en un HTTML con CSS básico." Y también me lo hubiera hecho de esa forma. Entonces, literal, mi profo eh técnico en este caso. Entonces, vamos a decirle que sí a todo está corriendo parámetros, está instalando, está revisando. Se fijan, ahorita está apenas analizando todo. No tengo nada de este lado. Ahorita vamos a ver cómo va a empezar a generar todo dentro de esa carpeta. me empieza a generar todos los documentos, archivos, todo lo que él considera que vamos a necesitar para este aplicación. Como yo no le dije dónde voy a hacer el deploy ni qué voy a tener ni nada, muy probablemente me está generando archivos de más que no necesitemos, pero queremos hacerlo lo más básico, al nivel más básico del usuario que le diga a la IA. Quiero hacer esto. Ve y hazlo. Vamos a revisar el plan. Okay. Task. Voy a ver si puedo adelantar un poco esta parte. No quiero poner pausa para que se pueda ver cuánto duró, pero tampoco me tenga que estar escuchando narrando. Okay, dice que inicializó el proyecto aquí. Local host 5173 y ya va haciendo esto. Vamos a ver si lo podemos visualizar. ¿Qué pasa si nos vamos a https dos puntos diagonal diagonal local host 5173? Nos va a mostrar algo. Ah, dice que no, también no se ha hecho el deploy. No hay problema. Vamos a darle aceptar. Okay, está trabajando en el index HTML. Aquí ya puedo ir viendo las cosas que va creando, tags. Ya hice todo esto, está generando, definiendo el CCS, la tipografía, etcétera. Nueva Bink. y todas las carpetas que necesitamos. Me está generando las imágenes con nanovanana. Eso está perfecto. Recuerden que eh al tener directamente nuestra Gravity nuestra cuenta Yemini, pues estamos eh puede generar usar ahí al acceso que tenemos a la cuenta de Yemini y utilizar eh aparte de los modelos que tenemos Yemini 3 Pro, High, Flash, etcétera, pues tiene acceso a Nanobanana y a muchas cosas que son directamente de Gemini. Aparte si nosotros queremos podemos generar las APIs desde nuestro Google Studio y darle una API de Gemini para que eh genere ya cosas directamente cuando estés interactuando con la interfaz. Por ejemplo, si yo quisiera poner un generador de imágenes con banana en mi app que voy a desplegar, tendría que darle yo una API key de Yemini para que pueda hacer la llamada y utilizar esa API key. Obviamente aquí como estoy en antigravity pues está usando directamente los tokens de mi cuenta, digamos. Para que lo tengas desplegado, pues es importante poderle dar tu yemin aquí para que pueda realizar esa esa conexión. Okay, entonces está trabajando en la parte, sigue en la parte de diseño y fijan, van apareciendo más cosas en todos los documentos. Lo puedes ir viendo en tiempo real todo lo que está lo que está editando. Y aquí me pide que acepte, pero no le voy a dar nada. Voy a dejar que todo lo haga directamente él. Y aquí ya puedo ir viendo lo que está haciendo. Está ahorita actualizando Task. Ahorita en unos segundos deberá de actualizarse eso. Y como pueden ver está creando todo lo que necesitamos. Muy bien. Y aquí es interesante porque también pueden ir viendo los tokens que está que está generando. Y podemos ir viendo aquí exactamente todo lo que está trabajando, hace cuánto lo editó, etcétera. Una vez que termine, como tenemos conectado GitHop, como lo vieron en el video anterior, podemos pedirle que haga un commit, que mande todo directamente, etcétera. Les prometí no poner pausa, pero creo que por su bien sí les puedo poner pausa. Tampoco quieron ver un video de media hora nada más hablando, pero les prometo que les voy a decir tiempo real cuánto se tarda en generar esto, porque al ser el modo eh planeación va a tardar un poquito más, pero es más probable que quede todo. A lo mejor es un prompí que tengamos que estar viniendo pidiéndole que modifique algunas cosas. Okay, van aproximadamente 3 minutos desde que le puse pausa. Como pueden ver, ya hizo todo esto. Está haciendo la parte de verificación y pulir los detalles. Y ahorita que termine esta parte de verificación y pulir, les voy a enseñar un truquito bastante padre. que está corriendo. Vamos a ir viendo que ya tenemos todos estos archivos con todo lo que fue creando. No importa si no tiende nada, no necesigravity. Obviamente si se fijan aquí pues bien tienen un un texto que si ustedes no les gusta que diga tool kit y caja de herramientas lo quitan y le dan guardar y tal cual para que no no se lo pierdan la leía, si no tal cual y pueden decir necesito que me cambies esto, esto, esto, esto, esto. Ahorita lo vamos a ver con un una opción bastante interesante que les voy a enseñar ahorita en vivo. Entonces, vamos a regresar al task y vemos que está eh preparando lo del walkthrough y finalizando todo. Vamos a ver si ya lo podemos ver o si hay que hacer ahorita el deploy. Obviamente no vamos a acceder todavía. Ahorita les voy a enseñar cómo podemos acceder. Okay, me está pidiendo un npm R build que lo acepte. Básicamente es construir la la aplicación, digamos. Okay, dice aquí ya corrió todo. Dice resumen del proyecto, cómo ejecutar el proyecto, cd nova biolink, npm rond def y va en el local host. Okay, entonces les enseño, me voy aquí, refresco, obviamente no puedo ver nada, así que regresamos antigravity y le damos aquí arribita donde dice todo el panel y nos va a abrir la consola. Así que vamos a hacer lo que nos dijo esto. CD Nova GU BU link enter y si conocen un poquito comando CD es para navegar hacia el directorio y después me pide que haga un npm run def. Listo. Me dice que ya está listo en 5173 de local host. Me puedo venir para acá y refresco y no nos permite verlo. Network is just expose 5173. Vamos a copiarlo y vamos a pegarlo y listo. Aquí tenemos nuestro estilo link, Alex Nova, automatizo, negocios con Toolit herramientas, tu mejor email. Vamos a ver qué pasa si pongo mi correo porque no le dimos ninguna instrucción. Le voy descargar y dice que listo, pero obviamente no está haciendo nada porque no le dijimos newsletter privada. Lo voy a dar mi correo otra vez. Obviamente no no va a hacer nada. y mi LinkedIn, Instagram, Facebook, TikTok y trabaja conmigo ver servicios y obviamente no empezar hoy y está. Okay, perfecto. Entonces vamos a hacer dos cosas. Vamos rápido antigravity y le voy a decir, "Okay, necesito que vayas, veas lo que yo estoy viendo para que veas los colores y el diseño. la foto de perfil. Te voy a pasar yo una foto de perfil y lo que quiero que hagas es que cuando pases el mouse en la foto de perfil esto en versión escritorio haga como un estilo flip que voltee la imagen y se ponga mi la foto que tienes ahorita y cambio por la foto perfil que te voy a subir y en mobile quiero que cada 2 segundos cambie dinámicamente con una animación. Okay, ahora lo que es la parte de eh descargar y el email list, obviamente no están haciendo nada. descargar. Quiero que mandes hacia una página que te voy a dar donde descarguen un archivo y la parte de el correo que crees que podamos hacer para que si se suscriban al correo. También te voy a pasar aquí abajo las URL de mis redes sociales. Okay. Entonces, vamos a hacer una cosa. Le voy a cargar la imagen que quiero que utilice de de perfil. Vamos a buscar una imagen mía. Okay. Y obviamente no voy a poner ahorita ninguna red social tal cual, pero lo voy a mandar, por ejemplo, ¿qué les parece si lo mandamos a la comunidad school? obtener enlace y vamos a decirle okay URL para descarga es esta URL para trabajar conmigo es esta. Y le voy a dar simplemente la de mi perfil de school. Obviamente ustedes aquí le pondrían la URL de su landing page, de su página web o lo que tengan y le voy a decir mis redes sociales. Actualiza los links. Okay. Y vamos a ver que tenemos LinkedIn, Instagram, Facebook, TikTok, así que le voy a poner tal cual no voy a poner redes reales. Voy a poner esto. Lo mismo para Facebook. Lo mismo para Instagram. Y lo mismo para TikTok. poner aquí TikTok y se la envío. Recuerden que en un principio le dije, "No que veas lo que yo estoy viendo y que veas los colores diseño de la foto y perfil." Vamos a ver si me hace caso ahorita para actualizar la foto. Vamos a darle aceptar. Aceptar. Y vean esa parte que dice preview. Vamos a darle aceptar y va a lanzar un browser. para que él pueda literal ir a ver lo que yo le estoy pidiendo. ¿Se fijan, yo no estoy moviendo nada? Eso, el alo azul que sale alrededor es eh quiere decir que Antigravity está viendo en el navegador para que vea lo que hizo, tal cual el diseño, los colores y y todo. Vámonos de vuelta antigravity. Y aquí vemos que sigue trabajando, está moviendo el mouse, está haciendo pruebas, está haciendo un resize, o sea, cambiando el tamaño de la pantalla para ver si se ve bien en mobile, si no se ve bien, etcétera. Está haciendo un scroll, está haciendo pruebas, está actualizando. Entonces, él mismo está viendo que está pasando y está entendiendo, está tomando screenshots y se va corrigiendo de eh todo lo que está haciendo, pruebas de ventana, de scroll, clicks, absolutamente todo. Y aquí podemos ver que si azul está trabajando y si se fijan está cambiando esto. Okay, dice que está trabajando los links. Tengo que dar confirmar que aquí sí que le estoy dando permiso de que le dé clic a los botones. Está pidiendo completar el campo. É, si se fijan, yo no estoy escribiendo nada. Él está escribiendo para hacer la prueba y redirigió a donde le pedí redigiera. En este caso, como desapareció elo azul, quece que ya terminó, así que vamos de vuelta Antigravity. Y ahorita está haciendo otras pruebas. Eh, aquí está haciendo las pruebas de abajo, eh, trabaja conmigo y etcétera. Dice que necesitan mi input, yo le puedo dar aquí para regresar y me está pidiendo permiso para interactuar con el resto de la página. Pedió clic ahí, me manda mi perfil, que es donde yo le pedí. Y si se fijas, sigue trabajando, está haciendo todas las pruebas. Dice que necesita mi permiso, quiere correr este script. Le voy a dar que sí y vamos de vuelta. Okay, se quitó el azul que sí que ya terminó. Antigravity dice que rendering playback y así que está renderizando el video para poder verlo y entender todo lo que está pasando. Y dice que está trabajando con unos problemas en dos cosas que identificó. Va a intentar navegar de nuevo después de lo que identificó para ver si se solucionaron los problemas. Ahora a intentar rellenar el campo y aquí le pondré pausa de nuevo, nada más para asegurarme que haya terminado. Perfecto, ya terminó. Fueron como otros 4 minutos. Dice, "Avatar interactivo, efecto flip implementado. Elaces y redirecciones reales. Tolk de trabaja conmigo redes sociales implementados. Estrategia de captura de email. Mi pregunta para pasar una simulación de una lista de correos real, mi recomendación técnica es integración con lead magnets. Actualmente el usuario siente que paga con su email para obtener el el tool kit de school. Eso es esto es excelente para la conversión. Base de datos suavis. Puedo crear una tabla con una base de datos real usando su pavis para que cada vez que alguien escriba su correo se quede guardado automáticamente. Una lista herramientas pro. Si yo salgo como B o convert kit, puedo conectar al formulario directo a Slapi para que los correos entren directo a tu newsletter. He verificado el diseño y efecto premium. Respeto a los tres bordes. ¿Te gusta conectar al formulario real ahora mismo? ¿Prefieres algún detalle visual primero? Okay, vamos a ver el detalle visual. Vamos a darle refrescar y vamos a hacer ya las pruebas. Deja pongo un correo. Obtener acceso. En la realidad ustedes no quisieran hacer esto porque una persona puede poner un correo falso y listo, ¿verdad? Lo mandan a otra sublanding que le puedo pedir a este mismo que se los genere donde tengan que verificar su correo y ya a ese correo le mandan el enlace después de verificar ya le mandan al link final. Eh, esto obviamente no va a funcionar. Lo LinkedIn me manda Instagram. Okay, perfecto. Y ver servicios me manda aquí. Muy bien. Entonces, vamos a ver. Visualmente me parece me parece genial. Te la volaste. No quiero implementar implementar Supas ahorita, lo quiero mantener esto como un MVP. Pero, ¿qué te parece si cuando pongan su correo y le den clic al botón eh, en lugar de que que generes una tabla de supace, ¿por qué no mandas un payload a N8N mandes el correo del usuario y yo en N8N me encargo de mandarles o guardarlo en en la tabla que yo que yo quiera, por favor, un escenario que se llame link tre lista de correos donde recibas con el workflow, el webhook, perdón, y después de eso yo ya me encargo en NHN. Vamos. Si se acuerdan, el video pasado vimos cómo conectar NHN con el MCP, así que en teoría no debería haber ningún problema para que haga esto. Está checando la conexión con N8N. Dice que todo está bien. Get note. Dice que está creando el link tri lista de correos. Vámonos a nuestro N8N. Ah, workflows. Y como ven, no está. Ahorita no los tendré que crear. está verificando al mismo tiempo otros errores, que acepte las modificaciones que está haciendo y window open tool kit error leit content type postwurl la va a tomar y ese es mi N8N Imperio Insignia toit. Entonces está actualizando y mientras termina esto, vamos a ver si de casualidad ya me generó el escenario. Vamos a refrescar. Aquí está link y lista de correos generado y yo le pedí únicamente que reciba. Yo ya me encargo. Perfecto. Vámonos de vuelta antigravity completa pasos. Okay. Vamos a Perfecto. Ya terminó la configuración. Ahora hagamos la prueba. Vamos a poner aquí nuestro correo. Unirme ahora. Listo. Revisa tu correo para confirmar y vámonos a NHN ejecuciones justo ahorita. y vemos aquí mi correo. Perfecto. Entonces, ya de aquí yo conectaría un nodo de Gmail o conectaría un nodo de eh después Google Sheet, table, lo que queramos ya para guardar estos leads que están dejando su correo. Entonces esta parte ya la continuamos con normalmente la haríamos, pero ya está funcionando la conexión. Okay, ya casi acabamos. Perfecto. Entonces vamos a decirle. Okay, pues todo se ve bien. Ya hice las pruebas. Me gusta cómo quedó la interfaz gráfica. ¿Qué te parece si creamos un repositorio en GitHub? Haces un push el commit, creas un readmi file y avísame cuando quede todo listo. Vamos a mandarlo a GitHu. Okay. Está pidiendo acceso a la consola para mandar el comando y status. está llamando la tool de crear repositorios para poderlo crear. Mientras hace esto, bueno, me va a pedir otro comando. Mientras hace esto, vamos rápido a nuestro Githup, al de nosotros. Vámonos al home. Vamos a ver que aquí tenemos Biolink. y que el repositorio, pero no tenemos nada, así que vámonos de nuevo anti Gravity. Aquí nos está pidiendo permisos. Aceptamos todo y está editando el ritmy, como le dije, analizando todos los paquetes, etcétera. que decidí hacer un push completo. Básicamente es como enviar todo a GitHub, todos los archivos, porque no habíamos hecho ningún push, ningún commit. Entonces va a actualizar ahorita el repositorio de GitHub. Eh, como es la primera vez, tiene que subir cada uno de los archivos. Igual no pesa mucho este proyecto. Y ya después cuando le hagas un commit simplemente va a actualizar únicamente los archivos que tienen una diferencia. como lo hace, hace un chequeo rápido, ve cuáles archivos no se han modificado y pues en ningún caso que los mande y solamente cambia los que sí han sido modificados. Perfecto. Dice hitos completados, repositorio creado, ritmo profesional, push inicial, git local. Vamos a ver. Repositorio de Redmi, una página biolink estilo características social, instalación, desarrollo. Okay. Sencilla pero bastante profesional. Y vamos a decirle, "Okay, ya lo vi, perfecto, me parece que todo está bien. Genero un nuevo proyecto en Versel y vamos a hacer un deploy. Recuerden como tenemos la conexión de MCP de Versel, le podemos decir que haga un proyecto que quiere decir que va a compilar, va a ser un npm build y después de eso va a crear el proyecto en Versel y va a ser deploy. Ahí está el npm build que les decía, lo está creando. Mientras voy a enseñarles igual. Vámonos a Verel directamente dashboard. Y si se fijan, solamente tenemos ahorita esto, que es lo que van a seguir viendo cuando termine este video. Continúen el curso y ahorita va a aparecer el otro proyecto. Vamos a darle aceptar. que sí mandé el proyecto a producción. Está subiendo, está haciendo el deploy y vamos a esperar a que termine. Vamos. Mientras aquí actualizamos. Ya nos aparece aquí no va Biolink. Vamos de vuelta para acá y está verificando. Vamos a decirle que siempre le damos permisos. Estaba verificando ya con el link de Versel que todo esté funcionando. Si se fijan, yo no le pedí que verificara, sin embargo, por mis instrucciones anteriores entendió que como acabamos de hacer un deploy, ya tenemos el link de Versel. Este link ya es público, lo pueden compartir. Entonces entendió que ya es necesario verificar que las funcionalidades que probamos el local efectivamente estén funcionando en eh verse ya con la app pública. Perfecto. Dice, "Búrele del proyecto, detalle de despliegue en Versel, equipo, estado, verificación final." Hizo todo. Así que vamos a cerrar esto. Vamos a nuestro antigo Versel, actualizamos y vemos que lo hizo hace 5 minutos. Ese es nuestro link público. Lo abrimos. Vemos que esto está funcionando. Esto está funcionando. Esto está funcionando. Vamos a probar. Vamos a ver. 8 refresco y vemos que acaba de llegar uno, así que perfecto, todo está funcionando. Felicidades, ya deberás tener tu primera appuny. Nos pasamos de los 30 minutos, pero por muy poquito, por 5 minutos, pero ya estamos listos. y continúa con los próximos videos para ver un poco más a detalle a profundidad cómo hacer una aplicación donde ya integramos Supace y muchas otras eh funciones. Yemini, la API de Gemini, utilizamos las variables de Sopa Base y de junto con Versel y va a estar muy bueno para que puedas tener la aplicación que tú sea que estés haciendo completamente funcional y lista para empezar a venderla o usarla para ti mismo. Entonces, espero que en este punto hayas podido hacer el deploy de tu primer app, la estés usando y nos vemos en el siguiente
