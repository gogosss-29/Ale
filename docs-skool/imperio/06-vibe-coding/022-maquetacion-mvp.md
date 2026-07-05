# 📝 Maquetación MVP

> Ruta: Vibe-Coding › 📝 Maquetación MVP

**🎬 Vídeo (28.6 min):** https://youtu.be/ftQs8rDs3B0

**📎 Recursos:**
- [GEM Generador de PRDs](https://gemini.google.com/gem/f3be5f5276c7)

---

## Parte IV. Mejores prácticas, metaprompting y maquetación del MVP

En esta lección vas a aprender la forma correcta de trabajar con Antigravity y agentes de IA para construir rápido sin hacer un desastre.  
Aquí definimos el método. Si entiendes esto, el resto del curso se vuelve 10 veces más fácil.

### Qué vamos a ver en esta lección

En este video cubrimos 3 cosas:

1. **Qué es metaprompting** y por qué importa en vibe coding.
2. **Qué es un PRD** y por qué es “la biblia” cuando trabajas con agentes.
3. Cómo usar **Google AI Studio** para maquetar el MVP de Automation Opportunity Finder y luego llevarlo a Antigravity con control de versiones en GitHub.

## 1. Qué es metaprompting

Metaprompting es un método para **refinar prompts usando IA**.  
En lugar de escribir un prompt a mano y esperar que funcione, le pides a la IA que:

1. Analice tu idea.
2. Identifique huecos o ambigüedades.
3. Y te genere el mejor prompt posible para construir el producto.

En este curso usamos metaprompting para transformar una idea general en un documento claro, usable y ejecutable.

## 2. Qué es un PRD y por qué lo necesitas

PRD significa **Product Requirements Document**.  
Es un documento que define el producto con claridad.

Un buen PRD incluye:

- Visión y objetivo.
- Problema que resuelve.
- Público objetivo.
- Funcionalidades.
- Restricciones.
- Criterios de aceptación.
- Prioridades.
- Métricas de éxito.
- Flujos de usuario.
- Tech stack.

En vibe coding el PRD no es “algo bonito”.  
Es literalmente la referencia principal para que el agente no invente cosas.  
Mientras más claro el PRD, mejores resultados obtienes.

## 3. Mejores prácticas para vibe coding (y para Antigravity)

Estas son las reglas que seguimos en el curso:

### Regla 1. Trabaja por “features”, no por “hazme toda la app”

Nunca le digas a un agente: “*hazme toda la aplicación*”.  
Divide el proyecto en piezas.

Ejemplos de features del Automation Opportunity Finder:

- Autenticación con Supabase.
- Dashboard con métricas.
- Wizard para crear diagnóstico.
- Pantalla de resultados.
- Módulo de clientes.
- Cotizaciones.
- Seguimientos.

Cada feature es una tarea.  
Así controlas calidad, velocidad y errores.

### Regla 2. Maneja el trabajo como un equipo de desarrollo real

Aunque sea IA, funciona igual que un equipo.

- Un agente puede trabajar en un feature.
- Otro agente puede corregir un bug.
- Otro puede hacer refactor.

No metas todo en una sola conversación interminable.  
Usa ciclos cortos, objetivos claros y revisa cambios.

### Regla 3. Primer prompt en Antigravity: “analiza el proyecto”

Cuando arrancas, lo primero que debes pedirle al agente es:

- Que analice el proyecto completo.
- Que lea carpetas y archivos.
- Que entienda el stack.
- Que te pregunte lo que falta.

No le pidas cambios antes de que entienda el sistema.

### Regla 4. Especifica el objetivo y limita el alcance

En cada tarea, define:

- Qué quieres lograr.
- Qué archivos puede tocar.
- Qué NO debe cambiar.

Deja que proponga cambios.  
Tú revisas el diff.  
Aceptas o corriges.  
Y sigues.

### Regla 5. Usa guías internas cuando escales

Antigravity permite reglas, archivos markdown y guías internas para que el agente:

- Siga lineamientos de autenticación.
- Respete estilo de UI.
- No rompa estructura.
- Mantenga calidad.

En el MVP no nos vamos a meter profundo en eso, pero sí vas a entender la idea para cuando subas de nivel.

## 4. Maquetación del MVP en Google AI Studio

En este video hacemos lo siguiente:

1. Partimos de la idea del producto.
2. [La pasamos por el “gem” que genera el PRD para vibe coding.](https://gemini.google.com/gem/f3be5f5276c7)
3. Revisamos el PRD y corregimos lo que no nos gusta.
4. Copiamos el PRD a Google AI Studio para que nos genere la app base.

Importante.  
En esta etapa, el objetivo NO es que todo funcione perfecto.  
El objetivo es definir:

- UI/UX.
- Estructura del proyecto.
- Rutas y pantallas.
- Componentes principales.

La funcionalidad real la terminamos en Antigravity.

## 5. Ajustes que hacemos después de la primera maqueta

Después de generar la primera versión, hacemos iteraciones rápidas, por ejemplo:

- Cambiar toda la interfaz a español.
- Ajustar el tech stack mostrado dentro de la app.
- Validar formularios. Ejemplo: no avanzar sin nombre.
- Crear una pantalla real de settings con dark mode y light mode.
- Mejorar el flujo de diagnóstico.

También revisamos un detalle importante:  
Si agregamos input de audio, debe haber confirmación clara de que:

- Se guardó.
- Se analizó.
- Y se refleja en el resumen del diagnóstico.

## 6. Control de versiones con GitHub (lo mínimo que debes hacer)

En este video también te muestro el flujo básico:

- Conectar repo a GitHub.
- Hacer commits por cambios.
- Revisar historial.
- Ver diferencias entre commits.

No vamos a profundizar en Git.  
Pero sí quiero que lo uses, porque sin versionado te vas a disparar en el pie.

### Resultado esperado al terminar esta página

Al finalizar esta lección debes tener:

- Un PRD usable para el MVP.
- Una primera versión maquetada en Google AI Studio.
- El proyecto guardado y versionado en GitHub.
- Claridad total de cómo trabajar por features y ciclos cortos.
- Una app base lista para continuar el desarrollo en Antigravity.

### Errores comunes

- Pedirle al agente “haz toda la app”.
- No tener PRD. Resultado: el agente inventa.
- No trabajar por features.
- No revisar cambios antes de aceptar.
- No usar commits. Luego no puedes volver atrás.
- Confundir maqueta con app funcional. La maqueta es solo el inicio.

## 🎙️ Transcripción

Okay, entonces en este video vamos a hablar de las mejores prácticas, tips y metaprompting. Vamos a ver qué es, cuáles son las mejores prácticas para el B coding, no únicamente para antigravity. Y nos vamos a meter en Google Studio y ya vamos a empezar a maquetar nuestro eh nuestra aplicación. Okay. Antes que nada, ¿qué es metaprompting? Okay, metaprompting es un método en el cual vamos a refinar o analizar otros prompts. Un metapromp básicamente le pide a la IA que cree el mejor promp posible para una tarea determinada o que mejore un existente. En este caso, nosotros tenemos que partir de una idea de nuestra aplicación. Esa idea podemos utilizar eh si ya tienes un algún custom GPT. Hay varios que puedes encontrar como para pelotear o o poder eh hacer un brainstorming, digamos, una idea. Ya que logras aterrizar un poquito esa idea, vas a usar el gem que te voy a dejar aquí abajo. Si quieres utilizarlo, si ya tienes tú algo, lo puedes usar para refinar ese prom, para generar un metapromp que va a ser a la vez el PRD. ¿Okay? ¿Qué es un PRD? Lo hablamos en videos anteriores, pero PRD significa productirements document. Básicamente, como lo dice su nombre, es un documento que describe la visión, problemas resolver, público objetivo, funcionalidades, criterios de aceptación y restricciones de un producto o una future. ¿Okay? suele iniciar como eh perdón, suele incluir secciones como visión objetivo, user stories, que es muy importante, que es una user story. Básicamente le dices, "En mi aplicación el usuario una vez que inicie sesión va a ir a la pantalla de inicio donde va a poder acceder a con solo dos clicks o dos tabs de distancia a en la opción de poder hacer un uprate al siguiente nivel." Eso es un user story donde escribes quién, cómo y qué va a hacer. ¿Okay? Eh, son también requistos funcionales, requistitos no funcionales, rendimiento, seguridad, plataformas, prioridades, métrica de éxito, flujos de usuario, textac que vamos a utilizar para autenticación, base de datos, front, APIs, todo. Y en entorno específicamente de vibe coding, donde usamos agentes de IA o como se le conoce como codeps, codesarrolladores, el PRD básicamente es la Biblia, se convierte en la fuente principal, es donde la gente va a ir a consultar qué es lo que tiene que hacer en todo momento y es básicamente es lo que lo alimenta. Entonces, mientras más claro y más definido desde un inicio, más estructurado va a ser mucho mejor, como hablamos en el video anterior. ¿Okay? Ahora, tips en general. Vamos a formular ya con el agente en Antigravity. Vamos a formular pequeñas tareas en en el agent manager. Vamos a enfocarnos por futures. No le vamos a decir, "Hazme toda esta app." Una porque ya vamos a llegar con la app maquetada desde Google Studio y dos porque la gente tiene es más fácil queini. Entonces imagínese tu future como cada una de las características que va a tener tu app. Si nosotros estamos hablando que en este caso nuestra app se va a llamar ah o va a ser un automation Opportunity Finder, que básicamente es un app que vamos a crear para todos los freelancers, dueños, agencias para que puedan entender un poco cómo funciona los negocios y encontrar esas oportunidades de automatización o de ofrecerle servicios de guía. Entonces, a lo mejor eh lo podemos dividir en diferentes secciones y a lo mejor vamos a tener un futur, va a ser un login registro que puedas crear usuarios antieticados y le vamos a decir que utilice su pavase. Ese es un future. Mandas un agente a hacer eso y vamos a tener un dashbo donde vamos a tener el resumen general, número de diagnósticos creados, clientes, condiciones activas, etcéteras. Eso es otro future. Vamos a poder crear un diagnóstico. Vamos a tener como un wiz, va a ser como el paso a paso para crear un diagnóstico. Ese es otro future. Y a lo mejor una vez que terminemos nos dio error el out. Entonces eso se le llama como un book. Entonces, le vamos a decir a la gente, ve y revisa este book de out, me está dando este error. Le podemos pasar el código de error, como vimos el video pasado también una captura de pantalla y dejamos que cada gente trabaje en ese future, en ese book, en esa refactorización, en lugar de que le digamos, revísame esto, revísame esto, revísame esto, porque así no así no funciona. que ya tiene posibilidad de trabajar con desarrayadores. Hay cosas que que se llaman dentro del break management, eh, o también hay sprints y todo eso lo dividen por alcances y digamos que cada desarrollador o o un desarrollador puede tener varios alcances, pero sabe que su alcance es hasta aquí, voy a trabajar con ese voy a esto. Entonces es lo mismo. Por más que sea la IA y es muy poderosa, manéjenlo por futures, books, refactorizaciones. Acuérdense que este es un eh agent manager, como lo dice ahí el nombre. Entonces puede manejar diferentes agentes. Asínenle a los agentes esas subtareas y no que un agente haga absolutamente todo. Otra cosa, cuando inicien su ah el desarrollo, la continuación del desarrollo de la aplicación en Antigravity, porque lo vamos a maquetar en Studio, lo primero que yo les sugiero es que le den un prompt, que lo vamos a ver, se los voy a dejar aquí abajo. Solo voy a dejar un poquito más técnico, pero va a ser algo así como que, okay, aquí tienes un proyecto, no le digan de qué se trata porque la idea es que de tengan un buen ritm file y un PRD. Aquí tienes este proyecto. Necesito que vayas, analices, leas todas las carpetas, entiendas qué es lo que hace sus funcionalidades del textac y me preguntes lo que no te digo quedó claro y lo dejas que se vaya y que se ponga a trabajar en en todo eso. Eh, tienes una de dos, utilizar el modelo pro para eso se va a tardar un poquito más, pero va a regresar mucho mejor. o el fast para esa lo que es la la planeación, no la planeación, sino todo ese pensamiento y entender un poco más el sistema, ¿okay? Trabaja en ciclos, especifica el objetivo de la tarea y los archivos que puede editar. Deja que la gente proponga cambios y tú simplemente ves revisando las diferencias, ve aceptándolo de inmediato y ve trabajando con lo siguiente. Escribe generación, eh, escribe guías de generación de contenido, rule guides. Aquí es algo que nos vamos a meter muy poco en esto porque ya es mucho más técnico, pero antigravity así como otros este idonía te permite tener skills y te permite tener tus markdown files, tus archivos markdown donde le vas a decir, "Okay, cuando vayas a hacer un future necesito que vayas y que revises este archivo que que tenemos para testing y vas a utilizar este MSP, vas a utilizar este framework para realizar el test, vas a comprobar cuando tengas tengas que hacer un ritmi o cuando tengas que escribir documentación, vas a seguir estos lineamientos. Cuando necesites crear autentificaciones, asegúrate que sigas esos lineamientos y eso ya es para llevarlo a un nivel técnico mucho más alto. En este caso tenemos un poquito incluido en el en el GEM que le estoy dejando en el GEM del del PRD, pero no lo vamos a ver muy a detalle porque eso ya brinca un poquito más técnico. A lo mejor lo veremos en alguna segunda etapa o una continuación. Okay. Entonces, ¿qué sería lo primero? Lo primero tendríamos que irnos a nuestro ah GE, a nuestro GEM, que les voy a dejar el link aquí abajo. Es un CG, ya tiene un unos settings, información y un contexto y todo ya está entrenado, digamos. Y voy a pasarle. Yo tengo en mi otra ventana, como ya les platiqué, eso no lo vamos a ver porque eso ya ustedes tienen que chatear o hablar su idea con la poder aterrizarla, tener un poquito más de idea lo que vamos a hacer. Entonces yo ya lo tengo aquí en otra ventana, lo voy a copiar y se lo voy a pegar aquí a mi eh generador de PRDs para BCOM. Lo voy a leer un poquito para que lo vean. Dice básicamente idea final de la app. No quiero una app llamada automation Opportunity Finder. La app sirve para que freelancer y agencias de automatización diagnostiquen negocios, detecten oportunidades de automatización con IA y generen recomendaciones, precios y siguientes pasos para vender servicios. La pues es para uso interno para clientes debe ser rápida, clara y etcétera, ¿no? Con todas las páginas, lo que se tiene que hacer, qué se puede hacer, qué no puede hacer, etcétera. Y hasta aquí abajo le voy a decir, necesito que utilices la imagen adjunta como inspiración para el UI, el user interface. Y como habíamos hablado, nos vamos a ir a Del. Okay. Y aquí yo voy a buscar, no sé, dashboards o puedo buscar eh product design. Ah, bueno, vamos a iniciar sesión por aquí para que no tengamos ningún problema. No hay que pagar nada, simplemente te piden que estés iniciar sesión en México. Continuar skip product design. Y aquí van a ver más o menos algo que les guste. Les gusta un poco más de negro, les gusta más en blanco. Yo en lo personal soy más como de tonos negros, morados y así. Este me gusta, pero lo veo como un poquito saturado. Vamos a ver otras opciones. Es muy parecido. Más tenemos a ver. Tampoco no nos dice mucho. Es como para una landing. Ya nos estamos saliendo un poquito. Vámonos para atrás y vamos a buscar dashboards y vamos a ver qué opciones tenemos. Bueno, hm, ese sí no me gusta. Entonces, voy a tomar una captura de pantalla y se lo voy a dar a mi este y lo voy a mandar. Vamos a dejar que trabaje, que nos genere todo y les voy a pausar para que no se haga muy largo el video. Okay, ya terminó. Me dice pierdut automation finder, MVP, ex summary, mobile first. Es importante el mi text, cuál es la tecnología, el text que va a estar utilizando para ir a base de datos, etcétera. Eh, ¿qué más tenemos aquí? Y de hecho nos dijo 1.5 flash y 3 para portadas de reporte. Ahorita se la vamos a cambiar, no estoy de acuerdo con eso. Y wizard diagnóstico inteligente. Los esos son los user stories son los shooters, etcétera. Okay, creo que está bastante bien en general, aunque hay algunas cosas que no me gustaron mucho, eh, pero ahorita las cambiamos. Entonces, ya que tenemos esto, lo vamos a copiar. Vámonos a nuestro Google Studio y vamos a generar una app. Vamos a dejar el TScript React Flash Pro preview. Le voy a dar todo esto y hasta aquí abajo vamos a cambiar lo que habíamos dicho y ustedes pueden decir qué quieren utilizar. Yo aquí en este caso les voy a les voy a decir que con 2.5 flash y nano banana pro. Okay. Y abajo voy a poner te dejo un diseño que vi y me gustó para que lo tomes como lineamiento. en cuenta que no tienes que desarrollar todos los futures completos. Necesitamos enfocarnos en la estructura del proyecto y en la norma y en el texta mejor te que vamos a utilizar todo debe ir document entado con sus objetivos entes, así como necesito un maestro que sea el rode todas las funciones de su base toma nota. Pero no las lleves a el objetivo de esta primera iteración es definir el UI adecuado, así como la estructura del proyecto. Crea todas las carpetas y los archivos necesarios. Pasarle build. Okay. Y aquí sí le voy a poner pausa. Vamos a dejarlo que trabaje. Y okay, me acabo de dar cuenta que no le había mandado y me di cuenta que no le había dado eh no le mandé la imagen que le había que le había pedido. Entonces vamos a hacerlo de nuevo. Vamos a volverle a pasar la la imagen y digo, vamos a volver a dar los comandos. Le damos esto y le pasamos los comandos otr dicho. Y importante pasarle la imagen que nos gustan. Okay, vemos que ya terminó. Así quedó más o menos la interfaz. Vemos que sí es muy parecida a lo que habíamos visto y tenemos el diagnóstico, la industria más o menos texta, slack. Entonces, lo podemos cambiar a nuestro gusto. Painpints data entry error. Vamos a meter una de contexto. Generamos reporte. Vamos a agregar una cotización, no funcionar las cotiziones todavía. Y si nos vamos al dashboard y podemos ver en qué etapa están. Un quick scan nos manda para acá. settings no tenemos nada porque no lo hemos pedido. Okay, creo que con esto es suficiente para irnos a antigravity, así que vamos a hacer algo. Vamos a No necesitas guardar una copia. Vamos a conectar la git. Vamos a llamarle así nada más con el prompt. Le damos save, le damos acceso a GitHub, le damos instalar autorizar. Pide que verifique el correo. Me voy a ir a mi correo y me tiene que llegar el código de verificación. de este expira cuando ustedes lo vieron ya va a estar expirado. Vamos a regresar. Se error intelectuar empezar los permisos. Vamos a volver a darle y aquí repositores save que ya está. Entonces sí lo hizo, pero me de un error. Vamos a actualizar micrófono. Aquí podemos ver el código, todas las carpetas, todo lo que hizo. Aquí tenemos eh prd.md, como les dije, le pedí que me lo generara, etcétera. Vamos a de vuelta preview. Okay. ¿Cómo le vamos a llamar? Ah, habíamos dicho que se iba a llamar habionity. Y vamos a parle de demo para imperio digital. Y en este caso lo voy a dejar público porque si lo quieren hacer, clonarlo y hacer lo que quieran. Vamos a darle. Okay, vamos a darle es todo lo que va a agregar porque no habí nada y vamos a darle el stage commit y listo. Y vamos a hacer un pequeño cambio. Se aquí sugiere como que qué cosas se pueden hacer. Vamos a hacer un pequeño cambio. Voy a decirle, "Okay, me pareció muy bien todo, pero sé que te di las algunas instrucciones en inglés, pero toda la interface tiene que estar en español. También necesito que cambies el textack por las plataformas que normalmente uso yo, eh, las cuales te las voy a listar a continuación." ¿Okay? Entonces vamos a decirles, porque si se acuerdan en diagnóstico no salía todo esto, ¿no? Entonces yo quiero decirle que sea GHL NHN make a table table WhatsApp. ¿Y qué más utilizamos? WordPress. Se me ocurre algo. Además, quiero que haya una función de que yo pueda agregar algún text en la segunda pantalla del diagnóstico y también me di cuenta que en la primera pantalla del diagnóstico me deja continuar, aunque no haya puesto ningún nombre. Quiero que por favor pongas ahí eh una restricción de que te pida un nombre para poder continuar y me di cuenta que settings no te lleva a ningún lado. Sé que no hemos definido settings, pero por favor agrega que settings me lleve a otra ventana de settings y en esa ventana lo único que vas a poner por ahora es cambiar entre dark y light mode. Listo. Vamos a darle enviar y le voy a volver a poner pausa. Okay, aquí vemos cómo está trabajando, va aplicando todos los cambios, idiomas y datos, navegación y configuración, user de diagnóstico, validación y lo el custom eh tags, ah nuevas vistas, estilos globales y aquí vamos lo que va cambiando y lo quise hacer en dos partes para que vean por qué está muy bueno GitHub y cómo funciona o qué es un commit. Fant ha un cambio al código, porque todo está haciendo cambios al código, puedes mandar hacer commits básicamente decirle, hice este cambio o guárdalo. Hice este cambio y guárdalo. Y cada vez que haces un comit, tú puedes poner una nota de qué estás haciendo, qué estás cambiando, ¿no? Entonces ahorita no nos vamos a meter muy a fondo a explicar qué es GitHub y qué es el control de versiones, pero es muy importante. Yo les recomiendo que lo investiguen. Por su cuenta hay muchos cursos en internet de cómo utilizar YouTube o por lo menos las partes básicas. Vamos a esperar más a que termine y nos movemos. Okay, vemos que ya no los puso en español. Reportes, diagnóstico. Vamos a darle. Okay. Por favor, el nombre. Entonces, si nos hizo ese cambio, continuar la industria, no se lo pedimos, pero está perfecto. Y aquí a mí se dic otro. Vamos a poner trelo. Es una buena. Muy bien. Sí, me gusta. Pasa un acepta el audio. Esta empresa tiene problemas, ya que tiene que procesar manualmente todos los días 50 facturas promedio que recibe de sus proveedores y tiene que subirlas todas a un spreadshe para que sean revisadas por contabilidad para después cargarlas a Quickwoods. Okay. Por ejemplo, esto no me gustó. No sé si se guardó, no sé si no se guardó. Entonces tenemos que que verificar eso. Okay, vamos a poner Perfecto. Gracias por los cambios. Estoy revisando cuando creamos una propuesta nueva. Ya vi que hiciste los cambios de que no acepte el nombre, la industria y que podamos agregar textac, pero al final cuando describes un poquito el problema, ya ves que hay una opción de agregar un audio. Eh, me parece increíble esa opción, pero necesito una confirmación de que después de que terminé de grabar sí se guardó efectivamente el audio. Y cuando me voy a mi siguiente ventana ya de análisis, quiero asegurarme de que si se haya analizado el audio de que yo mandé y que no solamente tengas como que Domata. Asegúrate que haya conexión hacia Yemini, que analice el audio, analice la información y aparte quiero ver en la parte de abajo, entre el gráfico de proyección de costos y acciones recomendadas, pon un resumen del problema en base a todo lo que te mandé y el audio para yo ver efectivamente que está siendo contemplado. Okay, me dio horror. Como pueden ver, estoy utilizando una aplicación que se llama Whisper Flow, así que denme un segundo, voy a traerla y regreso. Listo. Lo traje para acá y vamos a mandar otra vez. Te voy a poner pausa para mantener los videos bastante cortos. Regresamos ahorita que termine. Okay, me muestra que ya terminó. Vamos a probar antes lo de configuración que dije. Okay, perfecto. Vámonos a nuevo diagnóstico. Vamos a ponerle perioital, la industria s tecnología. hacer esto y vamos a decir que también utilizamos sheets. Lo agregamos continuar puntos de dolor. Respuesta reportes manuales. Voy a poner rato ni siquiera estaba funcionando porque no me pedía esto, nada más era un place folder visual. Okay. Uno de los mayores puntos de dolor de este cliente es el procesar datos hacia Google Sheets. Recibe más o menos 50 facturas al día, las cuales las tiene que procesar, extraer los datos y subir a Google Sheets. Audio guardado. Generar reporte. Analizando oportunidad. Okay, como pueden ver, ahorita está tardando más. Entonces, evidentemente antes tenía Domy data, no estaba haciendo nada, lo cual no está mal porque pues al final esto es un MVP y estamos haciendo ahorita la maquetación. Se sufre insistencia críticas personas en facturas. Okay, básic. Okay, efectivamente lo está leyendo, ¿no? Pues obviamente dentro de las acciones recomendades automación de proces de procesamiento de facturas, perdón, sincronización de datos entre vertical Google Sheets generación automáticos de reportes mensuales. Vamos a decir que queremos agregar las tres. Obviamente no está haciendo nada, no funciona la parte de agregar. Vamos a dejarlo aquí en Google Studio. Creo que esto ya está bien si lo continuamos en eh, ¿cómo se llama? antigravity. Entonces, antes de terminar este video, vamos a hacer un segundo comit. Vamos a guardar en GitHub. Y aquí te me dice, "Okay, ¿qué fue lo que cambió?" Le voy a decir, pasamos a español y nos aseguramos de que funcione la grabación de audio y el análisis con stage commit. Ya nada más por último, ¿cómo confirmamos? Vámonos a nuestro githop. Home tiene que aparecer ahorita el repositorio. Aquí está automation opportunity finder. Aquí vemos todos los documentos y lo que Google Studio, por si sale esto. Y aquí arriba donde dice tres commits vemos que es el commit original, el inicial commit, luego este cambio y luego ya lo que puse lo que yo puse ahorita pasamos español, aseguramos de que funcionen las grabaciones. ¿Y cuál es el código del commito? podemos ver el detalle tal cual te va a mostrar todos los cambios que se están haciendo en el COVID. Okay, entonces vamos para aquí este video y nos vamos en la siguientección. M.
