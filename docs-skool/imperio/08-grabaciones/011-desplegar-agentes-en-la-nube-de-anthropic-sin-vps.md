# Desplegar agentes en la nube de Anthropic sin VPS

> Ruta: 🔴 Grabaciones › Desplegar agentes en la nube de Anthropic sin VPS

**🎬 Vídeo (61.6 min):** https://www.youtube.com/watch?v=niBj_7a3cL0

---

Esto no es un plan de video, es una grabación de sesión. Voy directo con el formato que ya conozco.

---

**RESUMEN DE SESIÓN — 10 de abril de 2026**

---

**Problemas que resuelve:** Qué es Claude Managed Agents (CMA) y en qué se diferencia de Claude Code y OpenClaw, cuándo conviene usar CMA vs N8N para desplegar agentes, y cómo aprovechar las skills nativas de CMA que no están disponibles de forma nativa en N8N.

---

**Intervenciones**

**[00:00] Franco – Introducción a Claude Managed Agents** Presenta la sesión enmarcada en el lanzamiento de CMA, a dos días de su salida. Explica qué resuelve: el problema de tener Claude Code sin disponibilidad 24/7 y sin infraestructura propia. CMA permite desplegar agentes directamente en la nube de Anthropic, sin VPS, sin computadora encendida, con herramientas, MCPs y skills integradas.

**[05:00] Franco – Arquitectura de CMA: agent, environment, session, vaults** Recorre la documentación y la plataforma. Explica los cuatro conceptos clave: el agente (el modelo), el environment (el contenedor o "habitación" en el servidor de Anthropic), la sesión (la conversación activa) y los vaults (credenciales como conexiones a Supabase). Muestra cómo crear un agente con lenguaje natural desde la plataforma.

**[10:00] Miguel – Duda sobre plan anual de N8N** Consulta si vale la pena hacer el plan anual de N8N dado el surgimiento de CMA. Franco recomienda usar N8N en VPS en lugar de plan anual en SaaS, y aclara que CMA no reemplaza N8N: en casos como WhatsApp con buffer de mensajes, N8N sigue siendo necesario.

**[14:00] Daniel – Caso enterprise: cliente en Ecuador que exige servidor propio** Plantea el caso de una empresa mixta público-privada que requiere alojar todo en su infraestructura. Franco aclara que si usan la API de Anthropic, CMA puede ser un endpoint alternativo al agente de N8N, pero para agentes de voz con VAPI el cambio no aporta diferencias significativas. Advierte sobre los riesgos operativos de sostener un VPS en producción para empresas grandes.

**[19:30] Franco – Comparación de capacidades: CMA vs N8N** Muestra que CMA soporta sesiones multiagente de forma nativa, tiene caché de prompts integrado (lo que reduce el costo de ejecución frente a N8N), y permite usar skills sin ningún desarrollo adicional. Concluye que para el mismo agente con modelos de Anthropic, ejecutarlo en CMA es más barato que en N8N.

**[24:00] Franco – Cuándo usar CMA y cuándo usar N8N** Propone la distinción clave: agentes de cara al cliente (atención, calificación) → N8N, por el control minucioso que requieren. Agentes de uso interno (generación de propuestas, investigación, pipelines de desarrollo) → CMA, por la autonomía, las skills y la facilidad de desarrollo. Un error en un agente de atención al cliente cuesta mucho más que un error interno.

**[29:00] Miguel – ¿Un agente con varios roles o varios agentes especializados?** Franco responde con la filosofía de Nick Saraev: los agentes no son personas, funcionan mejor con tareas específicas. En Robu usan agentes por función: generador de contratos, evaluador de llamadas, planificador de flujos. La comunicación entre ellos crea una pipeline de trabajo sin que ninguno sea sobrecargado.

**[32:00] Miguel – Caso real: 15.000 referencias de medicamentos en Excel** Plantea una automatización con alta carga de datos y cruces complejos. Franco indica la regla: si las tareas son secuenciales A→B→C→D, un agente por tarea. Si el agente tiene que ir y volver, puede agrupar varias. Destaca que CMA es más probable que resuelva flujos complejos donde N8N tiende a volverse demasiado determinista.

**[34:30] Franco – Skills en CMA vs N8N** Muestra en vivo que N8N no tiene skills de forma nativa en su módulo de agentes. Agregarlas requiere desarrollo adicional y proxy. En CMA es nativo. Ejemplos de skills que sólo se pueden usar en CMA: self-improvement (ajuste iterativo del agente), creación de páginas web, cualquier skill del ecosistema Claude Code.

**[39:30] Franco – Gestión de archivos en CMA** Responde la pregunta sobre dónde se guardan los archivos generados por el agente: en el sistema de archivos persistentes del contenedor de la sesión. Para uso interno no hay limitaciones relevantes; para entrega al usuario final hay que integrar el canal de salida (Discord, Telegram, etc.) mediante desarrollo adicional.

**[43:00] Juan Miguel – ¿Cuándo migrar un chatbot de WhatsApp de N8N a CMA?** Franco responde: si es atención al cliente, no migrar. CMA no reemplaza el buffer de mensajes, y las ventajas de skills no aplican en ese caso. Si usa modelos de otros proveedores (GPT), migrar implicaría revisar todo el comportamiento desde cero. Haiku es el único modelo económico en CMA y deja bastante que desear para agentes conversacionales.

**[48:00] Flor – ¿Qué diferencia hay entre OpenClaw, Claude Code y CMA?** Franco dibuja la comparación en vivo en tres columnas: OpenClaw (multimodelo, cron jobs nativos, setup complejo, corre en PC o VPS), Claude Code (skills, modelos Anthropic, cron mejorado, corre en PC, consume desde suscripción y API), CMA (skills nativas, multiagente, sin cron nativo pero invocable desde N8N vía HTTP, corre en la nube de Anthropic, consume solo API). Conclusión: CMA es el más rápido de setear, el más seguro, pero el más costoso en tokens. Claude Code es el más eficiente en costo si se tiene acceso por suscripción.

**[58:30] Cierre** Franco resume que no llegaron a hacer un deploy en vivo pero que el complemento es el video de Benja sobre el armado práctico. Anuncia que en los próximos días van a compartir formas concretas de deploy para que los miembros puedan poner agentes en producción rápido.
