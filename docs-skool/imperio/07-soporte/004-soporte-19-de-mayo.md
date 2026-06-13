# Soporte - 19 de Mayo

> Ruta: 🛠️ Soporte › Soporte - 19 de Mayo

**🎬 Vídeo (80.7 min):** https://www.youtube.com/watch?v=cA6VZfkRJ14

---

**Problemas que resuelve:** Cómo gestionar el contexto en Claude Code para no perder información entre sesiones, cómo conectar WhatsApp de forma segura sin riesgo de baneo, cómo pasar credenciales a agentes de IA sin exponerlas en el chat, y cómo integrar webhooks de Mercado Pago en N8N.

**Intervenciones**

**[01:10] Iván – Cuándo cambiar de sesión en Claude Code** Consulta sobre la práctica de cerrar pestañas o limpiar contexto mientras desarrolla una app de finanzas. Franco explica que el criterio no es tiempo sino uso de contexto: al llegar al 20-30% conviene cambiar de sesión. Solución: pedirle a Claude que cierre la tarea y deje un handoff con contexto en un archivo (Memory MD, Obsidian, o carpeta del proyecto). La diferencia entre [CLAUDE.md](http://CLAUDE.md) y Memory MD: el primero define personalidad y rol, el segundo registra lo que fue pasando.

**[13:35] Glenda y José – Chatbot de WhatsApp para agencia de motos sin riesgo de baneo** Quieren automatizar el primer contacto con leads en los dos números de los vendedores. Franco recomienda levantar un número nuevo centralizado con Wati, donde el agente califica al lead y le avisa al vendedor con toda la info lista. Se explica la diferencia entre coexistencia (el vendedor puede intervenir desde el celular) y número en la nube (solo el bot tiene acceso).

**[23:36] Glenda – Cerradura electrónica Nuki que no genera el código de acceso** El webhook de creación de invitación falla con error code 20 y el huésped nunca recibe el link. No hay resolución técnica en sesión por falta de documentación. Recomendación: insistir con soporte de Nuki por todos los canales. Pregunta adicional sobre cómo guardar contexto al cerrar sesión, respondida de forma similar al caso de Iván.

**[37:01] Roberto – Elección de VPS recomendado por Claude** Claude le recomendó Netcup (8 GB RAM, 4 CPU, 250 GB disco) a $100/año. Franco confirma que cualquier proveedor conocido es estable y que lo relevante es la capacidad. Hostinger también es opción válida en Argentina.

**[41:37] Max – Seguridad al conectar credenciales de Outlook a Claude Code** Tenía miedo de pasar su contraseña por el chat para automatizar modificación de PDFs y envío por mail. Franco aclara que Claude Code es uno de los arneses más seguros y guía hacia OAuth (Microsoft 365 en el panel de Claude) para conectar sin exponer contraseñas. Se refuerza la regla: nunca pasar credenciales por el chat, siempre usar variables de entorno.

**[53:23] Ignacia – Automatizar extracción de Ads Library y generación de creativos en masa** Problema 1: Apify con Facebook Ads Scrapper no devuelve resultados desde Claude Code. Solución: testear primero manualmente vs. con Claude para verificar si el actor de Apify funciona antes de pagar. Problema 2: los creativos generados con Higgsfield pierden consistencia (cambia el diseño de los productos). Solución: separar el proceso en dos partes — primero fijar el design system en un MD de marca, luego pedir iteraciones. Abrir sesiones nuevas por imagen porque el contexto se llena rápido con archivos visuales.

**[1:02:06] Pat – N8N muestra sitio no seguro en Hostinger** Solución: es un certificado SSL que Hostinger entrega automáticamente. Solo hay que esperar unos días desde el deploy. Pregunta adicional sobre tokens de conexión con vencimiento: es opcional y configurable según preferencia.

**[1:04:54] Cristian – Hermes para organizar flujo de trabajo con múltiples agentes** Recomienda Franco arrancar con un solo agente, dominarlo bien y luego escalar. Separar sesiones por proyecto y por tarea. Nunca pedir en la misma conversación cosas de distinto contexto. Referencia a sesión de Carlos sobre configuración de Hermes.

**[1:08:45] Gonzalo – Webhook de Mercado Pago no se dispara en N8N** El pago entra pero N8N nunca se entera. Posibles causas: app de Mercado Libre no configurada en producción, webhooks solo activos para productos nuevos (no retroactivos). Solución: leer la documentación completa o dársela a Claude, crear un producto nuevo y testearlo. Confirmar que el workflow está publicado y no en modo "listen for test event".

**[1:13:49] Agustín – Wati API vs. coexistencia, y número para agente de voz con Retell** Diferencia entre API (más estable, sin acceso del cliente al número) y coexistencia (el vendedor puede tomar el mando). Para el caso de un abogado con agente de voz: Retell ya ofrece números nativos. Si igual quiere usar Twilio, pasarle el error a Claude Code paso a paso para resolver la verificación.
