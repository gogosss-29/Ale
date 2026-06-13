# Soporte - 7 de Abril

> Ruta: 🛠️ Soporte › Soporte - 7 de Abril

**🎬 Vídeo (65.5 min):** https://www.youtube.com/watch?v=G8jF9vo70bQ

---

**Problemas que resuelve:** Cómo gestionar el contexto y los límites de uso en Claude Code, cómo estructurar proyectos multicliente en VS Code, y cuándo usar OpenClaw versus Claude Code.

---

**Intervenciones**

**[****00:00****] Eliseo — Conectar Claude a N8N para crear agentes** Tiene N8N instalado en la nube con dominio propio y quiere que Claude genere flujos directamente. Franco le explica la diferencia entre la conexión nativa de N8N en Claude (limitada) y el MCP de la comunidad. El MCP no solo conecta las herramientas sino que incorpora buenas prácticas dentro del flujo de trabajo.

**[****06:00****] Miguel — Límites de uso en Claude Code y gestión de contexto** Llegó al límite de sesión haciendo una página web y no entendía por qué. Franco explica que hay dos límites independientes: el de sesión (cada 5 horas) y el semanal. Muestra cómo monitorear el contexto con `/context` y cómo compactar con `/compact` para reducir el consumo sin perder información importante. También explica que hablar seguido activa el caché de prompting, lo que reduce el gasto por sesión.

Punto adicional de Daniel: revisar qué MCPs y skills están activos, porque cada uno consume tokens desde el arranque. Un MCP innecesario puede cargar el 30-40% del contexto antes de hacer cualquier pregunta.

**[****34:00****] Axel — Organización multicliente en Claude Code** Tiene una agencia de e-commerce y quiere un sistema donde cada cliente tenga su propio contexto sin tener que cambiar de carpeta constantemente. Franco aclara que la estructura correcta no es una carpeta raíz con subcarpetas sino proyectos separados abiertos en distintas ventanas de VS Code. Para el contexto de cliente, recomienda skills específicas por proyecto en lugar de meter todo en el [CLAUDE.md](http://CLAUDE.md), que siempre consume tokens. La [memoria.md](http://memoria.md) sirve para contexto general del proyecto, no para instrucciones de comportamiento.

Para sincronizar la carpeta con el equipo, Carlos sugiere GitHub: cada colaborador hace un pull al empezar y trabaja sobre la versión actualizada.

Sobre automatizar la publicación de meta ads: Franco recomienda un flujo en N8N que se active cuando el estado del anuncio cambia a "listo para publicar" en Notion. Cambiar Drive por Dropbox simplifica bastante la descarga y subida de archivos dentro del flujo.

**[****57:00****] Carlos — Optimizar el uso de OpenClaw** Tiene un agente en OpenClaw consumiendo créditos muy rápido. Franco apunta directo al modelo: Opus es overkill para monitoreo. Haiku o modelos más baratos de Anthropic hacen bien ese trabajo a una fracción del costo. Para desarrollo de flujos en N8N usa Claude Code; para automatizaciones proactivas y multiagente, OpenClaw. En su opinión, Claude Code está cerrando la brecha y probablemente desplace a OpenClaw en el corto plazo.
