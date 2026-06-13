# Nodo 10: HTTP Request (El Arquitecto)

> Ruta: n8n Desde 0 › Nodo 10: HTTP Request (El Arquitecto)

**🎬 Vídeo (13.6 min):** https://www.loom.com/share/703cf76fd3874d4aa223d7c5445666ad

**📎 Recursos:**
- 10. HTTP Request - llamado a apps

---

**El Concepto:** "La Verdad Desnuda".   
  
Te voy a contar un secreto: **Todos los nodos de n8n (Gmail, Slack, Google Sheets) son en realidad nodos HTTP Request disfrazados.**   
  
Alguien de la comunidad de n8n simplemente les puso un ícono bonito y campos fáciles para que no tengas que configurar la conexión técnica a mano. Pero cuando ese "disfraz" no existe (porque la app es muy nueva o muy específica), tú te quitas los guantes y usas este nodo para conectarte "a fierro pelado".

### **1. La Situación (Escenario Real Chileno)**

- **El Problema:** Estás armando una automatización para cobrarle a un cliente. Tu servicio vale **10 USD**, pero necesitas enviarle el cobro en **Pesos Chilenos (CLP)** exactos al día de hoy.
- **El Obstáculo:** Buscas en n8n y no existe un nodo "Banco Central de Chile". No hay forma nativa de saber cuánto vale el dólar hoy.
- **La Solución:** Usas el nodo **HTTP Request** para conectarte a una API pública ([Mindicador.cl](http://Mindicador.cl)) y traer el valor en tiempo real.

---

### **2. Paso a Paso: Cómo construirlo**

#### **Paso A: Configurar la Llamada (El Pedido)**

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0509040bc28f47b59a6a12de398f1944a96ae21397a340a2af66a262621cce35.png)

1. Agrega el trigger “chat trigger”, que te permitira hablar en uan caja de texto. Dale a Open Chat y envía solo “50” ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/42212c9c8314400da3864bd86c41a8be4ab1baf3de7b41919f996d236490d202.png)
2. Agrega el nodo **HTTP Request**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/22e79834ebd946e0b311b449bd87ae827561397a242c49a7886a5244e3da2199.png)
3. 
4. **Method:** Déjalo en GET. - *(GET = "Dame info". Es como abrir una página web).*
5. **URL:** Pega esta dirección: [https://mindicador.cl/api](https://mindicador.cl/api) *(Esta es una API chilena gratuita y abierta, ideal para probar).*
6. **Authentication:** None (No pide llave).

Dale a **"Test Step"**.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a0978a270a4c44b8a772d3da71cbd88a9747f4c957c246e4b53d4d92aa14119e-md.png)

#### **Paso B: El Resultado (La Respuesta)**

Mira el Output. Acabas de hablar directo con un servidor externo y te respondió esto:

JSON

{

  "uf": {

    "valor": 36850.55,

    "fecha": "2025-12-08T..."

  },

  "dolar": {

    "valor": 950.20,

    ...

  }

}

#### **Paso C: Usar el Dato**

Ahora ese valor es tuyo. Puedes agregar un nodo siguiente (Edit Fields) y calcular: {{ 10 * $json.uf.valor }} *Resultado: $368.505 (o lo que valga la UF ese día).*  


![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/64705def4009400ab5b1a0ed84ecd499bc028fb78aa841d59ec1b8a5299b1aef.png)

*Asegúrate de eliminar los corchetes {{ y }} para que te queden dentro de una misma expresión*

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/575dc7dd953b486dbb1bc3149509fbbabf3604a1f4c54191a98bf9d710d84ab7.png)

*{{ $('Chat Trigger').item.json.chatInput * $json.dolar.valor }}*

---

### **3. Los Modos del Nodo (El Vocabulario)**

Como dijimos, todos los nodos usan esto por debajo. Aquí están las 4 palabras mágicas de internet:

- **GET:** "Traeme datos" (Consultar UF, Clima, Datos de un RUT).
- **POST:** "Envia datos" (Mandarle un WhatsApp a la API de Meta, crear una factura en un ERP).
- **PUT:** "Actualiza datos" (Cambiar el estado de un pedido).
- **DELETE:** "Borra datos" (Eliminar un usuario). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a020d263505b4251883b1b8dbf6a82b5d14ca34a198b4f4898083152fd1b82cf.png)

### **4. Criterio (Por qué usarlo)**

- **Libertad Total:** Es la diferencia entre ser un usuario que solo usa lo que viene en la caja, y un desarrollador que puede conectar **cualquier software del mundo**. Si tiene API, tú lo controlas.
- **Sin Límites:** Cuando un cliente te diga "¿Se puede conectar con mi CRM raro que hicieron a medida?", tú dices **SÍ**.

## 🎙️ Transcripción

te voy a contar un secreto. Todos los nuevos que estás viendo en N8N, en realidad, son HTTP requests que están difrasados. Sí, suena de rile, pero realmente no lo es. Por ejemplo, este nuevo que está acá para enviar un correo electrónico de Gmail en específico, es un HTTP request que está difrasado. Cada una de las aplicaciones que están acá, eh, vas a darte cuenta de que son exactamente eso. Entonces, qué es lo que tenemos que hacer ahora y cómo funciona? Bueno, existen dos grandes cosas que tienes que entender. El HTML de Berricües tiene que ser así, pero lo único que hace es pedirle permiso a alguien para ir a buscar algo o para mandar algo nada más, ok? Esa es un método que se inventó con alguna razón en los noventas, que seguimos usando y que es el estándar hoy día. Entonces, cuando ves la documentación, apide ciertas aplicaciones, ahí puedes ver qué tan flexibles o cuáles son las cosas que te permiten hacer. Entonces, vamos a mostrar un caso concreto, aquí voy a eliminar este, voy a ponerle un trigger de manual, ok. Aquí tenemos un HTTP request en específico para conseguir el precio del dólar. Lo que estamos haciendo es un método get porque queremos conseguir información y nos da el dólar, el UF, el euro, etcétera, el IPC, la inflación, el UDM, todo al valor de hoy día y actualizado. Tenemos distintas recuerdos porque podemos hacer para conseguir el clima, no tengo idea y después podemos trabajar con estos nojos en específico. Entonces supongamos acá que queremos después la automatización quisimos previamente desembianos un correo que nos vamos a mandar bueno nos vamos a mandar el precio del dólar ok precio dólar hoy vamos a bajar acá y vamos a tener el precio del dólar acá ok y si es que le vamos a ejecutar oops falta el mensaje hola si es que le vamos a ejecutar nuevamente, bueno esta la cuenta, así es que le vamos a ejecutar, ahora sí vamos a recibir el correo. HLDBRequest no es nada más que un nodo disfrazado, solamente que la gente de la comunidad de N8N se ha forzado en hacer estos nodos un poco más bonitos y más simples y más interior para el usuario. Dehamos otro caso que se me ha acabado ocurrir, verdad? Yo, por ejemplo, creo bastante las automatizaciones con Replicate. Replicate es una aplicación que uso para conectar distintos modelos de inteligencia artificial. Si que nos vamos a explorar y nos vamos a los modelos en específico, vamos a ver que podemos llamar todo. Flux2, podemos llamar, no tengo idea acá, ImageTurbo, Gemini3, podemos usar los modelos del anovanana todo y lo interesante es que no te cobra por una suscripción, sino que te cobra por uso, por ejemplo si es que me voy acá a los modelos de imágenes y pongo el imagen for fast vamos a ver que tenemos un cobro por uso que es de dos centavos por imágenes en específico y acá por ejemplo usamos que quiero generar una rana y perrealista con una corona sosteniendo un cartel que dice Hello ok aquí cambiaría lo que quiero el aspect ratio en específico pondría esto output jpj y le daría a correr entonces acá vamos a ver que se está generando la imagen y que debería demorarse unos segundos en este caso se demoró 3 segundos y dice hello ok bastante simple pero si que te fijas acá y te vas a la apiva a ver que tiene una integración ok tenemos integración de api en específico con todo esto que está acá, que se ve terrible pero realmente no lo es, ya te voy a explicar. Si es que nos vamos acá, estamos en el Playground del específico, vamos a ver que tenemos la opción de poner un JSON y un HTTP. JSON vendría siendo las variables, ¿verdad? como esta, que es el prompt, el aspect radio y las variables acá en específico. Pero en JSON, entonces para este caso rana y perrealista con corona, sosteniendo un cartel que dice peja, ok, este va a ser aquí el prompt, entonces aquí va a cambiar el prompt en JSON, ahora si nos vamos a la chete db, vamos a ver que tenemos el chete db estilo post, el tipo de autorización, etcétera, esto suena terrible, pero lo que puedes hacer es copiar esto, todo esto y poner la chargé db como lo puedo crear, pero por modo de simpleza lo voy a hacer, entonces vamos a irnos acá y vamos a crear un HTTP request, tenemos dos grandes tipos de HTTP request, los post y los GET, esos son los que quiero que te quede ahora, que son los GET para extraer alguna información de algún lugar y el post para mandar a hacer una publicación en algún lugar, entonces en este caso yo quiero mandar a hacer algo a este modelo en específico que corre en la nueva, voy a hacer un post y vamos a entrar acá a los URL. Tentro de la HTTP, aquí vamos a ver que hay un URL al final, simplemente lo voy a copiar, después lo voy a pegar acá. Y si es que le doy a execute step, no me da dejar porque dice que no hay una autorización. Que es una autorización, quiero decirle que puedes acceder a mi API a gastar créditos de replicate. Entonces voy a poner acá una autorización generica de estilo bearer esta son la mayoría porque bearer porque aquí sale autorización bearer y después te pides la llave ok bearer es el portador de la llave entonces si tú tienes la llave bear es portar bearer es el portador de la llave de que llave de mi API vamos a irnos acá y voy a poner bearer authentication y voy a crear la nueva creensial, la creensial, paréntesis la puedo conseguir acá si es que me voy aquí arriba a replica y me voy aquí al lado y pongo apetóquense, voy a poder crear una apetóquen y copiarlas, ok? Después la voy a seleccionar acá, que va a hacer esta. Si es que le voy a correr ahora, vamos a ver que no hay un recuest porque no tenemos el JSON, entonces vamos a mandar un cuerpo y vamos a mandarlo en raw, porque en raw, porque me acomodan un poco más. Tipo de aplicación, vamos a ver acá a que nos pregunta cuál es el content type, bueno, Aca aplicación Jason, ¿cuál es el cuerpo que quiero mandar? Ah, quiero mandar en específico el input que es este de acá. Entonces, podemos ver que tenemos todo en orden post arriba, ¿verdad? Authorization, authorization, bearer, después content type, content type raw body y el input en específico que vamos a mandar, bueno es el input que vamos a mandar, le voy a dar acá a expresión y le voy a pegar, ok, entonces ahora si es que voy acá y le voy a ejecutar paso, me voy a decir que todavía no lo puedo hacer, por qué no lo podemos hacer, bueno, ¿por qué? aquí te dice, yo recuerdo este simbali de cunod be process by the server, ¿por qué? ¿por qué? si es que me voy acá y veo en específico qué problema puede estar teniendo el prompt que es este de acá vamos a ver que hay un problema en el request, podemos apretar este botoncito de acá y vamos a ver que Jason se separa con variables de comillas, entonces acá tenemos el prompt es rana hiperrealista con corona se estén en un cartel que dice comillas venja, entonces aquí se confunden entero esto, lo que tenemos que hacer es eliminar las comillas, yo creo que es por eso, ya aquí termina y tenemos entonces valor, o sea, parámetro, parámetro, parámetro, parámetro, parámetro, hay debería funcionar, vamos a hacer el ejecutar y efectivamente se ejecutó, ahora si es que nos vamos acá y vamos a mi cuenta, vamos a ver que vamos a ejecutar una vez más y vamos a ver que debería actualizarse esto y deberíamos mandar a hacer esta animación específico vamos a mandarla una vez más aquí estamos con la duración en específico actualicemos veamos la última que se generó fue el cero acá vamos a hacerlo una vez más 0, 4G es lo que termina el último, y aquí está procesing y esto termina en dole ve de gente, lo que mandamos a hacer fue exactamente esto, una rana y verrealista sosteniendo un cartel que dice veja, ¿verdad? que es esto haga, lo interesante esto y ya aquí sería adelantarme un poco, es que podemos eventualmente hacer nodos de inteligencia artificial acá que nos generen 20 de estas imágenes y lo haga de manera continua y después la cuarta en un drive es realmente interesante y podemos hacerlo con cualquier modelo. Pensa cómo descargo ahora esto, vamos a usar otro nodo que es el HTTP, recués nuevamente, lo recuerdas que te dije que si es que antes, usábamos post para mandar información, usábamos el post para mandar información, bueno, también podemos usar el gate para extraer y recuperarse información. Esto es muy a grande rasgo, porque siempre, siempre hay excepciones a las reglas. Putes para reemplazar, etcétera, pero para en este caso post y gher son los dos esenciales, get, que es lo que quiero traer, bueno quiero traer en específico el get, este, que es lo que nosotros acabamos de generar, lo voy a dar a ejecutar una vez y me pidió nuevamente la autorización, la autorización ya vimos que era una credencia al genérica, bearer de este tipo y ahora sí lo podemos ejecutar y va a devolvernos, cual fue el output este de acá, vamos a abrirlo en la nueva bestaña y vamos a ver que esta es la imagen en específico que nos haga crear realmente interesante. Después si quisieramos podríamos empezar, no tengo idea, incluirla dentro de un correo electrónico para hacerlo aún más interesante, podemos subir la Instagram si es que uno de los nuevos que queremos, pero en fin esta automatización, dos casos en específico que están llamando un modelo de inteligencia artificial en la nube y que está publicándose y extrayendo. entonces acá yo puedo ponerle por ejemplo no tengo idea, puedo modificar esto para que sea una caja de texto en este caso por ejemplo acá chat trigger que es un tipo de trigger que se encadera cuando mandamos un mensaje en la casilla del chat, entonces acá open chat y va a ser como voy a ponerle a-a-a Y cual va a ser prompt ahora, bueno, va a ser a a a o el chat input en específico. Entonces ahora si es que yo lo voy a guardar y lo voy a ejecutar el chat y le pido, supongamos una, no tengo idea, un hombre saltando de un barco hacia otro barco con una army de ranas que están batallando y persiguiéndolos por el océano transatlantico y le voy a enter, ahora sí, vamos a ver que se acaba de generar, acaba de devolver, esto acaba de mandar justamente aquí y si es que ahora la imagen debería ser esta parte de acá, no me la tomó muy bien a lo que quería, pero en fin, por el modelo que estoy usando de inteligencia artificial, ahora te preguntarás porque no me devolvió esto acá y no me dio un output del especifico, porque esto se demoró casi 0 segundos o 0,1 segundos y tenemos un tiempo en especifico acá que se demoró de 4 segundos, entonces aquí tendríamos que agregar un módulo de weight, cuando vamos a esperar, bueno, sabemos que con 8 segundos la podemos lograr bien y esperamos aquí los 8 segundos. Ahora, así es que le damos a ejecutar nuevamente esto y le decimos un nombre mirando al horizonte como llueven hamburguesas y le damos a ejecutar ahora sí vamos a ver que se mandó a hacer precisamente acá seguís el llamado post ya esperamos y ahora acaba de devolverlo que nos devolvió esto acá vamos a abrirlo y vamos a ver qué está el hombre mirando cómo se genera las burguesas y cómo llueve las burguesas y todo esto con dos simples llamados un post y un get bastante increíble increíble esto es algo muy útil muy útil mi recomendación es sé que es alguna aplicación que quieres usar específico que tenga algún llamado htp y no sabes qué hacer entra copia toda esa documentación, pegar, en chargbete, en Gemini, en Cloud, tu herramienta de preferencia y dile, ok, que hago, que hago, y funciona bastante bien.
