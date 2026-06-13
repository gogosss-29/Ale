# El error que destruye tu agente de WhatsApp

> Ruta: 🔴 Grabaciones › El error que destruye tu agente de WhatsApp

**🎬 Vídeo (58.2 min):** https://www.youtube.com/watch?v=0CMGKkBmQwE

---

**Problemas que resuelve la sesión 24 de Abril:** Cómo gestionar y medir costos de API con clientes reales, cómo estructurar flujos de datos para evitar errores de consolidación, cómo elegir entre Evolution API y WhatsApp oficial según el riesgo del cliente, y cómo conectar Instagram a herramientas propias de forma escalable.

---

**Intervenciones**

**[****00:00****] Tomás – Modelo de cobro y medición de costos de API** Plantea cómo calcular el costo real de un sistema de atención al cliente (agente de voz, chatbot, WhatsApp) para presupuestarlo correctamente. Franco explica el modelo de retainer mensual como opción más estable, y muestra cómo crear una API key por cliente en el panel de Anthropic para medir el consumo real día a día. Se discute el trade-off entre asumir el costo internamente vs. trasladarlo al cliente.

**[****12:00****] Tomás – Problema al conectar número a WhiteCloud via portfolio de Meta** Al intentar vincular su número de WhatsApp Business a WhiteCloud, Meta rechaza el portfolio de negocio por considerarlo sospechoso o inactivo. Solución: usar un portfolio con historial de actividad, de un amigo o cuenta de agencia. No es necesario verificar el negocio para operar. Se aclara también que desde una sola cuenta de WhiteCloud se pueden gestionar múltiples portfolios de negocio.

**[****18:00****] David Cayuelas – App de conteo de inventario en el Bernabéu** Trabaja en una empresa que gestiona bebidas y snacks en 50 zonas del estadio. El proceso actual es manual: papel, consolidación en Excel, sin sistema centralizado. Quiere reemplazarlo con una app móvil simple que vuelque los datos a Microsoft Fabric. Franco propone una arquitectura de tres capas: carga de datos por operario → base provisional con validación humana → base final en Fabric. La clave es separar la entrada del dato de su visualización, y blindar el formulario de carga para minimizar errores. El desarrollo se puede iniciar con Claude para el front y Claude Code para el back.

**[****35:00****] Agustín Sol – WhiteCloud vs. API oficial de Meta y uso de Evolution API** Pregunta por qué usar WhiteCloud en lugar de conectarse directamente a la API oficial de Meta, y en qué casos es válido usar Evolution API con clientes. Franco explica que WhiteCloud es un intermediario oficial que simplifica la integración y el soporte. La API directa de Meta es técnicamente posible pero genera fricción y falta de soporte. Evolution API solo se recomienda para funciones que la API oficial no soporta (como agregar a grupos), en números aislados y con plena conciencia del riesgo de baneo. Nunca para recepción de clientes.

**[****40:30****] Presentación de Imperio OS** Franco muestra la nueva herramienta de búsqueda interna de la comunidad: un bot que navega más de 4.900 posts y 80.000 comentarios para responder preguntas sobre herramientas como WhiteCloud, N8N, Make y otras.

**[****44:59****] Melina – Herramienta de research de contenido para creadores con scraping de Instagram y TikTok** Desarrolló con Claude Code un dashboard que hace scraping de competidores, analiza hooks y genera guiones usando la API de Gemini. Quiere conectar el Instagram del creador principal de forma oficial para obtener estadísticas propias sin scraping. Franco reconoce la solidez del proyecto y explica que el signup embebido con Instagram requiere un proceso de verificación burocrático con Meta Developers. Como alternativa MVP: usar Make (que ya tiene acuerdo con Meta) para obtener datos vía webhook y conectarlo a la app. A mayor escala, conviene crear un scraper propio con Claude Code para reducir costos de APIFY.

**[****53:57****] Agustín Sol – Requisitos para levantar un número nuevo en WhiteCloud** Pregunta si un número sin actividad previa en WhatsApp puede conectarse a WhiteCloud. Franco aclara las dos modalidades: API oficial pura (solo necesita el número) vs. API oficial con coexistencia (requiere que el número ya exista como WhatsApp Business en un celular). Para agentes de atención al cliente se recomienda coexistencia, ya que permite que el operador también use el número manualmente si hay un problema con el cliente.

**[****57:45****] Cierre** Franco invita a usar Imperio OS para resolver dudas sobre herramientas y anuncia continuidad en la comunidad.
