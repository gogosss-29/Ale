# 🧠 11. Selección de Modelos y Uso de Memoria

> Ruta: Agentes de WhatsApp › 🧠 11. Selección de Modelos y Uso de Memoria

**🎬 Vídeo (8.8 min):** https://www.loom.com/share/7370252a750247d1a351ea9675a35471

---

## **1. Selección de Modelos**

Dentro del nodo del agente puedes elegir cualquier modelo, pero en la práctica solo unos pocos funcionan realmente bien para conversaciones.

### **Modelos recomendados**

**1. GPT-4.1 Mini**  
Ideal para conversación diaria:

- Más humano
- Natural
- Rápido
- Económico

No tiene razonamiento profundo, pero para chats fluidos es perfecto.

**2. GPT-4.1**  
La versión completa, con capacidad de análisis.  
Sirve cuando el agente debe pensar, planificar o resolver algo más complejo.

Puedes ajustar el **Reasoning Effort** para controlar:

- Tiempo de respuesta
- Consumo
- Profundidad del análisis

### **Modelos no recomendados**

**Nano**  
Suele fallar en consistencia. Para agentes conversacionales no es fiable.

---

## **Parámetros clave**

- **Temperature (0.6–0.7):** controla creatividad. Más alto → más riesgo de inventar.
- **Frequency Penalty:** reduce repeticiones.
- **Timeout:** normalmente no requiere cambios.
- **Max Iterations (5):** útil solo si el agente debe ejecutar varias acciones internas.

Estos ajustes te permiten equilibrar calidad, costo y velocidad según el uso del agente.

---

## **2. Memoria del Agente: cómo recuerda**

La memoria define cuánto contexto mantiene el agente entre mensajes.  
Sin una buena configuración, olvida datos, mezcla información o responde incoherente.

### **Opción 1: Memoria simple (nativa de n8n)**

Perfecta para pruebas o agentes pequeños.

Requiere dos cosas:

- **Session key:** en WhatsApp, se usa el *remoteJID* (el número del usuario).
- **Cantidad de mensajes a recordar:** por defecto son 5; para uso real, mejor 20.

### **Opción 2: Memoria con Postgres / Supabase**

Recomendada para producción.

Ventajas:

- Más estable
- Escalable
- Difícil de romper
- Fácil de consultar

En n8n solo creas una credencial de Supabase y el agente ya puede leer/escribir su memoria allí.  
Supabase permite usar Postgres de forma no-code, por eso es tan útil en agentes reales.

---

## **Qué logras con este módulo**

- Elegir el modelo adecuado para tu agente
- Controlar creatividad, razonamiento, velocidad y costos
- Construir memoria estable y escalable
- Evitar pérdidas de contexto y errores comunes
- Preparar un agente listo para producción en WhatsApp, web o cualquier entorno real

## 🎙️ Transcripción

Ahora sí, vamos a ver un poco de los modelos que podemos ponerle a la gente de ella y vamos a ir sobre estos tres puntitos Y como ven acá, de podemos ir agregando, para que quede de esta forma. Primero, tenemos que determinar qué modelo de ia vamos a usar. Nosotros, en este caso, vamos a usar GPT, entonces, la Vamos a poner open Neye y acá vamos a poner la credencial que querramos y acá elegimos el modelo entre todos los que tenemos. Vamos a ir a dar un pequeño repaso. sobre cuando conviene cada modelo. Nosotros generalmente usamos dos o tres modelos solamente. Primero, para lo que hay las conversaciones Usamos 4.1 mini porque vemos que conversa mucho mejor que es mucho más simpático que es más humano, no razona. Es verdad, pero es muy bueno para responder, entonces 4.1 Mini es excelente, realmente Vamos a usarlo en este caso. Después tenemos los morios de resonamiento, que son 4 y 3, que generalmente usamos 4. ¿Qué sucede con O4? Que nosotros podemos poner O4 y acá darle en este par, a Metro Rison in GeForth. Si queremos que piense mucho, si queremos que piense más o menos, o si queremos que piense poco. Esto va a determinar, ¿Cuán va a determinar que respondan mejor o peor o va a determinar que piense más o piense menos? Lo cual hace que responda más lenta. o más rápido y que gaste más o menos tokens, que es la moneda que se consumen o venía y ahí cuando la cuando cuando estás usando, pero bueno, estos andos ejemplos, si quieren poner otros modelos se pueden poner, nosotros vamos a ir con 4 .1 y 4.1 mini este que ven acá otra cosa importante nano no lo recomiendo realmente son muy pocas las veces donde nano ha funcionado bien, a menos a nuestra experiencia, así que siempre con minio 4.1 normal y luego si quede en jugar un poco más tenemos otros parámetros para poner que es el timeout de por ejemplo lo cuánto tiempo queremos que le tome o que te, después de un minuto así como hasta ahora después de un minuto va a parar si le tomas más de un minuto nosotros no usamos esto si usamos Este otro parámetro que es el en donde lo tengo temperatura acá. Esto lo que determina es Juan creativo es ser la gente de ella, generalmente entre 0.4 y uno va a estar muy bien si quieren que sea muy creativo lo pospone en uno en 1.2 pero acá ya vamos a empezar a ver qué alucina que inventa palabras y demás entonces por eso no solo siempre lo usamos en 0.7 o 0. 0.6, tal vez 0,6 y ahí va a estar bien, pueden jugar con otras cosas como por ejemplo lo de la frecuencia panel. y esto es para que no respon, para que no repita tantas cosas, mientras más alto si este valor menos va a repetir las cosas. Sí, después que otro tenemos, bueno, esos son los más importantes, el max aquí traéis que si queremos que he. de que si hace un ritario o sea que si tienes que ejecutar muchas veces el modelo de ya que voy a hacer, sí. 5 y después sí abrigado, yo generalmente lo pongo en 5 o no lo usamos, pero bueno, esto es lo más importante del modelo. Ahora, ya tenemos decidido el modelo, vamos con la memoria. ¿Qué es la memoria? La memoria es imagínense una tabla que va a huar, hablando de la información de la gente de ella de la conversación. Entonces, esto es lo que tenemos que hacer es ver bien según lo que tenemos. que necesitamos hay nosotros usamos dos opciones ahora la que vemos acá es la simple memory que es una memoria que nosotros la conectamos acá le ponemos de nuevo lo mismo si le ponemos esto funcionen igual que la IA. que le tenemos perdón que la gente de ella no le ponemos un mensaje acá o un sesion id acá porque no vamos vamos a usar el chat trigger, sino que le ponemos definir video y acá qué le vamos a dar para la memoria, le tenemos que dar algo que reconozca. un identificador del cliente. Vamos, no. Acá lo que estamos haciendo es crear una tabla. de mensajes, que le va a aparecer o internamente se ve como humano, ella, humano, ella, humano y a eso la conversación es un I. Entonces para poder diferenciar y para poder entender cuando es una conversación de una persona y cuando es su de otra persona, tenemos que poner una key, poner una llave, un identificador, y es de lo tomamos va a ser el número de teléfono porque estamos en WhatsApp entonces vamos a buscar acá donde tenemos el número de teléfono lo podríamos obtener de acá tal vez alguno de estos campos pero luego vamos a agarrar de acá que es el principio que nosotros teníamos, vamos a poner remote hot ID, esto recuerden que es el tercer nodo que teníamos antes. Entonces, nada, por eso es importante formatear y que quede todo súper claro. Y acá, ¿qué otra cosa le ponemos? Esto, ¿cuántas interacciones va a recibir el modelo como contexto? Importantísima, porque muchas veces pasa que la memoria falla, que no tienen tanta memoria, que se olviden las cosas. Entonces, acá lo que hay que hacer. es expandirle la cantidad de mensajes que recibe. Acá, en este caso, va a recibir máximo cinco interacciones. que hacemos es cambiarla a 20 por si se hace larga la conversación ya tenemos modero e chat y tenemos la de la memoria de cómo funciona. Hasta ahora va a funcionar y vamos a ya copiando lo que teníamos acá. Ahora en el próximo video Vamos a trabajar sobre las tools, porque las tools es algo súper, súper importante y se puede realmente expandir muchísimo sobre lo que se puede hacer. con las tools, y es lo que diferencia a una gente de ella de un bot simple. Así que vamos a trabajar ahora en otro vídeo también bastante. de profundizados sobre las tours. Algo muy importante que me olvidé de agregar acá es que esta es una memoria. Sin embargo, yo puedo usar puntos. Por ejemplo, esta, que nosotros es la que más usamos, porque la memoria de N8n se puede romper, usamos Postgres, que nosotros tenemos conectado a una cuenta de SupaBase. Vamos a ir a supabase un segundo porque esto también es muy importante que se vea si nosotros ponemos supabase acá Puedo iniciar sesión y acá vemos que yo tengo una organización RoboSystems y demás y acá tenemos tenemos un montón de tablas. Esto parece súper complejo, súper complejo, pero para poder conectarla es mucho más simple lo que parece. parece. Tenemos vídeos y tenemos también acá siempre si vamos por ejemplo acá a ZupaBasic creo que yo un nodo de SUPA para crear una credencial, yo puedo crear una credencial acá voy a estos documentos y les aparece la guía paso a paso sobre cómo conectar SupaBase y SupaBase que es este. este programa que vemos acá, lo que nos permite es poder tener una memoria de POSGRES, que son dos cosas diferentes pero están muy relacionadas. relacionadas. Ustedes imagínense como que SupaBase es un programa, SupaBase es un una aplicación que usa Postgres, que usa Excel, por decirlo así. Ahora, nosotros a acceder a ese Postgres manualmente, puede ser un poquito difícil o puede ser un poco complejo, técnico, en cambio SupaBase es como que te lo baja a no-code, así. código. Entonces por eso nos conectamos mediante SuperBase a una base ProPosGres, que es lo que tenemos acá. ¡Una vez más! es que todo esto es solamente teoría. Lo importante, lo que tienen que saber es que si van a salir a producción, no busquen usar solamente ésta de la memoria simple porque probablemente les dé problemas. Ahora, busquen crear una cuenta de Supabase, conectarla a N8n y usar la memoria simple. de pósteres, probablemente hagamos un vídeo también detallando cómo hacer paso a paso uno por uno porque es algo súper importante, pero bueno. ahora a este método la memoria simple les va a servir sin ningún problema y si quieren levantarla de postgres bienvenido sea
