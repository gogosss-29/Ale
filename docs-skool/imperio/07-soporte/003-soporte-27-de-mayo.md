# Soporte - 27 de Mayo

> Ruta: 🛠️ Soporte › Soporte - 27 de Mayo

**🎬 Vídeo (65.0 min):** https://www.youtube.com/watch?v=45vv3jHgmj4

---

**Problemas que resuelve:** Cómo decidir el flujo correcto cuando construyes un agente de IA con WhatsApp/Telegram, cómo evitar errores de memoria y session ID que rompen la persistencia de datos, cómo diagnosticar fallos comunes en N8N copiando código de Claude sin entenderlo, y cómo dimensionar costos reales de WhatsApp Business API antes de cerrar un cliente.

**Intervenciones**

[00:00] **Apertura y mecánica de la sesión** Franco abre la sesión de soporte de martes con 55 personas conectadas. Explica la dinámica de levantar la mano y mantener orden para aprovechar la hora.

[01:50] **Iván – App de finanzas personales en pareja con chatbot Telegram** Comparte que está construyendo una app de finanzas en pareja como diferenciador frente a apps genéricas. Su flujo actual: el usuario manda audio o texto por Telegram, se transcribe con Whisper, se procesa con Haiku y se guarda en Supabase. Quiere validar si está bien la decisión de usar chatbot en lugar de cargar gastos dentro de la app.

Solución: el chatbot reduce fricción real, los formularios tienen alta tasa de abandono. Whisper es la mejor opción para audio. Haiku puede quedar corto, conviene mover a Sonnet o probar DeepSeek. Lo más importante es normalizar el input (audio/imagen/texto) a texto ANTES de que llegue al agente, no dentro del agente. Para integración con Apple Pay sugiere investigar la app Oneec como referencia de cómo se configuran automations en iOS.

[17:00] **Tere – Automatización de contenido para agencia inmobiliaria** Es contadora, nueva en la comunidad. Una clienta le pidió automatizar el proceso de redes sociales desde ideación hasta publicación. Tiene Google Drive, Slack, Go High Level y CapCut. No sabe por dónde aterrizar la propuesta.

Solución: hablar primero con la clienta y pedir que explique paso por paso cómo lo hace hoy (de dónde saca ideas, qué hace que un guion sea bueno, qué descarta). Replicar el proceso actual, no inventar uno nuevo. Dejar la publicación manual en primera instancia y automatizar solo ideación y guiones. Para entrega usar Claude Code para desarrollar una web app y deployarla en su propio VPS, cobrándole mensual. Go High Level no brilla para gestión de contenido; Notion o desarrollo propio funcionan mejor.

[26:30] **Andrés – Agente de ventas en WhatsApp que se queda en bucle de bienvenida** Construyó un agente para productos homeopáticos basado en el workflow del curso, conectado con Evolution API 2.3.7 y N8N. El agente recibe mensajes pero se queda repitiendo el mensaje de bienvenida sin avanzar a buscar productos en Google Sheets. Su método de debug: copiar errores a Claude, borrar el workflow completo y volver a pegar la versión nueva.

Solución: diagnóstico en vivo paso a paso. Tres errores encontrados:

1. **Memoria mal configurada**: el `session ID` apuntaba a un campo computado de Airtable (`first JSON ID`) que cambiaba en cada ejecución, así que el agente nunca recuperaba contexto previo. Se reemplazó por el número de teléfono.
2. **Condicional vacío**: el nodo "cliente registrado" tenía un IF sin condición, así que siempre devolvía false. Se agregó un check `exists` sobre el campo ID.
3. **Búsqueda en Airtable rota**: buscaba por `user_ID` (campo autocomputado) en lugar de `phone`. Se corrigió la query.

Recomendación de proceso: nunca borrar el workflow para pegar la versión que da Claude. Trabajar siempre sobre el mismo canvas para mantener historial de ejecuciones y poder rastrear errores. Revisar nodo por nodo entendiendo qué hace cada uno antes de seguir.

[53:00] **Cris – Desarrollo de SaaS para corredores inmobiliarios** Trabaja en el mundo inmobiliario, lleva una semana en la comunidad y quiere construir un SaaS para asesores con upgrades modulares (agente de WhatsApp, calificador de leads, transcripción de llamadas, CRM básico). Su duda principal: cómo implementarlo en la cuenta del cliente.

Solución: no preocuparse por el deploy en esta fase. Dos caminos válidos: desplegarlo todo en tu propio servidor y dar acceso al cliente, o pedirle al cliente que levante un VPS y darle credenciales. La mayoría de clientes no se preocupan por dónde está alojado. Lo crítico ahora es validar mercado con algo funcional, no perfeccionar infraestructura.

[58:30] **Cris – Cálculo de costos de WhatsApp Business API** Pregunta cuánto gasta un cliente con ~200 conversaciones al mes en Chile.

Solución: Franco muestra la calculadora oficial de Meta. Diferencia clave entre conversaciones entrantes (gratis dentro de la ventana de 24h desde el último mensaje del cliente) y salientes (cobran por plantilla de marketing). Para inmobiliarias inbound que vienen de portales el costo es marginal. Para campañas outbound a bases de 6.000 contactos se dispara: ~$533 USD solo en abrir conversaciones más seguimientos. Recomienda preguntarle a Claude directamente para que explique el sistema de pricing en detalle.

Como alternativa a Evolution API, Franco menciona que en su agencia usan WhiteCloud para conectar con WhatsApp oficial.

[01:04:40] **Cierre** Franco cierra invitando a la sesión del viernes.
