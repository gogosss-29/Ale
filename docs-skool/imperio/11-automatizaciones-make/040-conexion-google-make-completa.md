# 📌 Conexion Google + Make COMPLETA

> Ruta: Automatizaciones Make › 📌 Conexion Google + Make COMPLETA

**🎬 Vídeo (14.0 min):** https://www.loom.com/share/b924b0ab6a0d4f4fbc20407f27ba8894

---

> #UPDATE: Incluir en el paso 3 "URI": [https://www.make.com/oauth/cb/google-email](https://www.make.com/oauth/cb/google-email)
> 
> 
> 
> [https://sentiorganization.notion.site/conexion-con-google-completa](https://sentiorganization.notion.site/conexion-con-google-completa)

# Conexion con Google Completa

👉 En este video te mostramos **paso a paso cómo conectar Google con Make** para que puedas automatizar Gmail, Google Sheets, Drive, Calendar, Docs y Forms sin enredos.  
Ideal si estás arrancando y quieres tener todo tu ecosistema de Google bien integrado con Make.

⚠️ Spoiler: vas a necesitar crear un proyecto en Google Console, activar APIs, y copiar un par de claves... pero no te preocupes, lo guiamos TODO y además te dejamos un **Notion con cada paso y los links correctos** para que no pierdas tiempo buscando.

📌 Vas a aprender:

- Cómo activar las APIs necesarias
- Cómo armar tu pantalla de consentimiento OAuth
- Qué dominios autorizar
- Cómo crear el cliente y pegar todo en Make

Y lo mejor... queda todo listo para usarlo en tus escenarios y empezar a automatizar como pro!

🧠 Si algo no te queda claro, deja tu duda en Skool y arroba a Santino.

👇 Tienes el [link al Notion](https://sentiorganization.notion.site/conexion-con-google-completa) con todo lo que usamos en el video.

---

# En esta guía vamos a integrar

## **1) Recursos Necesarios**

[Link a Google Console](https://console.cloud.google.com/welcome/new?_gl=1*1ro8i40*_up*MQ..&gclid=CjwKCAjwz_bABhAGEiwAm-P8YVnOQi7jYfe10EsJADZlkZu3sBhsM1nQg7o9Fe6aoNE6fx7-cDNa3xoCrIwQAvD_BwE&gclsrc=aw.ds&inv=1&invt=Abw-og)

### 2) Dominios:

[integromat.com](http://integromat.com)

[make.com](http://make.com)

### 3) URIs:

[https://www.make.com/oauth/cb/google-cloud-speech](https://www.make.com/oauth/cb/google-cloud-speech)

[https://www.make.com/oauth/cb/oauth2](https://www.make.com/oauth/cb/oauth2)

[https://www.make.com/oauth/cb/google-custom](https://www.make.com/oauth/cb/google-custom)

[https://www.make.com/oauth/cb/google-analytics-4](https://www.make.com/oauth/cb/google-analytics-4)

[https://www.integromat.com/oauth/cb/oauth2](https://www.integromat.com/oauth/cb/oauth2)

[https://www.integromat.com/oauth/cb/google-custom](https://www.integromat.com/oauth/cb/google-custom)

[https://www.integromat.com/oauth/cb/google-restricted](https://www.integromat.com/oauth/cb/google-restricted)

[https://www.integromat.com/oauth/cb/google-cloud-speech](https://www.integromat.com/oauth/cb/google-cloud-speech)

[https://www.integromat.com/oauth/cb/google-analytics-4](https://www.integromat.com/oauth/cb/google-analytics-4)

[https://www.integromat.com/oauth/cb/google/](https://www.integromat.com/oauth/cb/google/)  
  
[https://www.make.com/oauth/cb/google-email](https://www.make.com/oauth/cb/google-email)

## 🎙️ Transcripción

Buenas, imperiales, ¿cómo van? ¿Todo bien? Bueno, este es un video más que nada dedicado para los, para los más nuevitos, los que están arrancando, que quieran, ehm, agarrar y hacer conexiones, eh, con Make, para usar con Make, eh, con Gmail, Google Drive, Google Sheets y todo eso, todo lo que es el ecosistema de Google. Ehm, para eso hay que hacer una serie de pasos que no son nada complicados, Lo único que van a tener que hacer es seguir todo el video paso a paso, pero igualmente que lo más importante, no se preocupen que yo acá les arme un Notion para ustedes donde van a tener las cosas necesarias. ¿Ok? Para armar todas estas cosas. Cosas a tener en cuenta, en esta guía vamos a integrar estas aplicaciones ¿Ok? Gmail, Drive, Sheets, Calendar, Docs y Forms. Tenemos acá, abrir un escenario nuevo de Make para que nosotros vayamos testeando cada una de las conexiones ¿Ok? Por ejemplo, vamos a crear un módulo de esto, Agregamos un módulo de Drive, cualquiera, lo más importante es que se note que acá vamos a Vamos a ser todos testigos de que todas estas aplicaciones funcionan, ok. Voy a buscar Calendar acá. Vamos a agregar Docs, ¿no? Docs era otra de las que estaban acá. Y por último, Forms, ¿no? Google Forms, bien. Y entonces ahora nos vamos a encargar de que todas estas conexiones funcionen bien, ¿ok? Bueno, acá nos podemos guardar el escenario. Así que bueno, arrancamos. Lo primero que tienen que saber es que vamos a crear un proyecto. en google console ok esto es lo más sencillo toquen el link que está acá por favor no hagan esto por favor se los pido no hagan google console y se metan acá al patrocinado que dice empezar gratis esto no lo hagan por favor por favor se los pido porque van a entrar acá y les va a pedir que pongan acá información de la cuenta ok 300 no necesitan nada de esto entran el link que yo les pasé y se ahorran todo todo ese problema después vamos acá a seleccionar un proyecto y le vamos a dar crear un proyecto nuevo. Yo le voy a poner test imperial. Ya estuve haciendo acá unas pruebas de simulacro para que funcione todo bien. Vamos acá, nos van a mandar de vuelta acá a seleccionar proyecto. Bien. Y vamos a ir acá al menú de navegación. Y en el menú de navegación, me voy a correr del medio, estoy en el diome, vamos a ir acá a biblioteca, ok, y acá en biblioteca vamos a instalar, vamos a habilitar, esto va estas cuatro APIs de Google. Vamos a empezar por Google Drive. Importante, se meten, le tocan habilitar y tienen que esperar a que cargue y a que los redirija. No se vayan de esta página sin que los redirija. Acá, una vez que nos redirige, volvemos a tocar acá este botón de biblioteca y vamos a la de calendar. Vamos a hacer este proceso con las cuatro, así que mientras tanto me tomo un vasito de agua. Bien, volvemos a Biblioteca, vamos a Gmail, hacemos lo mismo, habilitamos. Bien y ahora nos queda la última, que va a ser Google Sheets API. bien bueno estamos más o menos a mitad de camino ok Es muy importante que, bueno a ustedes lo va a mandar acá, vamos a tocar pantalla consentimiento auth y van a ver que va a aparecer un cartel acá que dice que aún no se configuró. Seguramente a ustedes se habrán dado cuenta que hace un segundo que estábamos acá, estos paneles tenían otros nombres. Esto se les va a actualizar, apenas se muevan como hice yo recién. Pantalla con sentimiento y se les va a cambiar este menú. Esto es, está bien, es así. Vamos a ir acá a Descripción General y vamos a tocar Comenzar. Bien, le vamos a poner nombre de la aplicación, Make. El correo, el que estamos usando, siempre. El que estamos usando, con el que vamos a hacer la conexión. Tocamos Siguiente. En Público ponemos Usuarios Externos y le damos a Siguiente. Información de contacto, nuestro correo. Siguiente. Aceptamos. Continuamos. Y Creamos. Ok, bien sencillo esto. Usamos nuestro mail y al nombre de la aplicación le ponemos make. Bien, acá dice, aún no configuraste ningún cliente de tipo OAuth Bien. Bueno, no nos interesa, vamos a ir a desarrollo de la marca y vamos a ir acá abajo de todo donde dice dominios autorizados. Vamos a agregar dos dominios. A uno le vamos a poner make.com y al otro vamos a poner integromat.com. Ok. Estos son los dominios que les dejé acá, Bien, son estos dos. Ahora le damos a guardar y listo, cerramos este mensaje que cierran estos mensajes porque son bastante molestos. Bueno, vamos a acceso de los datos ahora. agregar o quitar permisos y acá vamos a darle permisos a todo básicamente pero primero cogemos acá y vamos a filas por página que ponemos 100 y seleccionamos todo y listo actualizamos acá importante y todavía más importante no se vayan de acá sin bajar hasta abajo de todo y poner save por favor, se los pido. Muy importante, paso muy importante, me ha pasado varias veces. Así que bueno, acá en público vamos a agregar usuarios de prueba. Y vamos a poner nuestro mail de vuelta. Vamos a guardar. Ahí estamos. Bien. Esto lo tenemos que tener acá en prueba. Esto antiguamente estaba bueno publicar la aplicación, pero ahora cambió y uno para publicar la aplicación necesita tener la aplicación verificada para algunos permisos que son sensibles. Entonces es como que nos trae un poco el proceso de conexión. Así que vamos directamente a clientes que es Lo último que vamos a hacer, vamos a crear acá cliente, aplicación web, vamos a poner make y acá en URIs de redireccionamiento autorizados, vamos a empezar a pegar todas estas todas estas urls que están acá, que es increíble que google se pone como loco cuando no pones la url, te sale en cartel se te mueve los, es tremendo. Bueno, les recomiendo para este proceso acá el doble clic. Funciona bárbaro, ¿ok? Me parece más cómodo que arrastrar así, la verdad, parece más cómodo y más rápido. Igual ya terminamos, nos quedan tres. Esto es bastante rápido, no sé c***** tiempo vamos pero estaremos llegando a los 10 minutos seguramente no mucho más que eso ahí va y seguramente ustedes lo están viendo el lumen entonces va a ser mucho más rápido bueno y vamos a ver acá a crear ok Y ahora empezamos, porque se viene lo lindo. Vamos a quedarnos acá y vamos a poner a prueba todo esto. Así que vamos a ir acá, vamos a ir a Google Sheets, a cualquier módulo de Google Sheets y vamos a crear la conexión. Acá le voy a poner Test Imperial Digital, me gusta. Vamos a mostrar opciones avanzadas y vamos a, por eso les dije que dejen esto acá, porque vamos a necesitar el ID del cliente y el secreto del cliente, que los vamos a pegar acá. Una vez que los pegamos, Arrancamos a iniciar sesión. Yo me voy a agarrar mi vasito de agua y vamos a seleccionar la cuenta con la que estamos haciendo la integración. Yo acá tengo las dos mías pero ustedes usen por favor la que con la que están haciendo la integración. Le damos a que sí a todo, le damos a continuar. Seleccionamos todo siempre, ok? Acá nos va a decir que no confíes en que sé yo, pero no sea un problema. Bueno, son seis, así que una de estas acá está hecha, ok? Vamos a ir con drive y vamos a hacer lo mismo. Vamos a poner Test Imperio Digital, vamos a ir a opciones avanzadas y vamos a copiar acá el ID de cliente, lo pegamos, copiamos el secreto de cliente, lo pegamos, a ver si lo pegué bien, bien, si lo pegué bien, de vuelta iniciamos sesión, entramos con nuestra cuenta, no le damos bola a esto, volver a un sitio seguro no, vamos a continuar nosotros continuamos no tenemos miedo a nada continuamos ok no pasa nada es una aplicación nuestra. Listo, ahí tenemos la otra conexión de Google Drive hecha. Vamos con Gmail. Nos va a salir acá la cuenta de la conexión. Así que le vamos a dar, pero nos va a decir que le demos permiso a algunas credenciales. Así que entramos. Acá no necesitamos poner el client ID y el secreto de cliente ninguna de las dos, es mucho más sencillo. Pero ya ven que es cuestión de darle clics a todos los botones que quieran continuar. Es básicamente lo mismo. Seguimos con Calendar y es lo mismo porque ya creamos el proyecto de Google Console que nos va a permitir ya integrar todo, así que bueno vamos 12 minutos ahí lo estoy viendo ya tenemos acá estas cuatro que son las principales y en Docs como ven no tuvimos que hacer absolutamente nada, ya está puesto y en Google Forms lo mismo. Así que nada, como ven acá está todo demostrado, todo el proceso. Esto lo pueden cerrar, ok? Le dan a aceptar y lo cierran. Nos olvidamos de esto. Cosas importantes tener en cuenta que a lo mejor en algún momento tengan que ir acá a conexiones y reautorizar las conexiones a veces cada tanto, cada cierto tiempo. Como les digo en otro video, capaz que lo veamos, pero acá ya lo estoy re-autorizando que no hace falta, porque lo acabo de armar. Pero bueno, capaz se los pide acá a cierto tiempo y lo tengan que hacer. Pero bueno, acá tenemos absolutamente todo conectado. Un título larguísimo este escenario. Pero este es el fin del video, espero que les haya servido un montón. Si tienen alguna duda o algún problema que no está cubierto acá en este video, por favor, si están en school, mándenme un mensaje a robenme. O sea, pongan una duda pero a robenme. Así lo leo y les contesto lo antes posible. Les mando un gran abrazo, se me cuidan y gracias por su tiempo. Nos vemos.
