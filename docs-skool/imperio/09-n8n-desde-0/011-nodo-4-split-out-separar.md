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
