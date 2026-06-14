# 🏗️ Despliegue en Local

> Ruta: Vibe-Coding › 🏗️ Despliegue en Local

**🎬 Vídeo (20.8 min):** https://youtu.be/uQEPoSNfLX4

---

## Parte V. Clonar el repo, plan de desarrollo, correr en local y primeros fixes

En esta lección vas a pasar de “maqueta” a “proyecto real corriendo en tu máquina”.

Aquí hacemos 4 cosas clave:

1. Clonamos el repositorio desde GitHub a Antigravity.
2. Le pedimos al agente que analice el proyecto y nos regrese un plan de desarrollo.
3. Configuramos variables de entorno y corremos la app en local con Vite.
4. Arreglamos los primeros bugs típicos. Tailwind, dark mode y legibilidad.

Si no terminas esta página con el proyecto corriendo en local, no avances.

## 1. Clonar el repositorio en Antigravity

En Antigravity seleccionamos **Clone Repository**.

Qué sucede aquí:

1. Antigravity te pide autenticar con GitHub.
2. Te da un código.
3. Pegas el código en GitHub y autorizas.
4. Seleccionas tu repo.
5. Eliges una carpeta local donde guardarlo.
6. Abres el proyecto.

Resultado:

- **Proyecto clonado en local.**
- **Archivos visibles en el explorador.**
- **Git listo para trabajar desde Antigravity.**

## 2. Primer paso antes de tocar nada. Pídele al agente que entienda el proyecto

Antes de pedir cambios, hacemos esto:

- Ponemos el agente en **modo Planning**.
- Elegimos un modelo “fuerte” para pensar.
- Le pedimos que: - Lea el PRD.
- Lea los README.
- Identifique el tech stack.
- Liste features completos y pendientes.
- Proponga un plan de desarrollo por fases.
- Priorice para lanzar un MVP hoy.
- Considere deploy final en Vercel, pero primero local.

Este paso evita el error clásico:  
Pedir cambios sin que el agente entienda el sistema.

## 3. Segundo agente en paralelo. Preparar “agent skills”

En paralelo abrimos otra conversación en modo Fast y le pedimos al agente:

- Investigar qué son los **agent skills** en Antigravity.
- Recomendar la mejor forma de usarlos.
- Crear carpetas y placeholders para futuros skills.

Ojo:  
Esto no es obligatorio para que corra el MVP, pero sí prepara el proyecto para escalar mejor.

Aquí vas a ver por qué Antigravity pide permisos antes de aplicar cambios.  
Tú revisas. Tú aceptas. Ese es el flujo.

## 4. Ejecutar el proyecto en local

Una vez que el agente nos da el plan, le pedimos algo práctico:

- Confirmar el estado real de features según el PRD.
- Decirnos cómo correr el proyecto local con Vite.
- Decirnos qué variables de entorno necesitamos.

Normalmente el flujo es:

1. Crear un archivo `.env.local` en la raíz.
2. Pegar las variables necesarias.
3. Instalar dependencias si aplica.
4. Correr el comando de desarrollo.

En el video ejecutamos el comando de Vite en terminal y abrimos el localhost.

## 5. Variables de entorno. Qué necesitas y de dónde salen

En este paso el agente te guía para conseguir:

- API key de Google AI Studio.
- Project URL y API Key de Supabase.

Importante:  
Estas variables solo son para desarrollo local.  
No compartas tus keys. No las subas a GitHub.

## 6. Problema típico. “Abre en blanco” y no carga UI

Después de correr Vite, en el video pasa algo clásico:

- La app abre, pero se ve en blanco.
- Parece que no hay UI.

El agente detecta la causa.  
En este caso fue un tema de configuración de Tailwind con Vite.

Solución:

- Parar el servidor con Ctrl + C.
- Volver a correr con la configuración corregida.
- Recargar el navegador.

Resultado:  
La UI aparece correctamente.

## 7. Dark mode. Funciona, pero se rompe el diseño

Luego probamos el toggle de tema.

Problemas típicos que aparecen:

- Cambia a dark mode pero algunos componentes siguen en light.
- Cambia a dark mode pero el texto queda ilegible.
- Títulos o labels con color demasiado oscuro contra fondo oscuro.

Aquí sucede algo importante:  
Le pedimos al agente que lo arregle y que verifique con pruebas reales.

## 8. Lo más potente del video. Antigravity probando en el navegador

En esta parte Antigravity pide permiso para usar el navegador.

Qué hace:

- Abre un navegador controlado.
- Navega la app.
- Reproduce el bug.
- Verifica el problema visual.
- Toma evidencia.
- Aplica cambios.

Eso es oro. Porque ya no es “yo creo que…”.  
Es el agente viendo lo mismo que tú.

Resultado:

- Dark mode funciona.
- El texto se ve bien.
- La interfaz es legible.

## Resultado esperado al terminar esta página

Al final de esta lección debes tener:

- Repo clonado en Antigravity.
- Plan de desarrollo definido por el agente.
- `.env.local` creado y configurado.
- App corriendo en local con Vite.
- UI visible correctamente.
- Dark mode funcionando y legible.
- Cambios guardados con commits.

## Errores comunes

- No clonar el repo correctamente, o no autorizar GitHub.
- No crear `.env.local` o poner variables incorrectas.
- Subir keys por accidente al repo.
- Confundir “maqueta” con app funcional.
- No reiniciar Vite después de cambios de config.
- Pensar que dark mode “ya está” cuando el texto no se lee.

### Qué sigue

En la siguiente página vamos con el siguiente paso del MVP:

- Conectar Antigravity con **n8n** vía MCP.
- Ejecutar un flujo real.
- Y empezar a generar automatizaciones desde prompts.

Después:

- Conexión y notificaciones con Supabase.
- Deploy final en Vercel.

## 🎙️ Transcripción

Okay, nos quedamos entonces en el que estamos revisando los commits en GitHub. Vámonos de vuelta aquí al al código fuente. Ya que tenemos todo esto, vamos ahora sí a continuar. Vámonos a Antigravity. Ahora sí vamos a ver Antigravity. Vamos a esperar que cargue la interfaz. Eso va a ser pantalla completa. Y si se fijan tenemos varias opciones, abrir folder, abrir legend manager o clonar repositorio. En este caso vamos a empezar con clonando repositorio. Nos va a decir aquí que clonemos de Gitcop, le damos que sí. Me dice que quiere iniciar sesión la extensión de Gitcop. Le damos que sí. Nos dice que nos va a dar este código. Vamos a copiarlo y le damos copia en continuity github. me lo va a abrir en una ventana que no es porque es el otro navegador. Ya recuerden que tengo un modo incógnito, así que lo voy a poner acá. Le vamos a dar continue y me vamos a pegarle el código que había copiado y ley continuar. Voy a dar que sí que autorizo antigravity y me regreso para antigravity. Ahorita nos va a mostrar todos los repositores que tenemos, que obviamente en este caso nada más tenemos uno, así que lo seleccionamos y nos va a decir que escojamos una carpeta donde queremos guardarlo, en local. Eso lo tenemos que hacer y lo voy a guardar en mi carpeta tal cual. Dice que si quiero abrirlo y lu decir que sí y listo. Y bueno, me dice que si quiero confirmar en este autor, que el autor soy yo. Entonces voy a decir que si quiero confirmar. Y como les había dicho, de este lado tenemos lo que es todos los archivos, configuración, etcétera. Ahora, dos cosas para verlo aquí en local. Como no, esto no es un HTML, no pueden ustedes nada más darle como que ay, quiero previsualizar, aquí corre el backend y aquí corre el frontend. Entonces, eh no les va a funcionar sin nada más para previsualizar. Vamos a tener que hacer unos cambios. Lo podemos pedir a la gente ahorita, pero vamos a iniciar. Ya estamos aquí con nuestra gente y aquí tenemos el modo fast y el modo plenamos que utilice el Gemine 3 Pro low. Vamos a utilizar el modo plenación y vamos a hablarle. Un segundo, cambio mi micrófono. Una, dos, dos. Probando, probando, probando. Una, dos. Dos, dos, probando. Una, dos, do, dos, probando. Por alguna razón no me está detectando el audio. Vamos a volver a probar. Okay. Necesito que analices este proyecto, que identifiques el text que se va a utilizar, que leas todos los RMI files. Es muy importante que leas el PRD y lo entiendas. vas a ver qué tecnología se va a utilizar, cuáles son los user stories y los futurs, qué tenemos pendientes, por dónde podemos empezar, vas a crear un plan de desarrollo. La idea es que el día de hoy lancemos esto como MVP y podamos hacer un deploy en Versel, aunque antes haremos un deploy en local. ve, revisa, entiende el documento y regresas conmigo con un plan bien definido. Okay, vamos a darle enviar. ¿Qué pasa? dice, "Generando, va a empezar a a trabajar y te va a decir, eso te lo dice en inglés, que es como que el el procesamiento que está leyendo, qué está haciendo, etcétera. Mientras podemos abrir esta empezar una nueva conversación. Si se fijan, eso está padre porque puedes ir viendo tal cual está revisando todo lo que yo lo que yo tengo. Y vamos a darle dismiss y vamos a abrir uno nuevo y este va a ser fast. Quiero utilizar el flash y que se fijan, eso está corriendo. Eh, mientras yo puedo abrir otras cosas, le voy a decir, necesito que investigues qué son los agent skills para antigravity. ¿Cuál es la mejor forma de usarlos? ¿Y qué crees? Las carpetas y los placeholders necesarios para utilizar los skills que te daré más adelante y vamos a mandarlo. Okay, aquí me dio un plan de implementación. Le voy a dar aceptar. Voy a dar aquí, voy a dar aceptar. ¿Por qué sí le tuve que aceptar? Porque yo le pedí que creara directorios agent para el agent skill y todo eso. Entonces, por eso tiene que modificarse. Se fijan, aquí me salió el agentil.md MD y le voy a dar aceptar todo y vamos a cambiarnos a los el otro agente, perdón, cerré cerré la ventana y ya terminó, así que vamos al otro agente. Se por no me deja seleccionarlo aquí. Okay. Implementación del plan. Okay. Implementation plan. Aquí lo tenemos. ¿Qué es lo que quiere hacer? Texta, la confirmación, que es lo que vamos a utilizar. Chat 100, tailwin, eh supa base. Vamos a tener que darle las bases, las los URL, los keys, todo lo que necesite. ¿Qué es lo que vamos a estar haciendo? Fase uno, infraestructura, navigation routing, modificar. Fase cuatro, integración con supabase y después correr en el local para verificar. Suena muy bien a todo lo que yo le dije. Le puedo dar aquí o le puedo dar aquí. Es exactamente lo mismo. Y le dijo que puedes empezar con el plan. Y aquí, ¿qué me va a decir? digo, obviamente si ustedes confían y que un buen pry en la IAP, no tendrían por qué leer todo, pero básicamente va a instalar Tailwind y que es básicamente esta el Tailwind CSS, este framework que se utiliza para lo que es el UI. Vamos a darle aceptar. Recuerden que el modo que configuramos es para que me proponga y yo lo acepte. podemos configurarlo para que básicamente corra solito y haga absolutamente todo y nada más me diga, "Ya está todo listo." Que si no eres muy técnico, igual te conviene hacer eso porque si no entiendes, si te pones a leer cosas nada más para darle aceptar, no tendrá mucho caso, también perderíamos. Me va a dar algunos errores, el solito lo va a checar, se va a autocorregir, me va a decir, etcétera. Entonces, vamos a darle ahorita que trabaje. Voy a parar el video para que no se haga muy largo y dejemos que se ponga a trabajar. Bueno, en lo que trabaja no más decirles que aquí es el implementation plan, pero aquí tenemos las task. Esas son todas las actividades, todo lo que va a hacer. Eso es lo que ya hizo y eso es lo que sigue por hacer. Vamos a dejarlo ahorita que que trabaje y regresamos. Okay, vemos que ya terminó. Como podemos ver, de este lado nos creó muchísimas más carpetas, eh documentos, todo lo que hacía falta y tal nos hace falta más. y me dice, "Okay, ¿quieres que pasamos con deployell?" O, "No, vamos a decirle, no, aún no quiero hacer deployers. Me gustaría ver cómo se ve mi interfaz. Quiero hacer algunas pruebas y darte feedback para que la sigamos mejorando. Haz dos cosas. Una, puedes ver todos los features que tenemos en el PRD, confirmar en qué estado están y cuáles faltan por terminar de configurar. y dos, ¿me puedes decir cómo hago un deploy en local para poder hacer una previsualización en tiempo real de tus cambios? Y MN3 Flash está bien porque le estoy preguntando algo, digamos, en modo chatear, no necesito que vaya y eso y hola, Marcel. Esto no sé por qué lo puse, pero bueno. Listo, vamos a darle enviar. Si se preguntan, ya le había comentado en el video anterior, est utilizando Whisper Flow. Es un una herramienta, tengo mi Mac que me permite hablar y entiende, no es una narración directa, entiende el contexto, lo que quiero decir y me hace correcciones, me deja un output mucho más claro. Vamos a ver qué nos dice. Okay, estado de filters del PRD. Vamos a hacer esto más grande. Infraestructura check. Mobile UX. Check. Epic Prospects. Check. Epic Wizards. Epic Wizard. Reporte. Reporte. Parcial. Okay. Cierre pendiente. Aquí vamos a meter un N8N más adelante. Y dice cómo en local. Primero tienes que configurar tus llaves. Asegúrate un archivo llamado en punto local en la raíz con lo siguiente. Inici de desarrollo y vite te dará una URL. Abran tu navegador, pruebas sugeridas, dashboard y te pasamos a lanzar en local y me dice qué es lo primero. Okay, antes de eso crea tú la carpeta por mí de end local, pon el place folder de lo que necesito estoy, las variables y explícame yo cómo poder conseguir esas variables. Bueno, no son esas variables, esas llaves. Okay, me dice que si le doy permiso. Le voy a dar que sí en esta conversación. Ya me creó esto. Okay, aquí yo tengo que sustituir, obviamente. Aquí me voy a especificar. Okay, te vas a Google Studio, cuenta crear Tapi Key y la pones aquí. Superabase, te vas a ir al Superbase dashboard. va a sacar un nuevo proyecto y ya lo ya lo tenemos. Settings, rueda API, encontras la URL URL que vamos a pegar aquí y te vas a ir a Project Apikis. Perfecto, guió todo. Entonces, vámonos de vuelta a Google Studio. Dijo que nos fuéramos para acá. App key, bueno, ya tenemos aquí una API key. Vamos a copiarla. Vámonos de vuelta. Todo esto lo voy a acabar borrando, así que no pasa nada. Y vámonos ahora a Supase. Y nos dijo que nuestro project URL, no recuerdo bien dónde decía, así que vamos de vuelta. En el menú lateral izquierdo, iconos settings, haz click en app y encraes la URL. Okay. Entonces de este lado aquí ya teníamos una ah pro URL. Aquí está Project URL. Vamos de vuelta. Y me decía que para la API Project API Kiss AP kiss, vamos a copiar la que ya teníamos aquí y nos vamos para acá y listo. Vamos a darle grabar. Y nos dijo, "¿Quieres que con algo más?" Mientras los consigues. Ya lo tenemos. Y aquí arriba me había dicho cómo hacer npm round de ojo, esto no lo vamos a hacer aquí. El npm don ref, eso lo tenemos que hacer en consola. Así que le damos aquí para abrir la consola y vamos a ponerle npm run de le damos enter. Listo. Dice que el local es este. Vamos a copiar esta URL. Vámonos para nuestro navegador y vamos a pegarla. Y nicho team finders local. Okay. Si se fijan está bien el texto, pero no tenemos nada de UI. Entonces vamos a aprovechar las virtudes de antigravity. Vamos a seleccionar esto y voy a copiarlo. Me regreso antigravity. Le voy a dar acá no más antes. Déjenme asegurar que no me haya dicho que tenía que hacer algún otro deploy de algo. Okay, se lo pego y luego voy a decir, revisa, por favor el screenshot que te acabo de dejar. Ya hice el mpm run def, corrió BT 6.4.1, abrí el local host con puerto 3000, pero como puedes ver en la imagen, sales todo en blanco, no hay como que ninguna carga eh del UI. ¿Me puedes verificar si pasó algo con React Tailwind o que por qué no puedo ver tal cual cómo debe ser mi dashboard de la manera correcta? Gracias. Vamos a mandar igual lo voy a poner pausa para que no se nos haga muy largo el video. Okay, ya terminó. Ya encontré el problema. Lo que está pasando es que 4 no funciona simplemente con imports. Tiene un proyecto de plugin específico para que sepa cómo usar esas nuevas reglas. Okay. Supuse que algo de instalé el plogin oficial actualicé tu bit config. ¿Qué tienes que hacer ahora? Presiona, reinicien el comando terminal, presiona control C para tener el proceso actual. Escribe de nuevo en Pond. Nos vamos para acá. Le voy a dar control C. Ya lo terminó, así que luego si lo de para arriba. Los que hacen usar terminal les sale el último comando. Le voy a dar enter de nuevo. Ya corrió. Es el mismo local. regreso, actualizo y ya lo tenemos funcionando. Perfecto. Entonces vemos que tenemos aquí nuevo diagnóstico, no me dejar. Perfecto. Mis reports generados todo esto no funciona porque tal vez no lo tenemos configurado. Vamos a cambiarlo a light. Okay, si se fijan aquí está fallando. Entonces, ya nada más por último, ya para terminar este video, le voy a decir esto. Me regreso y le digo, "Ve la imagen que te acabo de adjuntar. Eh, se supone que tengo un modo oscuro activado, sin embargo, lo sigo viendo en light mode. Puedes verificar por qué y hacer los ajustes necesarios. Lo mando y hacemos pausa. Okay, ya terminó. Dice que corregí variables de tema dinámicas, limpieza de componentes, soporte nativo B4 y si que me asegure correrlo de nuevo y haga pruebas. Si se echo un vistazo y no si es como lo esperaba. Está tan orden. Podemos seguir con el último paso PR que es el menor de lí públicas. Okay, entonces vamos a darle control C para parar. Volvemos a correr. Regresamos. Para acá se actualiza solo. No más quiero confirmar. Modo oscuro, modo claro, modo oscuro. Okay, está funcionando modo oscuro, pero el texto no es legible. [resoplido] Entonces vamos a decirle para hacer el cambio y terminal. Esperemos. Ahora sí. Perfecto. Está funcionando en modo oscuro. Sin embargo, el texto, más que nada los títulos y algunas otras partes del texto son de un color muy oscuro, muy similar al fondo, entonces no se logra distinguir. Necesito que por favor vayas, abras tú, hagas las pruebas y veas eh lo que está pasando para que puedas implementar los errores. y tráeme un screenshot de regreso para que pueda verificar que efectivamente estás viendo lo que yo estoy viendo y lo pudiste solucionar. Vamos a mandar. Okay, aquí decidí continuar la grabación porque está muy interesante. Dice que Antigravity me pide permiso para utilizar el browser, así que le voy a decir setup y me sale aquí que está lanzando el browser y ese es un propio browser que él está abriendo y le voy a decir que quiero instalar la extensión. Está haciendo Google Chrome. Vamos a darle agregar a Chrome. Agregar extensión. Está increíble. Está buenísimo. Okay. Si se fijan, yo no estoy haciendo nada. Ese aro azul, el brillo azul que sale alrededor es una forma de indicar que Antigravity está probando el sistema y está moviendo. Yo no estoy moviendo el mouse, aquí está mis manos y se está moviendo, está haciendo todas las cosas. Yo le pedí que fuera y que viera lo que yo estaba viendo y que tomara screenshots y quisiera todo lo necesario. Ahora ya desapareció el asul. Quiero cre que ya después de hacer esto. Vámonos por antigravity. Okay, perfecto. Y lo está eh analizando. A mí esto me sigue volando la cabeza todavía, honestamente. Vamos a decirle que aceptamos todo y le pongo pausa y regresamos cuando termine. Okay, ya terminó. Fue, corrigió, verificó, hizo todo, tomó las notas y me pregunta aquí, ¿qué me parece? Vamos a hacer un control C. Corremos de nuevo, regresamos al original, actualizamos y ya está solucionado, ya se alcanza el Entonces le voy a decir, muy bien, quedó genial. Continuemos con el PRD. Puedes analizar qué future sigue hundiente. Lo voy a enviar, pero aquí terminamos el video. Continuamos en con los features. En el siguiente video un pequeño eh spoiler de lo que se viene. Vamos a ver cómo instalar N8N, no cómo instalar, cómo configurar la conexión NHN entre Antigravity y nuestro NHN para que vayamos un flujo, procesemos algo y regresemos. Y no solo eso, vamos a intentar que Antigravity genere el flujo por nosotros y les damos un buen promp y logramos explicar. Después de eso, el siguiente video configuramos autentificación con supase. Después de eso nos vamos a lo que es dey conversel y ya veremos si hacemos un trouble shooting de Versel. Si todo sale bien, ahí terminaría el nos vemos en el siguiente
