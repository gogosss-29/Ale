# Blog con Categorías | Raúl Salazar

> Ruta: Automatizaciones Make › Blog con Categorías | Raúl Salazar

**🎬 Vídeo (20.5 min):** https://www.loom.com/share/73ddb4241aa94be1b51aa8493b84df79?sid=9ebb6bef-9e6c-4208-a479-b20d615a0886

**📎 Recursos:**
- Blog Con Categorías

---

📌 **Plantilla descargable al final del post.**

### **🎯 Objetivo:**

Automatizar la creación de contenido en un blog de **WordPress** generando publicaciones con IA, estructuradas con títulos y categorías optimizadas, además de imágenes generadas automáticamente. Esto permite publicar artículos de manera masiva y sin intervención manual, ideal para blogs de nicho o noticias.

Muchisimas gracias a [Raúl Salazar](https://www.skool.com/@raul-salazar-gonzalez-8895) por esta TREMENDA automatización!

---

## **🔄 Flujo de la Automatización**

### **1️⃣ Base de Datos en Google Sheets**

🔹 Se utiliza una hoja de Google Sheets como punto de partida.  
🔹 Contiene columnas con la **palabra clave principal**, la **categoría asignada**, el **slug (URL personalizada)** y el **estatus de publicación**.  
🔹 Se emplea **Google Translate** para traducir las palabras clave al inglés (requerido para la generación de imágenes).

### **2️⃣ Generación de Keyword Research con IA**

🔹 Un módulo de **OpenAI** realiza un análisis de palabras clave basado en la principal.  
🔹 Se generan hasta **10 palabras clave** adicionales para reforzar el SEO.

### **3️⃣ Creación de Estructura del Contenido**

🔹 Basado en el **Keyword Research**, se estructura el contenido en formato **H1, H2 y H3**.  
🔹 Se genera un **JSON estructurado** para que la automatización pueda reconocer fácilmente los diferentes niveles de encabezados.

### **4️⃣ Generación del Contenido en HTML**

🔹 Se crea el contenido del artículo en base a la estructura de títulos.  
🔹 Se formatea en **HTML** para facilitar su publicación en WordPress.  
🔹 Se extrae el **H1** por separado para asignarlo correctamente en la plataforma.

### **5️⃣ Generación Automática de Imágenes**

🔹 Se usa **Stability AI** para crear imágenes basadas en la palabra clave.  
🔹 Se traduce la palabra clave al inglés para una mejor precisión en la generación.  
🔹 Se ajusta el tamaño de la imagen según los parámetros compatibles con la API.

### **6️⃣ Verificación y Creación de Categorías en WordPress**

🔹 Se consulta si la categoría ya existe en el blog.  
🔹 Si no existe, se crea automáticamente.  
🔹 Si ya existe, se reutiliza sin necesidad de duplicarla.

### **7️⃣ Publicación del Artículo en WordPress**

🔹 Se sube el contenido con el **título (H1), cuerpo en HTML y slug personalizado**.  
🔹 Se asigna la categoría correspondiente.  
🔹 Se agrega la imagen generada como **imagen destacada** del post.

### **8️⃣ Registro de Publicación en Google Sheets**

🔹 Una vez publicado, la automatización marca el **estatus como "Publicado"** en la hoja de Google Sheets.  
🔹 Permite un control total sobre los artículos que han sido creados.

---

## **📈 Resultados:**

✅ Generación de contenido **100% automatizada** para blogs en WordPress.  
✅ Optimización **SEO-friendly** con estructura de encabezados y palabras clave.  
✅ **Publicación masiva y escalable** sin intervención manual.  
✅ Creación de imágenes **low-cost** con IA generativa.  
✅ Control total sobre **categorías y slugs personalizados**.

---

## **🔧 Requisitos:**

✔️ **Google Sheets** – Base de datos y gestión de palabras clave.  
✔️ **OpenAI** – Generación de contenido y análisis de palabras clave.  
✔️ **Stability AI** – Creación de imágenes con IA.  
✔️ **WordPress** – Plataforma de publicación de artículos.  
✔️ **Make** – Orquestación del flujo de automatización.

---

## **📝 Conclusión:**

Esta automatización permite crear y gestionar un blog **completamente autónomo**, ideal para generar tráfico orgánico sin esfuerzo manual. Desde la estructuración del contenido hasta la publicación final en WordPress, todo el proceso se optimiza con **IA y automatización avanzada**. 🚀

Si te interesa probarla, descarga la plantilla y adáptala a tu proyecto. **¡Dudas y mejoras son bienvenidas!** 👇🔥
