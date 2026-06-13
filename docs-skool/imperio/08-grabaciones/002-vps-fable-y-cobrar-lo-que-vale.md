# VPS, Fable y cobrar lo que vale

> Ruta: 🔴 Grabaciones › VPS, Fable y cobrar lo que vale

**🎬 Vídeo (100.5 min):** https://www.youtube.com/watch?v=U7g-0hNcHWo

---

**Problemas que resuelve la sesión 12 de junio:**  
Cómo elegir la infraestructura correcta para escalar un producto (VPS vs. Versel), cómo monetizar herramientas digitales que ya tienen usuarios, cómo gestionar el consumo de tokens en Claude Code sin agotar el plan, y cómo diseñar agentes personales tipo Hermes para casos de uso con múltiples frentes laborales.

---

**Intervenciones**

**[00:00] Alan – Extensión de Chrome para equipos de Salesforce**  
Desarrolló localmente un complemento que analiza historias de usuario en Jira, detecta ambigüedades y genera subtareas automáticas con estándares de Salesforce. Quiere escalarlo como SaaS con suscripción mensual. Consulta sobre infraestructura (VPS vs. servicios como Vercel) y pasarelas de pago en Chile.

Solución: Franco recomienda priorizar product-market fit antes de invertir tiempo en decisiones de infraestructura. Las diferencias entre opciones en etapa temprana son mínimas; lo urgente es conseguir feedback real del mercado.

**[06:53] Hernán – Recursos humanos en minería, nuevo en la comunidad**  
Trabaja en desarrollo organizacional y clima laboral. Busca orientación sobre cómo integrar IA en su área y por dónde empezar.

Solución: Franco le recomienda el Agéntico OS para generar un roadmap personalizado. Juaco complementa invitando a las sesiones de bienvenida los lunes y jueves.

**[12:27] Camilo – Scraper de eventos culturales con canal de WhatsApp**  
Tiene una herramienta de difusión de eventos para pequeños productores artísticos (teatro, restaurantes, experiencias), con ~120 usuarios activos en WhatsApp y corriendo en local. Quiere escalar y monetizar.

Solución: Franco recomienda subir a VPS como primer paso usando Claude Code para guiar el deploy. Para monetizar: modelo freemium con visibilidad pagada (promociones más frecuentes o destacadas para quienes paguen), con niveles de suscripción proporcionales a la exposición obtenida.

**[22:38] Eduardo – Agente de WhatsApp con visión para taller de chapa y pintura**  
Quiere un agente que reciba fotos o videos de autos dañados y genere cotizaciones automáticas para traer clientes al taller. Ya cerró el cliente.

Solución: Pasar de video a fotos reduce la complejidad en un 70%. El objetivo real no es la precisión sino el enganche: dar rangos estimativos que inviten a ir al taller. Franco recomienda no usar video, diseñar patrones de fotos claros y testear mucho para evitar expectativas incorrectas en clientes premium. Carlos anuncia nuevo curso de agentes de WhatsApp próximo a publicarse.

**[32:37] Mauricio – Consumo excesivo de tokens en Claude Code con Fable**  
Usó Claude Fable en Ultra Code con dos proyectos en paralelo y llegó al 90% del uso semanal en menos de 24 horas. Consulta sobre crear segunda cuenta para continuar.

Solución: Las sesiones se guardan en un archivo `.json` local, por lo que técnicamente una segunda cuenta leería el mismo contexto. Pero Franco enfatiza que el problema de fondo es el modelo de uso: Opus para planificar, Sonnet para ejecutar. Fable solo en planificaciones críticas o revisiones adversariales. Se menciona la "paradoja de Jevons": cuando hay tecnología más potente disponible, el consumo sube aunque no sea necesario.

Además, consulta sobre cómo conectar un agente de WhatsApp cuando Meta rechaza la verificación. Solución: usar Wcloud (Y Cloud), plataforma oficial recomendada con más de 40 números conectados en la agencia de Franco.

**[47:20] Lore – MVP de asistente contable para preliquidación**  
Tenía un prototipo en Gemini que organiza información desordenada de clientes para contadores. Quiere migrarlo a Claude Code y deployarlo en Vercel para tener una URL compartible y conseguir feedback real.

Solución: Franco confirma que es el camino correcto. El MVP en local o con link de Gemini genera demasiada fricción para testear. Buildear en Claude Code y deployar en Vercel es simple y da acceso directo a usuarios.

**[52:21] Tomás – Manager de músicos que quiere asistente personal total**  
Cliente con todo en Excel, múltiples negocios y frentes laborales. Quiere un agente que reciba audios por WhatsApp, lea facturas, cualifique proyectos entrantes, haga seguimientos y gestione pagos.

Solución: Franco y Carlos coinciden en Hermes. Carlos aclara que Hermes ya tiene integración oficial con la API de WhatsApp. Recomienda usar un Hermes propio primero para armar y testear el del cliente. Sobre pricing: Franco vendió un sistema similar en $3,000 + mantenimiento mensual de $500, con el cliente absorbiendo todos los costos de tokens para evitar consumos imprevisibles.

**[1:03:18] Iván – App de CRM gastronómico en producción con consumo excesivo en Vercel**  
La app está funcionando con clientes reales desde el martes. Vercel le consumió las 4 horas de CPU gratuitas por refrescos de pantallas y una importación masiva. Consulta sobre VPS vs. Vercel y buenas prácticas de monitoreo.

Solución: Franco advierte que el riesgo de VPS es quedarse sin recursos en horario pico sin aviso. Vercel lo avisa por mail y escala con costo. Para optimización: nueva sesión en Claude revisando toda la app, implementar caché con Redis, usar Sentry para errores y Uptime Robot para monitoreo externo. Carlos sugiere también Opstash para análisis de consumo.

**[1:22:26] Gonzalo – CRM simple para cliente sin conocimientos de marketing**  
Necesita recomendar plataforma para automatizar CRM, emails y base de datos para alguien que recién empieza.

Solución: GoHighLevel, sin dudarlo.

**[1:23:38] Marcos – Empresa de informática con datos sensibles, seguridad como prioridad**  
Su padre maneja RPS y datos de nóminas de empresas. Quiere implementar IA de forma segura, sin riesgo de fuga.

Solución: Evitar Open Claw y Hermes en contextos sensibles. Quedarse con Claude Code como arnés cerrado. Buena práctica: usar Opus para intentar hackear la propia app y arreglar las vulnerabilidades encontradas iterativamente.

**[1:28:25] Diego – Sistema de visitas agendadas para energía solar, quiere expansión a LATAM**  
Tiene 5 clientes activos y quiere sumar Hermes para hacer seguimiento proactivo de prospectos y clientes en distintos canales (WhatsApp, email, llamada).

Solución: Franco valida la idea y recomienda configurar Hermes con el propio miedo de seguridad como input ("mi miedo es que alguien extraiga el código, fortalezcámoslo"). Hermes no está diseñado para atención a clientes masiva pero en grupos de WhatsApp con supervisión es viable para testear.

**[1:32:04] Ricardo – Sistema de recordatorios para clínica odontológica**  
Detectó que su dentista no hizo seguimiento en 2 años y quiere venderle un sistema automatizado de recordatorios por WhatsApp.

Solución: N8N + Wcloud + Claude Code. Lo más importante es que el cliente tenga la base de datos ordenada antes de automatizar. GHL no es necesario para este caso.

**[1:35:17] Shen – Agente de atención en N8N con filtro de precio, no sabe cómo cobrarlo**  
Tiene un agente que detecta si el usuario solo pregunta precio o si tiene intención real, conectado con ManyChat y con funciones de agendar/cancelar/reagendar. No lo está presentando porque no sabe cuánto vale.

Solución: Franco recomienda buscar la primera venta por experiencia, no por ganancia. En esta etapa, $300–$500 es razonable para cerrar, implementar en producción y mejorar el sistema con feedback real. Después ese mismo sistema se puede vender mucho más caro.
