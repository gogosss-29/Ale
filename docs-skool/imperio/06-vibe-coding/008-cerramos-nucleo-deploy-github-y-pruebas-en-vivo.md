# Cerramos Núcleo: Deploy, GitHub y pruebas en vivo

> Ruta: Vibe-Coding › Cerramos Núcleo: Deploy, GitHub y pruebas en vivo

---

**Problemas que resuelve la sesión del 22 de Abril:** Cómo cerrar un proyecto complejo de manera ordenada sin perder contexto, cómo estructurar pruebas automatizadas con Playwright en Claude Code, y cómo organizar colaboración en GitHub con ramas y pull requests.

---

**Intervenciones**

**[00:00] Joaco – Bienvenida y recap del proyecto Núcleo** Presenta el contexto: sesión final del desarrollo de la aplicación Núcleo, un repositorio centralizado para links, PDFs y documentación personal. Explica el marco de trabajo y el sistema "La Forja" desarrollado por Carlos.

**[05:00] Carlos – Selección de modelo y comando "avivar"** Recomienda usar Sonnet con 1 millón de tokens de contexto para la fase de ejecución. Explica el comando `avivar` para retomar sesiones sin perder el estado del proyecto. Compara el consumo de tokens entre Opus 4.6 y 4.7.

**[08:00] Carlos – Métricas de éxito para la Fase 4 (Organización)** Explica por qué es clave pedirle al modelo que defina sus propias métricas antes de ejecutar. Establece 23 pruebas con Playwright como gate de salida. El agente trabaja de manera autónoma desde ese punto.

**[14:00] Carlos – Qué es un Epic y un User Story dentro de La Forja** Diferencia entre Epic (funcionalidad extensa, múltiples sprints) y User Story (flujo de un usuario de inicio a fin). Aplica el concepto a la fase de organización de Núcleo: folders, tags y categorías.

**[19:00] Joaco – Preguntas del chat: próximas sesiones y La Forja** Responde sobre la dinámica de sesiones semanales de Bytecoding. Explica que La Forja es un framework con skills, hooks y sub-agentes para desarrollar aplicaciones web de principio a fin, disponible con descuento para la comunidad.

**[24:00] Carlos – Playwright en acción: pruebas end-to-end automatizadas** El agente abre el navegador de forma autónoma, hace clics, escribe y toma capturas de pantalla. Explica la diferencia entre modo headless y con interfaz visual, y cuándo usar cada uno.

**[32:00] Carlos – Context7: documentación de APIs en tiempo real para agentes** Recomienda instalar Context7 como MCP para que los agentes consulten documentación actualizada de cualquier herramienta (Stripe, Playwright, etc.) sin alucinar. Demuestra cómo instalar un MCP con una sola instrucción en lenguaje natural.

**[39:00] Carlos – Revisión cruzada de código con otro LLM** Recomienda que si construiste un proyecto con Claude, lo revise Codex u otro modelo para obtener críticas más objetivas. Explica el plugin de adversarial review disponible en el marketplace de Claude Code.

**[43:00] Carlos – GitHub: ramas, pull requests y trabajo colaborativo** Muestra en vivo cómo funcionar con ramas para no romper producción. Explica el flujo: rama nueva → desarrollo → git diff → pull request → merge a main. Ilustra con un proyecto real con 4 desarrolladores en paralelo.

**[49:00] Carlos – Fase 5 completada y presentación de Insforts** Termina las fases 4 y 5 con 22/22 pruebas. Introduce Insforts como alternativa a Supabase: pensada para agentes, con autenticación integrada, PG Vector y menor consumo de tokens (estimado 40% menos).

**[58:00] Carlos – Little Bird: captura automática de contexto diario** Muestra una app que graba pantalla, audio y teclado para generar resúmenes automáticos en Obsidian. Explica cómo Claude Code consume esos resúmenes de noche para mantener continuidad entre proyectos.

**[01:31:00] Joaco y Carlos – Cierre y publicación del repositorio de Núcleo** Carlos anuncia que publicará el repositorio en la comunidad con una mini guía. Se abre votación para el tema de la próxima sesión: Claude Code + N8N, Git avanzado o buenas prácticas de seguridad en vivo coding.
