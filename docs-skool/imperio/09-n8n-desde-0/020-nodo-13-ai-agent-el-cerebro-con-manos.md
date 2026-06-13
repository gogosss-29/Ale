# Nodo 13: AI Agent (El Cerebro con Manos)

> Ruta: n8n Desde 0 › Nodo 13: AI Agent (El Cerebro con Manos)

**🎬 Vídeo (13.1 min):** https://www.loom.com/share/8a0fe4397aa542168bc7d3c5cc71ab21

**📎 Recursos:**
- 14. AI Agent - Buscador de Pedidos

---

**El Concepto:** "Un Empleado, no solo un Chatbot". Mucha gente confunde esto.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/78117a80602945769a96f644473b3fdc8a765a94fcbe4a6e893a6aa47558f5c0.png)

- **ChatGPT normal (LLM):** Es un cerebro en un frasco. Sabe mucho, pero no puede "hacer" nada. Si le preguntas la hora, no sabe. Si le preguntas por tu stock, inventa.
- **AI Agent:** Es ese mismo cerebro, pero **le pusiste manos y herramientas**. Si no sabe la respuesta, puede ir a Google a buscarla, abrir tu Excel para leer el stock o usar una calculadora. **Razona y ejecuta.**

### **1. La Situación (Escenario Real)**

- **El Cliente:** Te escribe un correo preguntando: *"Hola, ¿dónde está mi pedido #555?"*.
- **El Problema:** Si usas una IA normal (GPT-4) para responder, te dirá: *"Soy una IA, no tengo acceso a tus pedidos"*. Inútil.
- **La Misión:** Quieres que el Agente: 1. **Entienda** que le piden el estado de un pedido.
2. **Use una Herramienta** (vaya a tu Google Sheet de pedidos).
3. **Busque** el #555.
4. **Vea** que dice "En Reparto".
5. **Responda:** *"Hola, tu pedido #555 está en camino 🚚"*.

---

### **2. Paso a Paso: Cómo construirlo**

Este nodo es especial porque necesita "amigos" conectados a él para funcionar.

Supongamos que recibimos un mensaje que simualremos con el Chat Trigger

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d2007b6dc24245518e696fc5f809c0b28e7b7a50d0ea4943a1aabcb5c0174435.png)

#### **Paso A: El Núcleo (El Agente)**

1. Agrega el nodo **AI Agent**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b5bf3759a6514031b008640601cf501f44498887ca6c4be89480974842e03289.png)
2. **Agent Type:** Tools Agent (o Conversational Agent). - *(Esto le dice: "Vas a tener herramientas disponibles").*
3. **Prompt:** Escribe las instrucciones de tu empleado:  
*"Eres un asistente de soporte al cliente de Imperio Digital. Tu trabajo es responder dudas sobre el estado de los pedidos. Tienes acceso a una base de datos. SIEMPRE busca la información antes de responder. Sé amable y breve."}* ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/94245c355d354a1a9630b5855b28c9fb2412d49065d44dfb95cb21c73dd7953c-md.png)

#### **Paso B: El Cerebro (El Modelo)**

El Agente es el cuerpo, necesita un cerebro.

1. Verás un input que dice **Model**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ce73a7e72f004ec28aafd81c5e578c7ad20a4a15b6ea40a79a203f28a9f57ce3.png)
2. Conecta ahí el nodo **OpenAI Chat Model**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ad12c813e2f745218f3a5e535837405efc7e2251dcd540b48cda39bebdd17fcd.png)
3. Selecciona un modelo capaz (mínimo gpt-4.1). Los modelos viejos son tontos para usar herramientas. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/79de707835954fbfba87082fc965dbb47bfe8cc0bca04e30b877ddd722069f06.png)
4. Quizás debas hacer la conexion, para eso te vas a “Create new credential” ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2f9ea0c808fc4f899625c88cbc5386f7eb6e0780b7f54a64a0728062366677c9.png)
5. Entraras a [https://platform.openai.com/api-keys ](https://platform.openai.com/api-keys)y copiaras la API key recien creada ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/29b545becd6b44c6aeb22bb13f9824da6196460baa4b40e79a328804c3a9a017-md.png)

1. La pegarás aqui  
 ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/dbf1cb0e08c942a4a321808b559df9bb5a17648817cd435684629aab65ad22dc-md.png) **Paso C: Las Manos (Las Herramientas)**

Aquí está la magia.

1. Verás un input que dice **Tools**.  
 ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/424731cd365843ddb177bc334f13baccb9a9c9cdfdf746f0b5140f40e7e374ee.png)
2. Conecta ahí una herramienta. - **Ejemplo Básico:** Conecta el nodo **Calculator Tool**. - *Prueba:* Pregúntale al Agente "Cuánto es 543 * 123". En vez de alucinar, usará la calculadora y te dará el dato exacto. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e185fe5488714897b305286c38ec1f891fadb3b3078240a0a7918fd8ed524b74.png)
- **Ejemplo Pro:** Conecta el nodo **Google Sheets Tool** (o crea una "Custom Tool"). - *Prueba:* Al preguntarle por el pedido #555, el Agente irá a leer el Excel solo. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a5a110a73e1e412ba5a330ae06a919395557bf2202a54b46b6673a0b35ca9f44-md.png)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6ec6218790c049de86fa9e416850f4dd09b9e41196194b79bcad38e648363e3f-md.png)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5de7ec9e6b134888ae6840ef83b5360c9b586251f89940feb194d9a73ccb8acd.png)

### **3. Resultado Final**

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a9d1c62afc0345368e375a6217c2d43a00ea624df51248a9ab6037ca585213aa.png)

Cuando ejecutas el flujo:

1. El Agente recibe: "¿Donde esta el pedido 2025-4592?".
2. El Agente **piensa** (verás en el log): *"Necesito buscar el pedido *2025-4592?*. Voy a usar la herramienta Google Sheets"*.
3. Ejecuta la búsqueda.
4. Recibe el dato: "En Reparto".
5. Redacta la respuesta final: *"Hola, revisé y tu pedido va en camino"*.

### **4. Criterio (Por qué usarlo)**

- **Cero Alucinaciones:** La IA ya no inventa datos. Si no encuentra la información en tus herramientas, te dirá "No lo encontré" en lugar de mentir.
- **Autonomía:** No tienes que programar cada paso ("Si dice pedido, ve a sheets..."). Tú solo le das las herramientas y el Agente decide cuándo usarlas. Es como contratar a alguien inteligente.
