# Claude Code + NotebookLM como RAG

> Ruta: 🔴 Grabaciones › Claude Code + NotebookLM como RAG

**🎬 Vídeo (64.2 min):** https://www.youtube.com/watch?v=o7MgiprKnJU

---

**Problemas que resuelve:** Cómo organizar skills en Claude Code sin saturar el contexto, cómo usar NotebookLM como sistema RAG para consultar grandes volúmenes de información, y cómo coordinar múltiples agentes de IA evitando bucles y solapamiento de tareas.

---

**Intervenciones:**

**[00:00] Daniel – Organización de proyectos con Claude Code** Comparte cómo reorganizó todos sus proyectos usando Claude Code: descargó transcripciones de sesiones, creó un índice de skills unificado con más de 600 skills y armó una estructura de carpetas para que Claude acceda solo a lo necesario según el proyecto activo.

**[07:00] Franco – Diagnóstico del uso de contexto con **`/context` Muestra cómo revisar en tiempo real cuánto contexto consume cada sesión usando el comando `/context`. Explica la diferencia entre ventana de contexto de Sonnet vs Opus y por qué el porcentaje de uso varía según el modelo.

**[07:30] Daniel – NotebookLM: qué es y para qué sirve** Pregunta sobre NotebookLM. Franco explica que es una herramienta de Google que funciona como un RAG optimizado: permite cargar múltiples fuentes (videos, documentos, URLs de YouTube) y consultarlas con Gemini sin necesidad de cargar todo en el contexto del modelo.

**[09:00] Franco – RAG: contexto permanente vs. recuperación dinámica** Explica la diferencia entre meter documentos en el system prompt (consume contexto siempre) y usar un RAG (el agente va a buscar solo cuando lo necesita). Usa una analogía de biblioteca para ilustrar cómo el agente trabaja más limpio y eficiente.

**[27:00] Franco – RAG en N8N: ejemplo real con cliente** Muestra un agente de N8N con un RAG conectado a Supabase. Explica cómo el system prompt instruye al agente a ejecutar la herramienta RAG antes de responder cualquier consulta. Compara esto con el funcionamiento interno de NotebookLM.

**[34:00] Juan – Cómo exportar flujos de N8N desde Claude Code** Pregunta cómo obtener el archivo JSON de un flujo construido por Claude Code para importarlo en N8N. Franco explica la estructura de carpetas (madre vs. proyecto) y cómo pedirle a Claude el enlace directo al directorio donde guardó el archivo.

**[40:00] Juan – Prompts por cuaderno en NotebookLM** Pregunta si se pueden tener system prompts distintos por carpeta en NotebookLM. Franco aclara que cada cuaderno es independiente y tiene su propia configuración, sin posibilidad de vincular cuadernos entre sí.

**[43:00] Henry – Selección de modelos por tarea en OpenClode** Pregunta si es posible asignar modelos diferentes según la tarea dentro de un mismo agente. Franco confirma que sí: tienen configurado MiniMax para tareas rutinarias y Sonnet para tareas complejas. Pendiente compartir el método exacto.

**[45:00] Henry – Coordinación entre agentes sin bucles** Comparte el problema de agentes que se bloquean entre sí al usar sesiones directas. Franco explica su arquitectura de pipeline basada en Airtable como estado compartido: los agentes no se hablan entre ellos directamente, sino que leen y actualizan el tablero para coordinar tareas.

**[55:00] Franco – Qué es un subagente en Claude Code y cuándo usarlo** Explica que los subagentes son archivos markdown con un rol específico que se activan cuando el agente principal detecta que su ventana de contexto está saturada o que la tarea requiere especialización. Cada subagente abre un contexto limpio. Recomienda crear subagentes para tareas repetitivas como N8N, web o copywriting.

**[58:30] Cierre** Franco sintetiza: gestión de contexto, RAG vs. contexto permanente y coordinación de agentes por pipeline. Anticipa la próxima sesión del martes.
