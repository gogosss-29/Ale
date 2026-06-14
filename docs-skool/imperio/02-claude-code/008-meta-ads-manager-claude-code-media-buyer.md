# Meta Ads Manager + Claude Code = Media Buyer

> Ruta: Claude Code › Meta Ads Manager + Claude Code = Media Buyer

**🎬 Vídeo (12.6 min):** https://www.youtube.com/watch?v=mfk82SbXgGo&t=93s

**📎 Recursos:**
- [Politica de Privacidad (enlace)](https://raw.githubusercontent.com/benjacord/meta-app-policies/main/privacy-policy.md)
- [Eliminación de datos (Enlace)](https://raw.githubusercontent.com/benjacord/meta-app-policies/main/data-deletion.md)

---

Le pagaba $600 al mes a Cristóbal para manejar mis Meta Ads. Era bueno en lo suyo, pero la realidad es que yo igual tenía que decirle qué hacer, qué cambiar, qué probar. En algún punto me di cuenta de que el trabajo real lo estaba haciendo yo, él solo lo ejecutaba.

Entonces armé esto.

Un agente en Claude Code que se conecta directamente a la API de Meta, sin dashboards de terceros, sin SaaS, sin intermediarios. Código real que corre en tu terminal y que puedes controlar con lenguaje natural.

En el video de arriba muestro exactamente cómo lo armé y cómo funciona en vivo. Acá te dejo el resumen y los recursos para que lo repliques.

---

**Qué puede hacer**

Todo lo que harías tú dentro del Ads Manager, pero desde la terminal con un mensaje:

- Ver en qué campañas estás gastando y cuánto
- Identificar los ads con mejor CPA
- Pausar o activar campañas y adsets
- Cambiar presupuestos
- Crear campañas nuevas completas, con copies personalizados por país
- Analizar tus top performers por período

Lo que me voló la cabeza fue cuando le pedí que creara una campaña de retargeting para mis 5 mejores países con copy personalizado para cada uno. A España le metió "No curres solo", a Chile "No batalles solo". Nadie le dijo cómo hacerlo, él lo infirió del contexto.

---

**Por qué funciona mejor que contratar a alguien**

No porque sea más inteligente que una persona. Sino porque nadie conoce tu negocio mejor que tú.

Cuando tienes un media buyer, igual tienes que explicarle el contexto, los ángulos, qué quieres probar. Aquí ese paso se elimina. Tú le hablas directo, el contexto ya está en el [CLAUDE.md](http://CLAUDE.md), y los cambios son instantáneos.

---

**El setup en 3 pasos**

**1. Crea tu app en Meta for Developers**

Entra a [developers.facebook.com](http://developers.facebook.com) → My Apps → Create App. Dale todos los permisos posibles (Marketing API, páginas, catálogos). Publica la app y genera un access token desde Graph API Explorer con todos los scopes que necesitas.

**2. Inicializa el proyecto con Claude Code**

Copia el prompt de abajo, pégalo en Claude Code con tu token al final y deja que lo arme todo solo. En menos de 2 minutos tienes el proyecto completo funcionando.

**3. Verifica la conexión**

```
node src/cli.js accounts
```

Si ves tus cuentas de Ads, estás listo.

---

**One Prompt Setup**

```
Tu rol es ser Matías, mi Ad Manager personal de Meta Ads. Tu trabajo es 
gestionar, analizar, modificar y crear campañas directamente desde la 
terminal usando la API de Meta — sin que yo tenga que abrir el Ads Manager.

Cuando te pida algo, lo ejecutas. Si quiero pausar un adset, lo pausas. 
Si quiero subir el presupuesto, lo subes. Si quiero una campaña nueva 
con copies por país, la creas. Operas en español y confirmas cada acción 
antes de ejecutarla.

Para empezar, crea el proyecto Node.js desde cero.

Stack propuesto: ESM modules, fetch nativo, dotenv, Meta Marketing API.

Archivos a crear:
- .env → META_ACCESS_TOKEN y META_API_VERSION=v21.0
- src/api.js → cliente HTTP base con manejo de errores
- src/campaigns.js → listar cuentas, campañas, adsets, ads, insights; pausar/activar; cambiar presupuesto
- src/analyze-countries.js → gasto por país, CPA, ranking de mejor a peor
- src/analyze-ads.js → top performers por compras y por CPA
- src/cli.js → comandos: accounts, campaigns, insights, pause, activate, budget, adsets, ads
- CLAUDE.md → Créalo con lo que necesitamos,

Cuando termines avísame. Pego el token y corremos node src/cli.js accounts para verificar.

MI TOKEN: [pega aquí tu access token]
```

---

**Lo que viene**

El siguiente paso natural es conectar esto con un generador de crea.

## 🎙️ Transcripción

Esta gente que estás viendo acá acaba de analizar más de $30,000 que he gastado en anuncios de meta. Encontró los mejores anuncios de retargeting, empezó a crear y modificar campañas solo y yo no tuve que abrir el MetaS Manager una sola vez. De hecho, aquí podemos ver tenemos un historial con más de 14 millones de impresiones y esta campaña que está acá la creó completamente él. Lo más interesante es que puede literalmente crear nuevas campañas, analizar, hacer informes, puede hacer todo lo que tú harías dentro del Metaarts Manager, pero en Cloud Code con un mensaje y acciones conversacionales. Esto es realmente una locura. Y si te quedas hasta el final de este video, vas a aprender cómo hacerlo por tu cuenta. Te voy a mostrar absolutamente todo. El sistema completo, cómo lo armé, qué significa esto, lo que viene después. Y vamos a cubrir las siguientes tres cosas. ¿Qué es este sistema exactamente y cómo setearlo? Y en ocasiones, ¿por qué funciona mejor que contratar a alguien? casos de uso en vivo, es decir, cómo me analizó más de 10000 creativos y me tomó los que mejores estaban desempeñando y lo tomamos para un nuevo ciclo. Y cómo lo armé todo con Cloud Code y potencialmente cómo le podemos hacer integraciones con Nano Banana para ver cómo podríamos hacer un sinf de creativos próximamente. Antes de comenzar de lleno, déjame darte un poco de historia. Yo llevo bastante tiempo creando contenido y mandando tráfico hacia mi comunidad school, por lo que entiendo muy bien cómo funcionan los Metadals Manager y no estoy hypeando cuando digo que esto es una locura. Yo le pagaba $600 a mi paid media manager que era Cristóbal. Lo lamento, Cristóbal, pero después de esta actualización ya decidí seguir haciéndolo por mi cuenta, porque al final, por más crack que haya sido Cristóbal, nadie conocía mejor el negocio que yo. Entonces podía ir diciendo, "Oye, ya vamos haciendo esto, vamos mandando esto, que era básicamente lo que le iba diciendo a Cristóbal en gran parte, pero esta vez se refleja con cambios instantáneos. Entonces, esto es realmente una locura y la gente que lo sepa aprovechar bien va a compartir conmigo cuando digo que esto es un game changer, porque también meta con Pro manuso, pero solamente a un nivel de análisis, todavía no se puede hacer a un nivel de conversación lo que te voy a mostrar hoy día puede tomar acción a diferencia de lo que tiene Manus en su oente de Manus en sí. Así que vamos con la parte uno. Si tienes un negocio y usas Metads, tienes tres grandes formas de correr los Metaads. Uno, verlo a tú mismo. Dos, contratar a alguien para que los vea por ti. Y tres, tirar la plata a la basura, que es lo que la mayoría de la gente hace cuando aprieta el botón promocionar en ciertos lugares. Lo que construí es una nueva cuarta opción que creo que es la mejor, sinceramente, porque incluso cuando estás contratando a alguien, vas a seguir encima de él diciéndole los cambios que quieres hacer, solo si es que conoces lo que estás haciendo. lo que construí es un agente que habla directamente con el API de Meta. No es un dashboard de tercero, no es un SAS, es código real que está conectado a la API de meta. Y esto lo construí sin escribir una línea de código. Simplemente le hablas en español lo que quieres hacer y él ejecuta. Por ejemplo, si es que entro acá a VS Code, que es el terminal donde estoy corriendo las campañas y le digo, "Dime cosas que puedes hacer." Puedo decirle cosas como, ¿cómo va la campaña de Matías remarketing, cuánto gasté hoy día, monitoreo, gestión rápida, pausa el app de metaglases, sube el presupuesto a $ al día, cuáles son mis mejores ads, cuáles son los mejores países? No sé, hagamos una campaña dedicada de Black Friday, específicamente para las personas en España. No tengo idea, literalmente lo que queramos y podemos hacerlo en volumen. Entonces, podemos hacer crea esta misma campaña, pero personalízala para España, personalízala para Chile. Usa idioma chileno, ¿verdad? O Slang, en fin. Creo que se entiende un poco, ¿no? Esto no es una clase de marketing, esto es una clase o un tutorial de cómo puedes crear este sistema. Así que ya vamos un poco más de lleno. Lo que voy a hacer es voy a crear una nueva campaña específica para los países que le está yendo mejor. Entonces, voy a entrar acá y le voy a decir qué países son mis mejores países, es decir, los de menor CPA. Y aquí lo tenemos. Tenemos Estados Unidos con un CPA 45, Argentina, Chile, España, en fin, tenemos ya esto. Lo que vamos a hacer es personalizar una campaña para cada uno de estos países. Le pedí que me cree una campaña de retargeting con copies personalizados, ¿verdad? Una campaña que edite a nivel de campaña, pero con distintos adsets por país y que vaya modificando cada uno de los copies de estas campañas. Ya vamos a ver el resultado, pero por mientras te voy a mostrar cómo se setea. La verdad es que el seteo es bastante interesante y bastante sencillo dentro de la comunidad de Imperio Digital, de todos modos, donde puedes encontrar literalmente todo el paso a paso de lo que vamos a ver, la estructura que uso para el system prompt y mucho más. Vamos a entrar a developers.facebook.com. Vamos a entrar con nuestra cuenta de Arts Manager, nos vamos a ir a My Apps, aquí arriba a la derecha y vamos a darle a crear una app. Le vamos a poner aquí manejotads.com o le podemos poner el nombre que queramos. En verdad vamos a darle a todos los use cases posibles para que tenga la menor restricción posible. Si es que eres sensible con alguno de los scopes, puedes obviamente no incluirlos, pero esto es crear y manejar ads, ¿verdad? Medir las cosas. Estamos en un entorno relativamente seguro porque estamos en Cloud Code, no estamos en OpenCloud. Entonces, está bien. Y una vez que pongamos todos, todos, todos, le vamos a dar a siguiente. Vamos a conectar nuestro perfil y vamos a darle a siguiente. Paréntesis, si es que no has hecho la verificación de tu negocio, recomiendo que lo haga para que no esté limitado con la cantidad de cosas que podemos hacer, pero después le vamos a ir y vamos a ir a go to dashboard. Una vez que estemos acá, vamos a irnos a la parte que sale publish o publicar a la izquierda. Vamos a bajar y vas a ver que la opción de publicarla va a estar bloqueado. Esto es porque necesitas tener un Privacy Policy y un data delion policy. Entonces, vamos a abrirlos los dos en nuevas pestañas y vas a poner los links que te dejo publicados abajo. Y el Privacy Policy, delion policy puede sers simple si no es una aplicación que vas a hacer pública y la vas a usar a nivel personal. Yo igual te dejé publicado aquí dentro Imperio Digital el Privacy Policy, el data delion que cree. Los vas a pegar acá donde sale privacy policy URL y user data delion URL. Le agregas una imagen de literalmente lo que quieras. Para este caso, yo le puse la foto de perfil que tengo porque al final da igual, nadie más va a ver la app y le vas a dar a guardar. Ahora si es que volvemos a actualizar esto acá, vamos a ver que ahora sí tenemos la opción de publicar esto. Le vamos a dar a publicar abajo a la derecha y después nos vamos a ir a tools. Dentro de las tools vamos a ir a Craft App Explorer y vamos a seleccionar nuestro bot. Para este caso vamos a ir a manejothar, yo ya lo creé previamente, que se llama Matías el ad Manager y así es como lo van a encontrar también dentro del school y todas las cosas. Y vamos a poner get user access tokens. En los permissions, vamos a darle todos los permisos. Vamos a ir leer los ads, manejar los ads, manejar las páginas, los mensajes y mostrar las listas dentro de los otros permisos también. Manejar los catálogos, publicar videos e incluso le vamos a dar los de WhatsApp porque, ¿por qué no? Una vez que estemos acá, vamos a generar el access token. Vamos a darle a continuar. Vamos a darle acceso a las páginas, a los negocios, cuentas de WhatsApp y vamos a guardar. Vamos a poner got it y le vamos a dar generar access token estando acá. Vamos a generar el access token y vamos a copiar el token. Este token igual lo voy a eliminar después para cuando suba este video. Entonces no hay problema con que lo esté mostrando. Quiero mostrarles todo el proceso. Y nos vamos a ir a VS Code o cualquier lugar en el que estés corriendo. Cloud Code. VS Code es el que más me gusta a mí. Estando acá, necesitamos crear los archivos de Cloud MD, que es como el system prompt, por así decirlo, y empezar a crear nuestro proyecto. Aquí también te dejé publicado un prompt que es para hacerle un onehot. Ha publicado dentro Imperio Digital, pero también lo podéis copiar directamente acá. Lo único que le estamos diciendo es, eres la persona que está haciendo el ad manager para mi paid media. Básicamente aquí le voy a poner mi token, voy a hacerle control V, voy a pegarle el token que acabamos de hacer y le vamos a dar enviar. Y aquí va a empezar a setear literalmente todo. Y después de unos minutos, ni siquiera un minuto, 2 minutos, tenemos ya todo. Aquí tenemos las campañas, cómo está funcionando, está conectado acá, tenemos literalmente toda la información. Ahora, si llegamos y le decimos algo como, ¿cuáles fueron mis top performing ads en octubre? Darnos el recuento. Acá gastamos 7,000. Estos fueron los que nos convirtieron más, ¿verdad? Y aquí tenemos literalmente todos los datos. Y de hecho, si es que entramos aquí a las campañas nuevamente y vemos la campaña que le dijimos al principio con el remarketing, podemos abrirla y podemos ver qué nos creó para nuestro top cinco. Efectivamente, México, España, Chile, Argentina. Recordemos que también le pedimos que lo personalizara un poco. Entonces, veamos cómo nos personalizó Chile. Aquí tenemos los adsets. Veamos si es que le metió este toque de personalización. Y mira, aquí está. Comunidad que mola. Hostias, tío. no ocurre solo. Ay, ay, ay, la ¿Cómo le metió? ¿Qué estilo? Entonces aquí, mira, no sigáis solo. Después a España le metió, "No curres solo." Después aquí tenemos como no batalles solo, pero mantuvo el concepto, ¿verdad? Entonces al final está stop doing it alone, no sé, le está metiendo ahí a fondo, no más como que está bueno, está muy bueno. Al final creo que estamos pasando en esta personalización que este tipo de cosas son realmente claves, claves. Entonces, la verdad a mí me encantó. O sea, voy a decirle ahora, me encantó la campaña, pero activémosla con $5 diarios para para jugar no más porque sí, porque ¿por qué no? que ahí me creó ya la campaña de No curso con diario, que que honestamente me encanta, me encanta España. Tuve tuve el privilegio también de estar allá en septiembre del año pasado, septiembre, octubre, cuando fuimos al evento de automatizaciones de Waves. Realmente muy lindo, muy lindo. Nos quedamos ahí en Plaza Mayor. Realmente una maravilla, una maravilla España. De hecho, nos juntamos con un par de imperiales allá también que estuvo estuvo muy interesante también. Bueno, creo que ya entiendes un poco todo lo que se puede hacer acá. O sea, realmente te digo esto para la gente que lo sepa, aprovechar. Quizás este video no va a llegar a tanta gente, pero estoy seguro que a la gente que le llegue va a ser de altísimo valor, porque al final creo que que que estamos pasando una nueva economía de valor donde está subiendo la escalera de valor y estamos pudiendo dirigir todas estas cosas desde una simplea, ¿verdad?, una gente a nivel conversacional y antes teníamos que estar cambiando manualmente cada uno de los adsets y la gente que conoce eso sabe lo tortuoso que puede ser porque si fuera por mí, yo estaría haciendo cambios todo el día. Todo el día, literalmente estaría cambiando todo, probando cosas y se me ocurre un sinfín de ideas de cómo podemos mejorar este sistema. O sea, aquí simplemente hicimos la primera conexión. Ni te digo lo que se podría hacer si es que le conectamos a esto nano banana. O sea, si le conectamos a esto nanobanana, podemos generar un sistema que ataca el mayor dolor de todos los publicistas o todas las personas que generan publicidades en metads, que es el lack of creatives o es decir el shortage o el poco número de creativos que hay. Y podemos conectar la nano banana y decir, "Okay, générame 10 creativos de manera diaria. Vamos a probar distintos ángulos y sea arriesgado, sea igual, vamos a lanzar los 10 ángulos y todos los días vamos a ir midiendo las campañas de la semana anterior. Entonces vamos a crear 10 en estos días y vamos a correrlos por una semana y al cabo del día 7 quiero que elimines los peores nueve que le fueron y que dejes el primero y después el siguiente día vamos a hacer 10 más. Los vamos a testear por una semana y vamos a hacer nueve y así continuamente o podemos, no sé, probar 50 incluso y los corremos una semana y después volvemos a analizar y eliminar. O sea, al final las opciones son infinitas, infinitas, ¿ya? Y con nano banana podemos hacer muy buenas imágenes, también está conectado a la entonces podemos generar muy buenos cre, o sea, muy buenos textos o primary text al final. una barbaridad, o sea, como que la gente que la poca gente que le va a llegar este video, espero que realmente lo aprecie porque creo que es una de las bombas de valor más fuertes que he tirado en este último tiempo. Así que si te gustaría que haga ese video de cómo lo integro con Nano Banana para crear ads ilimitados, házmelo saber abajo en los comentarios, porque también creo que podría ser un video muy interesante. Coméntame, no sé, Matías parte dos o como queremos a Matías o algo así porque después reviso los comentarios y sé que si hay quórum y a la gente le gustó. Vamos a hacerlo ya. Déjame los comentarios abajo en el video de YouTube si estás en la comunidad de Imperio Digital donde estamos con todos los recursos, las sesiones en vivo, todas las cosas. También puedes hacer una publicación dentro de Imperio Digital comentándome porque a esa sí que estoy mucho más atento que al YouTube, aunque igual el YouTube lo voy revisando de manera periódica. Así que sin más que decir, espero que este video te haya servido y como yo no te conozco tan bien, pero YouTube sí, te recomiendo que veas este video que está acá que YouTube te está recomendando. Ya nos vemos.
