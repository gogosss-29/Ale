# Claude Code vs Hermes

> Ruta: 🔴 Grabaciones › Claude Code vs Hermes

**🎬 Vídeo (70.3 min):** https://www.youtube.com/watch?v=tfd-l8-D55c

**📎 Recursos:**
- [framework de auditoría](https://framework-auditoria.netlify.app)

---

**Problemas que resuelve la sesión 15 de Mayo:** Cómo elegir entre Claude Code y Hermes según el tipo de tarea de desarrollo, cómo construir un flujo autónomo de detección y resolución de bugs con GitHub Actions + Hermes + Cloud Code, y cómo conectar chatbots a Instagram y WhatsApp eligiendo entre la API directa de Meta o un proveedor como ManyChat.

---

**Intervenciones**

**[****00:00****] Franco – Apertura y mecánica de la sesión** Explica la dinámica: primero dudas, luego tema técnico si queda tiempo.

**[****01:34****] Anthony – Automatizar setting y cualificación de leads en Instagram** Quiere automatizar conversaciones para una marca de salud en España. Franco explica el esquema: Instagram → ManyChat → Agente → ManyChat → Instagram, y recomienda usar Claude Code para planificar antes de automatizar.

**[****11:59****] Patricio – Flujo en N8N que no conecta Google Sheets ni Gmail** Tiene el flujo creado pero falla en credenciales. Solución: conectar las credenciales de Google en N8N antes de correr el flujo. Se menciona Railway como alternativa de alojamiento gratuito.

**[****22:42****] Cris – Diferencia entre N8N en la nube y N8N self-hosted** Confunde el trial pago de N8N con el N8N self-hosted. Juaco y Franco aclaran: nadie paga la suscripción de N8N; se instala en un VPS (~$5-15/mes) usando Docker y se corre sin límites de uso.

**[****38:07****] Daniel – Claude Code, Hermes y desarrollo autónomo con tickets** Plantea cómo correr sesiones largas de desarrollo sin estar presente. Franco presenta el comando `/goal` de Claude Code para sesiones más autónomas. Carlos y Daniel explican cómo combinan GitHub Actions + Hermes + Cloud Code para detectar errores, crear issues y resolverlos mientras duermen, aprobando solo los pull requests finales.

**[****48:43****] Carlos – Engram y memoria persistente para agentes** Explica Engram (de Gentl AI): herramienta que conecta el agente con Obsidian usando SQLite para memoria persistente. Hermes ya trae SQLite integrado de fábrica, lo que lo hace ideal para flujos de largo plazo.

**[****52:13****] Franco – Traducción al español: Claude Code vs Hermes** Sintetiza para toda la comunidad: Claude Code es el arnés para desarrollar con vos presente. Hermes y OpenClaw son para correr 24/7 y resolver problemas cuando no estás. Hermes puede llamar a Claude Code para resolver tickets de forma autónoma.

**[****56:03****] Juaco – Cómo integrar chatbot a Instagram sin ManyChat** Franco y Carlos explican las dos opciones: ManyChat como intermediario (más fácil, más caro, logs malos) o API oficial de Meta directa (más compleja, más control). Carlos comparte un flujo dentro de ManyChat que usa campos personalizados y llamadas a Claude en bucle, evitando salir a N8N.

**[****1:01:52****] Agustín – Usar Hermes para tickets urgentes en empresa real** Trabaja en middleware para drones con tickets críticos a las 2am. Carlos le explica cómo documentar bien los tickets históricos para que Hermes investigue, proponga solución y deje el 98% hecho; él solo aprueba o decide el 2% final.

**[****1:09:56****] Cierre** Franco da por finalizada la sesión, anuncia que sube el video de la clase anterior y los cita el próximo martes.
