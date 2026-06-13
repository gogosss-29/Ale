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
