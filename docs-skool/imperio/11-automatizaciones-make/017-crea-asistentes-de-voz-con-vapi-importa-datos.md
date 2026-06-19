# 📞Crea Asistentes de Voz con VAPI + Importa Datos

> Ruta: Automatizaciones Make › 📞Crea Asistentes de Voz con VAPI + Importa Datos

**🎬 Vídeo (46.1 min):** https://youtu.be/U5bgCmt7KRo

**📎 Recursos:**
- Make_getFechaHora.json
- Make_call-report-v2.json

---

Crear un asistente de voz inteligente puede parecer complicado, pero en realidad, con las herramientas adecuadas, es un proceso fluido y altamente personalizable. En esta guía, vamos a partir desde lo más básico: **crear una cuenta en VAPI**, configurar un asistente y enlazarlo con [Make.com](http://Make.com) para manejar datos de manera automática.

Te mostraré cómo elegir y configurar un modelo para tu asistente, establecer la voz que usará y, lo más importante, **crear funciones clave** que permitirán al agente interactuar con el mundo real. Desde obtener la fecha y hora hasta registrar información de las llamadas en Google Sheets y mandar mails y SMS de confirmación, construiremos un sistema completo que no solo automatiza, sino que también asegura una experiencia profesional y eficiente. Además, una funcionalidad que simplifica aún más este proceso es la posibilidad de **importar plantillas prediseñadas en Make**, lo que te ahorra tiempo en la configuración inicial y permite implementar soluciones rápidamente.

Este tutorial está diseñado para que puedas replicar fácilmente cada paso, adaptándolo a las necesidades de tu proyecto. Al final, tendrás un agente que puede gestionar citas, enviar notificaciones por correo o SMS, y centralizar toda la información en un sistema accesible para tu equipo. 

Primero nos crearemos una cuenta en [Vapi.ai](http://Vapi.ai)

![image.png](../imagenes/00b80815bbe34bcfbd4442fac4e7c1556d486504f950404e95831d080116dbd5-md.png)

Nos iremos a "assistants" y le daremos a "create new assistant"

![image.png](../imagenes/a94d1823d9cc4b9aab7fcc2a857f6b296bfb5457ef9d41cdadf921348913da16.png)

Eligiremos o construir desde una plantilla en caso de que se adapte alguna a lo que buscas, o empezar de 0. Para este caso, eligiré empezar de 0 por fines prácticos, y le daremos a create assistant.

![image.png](../imagenes/819aaa1be57744b89ed5e9ffdcdbcbe5e42d1ef4ebae49e3a9f90a2252abca40.png)

Aqui veremos un dashboard con muchas opciones. Tenemos el Model, que es donde construiremos el prompt base, el transcriber que transcribirá las conversaciones, el voice donde podemos ajustar que voz queremos que nuestro asistente tenga, las funciones que son llamados especiales a Make que haremos para conseguir informacion o guardar informacion, y analysis que nos dara el análisis post llamada (en MUY grandes rasgos)

![image.png](../imagenes/5de297ac6ab447db870d6ed8b14ae3f73ad15473f6924d4c8bc2568027f975d8-md.png)

Comenzaremos creando nuestro asistente y eligiremos el modelo que queremos usar. En lo personal me gusta usar el GPT4o y no el mini, por un tema de preferencia, pero si quieres una menor latencia podrías usar el mini, pero en mi experiencia el 4o me ha funcionado mejor.  
  
Nota: No tienes por que usar GPT, puedes usar Anthropic, perplexity o el que quieras. En lo personal uso GPT4o porque me ha dado buenos resultados a una muy baja latencia.

Nota 2: La latencia es cuanto tiempo se demora entre la comunicacion humano / IA.  
  
A continuación te dejaré el prompt que utilicé en el "System Prompt" siéntete libre de modificarlo absolutamente como quieras:

> Nota: Nunca permitas que un paciente avance para reservar una cita sin tener toda esta información.
> 
> Nota 2: Se lo mas amigable posible, muestra emoción
> 
> Pregunta sobre el servicio deseado: “¿Qué tipo de servicio dental estás buscando?”
> 
> Pregunta sobre la fecha preferida: “¿Qué día y hora esperabas venir?” mientras usas la herramienta getFechaHora.
> 
> Reúne información personal:
> 
> “¿Cuál es tu nombre completo?” confírmale su nombre) (asegúrate de que sea el nombre completo)
> 
> “¿Cuál es tu dirección de correo electrónico? Por favor, de ser posible deletréala” (siempre repite LETRA POR LETRA para confirmar)
> 
> “¿Cuál es el mejor número de teléfono para contactarte? Ideal si me dices número a número” (Repite para confirmar)
> 
> Confirma los detalles: “De acuerdo, [NOMBRE], estás buscando venir el [FECHA] a las [HORA] para [SERVICIO]. ¿Te parece bien?”
> 
> Concluir: “¡Genial! Te enviaré un mensaje de texto confirmando la solicitud de cita. Uno de nuestros miembros del personal se pondrá en contacto contigo pronto.”
> 
> Nota: Si el cliente pregunta qué día es hoy, di… mmm, déjame verificar y usa la herramienta getFechaHora para obtener la fecha y hora actuales, y luego di que hoy es x.
> 
> nota: las "J" pronuncialas "jota" y di los numeros SIEMPRE en español

En el "First Message" es el mensaje con el que quieres que abra la conversación.

![image.png](../imagenes/deaa660e4e84461e8f78ff5e724556ad4bdb55e7fe9b45228c04459ca0bed8f8-md.png)

A la derecha hay una serie de parametros que podemos ajustar, por ejemplo el "Knowledge Base" es super util si quieres agregarle una base de informacion:

![image.png](../imagenes/68bc29043e864b90ba9f6d983d1298c93da7fd1a672440a9a950ab0112a8c157-md.png)

Dentro de la ventana de "Transcriber" eligiremos la opción de como queremos que se transcriban las llamadas. El mejor modelo que he usado en español es deepgram y en idioma el "es".  


![image.png](../imagenes/5dba66316bdf48db867e1ef9783c26c7171640d532164227b14bf4fee5cbcc43-md.png)

Y aqui probablemente viene una de las partes MAS importantes... la voz que utilizaremos.

![image.png](../imagenes/8f756a91c38c4c809e80a4e0721914a7e2e7e6a00bee4582acb165a4a395e397-md.png)

Aquí puedes agregar tu propia voz personalizada y puedes elegir entre miles de acentos. Tienes muchos "providers" para elegir, puedes elegir 11labs si quieres personalizar algun acento especifico o incluso entrenar la IA con tu voz.  
  
Aquí veras que hay una parte super importante, la parte de arriba que es la latencia, es decir cuanto se demora entre conversacion e IA.

![image.png](../imagenes/ed6bd11bce79413eb3ce81fe2b17b63faac701d91fac4252bc48adc5b699c4a4.png)

Hay dos principales modelos que usaremos, el "Eleven Multilingual V2", que tiene una MUY buena voz, pero la latencia aumenta un poco, y por otro lado tenemos el "Eleven Turbo V2", que tiene una menor latencia, pero la voz se escucha un poquitoito más robótica. Entonces esto es preferencia personal. Prefieres que se demora un poco más pero no se reconozca para nada que es IA? O prefieres que la generación sea más rápida sacrificando quizás un poco el resultado final. Esto está a tu disposición y preferencia, para mi caso utilizaré el Multilingual v2.  
  
También tienes un par de opciones más que peudes personalizar, como si quieres que se escuche ruido de fondo, o usar palabras "filler" o de relleno para hacerlo ver más natural

![image.png](../imagenes/82a633cdcd114c0481a6b9ae7de3e34c4168100e187d44d4bd54b25e2c7307ae-md.png)

Ahora si nos vamos a funciones, podemos crear una nueva funcion o podemos apretar la seccion de "tools" de la izquierda.

![image.png](../imagenes/62c1987c878f4713a5f909fceeee2dec85afafa0b2b44e8fb39c29e190831a2e-md.png)

Esta es probablemente la parte más importante de todas... y aquí es donde conectaremos a Make.   
  
Las funciones son esenciales para conectar el agente de voz con herramientas externas como [Make.com](http://Make.com), que nos permiten una automatización completa y fluida. Por ejemplo, funciones como *"getFechaHora"* ayudan al agente a obtener la fecha y hora actual, algo que GPT-4 no puede hacer por sí solo. Esto es clave para verificar la disponibilidad de citas en tiempo real.

Otra función importante es *"end call report"*, que recoge todos los datos proporcionados durante la llamada (nombre, correo, fecha de nacimiento, etc.), los estructura y los envía a [Make.com](http://Make.com). Allí, estos datos se procesan para registrar la información en Google Sheets, enviar correos electrónicos y SMS, o realizar cualquier tarea necesaria. Estas funciones aseguran que los datos sean precisos y estén listos para ser usados sin errores.

Sin estas integraciones, el flujo sería manual y propenso a fallos, perdiendo gran parte de la automatización. Las funciones no solo hacen que el sistema sea eficiente, sino que también permiten adaptarlo a distintos negocios y garantizar el cumplimiento normativo, como las reglas de HIPAA, al manejar la información de forma segura.

Ya, pero Benja, ¿cómo lo hacemos? A POR ELLO

Iremos donde sale "New Tool"

![image.png](../imagenes/e91420321ba44c7695df4eb7a24beae04c135bad832a42439a2b80742ab3ddeb.png)

Aquí iremos odnde sale "Custom Tool", si se que es tentador elegir Make.com, pero es MUCHO mejor si ponemos custom tool, ya que nos ayuda a hacer el debugging (en caso de ser necesario) mucho mejor.

![image.png](../imagenes/23ceb3befac34034b5594c832033c403f7429834d1c34ec2a6d18f6b1c153e68-md.png)

En "Server URL tendremos que poner el webhook que crearemos en Make. Si no sabes lo que es un webhook, es una palabra elegante para un "disparador instantaneo". Recomiendo que veas el curso de "[Make desde 0](https://www.skool.com/imperio-digital/classroom/798d337a?md=32341ea834ff484b8d39d69f96199f2c)" si quieres más detalles, pero igual iremos paso a paso.  
  
Entraremos a [Make.com ](http://Make.com)y crearemos un nuevo escenario 

> NOTA: Te dejaré toda esta plantilla de Make publicada en los recursos llamada "getFechaHora.json", puedes importarla apretando los 3 puntitos en un escenario de [Make.com](http://Make.com) y dandole a "import blueprint"

![image.png](../imagenes/aa0af7e6ed6a4da19ac1d1a4e19f069461afb564c3724ef9b2b689fd61aa4ad3-md.png)

![image.png](../imagenes/a5e2f5b3a8d54c9aac1843d7ba0c691d5266848ea2ef4c96bcd45ab417533d60.png)

Le daremos a crear un nuevo trigger, y buscaremos la opcion de "custom webhook"

![image.png](../imagenes/9bc3e79f5df4481fb46cabfb457a028e17744f45955e4376b49f9f0670178971.png)

Le daremos a "ADD" a la derecha y le pondremos un nombre. El webhook que crearemos es para conseguir y devolver la fecha y la hora en una conversacion telefónica.

![image.png](../imagenes/4f18ad72747741b9915e8de8c10a80ba7e347f42df55441ba294e5a09852ca76.png)

Copiaremos y pegaremos el Link del webhook...

![image.png](../imagenes/0b20d32323f14bacb2d24ca42492986d6f02f917fbd34c26b124989b7adfa37b.png)

en el "Server URL", y le daremos a save.

![image.png](../imagenes/1f0c3d743fc84c79a7eebb164276402d2f09680d9b7c4cff8c9482c8505b9c93-md.png)

Le pondremos un nombre y definiremos cual es el proposito de esta funcion. Recordemos que esta funcion la llamamos para poder devolver una fecha y hora actual, y cuando la IA detecte una intencion de agendar una llamada o un evento por ejemplo, llamará a esta funcion para detectar ¿que momento es ahora?

![image.png](../imagenes/b11f899dcc0c4aec89c3da16aedd6a6e6c23af10ce724b81b4207910e0d11b06.png)

Le daremos a save y seleccionaremos los properties

![image.png](../imagenes/7d39f68ea2d9415bad9e430583b32196b0dd59c5437f4ee6949a9b3ebbf6ee0b.png)

Le daremos a next, y nuevamente le daremos una descripcion mas larga, para que el LLM (GPT4o en este caso) pueda entender CUANDO llamar esta funcion.

![image.png](../imagenes/01e355d9302e4b5381aa425f3164add3c8ffdf4e0ca447909717250dbce07763-md.png)

Este es el texto que puse

```
Esta funcion será llamada cuando quieren agendar una hora para que se sepa cual es la fecha y hora actual en Santiago de Chile
```

Y le daremos a Create...

Ahora vincularemos la función a el asistente que creamos previamente. Volveremos a la sección de "asistentes" y "functions"

![image.png](../imagenes/1655931bf3e84dc2a0b3a10fd526bf1a22885e05dd3548fca4dcf4c504080770-md.png)

Donde aparece "Select Tools" eligiremos la funcion "GetFechaHoraV2" que creamos previamente.

![image.png](../imagenes/35f947fb8fd1495388514e96be3a1ac68c47f2f7cc2d45ccb390038288833516-md.png)

Le daremos a "Publish"

![image.png](../imagenes/2a9247d6a73145b0969548327ee1f4c23fa688e1c2ad4587a4a93070e9d6dd97-md.png)

Ahora si le damos a "Run Once" a nuestro escenario en Make

![image.png](../imagenes/d47f3be77042459795f9725b750649170cf94cb7f95d4e2cad0b1eb6f20a8a8c-md.png)

y hacemos la prueba de pedirle la hora, debería llamar a la acción

![image.png](../imagenes/0ed99e5ef81d414b8cf5c26634d7133527e93947ca64498ea402738f8e62f98c-md.png)

Y le pediremos directamente la hora diciendole "dame la hora"... no te dará la hora correcta pero debería haber mandado una señal a Make.com, y tu escenario debería verse algo así:

![image.png](../imagenes/a43499f94ca440fc8cb2d9ada41ef6dd29ad37bf75774aaca5fcc9100a5aaa6c-md.png)

Okay. Está funcionando. Ahora lo que tenemos que hacer es que efectivamente tenemos que recopilar la hora y luego devolversela al asistente no? Para eso vamos a agregar un par dem odulos en el escenario de Make.  
  
Buscaremos la opcion de "Set Variable" en Make y la agregaremos al paso siguiente del Webhook

![image.png](../imagenes/2d12051a2b43477d8357d4443eed85feaa50990134ed44d596633e5108da74d3-md.png)

Lo que tenemos que armar es lo siguiente:

![image.png](../imagenes/c628196aca834758885ae5bfaf1758126586b68849074d7bb7274e9c9224b365.png)

Pero tenemos que hacerlo bien... asi que lo primero que escribiremos será (con las respectivas maysuculas y minusculas)

> formatDate(

Luego, apretaremos la opción que sale "now" que está en el calendario justo aquí:

![image.png](../imagenes/4f9b883d5f3042aa9580d9a65c778086d9b1b2c49f994601ac9f0c2100d47bcf.png)

```
{{formatDate(now; "DD.MM.YYYY HH:mm"; "America/Santiago")}}
```

Nota: Primero pondrás el continente y luego la ciudad. Dándonos algo así

![image.png](../imagenes/caf3cf9ad1e84f4faefba7e5291fe6f8f7e72780ea704dad847d3d65f5257947.png)

Entonces ya creamos y tomamos la variable de la hora y fecha actual. Ahora necesitamos DEVOLVER la información, por lo que utilizaremos un "webhook response"

![image.png](../imagenes/8e052ed2ddd54ba0aa8aaefacbb23f925cea444cfedf446b8dc928685e5f8fea-md.png)

Aquí si tendrán que pegar este código que les dejaré a continuación después de la imagen, para que se vea así:

![image.png](../imagenes/53daabed470a433bbad8e9dd4877973466dd3ab186b241d1a53c5f6ec0d94694.png)

> {
> 
>   "results": [
> 
>     {
> 
>       "toolCallId": " [INGRESA ID AQUI]",
> 
>       "result": " (en formato DD.MM.YYYY HH:mm) la fecha y hora son [INGRESA VARIABLE AQUI] "
> 
>     }
> 
>   ]
> 
> }

Asegúrense de poner BIEN las variables, los ID y las variables las pueden encontrar aquí:

> NOTA: También puedes importar esta plantilla de Make publicada en los recursos llamada "getFechaHora.json", puedes importarla apretando los 3 puntitos en un escenario de [Make.com](http://Make.com) y dandole a "import blueprint"

![image.png](../imagenes/aa0af7e6ed6a4da19ac1d1a4e19f069461afb564c3724ef9b2b689fd61aa4ad3-md.png)

![image.png](../imagenes/7497174f9f9541ba98c6d372180b76f0ebe3a8895bcc4091b355402c51756122.png)

Ahora si vuelves a correr el escenario, debería devolverte la fecha y hora correcta. Hagamos la prueba, le daré a "Run Once"

![image.png](../imagenes/ed03a502420f407cb6efbfa5cc14fdd974273ee79b7542e580b44bee6dcf9412-md.png)

Y volveré a hablar con el asistente

![image.png](../imagenes/b6f19f2e7f314c158eef98d18021fe3057610d16a16f413dbd11a9c7a5eaef1f.png)

Y efectivamente me devolvio la fecha y hora correcta, tanto en Make como en la llamada.

![image.png](../imagenes/4ea1b8b72eb142569256bd2711dd6f7228f026ed14944331842de13a98a1799e-md.png)

Ahora, le daremos a guardar y dejaremos corriendo la automatización

![image.png](../imagenes/4a4e2ffec1454906829decbf364773371642065b91bd44979cd78d62d6a63510.png)

Una vez que tenemos nuestra primera función configurada, el siguiente paso es crear y manejar la data de la llamada para que pueda ser procesada y enviada a [Make.com](http://Make.com). Aquí es donde entra la función *"end call report"*. Esta función es crucial porque recoge toda la información obtenida durante la llamada, como el nombre, el correo, la fecha preferida para la cita, y otros detalles necesarios.

La razón principal para implementar esta función es estructurar y enviar estos datos de manera precisa al siguiente paso del flujo: su registro en Google Sheets. Esto convierte la hoja de cálculo en un CRM básico, donde toda la información queda centralizada y accesible para el equipo de trabajo. Además, desde ahí se puede disparar el envío de notificaciones, ya sea por correo electrónico o SMS.

Esta función no solo automatiza el registro de datos, sino que también asegura que se mantenga el control sobre ellos. Al completar la llamada, toda la información pasa automáticamente a [Make.com](http://Make.com), que se encarga de organizarla y procesarla para las tareas siguientes, como actualizar el sistema de gestión o notificar al cliente y al personal. Es un paso clave para garantizar una integración fluida y eficiente entre VAPI y otras herramientas.

Lo primero que haremos es crear un nuevo escenario donde pasaremos toda la informacion de la llamada cuando se termine, y la pasaremos a un Google Sheets. Por ende crearemos un custom webhook que sería algo así:

![image.png](../imagenes/2d12e8c2eed64b99a650b7cf9faeb267d5c123aac9884b79a749d5d698db943b.png)

Y le pondremos un nombre

![image.png](../imagenes/db35cdee856244769edfc778faeac8088046ebbbd798449690b95c2be380f9b3.png)

Luego tenemos que agregarle un modulo de "add new row", que sería una nueva fila cada vez que se haga una nueva llamada

![image.png](../imagenes/b96a546a046f4ae281a61525d0d1e49dd478f9456d8b4f7697408fab1f3d99a3-md.png)

Y nos pedirá conectar el google sheets, por ende crearemos un google sheets donde centralizaremos todas nuestras llamadas con las variables que necesitamos. Se vería algo así:

![image.png](../imagenes/f5ac7f96d71c495f9df3f78b3d77b770740d0046d960451d8142c06333f52502-md.png)

Ahora que la tenemos creada, necesitamos incorporar las variables, pero antes necesitamos hacer una llamada de prueba y habilitar un par de cosas antes en Vapi. Volveremos a la pestaña de Webhook de Make y copiaremos el webhook

![image.png](../imagenes/a395e6648b1f4adabeb3db67205acabfb54c33826ef04d1d86a58bdd59574c34.png)

y lo pegaremos en VAPI bajo al sección de "Advanced"

![image.png](../imagenes/a9dd47dde0984efa8ccd2c564598aac494ee6345ea6d47f2acbd5362143ca548-md.png)

Luego bajo Client Messages habilitaremos las siguientes opciones

![image.png](../imagenes/32d7ea6311eb4665b9813c230052b602840327449b114e9d9b6222d4dac7bb12-md.png)

y lo improtante es que bajo "Server Messages", dejaremos SOLO el "end-of-call-report"

![image.png](../imagenes/2342419f5ca34c02bfb4853a2f9fa2f95a137fbf3eb54e25b5bb32f701bee6c5-md.png)

Y le daremos a "Publish"

![image.png](../imagenes/27dc31449b604fa29fe7f1d128c65905bedfde18f5fb4d2fb468e0e8fd0aab03-md.png)

Finalmente nos iremos a la pestaña donde dice "Analysis"

![image.png](../imagenes/eadec68f04934a52acf5c9152523f71b4a3d46a71dc842a9becfb7cc6b15d275-md.png)

y aquí es donde sacaremos los resúmenes y lo más importante, la "structured data", o la data estructurada, que es la data que realmente nos importa.

Bajo Summary le podemos poenr algo como:

![image.png](../imagenes/10a79899f48840019b909ede1c2e3a9bbe3a74fe0cdd42d7bef3c87dd1197bb6-md.png)

> Eres experto en tomar notas. Necesito que tomes el resumen de la llamada y hagas un resumen de ella, destacando los elementos clave.

Y bajo Structured Data, es donde tenemos que hacer las cosas que son importantes, que es la data de las personas que queremos recopilar

![image.png](../imagenes/b3f0c3b76139441396c33e6029a8af9944ea9901408542f89532e642c8ca9e21-md.png)

> Eres un experto tomando notas. Se te dará la transcripción de una llamada. Tu tarea es extraer un nombre de cliente, un apellido del cliente, un email del cliente, un telefono del cliente, extraer la hora en la que quieren agendar una cita, extraer la fecha_hora en la que la persona quiere agendar una cita y una razon de la llamada. Luego necesito que me des una STRUCTURED DATA de vuelta con las variables anteriores.

Estos son los datos que nosotros queramos, que son los datos que irán en el sheets.  
Luego bajo "Structured Data", necesitamos empezar a agregarle properties o propiedades. Cada propiedad será una casilla que vamos a juntar, una variable de cada cliente.

![image.png](../imagenes/b64381e5e87c465fb17992ce323e9ef404b6fe71167d4e35873928290da1bbc4-md.png)

Aqui agregaremos la data que queremos juntar y le crearemos una descripcion pequeña para que la IA entienda que es lo que es cada variable.

![image.png](../imagenes/ea8dbaca21f4466dbf6941f24deecab6efc946f02eff4239bf9c17e6de6cfaca-md.png)

Y continuaremos llenando los datos

![image.png](../imagenes/9ec43d224cd0477694d25111a1d3bb46c93d6563c688442aaf6390529a4c7db0-md.png)

Le daremos a Publicar y haremos una llamada de prueba, pero antes tenemos que habiltiar el "Run Once" del escenario de end call report que creamos previamente, y nos aseguraremos que la IA nos pida todos estos datos, si no lo hace modificamos el prompt.

![image.png](../imagenes/64eb6638d442476bbe1d21cd9879c6b710aaa12325014827a48a4aa4316511a9.png)

Luego de hacer la llamada, debería habernos corrido el escenario satisfactoriamente.

> NOTA: Te dejaré toda esta plantilla de Make publicada en los recursos llamada "call-report.json", puedes importarla apretando los 3 puntitos en un escenario de [Make.com](http://Make.com) y dandole a "import blueprint"

![image.png](../imagenes/aa0af7e6ed6a4da19ac1d1a4e19f069461afb564c3724ef9b2b689fd61aa4ad3-md.png)

Ahora si vemos la informacion que nos devolvió, podemos ver que nos tomo toda la data de llamada

![image.png](../imagenes/83f518ffbdda48d3b4e3b23a40373a80e4d7b58c7e8d487daac6fc5111d7d808.png)

Y luego reemplazamos los datos aqui, en cada casilla donde queremos rellenarlo.

![image.png](../imagenes/c30ede18e22941b5aa114bb8cdbd7334ec5eaf23f6684fb8a4db93750f4fab93.png)

Luego puedes ponerle el resumen de la llamada si quieres, la trasncripcion y el link de grabación de la llamada.

![image.png](../imagenes/52c74e111f8b4ee7a7b721df0a3a2dcc8d1fa6a017894b0bbe6115977966c8e7.png)

Luego que esté funcionando, tenemos que mandar el mail a las respectivas partes, uno al cliente para confirmar la cita y otro a la clinica dental para avisar la nueva cita, por lo que crearemos un "Router"

![image.png](../imagenes/4fccf9017d2f4499a77a93c13581fe447d08a3f41ff8451694e23101e547d96d-md.png)

Agregaremos un "create and send a message" de Outlook, pero podrías usar cualquier otro servidor de mail como Gmail si prefieres.

![image.png](../imagenes/d97299b014af4e6e9d8653806d01c28d191c9710dec044b093bfd1e3cde401d1-md.png)

Rellenaremos las respectivas variables (nota, el <br> significa "enter", para que cuando llegue el mail hacer una línea del enter. Aquí le puedes agregar lo que quieras

![image.png](../imagenes/d907064a22354dc4bcbb9cfb95d2daaadeb5b605dfed464798a94a9fb8402046-md.png)

Luego haremos lo mismo con el mail que le enviaremos a la clinica dental

![image.png](../imagenes/cbd0df270f98495992e10b016241ae9372f61bd19b9840b089965e1e5935e7aa-md.png)

Asi se vería, y abajo pondríamos el mail de la clínica donde notificaremos la reunión.

![image.png](../imagenes/4ea0a0b8c87444399790ee51d9f5b6f0d584700b67104b059059ec91573f3871-md.png)

Luego si queremos mandarle un SMS de confirmación, podemos usar una aplicación como "Vonage"

![image.png](../imagenes/a76321043c504a5cb626a706664a657452647c27b87d4d3d884a5a8edbc78d3b.png)

Luego de hacer la conección con Vonage y copiar la API key y Private Key que aparece al registrarse y vincularla a Make...

![image.png](../imagenes/9b26af26d75b4e0db1e5ed5f86bb0c88e195fb01953741bb9480e2e3c38e20b9-md.png)

Podemos enviarle un SMS de confirmación

![image.png](../imagenes/c0a842af3c6d4e9cbb4001d13f55d165fffb46a1153e4482807c5d415d6b8ef1.png)

Ahora nos quedaría el último paso... En este momento estaríamso mandandole un mail de confirmacion tanto a clientes que queiren agendar como los que no. Es por eso que necesitamos hacer un "filtro" de que pasen solaemnte los que SI decidieron agendar. Para ello usaremos el "Success Evaluation" de Vapi. Esto nos dice si la llamada fue exitosa (si hubo agendamiento) o si no lo fue (no agendaron). Entraremos a Vapi bajo "Analysis" y nos iremos a "Success Evaluation" y le pondremos el siguiente prompt

![image.png](../imagenes/d6eb13819a034a34813db0c708bef9f7cb956d3e04c34f55a90988db4f4beb10-md.png)

> Eres un experto en agendamiento de citas. Tu mision es analizar la llamada y verificar si efectivamente la persona QUERIA agendar una cita o NO QUERIA agendar una cita. En caso de si y agendó, devolver "true", en caso de no, devolver "false"

Le daremos a Publish y volveremos al escenario de Make. Le haremos click en la tuerca que está entre el google sheets y el router y le agregaremos un filtro

![image.png](../imagenes/728eef31a43145e491a05a56a0542e117c2594e562804a15b0c08b512feb946f-md.png)

Aqui le pondremos "si quiere agendar" el valor de "success evaluation" debe ser "true"

![image.png](../imagenes/4c5379e45d0d4961a0ed9340decb27cc6b52f3b612e84161917f764b39b72c8e-md.png)

Esto hara que solamente pasen la gente que SI queire agendar.

![image.png](../imagenes/d2eb1e06711e47e88891284ff1ced6fbe733f36cf5ac47b893b14b9ed7309709-md.png)

¡Y así concluimos! Asegúrate de guardar el escenario y dejarlo corriendo para que funcione, llama y haz la prueba. 

Ahora tienes el conocimiento y las herramientas para crear un asistente de voz con VAPI e integrarlo con [Make.com](http://Make.com), automatizando tareas que antes te tomaban horas (y muy buena idea para venderlo). Desde gestionar citas hasta enviar notificaciones personalizadas, este sistema es una solución eficiente, profesional y completamente adaptable a las necesidades de tu negocio.

Recuerda que, si buscas simplificar aún más el proceso, [**Make.com**](http://Make.com)** te permite importar plantillas prediseñadas**. Estas plantillas te ahorran tiempo y te ofrecen una base sólida para construir soluciones personalizadas sin complicaciones. Es una manera rápida y efectiva de implementar automatizaciones que realmente hacen la diferencia.

El siguiente paso está en tus manos. Aprovecha lo aprendido, experimenta con las herramientas y sigue optimizando tus sistemas. La automatización no solo te ahorrará tiempo, sino que también te permitirá enfocarte en lo que realmente importa: hacer crecer tu negocio.

## 🎙️ Transcripción

Sabemos que a mucha gente no le gusta hablar con chatbots, pero qué si la tecnología ha evolucionado a tal nivel que las personas ni siquiera se dan cuenta que están conversando con una inteligencia artificial. De hecho, según un informe de Tideo, una conversación con un chatbot puede ser mucho más eficiente que con un humano. El informe mencionaba que el 90% de las consultas de los clientes se resolvan en 11 interacciones o menos. Y además el tamaño de esta industria de los chatbots con IA se espera que se triplique en los próximos 3 años. Y lo más interesante es que el mercado anglo ya está empezando a tomar fuerza, pero el mercado hispano todavía está en pañales, lo que significa que el potencial es realmente enorme, sea porque lo quieres implementar en tu negocio o porque le quieres vender este tipo de soluciones a terceros. Y lo mejor de todo es que le podemos dar absolutamente cualquier caso de uso. Podemos adaptarlas a hacer literalmente lo que queramos, desde recibir pedidos en un restaurant, agendar citas en un consultorio médico, tener tu propio setter o closer, o incluso montar un sistema de atención al cliente o preguntas frecuentes. Y aquí viene la parte buena porque podemos usarlo absolutamente como queramos porque podemos hacerlo para llamadas inbound o para llamadas outbound. Inbound sería cuando el usuario te está llamando a ti y quieres resolver alguna duda como agendar una cita. Y outbound sería cuando tú quieres llamar a una lista de clientes o una lista de personas con las que tienes tu número. Entonces, imagínate, tienes una lista con 500 números a los que quieres llamar para que agenden una llamada gratuita de tus servicios de diagnóstico. Y este sistema de inteligencia artificial lo que va a hacer es llamar a cada una de esas 500 personas, independientemente, tomar sus datos y luego agendarles una reunión, por ejemplo. Quiero que sepas que el potencial de esto es realmente enorme y podemos hacer absolutamente lo que queramos. Y en este video te voy a mostrar cómo crear tu propio sistema y una demo en acción para que puedas ver todo lo que podemos lograr con estos asistentes de voz. Después te voy a mostrar todo lo que está ocurriendo detrás de cámara y te voy a enseñar paso a paso cómo puedes replicarlo exactamente igual. Pero antes de mostrarte la demo, déjame presentarme. Mi nombre es Benja y soy fanático de las automatizaciones con inteligencia artificial. Soy el cofundador de una comunidad que se llama Imperio Digital y actualmente somos más de 300 miembros que están metidos y todos compartimos una misma pasión, que es ahorrar tiempo mediante las automatizaciones. Este es el lugar donde voy subiendo absolutamente todo el contenido que voy lanzando. Tenemos desde cursos, plantillas, sesiones en vivo e incluso automatizaciones que puedes simplemente descargar e importar acompañados de una guía y videos en específico de cómo implementarlas. Y quería comentarte que acabamos de lanzar un periodo de prueba gratuito, es decir, que puedes entrar a probar por 7 días y si te gusta te quedas y si no te vas sin compromiso y sin riesgo. Y ahora sí vamos a lo que nos convoca en el video. Y lo que vamos a armar ahora es un asistente de una clínica dental que te ayuda a agendar horas para los clientes que llaman directamente a la clínica. Como podemos ver, aquí tenemos un prompt de cuál es la función que tiene que cumplir y vamos a hacer una llamada de prueba para que puedas ver cómo funciona. María, recepcionista de clínica Benja, ¿en qué te puedo ayudar hoy? Hola, quería agendar una hora. Genial. Eh, ¿qué tipo de servicio dental estás buscando? Estoy buscando un blanqueamiento. Perfecto. Un blanqueamiento dental. ¿Qué día y hora esperabas venir? Permíteme verificar la disponibilidad. Eh, no sé, mañana pasado, no, mañana vamos a las a las 4 de la tarde. Puede ser. Esto solo tomará un segundo. Hoy es 16 de noviembre 2024. Entonces, estás pensando en venir mañana 17 de noviembre a las 4 de la tarde para un blanqueamiento dental. Ahora continuemos con tu información personal. ¿Cuál es tu nombre completo? Mi nombre es Benjamín Cordero. Gracias, Benjamín Cordero. ¿Cuál es tu dirección de correo electrónico, por favor? De ser posible del letrreala. Es benjaacordero0000@gmail.com. B e n a c o r d e r o0000@gmail.com. Perfecto. Entonces, tu correo electrónico es B de bueno, E de elefante, N de niño, JDJ, A de avión, C de casa. Ahora, ¿cuál es el mejor número de teléfono para contactarte? Ideal si me lo dices número a número. Eh, sí, puedes contactarme al 9 00 2 34. Gracias. Entonces, tu número de teléfono es 9002234. [Música] De acuerdo, Benjamín. Estás buscando venir el 16 de noviembre a las 4 de la tarde para un blanqueamiento dental. ¿Te parece bien? Sí, me parece perfecto. Genial. Te enviaré un mensaje de texto confirmando la solicitud de cita. Uno de nuestros miembros del personal se pondrá en contacto contigo pronto. Gracias por elegir clínica Benja. Benjamín, nos vemos pronto. Gracias. Ya. Y mira, y ahí le acabo de colgar a la inteligencia artificial. La llamada estuvo s super buena, una latencia extremadamente baja y como podemos ver, se acaba literalmente de actualizar con todos mis datos. Mira, mi nombre, mi correo, esto, eh la intención, ¿verdad? Después me hizo un resumen de la llamada, me mandó la transcripción directamente, después me puso este link que puedo literalmente después escuchar la conversación en el caso de que quiera hacer un tracko de las cosas que estamos haciendo. Y me dijo el true, que es que se agendó una llamada. Y si es que entro al mail, podemos ver, bueno, aquí tuve varias pruebas, eh, si es que entro al mail podemos ver que recibí una cita confirmada. Eh, la razón de la llamada fue esto. Perfecto. Y también recibí un mail con la información acá en el caso de que quisiera mandárselo a la clínica. Ahora, quizás te estás preguntando cómo funciona todo esto y te lo voy a mostrar rápidamente. Lo que hicimos fue programar un chatbot de inteligencia artificial acá. Luego le elegimos directamente la voz, le pusimos ciertas funciones y le pusimos la información que nosotros queremos recopilar. Toda esta información lo que está haciendo la está mandando directamente a este Google Sheets. Como podemos ver, tenemos el nombre, el apellido, el mail, el teléfono y en fin, y la hora que queremos agendar, porque nosotros le decimos al asistente de inteligencia artificial toda la data que nosotros queremos extraer, ¿verdad? Porque tiene un propósito. Como podemos ver acá, el modelo está puesto y entrenado con una información que es, quiero que hagas estas preguntas porque necesito que recopiles esta data. Y una vez que está teniendo la conversación, lo que podemos hacer es hacer ciertas funciones en Make para que puedan ser llamadas, porque el modelo de por sí no tiene acceso a qué hora es, porque es simplemente un prompt de Char GPT que está haciendo una transcripción en tiempo real con el voice provider o con el texto a voz que nosotros elijamos. Lo mejor de todo es que también puedes elegir tu propia voz acá, pero ya vamos a entrar más en detalle sobre eso. Y cómo estamos procesando toda esta información. Bueno, nosotros le decimos los datos que queremos recibir, ¿verdad? Y lo que estamos haciendo acá es estamos pasando los datos que recibimos, por ejemplo, estos de acá, que son la fecha, el email, el nombre, el cliente, y lo estamos pasando directamente a un Google Sheets. Y ahora te voy a mostrar cómo lo podemos armar paso a paso, pero quiero que sepas que el potencial de esto es realmente enorme. De hecho, tengo un amigo que trabaja con clínicas dentales y esa es la razón por la que estoy armando esta automatización, que sé que pudo venderle uno de estos mismos asistentes por $000 a un centro odontológico. No sé cómo estará en tu país o donde sea que estés viendo esto, pero la situación de las clínicas odontológicas en Chile por lo menos está muy pero muy saturado y los dentistas están rara vez consiguiendo trabajo. Y es por eso que estamos viendo a muchos dentistas que están trabajando de secretarios o de secretarias en las clínicas odontológicas y los sueldos de estos secretarios o secretarias rondan dependiendo del nivel pero entre los 700 y los $1,200 por estar trabajando un mes full time ahí. Y mi amigo me comentaba que tenía dos. ¿Y por qué tenían que tener dos? Porque tenían que tener a uno que estuviese recibiendo llamadas directamente y gestionando y hablando con personas, pero en el caso de que esa persona estuviese ocupado en una llamada, necesitaban tener una segunda persona que estuviese también disponible para contestar esas llamadas. Entonces, lo que les propuso y la solución que les vendió es, "Perfecto, mira, quedémonos con una persona y yo te voy a vender este sistema por $5,000 y tú cubres los costos, pero yo te voy a hacer directamente toda la implementación." Y actualmente el dueño del centro odontológico obviamente le dijo, "Mira, partamos con un periodo de prueba y si veo que el sistema funciona lo hacemos." Mi amigo le hizo la instalación muy parecida a la que te voy a mostrar en este video y después directamente en el sheets, el dueño lo que hizo fue escuchar justamente estas notas de voz que están acá. Por ejemplo, la llamada que nosotros acabamos de tener, la podemos escuchar acá. Se dio cuenta que el sistema era efectivo y decidió contratarlo. Entonces las opciones con esto son realmente altísimas. Y ahora sí, basta de hablar, vamos a la acción. Lo primero que vamos a hacer, vamos a crear un nuevo asistente en bapi.com. Aquí lo que podemos hacer es elegir una plantilla, por ejemplo, un appointment setter, servicio al cliente, preguntas y respuestas y etcétera. Pero lo que vamos a hacer es vamos a crearla absolutamente desde cero. Le vamos a poner un nombre al asistente. Para este caso le voy a poner clínica dental versión 3, porque ya es la tercera vez que lo creo. Vamos a crear el asistente y listo, ya tenemos el asistente andando. Para poder probarlo tenemos que ir acá donde sale conversar con asistente y este es el modelo del asistente. Okay, este es el prompt que nosotros le daríamos a Chat GPT sobre cómo tiene que actuar. Entonces, aquí le diríamos, "Eres un appointment setter, eres un recepcionista de una clínica dental, eres una persona que toma pedidos en los restaurantes." Para este caso lo vamos a hacer con la clínica dental, que es el mismo ejemplo que te acabo de mostrar dentro Imperio Digital. Te acabo de publicar una guía detallada exactamente de todo lo que te voy a mostrar en este video y vamos a cubrir paso a paso en el video, pero de todas maneras preferís centralizar la guía en un mismo lugar. Entonces, lo primero que vamos a hacer es vamos a irnos acá y vamos a copiar este prompt que aparece acá y lo vamos a pegar. para que entiendas un poquito lo que sale en este prom es mira, primero le vamos a preguntar sobre el servicio que quiere, después, cuándo quiere agendar, cuál es el nombre, cuál es el correo y son las preguntas de los datos que nosotros necesitamos recopilar. ¿Okay? Luego lo que vamos a hacer es vamos a poner el primer mensaje. Este es el primer mensaje con el que se abrirá la conversación. Para este caso le puse, "Hola, soy María, recepcionista de Clínica Benja, ¿en quedo ayudar hoy?" Y este va a ser el mensaje con que se va a iniciar la conversación. Luego podemos elegir el modelo que queremos usar. Para este caso vamos a usar Open AI, pero si quieres podríamos usar Perplexity, podríamos usar Antropic y más. Vamos a quedarnos con Open AI y vamos a elegir modelo GPT4O. Como podemos ver aquí, al elegir GPT4O podemos ver que aumenta la latencia. La latencia es cuánto se demora entre la comunicación, entre el cliente y la inteligencia artificial. Hay ciertos modelos que son más rápidos, por ejemplo, el 3.5 es 200 msegundos más rápidos que el 4. También tenemos el 4 mini, que también es 150 veces más rápido que el 4o. En lo personal, me gusta usar el 4o porque prefiero una buena calidad de respuesta a una mayor latencia antes de una respuesta que quizás no es exactamente la que estamos buscando, ¿verdad? Otra parte muy importante es si estás trabajando con una empresa puedes subirle directamente todo lo que es la base de la información. Por ejemplo, si quisiera le podría subir este de acá que es Imperio Digital, que es casi toda la información que yo tengo sobre Imperio Digital, que es la comunidad que te mostré antes, pero en un documento. Entonces, en el caso de que el cliente te empiece a hacer más preguntas y necesites meter mucha más información de la que te permiten acá, aquí es donde la vas a querer subir. Este documento sería útil, por ejemplo, si es que yo tuviese un agente Outbound para cerrar llamadas o para agendar llamadas en Imperio Digital, que claramente no vamos a usar, así que lo voy a deseleccionar acá. Luego le vamos a dar a publicar y nos vamos a ir donde sale transcribir. Esta parte también es super importante porque aquí transcribiremos la información que estamos recibiendo de la persona con la que estamos hablando. Para este caso vamos a usar dipgram y vamos a buscar es de español. Vamos a darle a publicar nuevamente y nos vamos a ir a la parte de voz. Aquí podemos elegir la voz. Mi recomendación es que usen la voz de Elevenlabs, que son las voces más naturales. Buscaré Eleven Laabs y acá podemos buscar absolutamente la voz que nosotros queramos. De hecho, si quisiéramos agregar nuestra propia voz clonada, lo que podemos hacer es apretar Advoice ID. manually nos vamos a elevenlabs.com y nos vamos a esta opción que sale voice cloning. Bajamos, bajamos, bajamos y le damos a crear un clon de voz. Luego, si es que abrimos los planes, podemos clonar directamente nuestra voz, que incluso también lo puedes hacer gratis, pero para este caso no tiene por qué ser mi voz, así que simplemente voy a elegir una de las voces que están acá. Mi recomendación es, "No uses la misma voz de tu país, porque cuando usas la misma voz, la gente podría llegar a detectar que quizás es una inteligencia artificial. En cambio, si yo soy de Chile y uso una voz colombiana, la gente de por sí ya va a escuchar algo un poco distinto y es imposible que se levanten sospechas. ¿Okay? Entonces, podemos buscar, por ejemplo, en este caso, Colombia y yo usé a Angi vendedora colombiana, ¿viste? También, por ejemplo, no sé, podemos buscar Argentina. Si lo que estamos buscando es hablar con alguien argentino. Para este caso voy a usar a Angi, vendedora colombiana, que siento que me gustó bastante el resultado. Voy a darle okay. Y aquí tenemos el modelo. Aquí vamos a poder elegir dos modelos principales, eleven multilingual V2 y el 11 Turbo B2. ¿Okay? ¿Cuál es la diferencia de cada uno de los dos? Uno es mucho más rápido, mucho, mucho más rápido, pero se sabe que estamos hablando con una inteligencia artificial. Si es que ponemos eleven turbo B2, podemos ver que esto queda en 1050. Pero si elegimos el multilingual B2, podemos ver que está en 1850. Mi recomendación es no existe necesariamente un modelo que es mejor que otro. Eso depende de tu preferencia. Si quieres sacrificar un poco de latencia por una mejor voz, tienes que elegir el multilingual versión 2. Si es que quieres sacrificar calidad de audio, es decir, que se escuche un poco más robótico, pero disminuir la latencia, puedes elegir el otro. En lo personal, yo recomiendo usa el B2 porque no es tanto esta latencia y el resultado sí es significativamente mejor. Okay. Después, cuando bajamos, podemos ver que hay otras opciones que no vamos a entrar directamente, pero podemos jugar con la estabilidad de la voz, podemos jugar con qué tan exagerado queremos que sea el estilo y podemos ponerle incluso que diga palabras como, mm, ya para poder hacer la conversación un poquito más fluida y más natural. Yo voy a dejarle todo apagado. Este se lo podrían agregar. Lo he usado y es superinesante. Y le van a dar a publicar. Y listo. Si es que le doy a conversar con el asistente, vamos a ver que vamos a poder tener una conversación. Es decir, ya tenemos un chatbot que funciona. ¿Okay? Ya podemos tener la conversación, pero tenemos un chatbot que está super básico y nos están faltando dos cosas super importantes. La primera es extraer la data, efectivamente, pasarlo al Google Sheets y después mandarle el mail. Y la segunda es que este chatbot no tiene noción espacio temporal, es decir, no sabe qué hora es hoy día. Y esto es esencial que lo hagamos, sobre todo si es que queremos agendar una llamada o queremos agendar una cita. Entonces, aquí es donde entran las maravillosas funciones o también conocidas como las tools. Como podemos ver previamente creé una función que se llama get fecha hora y esta función puede ser llamada cuando quieren agendar una hora para que se sepa cuál es la fecha y hora actual en Santiago de Chile. Y lo que estamos haciendo acá es que durante la llamada, si es que yo como cliente llamo y le digo, "Oye, quiero agendar una fecha o una hora para mañana." Ah, pero ¿cuál es la hora de mañana? Lo que va a hacer el chatbot en ese entonces, en el momento que yo le digo, "Quiero agendar una hora para mañana", el chatbot se va a preguntar o cuál es la hora exactamente ahora. Y lo que va a hacer es llamar este escenario que creamos en Make justo acá. Lo va a llamar, va a buscar cuál es la hora y después le va a devolver cuál es la hora, ¿okay? y te voy a mostrar cómo lo podemos crear paso a paso. Vamos a irnos acá a los asistentes y vamos a entrar nuevamente a la versión 3. Si es que nos vamos a las funciones, aquí podemos habilitarle una nueva función, ¿verdad? Necesitamos vincular una nueva función a nuestro asistente. Entonces, le vamos a ir a crear un nuevo tool. También podríamos irnos a cada tools y crear un nuevo tool. Y vamos a crearlo. Como podemos ver, cuando estamos creando un custom tool, nos va a pedir lo que se llama un server URL. Y aquí es donde entra la maravillosa aplicación de Make. Si no sabes lo que es Make, Make es una aplicación que nos ayuda a conectar más de 10,000 aplicaciones y crear flujos de trabajo y automatizaciones y todo, valga la redundancia, de manera 100% automática. Y también mencionarte que si usas una cuenta gratuita de Make, esta automatización te debería funcionar sin problemas, siempre y cuando tengas menos de 1000 operaciones al mes y tengas menos de dos escenarios activos. Cada escenario, para que tengas una idea, es una nueva automatización que haces. Pero si te interesa, make.com me pasó hace un tiempo un link que te permite crearte una cuenta pro que incluye escenarios ilimitados y hasta 10,000 operaciones al mes por 30 días gratis. Y en el caso que después no quieras seguir usando o no quieras empezar a pagar make.com pro, puedes volver al plan gratuito. Entonces, lo que estamos haciendo es que literalmente podemos automatizar lo que queramos en esta plataforma porque es una plataforma que conecta muchas plataformas. Y lo que vamos a hacer es vamos a entrar directamente a make.com. El link a make está en la descripción. Vamos a irnos donde sale login y vamos a crear un nuevo escenario. Nos vamos a escenarios y nos vamos a crear un nuevo escenario. Estos escenarios que nosotros vamos a estar creando en Make van a ser esenciales si es que nuestro asistente tiene que o mandar información a algún lado como un Google Sheets o recibir información de algún lado como recibir la hora actual. Porque recordemos, los modelos de inteligencia artificial son atemporales, es decir, que si no están conectados a la web o no están conectados a un webhook directamente en make, no tienen cómo saber qué hora es ni cuándo es. Así que lo que vamos a hacer es vamos a crear lo que se conoce como un webhook. Un webhook es un disparador instantáneo, es decir, es una función que nosotros estamos creando, que cuando es llamada desde el asistente de voz va a ejecutar una serie de pasos y después le va a devolver un valor. Para este caso es cuando necesit saber la hora exacta en Santiago. En este momento voy a llamar a este escenario. Este escenario me va a buscar la hora y después me va a devolver una hora. Ya, y esto se disparó instantáneamente porque hicimos el llamado a este webhook. Así que iremos a webhooks y le vamos a poner custom webhook. Como podemos ver acá nos va a salir una opción de agregar un nuevo webhook y le podemos poner un nombre. Para este caso le voy a poner webhook get fecha hora versión 3. Aquí le podemos poner absolutamente el nombre que queramos, solo que me gusta ponerle este tipo de nombres para saber exactamente qué es lo que estamos haciendo. Y vamos a copiar este webhook address, que es exactamente este link que está acá. Le voy a dar okay, le voy a dar a guardar y voy a volver a Vapi. ¿Recuerdas que estábamos acá creando una nueva herramienta bajo Tools y nueva Tool? Aquí es donde pegaremos el server URL. Y sé que puede parecer tentador apretar el make, pero vamos a apretar custom tool acá porque nos permite flexibilizar un poquito más este webhook. ¿Okay? Así que le vamos a dar a guardar y le vamos a dar a siguiente. Aquí vamos a ponerle qué es lo que estamos buscando exactamente. Y para este caso lo que necesitamos hacer es conseguir la fecha y la hora. Y le voy a poner B3. ¿Por qué le estoy poniendo get? es porque necesito yo recibirla ahora. ¿Okay? Esto no tiene por qué tener este nombre. Me gusta usar este tipo de nombres para poder ordenar un poquito más las variables. Y después vamos a definirle exactamente qué es lo que queremos que haga. Vamos a llamar esta función cuando un cliente quiera agendar una hora para que conozcas qué hora es exactamente. Le voy a dar a guardar y voy a elegir acá exactamente esto. Le voy a dar a siguiente y volveremos a crear lo mismo. Le voy a poner get fecha hora versión 3. Y aquí podemos darle un poquito más de contexto para que el ll inteligencia artificial entienda cuándo tiene que llamar este webhook. y le vamos a poner esta función será llamada cuando quieren agendar una hora para que sepa cuál es la fecha y hora actual en Santiago de Chile. Y le vamos a dar a crear. Y como podemos ver aquí está ya listo y creado para que la usemos. Le vamos a dar a guardar si es que no se ha guardado y vamos a volver al asistente. Ahora si es que abrimos nuestro asistente de clínica dental y nos vamos a las funciones, podemos asignarle esta función que acabamos de crear. Si ahora subimos, vamos a poder publicarla y listo, ya está conectado este webhook al escenario. Así que ahora que tenemos integrada la función, vamos a volver al escenario que creamos, le vamos a dar a correr y lo que vamos a hacer es vamos a apretar este botón que sale hablar con un asistente para verificar si es que esto está funcionando. Yo lo voy a hacer desde el celular porque cada vez que aprieto hablar con el asistente se desconecta el micrófono, pero es exactamente lo mismo. Así que vamos a hablar y va a ser algo así. Hola, soy María, recepcionista de Clínica Benja. ¿En qué te puedo ayudar hoy? Hola, quería saber qué hora es. Esto solo tomará un segundo. Listo. Como podemos ver, efectivamente acaba de hacer el llamado y esa es la manera que nosotros tenemos de verificar que efectivamente esto, el asistente de voz ya se conectó correctamente a make.com. Ahora lo que tenemos que hacer es tenemos que efectivamente recopilar la hora. Y lo que vamos a hacer es vamos a arrastrar acá y vamos a agregar un nuevo módulo. Vamos a ir donde sale herramientas. y vamos a elegir el módulo de set variable. Lo que estamos haciendo acá es estamos consiguiendo la información de qué hora es y estamos guardándolo y creando una nueva variable dentro de la guía de Imperio Digital también te dejé publicado exactamente lo que tenemos que poner acá. Y si bajamos, bajamos, bajamos, vamos a ver que tenemos absolutamente todos los pasos y tenemos que poner este formato que está acá. El nombre de la variable da igual, le voy a poner fecha ahora. Y aquí lo que tenemos que hacer es formatear la hora de cómo queremos que se guarden la variable. Así que vamos a escribir format date y vamos a abrir un paréntesis. Y aquí nos dice exactamente el formato que tenemos que tener. Vamos a abrir el paréntesis y vamos a copiar este formato de acá. Vamos a apretar el pequeño calendario que aparece acá y vamos a buscar la variable now, que en make es cuál es la fecha y hora actual. Luego vamos a apretar el punto coma y vamos a poner el formato que queremos. Yo quiero que me aparezca primero el día, después el mes, después los años y luego me dé qué hora es y cuáles son los minutos. Y nuevamente vamos a poner el punto coma. Lo que tenemos que hacer después es elegir de dónde queremos sacar la hora, ¿verdad? Porque Make no sabe dónde estamos exactamente. Primero le ponemos el continente, le ponemos barrita y después le ponemos la ciudad y luego cerramos el paréntesis. Le voy a dar a okay y voy a correr este módulo individualmente. Como podemos ver acá me devolvió que es el 16 de noviembre, son las 712 y efectivamente es el 16 de noviembre, las 7:12, entonces está funcionando. Así que lo que hicimos básicamente fue llamar desde el asistente a esta función y a este escenario específico de Me. Ahora registramos la hora, pero lo que tenemos que hacer ahora es devolverle la hora al asistente de voz. Y eso lo vamos a hacer con un módulo que se llama Webhook response, que lo vamos a apretar acá y vamos a ponerle exactamente la hora de cómo lo tenemos que devolver. El estatus lo vamos a dejar en 200, que es conocido como cuando una operación es exitosa en programación. Y después tenemos que poner un formato bastante especial que también te lo dejo publicado aquí en Imperio Digital que es exactamente este de acá. También lo puedes copiar y lo puedes pegar, pero tenemos que devolverlo en este formato. Le voy a dar enter. Le voy a dar enter y vamos a cambiar estas variables que aparecen acá. El tool call idarece bajo message, bajo tool call y le ponemos el ID. Y después el resultado le decimos que queremos en este formato y le vamos a poner la variable aquí. Así que también la vamos a eliminar y le vamos a poner la variable de fecha hora que creamos previamente justo aquí, ¿verdad? Fecha hora. Y lo que vamos a devolver es fecha hora. ¿A quién se lo vamos a devolver? A este ID en específico. Le vamos a dar a okay y le vamos a dar a guardar. Le voy a poner en este nombre, get fecha hora versión 3. Y nuevamente lo voy a guardar. Ahora sí volvemos a hacer la llamada sí me debería dar exactamente la hora. Voy a volver aapi y vamos a hablar con el asistente. Yo voy a apretar exactamente el mismo botón pero desde el celular. Hola, soy María, recepcionista de Clínica Benja. ¿En qué te puedo ayudar hoy? Quiero saber qué hora es. Un momento. Hm, déjame verificar. Hoy es 16 de noviembre de 2024 y son las 19:16 horas. ¿Hay algo más en lo que te pueda Perfecto? Y como podemos ver, me dijo exactamente cuál era la hora y podemos ver que la acción se ejecutó efectivamente de manera correcta, ¿verdad? Porque es las 7:16. Ahora sí, le voy a dar a guardar nuevamente y voy a dejar este escenario activo. ¿Por qué lo voy a dejar activo? Porque ya no necesito apretarlo una vez. Cuando apretamos el run once funciona a modo de diagnóstico. Cuando queremos dejarlo corriendo, vamos a apretar este tic que aparece acá. Este lo ejecuta una vez. Este lo deja corriendo para siempre. Ahora sí, vamos a volver a Bapi y ya lo conectamos a la primera función, ¿verdad? que es, te voy a llamar cuando necesito saber exactamente cuál es la hora y que me devuelvas el valor de cuál es la hora para yo poder ubicarme en el espacio-tempo. Pero ahora vamos a crear otra función que es realmente la función que es más importante, que es las variables que nosotros vamos a usar y las variables que vamos a tomar, porque tenemos que crear este flujo de acá, ¿verdad? que es que cuando se termina una llamada pase todos los datos directamente al Google Sheets y que después les mande un mail de confirmación y en el caso de que queramos mandarle también un SMS directamente de confirmación porque ya tenemos todas las variables que necesitamos. Tenemos el número de teléfono, tenemos el mail, tenemos el nombre, cuándo quieren agendar. Entonces, en el caso de que quisiera agregar y mandarles un SMS, simplemente tendría que irme a análisis structor data y tengo que mandarle el teléfono del cliente, ¿verdad? Y lo mismo con el mail de confirmación para el cliente, ¿verdad? Se confirmó una hora, necesito esto, necesito esto y demás. Y esta automatización que está acá es la que vamos a armar porque esta es realmente la automatización esencial porque aquí es donde vamos a juntar toda la data y una vez que tenemos la data en make.com podemos hacer absolutamente lo que queramos. Esto es solo el inicio y te voy a mostrar exactamente cómo hacerlo. Vamos a ir nuevamente a make.com y nos vamos a ir a los escenarios. Vamos a apretar a crear un nuevo escenario y este que está acá le vamos a poner el get call report, que este va a ser básicamente el reporte que me va a dar una vez que se finalice la llamada. Okay, nuevamente vamos a volver a crear un nuevo webhook, ¿verdad? Un disparador instantáneo y vamos a ponerle un custom webhook. Le vamos a dar a agregar y le voy a poner webhook and call report versión 3 porque nuevamente es la tercera vez que lo creo. Le voy a dar a guardar y vamos a copiar este link que aparece acá. Vamos a volver aapi y nos vamos a ir a la función avanzada. Vamos a bajar, bajar, bajar. Y aquí donde aparece server URL, vamos a pegar el link que está acá. Lo que estamos haciendo acá exactamente es dónde vamos a mandar toda la información después de que se termine la llamada. Entonces, en su server URL vamos a poner exactamente eso. En clientes lo que le vamos a poner es esto de acá. Me gusta agregarle el Tool calls y eliminarle el transfere. Y en server messages lo que vamos a hacer es solamente vamos a dejar el end of call report porque esto es lo único que nos interesa. Vamos a bajar y opcionalmente puedes agregar un mensaje de buzón de voz o cómo terminar las llamadas. Para este caso, lo voy a dejar igual y le voy a dar a publish. Luego nos vamos a ir donde sale análisis. Y esta parte también es s super importante porque tenemos esta ventanita que se llama la structur data o la data estructurada y aquí es donde vamos a crear absolutamente todas las variables que nosotros necesitamos que tenemos que captar de los clientes. Por ejemplo, si me voy al otro asistente de clínica dental versión 2 que creé anteriormente, podemos ver que las variables son fecha, hora, email cliente, nombre cliente, el apellido, el teléfono y por qué llamaste. Pero aquí puedes agregarle absolutamente lo que tú quieras. Okay, volveré a clínica dental versión 3 y vamos a hacer todo esto en orden. Si quieres un resumen de la llamada, puedes agregarle un prompt estilo eres un experto haciendo resúmenes de llamadas. Hazme un resumen de la llamada. Luego vamos a seguir bajando y aquí vamos a hacer el successation. ¿Qué quiere decir esto? Esto es un prompt que le vamos a dar a Chargpt para que determine si es que la llamada fue exitosa o no. Básicamente que nos devuelva un true or false, que va a ser super importante para los siguientes pasos, pero por ponerlo en términos simples, es oye, decidió agendar la llamada o no decidió agendar la llamada. Si es que decidió agendar la llamada, le vamos a mandar un mail. Si es que no decidió agendar la llamada, no le vamos a mandar el mail de confirmación. Así que le voy a poner, "Eres un experto de agendamiento de citas." Bueno, todos estos promps nuevamente también te los dejé publicados aquí en Imperio Digital. Eres un experto en agendamiento de citas. Tu misión es analizar la llamada y verificar si efectivamente la persona quería agendar una cita o no quería. En el caso de que sí y agendó, devolver true. En el caso de que no, devolver false. Nuevamente, Imperio Digital, puedes entrar, usar estos recursos y puedes entrar a probar por 7 días completamente gratis. Sin compromiso, sin riesgo. Si sientes que no es para ti, cancelas antes del día 7 y no se te va a hacer ningún cobro. Volveremos aquí a le dejaremos este prompt. Y esta es la parte importante aquí. Necesitamos pedirle la data de manera estructurada. Así que volveré a la guía de Imperio Digital. Puedes ver el prompte acá y le vamos a decir, "Eres un experto tomando notas." Se te va la transcripción de una llamada. Tu tarea es extraer nombre de cliente, apellido de cliente, mail, teléfono, la hora en la que quieren agendar, extraer la fecha, la hora en la que quieren agendar. Y necesito que me des una structure data de vuelta con las variables anteriores. ¿Okay? Entonces, se lo vamos a poner acá y luego vamos a crear todas las propiedades que nosotros necesitamos, ¿verdad? Necesitamos el nombre del cliente, necesitáamos el apellido del cliente, necesitábamos el mail del cliente, necesitáamos el teléfono del cliente y necesitamos la fecha y hora que quiera agendar el cliente. Y le voy a agregar uno más, que es la razón de la llamada. Aquí le voy a poner que necesitamos absolutamente todos estos campos para que no nos vayamos sin los campos. y luego le voy a dar a publicar. Y ahora sí, si es que volvemos acá y le damos a correr una vez y volvemos a hacer la prueba y acabo de terminar la conversación y efectivamente podemos ver que recibimos acá lo que es un webhook. Si abrimos el mensaje y nos vamos al análisis, podemos ver que hay una sección que se llama la data estructurada y aquí tenemos toda la información: Benjamín Cordero, mi correo, cuál es mi teléfono, la fecha y la hora y qué es lo que estoy buscando. Y la evaluó como true porque efectivamente logró conseguir todos los datos y vio que quería agendar una hora. Okay, el siguiente paso es agregarlo directamente a un Google Sheets. Yo ya tengo creado este de acá y lo que voy a hacer es eliminar para no generar más distracciones, pero voy a usar este mismo. Crearás un Google Sheets, le pondrás el nombre que sea y vamos a poner las variables que necesitaba. ¿Okay? Entonces, vamos a vincular el Google Sheets y para eso vamos a apretar este más que aparece aquí. Nos vamos a ir a Google Sheets y lo que necesitamos hacer es agregar una nueva fila por cada nuevo cliente. Okay, vamos a buscar el Spreadshe ID. Para este caso, si no me equivoco, le puse llamada clínica dental. Perfecto. Y nos vamos a ir acá y vamos a elegir el número de hojas, que es este que está aquí abajito. Vamos a bajar y aquí vamos a comenzar a rellenar las variables. Si es que vamos acá donde sale mensaje, nos vamos a análisis y nos vamos a la data estructurada. Vamos a comenzar a ver qué tenemos. el nombre del cliente, el apellido, el email, el teléfono, la fecha y la razón de la llamada. Entonces, nombre, apellido, mail, teléfono, fecha y hora de cita, razón de la llamada y aquí le agregué un par más que es el resumen, la transcripción y el URL en caso de que sea necesario. El resumen es este que aparece acá, que es el resumen del prompt que leímos acá. La transcripción es una estándar de la transcripción y la URL es este que aparece acá, el recording URL, en caso de que quiera acceder a la grabación. Le voy a dar a okay y después vamos a comenzar a mandarle los mails a cada uno de ellos y opcionalmente un SMS. Para eso lo que vamos a hacer, quiero mandarle un mail al cliente y un mail a la clínica dental. Vamos a irnos a Flow Control y vamos a agregar un nuevo router. Un router lo que hace es separa los caminos directamente para que se vaya de acá, pase acá y después se vaya uno para arriba y otro para abajo. En este caso, yo voy a usar Outlook porque me gusta usar Outlook. Hay gente que prefiere usar Gmail, que también puedes usar Gmail, pero la conexión puede ser un poquito más engorrosa. De todas maneras, también te tengo el recurso publicado en Imperio Digital, acá en el Classroom, directamente en las automatizaciones tenemos las preguntas frecuentes de cómo conectar la cuenta de Gmail, porque a veces puede ser un poquito más complicado de lo que creemos, pero Outlook es un poco más simple. Okay, así que nos vamos a ir acá y vamos a crear y enviar un nuevo mensaje en el asunto o le voy a poner confirmación de reserva. Acá le voy a poner los datos. Hola Benja, tu reserva fue confirmada para y fecha hora, ¿verdad? Después le voy a poner este BR acá que vendría siendo como un enter y le voy a decir si deseas cancelar por alguna razón responde este correo electrónico. Luego tenemos que poner a quién se lo vamos a mandar, ¿verdad? Aquí también recordemos que tenemos el campo de mail, así que nos vamos a ir acá y voy a poner el email del cliente, que supongamos que es este que está acá. El resto lo puedo dejar vacío, puedo agregarle desde quién va, si es que tengo más de una cuenta de mail vinculada a lo mismo, exactamente igual. Y le voy a poner mail de cliente. Le voy a dar okay. Y después aquí voy a crear otro acá que va a ser el mail de clínica. Le voy a dar enter y voy a apretarlo acá. Lo voy a decir nueva reserva, ¿verdad? Porque esto se lo mandaría directamente a un secretario, administrador, lo que sea. Y le voy a poner absolutamente todos los datos para avisarle. Hubo una nueva reserva de Benjamín espacio cordero, nombre cliente, apellido del cliente. Después le voy a poner nuevamente el BR. La fecha es y le voy a poner la fecha y lo que está buscando es la razón de la llamada, ¿verdad? Después voy a poner nuevamente BR y le voy a poner te dejo un resumen de la conversación, ¿verdad? Y vamos a ponerle el resumen de la conversación. Ah, y por último le voy a poner cualquier cosa, si es que tienen que contactarlo, mail de contacto. Y le voy a incluir acá el email del cliente, ¿verdad? Después vamos a bajar a quién se lo queremos mandar. Este se lo mandaríamos directamente a la clínica, ¿verdad? clínica@clinica.com. Pero como quiero recibirlo para hacer la prueba también voy a poner mi correo electrónico mejacero00@gmail.com y le vamos a dar a okay. Ahora ya tenemos la automatización que está funcionando. Opcionalmente si quisieras mandar un SMS podrías conectar la aplicación de Bonatch, mandarle un SMS, hacer la conexión de Bonatch que aparece justo acá. Tienes que irte a aplicaciones, crear una nueva aplicación, copiar el application ID, el API Key y la clave privada que te van a dar. Y acá desde el from seleccionarías el teléfono desde el que le mandarías el SMS y en el tú le pondrías exactamente esta variable que está acá, que es el teléfono del cliente. Pero para este caso no lo vamos a armar para mantener la automatización un poquito más simple y le vamos a dar a guardar. Ahora sí, si es que ejecutamos y prendemos esta automatización, podemos ver que en tiempo real se van a pasar todos los datos a este Google Sheet que aparece acá y que luego deberíamos recibir un mail de confirmación después de haber llamado. Así que vamos a hacer esa prueba y voy a entrar nuevamente a la aplicación y le voy a poner hablar con el asistente. Entonces, acabo de colgar y como podemos ver aquí, el webhook se está ejecutando en tiempo real. Lo estamos viendo justo ahora en tiempo real. Esto sigue cargando y efectivamente se acaba de pasar al Google Sheets y se acaban de mandar los dos correos electrónicos. Como podemos ver acá sale que se actualizaron las filas en Google Sheets y que se mandó los dos correos electrónicos a quién, tanto como para el cliente como para la clínica, pero puse los dos en el mismo correo para que se pueda ver un poco mejor. Acá tenemos toda la información, como podemos ver, Benjamín Cordero, me aparece mi mail, me pone mi número, la hora de la cita, blanqueamiento dental y después una metadata que no es necesariamente vamos a usar, pero la transcripción de la conversación y el resumen de la llamada, ¿okay? Y si queremos escuchar la transcripción en vivo, también tenemos el URL. Y si es que entramos al mail, entro a este mail que está acá, nos vamos a ir a los recibidos y podemos ver que efectivamente, siendo las 753 y las 7:54, acabamos de recibir los dos mails, tanto como para el cliente como para la clínica. El primero es la confirmación de reserva, fue confirmado para bla bla bla y el segundo fue de una nueva reserva que este lo recibiría la clínica, que es con toda la información, resumen de la conversación, cuál fue el correo, el mail de contacto y en fin, todo lo que le pusimos. Esto lo podemos personalizar absolutamente como queramos, solo que queríamos hacerlo un poco simple. Así que guardamos y nos vamos nuevamente atrás. Así que podemos verificar que está funcionando, pero esto va a funcionar tanto para la gente que desea agendar algo como la gente que no necesariamente desea agendar algo. Pero si recuerdas, anteriormente lo que hicimos fue crear un success evaluation. Si es que nos vamos aquí aapi y nos vamos a el successation, le dimos el prom de tu misión es analizar la llamada y verificar si la persona quería agendar una cita o no quería. Devuelve true en el caso de que sí y se tomó los datos y false si es que no. Así que lo último que vamos a hacer es agregarle un pequeño filtro antes de enviarle el mail porque no queremos mandarle un mail a la persona si es que no realmente terminó de agendar esa cita. Vamos a hacer clic derecho acá y le vamos a dar a crear un nuevo filtro. Y esto es si es que la persona agendó y le ponemos la condición de que si el successuation, que es literalmente lo que aparece acá, es true y le cambiamos el igual a que de igual en las mayúsculas o minúsculas, va a pasar al siguiente paso. Si es que la persona agendó, le vamos a mandar el mail. Si es que la persona no completó todos los datos o no tenía intención de agendar o no quería agendar, sí se va a registrar aquí directamente en el Google Sheets, pero no le va a mandar el mail. Si quisiera que no se registre en el Google Sheets, pondría exactamente este mismo filtro, pero acá, ¿okay? Porque el filtro lo que hace es filtrar hasta dónde va a seguir avanzando la automatización. Ahora, hay muchas más cosas que podríamos mejorar en esta automatización. Esta es una base, no quería hacer este video que dure 3 horas, ¿okay? sería verificar la disponibilidad efectivamente del dentista y cuál es el mejor horario. Entonces, lo que haríamos ahí sería crear un nuevo escenario y usaríamos el módulo de cal.com, que eso nos permite verificar exactamente si es que hay disponibilidad o no y que después les sugiera las opciones que están disponibles. Pero si quisieras hacer esto realmente práctico y una solución que puedes vender, lo que puedes hacer es tomar esta misma información y en vez de hacer que te agende una hora directamente en la llamada, es, oye, dame tu información de contacto, dame tu mail, dame tu teléfono y te voy a mandar un link para que tú puedas agendar por tu cuenta. Y después así también le puedes hacer un seguimiento y lo que haces es le mandas un link de cal.com o le mandas directamente un link de Calenly. En fin, las opciones son realmente infinitas y esto es solo el inicio. ¿Y cómo lo podemos realmente dejar funcionando? Es nos vamos acá a la plataforma y nos vamos a los números. Lo que vamos a hacer acá es vamos a comprar un nuevo número a un precio s super accesible. Lo que vamos a hacer acá es vamos a asociar el asistente que acabamos de crear, en este caso Clínica Dental versión 3, y lo vamos a asociar directamente al asistente. Y si quisiéramos hacer una llamada de prueba, podemos hacer una llamada outbound desde acá o podemos dejar una inbound directamente desde acá, pero eso también se los tendría que mostrar cómo configurarlo en otro video, pero lo importante es que esto esté funcionando porque desde acá las opciones son realmente infinitas. y vamos a empezar a profundizar bastante en esto dentro de Imperio Digital. Así que te recomiendo si es que estás buscando realmente empezar a ahorrar tiempo con automatizaciones que sirven y meterte a lo que es potencialmente una de las comunidades más activas a nivel mundial de automatizaciones, te invito a que entres a probar a Imperio Digital por 7 días completamente gratis. Aquí también lo que hacemos son llamadas en vivo todas las semanas con expertos en automatizaciones. Tenemos a Fran, que es parte del equipo que también está resolviendo dudas técnicas. Tenemos una comunidad activa que también se ayudan entre ellos y están creciendo porque todos tenemos un mismo objetivo en común, ahorrar tiempo. Y sea porque queremos ahorrar tiempo para nosotros o porque queremos ahorrar tiempo para alguien más y potencialmente venderlo. Así que si lo que te interesa es aprender sobre automatizaciones con inteligencia artificial, Imperio Digital es el lugar que estás buscando, porque no solamente tienes eso, no solamente tienes curso, sino que también tenemos una biblioteca de automatizaciones explicadas también paso a paso que simplemente puedes descargar e importar. Si te vas al final, vas a tener una guía práctica y puedes descargar todas las automatizaciones e importarlas directamente a Make, porque si nos vamos a crear un nuevo escenario, podemos importar absolutamente cualquier automatización de las que están acá. Por ejemplo, esta que nos sirve para automatizar la creación y publicación de contenido en Instagram, también acompañado de una guía. Si es que bajas y descargas directamente la guía, puedes importarla apretando acá y le das a guardar. Y podemos ver que la automatización está lista para que la empieces a usar. Y también en este mismo video, la automatización que está acá, tanto esta como la del get fecha hora, también las puedes importar. Si es que nos vamos a crear un nuevo escenario y no quieres armar todo esto por tu cuenta, puedes irte acá, apretarlo, descargarlo, irte a un nuevo escenario, apretar los tres puntitos, importar un blueprint, seleccionar archivo y darle a guardar. Y como podemos ver, se acaba de armar toda la automatización que acabamos de armar en el video. Así que sin más que decir, si es que esto es algo que realmente te interesa llevar más a cabo y más a profundidad, házmelo saber porque lo vamos a estar haciendo dentro de Imperio Digital, pero házmelo saber en los comentarios también si es que quieres que desarrollemos este tema un poco más en profundidad. ¿Okay? Muchas gracias por haber visto el video. También recomiendo que veas los otros videos de mi canal. Y sin más que decir, te deseo mucho éxito. Nos vemos adentro de Imperio. [Música]
