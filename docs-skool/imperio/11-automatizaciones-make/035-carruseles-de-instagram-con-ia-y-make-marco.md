# Carruseles de Instagram con IA y Make | Marco

> Ruta: Automatizaciones Make › Carruseles de Instagram con IA y Make | Marco

**🎬 Vídeo (20.5 min):** https://www.youtube.com/watch?time_continue=10&v=FZZru_4VEQQ&embeds_referring_euri=https%3A%2F%2Fwww.skool.com%2F&embeds_referring_origin=https%3A%2F%2Fwww.skool.com&source_ve_path=MjM4NTE

**📎 Recursos:**
- Blueprint de Make - Carruseles

---

Automatización de [Marco Sotos Navarro](https://www.skool.com/@marco-sotos-navarro-8790?g=imperio-digital)  
  
Plantilla descargable al final del post.

**Entendamos que hace ***(Resumen generado por GPT 4o1 según la transcripción del video)*  
  
**Objetivo:**  
  
Automatizar la creación y publicación de posts tipo carrusel en Instagram utilizando **Make**, **ChatGPT**, **Canva** y **Dropbox**. La automatización incluye la generación de contenido, diseño de publicaciones, y subida programada de imágenes con descripciones optimizadas.

---

**Flujo de la Automatización:**

1. **Generación del Contenido con ChatGPT:** - Utiliza un prompt para generar ideas de contenido estructuradas en formato CSV.
- La estructura típica incluye: - Imagen 1: Gancho o introducción.
- Imagen 2: Aportar valor (tips o información clave).
- Imagen 3: Llamado a la acción (CTA).
- ChatGPT genera descripciones optimizadas para SEO y añade hashtags sugeridos.
2. **Preparación en Canva:** - Crea una plantilla base para los posts (1080x1080px).
- Conecta los datos del CSV generado en ChatGPT a Canva mediante la función de autodatos.
- Genera múltiples diseños automáticamente y los guarda en una carpeta específica.
3. **Gestión de Archivos en Dropbox:** - Subida de los diseños generados en Canva a Dropbox.
- Se crea un enlace compartido para cada imagen almacenada en Dropbox.
4. **Programación y Publicación en Instagram:** - Utiliza el módulo de publicación de carruseles de Make para subir las imágenes a Instagram.
- Añade las descripciones generadas por ChatGPT como captions.
- El contador garantiza que cada ciclo de la automatización use las imágenes correctas del carrusel.
5. **Gestión del Contador:** - Un contador dinámico en Google Sheets asegura que la automatización continúe con las siguientes imágenes sin repetir las anteriores.
- Cada iteración actualiza el contador para mantener el flujo continuo.

---

**Resultados:**  
  
La automatización permite:

- Crear carruseles personalizados de forma masiva.
- Publicar posts programados con contenido atractivo y estructurado.
- Optimizar el tiempo de gestión en redes sociales.

---

**Requisitos:**

- **Google Sheets:** Para manejar el contador dinámico.
- **Canva:** Creación de los diseños con datos vinculados.
- **Dropbox:** Almacenamiento y gestión de imágenes.
- **ChatGPT:** Generación del contenido textual.
- **Make:** Orquestación del flujo y publicación en Instagram.

---

**Conclusión:**  
Marcos demuestra cómo integrar herramientas de IA y automatización para crear un flujo eficiente que transforma ideas en publicaciones impactantes de manera rápida y organizada. Ideal para quienes buscan profesionalizar su gestión de redes sociales. 🚀
