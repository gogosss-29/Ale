# Instala Claude Code (automatiza en n8n)

> Ruta: Automatizaciones n8n › Instala Claude Code (automatiza en n8n)

**🎬 Vídeo (18.4 min):** https://www.youtube.com/watch?v=Ivn4rX2wfxk

---

**¿40 minutos armando un workflow? Eso era antes.**

Pasé 2 años dominando n8n, nodo por nodo, workflow por workflow. Hasta que llegó Claude Code y cambió todo el juego.

En este video te muestro cómo crear workflows complejos de n8n en minutos, usando un agente de IA que entiende lo que quieres hacer y lo implementa directamente en tu instancia de n8n.

---

## 🎯 Lo que vas a aprender

✅ **Setup completo desde cero** - VS Code + Claude Code + MCP servers  
✅ **Crear tu agente personalizado "Claudio"** - Tu asistente de n8n 24/7  
✅ **Conectar Claude Code a tu instancia de n8n** - API keys y configuración  
✅ **Demo en vivo** - Workflow de newsletter con IA que se ejecuta solo  
✅ **Modificar workflows con lenguaje natural** - Sin tocar un solo nodo

---

## ⏱️ Timestamps del video

- **0:00** - Intro: 40 minutos vs 5 minutos
- **2:35** - ¿Qué son los MCP y cómo funcionan?
- **4:12** - Setup completo: VS Code + Claude Code + n8n
- **10:46** - Conectar tu instancia de n8n
- **12:48** - Demo en vivo: crear workflow con IA

---

## 🔧 Recursos necesarios

### Herramientas principales:

- [Claude Code](https://claude.com/claude-code) - Necesitas plan Pro o Max
- [n8n](https://n8n.io) - Tu plataforma de automatización
- [Visual Studio Code](https://code.visualstudio.com) - Editor gratuito

### Repositorios de superpoderes:

- [n8n MCP](https://github.com/lvisb/n8n-mcp) - Conexión a n8n
- [n8n Skills](https://github.com/lvisb/n8n-skills) - Buenas prácticas y patrones

---

## ✅ Checklist: Tu primer agente de n8n

Sigue estos pasos después de ver el video:

### 1. Preparación (5 min)

- Descargar e instalar Visual Studio Code
- Verificar que tienes plan Pro o Max de Claude
- Tener tu instancia de n8n lista

### 2. Instalación (10 min)

- Instalar extensión de Claude Code en VS Code
- Crear carpeta para tu agente (ej: "n8n-workflow-builder")
- Configurar permisos en Settings (allow dangerously skip permissions)

### 3. Crear tu agente "Claudio" (15 min)

- Abrir Claude Code en VS Code
- Darle instrucciones de quién es y qué hace
- Instalar repositorio n8n MCP desde GitHub
- Instalar repositorio n8n Skills desde GitHub
- Verificar que creó el archivo [claude.md](http://claude.md)

### 4. Conectar a n8n (5 min)

- Ir a tu instancia de n8n → Settings → API
- Crear nueva API Key (copia y guarda)
- Copiar tu n8n URL desde "Connection Details"
- Pegar ambas credenciales en Claude Code
- Confirmar conexión exitosa

### 5. Primera prueba (10 min)

- Pedirle a Claude que liste tus workflows existentes
- Crear un workflow simple de prueba
- Modificar algo con lenguaje natural
- Verificar que los cambios aparecen en n8n

**Total: ~45 minutos para tener tu agente funcionando para siempre** ⚡

---

## 💡 Ideas de workflows para probar

Una vez que tengas tu agente configurado, prueba con estos:

1. **Newsletter automatizado** (como en el video) - Investiga noticias semanalmente
- Genera resumen con IA
- Envía por email
2. **Monitor de competencia** - Scrapea sitios web
- Detecta cambios de precio
- Notifica por Slack/Telegram
3. **Content pipeline** - Genera ideas de contenido
- Crea drafts con IA
- Publica en múltiples plataformas
4. **CRM automation** - Captura leads desde formularios
- Enriquece datos con Apollo/Hunter
- Crea páginas en Notion automáticamente

---

## 🚀 Próximos pasos

**Si lograste configurarlo:**

- Comparte tu primer workflow en los comentarios 👇
- ¿Qué automatización creaste?
- ¿Cuánto tiempo te ahorró vs hacerlo manual?

**Si te trabaste en algún paso:**

- Publica tu pregunta aquí en la comunidad
- Incluye screenshots del error
- La comunidad te ayuda (y yo también)

**Próximo video de la serie:** Cómo combinar n8n visual con Claude Code para crear workflows híbridos aún más potentes. Si quieres que lo haga, déjamelo saber en los comentarios del video.

---

## ❓ FAQ rápido

**P: ¿Necesito saber programar?** R: No. Claude Code programa por ti. Solo necesitas describir lo que quieres.

**P: ¿Funciona con n8n cloud o solo self-hosted?** R: Funciona con ambos, solo necesitas la API key.

**P: ¿Cuánto cuesta Claude Code?** R: Viene incluido en los planes Pro ($20/mes) y Max ($200/mes) de Claude.

**P: ¿Puedo usar esto con Make o Zapier?** R: Por ahora solo hay MCP para n8n. Make y Zapier no tienen soporte oficial.

**P: ¿Es seguro darle acceso a mi n8n?** R: Sí, tú controlas los permisos de la API key y puedes revocarla cuando quieras.

## 🎙️ Transcripción

Hace un tiempo armé una automatización en la cual me demoré 40 minutos donde escrapeaba, buscaba una lista de clientes y conseguía sus correos electrónico, le redactaba un mensaje personalizado basado en sus intereses, su industria, etcétera, y les mandaba una propuesta directamente. Todo esto, como puedes ver acá, me tomó 40 minutos de armar. Hoy día puedo entrar a la Iadr Tropic Cloud Code y puedo decirle entra mi N8N crea una nueva instancia en la cual prospectamos list enio. Crea un workflow directamente en N8N para automatizar un sistema de prospección en frío. Outbound. La lógica del flujo es la siguiente. Extrae los leads. Usa Apolo para buscar la lista de contactos en una industria específica. Extrae el nombre, correo electrónico y datos de la empresa. Agente IA, el cerebro, Open Router, modelo Geminite 3. Redacta un correo persuasivo y altamente personalizado ofreciendo nuestros servicios. Genera un texto breve para una propuesta comercial a medida. genera un documento y envía el correo con el nodo Gmail. Cloud empieza a trabajar, investiga el nodo Apolo, busca la documentación, diseña el workflow completo y lo más importante lo implementó en nuestro o nuestra instancia de N8N. Mira, ahora de hecho, si es que entramos acá y actualizamos, vamos a ver que tenemos acá el sistema de prospección en frío con no solamente la plantilla funcionando en sí, sino que también las cosas que tenemos que cambiar y lo que tenemos que modificar. Yo no toqué absolutamente nada. Esto lo voy a ordenar para que se vea bien. No toqué absolutamente nada. Simplemente le puse el prompt que te acabo de mostrar. Aquí tenemos las cosas que tenemos que cambiar. Por ejemplo, la API K de Apolo, Open Router. Simplemente le conectamos nuestras credenciales y listo. Y aquí tenemos todo. La prospección, la configuración, buscar los leads, procesar cada lead, extraer los datos y después empezar a generar los correos. Pero combina los datos, genera el PDF y después le envía el correo. Aquí simplemente tendríamos que conectar nuestra cuenta. Hay un par de cosas que cambiaría, sí, probablemente este prom de acá para hacer los correos más simples, ¿verdad? Este de acá y en fin, pero mira, por ejemplo, acá ya tenemos toda la estructura funcionando y lo que me demoré antes, 45 minutos en armar aquí, lo generé simplemente en un par de minutos. A menudo te vas a encontrar con este tipo de errores. Cuando en N8N entra algo por arriba y sale por abajo significa que no funciona o que el nodo no está actualizado. Pero aquí simplemente le diría, "Tengo este error." Arréglalo. Y va a entrar Cloud Code a nuestra instancia N8N. Va a entrar a esta automatización en específico y la va a empezar a modificar. Ahora simplemente seguimos estas instrucciones que aparecen acá y tenemos la automatización funcionando y corriendo. Es realmente una barbaridad. Pero, ¿por qué podemos hacer todo esto? Bueno, porque tenemos la maravilla de los MCP. MSCP es la llave internacional que se creó, de hecho, del mismo Antropic, que se creó para estandarizar todos los inputs de las herramientas. Se llama Model Context Protocol y nos permite acceder y conectar distintas aplicaciones entre sí, conectar los servidores y permitir que se comuniquen entre ellos. En este caso conectamos Cloud Code directamente a N8N. ¿Y qué le permitimos hacer? Bueno, ejecutar workflows, editar workflows, eliminar workflows, mover workflows y también crear nuevos workflows. Entonces, es muy bueno para diagnosticar qué es lo que está ocurriendo. Si estás viendo todo esto y es una interfaz completamente nueva, no te preocupes porque voy a cubrir absolutamente todo desde cero. Quiero comenzar diciendo que para instalar Cloud Code necesitas tener alguno de los planes Pro o Max que directamente incluya el cloud code. ¿Y cuál es la diferencia estar usando Cloud Code versus estar usando Cloud en la plataforma? Bueno, que el Cloud Code es un agente que permite ejecutar acciones dentro de tu computador, bajo un ambiente controlado, claramente. Entonces, puede ejecutar distintas acciones, descargar repositorios si le pides, puede ejecutar acciones en el terminal, entonces realmente pasa a tener más control sobre las decisiones que estás tomando y puedes empezar a crear este tipo de agentes. Para este caso vamos a conectarlo a N8N para que nos cree las automatizaciones. Esto es una genialidad porque yo llevo enseñando mucho tiempo N8N y este es el fast track o el camino rápido para las automatizaciones. ¿Okay? ¿Qué es esta plataforma que estás viendo acá? Bueno, esta plataforma es BS Code o Visual Studio Code. ¿Okay? Cuando te la descargues vas a entrar acá, vas a ir a Visual Studio Download y te vas a descargar Visual Studio Code. Cuando se te abra, se te va a abrir algo así. Lo primero que tienes que hacer es instalar Cloud Code dentro de Visual Studio. ¿Cómo hacemos eso? nos vamos a ir acá al costado, vamos a buscar la extensión de Cloud Code. Vamos a irnos acá y le vamos a dar a instalar. Okay. Cuando le demos a instalar se nos va a abrir algo AS. Ya lo tenemos instalado. Genial. Y ahora vamos a empezar a crear nuestro agente de cloud code. Nota esto lo vas a tener que hacer solamente una vez y va a quedar habilitado para siempre. Ya nos vamos a ir acá y vamos a crear una nueva carpeta. Para este caso le voy a poner N8N workflow builder y le voy a poner Roberto. Okay, para poder acordarme mejor. Entonces, aquí estamos creando a Roberto, ¿no? Pues deberíamos haberle puesto Claudio porque es Cloud Code Claudio. Bueno, muy tarde. Ya quedó como Roberto. Será muy tarde para cambiarlo. Claudio. Ahora sí que sí, cuando entremos nos vamos a encontrar con algo así. Cuando apretamos esta pestañita de acá, se nos va a abrir Cloud Code. Pero antes, ¿qué es lo que estamos viendo? A la izquierda vas a encontrar los archivos o el folder, tal cual como lo encontrarías en tu computador. A la izquierda va a ser esto. Y si es que yo creo un nuevo archivo acá, por ejemplo, una nueva carpeta que se va a llamar carpeta uno, vamos a ver que se va a ver reflejado acá lo mismo con todos los archivos que vayamos creando. ¿Okay? Este entorno de acá es bueno el entorno principal donde cada uno de los archivos se va a ir creando. Por ejemplo, supongamos que creo acá un archivo que se llama archivo 1.md y aquí empezamos a escribir ciertas cosas. Ya, aquí vamos a tener el archivo 1 MD, que si lo visualizamos es el archivo que acabamos de crear. Entonces, ¿qué es lo que es Visual Studio Code? Es una manera más amigable de ver tu escritorio o tu folder si estás en Mac. Ya voy a eliminar el archivo y lo voy a mover. Y si es que lo elimino de acá, lógicamente se elimina de acá. No es nada más que eso, una manera más simple de visualizar los archivos, pero esto tiene superpereres. Por lo mismo lo que voy a hacer es instalarle cloud ahora. Entonces, nos fuimos acá, extensiones, instalamos Cloud y nos encontramos con algo así. Dentro de las opciones que podemos hablar con Cloud, tenemos distintas niveles de permisos que nosotros le podemos dar. Por ejemplo, aquí tenemos el modo de preguntar antes de las ediciones, de editar automáticamente, de modo planear si es que quiero planear y que no esté ejecutando cosas. Y quizás no te sale esta opción que sale bypass permissions. Esta es algo que a mí me gusta a mí porque le doy más libertad de ejecutar cosas sin que tenga que preguntarme si es que no te sale, puedes irte aquí a los ajustes, te vas a settings y buscas acá cloud code y simplemente habilitas esta parte que sale acá, allow dangerously skip permissions. Ya dicho y hecho esto, vamos a crear nuestro agente eh Claudio que nos va a ayudar con los workflows de N8N. Tu nombre es Claudio y vas a ser un agente que me va a ayudar a acceder o a modificar o a crear o a diagnosticar mis workflows en n8n. Vas a crear un archivo que se llama cloud.md, que aquí es donde vas a tener toda la información de lo que hace en general y vas a tener acceso y vas a instalar dos repositorios importantes. El primero es de skills de N8N, que te ayudará a entender cuáles son los mejores mecanismos que tienes o las habilidades que tienes que usar para crear, modificar, editar workflows en N8N. Y el segundo es N8N MC. P, que es toda la información que tienes del MSP para que entiendas qué es lo que estamos haciendo. Con estos dos repertorios que vas a instalar de GitHub, vas a ser mi asistente que va a editar, modificar o crear o ejecutar los workflows de N8N. Vas a ser mi N8N manager. Voy a darle a enter si es que no sabes la aplicación que estaba usando. Es una aplicación de Mac Whisper. Y aquí vamos a hacer algo que es genial, que esto es lo que le da superpoderes a Cloud. Vamos a buscar acá N8N MSP KitHub y vamos a buscar N8N MSP Skills. Vamos a abrirlo, el primero que nos sale acá y vamos a abrir el primero que nos sale acá. ¿Qué son estos? son habilidades que nosotros le estamos dando o superpoderes que le estamos dando. Por ejemplo, N8N Skills, si es que vemos acá, tiene muchas cosas geniales como cómo hacer la sintaxis en específico, como qué cuáles son los correctos sintaxis, los patrones que existen en los workflows, los la configuración de los nodos, ¿verdad? los códigos y este otro que es el MCP es eh 1000 nodos de N8N además de propiedades, operaciones y lo que estamos haciendo le estamos instalando esto porque es como darle como más contexto de las cosas que tiene que hacer y cómo tiene que hacerlos. Esta persona que está acá, Lwski, nos creó y nos facilitó esto. Entonces, aquí tenemos todas las cosas y todo lo que vamos a instalarle. Entonces, aquí voy a bajar, volveré a Cloud Code y le voy a decir, "Aquí tienes el N8N MSP y aquí tienes el N8N Skills." Ya. Voy a volver aquí, voy a copiar los skills, control C, voy a volver acá. Control B. Y ahora que les dije todo esto, voy a darle a enter y vamos a ver cómo empieza a armar por lo menos la primera versión de todo. Hola, soy Claudio, tu asistente especializado. Voy a configurarme para eh empezar a gestionar tus workflow. Y aquí podemos ver todas las cosas que está haciendo. Por ejemplo, clonar el repositorio de MSP, clonar el repositorio de N8N Skills y crear el archivo MD. Y ahora podemos ver que está empezando a crear ciertos archivos que si es que nuevamente vamos a nuestro find a estar acá. N8N MSP, N8N Skills y aquí tenemos todos los archivos de lo que estamos viendo. Lo que va a hacer al final Cloud es llamar a estas skills cada vez que quieran modificar algún workflow o crear algún workflow porque está lleno de buenas prácticas para hacerlo. Si es que abrimos lo de skills, por ejemplo, vamos a tener acá que hay distintos skills como codificar en Python, MSP Tools, configuraciones de nodo, puras cosas que no tenemos que saber realmente. Entonces este archivo le da guía a Cloud Code cuando esté llamando en específico a N8N, ¿okay? Con las buenas prácticas, las cosas que tiene que seguir, etcétera. Y mira, perfecto, he completado la configuración inicial. Ahora estoy listo para ser tu asistente especializado en N8N. conectó N8N MCP y conectó N8N Skills. He creado el archivo de Cloud MD que contiene mi identidad, la arquitectura completa, la Painterrament y listo. Ahora puedes ver que me está pidiendo dos cosas. Me va a pedir lo que es la N8NUR URL y la N8N API Key, que son estas cosas las encontramos en nuestro N8N. Y lo lindo de esto es que, okay, me manda esto y yo podría decirle, "Okay, aquí tienes mi AP Key, aquí tienes mi URL de la instancia. Pero supongamos que no sé y quiero preguntarle dónde consigo esas cosas y dónde lo puedo subir. Y esto es muy importante porque mientras tengamos un endal o un objetivo claro, eh al final cloud code y Code y todas estas cosas nos van a ayudar a llegar a ese objetivo de la mejor manera. Entonces, ¿cómo obtener y configurar las credenciales? Bueno, aquí G N8N API URL y aquí tenemos todos los pasos. Okay, voy a ir a mi inicio. Voy a ir acá y voy a ir donde sale N8N API. Voy a crear una API key que va a expirar en exactamente un día. Esto es para que el momento en el que saque el video no tenga que borrarla. Y le voy a dar a copiar y le voy a decir acá API Key dos puntos acá. Luego para obtener el N8N API URL está simplemente en la instancia. Voy a ir a Google Chrome, voy a ir a instance Level Report. Detalles de conexión y server URL. Copiar, pegar y listo. Ahora le voy a dar a enviar. Configuración completada exitosamente. Todo está funcionando perfecto. El URL de conexión, los workflows que se encontraron, tus primeros tres workflows que puedo hacer ahora. Aquí tenemos algunos ejemplos. Lista todos mis workflows. Muéstrame los detalles. Activa el workflow X. Crea un workflow que recibe un webhook y envía un mensaje a construir un workflow para procesar emails. Busca templates automatización. añade un nodo HTTP request, o sea, modificar los workflows existentes, buscar y explorar, validar y diagnosticar códigos y expresiones. Entonces, esto es realmente una genialidad. Okay, mira, ahora vamos a ir acá, vamos a ir a Clear para empezar una nueva conversación. Si es que quieres acceder a conversaciones previas, simplemente tienes que abrir acá y le voy a decir, "Genial, créame un nuevo workflow que se ejecute todos los días miércoles a las 9 de la mañana, hora de Santiago, y que me investigue qué es lo que está pasando en el mundo de la inteligencia artificial e y las automatizaciones y que me mande un newsletter estilo newsletter de una manera muy cómica y muy chistosa con las top noticias que pasaron en los últimos 7 días. ¿Okay? Esto va a ser un agente de investigación y quiero que me llegue a mi correo electrónico que es benja@imperiodigital. Y bueno, claramente muy importante que tenga acceso a internet. Quiero usar el nodo de AI Agent y se va a conectar vía algún modelo de Google como, no sé, Gemini 3 Pro. Una vez que lo que esté listo, quiero que me lo pase a un formato de HTML bastante estético, bastante interesante y que me dé una buena recomendación para el día. ¿Okay? y le agregar, "Quiero que el workflow se llame Claudio el motivador matutino semanal." Ahora le voy a dar enter y listo. Ahí podemos ver que está creando el workflow, está teniendo acceso a todo y tenemos, mira, buscar templates relevantes de AI agents, investigar los nuevos necesarios, schedule, AI agent, configurar el schedule trigger, el AI agent con Gemini y aquí podemos ver todo el proceso de cómo lo está haciendo. Me la registró mal mi mail, eso sí, pero en fin, ahí lo puedo modificar yo de manera manual. Y mientras trabaja, yo voy a estar literalmente tomándome un cafecito y en vez de estar trabajando, voy a estar supervisando a ver lo que hace, porque es bastante interesante. Y ahora que recopiló toda la información va a empezar a crear el workflow. Y como podemos ver, acaba de crearlo acá Claudio Motivador Matutino. Lo que hace nos explica el workflow, la estructura del workflow, pasa acá, pasa acá, cómo usarlo, qué es lo que está usando. Pero mira, aquí me di cuenta de algo, quiero que me lo importe, no quiero que me lo haga. Entonces, le voy a decir, créalo, eh, impórtalo en mi instancia de N8N. Y mira lo interesante, porque no solamente creó el workflow, sino que empezó a probar si es que funciona o no. Ahora está empezando a crear el archivo Ritmi, que es el archivo de que nos explican cómo hacerlo. Y bueno, y aquí lo tenemos una vez que actualizamos. Y bueno, y si lo abrimos, nos vamos a encontrar con algo así realmente genial. Eh, tenemos el trigger, preparar el contexto que nos lo hace acá, investiga las noticias más importantes, nos prepara el prom, después se comunica con el agente, el que está acá, como le pedimos, nos formateó el newsletter, como le pedimos también. Y bueno, aquí enviar el correo por el nodo de correo. Alternativamente, yo aquí no me gusta tanto este correo quizás, entonces puedo llegar y cambiarlo por, no tengo idea, un Gmail acá y ponerle enviar mensaje. O puedo entrar acá y le digo, "Modifícame el workflow actual y cambia al final por un nodo de enviar correo oficial de Gmail." El correo es Benim perio Digital. Aquí tenemos también el MD de los pasos finales de cómo acceder al workflow y aquí está haciendo los pasos modificando el nuevo Gmail a Gmail, cambiar el destinatario y listo, nos acaba de hacer los cambios. Aquí podemos ver todo, nos va a decir todo, crear las credenciales de Gmail, que puede ser un poco complicado, eh, documentación creada, ventajas del cambio, etcétera. Y aquí nos actualizó el workflow. Si es que vuelvo acá y le doy a actualizar. Ahora vamos a ver que se reemplazó el eh original por enviar esto desde alguno de los correos. Okay, voy a darle ejecutar a ver si es que esto está funcionando. Paréntesis, mientras se ejecuta. Conectar a Gmail puede ser un poco complicado. Y por lo mismo también tengo este eh video acá donde lo explicamos bastante simplificado. Y si es que refrescamos nuestro correo, vamos a ver que aquí tenemos el correo de Claudio, el motivador matutino. Okay, aquí tenemos service Now más open AI. Vamos a verlo. Tenemos aquí la la fuente de dónde sacaron las cosas o esta otra fuente de acá, ¿verdad? Son dos fuentes distintas que nos van diciendo esto. Envidia declara el momento de echar GBT de la robótica. Google search AI mode. Open AI Nvidia. Y aquí claramente tenemos las fuentes porque necesitamos siempre tener las fuentes. Un workflow bastante funcional, muy interesante si es que quieres mantenerte informado. Le voy a dar a guardar y listo. Recordemos que si es que quiero volver a abrir cloud, simplemente tengo que apretar acá esta pestañita que aparece de Cloud. Si es que cierro todo y lo vuelvo a abrir. Voy a tener que volver a abrir aquí a Claudio documentos Claudio abrir y voy a retomar exactamente dónde estaba. Así es que quiero limpiar la conversación. Simplemente le pongo clear conversation y así es como armas workflows que antes quizás te tomaban bastante tiempo en armar. Específicamente aquí podemos ver que son los videos más largos como los de 40 minutos, 50 minutos. Así es como lo hacemos y lo hacemos en un par de minutos. Lo interesante es que ya no tienes que volver a hacer esto porque lo haces una vez y te quedas para siempre con tu agente que te ayuda en los workflows. Quizás el paso más difícil de esto hubiese sido conectar a Google dentro de lo técnico, pero también nos dejaron una guía específico de cómo hacerlo. Puedes hacerlo también viendo el video de YouTube que subí donde hago esto o publicando en la comunidad de Imperio Digital, accediendo a soporte y haciendo la pregunta acá, tipo, ¿cómo conecto Google a N8N? Okay, dicho y hecho esto, espero que este video te haya servido. Hay bastantes videos en el canal que te pueden gustar y como yo no te conozco tan bien, pero Google sí, te recomiendo que veas este video que Google te va a sugerir acá. Mucho éxito.
