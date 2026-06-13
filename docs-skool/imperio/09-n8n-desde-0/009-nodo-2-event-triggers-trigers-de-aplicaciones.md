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
