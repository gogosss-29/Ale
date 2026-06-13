# Soporte - 6 de Enero

> Ruta: 🛠️ Soporte › Soporte - 6 de Enero

**🎬 Vídeo (58.8 min):** https://www.youtube.com/watch?v=AxmfpW1Nruw

---

## Problemas que resuelve

Cómo procesar currículums en múltiples formatos (PDF, Word e imágenes) usando N8N, cómo decidir **cuándo usar lógica y cuándo IA** para evitar alucinaciones, y cómo diseñar flujos estables para normalizar datos inconsistentes sin romper la arquitectura ni agregar complejidad innecesaria.

---

## 🧩 Intervenciones

---

### [00:22] Jorge – Automatización de currículums en múltiples formatos

Explica un sistema donde los usuarios suben currículums (Word, PDF o imagen) que deben ser leídos, procesados y convertidos en JSON para guardarlos en una base de datos. El problema principal aparece al intentar procesar documentos Word, ya que N8N no logra extraer correctamente el contenido ni convertirlo a un formato usable.

---

### [02:40] Daniel – Problemas reales al leer PDFs y documentos mal estructurados

Comparte su experiencia procesando PDFs con estructuras internas inconsistentes. Explica por qué muchos PDFs “se ven bien” pero internamente están mal formateados, lo que genera errores al usar IA. Recomienda herramientas específicas (PDF to Text / contenedores propios) y advierte sobre el alto costo oculto de soluciones pagas que no resuelven el problema real.

---

### [04:47] Jorge – Bloqueo técnico: conversión de Word a PDF o texto

Aclara que el problema no es el PDF (ya resuelto), sino el documento Word. Muestra intentos fallidos usando nodos de conversión y servicios pagos, y plantea la dificultad de integrar APIs externas sin complejizar demasiado el flujo.

---

### [07:14] Daniel – Solución práctica: usar Google Drive como normalizador

Propone una alternativa más simple y estable:  
Subir el archivo Word a Google Drive, convertirlo a Google Doc y luego descargarlo como PDF o texto. Esto permite reutilizar la misma lógica de procesamiento ya existente para PDFs, evitando servicios externos y errores de parsing.

---

### [10:02] Carlos – Estrategia de normalización por tipo de archivo

Explica un enfoque práctico:

- Si el documento es texto plano → extract to text
- Si tiene imágenes o estructura compleja → OCR  
Comparte cómo en sus flujos convierte todo a un formato uniforme antes de analizar, reduciendo errores y variabilidad.

---

### [11:40] Jorge – Duda clave: cuándo usar IA y cuándo no

Pregunta qué módulo de OpenAI usar para validar que el texto extraído sea correcto y generar el JSON final. Plantea el riesgo de alucinaciones y errores al estructurar datos sensibles como currículums.

---

### [12:50] Franco – Regla crítica: no usar IA para estructurar texto consistente

Aclara que **no se debe usar IA para convertir texto a JSON** cuando el texto ya es consistente. Recomienda usar lógica o código para estructurar datos y reservar la IA solo para casos donde el input sea impredecible (formatos variables, distintos layouts de CV).

---

### [15:35] Franco – Cuándo sí usar IA en currículums

Explica que, dado que los currículums llegan en formatos muy distintos, la IA **sí es útil** para normalizar cuando el output del nodo no es consistente. Recomienda:

- Normalizar primero (convertir todo a PDF)
- Luego usar un agente con prompt estricto y output en JSON definido

---

### [16:20] Daniel – Uso de agentes con Gemini para análisis de archivos

Comparte su implementación usando un agente con Gemini, ya que permite pasar archivos directamente al modelo. Explica cómo define el schema del JSON en el system prompt y luego mapea el resultado a AirTable sin problemas.

---

### [18:08] Debug en vivo – Error al procesar documentos Word en N8N

Se analiza un error específico del nodo `Convert File`, donde el campo `data` no se recibe correctamente. Se muestra cómo inspeccionar el error, copiar el log y usar IA para interpretar el mensaje técnico antes de ajustar el flujo.

---

### [21:30] Franco – Diagnóstico final del problema

Aclara que el bloqueo no está en la IA sino en el paso previo: la conversión del documento. Una vez convertido a PDF o texto, el resto del flujo funciona correctamente. Recomienda no seguir avanzando hasta resolver esa etapa base.

---

### [23:05] Franco – Enfoque correcto de diseño

Refuerza el criterio general:

- Primero resolver el formato de entrada
- Luego normalizar
- Después decidir si hace falta IA  
Usar IA antes de tiempo solo agrega ruido y errores difíciles de debuggear.

---

### [24:09] Nicolás – Adaptar un flujo de WhatsApp sin formulario

Consulta cómo reutilizar un flujo de WhatsApp que originalmente funcionaba solo con formularios para que responda a cualquier mensaje entrante, sin perder control ni romper el sistema.

---

### [26:00] Franco – Debug de flujo copiado y restauración correcta

Se detecta que al borrar nodos clave (filtros y búsquedas en tablas) el flujo deja de funcionar. Se muestra cómo restaurar versiones anteriores, eliminar solo el filtro incorrecto y mantener la estructura mínima necesaria para que el sistema siga operativo.

---

### [29:36] Franco – Diseño correcto de agentes con WhatsApp

Explica que no es recomendable usar un agente simple si también va a intervenir un humano. Advierte sobre los errores comunes cuando no se gestiona correctamente el “handoff” entre IA y humano.

---

### [36:04] Carlos – Arquitectura completa de agente WhatsApp en producción

Muestra un flujo completo con:

- Buffer de mensajes (Redis)
- Control de latencia y escritura
- Guardrails de seguridad
- Sanitización de outputs
- Integración con [Cal.com](http://Cal.com)  
Explica cómo simular comportamiento humano y reducir bloqueos de WhatsApp.

---

### [46:14] Franco – Control humano vs IA usando `fromMe`

Explica una estrategia clara para detectar cuándo un humano interviene en una conversación usando el flag `fromMe`. Muestra cómo pausar la IA automáticamente y evitar respuestas cruzadas o inconsistentes.

---

### [50:10] Franco – Seguimientos automáticos por tiempo

Muestra un sistema de follow-ups basado en reglas lógicas y tiempo (polling), sin depender de IA. Explica cómo escalar seguimientos a cientos o miles de conversaciones usando lógica y bases de datos.

---

### [58:30] Cierre

Franco cierra la sesión reforzando los aprendizajes clave:

- Normalizar antes de automatizar
- Lógica primero, IA después
- Diseñar sistemas antes de copiar flujos  
Invita a continuar el trabajo en las próximas sesiones de martes y viernes.

---
