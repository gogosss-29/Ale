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

## 🎙️ Transcripción

a continuación vamos a ver un nodo que es clave, ehm, es muy importante y puede hacer muchas cosas porque te vas a ver cuenta que a veces gn8n no puede hacer ciertas cosas, para eso vamos a necesitar el nodo de código, el codo de nodido, el nodo de código, y bastante hermoso, hermoso porque es bastante sencillo y bastante completo, ok, sobre todo cuando nos apoyamos de inteligencia artificial, para este caso supongamos que tenemos un formulario, Este formulario rellena la gente directamente a sus nombres y después queremos pasarlos a un formato en específico Por ejemplo, queremos que todo sea en mayúsculas, o en minúsculas Y la gente simplemente no lo hace así O supongamos que no sea En Chile tenemos un root único identificador Que es un número que identifica que persona eres, verdad, para el estado chileno, para la sociedad, etc Y un número que usamos para todo Y es con puntos y guion entonces hay gente que lo escríbe con puntos, gente que lo escríbe con guiones y si quisieramos estandarizar todo eso usaremos el nuevo de código. Para este caso vamos a hacerlo con nombre, deja Cordero, todo mayúscula, todo minúscula y Javier. Y si ejecutamos esto una vez, vamos a ver que nos lo va a volver así y si es que lo volvemos a ejecutar una vez más, pero está es completo y ponemos el Append Sheets justamente acá, vamos a ver que ahora se va a, ahora sí, déjame conectarlo, que no se conectó bien, se va a agregar con la versión antes y después, me deja cortero, todo mayúscula, menúscula y esto y después es con la B y la se mayúscula, la esme en la P en mayúscula y la jodas mayúscula, esto lo hace este nodo que está, acá que se terrorífico pero realmente no lo es porque vamos a crear lo paso a paso, ok, para este caso simplemente vamos a usar nuevamente este mismo módulo, este nodo en específico que es el ejecutar trigger y vamos a buscar code y vamos a poner en este caso JavaScript, vamos a pegar esto y esto es simplemente de volver lo que estamos poniendo acá, nada más que eso, estos es el tres son los tres items que estamos viendo que los podemos visualizar aquí en la tabla matía javier y venja que nos lo está devolviendo con las mayúsculas en específico ahora si quisieramos estandarizarlas simplemente podemos ir a chargbete y podemos decirle algo por el estilo de tengo un Jason en n8vn con un campo nombre que es este campo de acá nombre escribimos un código Y luego JavaScript para el Node Code de N8N que limpia el campo. Aquí de lo espacio extrae pongo formato título. Primera letra mayúscula y el resto minúscula. Le voy a dar a subir y me da a devolver un campo JavaScript en específico. Return esto, quita lo espacio, repuplaza, no sé qué no sé qué. Y así es simple, se lo explicamos. Entonces después vamos a irnos acá. Vamos a agregar nuevamente el código, vamos a ponerla acá. Code In JavaScript, vamos a copiar lo que está y vamos a ejecutar. vamos a ver si está funcionando y nos funcionó. Después vamos a agregarlo acá al Sheets para hacerlo exactamente igual como lo hicimos previamente para mostrarte y queremos buscar el Sheets en específico. Para este caso es el código 9, este es el Sheets y vamos a poner el nombre antiguo que que es este nombre y el nombre después de haberlo corrió, ok, y ahora si es que ejecutamos esto se va a cargar tres veces y se nos va a actualizar esto, así es sencillo, este no al final la trampa es que lo podemos usar para prácticamente lo que queramos, o sea, estamos ejecutando JavaScript en el entorno de N8N de JSON, entonces es muy, muy práctico para muchas cosas, todo esto nuevamente está tenderizar los routes, por ejemplo, o cuando recibimos una serie de, no tengo idea, de códigos o cosas en específico que queremos tenderizar o crear identificadores únicos, por ejemplo, si tengo una lista grande de ordenes, si quiero crear un identificador único para la orden puede ser como el nombre del cliente, las iniciadas de cliente y abajo, la fecha que lo hizo y abajo o rayita y el producto, no tengo idea, algo así, identificadores únicos son realmente valiosos y los podemos crear así o en el setfils, pero en fin, creo que me estoy escapando un poco, el nodo código es muy útil porque ayuda a ordenar tu caos y tu desastre y para diagnosticarlo con inteligencia artificial es realmente sencillo, o sea si es que por ejemplo este acá simplemente le dije algo como creame otro que sea el return de los tres nombres con el mismo nombre de variable nombre pero que me de tres nombres distintos sólo creame el return este es otro code otro nodo de código como piamos esto nos vamos acá ahora sí cambiamos esto y lo pegamos acá vamos a ver que tenemos el return number 1, return number 2, return number 3, entonces acá lo va a poner 2, 3 y vamos a darle a ejecutar todo una vez para que veas cómo cambia y cómo se adapta y cómo funciona esto, ok, esta plantilla nuevamente también la voy a y te lo voy a dejar pública aquí en la parte de el código.
