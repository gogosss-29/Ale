# Haiku no sirve: modelo y arquitectura en agentes

> Ruta: 🔴 Grabaciones › Haiku no sirve: modelo y arquitectura en agentes

**🎬 Vídeo (66.0 min):** https://www.youtube.com/watch?v=UzCzr-H9yRM

---

**Problemas que resuelve la sesión 5 de junio:** Cómo elegir el modelo de lenguaje correcto para agentes conversacionales, cómo estructurar prompts para que el modelo obedezca, cómo separar información estática y dinámica en flujos de WhatsApp, cuándo usar N8N versus código puro, y cómo proteger la infraestructura de un agente desplegado.

---

**Intervenciones**

**[****00:00****] Franco – Apertura y formato de la sesión** Explica la dinámica: primera mitad para dudas y consultas uno a uno, segunda mitad para tema técnico si el tiempo lo permite. Invita a levantar la mano desde el botón de reacciones.

**[****01:49****] Tomás – Agente de WhatsApp para e-commerce que no obedece el prompt** Armó un agente para un cliente en N8N usando Claude Haiku. El prompt tiene reglas de tono (evitar lunfardo, no usar "che") que el modelo ignora. También tiene un PDF de siete páginas del cliente como referencia y está construyendo un recuperador de carritos abandonados.

Solución: cambiar inmediatamente a Claude Sonnet, que es mucho más obediente. Reorganizar el prompt por categorías separadas (rol, tono, formato, restricciones) con headers de markdown. Eliminar contradicciones internas. Extraer el 20% útil del PDF, descartar el resto. Para información variable del cliente (horarios, promociones), usar AirTable con una interfaz simple donde el cliente pueda editar sin tocar el flujo. Para catálogo de productos, conectar vía API al e-commerce en lugar de hardcodear en el prompt. Para el recuperador de carritos, conseguir acceso de administrador al WooCommerce antes de seguir depurando.

**[****07:00****] Franco – Por qué Haiku falla en agentes conversacionales** Explica el ciclo vicioso: modelo poco obediente → el builder agrega más instrucciones → el modelo obedece menos. La solución no es más prompt, es mejor modelo. Haiku solo sirve para tareas binarias (cero o uno) donde se quiere ahorrar tokens antes de pasar al agente principal.

**[****15:17****] Carlos – Cómo separar prompt fijo y dinámico usando AirTable** Comparte su implementación: tabla de prompts en AirTable dividida por secciones (rol, límites, herramientas, info del negocio). El prompt en N8N combina un bloque fijo que el cliente no toca y bloques dinámicos que se alimentan de AirTable en tiempo real. El cliente tiene una interfaz sencilla para cambiar horarios, feriados o promociones sin que el builder tenga que intervenir.

**[****23:33****] Óscar – Qué herramienta usar para agente WhatsApp que vende tickets** Quiere automatizar: lead de Meta → WhatsApp → conversación → link de pago → QR de confirmación.

Solución: N8N para el flujo completo, Whitecloud para la conexión con WhatsApp, agente de IA dentro de N8N. Alternativa: Claude Code para código puro si quiere más control. Tiempo estimado para alguien que recién empieza con dedicación: dos semanas a un mes.

**[****28:20****] Iván – N8N versus código puro para su agente setter** Está migrando a código puro porque Claude Code puede ver y depurar el flujo directamente. Pregunta si pierde algo.

Solución: no pierde nada, gana control. En código puro puede implementar caché de prompts (prompt caching), que reduce hasta un 90% el costo del system prompt enviando siempre el mismo bloque cacheado. El system prompt se cachea; el user prompt (lo que escribe el usuario cada turno) no. Recomendación: documentar bien, usar logs por ejecución, armar ramas en GitHub función por función.

**[****34:57****] Daniel – El código puro desde la mirada de un programador de 20 años** Coincide con Franco. Advierte sobre los riesgos reales: cache invalidation cuando cambia el contexto, magic strings que fallan por mayúsculas, AI que va directo del punto A al Z saltándose pasos necesarios. Su workflow: Claude Code + GPT-5 alternados, pidiendo avanzar paso a paso y aprobando cada cambio antes de que el modelo continúe.

**[****52:56****] Andrés – Cómo revisar seguridad de un agente N8N en producción** Tiene su agente armado en N8N (Shopify, Bolt, pasarelas de pago) y quiere saber cómo auditarlo.

Solución: el foco de seguridad no está en el flujo sino en el VPS donde corre N8N. Pedirle a Claude Code que revise la configuración del servidor. Dentro del flujo, agregar guardarrails (nodo de evaluación antes del agente) para detectar prompt injection. Las restricciones de tono en el prompt (no hablar de política, mantenerse en el nicho) ayudan pero no reemplazan la seguridad de infraestructura. Sobre el modelo: GPT-4.1 mini cae entre Haiku y Sonnet; si da problemas, subir a Sonnet o GPT-5.4 mini.

**[****59:41****] Roma – Codex versus Claude Code, y cuándo usar Go High Level** Pregunta por sensaciones con Codex y orientación sobre GHL.

Respuesta Codex: Franco lo probó poco porque ya tiene el ecosistema armado en Claude Code. El costo de cambiar supera la ganancia marginal. Reportes de conocidos: está muy potente. Para la barbería con agendamiento que Roma quiere armar: código puro es suficiente, N8N para el backend, Claude Code para el frontend. GHL tiene sentido cuando se necesita gestionar funnels, múltiples contactos, llamadas y pauta desde un solo lugar; para un proyecto chico, es sobredimensionado.

**[****01:04:33****] Franco – Cierre** No hubo tiempo para el tema técnico preparado. Queda pendiente para la próxima sesión. Próximos encuentros: lunes con Juaco (recomendado para nuevos), martes sesión regular.
