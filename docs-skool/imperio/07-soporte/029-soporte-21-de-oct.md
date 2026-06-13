# Soporte - 21 de Oct

> Ruta: 🛠️ Soporte › Soporte - 21 de Oct

**🎬 Vídeo (56.7 min):** https://www.youtube.com/watch?v=hah2-9Wj6iA

---

**Problemas que resuelve:** Cómo hacer prospección en WhatsApp sin disparar bloqueos, abrir conversaciones con plantillas y webhooks bien configurados, paquetizar y cotizar asistentes de voz para empresas, y elegir entre Make o n8n según costos, volumen y perfil técnico (incluyendo SMS y “warm-up” de números).

---

## Intervenciones (cronológicas)

[00:00] **Host – Apertura y dinámica**  
Formato Q&A de los martes; cómo “levantar la mano” y ordenar la fila para resolver bloqueos puntuales de implementación.

[02:01] **Agustín – Prospección por WhatsApp (estrategia y límites)**  
Objetivo: 100 contactos/día con mensajes personalizados. Riesgo: reportes y bloqueos. Recomendación: comenzar con 15–25/día, “warmeo” del número con conversaciones reales, y asumir que habrá números que caigan (tener plan de reemplazo). Herramientas: WhatsApp Business API, base de datos de leads.

[12:53] **Agustín – Apertura de conversaciones con plantillas**  
Flujo correcto: 1) Enviar **plantilla aprobada** (HSM) → 2) Usuario responde (botón de respuesta o texto) → 3) Ventana de conversación libre. Evitar links como única “respuesta” si no generan mensaje entrante. Métrica y riesgo: reportes bajan reputación del número. Herramientas: Meta WhatsApp Cloud API, botones de respuesta.

[16:01] **Agustín – Webhook en Make que no aparece**  
Síntoma: conexión de WhatsApp en Make no expone URL del webhook. Solución: crear **Custom Webhook** manual en Make y pegarlo en Meta Developers (Callback URL + Verify token). Mantener separados “input” (webhook entrante) y “output” (envío) dentro del escenario.

[21:38] **Gabriel – Asistente de voz para aseguradora (Vapi) – bug de server messages**  
Error al publicar por duplicado en **Server Messages** (“End of call report” repetido). Fix: eliminar el mensaje duplicado y publicar; el webhook vuelve a registrar datos. Caso de uso: demo para empresa con múltiples agencias. Herramientas: **Vapi**, Make (webhook de End of Call Report).

[27:16] **Gabriel – Pricing y alcance para voz**  
Claves: estimar tiempo de desarrollo + costos de uso (Vapi reportado a **$0,16/min**) y proponer **período de prueba** para medir volumen real. Documentación base: el asistente puede leer **documentos de texto** (conocimiento del negocio). Paquetizar setup + mantenimiento, y separar costos variables del proveedor de voz.

[33:05] **Fernando – ¿Make o n8n para automatizaciones y agentes?**  
Criterios:

- **Perfil técnico**: Make es más amigable; n8n exige más técnica.
- **Escala/costos**: Make cobra por operaciones; en **n8n** (self-hosted) el costo por ejecución tiende a cero, ideal para **altas volúmenes** (agentes, chat, routing).
- **Infra**: n8n requiere **VPS**/hosting (ej. Hostinger/VPS).  
Recomendación: si ya dominas Make, arranca allí y **migras** a n8n cuando el volumen lo justifique.

[40:48] **Comparativa de costos real**  
Ejemplo compartido: ~30–50 conversaciones/día en Make pueden sumar decenas de miles de operaciones/mes (coste relevante). En n8n self-hosted, ese costo operativo no crece igual. Decisión: construir MVP en Make; si escala, re-armar en n8n.

[42:31] **Jorge – Asistente de voz + confirmación por SMS**  
Necesidad: enviar SMS al final de la llamada. Opciones: **Twilio** (puede pedir website) o **Vonage** como alternativa. Sitio rápido sin fricción: generadores tipo **Bolt** (para cumplir requisito de sito en Twilio). Integración: webhook desde Vapi → SMS API.

[50:58] **Marcos – Cómo empezar si tengo lógica pero aún no arranco**  
Ruta sugerida: seguir **“Make desde 0”** (módulos cortos), practicar en paralelo con **Airtable** como BD, y replicar automatizaciones básicas (facturación, formularios → Sheets → email) para afianzar inputs/outputs y mapping. Consejo de la comunidad: importar plantillas, “romper y entender”, luego re-armar propio flujo.

[56:17] **Cierre – Próximos pasos**  
Profundizar en: plantillas de WhatsApp, webhooks en Make, métricas de reportes, paquetización de asistentes de voz y selección de stack según escala prevista. Revisión el viernes en la sesión temática.
