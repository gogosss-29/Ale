# Soporte - 3 de Febrero

> Ruta: 🛠️ Soporte › Soporte - 3 de Febrero

**🎬 Vídeo (54.2 min):** https://www.youtube.com/watch?v=vTqMAYOH72A

---

**Problemas que resuelve:** Cómo automatizar completamente el ciclo de ventas de una agencia de diseño web (desde prospección hasta cierre), cómo validar métodos de outreach antes de automatizar, cómo usar IA para negociación automática por email, y cómo crear landing pages personalizadas en 30 segundos para outreach masivo con Cloudbot.

**Intervenciones**

**[****00:00****] Franco – Apertura y formato de auditoría en vivo** Presenta sesión con formato roleplay: un participante simula ser cliente/empresa que necesita auditoría, Franco hace preguntas para detectar necesidades y diseñar solución con automatizaciones e IA. Menciona grabaciones anteriores exitosas con esta dinámica.

**[****04:02****] Raúl – Consulta sobre speech preparado** Pregunta si es recomendable tener speech preparado antes de llamada de ventas.

**Solución:** Franco explica que prefiere no hacerlo porque sesga la conversación. Prefiere enfoque natural para detectar necesidad real vs llegar con propuesta predefinida. Aclara que ambos métodos funcionan, depende de con cuál te sientas más cómodo.

**[****04:57****] Max – Caso: Automatizar outreach de agencia de diseño web** Presenta escenario: agencia que vende landing pages ($300-$500). Descubrieron forma de crear MVPs de páginas web en 35 segundos con Cloudbot/Claude Code. Ya vendieron 3 en 2 días. Quiere automatizar todo el ciclo: outreach, negociación, cierre con Stripe, usando bases de datos de Apollo o Instantly.

**[****07:20****] Franco – Validación de método antes de automatizar** Explica principio crítico: muchos quieren automatizar outreach sin haberlo validado manualmente primero. Dos enfoques:

- **Conservador:** persona real arma funnel, valida método, luego se automatiza
- **Agresivo:** si hay presupuesto amplio ($5k+), se puede iterar automatizando directamente

Enfatiza que con presupuesto limitado ($2k o menos), mejor validar manualmente para evitar automatizar "por la izquierda cuando era por la derecha".

**[****10:02****] Franco – Ventaja diferencial con tecnología actual** Destaca que con Cloudbot generando páginas en 30 segundos, la automatización puede ser mejor que humanos por velocidad. No es solo eficiencia, sino capacidad de outreach que humanos no tienen. Permite enviar producto terminado en primer contacto.

**[****11:13****] Franco – Mapeo del sistema completo en Miro** Inicia diseño visual del flujo completo de automatización. Primera etapa: obtención de base de datos con campos clave (nombre empresa, web, email, empleados, potencial contacto, potencial dolor, industria).

**[****13:15****] Franco – Importancia de personalización** Explica máxima de marketing: mientras más personalizado el mensaje, mayor tasa de conversión. Por eso base de datos rica es crítica para comunicación asertiva.

**[****14:16****] Franco – Sistema de tiers para priorización** Diseña filtrado inteligente con IA que analiza si empresa tiene web y su calidad:

- **Tier 1 (verde):** No tiene web → prioridad máxima, mayor oportunidad
- **Tier 2 (amarillo):** Tiene web de baja calidad → segunda prioridad
- **Tier 3 (rojo):** Tiene web de alta calidad → última prioridad

Estrategia: contactar todos los verdes, luego amarillos, luego rojos.

**[****18:25****] Franco – Secuencia técnica en N8N** Mapea flujo técnico:

1. Trigger cada 15 minutos
2. Obtener info de empresa desde base de datos
3. Filtrado inteligente (IA lee HTML, determina calidad)
4. Crear prompt con OpenAI usando toda la data
5. Enviar mensaje a bot de Telegram (Cloudbot)
6. Esperar 5 minutos (segunda secuencia)

**[****28:10****] Franco – Segunda secuencia: Deploy y envío** Secuencia separada que se activa cuando bot responde:

- Trigger: webhook de Telegram cuando bot manda página web con deploy
- Redacción de mensaje personalizado con IA
- Envío de email con URL de web

Resultado: email personalizado con landing page ya creada específicamente para el prospecto.

**[****35:09****] Franco – Disclaimer sobre predicción de respuestas** Advierte error común: creer que se pueden predecir todas las respuestas de prospectos en fase de diseño. Enfatiza que categorización es hipótesis inicial que se refina con práctica real.

**[****39:00****] Franco – Automatización de negociación con agentes IA** Diseña tercer flujo crítico:

- Trigger: watch emails (se activa cuando lead contesta)
- Filtro de categorización con IA: interesado en comprar, interesado en negociar, no interesado
- **Agente negociador:** IA con parámetros para negociar según presupuesto, etapa, objeciones
- **Agente vendedor/cobranza:** cuando ya hay interés de compra, envía link de Stripe personalizado

**[****43:40****] Franco – Punto crítico del sistema** Identifica la negociación automática como el punto crítico y diferenciador. Muchas herramientas hacen outreach masivo, pero pocas negocian automáticamente. Sin esto, el dueño se convierte en cuello de botella respondiendo emails manualmente.

**[****45:24****] Franco – Personalización de links de pago** Propone usar tool de IA para generar links de Stripe personalizados: "Página web Robu Systems, descuento especial $250" vs link genérico. Mayor personalización aumenta conversión.

**[****47:12****] Franco – Cierre del ciclo: Notificación de venta** Última secuencia:

- Trigger: webhook Stripe cuando lead compra
- Enviar WhatsApp a dueño con resumen: "Le vendimos a Juaco, este es su número, compró esto, interesa esto, háblale para delivery"

Dueño solo interviene post-venta para delivery, todo el marketing/ventas es automático.

**[****50:59****] Max – Validación del método con casos reales** Confirma que el "loop" de mostrar página web ya hecha tiene closing rate mucho más alto. Ya vendieron a estudio de abogados y consultora auditora viendo la demo. Comparable a cuando hacían páginas en WordPress/Divi en 1 hora para opening calls.

**[****52:28****] Franco – Concepto de lead magnet ultra-personalizado** Resume: meter valor fuerte y diferenciado en primer outreach (producto terminado) puede subir tasas de conversión dramáticamente. Aplicable no solo a páginas web sino a otros servicios (menciona Carlos con staging para Real Estate).

**[****53:43****] Cierre y próximos pasos con Cloudbot** Franco anuncia videos próximos con Carlos mostrando instalación de Cloudbot en VPS desde cero. Menciona que Benja subió videos y ha recibido múltiples ataques (prompt injection, brute force), trabajando en protecciones todo el fin de semana.
