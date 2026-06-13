# Soporte - 21 de Abril

> Ruta: 🛠️ Soporte › Soporte - 21 de Abril

**🎬 Vídeo (58.5 min):** https://www.youtube.com/watch?v=sDRHeqAjCVM

---

**Problemas que resuelve:** Cómo resolver errores de credenciales OAuth en Airtable, cómo configurar [CLAUDE.md](http://CLAUDE.md) a nivel global vs proyecto, y cómo conectar Claude Code o agentes de IA a CRMs y plataformas externas de forma segura.

**Intervenciones:**

**[00:00] Glenda – Error de credenciales en Airtable con N8N** Muestra un flujo funcional que falla en un nodo de Airtable por permisos incorrectos. Solución: regenerar la credencial OAuth desde cero en el centro de creadores de Airtable, configurar redirect URL, obtener client ID y secret, y reconectar con acceso completo a recursos.

**[07:48] Silvia – Claude Code no genera archivos en la carpeta del proyecto** Trabajó con Claude Code desde VS Code pero los archivos generados no aparecen en el directorio esperado. Solución: pedir a Claude Code que busque en toda la computadora el directorio donde realmente trabajó, o arrancar de cero en una carpeta conocida. Recordatorio: siempre abrir la carpeta correcta antes de iniciar sesión.

**[16:31] Mateo – Portfolio comercial de Meta bloqueado para API de WhatsApp** Portfolio bloqueado por intentos fallidos, no se puede eliminar ni crear uno nuevo. Carlos amplía con el flujo completo de partner de Meta. Solución: contactar soporte de Meta en paralelo y usar un portfolio con trayectoria previa. Para escalar el CRM a múltiples clientes, buscar el modo SaaS de Meta para un onboarding embebido. El override de webhook por cliente es clave para separar las respuestas entrantes.

**[27:46] Pregunta anónima – ¿El **[**CLAUDE.md**](http://CLAUDE.md)** es por proyecto o global?** Duda sobre la jerarquía de contexto en Claude Code. Solución: hay dos niveles. El [CLAUDE.md](http://CLAUDE.md) en la carpeta `.claude` del sistema aplica a todos los proyectos; el [CLAUDE.md](http://CLAUDE.md) dentro de cada carpeta de proyecto aplica solo a ese contexto. Ambos conviven. Se puede pedir a Claude que genere o actualice el global diciéndole dónde guardarlo.

**[31:05] Pablo – Migración de automatizaciones de Zapier a N8N** Usa Zapier para notificar acciones de GoHighLevel a Discord, con alto volumen de tareas. Solución: migrar directamente a N8N en VPS para eliminar costos. Pasarle las automatizaciones a Claude directamente para que genere el JSON importable en N8N.

**[35:56] Gustavo – Validación del stack: de Zapier a N8N a Claude con Routines** Comparte que en dos semanas pasó de Zapier a Make a N8N, y terminó corriendo automatizaciones directamente en los servidores de Anthropic via Routines. Intervención positiva: Franco destaca Routines como una de las apuestas más fuertes del ecosistema actual.

**[38:28] Diego – ¿Especializarse en N8N o profundizar en Claude Code?** Duda entre aprender plataformas de automatización o hacer todo desde Claude. Solución: no hay una respuesta única. Claude Code puede hacer todo, pero N8N sigue siendo valioso porque es maleable y no requiere depender 100% de un LLM para mantener flujos en producción. La clave es no quedar atado a una sola herramienta.

**[44:45] Henri + Diego – Cómo usar y adaptar skills de terceros** Reflexión sobre el mercado de skills y cuándo conviene descargar una vs construirla desde cero. Conclusión: una skill ajena puede servir al 10%, al 50% o al 100%. Lo importante es saber leerla, tomar las partes útiles y ajustarla al propio proceso. Nadie conoce mejor el proceso propio que uno mismo.

**[46:14] Henri – Comunicación entre agentes y Evolution API Nexus** Retoma pregunta de sesión anterior sobre cómo coordinar múltiples agentes. Carlos presenta Evolution API Nexus: dashboard open source para orquestar sesiones y subagentes de Claude Code con memoria persistente, métricas de tokens y gestión de skills.

**[51:29] David – Integrar agente con CRM propietario (Repair Shopper) de forma segura** Preocupación por conectar un MCP a un CRM con datos reales de clientes sin entorno de prueba. Solución: configurar el MCP con accesos granulares, restringir acciones de borrado o actualización masiva desde el prompt de sistema, y limitar el alcance a un cliente de prueba. Carlos recomienda la sección de MCPs en el curso Antigravity.

**[57:28] Cierre – Franco recomienda Obsidian con Claude Code** Franco cierra destacando que, entre todo el ecosistema disponible, la integración de Obsidian con Claude Code es la de mayor palanca práctica en este momento. Recuerda la sesión con Carlos del día siguiente.
