# Soporte - 25 de Mar

> Ruta: 🛠️ Soporte › Soporte - 25 de Mar

**🎬 Vídeo (56.4 min):** https://www.youtube.com/watch?v=Fv6Axormjh4

**📎 Recursos:**
- Derivar a Humano
- Descartar
- AsignarIAIN

---

### 🧠 **Resumen de la Sesión**

- **Optimización de operaciones en Make**: - Se abordó cómo **evitar el exceso de operaciones al cargar datos masivos a Airtable**, usando el módulo de `Bulk Create Records`.
- Se explicó el uso de `Array Aggregator` para agrupar registros y enviar lotes de hasta 10, y cómo gestionar esa agrupación para no saturar el sistema.
- Se propuso una solución intermedia: **guardar los datos primero en Google Sheets** usando `Bulk Add Rows`, y luego crear un segundo escenario que extraiga 10 registros con `Search Rows` para cargarlos en Airtable en pequeños lotes.
- **Automatización de comentarios en Google My Business**: - Se explicó que la API oficial de Google tiene restricciones fuertes, pero que existen alternativas como **Apify** para intentar acceder de forma no oficial (con precaución).
- **Base de datos para contenido educativo**: - Se recomendó usar **Airtable en lugar de Notion** por su flexibilidad en automatización y manejo de registros.
- Se explicó que se puede usar LaTeX para escribir fórmulas matemáticas, y luego convertirlas a HTML o PDF para presentaciones o guías educativas automatizadas.
- **Procesamiento de múltiples URLs en Make (caso Vilma)**: - Se revisó por qué un iterador no procesaba todas las URLs correctamente.
- Se detectó que las URLs venían en un solo string, y se ajustó la configuración para que el `Iterator` leyera cada URL individualmente desde un arreglo real.
