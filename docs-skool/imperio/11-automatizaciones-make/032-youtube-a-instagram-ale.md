# YouTube a Instagram | Ale

> Ruta: Automatizaciones Make › YouTube a Instagram | Ale

**📎 Recursos:**
- YouTube a Instagram

---

![b53efe0e7c454f4fbdc88d53baf86409cf84e6c352e54d5fbee8d3db022eda7f.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6403d615625e4d22b32bdd2849718b2105d1dd337a23426f91c9839ef2bb0b96-md.png)

Automatización de [Alejandro Álvarez](https://www.skool.com/@alejandro-alvarez-4462?g=imperio-digital)

📌 **Plantilla descargable al final del post.**

### **Entendamos qué hace**

**🎯 Objetivo:**  
Automatizar la generación de publicaciones en Instagram a partir de un video de YouTube. La automatización extrae la transcripción del video, la procesa y genera un post optimizado para Instagram en formato JSON.

---

### **🔄 Flujo de la Automatización**

#### **1️⃣ Inserción del Link en Google Sheets**

🔹 Se introduce el link del video de YouTube en una hoja de cálculo de Google Sheets.  
🔹 Similar al sistema de automatización de redes sociales de @Benjamin Cordero, donde un enlace sirve como base para generar contenido.

#### **2️⃣ Extracción de la Transcripción del Video**

🔹 Se utiliza una API de transcripción de YouTube obtenida en RapidAPI.  
🔹 Se configura un módulo GET en Make para obtener el texto del video.  
🔹 Se usa la función de **"Ayuda IA"** de Make para generar automáticamente el módulo a partir del código de la API.

#### **3️⃣ Creación del JSON para Instagram**

🔹 Se procesa la transcripción y se genera el formato JSON para la publicación en Instagram.  
🔹 Se reutiliza la estructura de una automatización previa que convertía PDFs en posts de Instagram.

#### **4️⃣ Publicación en Instagram**

🔹 Se conecta el JSON generado con Make para realizar la publicación automatizada en Instagram.  
🔹 Se aseguran los parámetros correctos para evitar errores con asistentes de tonalidad y prompts.

---

### **📈 Resultados:**

✅ Convierte automáticamente videos de YouTube en publicaciones de Instagram.  
✅ Optimiza la creación de contenido sin intervención manual.  
✅ Permite transformar transcripciones en posts atractivos y estructurados.

---

### **🔧 Requisitos:**

✔️ **Google Sheets** – Almacenar y gestionar los enlaces de YouTube.  
✔️ **RapidAPI** – Obtener la transcripción del video.  
✔️ **Make** – Procesar la automatización y publicar en Instagram.  
✔️ **ChatGPT** – Opcionalmente, mejorar y optimizar el texto del post.

---

### **📝 Conclusión:**

Alejandro demuestra cómo integrar herramientas de automatización e IA para transformar contenido de YouTube en publicaciones optimizadas para Instagram. Ideal para creadores de contenido que buscan agilizar su flujo de trabajo en redes sociales. 🚀
