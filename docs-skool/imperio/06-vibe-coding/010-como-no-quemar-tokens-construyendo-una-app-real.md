# Cómo no quemar tokens construyendo una app real

> Ruta: Vibe-Coding › Cómo no quemar tokens construyendo una app real

---

**Problemas que resuelve la sesión del 8 de Abril:** Cómo gestionar el caché y los tokens en Claude Code para no desperdiciar contexto, cómo usar el framework Getforge para planear apps robustas sin escribir código, y cómo entender Git y los agentes paralelos en proyectos reales.

---

**Intervenciones**

**[****00:00****] Joaco & Carlos – Recap y continuación de Núcleo** Se retoma el proyecto Núcleo (plataforma tipo "segundo cerebro" para guardar y consultar conocimiento). Carlos explica por qué no conviene continuar en el mismo chat tras una semana: el caché de Claude Code expira en 5 minutos, y pasada una hora o un día lo más eficiente es abrir una sesión nueva. Se ejecuta el comando `/avivar` del framework Getforge para retomar sin perder contexto.

**[****10:00****] Carlos – Cache Prompting y ventana de contexto** Explica las tres ventanas de tiempo (5 min, 1 hora, +1 día) y cuándo conviene compactar con `/compact` vs abrir sesión nueva. Muestra cómo el comando `/context` revela el porcentaje de tokens consumidos y por qué hay que mantenerse bajo el 50–75% para evitar alucinaciones.

**[****14:00****] Carlos – Comando **`/model opus-plan` y gestión de modelos Explica cómo usar Opus para planificación y Sonnet para ejecución dentro de Claude Code, y cómo cambiarlo afecta el consumo de tokens.

**[****20:00****] Carlos & Joaco – Modo Yunque vs Modo Forja** Diferencia entre los dos modos de construcción de Getforge: Yunque (secuencial, paso a paso, controlado) y Forja (paralelo, N agentes en sandbox simultáneos, cada uno construye desde cero). Se discute el consumo de RAM por agente (~3–4 GB) y cuándo tiene sentido usar cada modo.

**[****28:00****] Carlos – Mitos Preview y el límite del hardware** Anthropic lanzó internamente un modelo experimental que detectó una vulnerabilidad de 16 años en OpenBSD. No se liberó públicamente porque la infraestructura global aún no puede soportarlo. Se discute la oportunidad de mercado: menos del 5% de profesionales de marketing, ventas, finanzas o legales usan Claude Code hoy.

**[****37:00****] Carlos – Generación del UX Design y anti-slop** Getforge genera el documento de Screen Flows con descripción visual de cada pantalla antes de construir. Esto evita que todas las apps generadas con IA se vean iguales: el modelo recibe instrucciones de colores, tipografía y layout desde la planificación. Se elige estilo inspirado en Notion light.

**[****43:00****] Carlos – Apagado de MCPs para optimizar contexto** Muestra cómo desactivar MCPs innecesarios desde terminal con `/mcp` para reducir el gasto de tokens. Context7 se mantiene activo: es una base de datos con documentación de APIs, frameworks y herramientas que el agente consulta cuando encuentra errores.

**[****48:00****] Carlos – Security Audit del proyecto** Getforge corre una auditoría de seguridad automatizada: detecta issues críticos, altos, medios y bajos, corrige los que puede en el momento y documenta los que requieren Supabase activo (RLS, captcha en login).

**[****55:00****] Carlos – El Blueprint Maestro** Se genera el documento final de planificación: resumen ejecutivo, stack, fases de construcción (7 en total), subfases, tareas, dependencias entre fases y qué se puede ejecutar en paralelo. Es el mapa que van a usar los agentes para construir sin alucinar.

**[****1:05:00****] Carlos – Git, GitHub y control de versiones desde el celular** Explica Git init, commit, push, pull request y merge con analogías visuales. Muestra cómo trabajar desde el celular con Claude Code mobile y luego hacer merge al repositorio principal. Se discute cómo configurar tokens de GitHub con permisos limitados para agentes autónomos.

**[****1:21:00****] Joaco & Carlos – OpenClaw con GPT y Wiki LLM** Carlos lleva 2 meses usando OpenClaw con GPT-4o (Codex 5.4). Joaco activa el plan Go de OpenAI (~$7/mes) para correrlo. Se menciona Obsidian como herramienta de segundo cerebro conectada a MCP, y el concepto Wiki LLM del post de Karpathy: usar un agente para nutrir automáticamente una base de conocimiento en formato Markdown.

**[****1:33:00****] Cierre** Carlos inicializa el repositorio de Núcleo en GitHub y lo deja público para la comunidad. La próxima sesión arranca el build con el Blueprint listo.
