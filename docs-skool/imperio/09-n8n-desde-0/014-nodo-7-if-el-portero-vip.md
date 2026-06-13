# Nodo 7: If (El Portero VIP)

> Ruta: n8n Desde 0 › Nodo 7: If (El Portero VIP)

**🎬 Vídeo (6.8 min):** https://www.loom.com/share/268dab2f758c477d87f15714a6168bf0

**📎 Recursos:**
- 7. If - Clasificador de Leads

---

**El Concepto:** "El Cadenero de la Discoteca". Tu formulario es la puerta de entrada. El nodo **If** es el guardia que mira la billetera (el presupuesto) y decide si el cliente pasa a la zona VIP (atención inmediata) o a la fila general (base de datos).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2e98c382752e409eae3982bb4e12704cc8394252eca9419cbe8bdcf3fa26547c.png)

### **1. La Situación (Escenario Real)**

- **La Entrada:** Creas un formulario simple en n8n que le pide al cliente: *"Nombre"* y *"¿Cuál es tu presupuesto?"*.
- **La Regla:** - Si tiene **más de $1.000 USD**: Es un cliente "High Ticket". Quieres que te suene el celular (Notificación urgente).
- Si tiene **menos**: Es un lead normal. Solo lo guardamos en un Excel para contactarlo después.

---

### **2. Paso a Paso: Cómo construirlo**

#### **Paso A: El Formulario (La Puerta)**

1. Busca y agrega el nodo **n8n Form Trigger**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2f9ad232e44445c48bf869685815d063ba5adbdbe4504ac39cbc2364546cf65b-md.png)
2. Ábrelo y verás que puedes diseñar el formulario ahí mismo. - **Form Title:** "Cotización Imperio Digital".
- **Form Fields:** - Dale a *Add Field* -> **Text**. Label: Nombre. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/bc94eb6a688d4c0ea25247b699eebe505dd389db4c0c40d0ba3354dcafceeff4-md.png)
- Dale a *Add Field* -> **Number**. Label: Presupuesto. (Importante que sea *Number* para que el If funcione bien). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f0ba2f1ff1d348c7afc1e8768a9bf14fbf90e2a3ada743d9be424d47f1ff2e72.png)
3. **Testear:** - Dale al botón **"Test Step"** (Waiting for form submission).
- n8n te dará una URL (Link de prueba). Ábrela en otra pestaña.
- Rellénala como si fueras un cliente VIP: Nombre "Elon", Presupuesto 5000. Envíalo. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/01b56f80496d48da83cfc066cb41aa0174863a95e3b9425180d64f05fbd2fcd4-md.png)
- Vuelve a n8n. Verás que el nodo recibió los datos (globo verde). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3af3aa6ee15b47b6bb3580e6886523c195b8bcc9d2054b7faab80c2a32b7df77-md.png)

#### **Paso B: El Filtro (El If)**

Ahora que tenemos el dato "5000" en el sistema, vamos a filtrarlo.

1. Agrega el nodo **If** conectado al Formulario. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/12e207a2c9a14284ac768f707dcc39c69e8832bbfe594bc7b9db040d7ce99d9b.png)
2. **Condition:** - **Value 1:** Arrastra el campo Presupuesto desde el nodo anterior.
- **Operation:** Number -> > (Mayor que).
- **Value 2:** Escribe 1000. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/88d3cea503574a40864375d2ab577cb966ac11b190f742cf955919fed6a59f58-md.png)
3. Dale a **"Test Step"**. - Como pusimos 5000 en el formulario, verás que el dato sale por la salida **True** (Arriba).

#### **Paso C: Los Dos Caminos**

Ahora dale destino a esos clientes.

1. **Camino VIP (Salida True - Arriba):** - Conecta un nodo **Slack**, **Telegram** o **Gmail**.
- Mensaje: *"¡Alerta Benja! Entró {{ $json.Nombre }} con presupuesto de ${{ $json.Presupuesto }}. ¡Atender YA!"*. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/367c303e2f404e8bbe8add2bf93268c7845ec31c448a4d16b9fd8b9a346e8b5f-md.png)
2. **Camino Normal (Salida False - Abajo):** - Conecta un nodo **Google Sheets**.
- Acción: *Append Row* (Agregar fila). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d23cf5f9e1794a908ae1081435d9557862697dc4307d46b98d5a3595e9f02ecd.png) Simplemente guarda los datos para la newsletter o contacto en frío. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/73e656c512a947b18bcedf0b804e09ae52df98ed3549454f934d208ce4cb8ad7-md.png)

---

### **3. Resultado Final**

Acabas de crear un embudo de ventas automatizado en 5 minutos:

- El cliente llena el formulario.
- n8n revisa el dinero automáticamente.
- Tú solo recibes notificaciones de los clientes que valen la pena.

### **4. Criterio (Por qué usarlo así)**

- **Eficiencia Mental:** No pierdas tiempo revisando correos de clientes que no tienen presupuesto. Deja que el bot filtre por ti.
- **Inmediatez:** Al cliente VIP lo contactas en 5 minutos (porque te llegó la alerta), y eso aumenta brutalmente la probabilidad de cierre.

## 🎙️ Transcripción

Supongamos que tenemos un formulario, este formulario va a clasificar los casos que nos sirven o los clientes potenciales que nos sirven de los que no. Este formulario tiene que pasar por dos caminos. El primero es que si es que se cumple los requisitos, quiero que mando correo y si es que no, quiero que se registre en un Google Sheets. Este formulario es un formulario bastante sencillo, donde si es que le doy a ejecutar, rellenamos esto acá, mi nombre es veja, mi presupuesto es de 20.000, le voy a enviar, se ejecuta el escenario. El módulo que vamos a ver ahora es el módulo IF, que es este de acá, en español sería el sí, si es que se cumple esto, anda de por arriba, y si es que no se cumple, anda de por AH. Aquí le ponemos el presupuesto, si es que el presupuesto que recibimos es mayor que mil, andate por arriba y si es que el presupuesto que recibimos es menor que mil, menor o igual, vamos a agregarlo en un Google Sheets. Vamos a agregarlo esto de tercero. Tenemos acá el nuevo nodo, que sería el nodo de Nathan Form. Este es un nodo bastante interesante porque no hemos cubierto antes y es muy útil para hacer cosas rarias. El trigger es cuando hay un nuevo evento. El título va a ser cotizaciones imperiales. Aquí le vamos a poner cotiza tus servicios con nosotros. Vamos a ponerle en el primero que es, ok, cuál es tu correo. Y vamos a poner en la caja, cuál es tu presupuesto. Así es simple. El tipo de elemento acá que queremos en este caso, podemos elegir, queremos que sea texto, email, checkboxes, drop down, etcétera. Para este caso, lo que queremos hacer es este, queremos que sea un email y este queremos que sea texto, ¿ok? Así es simple. Puede ser, o podemos ponerle incluso un número, ¿ok? Vamos a ejecutar, vamos a ver si esto está correcto, aquí le ponemos un número, perfecto, puede rellenarlo, puede hacer la cosidad, aquí vamos a poner levé, vamos a la enviar y está funcionando el formulario, ¿ok? ¿Por qué? Porque recibimos la información y que recibimos el correo al presupuesto y cuando se envió. El siguiente paso es ver si es que esto es alguien con el que queremos trabajar, supongamos que nosotros no hacemos trabajos de menos de 10.000 dólares, ok? Aquí vamos a hacer un nodo if, ya, también está alternativamente el switch que lo vamos a ocurrir en el próximo video, pero tenemos el if, ¿cuál es el if? si es que el número que mandó es mayor que 10.000. Quiero que tu output sea tru. Si es que no, es decir, sea por arriba, tru es verdadero. Si es que no, va a ser false. Entonces subongamos que acá, nuestra idea es mandarle un correo a la persona para que agentes subongamos. Entonces acá vamos a trabajar con el correo y va a hacer algo como clasificaste, escríbeme al whatsapp, tengo idea, y vamos ponerle lo que sea, escríbeme al whatsapp y le vamos a poner aquí el número pero de whatsapp, ok, escribame whatsapp, BR, no sé, este invento número, ya, perfecto, y esto va a ser en el caso, siempre se va al día a cambiar el mail, va a ser el caso de que sea verdadero, en el caso de que sea falso, vamos a simplemente registrarlo en un sheet, vamos a ponerle a new row o a pen row en este caso vamos a buscar el sheets del documento vamos a ponerle en cual puede ser interesante certifier no vamos a ponerlo en orden esta igual en ordenes y vamos a ponerle aquí el correo y aquí el presupuesto. Ahora sí, si es que ejecutamos esto en específico, va a ser cuál es tu correo, vamos de nuevo, vamos con una de mis correos y el presupuesto va a ser 30.000. Así es que así, vamos a ser por arriba y me va a mandar un correo. Si es que dentro acá vamos a ver que efectivamente recibió el correo, la cificaste, escribió el whatsapp y si es que fuese esto mismo con menos que va a ser mil, bueno, en este caso va a ser 9, 9, 9, 9 para que veamos, Submit, vamos a ver que es menor a por ende, el la salida es falsa y si es que abrimos el el sheetz acá vamos a ver que efectivamente ya se registró en el sheetz. Vamos a cambiar de cuenta porque está en la que usó en las órdenes en específico vamos a ver que se registró, ¿ok? Así es sencillo. Así es simple este módulo o este nodo es crucial para las clasificaciones. Tenemos otro tipo de clasificaciones como los de número. Esto es simplemente si es que existe o no existe verdad o si empieza con algunas cosas, perdón los de texto, que si existen o no existe, si que está vacío, no, muy, muy útil, muy práctico, los números también para ser partes lógicas, ne matemáticas, el tiempo, verdad, si es antes o después de cierta fecha, tenemos si existe o si es igual, tenemos los arrays, que tendrías entre las talitas que vimos antes y tenemos los objects, ok, el número tendrías en uno de los que más se usan para terminar de clasificaciones y en mi opinión también usa bastante el que existe o no existe, o sea, si es que existe algo, quiero que haga esto, si es que no existe algo, quiero que haga esto otro. Otro cosa muy importante que vamos a ver en el próximo módulo es el switch, que es este no de acá, que tendría siendo exactamente lo mismo, pero podemos agregar más de un criterio en específico, por ejemplo placa, yo puedo ponerle el switch y agregarle 4 routings distintos para cada uno, en los casos que lo vamos a ver ya en el próximo, no.
