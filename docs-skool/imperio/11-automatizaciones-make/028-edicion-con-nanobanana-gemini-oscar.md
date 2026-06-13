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
