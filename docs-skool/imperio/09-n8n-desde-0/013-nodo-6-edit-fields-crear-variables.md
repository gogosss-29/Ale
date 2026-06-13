# Nodo 6: Edit Fields (Crear Variables)

> Ruta: n8n Desde 0 › Nodo 6: Edit Fields (Crear Variables)

**🎬 Vídeo (9.8 min):** https://www.loom.com/share/8913d4ce93c046f4bd5eee44e4d0fbcd

**📎 Recursos:**
- 6. Edit Fields - Crear Variables

---

**El Concepto:** "Preparar antes de servir". Entre tener los datos en la mano (del nodo *Aggregate*) y entregarlos al cliente (con el nodo *Gmail*), necesitas un paso intermedio para limpiar, contar y dar formato. Aquí es donde transformas una lista de datos en un mensaje humano.

### **1. La Situación (Continuando tu Flujo)**

- **¿Dónde estamos?** - Vienes del nodo **Aggregate**.
- Tienes un solo ítem con una lista cruda: summary: ["Reunión Cliente", "Gimnasio", "Almuerzo"].
- **El Problema:** - Si conectas esto directo a Gmail, solo puedes pegar la lista tal cual. No puedes poner en el Asunto: *"Benja, hoy tienes ****3**** cosas"*, porque ese número "3" n8n todavía no lo sabe, solo tiene la lista.
- **La Misión:** - Usar **Edit Fields** para crear dos variables nuevas que usaremos en el correo: 1. El conteo total (para el asunto).
2. La lista bonita con saltos de línea (para el cuerpo del correo).

---

### **2. Paso a Paso: Cómo construirlo**

Inserta este nodo justo **después** del *Aggregate* y **antes** del *Gmail*.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cd296f756598409faf1f33813cb950329368191baade407b8528b6d4ac048e0c.png)

#### **Paso A: Crear las Variables**

1. Agrega el nodo **Edit Fields**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/af7fda98e8b440b2adefe4155edb6d157578b3a4a1ee4fe49df75d33d870f2c5.png)
2. **Mode:** Elige Define Below (Mapping Manual).
3. **Campo 1 (El Contador):** - Queremos saber cuántas reuniones hay para ponerlo en el asunto.
- **Name:** cantidad_reuniones
- **Value:** Activa *Expression* y escribe:  
JavaScript

  
{{ $json.summary.length }}

- *(El .length es comando básico de JS que cuenta cuántos ítems hay en la lista. Si tienes 3 reuniones, guardará un 3).* ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c2659f683ef24420a36c5a794f82ae10ef391c28d7434f55b135a68eebad726c-md.png)

1. **Campo 2 (El Formato Visual):** - Queremos que en el correo se vean una debajo de otra, no todas pegadas.
- **Name:** lista_formateada
- **Value:** Activa *Expression* y escribe:  
JavaScript

  
{{ $json.summary.join('<br> - ') }}

- *(El .join une los elementos. Aquí le decimos: "Une las reuniones y pon un salto de línea <br> y un guión - entre cada una").* ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/40c3a7d6547d4eaea86d56a8aa6c1439430107cd253d4f91b867f666632b2d21-md.png)

Dale a **"Test Step"**.

#### **Paso B: El Resultado (Output)**

Ahora el nodo te entregará esto limpio para que lo uses:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9cf6edee2ae5415299cea2bf3c59c949f6212f883b124bcd935e5f439fed2718.png)

JSON

{

  "cantidad_reuniones": 3,

  "lista_formateada": "Reunión Cliente <br> - Gimnasio <br> - Almuerzo"

}

---

### **3. El Remate (Actualizar el Gmail)**

Ahora abres tu nodo **Gmail** (el que ya tenías al final) y cambias lo que habías puesto por tus nuevas variables VIP:

**Subject:** Agenda de hoy: Tienes {{ $json.cantidad_reuniones }} eventos importantes

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e0741d1d3364408a9a471fb2ecd42ed0c756991981cc4c48a80e638d57a15440.png)

**Body (HTML):**  
HTML

  
Hola Benja,<br><br>

Aquí está tu resumen del día:<br>

- {{ $json.lista_formateada }}

<br><br>

¡A darle con todo!  


![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/57b1d5d37d224db8a0ff4d3b5fa88c587969c24a09d54850bc6fcb321db80ee5.png)

### 

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/035eee6fa03a4f17b00d51af0daacc5021b72740a7904369a23935b82f5e26f6.png)

### **4. Criterio (Por qué hacerlo así)**

- **Personalización:** Pasas de enviar un "aviso de robot" a enviar un "asistente ejecutivo". Ese detalle del número en el asunto ("Tienes 3 eventos") aumenta la tasa de apertura.
- **Orden:** Mantienes el nodo de Gmail limpio. Si mañana quieres cambiar el formato de la lista (ej. usar emojis en vez de guiones), solo editas el **Edit Fields** y no tocas el envío de correo.
