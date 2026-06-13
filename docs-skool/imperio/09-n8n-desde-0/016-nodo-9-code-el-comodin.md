# Nodo 9: Code (El Comodín)

> Ruta: n8n Desde 0 › Nodo 9: Code (El Comodín)

**🎬 Vídeo (5.7 min):** https://www.loom.com/share/5e9e1bbca68c42c5880feedbbd728d72

**📎 Recursos:**
- 9. Code - Formateador de Textos

---

**El Concepto:** "El Traductor Universal". A veces los datos vienen sucios, rotos o en formatos raros. Los nodos normales no pueden arreglarlos. El nodo Code es donde metes la basura, ocurre una magia negra (escrita por IA), y sale el dato limpio (que en realidad tiene un millón de casos de uso más)

### **1. La Situación (Escenario Real)**

- **El Problema:** Tienes un formulario donde la gente escribe su nombre como quiere. - Uno pone: "BENJA CORDERO" (Todo mayúscula).
- Otro pone: "benja cordero" (Todo minúscula).
- Otro pone: " Benja Cordero " (Con espacios sobrantes).
- **La Misión:** Tú quieres que en tu base de datos todos entren perfectos: "Benja Cordero" (Capitalizado y sin espacios extra).
- **El Obstáculo:** Hacer esto con nodos normales ("Edit Fields") requiere fórmulas complejas y largas.

---

### **2. Paso a Paso: Cómo construirlo (Modo IA)**

#### **Paso A: Crear el Desastre (Datos Sucios)**

Vamos a simular que entraron datos feos.

1. Agrega un nodo **Code** (sí, el primero, solo para generar datos). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/57a9b9db509f44948fb6792fcf449a435587813992904c468c5d48f04ccd714a.png)
2. Pega esto y dale a ejecutar:  
JavaScript

  
return [

  { "nombre": "BENJA CORDERO" },

  { "nombre": "matias perez" },

  { "nombre": "  JAVIERA   " }

];

1. *(Ves que salen 3 ítems desordenados).* ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4d236aa395454ca49bed9820199433268b6ccbf509684315973a19e0ac1a3a8a-md.png)

#### **Paso B: La Solución (La Magia)**

Aquí es donde entra el truco. No vas a escribir el código.

1. Agrega otro nodo **Code** a continuación.
2. **El Truco:** Vas a ChatGPT (o Claude) y le escribes este prompt:  
*"Tengo un JSON en n8n con un campo 'nombre'. Escríbeme un código Javascript para el nodo Code de n8n que limpie ese campo: quita los espacios extra y ponlo en formato Título (primera letra mayúscula, resto minúscula)."* ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/706bf0fb4cc943c081f73d27a81c1427baa5dbcf46374eb8826d52e6fde28e89.png)
3. La IA te dará algo como esto (puedes copiar y pegarlo ahora):  
JavaScript ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/53179e45799e47bf8e2661a71a76c410169d5428e31242fab798296c6b398b39.png)   
  
for (const item of $input.all()) {

  let nombre = item.json.nombre;

  // Quitar espacios y pasar a minusculas

  nombre = nombre.trim().toLowerCase();

  // Capitalizar cada palabra

  nombre = nombre.replace(/\b\w/g, l => l.toUpperCase());

  item.json.nombre_limpio = nombre;

}

return $input.all();

1. 
2. Pega eso en tu nodo Code y dale a **"Test Step"**.

---

### **3. Resultado Final**

Mira el Output.

- **Entró:** "BENJA CORDERO"
- **Salió:** "Benja Cordero"
- **Entró:** " JAVIERA "
- **Salió:** "Javiera" ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ea7de587a8e6474eafc97489145d0693de9f08184b7c413ab90412580481ae88-md.png)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9a62fb27b1e846ec93b2f0341de8c7c9134e026f37274427afdbbf454b6afb3d.png)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9174e287a7114209bfd19ed8f4800b1606648e1f1516492e8025511b36d647f2.png)

### **4. Criterio (Por qué usarlo)**

- **Potencia:** Hay cosas que los nodos visuales simplemente no pueden hacer bien (como matemáticas complejas, reformatear fechas raras o limpiar textos con reglas difíciles).
- **Velocidad:** En lugar de poner 5 nodos para limpiar un texto (uno para quitar espacios, otro para minúsculas, otro para mayúsculas...), lo haces todo en **un solo nodo Code**.
- **Tu Asistente:** Desde que existe ChatGPT, el nodo Code dejó de ser exclusivo para programadores. Ahora es para cualquiera que sepa explicar lo que necesita.
