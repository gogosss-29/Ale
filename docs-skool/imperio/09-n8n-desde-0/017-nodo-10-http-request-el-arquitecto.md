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
