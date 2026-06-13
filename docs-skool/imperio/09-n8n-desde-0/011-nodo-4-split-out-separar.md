# Nodo 4: Split Out (Separar)

> Ruta: n8n Desde 0 › Nodo 4: Split Out (Separar)

**🎬 Vídeo (4.4 min):** https://www.loom.com/share/6c1960ded5c4425bbd7f552a5860c015

**📎 Recursos:**
- 4. Split Out - Productos Ecommerce

---

**El Concepto:** "De uno a muchos". A veces n8n recibe un solo "paquete" de datos que adentro trae una lista (como una factura que trae 5 productos). Si quieres procesar esos productos uno por uno (ej: guardarlos en filas distintas de Excel), necesitas "desempaquetarlos" primero.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6e8b67e2718c45cf878c6453af5f641d48c2f7bde16d416e900ec7694f6b930d-md.png)

### **1. La Situación (El Escenario)**

Imagina que tienes una tienda en Shopify o WooCommerce.

- **El Evento:** Entra una orden de compra nueva (Orden #101).
- **El Dato:** Esa orden trae una lista de productos: ["Camiseta", "Gorro", "Calcetines"].
- **El Problema:** n8n ve la orden como **1 solo ítem** (un solo bloque verde). Si conectas un Google Sheets directo, te va a intentar meter los 3 productos en una sola celda fea o solo guardará el primero.
- **La Solución:** Usar **Split Out** para separar esa lista y convertirla en **3 ítems independientes**. Así, los nodos siguientes se ejecutarán 3 veces automáticamente.

---

### **2. Paso a Paso: Cómo construirlo**

Vamos a simular una orden de compra para ver la magia.

#### **Paso A: Crear los datos de prueba (El Paquete)**

Como no tenemos una tienda real conectada ahora, usaremos un nodo de Código para simularlo.

1. Agrega un nodo **Code**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a8758fd183d940de8daed720c6a873c64bb2a297ff0342f1a9f73fc26744dee2-md.png)
2. Pega este JSON en el editor (simula una orden):  
JavaScript

  
return [

  {

    "id_orden": 101,

    "cliente": "Benja",

    "carrito": [

      { "producto": "Laptop", "precio": 1000 },

      { "producto": "Mouse", "precio": 50 },

      { "producto": "Teclado", "precio": 100 }

    ]

  }

];

1. Dale a "Test Step". Verás que sale **1 Item** (color verde). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cb1899f14a134702a7a22c0ff3d422a03aa8bc2d0e3b4d57bd098fc64ce9caa9-md.png)

#### **Paso B: Desempaquetar (La Magia)**

Ahora vamos a separar los productos.

1. Agrega el nodo **Split Out** a continuación. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/99c028024d7646c882dac379889523e55b915854179743b8ad07d5a79896319b-md.png)
2. **Field to Split Out:** Escribe el nombre del campo que contiene la lista. En nuestro ejemplo es: carrito. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/723a38086c8247718a576e0d9d55e9e9327cde19869a403e9d28f8ba383e219f-md.png)
3. **Include Other Fields:** (Opcional pero útil) Déjalo activado si quieres conservar el id_orden y cliente en cada producto.
4. Dale a **"Test Step"**.
5. Agrega un “send email” en gmail: ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ef1b7aa2facc4518be9cc7dc6e63b7dd5fb77fb8de644475a5b464a34320e1b4-md.png)

---

### **3. Resultado Final**

Mira la salida del nodo (Output).

- **Antes:** Tenías 1 ítem (La orden completa).
- **Ahora:** Tienes **3 ítems** separados. - Ítem 1: Laptop (Orden 101)
- Ítem 2: Mouse (Orden 101)
- Ítem 3: Teclado (Orden 101)

Si ahora conectas un nodo de **Google Sheets** (Append Row) después de esto, verás que n8n crea automáticamente **3 filas**, una por cada producto.  


![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/eac42af5cf204367a23144a091e69ac5080fa41d2b7645a6ad8a514534343967-md.png)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1498a30ffaa4406bb1b79e7de8e54928bc81b47d2fc141198402421d105898c4-md.png)

### 

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/53232539cc9a49dbbd745b0579f0f8b74177d601430145bab6b46d5995783403-md.png)

### 

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/71cab768cf4d4aeaafe3f8e56d818b76b829715c33764e0fad4cec91164cc2d0-md.png)

###   
**4. Criterio (Por qué usarlo)**

- **Granularidad:** Te permite trabajar al detalle. Puedes filtrar productos específicos (ej: "Si el precio es mayor a 500, manda alerta") después de separarlos.
- **Orden:** Es fundamental para bases de datos relacionales. No quieres guardar listas separadas por comas en tu CRM, quieres registros limpios.

## 🎙️ Transcripción

Supongamos que tenemos un e-commerce y lo que queremos hacer es agregar cada producto y cada uno de los precios a una hoja de cálculo. Pero el e-commerce, 8b5, por ejemplo, nos devuelve directamente la información. Así, cada vez que ejecutamos este step, vamos a ver que nos devuelve la información que tenemos el carrito y todo metido en un producto carrito 0, 1 y 2 y cuando intentamos de meterlo acá en un sheet, por ejemplo, corremos esta automatización específico, vemos que solamente se nos agrega el primero. ¿Por qué pasa esto? Bueno, porque dentro de esto, vamos a ver que tenemos solamente un item. Este item en específico es el carrito con carrito 0, carrito 1, carrito 2. Ok, tenemos tres items en específico. Paréntesis, casi ser el computador. Paréntesis, aquí estoy ejecutando suplemento un código que no visualiza esto pero vamos a ver que tenemos muchos escenarios donde nos muestra y nos entregar los items de esta misma forma. ¿Cuál sería la solución usar el node splitout? ¿Qué va a pasar cuando usamos splitout? Vamos a ejecutarlo y vamos a ver que ahora sí se va a agregar cada uno de los terprosutos, laptop, mouse y teclado, ¿ok? ¿Por qué pasa esto? Porque el código que recibimos sí que nos lo entregó en una, un bandel o un grupo, split out lo que hizo fue separarlo en tres ítems, producto presión, ok, entonces después pasamos de un item, pasamos a tres ítems en específico y cada item se agregó en un nuevo row, ok, la diferencia, decís que lo hacíamos al revés, vamos a ver que no es uno, tres, sino que es uno y uno, y se agregar un item. Ok, vamos a hacerlo entonces pasabasso. Ahora sabemos y tenemos esto. Tenemos vamos a usar este código en JavaScript que no se asusten es simplemente si es que queremos usarlo de alguna manera y vamos a agregar este nodo de code. Ok, el nodo de code es bastante útil para hacer estas tipo de iteraciones rápidos. Esta iteración lo único que va a ser es devolvernos esto con estos tres productos nada más es por fines prácticos. Ok, vamos a ejecutarlo y vamos a correrlo y vamos a ver quien nos devolvió esto de acá. Lo importante ahora es que sabemos que nos devolvió un item que es este item que aparece aquí. Y ese item lo que queremos hacer ahora es dividirlo. Para ello vamos a usar un módulo que se llama o un nodo que se llama split out, turn inside items into a list of items. Aquí si es que vemos y arrastramos el carrito en específico y ejecutamos una vez esto, vamos a ver que no devuelve de un item y pasa devolvernos 3. Esto es un item y aquí tenemos 3, que son el laptop, verdad? En este producto en específico y tenemos el precio. Más tanto interesante aquí lo podemos ver también en un formato de tabla o en formato JSON. Tenemos el laptop a mil, el mouse a 50 y el teclado a 100. Tenemos también el JSON que lo podemos ver, que es otra manera de visualizar estas cosas. Muy, muy interesante. Entonces, ahora si es que nos vamos acá y vamos a agregar un nuevo row en Google Sheets, haremos el Google Sheets, vamos a agregar un nuevo row en específico que vamos a buscar, bueno, en el Sheets de órdenes y aquí agregamos el Sheets que tendría siendo este de acá, esto lo va a eliminar, por fin es prácticos, ¿qué es lo que vamos a mandar? Bueno, vamos a mandar producto y vamos a mandar precio, pero importante, los de el split out, no los de el código, ahora específico. Ahora si es que, voy acá, conecto esto y le doy a ejecutar, vamos a ver que se va a agregar a cada uno de los shits, ok, después vamos a ver otro en específico que nos va a ayudar a agregar los, entonces ya vamos a ver lo eso en el próximo nuevo pero este es súper súper práctico en el caso de que tengas que manejar grandes listas de datos en específico o listas que no vienen en el formato que tú estás buscando, tienes que hacer un split out para poder separarlo y poder trabajar las de manera independiente.
