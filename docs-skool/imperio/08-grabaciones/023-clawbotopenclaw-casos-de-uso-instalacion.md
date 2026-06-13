# Clawbot/OpenClaw: Casos de Uso, Instalación

> Ruta: 🔴 Grabaciones › Clawbot/OpenClaw: Casos de Uso, Instalación

**🎬 Vídeo (55.4 min):** https://www.youtube.com/watch?v=vF3MisHetOI

---

**Problemas que resuelve:** Cómo diferenciar entre usar un SAS vs un asistente personal con IA, cómo implementar y asegurar Cloudbot/OpenClaw en servidores, cómo automatizar conversión y procesamiento de PDFs a Excel, y cuándo usar proactividad de agentes vs automatizaciones tradicionales.

**Intervenciones**

**[****00:00****] Franco – Apertura y mecánica de la sesión** Presenta la sesión del viernes 6 de febrero de 2026 con formato de preguntas y respuestas. Explica la dinámica de levantar la mano para participar.

**[****01:28****] Max – Avances con Cloudbot y asistentes personales** Comparte progreso en deploy de Cloudbot en servidores (WhatsApp, Telegram), temas de seguridad y vulnerabilidades. Menciona skills como "Last 30 Days" para investigación automática en X. Explica integración con agentes director e imperial que operan 24/7.

**[****03:00****] Carlos – Arquitectura multi-agente con Cloudbot** Explica cómo crear organigrama de agentes que se comunican entre sí (@asistentemarketing, @asistentecontenido). Describe casos donde agentes se delegan tareas y notifican resultados automáticamente.

**[****05:32****] Daniel – Debate sobre SAS vs asistente personal** Plantea pregunta crítica: ¿cuál es la diferencia entre ofrecer un SAS a empresas vs usar Cloudbot como agente personal? Menciona casos donde empresas necesitan conectar inventario, contabilidad y leads vs tareas personales.

**[****13:01****] Carlos – Casos de uso empresarial con agentes** Responde con ejemplo de startup que usa agentes como empleados: analistas, diseñadores, equipo de marketing, todos operando como agentes IA supervisados por directores humanos. Enfatiza que no es eliminar posiciones sino AI-first design.

**[****16:55****] Max – Personalización de outreach con Moldbot** Explica caso real de cliente con programa high-ticket ($25k+). Cloudbot espera respuestas positivas, accede a bases de datos e historial, personaliza followups basándose en contexto real vs respuestas genéricas de [instantly.ai](http://instantly.ai).

**[****24:00****] Franco – Sistema de memoria dual (permanente + sesiones)** Carlos explica metodología Soul: memoria permanente con relative paths hacia memorias diarias. Ahorra tokens porque el agente busca solo en días específicos en lugar de leer toda la memoria cada vez.

**[****29:00****] Franco – Cloudbot para gestión de clientes** Plantea usar Cloudbot para leer canales de Discord/Slack de cada cliente, reportes semanales y dar status de proyectos sin necesidad de revisar toda la información manualmente.

**[****31:17****] Max – Proactividad como diferenciador clave** Muestra conexión con Apple Health y Rise (tracking de actividades). Cloudbot analiza datos biométricos, sugiere entrenamientos, identifica tareas delegables y recomienda freelancers. Caso extremo: compró número Twilio para llamar al dueño cuando detectó correo urgente ignorado.

**[****34:00****] Daniel – Clarificación: software personal vs SAS** Concluye que Cloudbot es "software personal" o "agente digital", diferente de un SAS empresarial. Sirve para tareas repetitivas, organización personal, filtrado de información.

**[****46:21****] Fran – Formato debate y apertura a consultas** Valora el formato de debate abierto. Abre espacio para consultas técnicas específicas.

**[****47:37****] Serai – Consulta: automatización PDF a Excel en Make** Problema: convertir PDFs de Slack a Excel en Google Sheets. Necesita desglosar dimensiones de muebles con imágenes en celdas específicas.

**Solución:** Franco sugiere [pdf.co](http://pdf.co), smallPDF o ilovePDF. Carlos comparte hack de crear alias en Gmail Workspace para resetear créditos mensuales. Proceso requiere conversión completa primero, luego extraer dimensiones específicas a celdas.

**[****51:25****] Consulta sobre instalación y seguridad de Cloudbot** Carlos explica: Hostinger ofrece instalación one-click. Riesgos: bots escanean IPs públicas intentando inyectar código.

**Solución:** Usar Tailscale (VPN privado), cerrar puertos por defecto, configurar firewall (permitir saliente, bloquear entrante), nunca usar usuario root. Alternativa: plataformas con deploy one-click que gestionan APIs enmascaradas de forma segura.

**[****58:30****] Cierre** Franco agradece participación, valora formato debate. Confirma contenido adicional sobre OpenClaw próximamente. Cierra invitando a seguir el martes.
