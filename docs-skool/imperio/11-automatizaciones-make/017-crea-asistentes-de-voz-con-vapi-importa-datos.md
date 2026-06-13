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

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/00b80815bbe34bcfbd4442fac4e7c1556d486504f950404e95831d080116dbd5-md.png)

Nos iremos a "assistants" y le daremos a "create new assistant"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a94d1823d9cc4b9aab7fcc2a857f6b296bfb5457ef9d41cdadf921348913da16)

Eligiremos o construir desde una plantilla en caso de que se adapte alguna a lo que buscas, o empezar de 0. Para este caso, eligiré empezar de 0 por fines prácticos, y le daremos a create assistant.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/819aaa1be57744b89ed5e9ffdcdbcbe5e42d1ef4ebae49e3a9f90a2252abca40)

Aqui veremos un dashboard con muchas opciones. Tenemos el Model, que es donde construiremos el prompt base, el transcriber que transcribirá las conversaciones, el voice donde podemos ajustar que voz queremos que nuestro asistente tenga, las funciones que son llamados especiales a Make que haremos para conseguir informacion o guardar informacion, y analysis que nos dara el análisis post llamada (en MUY grandes rasgos)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5de297ac6ab447db870d6ed8b14ae3f73ad15473f6924d4c8bc2568027f975d8-md.png)

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

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/deaa660e4e84461e8f78ff5e724556ad4bdb55e7fe9b45228c04459ca0bed8f8-md.png)

A la derecha hay una serie de parametros que podemos ajustar, por ejemplo el "Knowledge Base" es super util si quieres agregarle una base de informacion:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/68bc29043e864b90ba9f6d983d1298c93da7fd1a672440a9a950ab0112a8c157-md.png)

Dentro de la ventana de "Transcriber" eligiremos la opción de como queremos que se transcriban las llamadas. El mejor modelo que he usado en español es deepgram y en idioma el "es".  


![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5dba66316bdf48db867e1ef9783c26c7171640d532164227b14bf4fee5cbcc43-md.png)

Y aqui probablemente viene una de las partes MAS importantes... la voz que utilizaremos.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8f756a91c38c4c809e80a4e0721914a7e2e7e6a00bee4582acb165a4a395e397-md.png)

Aquí puedes agregar tu propia voz personalizada y puedes elegir entre miles de acentos. Tienes muchos "providers" para elegir, puedes elegir 11labs si quieres personalizar algun acento especifico o incluso entrenar la IA con tu voz.  
  
Aquí veras que hay una parte super importante, la parte de arriba que es la latencia, es decir cuanto se demora entre conversacion e IA.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ed6bd11bce79413eb3ce81fe2b17b63faac701d91fac4252bc48adc5b699c4a4)

Hay dos principales modelos que usaremos, el "Eleven Multilingual V2", que tiene una MUY buena voz, pero la latencia aumenta un poco, y por otro lado tenemos el "Eleven Turbo V2", que tiene una menor latencia, pero la voz se escucha un poquitoito más robótica. Entonces esto es preferencia personal. Prefieres que se demora un poco más pero no se reconozca para nada que es IA? O prefieres que la generación sea más rápida sacrificando quizás un poco el resultado final. Esto está a tu disposición y preferencia, para mi caso utilizaré el Multilingual v2.  
  
También tienes un par de opciones más que peudes personalizar, como si quieres que se escuche ruido de fondo, o usar palabras "filler" o de relleno para hacerlo ver más natural

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/82a633cdcd114c0481a6b9ae7de3e34c4168100e187d44d4bd54b25e2c7307ae-md.png)

Ahora si nos vamos a funciones, podemos crear una nueva funcion o podemos apretar la seccion de "tools" de la izquierda.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/62c1987c878f4713a5f909fceeee2dec85afafa0b2b44e8fb39c29e190831a2e-md.png)

Esta es probablemente la parte más importante de todas... y aquí es donde conectaremos a Make.   
  
Las funciones son esenciales para conectar el agente de voz con herramientas externas como [Make.com](http://Make.com), que nos permiten una automatización completa y fluida. Por ejemplo, funciones como *"getFechaHora"* ayudan al agente a obtener la fecha y hora actual, algo que GPT-4 no puede hacer por sí solo. Esto es clave para verificar la disponibilidad de citas en tiempo real.

Otra función importante es *"end call report"*, que recoge todos los datos proporcionados durante la llamada (nombre, correo, fecha de nacimiento, etc.), los estructura y los envía a [Make.com](http://Make.com). Allí, estos datos se procesan para registrar la información en Google Sheets, enviar correos electrónicos y SMS, o realizar cualquier tarea necesaria. Estas funciones aseguran que los datos sean precisos y estén listos para ser usados sin errores.

Sin estas integraciones, el flujo sería manual y propenso a fallos, perdiendo gran parte de la automatización. Las funciones no solo hacen que el sistema sea eficiente, sino que también permiten adaptarlo a distintos negocios y garantizar el cumplimiento normativo, como las reglas de HIPAA, al manejar la información de forma segura.

Ya, pero Benja, ¿cómo lo hacemos? A POR ELLO

Iremos donde sale "New Tool"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e91420321ba44c7695df4eb7a24beae04c135bad832a42439a2b80742ab3ddeb)

Aquí iremos odnde sale "Custom Tool", si se que es tentador elegir Make.com, pero es MUCHO mejor si ponemos custom tool, ya que nos ayuda a hacer el debugging (en caso de ser necesario) mucho mejor.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/23ceb3befac34034b5594c832033c403f7429834d1c34ec2a6d18f6b1c153e68-md.png)

En "Server URL tendremos que poner el webhook que crearemos en Make. Si no sabes lo que es un webhook, es una palabra elegante para un "disparador instantaneo". Recomiendo que veas el curso de "[Make desde 0](https://www.skool.com/imperio-digital/classroom/798d337a?md=32341ea834ff484b8d39d69f96199f2c)" si quieres más detalles, pero igual iremos paso a paso.  
  
Entraremos a [Make.com ](http://Make.com)y crearemos un nuevo escenario 

> NOTA: Te dejaré toda esta plantilla de Make publicada en los recursos llamada "getFechaHora.json", puedes importarla apretando los 3 puntitos en un escenario de [Make.com](http://Make.com) y dandole a "import blueprint"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/aa0af7e6ed6a4da19ac1d1a4e19f069461afb564c3724ef9b2b689fd61aa4ad3-md.png)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a5e2f5b3a8d54c9aac1843d7ba0c691d5266848ea2ef4c96bcd45ab417533d60)

Le daremos a crear un nuevo trigger, y buscaremos la opcion de "custom webhook"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9bc3e79f5df4481fb46cabfb457a028e17744f45955e4376b49f9f0670178971)

Le daremos a "ADD" a la derecha y le pondremos un nombre. El webhook que crearemos es para conseguir y devolver la fecha y la hora en una conversacion telefónica.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4f18ad72747741b9915e8de8c10a80ba7e347f42df55441ba294e5a09852ca76)

Copiaremos y pegaremos el Link del webhook...

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0b20d32323f14bacb2d24ca42492986d6f02f917fbd34c26b124989b7adfa37b)

en el "Server URL", y le daremos a save.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1f0c3d743fc84c79a7eebb164276402d2f09680d9b7c4cff8c9482c8505b9c93-md.png)

Le pondremos un nombre y definiremos cual es el proposito de esta funcion. Recordemos que esta funcion la llamamos para poder devolver una fecha y hora actual, y cuando la IA detecte una intencion de agendar una llamada o un evento por ejemplo, llamará a esta funcion para detectar ¿que momento es ahora?

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b11f899dcc0c4aec89c3da16aedd6a6e6c23af10ce724b81b4207910e0d11b06)

Le daremos a save y seleccionaremos los properties

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7d39f68ea2d9415bad9e430583b32196b0dd59c5437f4ee6949a9b3ebbf6ee0b)

Le daremos a next, y nuevamente le daremos una descripcion mas larga, para que el LLM (GPT4o en este caso) pueda entender CUANDO llamar esta funcion.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/01e355d9302e4b5381aa425f3164add3c8ffdf4e0ca447909717250dbce07763-md.png)

Este es el texto que puse

```
Esta funcion será llamada cuando quieren agendar una hora para que se sepa cual es la fecha y hora actual en Santiago de Chile
```

Y le daremos a Create...

Ahora vincularemos la función a el asistente que creamos previamente. Volveremos a la sección de "asistentes" y "functions"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1655931bf3e84dc2a0b3a10fd526bf1a22885e05dd3548fca4dcf4c504080770-md.png)

Donde aparece "Select Tools" eligiremos la funcion "GetFechaHoraV2" que creamos previamente.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/35f947fb8fd1495388514e96be3a1ac68c47f2f7cc2d45ccb390038288833516-md.png)

Le daremos a "Publish"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2a9247d6a73145b0969548327ee1f4c23fa688e1c2ad4587a4a93070e9d6dd97-md.png)

Ahora si le damos a "Run Once" a nuestro escenario en Make

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d47f3be77042459795f9725b750649170cf94cb7f95d4e2cad0b1eb6f20a8a8c-md.png)

y hacemos la prueba de pedirle la hora, debería llamar a la acción

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0ed99e5ef81d414b8cf5c26634d7133527e93947ca64498ea402738f8e62f98c-md.png)

Y le pediremos directamente la hora diciendole "dame la hora"... no te dará la hora correcta pero debería haber mandado una señal a Make.com, y tu escenario debería verse algo así:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a43499f94ca440fc8cb2d9ada41ef6dd29ad37bf75774aaca5fcc9100a5aaa6c-md.png)

Okay. Está funcionando. Ahora lo que tenemos que hacer es que efectivamente tenemos que recopilar la hora y luego devolversela al asistente no? Para eso vamos a agregar un par dem odulos en el escenario de Make.  
  
Buscaremos la opcion de "Set Variable" en Make y la agregaremos al paso siguiente del Webhook

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2d12051a2b43477d8357d4443eed85feaa50990134ed44d596633e5108da74d3-md.png)

Lo que tenemos que armar es lo siguiente:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c628196aca834758885ae5bfaf1758126586b68849074d7bb7274e9c9224b365)

Pero tenemos que hacerlo bien... asi que lo primero que escribiremos será (con las respectivas maysuculas y minusculas)

> formatDate(

Luego, apretaremos la opción que sale "now" que está en el calendario justo aquí:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4f9b883d5f3042aa9580d9a65c778086d9b1b2c49f994601ac9f0c2100d47bcf)

```
{{formatDate(now; "DD.MM.YYYY HH:mm"; "America/Santiago")}}
```

Nota: Primero pondrás el continente y luego la ciudad. Dándonos algo así

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/caf3cf9ad1e84f4faefba7e5291fe6f8f7e72780ea704dad847d3d65f5257947)

Entonces ya creamos y tomamos la variable de la hora y fecha actual. Ahora necesitamos DEVOLVER la información, por lo que utilizaremos un "webhook response"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8e052ed2ddd54ba0aa8aaefacbb23f925cea444cfedf446b8dc928685e5f8fea-md.png)

Aquí si tendrán que pegar este código que les dejaré a continuación después de la imagen, para que se vea así:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/53daabed470a433bbad8e9dd4877973466dd3ab186b241d1a53c5f6ec0d94694)

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

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/aa0af7e6ed6a4da19ac1d1a4e19f069461afb564c3724ef9b2b689fd61aa4ad3-md.png)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7497174f9f9541ba98c6d372180b76f0ebe3a8895bcc4091b355402c51756122)

Ahora si vuelves a correr el escenario, debería devolverte la fecha y hora correcta. Hagamos la prueba, le daré a "Run Once"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ed03a502420f407cb6efbfa5cc14fdd974273ee79b7542e580b44bee6dcf9412-md.png)

Y volveré a hablar con el asistente

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b6f19f2e7f314c158eef98d18021fe3057610d16a16f413dbd11a9c7a5eaef1f)

Y efectivamente me devolvio la fecha y hora correcta, tanto en Make como en la llamada.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4ea1b8b72eb142569256bd2711dd6f7228f026ed14944331842de13a98a1799e-md.png)

Ahora, le daremos a guardar y dejaremos corriendo la automatización

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4a4e2ffec1454906829decbf364773371642065b91bd44979cd78d62d6a63510)

Una vez que tenemos nuestra primera función configurada, el siguiente paso es crear y manejar la data de la llamada para que pueda ser procesada y enviada a [Make.com](http://Make.com). Aquí es donde entra la función *"end call report"*. Esta función es crucial porque recoge toda la información obtenida durante la llamada, como el nombre, el correo, la fecha preferida para la cita, y otros detalles necesarios.

La razón principal para implementar esta función es estructurar y enviar estos datos de manera precisa al siguiente paso del flujo: su registro en Google Sheets. Esto convierte la hoja de cálculo en un CRM básico, donde toda la información queda centralizada y accesible para el equipo de trabajo. Además, desde ahí se puede disparar el envío de notificaciones, ya sea por correo electrónico o SMS.

Esta función no solo automatiza el registro de datos, sino que también asegura que se mantenga el control sobre ellos. Al completar la llamada, toda la información pasa automáticamente a [Make.com](http://Make.com), que se encarga de organizarla y procesarla para las tareas siguientes, como actualizar el sistema de gestión o notificar al cliente y al personal. Es un paso clave para garantizar una integración fluida y eficiente entre VAPI y otras herramientas.

Lo primero que haremos es crear un nuevo escenario donde pasaremos toda la informacion de la llamada cuando se termine, y la pasaremos a un Google Sheets. Por ende crearemos un custom webhook que sería algo así:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2d12e8c2eed64b99a650b7cf9faeb267d5c123aac9884b79a749d5d698db943b)

Y le pondremos un nombre

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/db35cdee856244769edfc778faeac8088046ebbbd798449690b95c2be380f9b3)

Luego tenemos que agregarle un modulo de "add new row", que sería una nueva fila cada vez que se haga una nueva llamada

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b96a546a046f4ae281a61525d0d1e49dd478f9456d8b4f7697408fab1f3d99a3-md.png)

Y nos pedirá conectar el google sheets, por ende crearemos un google sheets donde centralizaremos todas nuestras llamadas con las variables que necesitamos. Se vería algo así:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f5ac7f96d71c495f9df3f78b3d77b770740d0046d960451d8142c06333f52502-md.png)

Ahora que la tenemos creada, necesitamos incorporar las variables, pero antes necesitamos hacer una llamada de prueba y habilitar un par de cosas antes en Vapi. Volveremos a la pestaña de Webhook de Make y copiaremos el webhook

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a395e6648b1f4adabeb3db67205acabfb54c33826ef04d1d86a58bdd59574c34)

y lo pegaremos en VAPI bajo al sección de "Advanced"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a9dd47dde0984efa8ccd2c564598aac494ee6345ea6d47f2acbd5362143ca548-md.png)

Luego bajo Client Messages habilitaremos las siguientes opciones

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/32d7ea6311eb4665b9813c230052b602840327449b114e9d9b6222d4dac7bb12-md.png)

y lo improtante es que bajo "Server Messages", dejaremos SOLO el "end-of-call-report"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2342419f5ca34c02bfb4853a2f9fa2f95a137fbf3eb54e25b5bb32f701bee6c5-md.png)

Y le daremos a "Publish"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/27dc31449b604fa29fe7f1d128c65905bedfde18f5fb4d2fb468e0e8fd0aab03-md.png)

Finalmente nos iremos a la pestaña donde dice "Analysis"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/eadec68f04934a52acf5c9152523f71b4a3d46a71dc842a9becfb7cc6b15d275-md.png)

y aquí es donde sacaremos los resúmenes y lo más importante, la "structured data", o la data estructurada, que es la data que realmente nos importa.

Bajo Summary le podemos poenr algo como:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/10a79899f48840019b909ede1c2e3a9bbe3a74fe0cdd42d7bef3c87dd1197bb6-md.png)

> Eres experto en tomar notas. Necesito que tomes el resumen de la llamada y hagas un resumen de ella, destacando los elementos clave.

Y bajo Structured Data, es donde tenemos que hacer las cosas que son importantes, que es la data de las personas que queremos recopilar

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b3f0c3b76139441396c33e6029a8af9944ea9901408542f89532e642c8ca9e21-md.png)

> Eres un experto tomando notas. Se te dará la transcripción de una llamada. Tu tarea es extraer un nombre de cliente, un apellido del cliente, un email del cliente, un telefono del cliente, extraer la hora en la que quieren agendar una cita, extraer la fecha_hora en la que la persona quiere agendar una cita y una razon de la llamada. Luego necesito que me des una STRUCTURED DATA de vuelta con las variables anteriores.

Estos son los datos que nosotros queramos, que son los datos que irán en el sheets.  
Luego bajo "Structured Data", necesitamos empezar a agregarle properties o propiedades. Cada propiedad será una casilla que vamos a juntar, una variable de cada cliente.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b64381e5e87c465fb17992ce323e9ef404b6fe71167d4e35873928290da1bbc4-md.png)

Aqui agregaremos la data que queremos juntar y le crearemos una descripcion pequeña para que la IA entienda que es lo que es cada variable.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ea8dbaca21f4466dbf6941f24deecab6efc946f02eff4239bf9c17e6de6cfaca-md.png)

Y continuaremos llenando los datos

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9ec43d224cd0477694d25111a1d3bb46c93d6563c688442aaf6390529a4c7db0-md.png)

Le daremos a Publicar y haremos una llamada de prueba, pero antes tenemos que habiltiar el "Run Once" del escenario de end call report que creamos previamente, y nos aseguraremos que la IA nos pida todos estos datos, si no lo hace modificamos el prompt.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/64eb6638d442476bbe1d21cd9879c6b710aaa12325014827a48a4aa4316511a9)

Luego de hacer la llamada, debería habernos corrido el escenario satisfactoriamente.

> NOTA: Te dejaré toda esta plantilla de Make publicada en los recursos llamada "call-report.json", puedes importarla apretando los 3 puntitos en un escenario de [Make.com](http://Make.com) y dandole a "import blueprint"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/aa0af7e6ed6a4da19ac1d1a4e19f069461afb564c3724ef9b2b689fd61aa4ad3-md.png)

Ahora si vemos la informacion que nos devolvió, podemos ver que nos tomo toda la data de llamada

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/83f518ffbdda48d3b4e3b23a40373a80e4d7b58c7e8d487daac6fc5111d7d808)

Y luego reemplazamos los datos aqui, en cada casilla donde queremos rellenarlo.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c30ede18e22941b5aa114bb8cdbd7334ec5eaf23f6684fb8a4db93750f4fab93)

Luego puedes ponerle el resumen de la llamada si quieres, la trasncripcion y el link de grabación de la llamada.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/52c74e111f8b4ee7a7b721df0a3a2dcc8d1fa6a017894b0bbe6115977966c8e7)

Luego que esté funcionando, tenemos que mandar el mail a las respectivas partes, uno al cliente para confirmar la cita y otro a la clinica dental para avisar la nueva cita, por lo que crearemos un "Router"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4fccf9017d2f4499a77a93c13581fe447d08a3f41ff8451694e23101e547d96d-md.png)

Agregaremos un "create and send a message" de Outlook, pero podrías usar cualquier otro servidor de mail como Gmail si prefieres.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d97299b014af4e6e9d8653806d01c28d191c9710dec044b093bfd1e3cde401d1-md.png)

Rellenaremos las respectivas variables (nota, el <br> significa "enter", para que cuando llegue el mail hacer una línea del enter. Aquí le puedes agregar lo que quieras

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d907064a22354dc4bcbb9cfb95d2daaadeb5b605dfed464798a94a9fb8402046-md.png)

Luego haremos lo mismo con el mail que le enviaremos a la clinica dental

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cbd0df270f98495992e10b016241ae9372f61bd19b9840b089965e1e5935e7aa-md.png)

Asi se vería, y abajo pondríamos el mail de la clínica donde notificaremos la reunión.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4ea0a0b8c87444399790ee51d9f5b6f0d584700b67104b059059ec91573f3871-md.png)

Luego si queremos mandarle un SMS de confirmación, podemos usar una aplicación como "Vonage"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a76321043c504a5cb626a706664a657452647c27b87d4d3d884a5a8edbc78d3b)

Luego de hacer la conección con Vonage y copiar la API key y Private Key que aparece al registrarse y vincularla a Make...

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9b26af26d75b4e0db1e5ed5f86bb0c88e195fb01953741bb9480e2e3c38e20b9-md.png)

Podemos enviarle un SMS de confirmación

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c0a842af3c6d4e9cbb4001d13f55d165fffb46a1153e4482807c5d415d6b8ef1)

Ahora nos quedaría el último paso... En este momento estaríamso mandandole un mail de confirmacion tanto a clientes que queiren agendar como los que no. Es por eso que necesitamos hacer un "filtro" de que pasen solaemnte los que SI decidieron agendar. Para ello usaremos el "Success Evaluation" de Vapi. Esto nos dice si la llamada fue exitosa (si hubo agendamiento) o si no lo fue (no agendaron). Entraremos a Vapi bajo "Analysis" y nos iremos a "Success Evaluation" y le pondremos el siguiente prompt

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d6eb13819a034a34813db0c708bef9f7cb956d3e04c34f55a90988db4f4beb10-md.png)

> Eres un experto en agendamiento de citas. Tu mision es analizar la llamada y verificar si efectivamente la persona QUERIA agendar una cita o NO QUERIA agendar una cita. En caso de si y agendó, devolver "true", en caso de no, devolver "false"

Le daremos a Publish y volveremos al escenario de Make. Le haremos click en la tuerca que está entre el google sheets y el router y le agregaremos un filtro

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/728eef31a43145e491a05a56a0542e117c2594e562804a15b0c08b512feb946f-md.png)

Aqui le pondremos "si quiere agendar" el valor de "success evaluation" debe ser "true"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4c5379e45d0d4961a0ed9340decb27cc6b52f3b612e84161917f764b39b72c8e-md.png)

Esto hara que solamente pasen la gente que SI queire agendar.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d2eb1e06711e47e88891284ff1ced6fbe733f36cf5ac47b893b14b9ed7309709-md.png)

¡Y así concluimos! Asegúrate de guardar el escenario y dejarlo corriendo para que funcione, llama y haz la prueba. 

Ahora tienes el conocimiento y las herramientas para crear un asistente de voz con VAPI e integrarlo con [Make.com](http://Make.com), automatizando tareas que antes te tomaban horas (y muy buena idea para venderlo). Desde gestionar citas hasta enviar notificaciones personalizadas, este sistema es una solución eficiente, profesional y completamente adaptable a las necesidades de tu negocio.

Recuerda que, si buscas simplificar aún más el proceso, [**Make.com**](http://Make.com)** te permite importar plantillas prediseñadas**. Estas plantillas te ahorran tiempo y te ofrecen una base sólida para construir soluciones personalizadas sin complicaciones. Es una manera rápida y efectiva de implementar automatizaciones que realmente hacen la diferencia.

El siguiente paso está en tus manos. Aprovecha lo aprendido, experimenta con las herramientas y sigue optimizando tus sistemas. La automatización no solo te ahorrará tiempo, sino que también te permitirá enfocarte en lo que realmente importa: hacer crecer tu negocio.
