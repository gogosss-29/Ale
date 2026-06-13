# Nodo 6: Edit Fields (Crear Variables)

> Ruta: n8n Desde 0 › Nodo 6: Edit Fields (Crear Variables)

**🎬 Vídeo (9.8 min):** https://www.loom.com/share/8913d4ce93c046f4bd5eee44e4d0fbcd

**📎 Recursos:**
- 6. Edit Fields - Crear Variables

---

**El Concepto:** "Preparar antes de servir". Entre tener los datos en la mano (del nodo *Aggregate*) y entregarlos al cliente (con el nodo *Gmail*), necesitas un paso intermedio para limpiar, contar y dar formato. Aquí es donde transformas una lista de datos en un mensaje humano.

### **1. La Situación (Continuando tu Flujo)**

- **¿Dónde estamos?** - Vienes del nodo **Aggregate**.
- Tienes un solo ítem con una lista cruda: summary: ["Reunión Cliente", "Gimnasio", "Almuerzo"].
- **El Problema:** - Si conectas esto directo a Gmail, solo puedes pegar la lista tal cual. No puedes poner en el Asunto: *"Benja, hoy tienes ****3**** cosas"*, porque ese número "3" n8n todavía no lo sabe, solo tiene la lista.
- **La Misión:** - Usar **Edit Fields** para crear dos variables nuevas que usaremos en el correo: 1. El conteo total (para el asunto).
2. La lista bonita con saltos de línea (para el cuerpo del correo).

---

### **2. Paso a Paso: Cómo construirlo**

Inserta este nodo justo **después** del *Aggregate* y **antes** del *Gmail*.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cd296f756598409faf1f33813cb950329368191baade407b8528b6d4ac048e0c.png)

#### **Paso A: Crear las Variables**

1. Agrega el nodo **Edit Fields**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/af7fda98e8b440b2adefe4155edb6d157578b3a4a1ee4fe49df75d33d870f2c5.png)
2. **Mode:** Elige Define Below (Mapping Manual).
3. **Campo 1 (El Contador):** - Queremos saber cuántas reuniones hay para ponerlo en el asunto.
- **Name:** cantidad_reuniones
- **Value:** Activa *Expression* y escribe:  
JavaScript

  
{{ $json.summary.length }}

- *(El .length es comando básico de JS que cuenta cuántos ítems hay en la lista. Si tienes 3 reuniones, guardará un 3).* ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c2659f683ef24420a36c5a794f82ae10ef391c28d7434f55b135a68eebad726c-md.png)

1. **Campo 2 (El Formato Visual):** - Queremos que en el correo se vean una debajo de otra, no todas pegadas.
- **Name:** lista_formateada
- **Value:** Activa *Expression* y escribe:  
JavaScript

  
{{ $json.summary.join('<br> - ') }}

- *(El .join une los elementos. Aquí le decimos: "Une las reuniones y pon un salto de línea <br> y un guión - entre cada una").* ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/40c3a7d6547d4eaea86d56a8aa6c1439430107cd253d4f91b867f666632b2d21-md.png)

Dale a **"Test Step"**.

#### **Paso B: El Resultado (Output)**

Ahora el nodo te entregará esto limpio para que lo uses:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9cf6edee2ae5415299cea2bf3c59c949f6212f883b124bcd935e5f439fed2718.png)

JSON

{

  "cantidad_reuniones": 3,

  "lista_formateada": "Reunión Cliente <br> - Gimnasio <br> - Almuerzo"

}

---

### **3. El Remate (Actualizar el Gmail)**

Ahora abres tu nodo **Gmail** (el que ya tenías al final) y cambias lo que habías puesto por tus nuevas variables VIP:

**Subject:** Agenda de hoy: Tienes {{ $json.cantidad_reuniones }} eventos importantes

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e0741d1d3364408a9a471fb2ecd42ed0c756991981cc4c48a80e638d57a15440.png)

**Body (HTML):**  
HTML

  
Hola Benja,<br><br>

Aquí está tu resumen del día:<br>

- {{ $json.lista_formateada }}

<br><br>

¡A darle con todo!  


![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/57b1d5d37d224db8a0ff4d3b5fa88c587969c24a09d54850bc6fcb321db80ee5.png)

### 

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/035eee6fa03a4f17b00d51af0daacc5021b72740a7904369a23935b82f5e26f6.png)

### **4. Criterio (Por qué hacerlo así)**

- **Personalización:** Pasas de enviar un "aviso de robot" a enviar un "asistente ejecutivo". Ese detalle del número en el asunto ("Tienes 3 eventos") aumenta la tasa de apertura.
- **Orden:** Mantienes el nodo de Gmail limpio. Si mañana quieres cambiar el formato de la lista (ej. usar emojis en vez de guiones), solo editas el **Edit Fields** y no tocas el envío de correo.

## 🎙️ Transcripción

Vamos a suponer que tenemos esta automatización que nos dice, eh, cuáles son nuestros eventos de el día de mañana y se ejecuta a la hora de tomarnos el café, en la automatización que armamos en el móvil anterior, que básicamente funciona así. Cada vez que tenemos un, eh, trigger de tiempo, es decir, un alarmo de espertador que dan las 9 de la mañana, vamos a extraer todos los eventos en específico del día, lo vamos a agrupar y después los vamos a mandar, pero como haríamos si es que quisieramos, por ejemplo, tener el número de eventos basado en, no sé, en la cantidad que hay, aquí entramos uno de los módulos más importantes que vamos a ir usando para mantener las automatizaciones ordenadas y es el edit field, ok, el edit field lo que hace es nos permite literalmente estetiar una variable, eso es todo, no es nada más que eso, antes se llama set fill, ahora está como edit fill directamente o set node en específico, ahora está set fill, ok perdón edit fill que está acá, la automatización específico en este caso lo que hace es el que vimos previamente, pero aquí la agregamos cuánto es el total de reuniones, como lo vamos a hacer, bueno le pedimos un número en específico con el length de cuántas reuniones estamos teniendo en este caso, así que si ejecutamos este paso, vamos a ver que tenemos tres data y como le pusimos el JSON Samaril X nos va a devolver tres, o aquí el resumen de texto donde nos va a separar con una línea y no lo va a crear, pero esto es lo importante, esto da igual al final lo que hicimos, lo importante es que después cuando creemos las otras automatizaciones ya no vamos a tener que sacarlos necesariamente de acá porque ya no sabemos qué es esto no tenemos idea lo que es vamos a poder sacarlos de el nombre de la variable que nosotros creamos y podemos crear la variable que quieramos por ejemplo sumamos que voy acá vamos a agregar un nodo que va a hacer el fill o el set en este caso y vamos a crear no tengo idea aquí el asunto, el asunto va a hacer o la peja como estas y después vamos a ir nos acá al mail, si es que me voy a enviar un correo en específico vamos a ejecutarlo esto una vez y después me voy acá, podemos mandar y poner el asunto acá, eso es lo importante, entonces después puedo crear más de unos 6 que así quisiera, puedo ponerla acá el correo verdad y puedo poner acá el cuerpo que va a hacer cuerpo del correo justamente y ahora si es que ejecuto este paso vamos a ver que nos va a dar tres casos y después simplemente podemos mapear esto acá el correo reo, perdón, el cuerpo y el correo acá y ahora sí, si es que ejecutamos esta automatización que estamos viendo acá, voy a agregarla aquí un nodo de trigger, ahí sí y ejecuto esta automatización, vamos a ver qué, ahora sí, tenía la otra cuenta del correo, vamos a ver que me va a mandar un correo porque ya sabe cuál es el asunto, ya sabe cuál es el correo, ya sabe cuál es el cuerpo, y ahí acabo de recibir el correo electrónico. Ahora sí, vamos a lo importante. ¿Cómo se verían un caso real? Esto ejemplifica bastante bien, el caso real lo sirve bastante también para ir actualizando la última versión de las cosas, hay muchas, muchas cosas prácticas que podemos usar. Para este caso, supongamos que queremos usarlo para no sitiar una variable sino contar el número de cosas que tenemos. Ok, entonces vamos a eliminar esto, vamos a eliminar esto. El módulo anterior vimos que cuando ejecutábamos esto extraíamos la cantidad de datos y los juntábamos en un aggregate. Este aggregate notaba los tres eventos separados. Supongamos que ahora queremos saber para poner el asunto, oye, veja, mañana tienes tres eventos en específico, como lo oriamos. Punto length, nada más, tenemos varias funciones acá como para el join, el length, etcétera, pero para este caso vamos a usar el punto length, porque es lo que nos interesa. Creo que hay bastantes cosas similares o bastantes sencillas en Jason que nos van a ir directamente alivianando la vida por así decirlo, pero vamos a crearlo desde cero. el este es una de ellas que no es algo esencial que aprendas pero bastante otra entonces en el edit fills acá vamos a irnos y vamos a poner acá cuál es el número de reuniones ok queremos que esto sea un número y vamos a trabajar con el summary en específico si es que aquí le ponemos punto vamos a ver que nos salen varias opciones, como el length, includes map filter, oops, punto, tenemos varias cosas, apend join merge varias, pero yo creo que las que vamos a usar para hacer los join y quizás el length, pero esta al final son maneras de poder trabajar la data de una mejor manera, para este caso lo que quiero hacer es que me saque el length, que es el número de elementos dentro de un array. Un array es lo que acabamos de crear, es un conjunto de datos, y si es que ejecuto esto, vamos a ver que el número de reuniones, lo que se espera es, vamos a tu fix de error, trae el número de reuniones, o acta de opción, opción, a perdón, ya es que esto está en array, lo que tenemos que hacer es un number, ahora sí y si lo ejecutamos vamos a ver que esto es 3 ya nos vamos a crear otro que va a ser no tengo idea cuál es el otro que creamos acá vamos ok resumen del texto con este separador de BR vamos a ver el otro punto entonces acá nuevamente Samary lo vamos a poner acá esto no va a hacer una race sino que queremos trabajarlo como string y vamos a ponerle punto join y vamos a los paréntesis y vamos a poner en los coches, que es lo único que quiero, quiero que me lo separe con un BR, no te asusto ese esto, lo único que hace esto es separar BR en formato HTML que es el equivalente a un enter, ok, entonces ahora si es que ejecuto esto va a ser sesión de comandantes, BR e gimnasio BR reunión clientes, en vez de una coma, ahora si es que me voy acá donde sale el correo electrónico va a ser venja tienes vamos a conectarlo venja tienes X número de reuniones mañana ok y después acá nos vamos a ir también a la expresión vamos a poner tipo de email html y vamos a ponerle tu agenda hoy es la poner esto que vendría haciendo el equivalente a un enter y acá ahora sí le voy a poner el sa ma reen específico ya no me gusta trabajar a Samary de hecho le va a poner otro nombre aquí va a ser resumen Reuniones, ahí sí, ya lo dejecutar una vez. Ahora sí, resumen reuniones, entonces quiero hacer tu agenda hoy es 3 reuniones 2 puntitos entre ok vamos a hacer el trigger para si es que está todo funcionando correctamente y si es que ahora está vamos a recibir el cuerpo veja tienes tres mañana me faltó el reunión, lo agenda hoy bueno es tres reuniones aquí se volvió se empezó el día cambiarlo a mañana, mañana es tres reuniones, tienes tres reuniones mañana, ahora sí vamos a la guardar y vamos a la a execute workflow, ahora sí es que revisamos el correo, deberíamos esperar, veja tienes tres reuniones mañana y ahora sí está funcionando bastante bien para que veas el BR es lo único que necesitas aprender de HTML cada vez que pone un BR va a ser un espacio entonces ahora sí que mando este correo vamos a recibir bastantes espacios acá cada BR es un enter aquí pusimos 1, 2, 3, 4 entonces aquí pusimos 1, 2, 3, 4, 5 ya porque el primero también está incluido así que bueno eso es lo que tienes que saber respecto a esto, es muy útil, es una muy buena práctica si es que estamos siempre usando esto, porque a mí me gusta trabajar de una manera ordenada, me gusta setear las variables acá, porque también cuando les hubo las plantillas, por ejemplo, me gusta poder personalizar donde pongo ciertas parámetros, ciertas cosas que sepas que es lo que tienes que dar, así que me gusta usarlo bastante porque me ayuda a ordenarme, ok si lo queremos dejar publicado para que esté funcionando simplemente le vamos a publicar y ahora sí todas las mañana me va a dar que es lo que tengo que hacer mañana
