# Codex vs Claude Code: Comparación | Solución

> Ruta: 🔴 Grabaciones › Codex vs Claude Code: Comparación | Solución

**🎬 Vídeo (40.2 min):** https://www.youtube.com/watch?v=0ftBlqDn8a0

---

**Problemas que resuelve:** Cómo configurar correctamente secuencias de chatbot con triggers múltiples en Make y Manichat, cómo evitar que un flujo de cualificación se rompa después del primer mensaje, cómo usar etiquetas para mantener conversaciones persistentes, y comparación práctica entre Codex y Claude Code para generación de código HTML.

**Intervenciones**

**[00:02] Franco – Apertura y demostración inicial de Codex** Presenta la sesión del martes con formato de resolución de dudas. Hace instalación en vivo de Codex para mostrar la herramienta por primera vez. Explica templates disponibles y estructura de skills.

**[02:06] Franco – Comparación Codex vs Claude Opus 4.6** Propone hacer prueba comparativa del mismo prompt en Codex y Claude Code (Opus 4.6) para evaluar diferencias en generación de código.

**[04:52] Daniel – Advertencia sobre trabajo en paralelo** Aclara limitación importante: cuando se codifica, no se pueden actualizar múltiples archivos simultáneamente en diferentes chats porque se rompe el código. Un chat modifica un archivo y otro lo corrige, causando conflictos. Funciona bien para tareas independientes, no para dependencias del mismo proyecto.

**[06:23] Franco – Análisis de resultados Codex** Muestra que sin vincular repositorio de GitHub, Codex ya generó archivos y código corriendo en navegador. Destaca la velocidad de setup inicial.

**[07:32] Gabriel – Consulta: Chatbot de cualificación en Instagram se rompe** Presenta problema: flujo con Manichat + Make + Chat GPT para agendar llamadas cualificando leads vía Instagram DMs. El bot responde primera pregunta ("¿de qué es tu negocio?"), pero cuando el usuario contesta, la conversación muere. No sigue cualificando ni agenda. El router no ejecuta ninguna de sus dos opciones (agendar o seguir cualificando).

**[11:25] Franco – Diagnóstico del problema** Identifica que el flujo pasa correctamente por el router (3 segundos de ejecución), pero no envía respuesta al usuario. Solicita revisar filtros del router y ejecución completa.

**[14:33] Franco – Raíz del problema: trigger mal configurado** Descubre la causa: el trigger de Manichat solo se activa cuando el mensaje contiene "quiero más información". Primer mensaje funciona, pero segundo mensaje del usuario ya no activa la automatización porque el flujo ya terminó. No es un flujo continuo.

**Solución completa: Arquitectura de dos secuencias con etiquetas**

**[24:10] Franco – Diseño de solución con dos flujos** Explica estrategia: crear dos secuencias separadas.

- **Primera secuencia:** maneja mensaje inicial ("quiero más información"), responde primera pregunta y agrega etiqueta "contacto IA" al contacto.
- **Segunda secuencia:** copia de la primera pero con trigger "respuesta predeterminada" (cualquier mensaje) y filtro al inicio que verifica si contacto tiene etiqueta "contacto IA".

**[25:00] Franco – Implementación paso a paso** Guía implementación:

1. Duplicar automatización existente
2. En Manichat, cambiar trigger de segunda secuencia a "respuesta predeterminada"
3. Crear etiqueta "contacto IA" desde sección de contactos
4. Agregar filtro al inicio de segunda secuencia: "si etiqueta = contacto IA → continuar"
5. En primera secuencia, agregar acción al final: "añadir etiqueta contacto IA"
6. Eliminar nodos innecesarios de "esperar respuesta del contacto"

**[34:25] Franco – Explicación de lógica final** Resume funcionamiento: Primera secuencia solo se activa con "quiero más información", envía pregunta inicial, agrega etiqueta y termina. Cualquier respuesta posterior del usuario activa segunda secuencia porque ya tiene la etiqueta, permitiendo conversación continua con Make y Chat GPT.

**[38:02] Franco – Comparación Codex vs Claude Code** Paco comparte resultado de Claude Code con mismo prompt. Franco muestra ambos HTML en pantalla. Conclusión: resultado de Claude Code es visualmente superior (mejor diseño gráfico, tiene animaciones). Codex genera código funcional pero más básico. Único defalle de Codex: elementos UI se sobreponen.

**[39:49] Cierre** Franco agradece participación, menciona que probablemente dedique sesión completa a Codex en el futuro para prueba exhaustiva. Despide y desea buena semana al equipo.
