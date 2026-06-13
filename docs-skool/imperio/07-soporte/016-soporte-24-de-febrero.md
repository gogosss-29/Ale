# Soporte - 24 de Febrero

> Ruta: 🛠️ Soporte › Soporte - 24 de Febrero

**🎬 Vídeo (60.6 min):** https://www.youtube.com/watch?v=fDbtO1Cj94E

---

---

**Problemas que resuelve:** Cómo generar landing pages personalizadas a escala usando IA y N8N, cómo elegir entre WhatsApp personal, Business o API para campañas de prospección, y cómo construir un flujo de scraping de noticias para generar contenido en LinkedIn sin morir en el intento.

---

**Intervenciones**

**[00:00] Franco – Apertura y contexto de la sesión** Retoma las sesiones tras 15 días de descanso. Recuerda el formato: espacio abierto de preguntas y casos reales de automatización e IA. Menciona sesión de vibe coding con Carlos al día siguiente.

**[03:16] Tomás – Landing pages masivas para prospección dental** Comparte su flujo: scraping de Google Maps con Apify, filtrado de leads sin página web, generación de HTML con Claude y deploy en GitHub + Vercel. El problema: las ediciones que le pide a la IA no se aplican correctamente y perdió el template que le gustaba.

Solución: hacer ediciones simples de color y fuente directamente en el HTML con buscar y reemplazar, en vez de pedírselas a la IA. Para variar títulos y textos entre páginas, agregar un nodo de GPT en N8N que genere el contenido variable antes del deploy.

**[23:01] Sofi – Agente de IA con imágenes en Make que supera el límite de tokens** Su flujo de probador virtual con el modelo Gemini arroja error de input tokens excedidos. Incluso al simplificar el prompt, aparecen nuevos errores de argumentos inválidos.

Solución: las imágenes también consumen tokens de contexto. Se recomienda revisar los parámetros avanzados del nodo y, como paso clave, migrar el flujo a N8N, que es más expresivo con los errores y facilita el diagnóstico.

**[33:33] Vilma – Automatización de comentarios en LinkedIn y alternativas a plugin de WhatsApp en Go High Level** Consulta si es posible enviar un DM automático a quien comenta un post en LinkedIn, y si existe una alternativa más económica al plugin de WhatsApp de GHL ($29/mes).

Solución: para LinkedIn, usar Phantombuster que ya tiene phantoms armados para ese flujo. Para WhatsApp en GHL, el plugin es prácticamente inevitable si se quiere verlo ahí dentro; la alternativa es externalizar el chat a plataformas como Chatwoot, que no tiene costo.

**[41:01] Tomás + Juaco – Estrategia de envío y WhatsApp para prospección** Juaco pregunta por el proceso de envío de las landing pages. Tomás explica que por ahora el envío será manual hasta validar que las páginas funcionen, y que aún no tiene WhatsApp Business configurado.

Solución: investigar las diferencias entre WhatsApp personal, Business y API antes de escalar. Se recomienda iCloud (recomendado por Carlos) como solución intermedia que combina lo mejor de ambos mundos. Advertencia clara: nunca usar el número personal para envíos masivos por riesgo de bloqueo.

**[48:34] Jaime – Flujo de scraping de noticias para generar posts en LinkedIn** Está construyendo en N8N un sistema que lee noticias de distintos medios y con IA genera borradores de posts para LinkedIn. El problema: cada portal tiene estructura distinta y algunos bloquean el scraping.

Solución: usar RSS en vez de scraping directo, que es más estable y ya funciona en N8N. Para medios que no lo soporten, complementar con Twitter/X siguiendo cuentas clave. Carlos propone una solución más directa: usar OpenClow con el skill "Last Days" para que el agente haga toda la investigación, el reporte y la redacción sin necesidad de N8N. También se recomienda actualizar el modelo configurado a GPT con suscripción Plus para evitar quedarse sin tokens de API.

**[1:00:08] Cierre** Franco resume la sesión y se despide. Próximas sesiones: miércoles con Carlos (vibe coding) y viernes sesión regular.
