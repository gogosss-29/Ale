# Nodo 11: Loop Over Items (El Procesador de Listas)

> Ruta: n8n Desde 0 › Nodo 11: Loop Over Items (El Procesador de Listas)

**🎬 Vídeo (9.5 min):** https://www.loom.com/share/dfc3caab29c24a6f9e7c147b854f560c

**📎 Recursos:**
- 11. Loop Over Items - Mails únicos

---

El Concepto: "La Fila India". Si tienes una planilla de Google Sheets con 50 clientes y quieres mandarles un correo a todos, no puedes hacerlo todo junto en un segundo (Gmail te bloquearía por spam).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/120b6bd309704c1eaa45518f1ecfaff2db804968316f47f696cdaa8734c2356b-md.png)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2342a308b64f48b0b195e32578abc4ca9fba3fc138a74ad580269ae1aab16b11-md.png)

El nodo Loop toma esa lista de 50 filas y dice: "Vamos a atenderlos de a uno. Primero la fila 1, terminamos, y luego la fila 2...".

Ya no solo tienes una fila india de clientes. Ahora, antes de que salgan por la puerta (enviar el mail), los pasas por una oficina donde hay un **Escritor Experto (Tu Agente IA)** que lee sus datos y escribe una carta a mano dedicada solo para ellos.

### **1. La Situación (Escenario Real de Agencia)**

- **El Origen:** Tienes un Google Sheet llamado "Nuevos Prospectos" con dos columnas: Nombre y Email.
- **La Misión:** Quieres enviarles un correo de bienvenida personalizado a cada uno.
- **El Riesgo:** Si envías 50 correos en el mismo segundo, Google detecta comportamiento de robot y te manda a la carpeta de Spam.
- **La Solución:** Usar el Loop para enviar $\rightarrow$ esperar 5 segundos $\rightarrow$ enviar el siguiente.

---

### **2. Paso a Paso: Cómo construirlo**

#### **Paso A: Obtener la Lista (Google Sheets)**

Usemos el google Sheets de antes

1. Agrega el nodo **Google Sheets**.
2. **Operation:** Get Rows (Traer muchas filas). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9c6513b094a945e2912bdb0d7b230f760a0e927f8af24ef58be1ad2b2c134a26-md.png)
3. Selecciona tu hoja ("Nuevos Prospectos").
4. Dale a **"Test Step"**. - *Resultado:* Verás, por ejemplo, **50 globos verdes** (items). Cada uno es una fila de tu Excel. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/01939f03e75947d7aa36d99dcbd4b707552519c74d9b44f2833808c8cdeff9dc-md.png)

#### 

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/41ebf09fa9f24b0bb16a5512e66214cb6c5e5ab0144346ae918b84d7fc9dbc2f.png)

#### **Paso B: Ordenar la Fila (El Loop)**

Ahora tenemos a las 50 personas esperando.

1. Agrega el nodo **Loop Over Items** conectado al Google Sheets. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cb91dfb39a2f43c39168fca982dca7b5eb346602b05d40a785d8a03e5431dbeb-md.png)
2. **Batch Size:** 1. - *(Clave: "Pasa de a 1 fila").* ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/08991652ab9142a2a2fc63002386b6242a4f750616c746dfacfaaa294b158b26-md.png)
3. Dale a **"Test Step"**. - *Resultado:* El Output mostrará solo **1 ítem** (La Fila 1: "Juan Pérez"). El resto espera su turno. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2bed7beadf1544bd88c067242aa9904818bc6cfa93994a948702fc2b19454441-md.png)

#### **Paso C: La Acción (Dentro del Bucle)**

Aquí defines qué le pasa a CADA persona de la lista. Conecta esto a la salida **"Loop"**.

1. **Nodo 1: Wait (Espera)** - Conecta un nodo **Wait** y ponle **5 segundos**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/fa4af90702a340a2abe35966029c4e43ae9127fef23b44f59dea90e5d622790c-md.png)
- *(Esto es higiene digital. Haces que parezca que un humano está enviando los correos, no una máquina).*
2. **Nodo 2: Gmail (El Envío)** - Conecta el Gmail después del Wait.
- **To:** Arrastra el campo Email de tu hoja.
- **Body:** "{{ $json.output }}...". Lo que generamos con el agente
- *(Nota: Como estamos dentro del Loop, $json.Nombre cambiará automáticamente en cada vuelta: primero será Juan, luego María, etc.).* ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8636f2f26f184177886919afc55be22885ff648a08be4f759e6b3ef618bb0ed6-md.png)

---

### **3. Resultado Final**

Al activar el flujo:

1. n8n lee las 50 filas.
2. Toma a Juan (Fila 1) $\rightarrow$ Espera 10 seg $\rightarrow$ Le manda el correo.
3. Vuelve al principio automáticamente.
4. Toma a María (Fila 2) $\rightarrow$ Espera 10 seg $\rightarrow$ Le manda el correo.
5. ... Y así hasta terminar la lista. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2d50e33b91944a1a99f46e9781f256df3db471f0c466497aa58be9380d295c56-md.png)

**3.5 OPCIONAL Agregar un agente **  
  
Paso C: El Cerebro (AI Agent)

Aquí ocurre la magia. Conecta esto a la salida "Loop".

1. Agrega el nodo AI Agent (o Basic LLM Chain). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/bd1ffcce398b4bd1a98f852108cbb9ce1da631b3759f4d0db6c08bff74c0ac92.png)
2. **Model: Conéctale un modelo rápido y barato (ej: gpt-4o-mini o gpt-3.5-turbo) usando el nodo OpenAI Chat Model. En Chat Model lo eliges. Nota, si no h as ingresado t u api key, puedes ver como hacerlo aquí:** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cc887e14b529463b8f719976309d0c3499dc9efdc2664c378eb7af1c0fc2ace1.png) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ed3b794dbaf346dd8fca351dc3d162cef991cb48035c493491ccd6411e6be1fc.png) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/98c3436c5ff44c75a211fb02571bb5d6287ac3330e864a77a7edfb9fe3c43aaf.png)
3. Prompt (El Texto): Aquí le das las instrucciones usando los datos del Loop.  
*"Actúa como un experto en ventas B2B. Redacta un correo corto y persuasivo para {{ $json.Nombre }}, que trabaja en una empresa de {{ $json.Rubro }}. El objetivo es agendar una reunión. Tono: Cercano y profesional. Máximo 50 palabras."*

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9fda85cd4e8245f38dd7b2dab320431fff00d7e6edf5443c83daa9e2bf291d59-md.png)

1. Dale a "Test Step". - *Resultado:* Verás que la IA genera un texto único: *"Hola Juan, sé que la gestión de inventario en una panadería es crítica..."*.

### **4. Criterio (Por qué usarlo)**

- **Entregabilidad:** Es la única forma segura de hacer email marketing masivo desde tu propio Gmail sin caer en spam.

**Personalización:** Puedes usar "Ifs" dentro del Loop. Por ejemplo: *"Si la fila dice 'Cliente VIP', mándale el correo A; si no, mándale el correo B"*. Eso es imposible en herramientas de email marketing tradicionales.
