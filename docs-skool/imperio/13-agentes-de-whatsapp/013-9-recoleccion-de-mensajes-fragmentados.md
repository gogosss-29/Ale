# 🔄 9. Recolección de mensajes fragmentados

> Ruta: Agentes de WhatsApp › 🔄 9. Recolección de mensajes fragmentados

**🎬 Vídeo (5.9 min):** https://www.loom.com/share/a54887e7ef0c4c5b9327fc62f4aa6812

---

En este módulo resolvemos un problema muy común en WhatsApp: los usuarios escriben en varios mensajes seguidos. Si tu agente procesara cada uno por separado, perdería contexto y las respuestas serían incoherentes.

Este bloque evita eso agrupando los mensajes fragmentados antes de enviarlos a la IA. Lo que para el usuario son 3, 5 o 10 mensajes escritos rápido, para el modelo se convierte en un único mensaje claro y coherente.

---

### **Cómo funciona**

Cada vez que llega un mensaje:

1. El sistema revisa cuánto pasó desde el mensaje anterior del mismo usuario.  
Si son solo unos segundos, se considera parte de la misma idea.
2. El mensaje se guarda en la tabla **messageBuffer**, registrando: - ID del usuario
- Texto recibido
- Fecha y hora
- Estado (pendiente o procesado)
3. Mientras el usuario sigue escribiendo, el agente no responde todavía; solo acumula.
4. Cuando pasa el tiempo límite sin nuevos mensajes, el sistema: - Une todos los fragmentos
- Forma un único *input* limpio
- Marca la conversación como lista para procesar

Así, la IA recibe algo como:

> “Hola Benja, tengo una duda.  
> Estoy tratando de conectar mi base de Airtable con Make, pero no se me actualiza el estado.  
> Te paso un ejemplo…”

Y no cinco mensajes independientes que cortarían la coherencia.

---

### **Por qué importa tanto**

Este módulo mejora de forma directa:

- La coherencia de las respuestas
- La experiencia del usuario
- La calidad del contexto entregado a la IA
- La estabilidad del flujo completo

También evita problemas como:

- Responder antes de que el usuario termine
- Cortar ideas a la mitad
- Mensajes fuera de orden
- Conversaciones que se sienten “rotas”

---

### **Qué aporta este módulo**

- Un sistema que entiende cómo escriben las personas, no cómo deberían escribir.
- Un agente que espera, escucha y unifica antes de responder.
- La base para conversaciones más naturales, largas y fluidas.

En resumen: convierte escritura humana desordenada en *dato limpio*, para que tu agente responda con la mayor claridad y precisión posible.

## 🎙️ Transcripción

Vamos a ir ahora con el sistema de recolección de mensajes fragmentados, que es este amarillo que ven acá. Este es de los sistemas que por ahí son un poco más confusos y hay también más formas de hacerlo. Nosotros esto muchas veces vemos que falla y se cambia, pero realmente así como está es como más lo tenemos. más mejor funciona usando airtable para hacer la recolección de mensajes fragmentados. Vamos a bajar a tierra. Si yo estoy hablando con una persona, hablando con un bot, estoy hablando por whatsapp, no voy a mandarle siempre el mismo, no voy a mandarle siempre un solo mensaje con la información, sino que por ahí le voy a mandar un mensaje que sea hola y luego le envío otro mensaje que sea cómo estás y luego, veo otro mensaje de ¿tienen tal propiedad a la venta? Por ejemplo, no. O ¿me podrías resolver esta duda? Entonces, Y esto es importante que se entienda, en un plazo de 30 segundos yo le mandé 3 mensajes, pero eso, tres mensajes forman parte de un mismo mensaje. Entonces la tarea de esto que ven acá es esperar esos 30 segundos. para poder armar y para poder recolectar todos los mensajes, formar un solo mensaje y mandárselo a la Inteligencia Artificial. Ahora, ¿qué tiene de bueno esto? Que como tenemos el sistema que vimos recién esto, este reto recolección de mensajes fragmentados, si yo le mando un audio, dos fotos y un mensaje de texto, va a recolectar y va a armarlo todo y lo voy va a llegar todo de una a la inteligencia artificial entonces vamos a ir ya metidos directamente a esto primero qué es lo que pasa se carga el mensaje si yo lo vamos a ejecutar este este campo acá directamente yo lo ejecuto y esto lo que hace es cargar el mensaje que se acaba de cargar ahora, ¿bien? Ahora luego de esto esperamos unos segundos porque Artable no siempre es muy rápido entonces hay que esperarlo y luego volvemos a obtener el primer mensaje para poder comparar después, que esto lo que hace es obtenerlo directamente de esto. ¿Se podría usar directamente esto? Se podría usar esto, pero encontramos que es mejor hacerlo de esta forma, porque hay momentos donde no se carga siempre. y demás. Igualmente, esto creo que hace bastante que no pasa, así que podría funcionar solo, pero acá lo tenemos de esta forma y siempre funciona. es mejor asegurarse. Ahora, después de esto, ¿qué evaluamos acá? Vamos a evaluar si es el primero de la lista si es el primer mensaje que nos llega y esto es importante porque porque si es el primer mensaje que nos llega llega nos va a activar la espera, nos va a activar esos 30 segundos o 10 segundos que es esto que ven acá que hoy son 10 segundos pero que si lo quiero poner en 20 se pone en 20 y ejecutamos entonces hasta ahora qué pasó en teoría. Yo le mandé un mensaje y con ese primer mensaje que se mandó se activa la espera de 20 segundos que yo lo sete ahora el vídeo. Si durante estos 20 segundos se manda otro mensaje, va a ir por esta ruta, y lo único que hace es llegar. a cargar el mensaje y se van a empezar a cargar otros mensajes acá, que esto es algo que dura un par de segundos. segundos. Se carga el mensaje acá y, Luego de esto, vamos a hacerlo, que es lo que sucede acá, hace un geta. obtiene todos los mensajes que ahora de nuevo ahora tenemos uno pero esto en el caso de tener muchos mensajes los acumula. Entonces esto funciona tanto si le mandamos un mensaje como si como si le mandamos varios. Luego, ¿qué sucede? Une todos los mensajes que encuentras y encuentra 1, 2, 3, 4, los une a todos, lo hacemos de esta forma, que esto ya está también armado si hay algún duplicado lo saca, que nos ha pasado que hay veces que se generan duplicados y luego saca se setea la información de la sesión, acá con esto, que en este caso lo importante es esto. Esto vamos a borrarlo, probablemente no nos sirve en este punto. y acá ya lo tenemos que genera limpio, tenemos el mensaje chat input, bien. Ahora, por otro lado, ¿qué sucede una vez que se procesa esto? vamos a borrarlo el mensaje porque no queremos que se acumulen entonces acá se va a correr el wait automáticamente y vamos a borrar los mensajes una vez que tenemos esto que qué resultado tenemos acá que ya en este punto ya tenemos la información del mensaje que queremos queremos que le llegue a la persona, que le llegue a la inteligencia artificial, que es lo que tenemos en este nodo. Si, entonces vamos a hacer un pequeño repaso de esto Todo este sistema que ven acá es para la recolección de mensajes de fragmentados, es para poder mandarle a la IA 3, 4, 5 mensajes a la vez y que se acumulen y no romper la inteligencia de artificial o que no te conteste una vez por mensaje, sino que si yo le mandé tres mensajes seguidos, que me conteste como si fuera un humano, que lo que hace es es esperar, armar todo y contestar. Entonces, esta es la lógica de mensajes fragmentados. Ahora vamos a ir profundizando un poco con el agente.
