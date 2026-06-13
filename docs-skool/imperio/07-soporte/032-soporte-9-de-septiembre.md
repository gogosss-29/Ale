# Soporte - 9 de Septiembre

> Ruta: 🛠️ Soporte › Soporte - 9 de Septiembre

**🎬 Vídeo (67.9 min):** https://www.youtube.com/watch?v=LVO-SzYK37M

---

En esta sesión se resolvieron dudas prácticas de la comunidad sobre automatización en Make y N8N. Se abordaron casos como generar imágenes personalizadas, integrar APIs médicas en agentes, hacer seguimientos comerciales con Airtable, gestionar archivos binarios pesados en N8N, estructurar formularios en Airtable, compartir automatizaciones y cobrar servicios, además de optimizar recordatorios contables con relevance y WhatsApp.

---

### **Lista de intervenciones:**

- **[****00:08****] Franco – Bienvenida y dinámica de la sesión**  
Explica que la reunión de martes es un espacio de Q&A abierto y recomienda levantar la mano temprano para organizar mejor las intervenciones.
- **[****02:03****] Víctor – Generador de contenido con imágenes en Make**  
Problema: la IA genera imágenes aleatorias en lugar de basarse en la imagen subida.  
Solución: usar el módulo de *image edits* de OpenAI con prompt + imagen como input, eliminando pasos redundantes.
- **[****07:58****] Pablo – Agente de agendamiento médico en N8N**  
Problema: necesita mapear especialidades e IDs obtenidos por API y pasarlos a la disponibilidad.  
Solución: unificar tools en el agente principal y definir variables de entrada/salida entre workflows para que la IA gestione parámetros dinámicos.
- **[****18:11****] Camilo – Seguimiento comercial automático en Make**  
Problema: quiere que tras cierto tiempo sin respuesta se envíen mensajes de seguimiento por WhatsApp.  
Solución: migrar la lógica a Airtable con campos de última respuesta, horarios y checks lógicos (true/false) para determinar seguimientos y evitar duplicados.
- **[****29:20****] Carlos – Problemas con binarios pesados en N8N**  
Problema: videos de 300 MB–1 GB cargados en Airtable no pueden procesarse en N8N.  
Solución: N8N tiene límites técnicos, no depende del servidor. Recomendación: normalizar proceso de carga (Drive, Loom, Dropbox) o usar Airtable como repositorio intermedio, evitando archivos masivos en N8N.
- **[****37:25****] Cristian – Formularios y exportación de respuestas en Airtable**  
Problema: necesita compartir respuestas de formularios en formato legible (tipo PDF).  
Solución: crear interfaces en Airtable que simulen el formulario con títulos y campos, habilitando la opción de impresión/exportación.
- **[****41:07****] Gabriel – Cómo compartir automatizaciones y cobrar servicios**  
Problema: quiere que otros usen sus escenarios de Make y no sabe cómo cobrar.  
Solución: se recomienda instalar y configurar la automatización directamente para el cliente, no solo entregar el JSON. Para pagos internacionales: Wise, Payoneer o criptomonedas.
- **[****48:45****] Juan Felipe – Facturas en Make + Airtable con IA**  
Problema: al convertir facturas en JSON, algunos campos llegan vacíos en Airtable.  
Solución: la IA cambia nombres de variables (“nombre paciente” vs. “nombre del paciente”). Se recomienda estructurar JSON con nombres estrictos y usar *Transform to Structured Data* para fiabilidad.
- **[****1:00:01****] Juan Javier – Subagentes en Relevance**  
Problema: la interfaz ya no muestra la opción de subagentes como en los videos antiguos.  
Solución: ahora se usan *Workforce* para crear y anidar agentes. Relevance sigue siendo útil para proyectos contables simples (recordatorios de pagos con WhatsApp).
- **[****1:07:26****] Franco – Cierre de la sesión**  
Resumen de aprendizajes, recomendación de revisar la grabación del viernes anterior sobre elección de software, y recordatorio de que las dudas también se pueden discutir en la comunidad.
