# Claude Code Desktop vs CLI vs Extensión

> Ruta: Vibe-Coding › Claude Code Desktop vs CLI vs Extensión

---

**Problemas que resuelve la sesión del 15 de Abril:** Cómo comparar entornos de Claude Code (CLI, extensión, Desktop, Web), cómo gestionar contexto y tokens eficientemente en sesiones largas, y cómo conectar Claude Code a bases de datos como Supabase mediante MCP para desarrollo real.

---

**Intervenciones**

**[00:00] Joaco & Carlos – Apertura y novedades de Claude** Se menciona la caída temporal de Claude y se presentan las novedades del rework de la app de escritorio: nuevo IDE integrado dentro de Claude Code Desktop con terminal, visor de archivos y panel de tareas.

**[03:25] Carlos – Comparativa de 4 entornos de Claude Code** Explica las diferencias entre Claude Code como extensión (Cursor/Windsurf), desde consola (CLI), en Desktop y en Web. Cada entorno tiene capacidades distintas: la extensión da contexto visual de archivos; el CLI permite ejecutar comandos Bash directos; Desktop combina ambos con interfaz propia; Web es más limitado. La elección depende del proyecto y las necesidades del usuario.

**[08:58] Carlos – Retomando el proyecto Núcleo con la Forja** Explica por qué es mala práctica continuar una sesión vieja de Claude Code después de varios días: el caché se pierde y se desperdician tokens. Muestra el comando `avivar` de la Forja para inicializar sesiones eficientemente. Cambia el modelo de Opus a Sonnet (1M contexto) ya que el plan ya está definido.

**[14:00] Carlos & Joaco – Conexión de Supabase vía MCP y CLI** Conectan Supabase al proyecto Núcleo mediante MCP y CLI simultáneamente. Explican la diferencia: MCP permite operaciones visuales desde el agente; CLI habilita migraciones SQL directas. Se aclara cómo manejar tokens y credenciales de forma segura: nunca pegarlos en el chat, siempre en archivos `.env` o `.mcp.json` locales, ignorados por `.gitignore`.

**[18:35] Carlos – Coolify vs Easypanel vs Portainer** Explica por qué usa Coolify para gestionar contenedores Docker en su VPS (Hostinger): es gratuito, ilimitado en proyectos y tiene conexión MCP nativa. Esto permite que Claude Code cree y configure servicios en el servidor de forma autónoma. Easypanel limita a 3 proyectos en su versión gratuita.

**[35:00] Carlos – Supabase Cloud vs autoalojado** Migra a Supabase Cloud para las pruebas. Explica los límites del plan gratuito: 2 proyectos activos, 7 días de inactividad antes de suspensión, y cuota de requests. Para producción, recomienda activar confirmación de email y revisar políticas de contraseña.

**[38:44] Carlos – Novedades de Claude Code Desktop: rutinas, worktrees y tareas** Muestra funcionalidades nuevas: rutinas programadas (para correr tareas en horarios de menor costo), worktrees (copias aisladas del repositorio para pruebas sin afectar `main`), panel de tareas en tiempo real y vista del plan completo. Se compara con la experiencia de Cursor.

**[47:30] Carlos – Fase 2 del desarrollo: Dashboard con datos reales y Playwright** Claude Code ejecuta pruebas automatizadas con Playwright: navega la app, crea cuenta, agrega ítems, prueba duplicados y elimina tarjetas. Detecta un bug con drag-and-drop en Playwright (funciona con mouse real, no con el simulado) y lo documenta. Todo funciona sin intervención manual.

**[51:00] Joaco – Demo de Antomatic (proyecto propio)** Joaco presenta su aplicación construida con la Forja: genera demos de chatbots para e-commerces de forma casi automática. El flujo: se ingresa la URL de la tienda, Claude hace scraping con Playwright, genera una base de datos en Supabase y configura un chatbot con tono, fallback y system prompt apropiados. El resultado es un popup funcional idéntico al sitio real, con script instalable.

**[52:04] Carlos – Integración de Claude Code con N8N** Responde cómo trabajar con N8N desde Claude Code: conectar el MCP oficial de N8N, importar los flujos existentes, documentarlos y generar un `CLAUDE.md` con las preferencias del usuario (nodos habituales, credenciales activas, estilo de construcción). Anuncia sesión exclusiva dedicada a este tema.

**[58:30] Carlos – Fase 3 completada y cierre** Se termina la fase 3 de Núcleo con todas las verificaciones aprobadas. Carlos ejecuta `git push` con mensaje de commit descriptivo para que el repositorio quede actualizado. Anuncia que habrá una sección exclusiva de la Forja en el classroom de la comunidad con casos de uso paso a paso.
