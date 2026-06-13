# Soporte - 23 de Septiembre

> Ruta: 🛠️ Soporte › Soporte - 23 de Septiembre

**🎬 Vídeo (59.5 min):** https://youtu.be/tPKlu8lR_ig

---

**Problemas que resuelve:** Cómo validar dominios únicos antes de disparar un webhook, estructurar un bot de ventas en WhatsApp con memoria y traspaso a humano, normalizar fechas para dashboards, estabilizar integraciones de WhatsApp (Meta/WAPI) y resumir feedback mensual con IA para enviarlo a Slack.

---

[00:00] Franco Ricci – Apertura de la sesión  
Formato Q&A de martes, dinámica de levantar la mano y foco en destrabar bloqueos reales en automatización y agentes IA.

[01:05] Jorge – Evitar pruebas repetidas por empresa: dominio único en Airtable  
**Reto:** Permitir un “primer uso gratis” de un generador de avisos con IA, bloqueando usos siguientes por el mismo dominio.  
**Solución:** En **Airtable Automations**, usar **Find records** filtrando `correo contiene {dominio}` y luego **lógica condicional** evaluando `length < 2`. Si cumple, **Ejecutar script / Webhook a Make**; si no, actualizar el registro con “rechazado” y mensaje de contacto. Resultado: el **primer dominio** pasa, los siguientes no disparan Make.  
**Herramientas:** Airtable (Automations, fórmulas), Make (Webhook), IA para redacción.

[22:42] Vicente San Martín – Bot de WhatsApp que califica y deriva a ventas  
**Reto:** Bot que entiende texto/audio, responde dudas del curso y crea tarea en HubSpot cuando hay intención de compra; memoria e intención inestables.  
**Solución:** Migrar de “prompt + múltiples system” a **Make Agent** o **OpenAI Assistant** con **threads** (memoria nativa). En Make, dar **tools** al agente para: guardar nombre/email/ciudad y **actualizar HubSpot** en tiempo real; usar intención como **gate** para crear contacto y tarea. Estándar: un solo system bien diseñado + contexto dinámico.  
**Herramientas:** Make (Agents, Data store), OpenAI Assistants, Whisper, HubSpot, WhatsApp.

[34:43] Juan – Fechas inconsistentes en facturas: unificar para el balance diario  
**Reto:** Entradas con formatos mixtos (dd/mm vs mm/dd) rompen la vista por día en Airtable.  
**Solución:** Forzar formato en la etapa de parseo con `parseDate()` antes de crear la fila en Airtable y **configurar el campo Fecha en ISO** en la base. Además, pedir al modelo IA que **devuelva fecha en **`dd/mm/yyyy` estrictamente.  
**Herramientas:** Make (transformers, `parseDate()`), IA para extracción, Airtable (campo Date en ISO).

[42:44] Oto – WhatsApp Business dejó de responder: “Legacy” y fallback con WAPI  
**Reto:** Webhook de WhatsApp Business (Meta) marcaba **Legacy** y no recibía eventos; con WAPI funcionaba pero aparecían errores intermitentes.  
**Solución:** **Crear nueva conexión oficial en Make** (nuevo Watch Events), reemplazar el webhook viejo en Meta, re-mapear variables. Si se usa **WAPI**, agregar **Error Handler → Ignore** en módulos ruidosos y ajustar **throughput** (mensajes por minuto) + filtro para no auto-responder al propio número.  
**Herramientas:** Make (WhatsApp Business Cloud, Error handler), Meta/WAPI.

[56:27] Ana – Resumen mensual de feedback en Slack con Anthropic  
**Reto:** Analizar cada mes respuestas de Typeform en Google Sheets y enviar un resumen accionable al equipo.  
**Solución:** En Make: **Google Sheets → Search Rows** filtrando por rango de fechas del mes; procesar cada fila o **Aggregate** para un bloque; pasar el lote a **Anthropic/OpenAI** para extraer **4 insights + oportunidades + alertas**; **postear en Slack** con bullets y owners sugeridos.  
**Herramientas:** Google Sheets (Search Rows), Make (Array Aggregator), Anthropic/OpenAI, Slack.

[59:17] Cierre – Próximos pasos  
Foco en profundizar el viernes y seguir afinando casos reales de la comunidad.
