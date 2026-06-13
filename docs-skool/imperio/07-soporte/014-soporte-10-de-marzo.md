# Soporte - 10 de Marzo

> Ruta: 🛠️ Soporte › Soporte - 10 de Marzo

**🎬 Vídeo (57.6 min):** https://www.youtube.com/watch?v=pt76txtEnCA

---

**Problemas que resuelve:** Qué modelo de IA usar para programar sin perder tiempo corrigiendo errores, cómo conectar agentes de WhatsApp con Evolution o WCloud sin romper flujos existentes, y si conviene aprender N8N manualmente o delegar todo a Cloud Code.

---

**Intervenciones**

**[00:00] Franco – Apertura y dinámica de la sesión** Presenta el formato de la sesión, levantada de mano para orden, e invita a traer preguntas y casos concretos.

**[01:07] Walter – ¿Qué herramienta usar para programar con IA?** Comparte que está usando Gemini con Bycoding y tiene muchos errores acumulados. Pregunta qué herramienta recomiendan para programar con menos fricciones.

Solución: Recomendación unánime de Claude (Opus para proyectos complejos, Sonnet para uso diario). Franco y Benja explican la diferencia entre modelos, la opción de Claude Max ($100–$200), y la nueva funcionalidad `/loop` de Claude Code que verifica y reescribe el código automáticamente hasta alcanzar el objetivo. Se recomienda no cambiar de modelo durante una misma conversación para evitar pérdida de contexto y mayor costo.

**[19:27] Daniel – Aporte desde experiencia como programador senior** Con más de 20 años de experiencia, valida el uso de Claude pero advierte sobre el riesgo de Bycoding sin entender lo que se genera. Recomienda usar la opción "Ask" en Cursor antes de ejecutar, hacer prompt engineering preciso, y tener cuidado con errores de mayúsculas/minúsculas en filtros (magic strings/numbers).

**[27:19] Franco – Estrategia de rotación de modelos y caso de backup con Minimax** Explica cómo rotar entre modelos según el tipo de tarea para no gastar tokens innecesariamente. Comparte el caso real de un viernes a las 10 de la noche donde usaron un backup de N8N para que un Cloudbot detectara un error en producción sin acceso a la computadora.

**[31:48] Tomás – ¿Aprender N8N manualmente o ir directo con Cloud Code?** Necesita automatizaciones para reportes de un local gastronómico y un bot de WhatsApp. Pregunta si N8N está quedando obsoleto.

Solución: Franco y Carlos recomiendan aprender N8N como base. Sin entender los nodos, inputs y outputs, es muy difícil dar buenas instrucciones a Cloud Code o debuggear cuando algo falla. Punto medio recomendado: aprender N8N de la mano de Cloud Code. Carlos agrega que él ya dejó de tocar N8N manualmente, pero solo porque pasó por esa curva de aprendizaje antes.

**[11:32] Tomás – Agente de WhatsApp para consultorio odontológico** Quiere hacer un agente recepcionista. Está usando Evolution para outreach y tiene miedo de conectar WCloud y perder esa configuración.

Solución: Franco confirma que conectar WCloud desconecta Evolution. Recomienda migrar todo a WCloud con plantillas si se quiere estabilidad. Si sigue en Evolution para pruebas está bien, pero advierte que al migrar habrá que rehacer los nodos de input/output porque el payload (incluyendo el identificador `remoteJID`) cambia entre plataformas.

**[44:12] Franco – Problemas frecuentes al conectar cuentas en WCloud** Describe los dos bugs más comunes: cuentas vinculadas a un business portfolio diferente, y mensajes que aparecen como "unsupported" cuando se usa coexistencia con WhatsApp Web abierto en computadora al mismo tiempo. Solución: usar WCloud solo en celular + [white.com](http://white.com) en la compu si se quiere leer mensajes.

**[48:37] Octavio – ¿Antigravity u OpenClaw para crear agentes?** Carlos aclara que son herramientas de distinta naturaleza: Antigravity es un IDE, no un agente. La recomendación para crear flujos en N8N es usar Claude Code con los skills de N8N y el MCP conectado.

**[52:00] Franco y Carlos – Claude Code: CLI vs app vs IDE** Carlos describe cómo usa los tres entornos según el contexto: app de Claude en el celular para cambios rápidos con push a GitHub, Antigravity + Claude Code para proyectos completos, y CLI para tareas rápidas sin distracción visual. Cowork se usa cuando se necesita acceso al sistema de archivos local, mover documentos o generar archivos como Excel con dashboard.

**[57:19] Cierre** Franco resume la sesión destacando la discusión sobre modelos, criterios para elegir herramientas y estrategias de integración. Recuerda que el próximo encuentro es el viernes.
