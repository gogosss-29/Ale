# Nodo 3: Execute Workflow (Sub-workflows)

> Ruta: n8n Desde 0 › Nodo 3: Execute Workflow (Sub-workflows)

**🎬 Vídeo (10.5 min):** https://www.loom.com/share/cd73f83e85964a41a90e384d938d3e09

**📎 Recursos:**
- 3.a Execute Workflow (JEFE)
- 3.b Sub-flujo (HIJO)

---

**El Concepto:** "Delegar tareas repetitivas". En lugar de que tu flujo principal haga todo el trabajo sucio (y se vuelva gigante), le pasa la tarea final a un flujo especializado. Aquí separaremos al **"Cerebro"** (quien piensa qué decir) del **"Brazo"** (quien envía el mensaje).

### **1. La Situación (El Escenario)**

Estás armando una automatización para **Imperio Digital**.

1. **El Jefe (Main Workflow):** Detecta un correo entrante de un cliente, lo lee y usa Inteligencia Artificial para redactar una respuesta personalizada.
2. **El Mensajero (Sub-workflow):** Es un flujo tonto pero eficiente. Solo sabe recibir un texto y enviarlo por correo (o WhatsApp).

**¿Por qué separarlos?** Porque si mañana quieres dejar de enviar correos y empezar a enviar WhatsApps, **solo modificas al "Mensajero"**. El "Jefe" (la IA y la lógica) sigue funcionando igual sin que tengas que tocarlo.

---

### **2. Paso a Paso: Cómo construirlo**

*Nota: Siempre construye primero al "Empleado" (Sub-workflow) para que el "Jefe" tenga a quién llamar.*

#### **Paso A: Crear el Sub-flujo ("El Mensajero")**

Este flujo recibe la carta y la pone en el buzón.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/83d78f237a134f0786d32b4e6128831fa968883d5c1c4c3aa5e0220d95027570-md.png)

1. **Nuevo Workflow:** Crea uno nuevo y llámalo 3.b Sub-flujo "El Mensajero".
2. **El Trigger:** - Busca el nodo **Execute Workflow Trigger**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c5f4cec8e58244ee866bc85363378ec3b5015869fb974800a05bfe7e325278ab.png)
- **Configuración:** En "Input Data Mode" elige Define using fields below. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/edecc230588b4e29aca6c8e1e75f735e666d8fd9ac884f2d9515e9576969e868.png)
- **Campos:** Agrega un campo nuevo, nombre mensaje, tipo String.
- *(Esto crea la "puerta de entrada" para recibir el texto).*
3. **La Acción (Gmail Send):** - Agrega un nodo **Gmail** (o Send Email). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e26b0caee1924f6d8facb1c3c999d4a190822a9f37134c61bfc216bd8023c281.png)
- **Acción:** Send.
- **Message:** Aquí no escribas texto fijo. Arrastra la variable mensaje desde el input del trigger (se verá algo como {{ $json.mensaje }}). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a0adf8d023d148fb803ddfa94540038dd5ee4a1fe1ac4175a5c0d540c309be85-md.png)
4. **Guardar:** Dale a Save y **actívalo** (switch arriba a la derecha).

#### **Paso B: Crear el Flujo Principal ("El Jefe")**

Este flujo escucha, piensa y da la orden.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e88be3471c264baebc974054712d477a78bb3240e2fb4b7b9612953545fd50dc-md.png)

1. **Nuevo Workflow:** Crea uno nuevo y llámalo 3.a Execute Workflow ("El Jefe").
2. **El Trigger (Oído):** - Nodo **Gmail Trigger**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/18686a632d8d4ba1ba3d036b73bebc992b69cf2dbab24cbeaf8f34c04715e2a3.png)
- Filtra para que detecte correos específicos (ej. from:[becord00@gmail.com](mailto:becord00@gmail.com)). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1a592196afe349a8a7627660f94a0d43034c0f19710249d38e540d4f737e78a4-md.png)
3. **El Cerebro (AI Agent):** - Conecta tu nodo de **AI Agent** + **OpenAI Model**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/82f9c2b23bdc4d66b08febe5a458da965f550f7d5e624c9a8ba5b854fa7058aa.png)
- **Prompt:** "Redacta una respuesta amable y breve para este correo: {{ $json.snippet }}". ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cb58d9ac301a40bdb3b586a2fa58ac20a787142f606b408488ad22a704827ca1.png) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9032198abc574a67a9d7c6830b0af08b4bf328a851e545699facea982e3fe688.png)
4. **La Orden (Execute Workflow):** - Agrega el nodo **Execute Sub Workflow**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/bfdab48395d845ef9f583d91e41040c166ae3904322746b6844cb2d126264086-md.png)
- **Source:** Database.
- **Workflow:** Selecciona de la lista a 3.b Sub-flujo "El Mensajero". ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/279130e28f2d497ba49fbcf0a6466f3447313eb65fc1488caa97827e41e2a17f.png)
- **Workflow Input:** Selecciona Mensaje. (si no te aparece el mensaje tienes que darle a “Execute Workflow” una vez) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1712c46467234df494f5318865aab00f0c7ef0272c8c4d2797c524da9482b2dd-md.png)
- **Mapeo:** Verás que aparece el campo mensaje que creaste en el otro flujo. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/71aa9878e0524784bb7b1ee0aff422297947a77116db47a084c06c8d515e57f7-md.png)
- **Valor:** Arrastra aquí el **Output** (la respuesta generada) del nodo de IA Agent (ej. {{ $json.output }}).

---

### **3. Resultado Final**

Cuando llegue un correo:

1. **El Jefe** lo lee y la IA escribe el borrador. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a8f4e2c94b8c497b868aa4a7fd243111d6c03e3a1d9946ebb352514cab3e2b46-md.png)
2. El nodo **Execute Workflow** toma ese borrador y se lo pasa "en mano" al otro flujo. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/18aa09af3d1c4835890a437df14d42d1248c76af240a4dc49899ee8b043b6cf4.png)

1. **El Mensajero** despierta, recibe el texto y lo envía al destinatario final. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f05ee08d01c04792bdfa16c8fcb526fe3233ddd46e964bbbaa4deebc6f2f94ee.png)

### **4. Criterio (Por qué usarlo)**

Esta estructura es profesional porque **desacopla** la lógica.

- Si falla el envío de correos, no pierdes la lógica de la IA.
- Puedes reutilizar al "Mensajero" en 10 automatizaciones distintas (Ventas, Soporte, Reclamos) sin configurar Gmail 10 veces.
