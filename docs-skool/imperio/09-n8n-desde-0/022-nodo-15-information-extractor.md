# Nodo 15: Information Extractor

> Ruta: n8n Desde 0 › Nodo 15: Information Extractor

**🎬 Vídeo (7.9 min):** https://www.loom.com/share/e01f060cc74e493f80eb868e492e02d7

**📎 Recursos:**
- 15. Information Extractor - Boleta

---

## **El Puente entre la Inteligencia Artificial y la Lógica**

**Workflow: Extracción Inteligente de Datos**

El Concepto: "El Traductor de Burocracia".

Te llega un correo largo, desordenado y aburrido con una factura pegada en el texto.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8ac21d9883f943dea12ba4c51b92f71a859bb74c549244ffbbb02773af1533f7-md.png)

Tú no quieres leerlo. Quieres que el robot lo lea, entienda qué dice, saque solo lo importante (Precio, Cliente, Correo) y decida por ti si es una venta grande o chica.

### **1. La Situación (El Input Desordenado)**

Te llega este texto por correo (simularemos que el cliente escribe como quiere):

*"Hola equipo, adjunto detalle del pago de la empresa ****Constructora Los Andes****. El monto total es de ****$1.500.000**** por los servicios de consultoría de agosto. El contacto es *[***pagos@losandes.cl***](mailto:pagos@losandes.cl)*. Quedo atento."*

**La Misión:**

1. **Extraer:** Convertir ese texto en esto: { "cliente": "Constructora Los Andes", "total": 1500000, "email": "[pagos@losandes.cl](mailto:pagos@losandes.cl)" }.
2. **Clasificar:** Si es más de 1 millón $\rightarrow$ Aviso urgente a Gerencia.

---

### **2. Paso a Paso: Cómo construirlo**

#### **Paso A: El Input (Simular la Factura)**

Como no tenemos un correo real entrando ahora mismo, usaremos un nodo para simular el texto.

1. Agrega un nodo **Edit Fields**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/845eae346390400daba0a0a51bd5e0eebaa763802bd1444c80415965bffda79a.png)
2. Crea un campo llamado texto_correo. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/bc35b73b0f1c4ae6a37c556413db8cf79471db76f827499faebc72dc2e333b17-md.png)
3. **Valor:** Pega el texto del ejemplo de arriba (el de la Constructora).

#### Paso B: El Extractor (Information Extractor)

#### En lugar de escribir un prompt largo rogándole a la IA que te dé JSON, usaremos este nodo que te obliga a ser ordenado.

1. Agrega el nodo Information Extractor conectado al Edit Fields.
2. **Text: Haz clic en el engranaje (Expression) y arrastra tu campo de texto sucio: {{ $json.texto_correo }}** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1aff85e5cdc6416e990f761471c13ac285719b189c65458294d639af045bed75-md.png)
3. **Schema Type: Selecciona From Attribute Descriptions (Esto es clave, aquí defines qué quieres extraer sin código).**
4. Attributes (Define tus variables): Aquí le dices al nodo qué buscar. Agrega 3 atributos: - Atributo 1 (Cliente): - **Name: cliente**
- **Type: String**
- **Description: nombre de la empresa cliente**
- Atributo 2 (Email): - **Name: email**
- **Type: String**
- **Description: correo electrónico de contacto**
- Atributo 3 (Total) - ¡Ojo aquí!: - **Name: total**
- **Type: Cambia esto a Number (En tu foto sale String, pero ponle Number para que el nodo If siguiente funcione directo sin conversiones).**
- **Description: monto total del servicio (solo el número)**
5. Conecta un nodo de cualquier LLM, cualquiera el mas economico bastaría.
6. Dale a "Test Step".

#### Resultado Mágico: El nodo leerá el párrafo y rellenará tus casilleros automáticamente. Obtendrás esto limpio:

#### JSON

#### {

####   "cliente": "Constructora Los Andes",

####   "email": "[pagos@losandes.cl](mailto:pagos@losandes.cl)",

####   "total": 1500000

#### }

#### *Nota: Al usar este nodo, te ahorras el problema de que la IA te responda con texto extra o bloques de código markdown. Siempre te entrega la estructura exacta que definiste en los Atributos.*  
  
  
**Paso D: El Clasificador (Nodo 7: If)**

Ahora que tenemos el dato total: 1500000 limpio, podemos aplicar reglas de negocio.

1. Agrega el nodo **If** conectado al Agente.
2. **Condition:** - **Value 1:** Arrastra el campo total que generó la IA.
- **Operation:** Number -> > (Mayor que).
- **Value 2:** 1000000. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b5e24ad6add74fb9937deb1df058c69cc3c8e38d8e184a1896ce14274d19ef81-md.png)

#### **Paso E: Los Caminos**

1. **True (Venta Grande):** Conecta un nodo gmail y mandale un correo al gerente. - Mensaje: *Boom! 🚀 Venta grande de {{ $*[*json.output.total*](http://json.output.total)* }} por $ {{ $*[*json.output.total*](http://json.output.total)* }}* ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ec41df4bb97046e28dca9c019cef0be34728ac3404674a9d9f6c4d0b09820103-md.png)
2. **False (Venta Normal):** Conecta un nodo **Google Sheets**. - Acción: Guardar el registro silenciosamente en la contabilidad. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6556fa0cf6464875bf4c7693a4cb6be3674daeb72eb942ad938fcdbfb7b81e51-md.png)

---

### **3. Resultado Final**

Acabas de crear un **Procesador de Facturas Automático**.

- No importa si el cliente escribe el correo desordenado, con faltas de ortografía o en otro formato.
- La IA "entiende" y estandariza la información.
- El If toma decisiones financieras basadas en esa comprensión.

### **4. Por qué esto vale oro**

- **Adiós "Data Entry":** Ya no tienes que tener a una persona copiando y pegando datos de correos a Excel.
- **Estructura:** Transformas **Texto Libre** (que es caos y no sirve para nada) en **Base de Datos** (que es orden y sirve para todo).
