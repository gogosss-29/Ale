# Edición con NanoBanana + Gemini | Oscar

> Ruta: Automatizaciones Make › Edición con NanoBanana + Gemini | Oscar

**🎬 Vídeo (5.1 min):** https://www.loom.com/share/141c4f74002d4ee081c05d9e97e45f03?sid=1e6be8dc-6a60-4731-9b21-9fab402c9f5d

**📎 Recursos:**
- NanoBanana + Gemini

---

Automatización de [Oscar](https://www.skool.com/@oscar-tellez-2612?g=imperio-digital)

### 🎯 **Objetivo**

Transformar imágenes automáticamente usando **Google Gemini y NanoBanana**, logrando resultados visuales profesionales sin necesidad de herramientas de diseño.  
Ideal para **e-commerce, campañas publicitarias o generación de contenido visual** automatizado.

---

### 🔄 **Flujo de la Automatización**

**1️⃣ Preparación de Archivos en Drive**  
🔹 Las imágenes se almacenan en una carpeta de **Google Drive**.  
🔹 Se usa un módulo de búsqueda con límite de 25 elementos para evitar sobrecarga.  
🔹 El sistema detecta automáticamente los archivos que deben ser procesados.

**2️⃣ Descarga y Procesamiento Previo**  
🔹 Se utiliza el módulo **HTTP Get a File** para obtener correctamente el archivo antes de subirlo a Gemini.  
🔹 Este paso es necesario para conservar el tipo MIME correcto y evitar errores de formato.

**3️⃣ Carga en Google Gemini**  
🔹 Se emplea el módulo **Upload a File**, que genera el **URI** necesario para el modelo de imagen.  
🔹 Este URI se conecta con el módulo siguiente para realizar la modificación visual.

**4️⃣ Generación de la Imagen con NanoBanana**  
🔹 En el módulo **Create a Completion**, se selecciona el modelo “**nano-banana-preview**” (versión más estable y de mejor calidad).  
🔹 Se configuran dos mensajes:

- **Usuario:** se adjunta el archivo con su MIME TYPE y URI.
- **Prompt:** se describe la transformación deseada (por ejemplo, “cambiar el fondo”, “mejorar iluminación”, “optimizar para campaña de zapatos”).  
🔹 En *System Instructions* se repite el prompt para mayor precisión.  
🔹 En *Advanced Settings*, se define que la salida debe ser **una imagen**.

**5️⃣ Conversión y Subida del Resultado**  
🔹 El modelo devuelve la imagen en **Base64**, que se transforma con la función *To Binary*.  
🔹 Se carga automáticamente en **Google Drive**, lista para revisión o publicación.  
🔹 Si no se hace la conversión, el archivo resultante queda vacío —por eso este paso es esencial.

---

### 📈 **Resultados**

✅ Imágenes generadas automáticamente con gran fidelidad de color y luz.  
✅ Eliminación del trabajo manual en herramientas de edición.  
✅ Flujo adaptable a campañas publicitarias, catálogos o pruebas visuales rápidas.  
✅ Control total de cada paso dentro de Make, sin intervención humana.

---

### 🔧 **Requisitos Técnicos**

✔️ **Make** – para el flujo principal y gestión de archivos.  
✔️ **Google Drive** – almacenamiento de imágenes originales y finales.  
✔️ **Google Gemini** – procesamiento y modificación de imágenes con IA.  
✔️ **NanoBanana (modelo)** – motor de IA para transformación visual avanzada.

---

### 📝 **Conclusión**

Esta automatización muestra el poder de **combinar Gemini con NanoBanana** para crear procesos visuales inteligentes: desde la detección de archivos hasta la generación automática de nuevas imágenes.  
Un flujo ideal para quienes buscan **ahorrar tiempo en diseño y obtener resultados profesionales** directamente desde su sistema de automatización.

## 🎙️ Transcripción

Hola chicos, les quiero explicar rápidamente cómo utilizar NanoBanana en nuestras automatizaciones. Y tiene un punto malo y es que se ocupan demasiados módulos para llevarlo a cabo, pero pues el resultado es bastante bueno. Mira, vamos a ver. Lo primero es que tengo un flujo de trabajo en donde tengo las fotografías almacenadas en Drive y quiero que se exporten a Drive. En este caso lo que estoy haciendo es modificar una fotografía. entonces aquí lo que estamos haciendo es estamos diciendo exactamente dónde se encuentra la fotografía es decir aquí vamos seleccionando toda esta parte creo que es lo más básico que hay en el que vamos seleccionando donde encontrar las fotografías en las carpetas, aquí le decimos qué tipo de nombre tienen y tal, yo le puse que tenga un límite de 25, también para que no se nos sature, y luego después de esto tenemos que utilizar este módulo http getafile, esto porque, aunque aquí nos de un enlace de descarga, resulta que tiene que pasar por un módulo como éste para que se pueda procesar después en uploadafile de Gemini, porque si no el MIME type, es decir como el tipo de archivo se confunde digamos entonces tiene que pasar por aquí aquí es muy simple simplemente queda file y ponemos aquí éste que es el web control link en caso de que lo suban a dropbox pues igual el enlace es descarga o si lo tienen también en Wordpress también puede funcionar. Y se pasa para acá. Hecho esto, nos vamos a ir aquí a Google Gemini y tenemos que utilizar esta función de Upload a File. Si no la utilizamos no se puede convertir. ¿Por qué? Porque necesitamos aquí una información que es el URI, que solamente nos puede dar este módulo. Entonces lo subimos aquí y simplemente se hace la conexión ya en automático, Get a File. Posteriormente, para hacer las imágenes, aquí no tenemos en Gemini un módulo que es crear imagen pero aquí como queremos lo que queremos hacer es modificarla tenemos que utilizar aquí el módulo de create a completion aquí mismo va a escoger el nano banana Ojo, hay dos nanobananas, uno que si nos vamos aquí al botón de mapear, aparece así, flash image y hay otro que dice preview al final, aquí ese preview es como la versión pasada, entonces hay que mantenerlo con esa para obtener la mejor calidad posible. Ya que lo tengamos aquí, tenemos que poner aquí en los mensajes el primer ítem con un rol de usuario y aquí seleccionamos File y en el módulo anterior nos va a aparecer esta opción que es MIME TYPE y URI, los colocamos aquí posteriormente aquí mismo voy a poner un segundo mensaje que es el PROMPT de que quiero que el fondo tal tal tal tal tal aquí lo Puse pues bastante amplio, digamos, y luego, en System Instructions, estoy poniendo exactamente el mismo prompt. ¿Por qué? Por si acaso. Es importante que, como estamos usando aquí NanoBanana, nos va a devolver usualmente un texto. Entonces, es importante que pongamos aquí el botón de Advanced Settings, y luego pongamos que lo que queremos es una imagen. Todo lo demás lo dejamos vacío. Entonces, ya que ha hecho esto, lo guardamos. Y una vez guardado, aquí viene también otra capa de complejidad, aquí nos crea la imagen pero no las crea como en código, en base 64. Entonces lo que tenemos es que convertir esa imagen en Imagen 64 en lo que es la imagen, en este caso lo estoy subiendo aquí a Drive y para ello nos vamos a seleccionar donde la queremos y tal y cuando pongamos el archivo, aquí está el nombre y tenemos que poner esta parte de aquí, ¿cómo la encontramos? Simple, nos vamos aquí a esta parte de texto y aquí dice To Binary y aquí nos da las indicaciones, Entonces, después de esto vamos a poner aquí este módulo que es algo arrevesado, digamos, porque tenemos que irnos, no a resultados, sino a Candidates, Content, Parts, Online Data. data y data, realmente donde está la imagen es en esta data, en este código, y lo que tenemos que hacer es transformarlo, y para ello tenemos que poner este punto y coma y luego base64, ya una vez hecho esto, ahora si nos va a cargar la imagen, si no lo convertimos a base64 en nuestro drive, donde quiera que los guardemos nos va a aparecer un archivo, pero va a ser un archivo vacío, y pues ya, como un poquito el resultado que tenemos aquí, con ese prawn y tal es esto que nos transformó realmente la imagen en este caso es para la venta de zapato digo hay cosas que mejorar pero en general pues yo lo veo la mayoría bastante bastante bien aquí nos respeta todo el tema de las luces color todo Entonces, bueno, es la manera en que podemos utilizarlo. Y que también me sorprende que me haya dejado hacerlo con niños, afortunadamente. También por eso, un poquito para prevenir esa parte, aquí en el prompt le puse que será usado para una campaña de zapatos, para que no vaya a pensar mal ni nada. Entonces, con eso queda listo y bueno, espero que les sirva.
