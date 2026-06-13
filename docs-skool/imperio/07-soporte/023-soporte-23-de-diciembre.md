# Soporte - 23 de diciembre

> Ruta: 🛠️ Soporte › Soporte - 23 de diciembre

**🎬 Vídeo (57.2 min):** https://www.youtube.com/watch?v=XymJAV4zJvo

---

## Problemas que resuelve

Cómo decidir correctamente entre **lógica tradicional e IA** en automatizaciones reales, cómo **evitar errores comunes al procesar grandes volúmenes de datos** en Make y N8N, y cómo **diseñar soluciones más estables** cuando hay criterios blandos, formatos inconsistentes o múltiples tipos de archivo.

---

## 🧩 Intervenciones

---

### [00:00] Franco – Apertura y dinámica de la sesión

Explica que se trata de una sesión de preguntas y respuestas en vivo (martes), enfocada en **destrabar problemas reales**. Aclara la fecha (23 de diciembre) y pide a los participantes que traigan bloqueos concretos para resolverlos en el momento, priorizando criterio y diseño por sobre teoría.

---

### [01:17] Juan Felipe – Reportes administrativos con IA que alucina datos

Plantea un sistema que consolida múltiples formularios en AirTable para generar informes mensuales de gestión para directores de clínicas. El flujo funciona a nivel datos, pero al pasar el JSON a la IA para generar el reporte, el modelo **alucina**, mezcla fechas y crea información incorrecta.

**Solución:** separar claramente las etapas del proceso:

- Datos → Reporte (con lógica, sin IA)
- Reporte → Análisis (con IA)  
Se recomienda generar reportes estructurados por tabla mediante plantillas simples y luego pedir a la IA que analice cada reporte por separado, evitando pasarle JSON crudo y sobrecargarla.

---

### [08:06] Franco – Diseño correcto del flujo de datos y análisis

Explica con un esquema visual que el error principal es mezclar **reporte y análisis en un solo paso**. La IA no debe generar reportes desde datos crudos cuando hay grandes volúmenes. Primero se ordena la información con lógica, luego se aplica IA para análisis blando y conclusiones.

---

### [13:08] Jorge – Automatización de carga de currículums con IA

Describe una plataforma de reclutamiento donde los usuarios suben CVs (PDF, Word o imágenes) y luego deben completar manualmente sus datos. Quiere automatizar la lectura del archivo, generar un JSON estructurado y devolverlo al servidor usando N8N.

**Solución:** dividir el problema en dos partes:

- Recepción y respuesta correcta del webhook (POST + Respond to Webhook).
- Procesamiento del archivo según su tipo.  
Se recomienda empezar con imágenes para lograr un *quick win*, luego escalar a PDFs y otros formatos, y no usar OpenAI directamente para PDFs, sino herramientas intermedias (ej. OCR o PDF processors).

---

### [18:25] Franco – Configuración correcta de webhooks en N8N

Aclara la importancia de usar `Respond immediately` y un nodo `Respond to Webhook` para evitar procesos asincrónicos que dejan colgada la respuesta. Explica que el JSON final puede devolverse completo en la respuesta del webhook sin problemas de tamaño.

---

### [24:01] John – Error al enviar imágenes por WhatsApp usando URLs

Explica que intenta enviar imágenes almacenadas como URLs desde una base de datos, pero el envío falla constantemente.

**Solución:** WhatsApp no acepta URLs, necesita el archivo como media.  
Se muestra el flujo correcto:

1. Descargar la imagen con HTTP.
2. Convertirla a binario/Base64.
3. Enviar el archivo como media.  
Se recomienda encapsular este proceso en un **sub-workflow reutilizable** para mantener el flujo principal limpio.

---

### [36:59] Sofía – Envío mensual de prefacturas agrupadas por proveedor

Tiene múltiples archivos Excel con nombres variables que contienen el nombre del proveedor. Necesita enviar **un solo mail por proveedor**, incluso si hay varias prefacturas.

**Solución:** el flujo debe nacer desde un **listado de proveedores**, no desde los archivos.  
Por cada proveedor:

- Buscar archivos cuyo nombre contenga el proveedor.
- Agruparlos.
- Enviar un único correo con todos los adjuntos.  
Se aclara que puede resolverse con agregators o routers según el caso.

---

### [47:19] Sofía – Lectura de archivos desordenados y PDFs con imágenes

Plantea el problema de archivos en múltiples formatos (PDF, imágenes, PDFs con imágenes incrustadas) y sin estructura consistente.

**Solución:** unificar el formato antes de analizar:

- Detectar la extensión.
- Convertir todo a imagen (PNG).
- Procesar siempre imágenes con IA.  
Esto simplifica el sistema y evita manejar múltiples lógicas de lectura.

---

### [51:25] Juana – Confusión con webhooks y flujos copiados de la comunidad

Consulta sobre un flujo descargado de la comunidad que no entiende completamente, especialmente el origen de los datos y el uso de JSON.

**Respuesta:** se recomienda seguir el tutorial original paso a paso y evitar copiar flujos sin entender el sistema completo, ya que suelen faltar conexiones clave como el origen del webhook.

---

### [56:50] Cierre

Franco cierra la sesión destacando la importancia de **entender procesos antes que herramientas**, evitar copiar soluciones sin criterio y diseñar sistemas simples y robustos. Invita a continuar el trabajo en la próxima sesión.
