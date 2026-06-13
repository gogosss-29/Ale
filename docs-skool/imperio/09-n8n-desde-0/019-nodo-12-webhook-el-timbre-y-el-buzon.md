# Nodo 12: Webhook (El Timbre y el Buzón)

> Ruta: n8n Desde 0 › Nodo 12: Webhook (El Timbre y el Buzón)

**🎬 Vídeo (9.4 min):** https://www.loom.com/share/9284535b97564370a1bac6bad1d1d2ba

**📎 Recursos:**
- 12. Webhook - El Timbre

---

El Concepto: "Tu Dirección Digital".

Imagina que tu automatización vive en una casa cerrada. Para que alguien de afuera (tú mismo, un cliente o una app externa) pueda entrar y decirle "¡Trabaja!", necesita tocar el timbre.

El nodo Webhook te entrega una URL única (un link). Cuando alguien visita ese link, n8n se despierta y ejecuta la tarea.

### **1. La Situación (El Escenario Básico)**

- **El Problema:** Quieres una forma ultra rápida de registrar algo sin abrir mil apps. Por ejemplo: *"Cada vez que llegue a la oficina, quiero apretar un solo botón en mi celular y que quede guardada la hora exacta en un Excel"*.
- **La Solución:** Creas un Webhook en n8n. Ese nodo te da un link. Guardas ese link en los favoritos de tu celular como si fuera una App. Listo, tienes tu botón de fichaje.

---

### **2. Paso a Paso: Cómo construirlo**

#### **Paso A: Crear el Timbre (Configuración)**

1. Busca y agrega el nodo **Webhook**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/258962e9e4b240049f9c62caca150e7289e1d40857d4454c836818c618a3c14f.png)
2. **Authentication:** None (Para que sea público).
3. **HTTP Method:** **GET**. - *(Clave: GET significa que el link se activa simplemente visitándolo).* ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/798f13f0a2a74746aa6bdf7a475aadf722ac267a266947c39195bc3cdaa6a5dc.png)
4. **Path:** Ponle un nombre fácil, ej: fichar-entrada.

#### **Paso B: Probar el Link (La Trampa)**

1. Haz clic en la pestaña **Test URL**.
2. Dale al botón grande **"Listen for Test Event"**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4d5bf2bc4caa4379b5a8aad14a77190da01cfd666fc9469a9b6181db519e5dc3.png)
3. Copia la dirección (.../webhook-test/fichar-entrada).
4. Abre una pestaña nueva en tu navegador, pega el link y dale Enter. - Verás una pantalla blanca que dice: *"Workflow got started"*. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e3bce5dac7a944b19e351fd823c5d65918f3225b8a7643a5bdb49ff13a7716d6.png)
5. Vuelve a n8n. ¡Pum! El nodo se puso verde. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/366b94b790144b939c809e5bb55b4f6f57c8a4d44a8b43cc8f3ee535f55c828f.png)

Ahora lo interesante es que si agregamos una automatizacion despues del webhook como enviar un correo

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/fe0d3cc2bbe648078416e2814b589b5ab1ade8ac0f6840c9841cc2b4067111ac.png)

Ahora cada vez que entremos al link [https://n8n.imperiodigital.cloud/webhook-test/fichar-entrada](https://n8n.imperiodigital.cloud/webhook-test/fichar-entrada)

---

### **3. Lo Interesante (Nivel Pro: Mandar Datos)**

Aquí es donde la cabeza te hace clic.

El Webhook no solo sirve para "tocar el timbre" (GET). También sirve para "pasar una carta por debajo de la puerta" con información específica.

- ¿Cómo funciona?  
En lugar de solo visitar el link, puedes enviarle Datos Estructurados (JSON) usando el método POST (HTTP).
- El Caso de Uso Brillante:  
Imagínate que creas una interfaz o app muy simple (con herramientas como Lovable, Bolt o un formulario web). - En esa app pones tres campos: Accion, Accion, Producto y Precio.
- Cuando le das "Enviar", la app manda esos datos a tu Webhook.
- **Resultado:** n8n recibe el timbreazo Y ADEMÁS recibe el paquete: { "accion": "nueva_venta", "producto": "Pizza", "precio": 10000 }. Con eso, el robot puede hacer la boleta automáticamente.

Básicamente, el Webhook convierte a n8n en el **cerebro (Backend)** de cualquier aplicación o interfaz que quieras inventar.

O supongamos que tienes otra automatizacion y quieres mandarle datos a través de un http request, puedes hacerlo si le pones esto

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5fc87955828a43538a9c40bf47543578138ce71add1849e4bdd28e356c316abf.png)

Y en la otra automatizacion del webhook recibiras algo asi

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/79c45040fd764cf28ec4c01e14e0de74c8d85d681e5a401297df4361b9533eda.png)

---

### **4. Criterio (Por qué usarlo)**

- **Inmediatez:** Es instantáneo. Toco el timbre $\rightarrow$ Se abre la puerta.
- **Flexibilidad Total:** Puedes usarlo como un botón simple (GET) o como un receptor de datos complejo (POST) para conectar apps hechas a la medida.
- **Simplicidad:** Convierte cualquier navegador web en un control remoto para tus bots.
