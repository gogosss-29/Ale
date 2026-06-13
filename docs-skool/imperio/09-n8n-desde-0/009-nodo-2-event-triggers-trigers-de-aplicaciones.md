# Nodo 2: Event Triggers (Trigers de Aplicaciones)

> Ruta: n8n Desde 0 › Nodo 2: Event Triggers (Trigers de Aplicaciones)

**🎬 Vídeo (4.9 min):** https://www.loom.com/share/6117ed42ecfc46faaadd0c3651ce0376

**📎 Recursos:**
- 2. Event Triggers - Correo VIP

---

**Qué son:** Si el nodo anterior era una "alarma" (por tiempo), este es un **"sensor de movimiento"** o un **"timbre"**. El flujo está dormido esperando que pase algo específico en una aplicación externa para despertar y actuar al instante.

En n8n no hay un nodo llamado "Event Trigger", sino que hay un nodo trigger por cada app: *Gmail Trigger, Slack Trigger, Google Sheets Trigger, Stripe Trigger*, etc.

**Para qué sirve:** Para reaccionar en tiempo real.

- "Apenas me llegue un correo de un cliente, avísame por Slack".
- "Apenas alguien compre en Shopify, agrégalo a la base de datos".

**Ejemplo Concreto (Para recrear):** *Nota: Este requiere conectar una cuenta real (Gmail, Slack, etc.). Si no tienes credenciales a mano, solo visualiza la configuración.*

Vamos a usar el **Gmail Trigger** (el más común):

1. Busca y agrega el nodo **Gmail Trigger** (Ojo: tiene que decir "Trigger", no el nodo normal de Gmail).  
 ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/fdbf287ce2aa4d9596ba5131b427811bb25ee6dcf3ea4457bbbeb0c24ef26f79-md.png)

1. **Event:** Selecciona Message Received.
2. **Filters (La clave):** - Aquí es donde filtras para no disparar el flujo con *spam*.
- Agrega una opción de filtro, por ejemplo: from:[becord00@gmail.com](mailto:becord00@gmail.com)  
  
 ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d6cb37e022db4ddda867243de98ce957dec25601651d4ca49e652ab5a7223e5f-md.png)
3. **Poll Times:** (Esto a veces aparece dependiendo de la versión/conexión). Define cada cuánto revisa, o si usa "Push" (instantáneo).

Luego agrega el resto de la automatización… para este caso haré que me envíe un Whatsapp cada vez que me llegue un correo electrónico.”

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0496fc428e5147fb8b337776a61a4bafadc2996d74b9473fa22b954bb9f46f10.png)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/af46596e0e9b4aabb8e2a0e1181589da1d290ce772a549dab7464e91eda3f9da-md.png)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/efe69f78401e4bf1bb82eb320a0c228c31a3cfc1fa2d427ebe10f550a652f9c2-md.png)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e17f9a6a16334de8a2cb7ae95f1494ae48afa60d9b564ecea2f6a09dda6a0deb.png)

**Resultado:** Tu flujo estará en silencio absoluto. Pero en el segundo que te llegue un correo que en el asunto diga "Urgente", el flujo se dispara y procesa ese correo.

## 🎙️ Transcripción

Ya vimos que teníamos los scheduled trigger o el despertador, ahora vamos a pasar a lo que son los triggers de evento. Estos son bastante útiles dentro de tu 80, porque se ejecutan cada vez que ocurre un evento en específico. Es decir, cuando recibo un mail, cuando recibo un mensaje Slack, cuando se cambia una fila en un rose, cuando se rellenó formulario, Quiero que ejecute la automatización. Esta es bastante útil en 80 int, es decir, el 20% de los nuevos que necesitas para armar el 80% de las aplicaciones, porque está siempre corriendo en segundo plano. Aquí te va a ilustrar con un ejemplo bastante sencillo, que es cuando recibo un correo de un usuario en específico, quiero que me mandes un WhatsApp. Bastante sencillo, lo voy a ejecutar. Una vez, podemos perder ahora mi WhatsApp y debería llegarme uno, ahí me acabo de llegar, y este llegó un mensaje de beja cordero 00, ok, es decir, el correo en específico que quiero hacer. Si es que yo le doy a publicar a este workflow en específico acá, ya vamos a ver cómo lo hacemos, lo voy a decir, Garrett, y entre acá y le digo al correo en específico que es beja roa imperio, tipo conectate al suma hora, estás un tratar de guadón y le voy a enviar. Ahora lo que debería pasar en este caso en específico ya que está activo es que debería llegar al correo electrónico y después me debería mandar un WhatsApp. Ahí podemos ver que está ejecutándose porque lo acabo de recibir y, mirá efectivamente, me llegó un correo electrónico a decir fue éxitos, ¿ok? Para crear este trigger en específico lo que vamos a hacer es bastante sencillo vamos a irnos acá vamos a agregar un nuevo nodo y vamos a buscar cualquiera que sea watch todos los que son watch en específico vamos acá por ejemplo gmail acá y es gmail trigger triggers aquí están on message whistle eso no era watch watcher and make mal a ver on message whistle es decir un trigger de gmail que se va a disparar una vez que recibamos un correo electrónico. Aquí vamos a elegir la cuenta, voy a elegir la mía. Y voy a hacer que cada vez que recibo un mensaje en específico, y aquí tenemos cierto filtro en específico, se ejecute la automatización. Para este caso, lo que hicimos acá en el módulo anterior, bastante sencillo, era ponerle el search, es decir, que sea el from. Aquí también te explican bastante bien cuando abrimos esta parte acá y le ponemos el search, Tenemos que seguir el mismo formato del Gmail search box. Es decir, de acá. Por ejemplo, si es que yo busco B eCord en específico, son los correos que me mando. Y es el From. Entonces, acá vamos a hacer Has, Attachment, O, From, 2.2, B, Cord, 0, 0, Arroba, Gmail. Punto, con su pongamos que este es un cliente Bip con el que estoy trabajando acá. Entonces, lo voy a estar buscando aquí en Gmail en específico. y es from becord. Entonces, ahora sí, es que le doy a fetch, esto va a hacer correr el evento, vamos a ver que recibimos el correo de conecta de al zoom, ahora ya que lo ejecutamos buscando el último caso. Después simplemente voy a copiar y pegar este módulo, que este es el módulo que me permite enviar whatsapps, si es que quieres aprender a conectar porque este no es simplemente hacer uno y otro, ya tenemos que hacer un par de pasos más, pero si quisiera enviar un whatsapp en específico, aquí pondría el mensaje, oye, has esto, esto, esto y lo ponemos aquí justo abajo, ok? Entonces ahora, si es que corremos esta automatización, una vez, debería mandarme un whatsapp en específico con la información, una vez que la Junte, acá, muy importante, paréntese si es que te interesa aprender a hacer esta conexión en específico, tenemos el agentes de whatsapp donde se llamamos el paso a paso, requiere un par de conexiones más pero una vez que lo haces realmente te va a salvar la vida y así funcionaría el event trigger tenemos varios tipos de event trigger si es que haremos acá vamos a agregar los nods y podemos ver los triggers dentro de los triggers tenemos on app event que son los que aparecen acá y tenemos todos estos en específicos sin contar los web juzg sean entonces es bastante interesante porque que por ejemplo si es que yo quisiera hacer algo en AirTable es cada vez que en AirTable pase algo hacemos esto, si quisiera buscar algo en Sheets como cada vez que se agrega una nueva fila en Sheets quiero que se ejecute la automatización lo mismo si es que recibo un mensaje en Slack quiero que pase algo específico, bastante interesante, muy útil sin duda es el uno de los nuevos más importantes que vas a aprender en este 8020.
