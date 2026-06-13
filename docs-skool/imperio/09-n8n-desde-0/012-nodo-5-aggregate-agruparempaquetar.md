# Nodo 5: Aggregate (Agrupar/Empaquetar)

> Ruta: n8n Desde 0 › Nodo 5: Aggregate (Agrupar/Empaquetar)

**🎬 Vídeo (7.2 min):** https://www.loom.com/share/318ce960557e470e9a9f5b350d4acd7d

**📎 Recursos:**
- 5. Aggregate - Lista Eventos

---

**El Concepto:** "De muchos a uno". Es exactamente lo contrario al anterior. Es el equivalente al **Array Aggregator** o **Text Aggregator** de Make. Tomas varios ítems sueltos (filas, productos, correos, eventos) y los fusionas en un solo paquete para procesarlos juntos.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/39199f48396d46758293191c4e33932587d8c1ca45ce42df8b98b573417f5a78-md.png)

### **1. La Situación (Tu Caso Real)**

- **Get Eventos:** Buscas en tu Google Calendar los eventos del día. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/132705bf1ecc47c8a8719c4d162d42c0917169dfa977494687a6efe08de9e83c-md.png)
- **El Dato:** Encuentras 4 cosas: *"Sesión 1 a 1", "Gimnasio", "Coaching", "Golf"*. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c8f7b4740a8842ada2618bc53fc19f4dcaa28d1f32174a31b13ef341e59e9e7a.png)
- **El Problema:** Para n8n, estos son **4 ítems separados**. Si conectas el Gmail directo, recibirás 4 correos distintos. Eso es spam para ti mismo. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/dd6ac8cb12454bfda3cf0baf53d6c3be5dc3327d9bd24c47a6f97c22035517e0-md.png)
- **La Solución:** Usas **Aggregate** para meter esas 4 reuniones en una sola lista y enviar **UN solo correo** que diga: *"Aquí está tu agenda completa: Sesión, Gimnasio, Coaching, Golf"*.

---

### **2. Paso a Paso: Cómo construirlo**

#### **Paso A: Obtener los datos (Google Calendar)**

1. Usas el nodo **Google Calendar**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5e7853b99bf14d04bd1ee62d0bcae4e8acdf1993de044369bd6d1472469cb1f8-md.png)
2. Operación: Get Many.
3. **Resultado:** Al probarlo, ves que salen **4 Items** (globos verdes). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f66406d5e118461b87ddee1486c0a5187d8b888288df455185b12d480d852ae0.png)

#### **Paso B: Agrupar (El Embudo)**

Aquí es donde ocurre la magia.

1. Agrega el nodo **Aggregate** después del calendario. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/186df400b0c24db9b8ba11e5391e7c74e9c31588723c4074bdb0b4a4396412a6.png)
2. **Aggregate:** Selecciona Individual Fields (o Specific Fields). - *Por qué:* Porque no quieres toda la basura técnica de Google (IDs, links, zonas horarias), solo quieres los nombres de los eventos.
3. **Fields to Aggregate:** - **Input Field Name:** Escribe summary (que es como Google llama al título del evento).
- *(Opcional)* Puedes cambiarle el nombre de salida, pero dejémoslo en summary. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3b7eb5af7cc843aeabd490a52e0a1b34a07f2e4234e743b98a92e74a3bdd6775-md.png)
4. Dale a **"Execute Step"**.

#### **Paso C: El Resultado**

Mira tu Output (como en tu foto):

- **Antes:** 4 ítems sueltos.
- **Ahora:** **1 solo ítem**.
- **El contenido:** Una lista (Array) que se ve así: summary: ["Sesión 1 a 1 con Ben", "Gimnasio", "Coaching", "Golf"] ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/93633adfb209423d979230f7056f7fabf2c42534d0c945ffaad332be0cea3041-md.png)

#### **Paso D: Enviar el Resumen (Gmail)**

Conecta el nodo **Gmail**.

En el **Body** (cuerpo del mensaje), selecciona el campo summary.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1cac7a29841f4daead6d2e9f7f910fdf6bdac6721efd42debac35020a0292d5b-md.png)

**Truco Pro (Formato):** Como summary ahora es una lista, n8n la escribirá separada por comas. Si quieres que se vea mejor, activa el modo expresión y usa .join:  
JavaScript

- Tu agenda de hoy:
- {{ $json.summary.join(' | ') }}  
  
 ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/326c95cb1a7547e8a1d84dce4d097e77117c1209374a4b9ead5ed14e19b52a01-md.png)   
*Resultado visual:* "Sesión 1 a 1 | Gimnasio | Coaching | Golf".

---

### **3. Criterio (Por qué usarlo)**

- **Anti-Spam:** Fundamental para notificaciones. Nadie quiere 10 mensajes si puede leer 1 resumen.
- **Eficiencia:** Si usas APIs que cobran por llamada (como OpenAI o Twilio), procesar en lote (batch) te ahorra dinero.
- **Orden:** Transformas datos brutos en información digerida lista para tomar decisiones.
