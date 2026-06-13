# Soporte - 29 de Julio

> Ruta: 🛠️ Soporte › Soporte - 29 de Julio

**🎬 Vídeo (58.1 min):** https://www.youtube.com/watch?v=e49Rzpqv7m0

---

**Problemas que resuelve:** Automatización de contenido mensual con AirTable, solución de errores al etiquetar en WhatsApp con Wapi, alternativas económicas para generar videos IA, y trabajo eficiente entre Google Sheets y N8N para mantener estructura de datos.

📌 **Lista de preguntas con Timestamps:**

- **[****01:31****] Mailin** – Problemas con el etiquetado de chats en WhatsApp usando Wapi. El flujo deja de funcionar al migrar a una nueva cuenta gratuita. Se sospecha que el error proviene del canal Wapi o del token. Recomendaciones: contactar soporte para reiniciar canal o probar **Evolution API** como alternativa más estable.
- **[****12:58****] Andrés** – Usa **Veo 3** de Gemini para generar videos cortos desde prompts. Problema: cada video cuesta ~6 USD usando la API directamente. Se sugiere usar **Gemini Flow Pro** (20 USD/mes), que ofrece 1,000 créditos mensuales y permite generar ~50 videos. También se menciona **Sora (OpenAI)** y **Pika** como opciones más económicas.
- **[****22:01****] Jonathan** – Quiere automatizar la generación mensual de contenido para múltiples clientes en AirTable. Consulta si necesita un escenario por cliente. Solución: usar un solo escenario con **Webhook por botón en AirTable** usando el `recordID` para obtener datos específicos de cada fila. Ideal para escalar producción sin duplicar escenarios.
- **[****33:35****] Carlos** – Problemas con AirTable versión gratuita al intentar disparar Webhooks. Además, plantea limitaciones de **Google Sheets en N8N**: no retorna el `row number` tras `Append Row`. Solución: usar columna ID personalizada o migrar a **AirTable**, mucho más amigable y robusto en automatizaciones.
- **[****41:12****] Antonio** – Recibe archivos `.zip` desde Bolt con un video y PDF que necesita procesar en Gemini. Problema: Make no permite enviar ambos archivos simultáneamente. Solución: usar **Array Aggregator** y acceder a elementos por índice (`[0]`, `[1]`) para enviarlos juntos al módulo Gemini. Se discute alternativa más compleja si el número de archivos varía.
