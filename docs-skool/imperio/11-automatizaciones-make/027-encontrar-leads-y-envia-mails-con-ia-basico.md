# 🔍 Encontrar Leads y Envía Mails con IA (Básico)

> Ruta: Automatizaciones Make › 🔍 Encontrar Leads y Envía Mails con IA (Básico)

**🎬 Vídeo (9.6 min):** https://www.youtube.com/watch?v=U_78UFwrX7c

**📎 Recursos:**
- Auto Prospección Leads con ChatGPT

---

En este post, te mostraré cómo utilizar la inteligencia artificial para generar miles de leads y automatizar el contacto con ellos. Este método es ideal para agencias de IA o de marketing, pero puedes adaptarlo a cualquier nicho o profesión. Sigue estos pasos prácticos para poner en marcha tu sistema automatizado.

#### Paso 1: Buscar Leads en Google

1. **Definir tu búsqueda**: - Abre Google y prepara tu búsqueda usando la siguiente plantilla: ```
"profesión o nicho" "@gmail.com" OR "@outlook.com" OR "@yahoo.com"
```
- Utiliza `OR` para incluir diferentes dominios populares en tu sector. Esto aumenta las posibilidades de encontrar más emails relevantes
- *Cada palabra entre "comillas" es un filtro de búsqueda. Si le agregamos el OR entre  dos filtros que están con comillas, es encuentra alguno de los que estén al costado. Si no le agregamos el OR, es filtra por cada uno de los resultados que estén entre comillas. *.
- Ejemplo para restaurantes: ```
"Restaurant Chile" "@gmail.com" OR "@outlook.com" OR "@yahoo.com"
``` Bonus
- Si le agregamos antes el "site:[instagram.com](http://instagram.com)", solamente nos mostrará perfiles de instagram. Esta página puede ser reemplazado por cualquier página que estimes conveniente. Por ejemplo: ```
site:instagram.com "Restaurant Chile" "@gmail.com" OR "@outlook.com" OR "@yahoo.com"
```

#### Paso 2: Copiar Resultados de Búsqueda

1. **Seleccionar y copiar resultados**: - Una vez que Google muestre los resultados, selecciona toda la página utilizando `Ctrl + A` y copia con `Ctrl + C`.
- Abre ChatGPT y pega los resultados copiados.
2. **Repetir para más páginas**: - Ve a la segunda página de resultados de Google.
- Repite el proceso de seleccionar (`Ctrl + A`), copiar (`Ctrl + C`) y pegar en ChatGPT.
- Haz esto para al menos 4 o 5 páginas de resultados.

#### Paso 3: Crear una Tabla en ChatGPT

1. **Pedir a ChatGPT que organice los datos**:

- Utiliza el siguiente prompt en ChatGPT para organizar la información: `Crea una tabla con los datos anteriores en estas columnas: Nombre, Nombre de la empresa, URL de la web, Correo electrónico, Número de teléfono, Instagram.`
- *Aquí incluirás solo las variables que encuentres relevante.*

1. **Revisar la tabla generada**: - ChatGPT devolverá una tabla organizada con todos los leads extraídos.

#### Paso 4: Transferir los Datos a Google Sheets

1. **Copiar la tabla**: - Selecciona la tabla generada por ChatGPT y cópiala.
2. **Pegar en Google Sheets**: - Abre Google Sheets y pega los datos copiados en una nueva hoja de cálculo.

#### Paso 5: Automatizar el Envío de Correos con Make

1. **Configurar Google Sheets en Make**: - En Make, añade un módulo de Google Sheets.
- Selecciona "Watch New Rows" y elige el documento y la hoja donde pegaste los datos.
- Configura el límite de filas a 1 para enviar un correo a la vez y evitar ser marcado como spam.
2. **Configurar el módulo de Email en Make**: - Añade un nuevo módulo de "Send an Email".
- Conecta tu cuenta de correo electrónico.
3. **Personalizar el Asunto y el Contenido del Email**:

- En el campo del asunto, utiliza el nombre del destinatario:
- `Por ejemplo, propuesta para {{Nombre completo}}`
- En el contenido del correo, personaliza el mensaje.

1. **Configurar el Envío**: - Configura Make para enviar un correo cada x minutos para evitar ser marcado como spam. (En este caso, es recomendable elegir una mayor cantidad de tiempo para que no te detecten como Spam).

![15.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/22816f1d3edc4ba0bfc52a7073665536b9aaa4d1f47242848d24684a1a1c13f1-md.png)

Siguiendo estos pasos, puedes crear un sistema automatizado y eficiente para generar y contactar leads de cualquier industria o nicho. Este método no solo ahorra tiempo, sino que también incrementa la eficacia de tus campañas de marketing.

## 🎙️ Transcripción

sabemos que la Inteligencia artificial está cambiando la manera en la que hacemos las cosas y hoy día te voy a mostrar un sistema para conseguir leads o clientes potenciales de manera ilimitada usando la Inteligencia artificial y después credenciales entonces lo que vamos a hacer es Vamos a entrar al computador y vamos a buscar en Google cuáles son los mails y los vamos a procesar con Inteligencia artificial entonces supongamos que estamos intentando de ubicar una serie de restauranes que están ubicados en Chile simplemente vamos a copiar y pegar esto que está acá y vamos a poner restaurant chile y le vamos a poner que además incluya @gmail o @outlook de esta manera nos va a dar todos los resultados de los perfiles que incluyan la palabra restorant chile y que además tengan un mail asociado y bonus Podemos agregar Por ejemplo si es que queremos conseguir los instagrams que solamente nos muestre resultados de Instagram Entonces cuando buscamos esto nos va a salir una serie de distintos restauranes como podemos ver acá primer segundo tercer restaurant un dos tres y manualmente lo que hubiésemos tenido que hacer era escribirle a cada uno de estos pero lo que te voy a mostrar ahora es un método mucho más sencillo vamos a apretar control a y vamos a copiar todo y lo vamos a pegar en charg PT después vamos a pasar a la segunda página control a y pegar después tercera página control a copiar y pegar después lo que vamos a hacer es Vamos a entrar a chat gpt y sobre todo le vamos a pedir que nos tener una tabla con el nombre y el mail de contacto gérer columna incluya el nombre del restaurant y en la segunda el mail de contacto además como le pedimos que incluyese el Instagram podemos también pedirle y en la tercera escribe el Instagram Entonces todos estos datos van a estar desorganizados cuando los copiamos y los pegamos pero una vez que le pedimos el prom chat gbt Mira la maravilla que ocurre como podemos ver solamente copiando tres páginas nos dio 1 2 3 4 5 muchos leads que podemos copiar y pegar y ahora podemos automatizar un mail a cada uno de estos tenemos la información de el Instagram de contacto y tenemos el mail de contacto tenemos todo en una tabla Cómo podemos mandarle un mail a todos sin tener que mandárselo manualmente entrando directamente a make.com Pero antes tenemos que pasar est una tabla entonces voy a copiar toda la tabla y abriré una nueva hoja de cálculo en Google sheets Para eso entraré a Google sheets y pegaré los resultados y como podemos ver acá tenemos todo lo que necesitamos nombre del restaurant correo de contacto y el Instagram ya el Instagram es opcional también si es que es algo que te interesa podrías juntar su número pero en fin el siguiente paso que vamos a hacer es nombrar esto y le voy a poner generación de leads restaurant y vamos a entrar a make cuando entremos a make vamos a crear un nuevo escenario y el primer paso es que tenemos que recopilar la información del Google sheets o de la hoja de formulario que acabamos de crear y para eso entraremos a Google sheets bajaremos y le pondremos watch a New Row esto significa que analizará Cuáles son las filas entraremos a make.com iremos acá donde sale spreadsheet ID elegiremos Cuál era el Google sheet donde le cargamos toda la información en este caso es generación de leads restaurant eligiré La hoja uno que es donde está y le pondremos como límite uno esto quiere decir que cuando ejecutemos esta automatización el límite de mails que va a poder mandar es uno cada 15 minutos Luego le vamos a dar a Okay y le vamos a dar a Okay y lo que vamos a hacer después es vamos a agregar un nuevo módulo ahora ya tenem tenemos la información de las personas de la tabla que tenemos acá y lo que tenemos que hacer ahora es mandarle un mail a cada una de estas personas de la tabla y para eso volveremos a make y buscaremos el email y vamos a poner que mande un email y después acá empezamos a rellenar los espacios A quién queremos que le llegue a las personas que están en esta columna en la columna B de correo de contacto para eso vamos a ir a la columna B correo de contacto y aquí se autorellenar con cada casilla de cada uno de los que está acá después Cuál es el asunto que queremos mandarle digamos que quiero ofrecerle mis servicios a todos estos restaurantes para la automatización de clientes y aumentar el remarketing o aumentar la tasa de personas que vuelven al restaur Entonces le voy a decir como asunto algo natural tipo eres el dueño de y aquí lo lindo de esto es que podemos empezar a reinar con las casillas y le vamos a poner acá nombre del restaurante y le vamos a abrir el signo de pregunta lo más natural posible después voy a elegir como texto plano y le vamos a poner el contenido voy a hacer como que fue escrito a mano para que pareciera que le escribí a cada uno de ellos entonces después de elegir el texto plano le podemos rellenar un mail genérico por ejemplo Hola eres el dueño de nombre el restaurant me llamó la atención tu restaurant y te quería preguntar si estás automatizando algún proceso de recolección de mails para aumentar la tasa de personas que vuelven a tu restaurant Yo me dedico a eso si te interesa que conversemos me avisa Saludos aquí se puede rellenar con absolutamente cualquier cosa e incluso se le puede escribir un mensaje personalizado a cada uno con charg PT pero vamos a mantener las cosas básicas Okay entonces después lo que vamos a hacer es vamos a apretar okay Y si es que le damos a correr va a empezar a mandarles un mail cada 15 minutos a cada uno de estas personas y para mostrarte cómo funciona voy a cambiar y voy a editar acá Cuáles son las listas de mails y voy a agregar mi mail de primero entonces supongamos que yo tengo un restaurant que se llama benc Core mi mail es Benja @c.corali y acabo de escuchar mi celular vibrar y si es que entro al mail efectivamente podemos ver que Acabo de recibir el mail Hola eres dueño de Ben corde recordemos que este es el nombre del restaurant La variable que pusimos acá me llamó la atención tu restaurant y te quería preguntar si estás Bueno ya en fin aquí lo pueden personalizar con absolutamente el mensaje que quieran ahora si es que le doy a correr a esta automatización y la prendo cada 15 minutos le va a mandar un mail a la persona siguiente de toda la lista Entonces nos demoramos 20 30 segundos en copiar las cosas en charg bt pegarlos y después Un minuto más en pasarlos a una tabla y una automatización que nos demoró no más de 2 minutos y así puedes juntar una cantidad de leads ilimitados recordemos que también puedes jugar con las variables Por ejemplo si es que no quisiera Buscar en instagram puedo cambiarla acá por ejemplo a cualquier otra página o si es que quiero también puedo eliminar el site Instagram y me van a aparecer las páginas de Instagram las páginas de Facebook también si es que quisiera recolectar los teléfonos también puedo poner los dos corchetes y puedo empezar a pedirle los teléfonos o que incluyan teléfonos y en fin mi punto es que las oportunidades y la cantidad de cosas que se pueden hacer con esto son ilimitadas incluso existen aplicaciones que se dedican a hacer web scrapping directamente de los mails a medida que estás buscando en Google y lo hace por ti pero esta es una manera sers sencilla gratuita que tenemos de contactar a una cantidad de elits que hacerlo manualmente nos demoraría mucho mucho tiempo y esta plantilla que está acá como siempre va a estar publicada en imperio digital si es que no sabes lo que es imperio digital es una comunidad es un espacio donde nos dedicamos a hacer automatizaciones ver herramientas y todas las cosas que puedes necesitar que ayudan a los creadores a potenciar y escalar sus negocios y si bien podríamos haber hecho este video un poquito más complejo quizás en una próxima ocasión o hazme saber en los comentarios si te interesaría que Comencemos a meter la Inteligencia artificial porque por ejemplo una de las cosas que podríamos haber hecho que le podríamos haber pedido a char gpt mediante make es que nos redacte un mail personalizado a cada uno dependiendo del Nicho en el que estaban y decirles Cómo tu solución crees que es la mejor para el Nicho en el que se encu entran por ejemplo pero sin más que decir les deseo mucho éxito y nos vemos en un próximo video adiós
