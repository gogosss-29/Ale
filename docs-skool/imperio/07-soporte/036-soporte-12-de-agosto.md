# Soporte - 12 de Agosto

> Ruta: 🛠️ Soporte › Soporte - 12 de Agosto

**🎬 Vídeo (64.4 min):** https://www.youtube.com/watch?v=IQAZ1JdSS2Y

---

**Problemas que resuelve:**  
Sesión práctica resolviendo casos reales sobre integración y automatización de procesos con Airtable, LinkedIn y Make. Se abordaron estrategias para optimizar reportes mensuales para clientes, configurar menciones dinámicas en publicaciones, y reducir errores y consumo de operaciones en campañas automatizadas.

**Cronología de intervenciones:**

[00:09] **Franco – Introducción**  
Explica la dinámica de la sesión de preguntas y respuestas, invitando a los participantes a levantar la mano para resolver problemas de automatización y desarrollo.

[01:20] **Juampi – Reportes mensuales con Airtable y Make**  
Quiere generar reportes de clientes comparando métricas mes a mes y enviarlos con análisis de IA. Problema: dificultad para capturar interfaces y actualizarlas automáticamente. Solución: usar OVNI de Airtable para consultas nativas, mantener datos bien estructurados con campos de fecha y fórmulas, y evitar complejidades innecesarias en Make.

[16:42] **Miriam – Envío de correos con datos de Google Maps Scraper**  
Tiene datos en Google Sheets y quiere hacer envíos automatizados sin caer en spam. Problema: envío repetido y estructura de datos incompleta. Solución: filtrar por correos existentes, limitar contactos diarios, agregar columna “Contactado” en Sheets y actualizarla automáticamente en Make para evitar duplicados.

[37:02] **Florencia – Publicaciones con menciones en LinkedIn**  
Necesita automatizar publicaciones con menciones dinámicas a empresas. Problema: parámetro “start index” en LinkedIn API varía según posición de la mención. Solución: probar enviando texto ya formateado con la sintaxis de mención directamente en el campo `content`, o calcular posición con fórmulas `indexOf`.

[50:54] **Jorge – Optimización de campaña de noticias**  
Automatiza publicaciones en redes desde un portal de noticias. Problema: errores en JSON generado por GPT y alto consumo de operaciones. Solución: usar configuración “response format = JSON object” en el módulo de OpenAI para respuestas limpias y aplicar filtros al inicio del flujo para reducir operaciones innecesarias.

[1:03:20] **Franco – Cierre**  
Recuerda la importancia de optimizar flujos desde el primer módulo para ahorrar operaciones y mantener datos ordenados. Invita a los ausentes a continuar la próxima semana o publicar en la comunidad.
