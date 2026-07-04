# 8️⃣ Integración n8n & Github

> Ruta: Vibe-Coding › 8️⃣ Integración n8n & Github

**🎬 Vídeo (36.3 min):** https://youtu.be/fW9mSRhQLhA

---

## Parte VII. Integración híbrida con n8n, feature nueva de cotizaciones y hábitos pro con GitHub

En esta lección le damos un giro al MVP. Ya no es solo “frontend bonito con Supabase”. Ahora lo convertimos en un **frontend limpio** que puede disparar procesos reales en **n8n**.

La idea es simple:

- Si tu comunidad vive en n8n y quiere mantener lógica en n8n, perfecto.
- Pero igual quieres una interfaz moderna, rápida y presentable para clientes.
- Entonces hacemos un modelo híbrido: **UI en Antigravity. Automatización en n8n**.

## 1. Concepto clave. “Frontend pro” + “backend en n8n”

Aquí defines dos caminos válidos:

- Todo en n8n. Backend, lógica, storage, todo.
- O híbrido. UI y control en el front, automatización pesada en n8n.

Este video se enfoca en el híbrido porque es el más práctico para:

- agencias,
- freelancers,
- y equipos que ya dominan n8n.

## 2. Nueva feature. Página de cotizaciones con “email composer”

En lugar de seguir agregando pantallas random, aquí hacemos una feature de negocio real:

### Qué agregamos:

- Un nuevo menú: **Cotizaciones** (vista lista).
- Al seleccionar una cotización: - Panel izquierdo: composer del correo.
- Panel derecho: historial de correos enviados y estado.

### Lo importante:

- Botón para generar el email con IA (sin escribir desde cero).
- Selección del cliente. Que autopopule su email.
- Inserción dinámica del link único de la cotización.
- Botón para enviar payload a n8n.
- UI de confirmación: fecha de envío + check verde cuando fue exitoso.

Esto convierte el MVP en algo vendible. No es demo. Es herramienta.

## 3. Diseño correcto del flujo n8n

Aquí está el “pattern” que te tienes que aprender:

1. **Webhook Trigger** recibe payload desde la app.
2. Procesas lo necesario (en este video terminamos simplificando).
3. **Gmail node** envía el correo.
4. **Webhook Response** devuelve confirmación al frontend.

### Twist importante del video

Decisión inteligente para simplificar el MVP:

- Ya estamos generando subject y body en el frontend con IA.
- Entonces el payload a n8n se reduce a: - `to_email`
- `subject`
- `body`
- `client_id` o `client_name`
- `quote_id` y `share_link`

n8n solo ejecuta envío y respuesta. Mucho más estable.

## 4. MCP de n8n. Qué sí y qué no debes esperar

Tema clave para expectativas:

- El MCP puede ayudarte a buscar, ejecutar, inspeccionar, y guiarte.
- Pero dependiendo de cómo esté implementado el MCP server, puede que no soporte “crear workflows completos” de forma directa.

Lección práctica:

- No te cases con “IA lo hace todo”.
- Usa IA para estructura, JSON, nodos, mapeos, y checklist.
- Y si no puede crear el workflow, lo montas tú en 3 minutos con la guía.

## 5. API Key correcta de n8n

Aquí está el truquito que te ahorra horas:

Si el MCP no conecta o te da “no autorizado”, normalmente no es “el URL”.  
Es la key.

Ruta correcta:

- n8n . Personal settings . API . Create API key

Luego la pones en tu `.env.local` para que Antigravity pueda usarla.

## 6. Buenas prácticas para payloads entre UI y n8n

Reglas rápidas:

- Payload pequeño. Solo lo que n8n necesita.
- Campos claros y predecibles. Nada “free text” si no es el body.
- Siempre devolver un response JSON al frontend con: - `success: true/false`
- `message`
- `sent_at` (timestamp)
- `email_id` o tracking id si existe

El frontend NO debe marcar “enviado” hasta que llegue `success: true`.

## 7. Feature obligatoria cuando ya envías correos. Gestión de clientes

En el video aparece un punto de producto real:

Si ya vas a enviar correos:

- necesitas ver clientes,
- y editar email.

Entonces agregamos:

- Vista “Clientes”
- Edición del cliente
- Campo de email
- Guardar cambios

Esto no es “nice to have”. Es parte del flujo.

## 8. GitHub. Tu hábito más importante en todo el curso

Aquí no hay debate:

Si no haces commits frecuentes, tarde o temprano te vas a arrepentir.

Buenas prácticas del video:

- Commit después de cada cambio grande.
- Mensaje de commit describiendo qué cambió.
- Update de documentación cuando agregas features importantes.
- Si el agente va a hacer cambios grandes, que te pregunte si quieres commit.

## 9. README actualizado. El MVP debe ser “instalable”

Un MVP real no es solo código. Es “alguien lo puede correr”.

README mínimo obligatorio:

- Qué es la app.
- Qué hace el MVP.
- Tech stack.
- Cómo correr en local.
- Variables de entorno necesarias.
- Cómo conectar n8n (webhook + API key).
- Qué parte hace UI y qué parte hace n8n.

Esto también te ayuda si lo compartes en Skool para que la gente lo clone y lo pruebe.

Al final debes tener:

- Página de cotizaciones con composer e historial.
- Payload listo para enviar a n8n.
- Workflow en n8n con webhook + Gmail + response.
- UI que marca “enviado” solo con respuesta exitosa.
- Vista de clientes para editar email.
- Commits hechos correctamente.
- README actualizado para correr el MVP.

## 🎙️ Transcripción

Okay, ya tenemos el MVP 100% operativo, pero ahora vamos a darle un pequeño twist. Eh, vamos a integrar en 8N. ¿Por qué vamos a integrar N8N? Porque digamos que ustedes quieran mantener el backend en N8N, que es a lo que están más cómodos, pero necesiten un front limpio, bonito, el cual puedan utilizar. Entonces está ya les va a ayudar para eso. Si quisieran hacerlo sin N8N y que todo sea desde acá también se puede sin ningún problema. Pero entonces vamos a hacer un híbrido. Voy a eh pedirle lo siguiente a el agente y me voy a cambiar a Vamos a probar el opuso planeación porque quiero que me dé un plan. Okay, con el MVP ya al 100% se me ocurrió agregar una última funcionalidad. ¿Qué te parece si agregas eh un nuevo future? Esto va a ser un nuevo menú donde vamos a tener eh todo lo que son eh las cotizaciones generadas por los clientes, pero en una vista de lista una vez que se le haya enviado el correo. ¿Qué vamos a tener que tener en esta nueva página? Vamos a tener la opción de eh poder generar un correo desde cero. Yo lo voy a poder escribir, lo voy a poder un botón que le pida a la que me escriba ese correo. Voy a poder seleccionar el cliente al que va y automáticamente va a popular el email. me va a permitir insertar de manera dinámica el enlace único que se genera y voy a necesitar también una vista paralela a un lado. Okay, se me paró porque llega el tiempo. El otro necesar una vista paralela a un lado donde haya un botón para mandar un payload completo a N8N. Toma nota de esto. Necesito que te conectes al MCP de N8N y tú generes un flujo. El flujo va a constar de lo siguiente. Mi trigger va a ser un webhook donde voy a recibir todo mi payload. De ahí va a procesar el agente. Utilicemos Gemini. Va a procesar ese correo. Le tenemos que mandar toda la información que estamos generando de la cotización. Esto lo va a procesar. Lo único que nos va a hacer es hacer un output con un Jason estructurado con el subject, el correo final que va a tener el enlace en bebidor y al final vamos a tener un nodo de Gmail para enviar el correo y hasta el último necesitamos un Webhook response para regresar la respuesta hacia la nueva interfaz que el correo ha sido enviado exitosamente y Ese historial del correo se tiene que guardar en esa misma página en la que tenemos para que yo pueda consultar todo el historial de todos los correos que he estado mandando con mis cotizaciones a los clientes. Revísalo, genera un plan y regrese conmigo. Okay, eso es un poco ambicioso. Vamos a ver en cuánto lo separa. Aquí hay que hacer un cambio que puso MCP en lugar de MSP. Ah, creo. Okay, estamos en plan 4.5 Thinking y vamos a mandarlo. Perfecto. Como siempre le pondré pausa porque esto va a tardar un poquito, pero regreso ya que me haya dado la respuesta. Okay, no ha terminado de todo al 100%, pero ya me generó un plan. ¿Qué es lo que va a hacer? va eh bueno, dicen la investigación del MCP de N, sus capacidades, creo el plan de implementación, el breakdown aquí lo podemos tener todo lo que me hizo. Qu manager future implementation plan, crear una nueva tabla va a ser el W trigger, Yine agent, Gmail sende. los componentes, panel izquierdo, panel derecho y eso es todo lo que va a hacer. Va a haber plan de verificación, pruebas automáticas, verificación manual. Es importante que el work de noche instal de WFC el flujo o puedo generar automáticas workspace de noche. Ya tenemos conectado MCP creencias de Gmail. Okay, vamos a darle proceder. Okay, el usuario lo aprobó y va a empezar a trabajar. Aquí tenemos los task porque le pedí que hiciera todos los sta y el plan y podemos ver que accedió al PRD para verificar información. Y en teoría lo que quiero ver es que pueda acceder a mi N8N y me cree el flujo sin que haga nada. El flujo no va a estar al 100% no va a estar conectado, pero es un avance muy muy importante. Entonces voy a abrir mi N8N mientras esto sigue trabajando. Esto aquí en mi 8N. Este veo que fue el último, el que tengo hasta arriba, el último que se se ejecutó. No tengo nada más. Vamos a ver si Antigravity me puede puede ser capaz de crearme un flujo completo conectándose con MCP. Vemos que este es el plan, el cual suena bastante bien. Vamos borrar esto. Y esas son todas las tas que va a hacer. Al utilizar Opus 4.5 Tinking, a lo mejor se tarda un poquito más, pero como le pedí múltiples cosas, era importante que lo dividiera en etapas y importante utilizar o el Opus 4.5 Thinking o utilizar también el Gemini 3 file. Hubiera utilizado yo en este caso. Y vamos a ver ahorita que que avance. Igual le pondré pausa y regreso cuando ya me dé un poco más de información. Okay, dice que está llamó la tool del MCP de N8N y dice que el servidor MCP no soporta creación directa Wordflow desde código, solo permite ejecutar y buscar. Voy a documentar la configuración manual de Wordflow y identificar el usuario para que lo configure. Okay, no me está aceptando que lo cree directamente y estoy casi seguro que sí se puede conectar. A lo mejor no conecté el MCP correctamente. Ahorita hacemos unas pruebas. Okay. Esto está eh trabajando, está haciendo muchas cosas. Mientras me pide que vaya, que verifique esto, que vaya al ques, verifique que la página cargue correctamente, que que se vea el email compuser en el lado izquierdo, el historial del lado derecho. Checa que en el side diga conciones con un menú. Si están haí con disponibles, salga en el dropdown, tomo un screenshot y reportes errores. Vamos para acá. Estoy en cotiziones. Vamos panel. Quiero ver que si sea navegable. Perfecto. Elige una cotización. Imperio 3 sin email. Okay. Asunto. Esto es una prueba. Cuerpo por el correo que me lo escriba la IA. Y el link ya está aquí. Saludos cordiales. Y si enviar el correo, no me dice nada. El cliente no tiene correo registrado. Perfecto. Me voy a mi panel. Tengo Imperio 3 y Okay. Es otra cosa que habrá que hacer. ¿Cómo edito los clientes actuales para agregar el correo? Entonces vamos a de vuelta a eso. Vamos a ver que todo me esté funcionando. Okay, perfecto. Ahorita no lo voy a decir porque veo que sigue pensando, pero al mismo tiempo si me voy a mi otro que le pedí que me investigara acerca de 8N, me dijo que me pidió que pusiera esto en el local para que él probara a conectarse. Entonces, vámonos de este lado, mi local, vámonos hasta abajo, enter. Pegamos esto y me voy a ir a mi N8N. Eso sí lo voy a ocultar porque eh si no quiero cambiar esta información de mi NHN directamente, pero simplemente cambian aquí sus datos, API y ya la saben sacar todos. La NH8N base URL, pues tal cual es la URL con la que entran la N8N. Listo, ya dice lo que me pidió. Si prueban. Vamos a ver. está entrando el M local para revisar los parámetros. Es que ya lo pudo configurar satisfactoriamente. Y ese es un hello world para testear. Vamos a verle aceptar. Y si crear el workflow token doc Jason. Okay. Es un error al parecer algo está mal en su Jason. Ahorita lo va a tener que checar. Lo corrigió, me lo va a volver a mandar. Okay, sigue fallando y está iterando para ver qué es lo que está pasando. ¿Qué dice mensaje que no está autorizado? Okay. Có tener llave correcta. El tema de local y notado que venía que tienes tiene un formato de token JWT. para que yo pueda crear flujos no pública de instancia de noche vea settings la reda de abajo a la izquierda personal settings API create AP ke nhn ap me pide que la cambie okay entonces vamos a hacer eso. Pongo pausa y regreso. Okay, ya hice los cambios. cambiar le dir API Mor creado exitosamente se supone que se llama antigravity test world entonces vámonos de vuelta a nuestro HN aquí está antigravit Hello World si nos metemos para acá es un post con un mensaje con necesito sacarlos ahora puedo construir lo que tú quieras de vuelta antigravity y me dice Okay, perfecto. Si que sí, ahora que el P está construido y verificado, puedes darme órdenes complejas como soy el arquitecto. Yo me encargo de seleccionar, bla, bla, bla. Okay, vámonos. Ahorita no quiero nada con este otro chat. arnos de vuelta en el que estábamos, que es este. Y aquí siento que este chat se quedó trabado en esto, así que le voy a dar parar y le voy a decir en ya en fast le voy a decir. Okay, tuve que parar la ejecución, ya te estabas tardando demasiado tiempo. Por favor, revisa rápidamente, no te tardes, en qué fue lo que te quedaste de la implementación y vuelve a verificar que efectivamente tengas la conexión a N8N. Recuerda que vas a crear un escenario que se llame envío de correo a clientes donde tu nodo inicial sea un webhook trigger que va a recibir el payload que tú le vas a mandar desde aquí va el payload que le vas a mandar son todos los datos del cliente más el link de la cotización. Eso lo va a usar un agente para generar el correo con el link embebido en el correo para después mandarlo por Gmail. Obviamente para eso tienes que mandarle todos los datos del cliente en tu payload para después usar un response Wbook que te avise que ha sido enviado exitosamente para que tú puedas actualizar la parte de cotizaciones y salga con enviado. Me faltó agregar que quiero que salga la fecha en la que se envió y un green check o algo que compruebe que fue enviado exitosamente. Revísalo y me avisas. Okay, vamos a darle enviar. Okay, por alguna razón no vi que pasara nada. Y si se pante. Okay. Para no tener que volver a escribir todo, voy a volverme la aplicación de Whisper Flow donde tengo mis transcripts y regreso. Listo, ya se lo envié. Lo está analizando todo de nuevo y no que me confirme ahorita. Okay, están realizando el PS. Recuerden lo que habláamos en un principio de las skills. Si nos vamos en agent skills enent builder skill md y aquí es todo lo que dice. Esas son skills. Cada vez que tú requieras hacer algo. Es importante que bueno, no es importante, pero es de buena práctica que tengas tus skills para de las cosas que tenga que hacer para que la gente sepa directamente qué llamar y cuál es la forma en la que tiene que procesar ciertas tareas que tú le pidas. Okay, vamos a ver que si permito correr el comando. Le digo que sí. Dice inválido. Intentar de nuevo workflow request body. Vamos a volver a dar. dice que Warfare creadoamente mientras me sigue pensando de vuelta. Vamos para atrás envío de correo a clientes como yo le pedí un webbook lo procesa Gemini se envía por correo y una respuesta aquí me va a pedir que conecte mi carencial conectada a estos y el mensaje esto no me lo mapeó. Así que lo tengo que mapear. Dice que mi VT esta la está mandando a través del web. Bueno, aquí ya no tengo aquí mis variables de entorno, entonces esto lo tengo que mapear y mi web finish envío puesta. Okay, me toca ponerle un mensaje temporal y un correo temporal. Me voy a poner mi correo para poder hacer una prueba. Voy a dar save publish. Y ahorita la prueba. Vamos de vuelta para acá. NHN envío corre utizamiento deciones nueva vista la página deesar material compostor checkes y okay vamos para allá y vamos a A ver qué nos llega. Vamos a refrescar. Ah, lo que rechazó. Vamos a ver directamente. Okay, no está cargando, así que vámonos para acá y le voy a poner npm r. Y ya está corriendo. Me regreso. Listo. Cotizaciones. Seleccionar cotización. Impedil. Ah, okay. Nos faltó eso. Sí, cierto. Vamos de vuelta. Okay, me parece genial, pero antes de poder hacer la prueba, fíjate que ya hay algún cliente que alte que no puse correo porque eso lo implementamos después. Así que necesito la opción de poder uno, ver mis clientes y dos, editarlos para agregar la información que me haga falta. puedes eh verificar y agregar en el cliente Imperio 3 el correo que te voy a dejar a continuación para que pueda confirmarlo. Gracias. que el correo que es vamos a mandarlo que está evaluando todo. Vale, le pongo pausa para no hacerlo tan largo. Okay, dice, gestión de clientes nueva vista, cliente Imperio 3 actualizado. Probar el flujo. Ahora vamos a ver. Vamos para acá. Estamos aquí. Actualizo. Tengo clientes. Imperio 3. Ya le puse el correo. Perfecto. Quiero ver que lo pueda editar. Muy bien. Le doy guardar. Okay. Aquí hay un detalle. No funciona el botón guardar. Sol. Bueno, a lo mejor no funciona porque no hice ningún cambio. No, si cambio aquí. Okay, entonces para tomar nota de que no funciona el botón guardar. Vamos a cotizaciones Imperio 3. Okay, está escribíelo con IA y enviar correo. Error al guardar registro de correo. Okay. Enviar correo. Rar guardar registro de correo. Okay. Vamos a hacer un cambio. Quiero asegurarme si se ejecutó esto. Okay, le voy a decir. Perfecto, ya lo probé, veo que ya puedo editar. Solo hay un detalle. Cuando intento editar me aparece el botón de cancelar, edición y guardar. El de cancelar funciona, el de guardar no. Por favor, para que lo revises. Segundo punto, cuando le doy al botón de generar, se me olvidó cómo se llamaba, una disculpa. Enviar correo. Me sale error. Guardar registro del correo. Okay. Enviar correo me dice al generar registro de el correo. Verifica eso, por favor. Para confirmar. La idea es que una vez que yo envié el correo, que le dé clic al botón enviar correo, eso haga el trigger de mi workflow de N8N. Así que tienes que mandar todo el payload. Decidí hacer un cambio. Ya no vamos a instalar a la gente en NN porque veo que ya estamos generando el subject y ya estamos generando el cuerpo del correo. Así que lo único que le tienes que mandar a N8N es en el payload es el subject, ¿okay? el body del correo, el email de el cliente y eso es todo. Yo me encargo hacer los cambios ahorita en el N8N. Tú mándalo. Y recuerda que al final el último nodo de N8N, mandamos la respuesta a de vuelta y tenemos que validarla para que aparezca del lado derecho. Hasta que no se valide no tiene que aparecer. Okay. Y vamos a mandar mientras, bueno, antes de tocarlo, quiero ver si él no hace el cambio del workflow, que le pude haber pedido que lo hiciera, pero prefería hacerlo yo. Recuerden que es este es un MVP, es un caso muy simple, digamos, el de enviar un correo podemos ejecutar cosas muchísimo más complejas en el workflow. Así que vamos a ver aquí algo interesante, si se fijaron, eh, me salió algo de su pavé si lo lograron ver rápido. Este decía RCL. Lo más seguro es que como yo le estoy pidiendo que voy a mandar el correo, al mandar el Word en el ejecutar y mandar el payload del correo, estoy exponiendo en la red, digamos, el correo de de los clientes. Entonces, muy probablemente esté viendo si lo tienen que encriptar o qué configuración tengo yo en mi Superabase para poder mandar su información ace failure. Entonces, ahorita vamos a ver lo que nos dice. Okay. Permitir clientes. Check más la lógica. Check verde, email. Es es lo que nos están mandando. Perfecto. Edita los clientes. Dale enviar. Okay. Entonces, vámonos de vuelta en 8N. Vamos al editor. Obviamente esto ya no lo necesito. Sería nada más esto. No debería de funcionar porque no tengo que mapear todavía. Así que vamos a hacer la prueba. Vamos a actualizar. Elijo la cotación que me lo escriba la envío correo. Error en el proceso web por corre 500 message error workflu. Así que se lo voy a enviar. Copio, ya quiero ver si recibí llegó, pero no recibo respuesta. Es correcto. Perfecto. Voy a darle debook to editor. Abro este nodo. El subject ya lo estamos recibiendo, entonces lo quiero mapear. Pam. El correo va a ser dinámico, el body lo estamos recibiendo acá. Okay, aquí va a ser un cambio mínimo, pero si fijan ha llegado el Imperio 3, que es el nombre de la empresa, en lugar de que llegue el nombre del cliente, más para que lo tengamos en cuenta, al ser un MVP, no lo voy a no lo voy a cambiar. Y que le estoy diciendo comin safe publish. No lo voy aar desde aquí ahorita, pero voy a regresar y voy a volver a darle enviar correo el proceso. Vamos a ver qué pasó. Esecuciones. Vamos a ver dónde falló. Gmail. por alguna razón como si no estuviera autenticada este cuenta. Déjenme ver si cambió algo en mis credenciales porque hace poco hice unos cambios y regreso. Okay, ya lo arreglé. Si tenía un problema con mi correo, eh, las credenciales, así que le voy a dar enviar correo otra vez. Y si el proceso no se puede guardar registro historial tras el envío. Eso ya es un error diferente, pero vamos en ejecuciones y veo que si se envió y aquí tenemos un response sent y entonces voy a regresar antigravity y voy a volver a generar una cotización nueva. No sé si algo haya caducado. Vamos a ver aquí el asunto escribir ponía enviar correo. Okay. Y le digo esto. Copio. Aceptar. Regreso. Por favor, revisa la imagen que te mandé. Si se ejecutó mi workflow. Sí se mandó el correo. Sin embargo, hay algú un problema con la respuesta de N8N. Yo la veo satisfactoria, pero por alguna razón no la está recibiendo o está pasando algún error. Por favor, revisa loss. Okay. Dice, "Diagnóstico detallado en errores. Actualizado services para mensaje genérico. Está pasando. Solución de permisos de super lo que decía. Por favor, ejecute este códigoamos. Acá suabaseql editor ya podemos eliminar esto. Pegamos, borremos lo de que sí. Relation exist. Okay. Alter policy. Okay. Voy a tablas. No existe. ¿Sabes qué? Estoy verificando y la tabla emails y bajo sente. Entonces por ahí está el error. Asegúrate de crear la tabla primero o si no te deja dame el código SQL para que yo la cree y de una vez si tengo que crearla yo, dame el resto del código para hacer el RLS. Okay, tienes toda la razón. Aquí está la tabla porque se arregló el error. El código completo. Regresamos al Supase. Editor. Borramos, pegamos, okay, perfecto. Regresamos antigravity. correo de nuevo aparecer historia. Vámonos de nuevo aquí la ejección enviar correo y listo y aparece aquí. Perfecto. Antes de terminar nada más quiero mencionar algo que me di cuenta que estoy cometiendo un eh no un error, sino no siguiendo buenas prácticas. Si nos vamos a nuestro GitHub, podemos ver que el último comit fue el día de ayer y hemos hecho varios cambios. Intenten como buena práctica mandar commits cada que hagan un cambio grande por si algo pasa pueden regresar a ese versión del código anterior o si quieren hacer algún branch. Entonces vamos a hacer dos cosas. Le voy a decir, "Oye, me he dado cuenta que no hemos hecho commits desde ayer. Por favor, haz un comit completo, detallado de todos los cambios que que hemos hecho." Y también necesito que actualizes tu documentación para que cada después cada después de cada cambio relativamente grande hagas un commit actualizando. Si no te queda claro en qué momento tienes que hacer un commit antes de que lo hagas automáticamente, pregúntame si quiero hacer un commit en ese momento. Vamos a enviarlo. Geek status. está actualizando el implementation plan por alguna razón ya lo puedo editar. Next steps. Rules perform after every significant change. Okay. Segundound del comit ya sube 37chillos. Perfecto. Vámonos de nuevo para acá. Actualicemos. Y no ve no veo yo ningún commit, perdón, los comit que hecho el comit. No veo los commit en mi git. ¿Puedes verificar que efectivamente ahí has hecho el comit? Tienes razón no verlo. Ha realizado el comit localmente permit el pushit un error de permisos 483 para usuario local no tiene permisos que por alguna razón me está haciendo un cambio de gitub porque este no es el githop que teníamos conectado. Ah, okay. Vamos para aquí. El git debe ser este. Okay, vamos a MSP Servers. por alguna razón está intentando mandarlo desde una cuenta de Gitcub diferente a la cual no es la que ya había conectado. Okay. Ve un detalle. Estoy viendo que la cuenta desde la cual estás intentando hacer el comit el push no es la cuenta que yo conecté. ¿En qué parte de la configuración puedo cambiar o asegurarme que estemos haciéndolo desde la cuenta correcta? Vamos a ver. me dice esto entre no les lle a pasar a ustedes porque yo estoy cambiando, desinstalando, instalando, cambiando y probando con diferentes githops. Probablemente queda un poco de basura de lo último, o se quedaron eh archivos de configuración anteriores, entonces tengo que hacer el cambio de Gitcop, pero no es algo que les debería estar pasando a ustedes. Voy a poner pausa para no ser muy largo. regreso cuando esté solucionado y terminamos esta parte del video. Okay, listo. Ya estarme peleando juego en GitHub. Digo, es un tema que no les va a pasar a ustedes, un tema de credenciales. Ya lo acabé resolviendo y si nos vamos para acá, ya tengo mi commit de ahorita con todos los cambios que implementamos. Y si nos regresamos al código, aquí va a salir que se cambia ahorita, ahorita, ahorita y todo lo bloque se ha cambiado. Y por aquí deberamos tener un RMI no tiene realidad mucho. Me parece que lo que está actualizando han sido el el PRD, no es de ser mi action plan. H No sé si hay algún git ignore. El ritmi no tenía mucho, pero vamos a hacer una prueba. Puedes actualizar el Ritmi para que refleje de qué se trata este MVP, todo lo que se hace y con las instrucciones de cómo correrlo. A ver si me pregunta de la gente si quiere hacer que hacemos comits. Okay. Los cambios es el ritmo la estructura descripción. ¿Quieres que haga el commit? Perfecto. Gracias por preguntar. Sí. Haz el comit. Comit. Me puse carón. Listo. Vámonos. Aquí regresamos. 3 minutos. Solo cambiamos el BR. Vamos a código. Ah, bueno, algo del commit que si le commit details van a poder ver exactamente lo que se cambió. En este caso fue si nos vamos de vuelta para acá y yo busco mi y me va a salir con todo lo que le pedí. Perfecto. Vamos a dejar el video hasta aquí. M.
