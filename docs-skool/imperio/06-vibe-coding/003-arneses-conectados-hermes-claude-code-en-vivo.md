# Arneses Conectados: Hermes + Claude Code en Vivo

> Ruta: Vibe-Coding › Arneses Conectados: Hermes + Claude Code en Vivo

**📎 Recursos:**
- Arnes Presentacion

---

**Problemas que resuelve la sesión 27 de mayo:** Qué es un arnés y cómo se diferencia de un LLM, cómo conectar Claude Code con Hermes para trabajar agentes remotos vía A2A, cómo intercambiar modelos sin perder la memoria ni la configuración del proyecto, y cómo elegir entre MCP y CLI para optimizar consumo de tokens en arneses como Cloud Code.

**Intervenciones**

[00:00] Joaco — Apertura de la sesión Saluda a la comunidad, da la bienvenida a una nueva sesión de Vibecoding junto a Carlos y explica las dinámicas de interacción (levantar la mano, chat).

[04:30] Carlos — Agenda de la sesión Anuncia los temas: definir qué es un arnés, profundizar en Hermes, conectar Hermes con Cloud Code y mostrar el Agents SDK de Cloud Code aplicado a una interfaz web. Adelanta que verán demos reales sobre Núcleo (PKM open-source construido en sesiones anteriores).

[06:11] Carlos — LLM vs arnés (la analogía del cerebro) Explica que un LLM solo es "un cerebro en un frasco": recibe texto y predice texto, pero no puede leer archivos, correr comandos ni instalar nada. El arnés es la infraestructura que envuelve al LLM para que pueda ejecutar tareas reales del mundo. Define los componentes clave: Bash, File System, Sandbox, Agent Loop y memoria persistente.

[10:35] Joaco — Analogía del motor y la carrocería Refuerza el concepto: el LLM es el motor, el arnés es la carrocería completa. Un motor potente en una mala carrocería no rinde, y la ventaja es que el motor (modelo) es intercambiable.

[11:46] Carlos — Arneses anidados y filtración del arnés de Cloud Code Explica que puede haber arneses dentro de arneses (VS Code → extensión de Cloud Code → Forge corriendo dentro). Menciona la filtración del arnés de Cloud Code hace meses, que permitió que la comunidad clonara forks del sistema y entendiera cómo funciona por dentro.

[15:30] Carlos — Diferencia entre Hermes (arnés con agente) y Cloud (modelo) Aclara la confusión común: Hermes es un arnés en el que vive un agente; Cloud Code es un arnés que usa modelos de Anthropic. El mismo Cloud Code (CLI, extensión, app móvil) es el mismo arnés con diferentes interfaces. Dentro de Cloud Code se pueden correr modelos chinos (DeepSeek, Qwen, Kimi) modificando los endpoints.

[20:30] Carlos — Las 5 piezas de un arnés y por qué la memoria vive en el arnés Detalla Bash Tool, File System, Sandbox + Permissions, Agent Loop y Skills/MCPs. Insiste en que la memoria del proyecto (archivos .md, PRD, blueprint, auto-aprendizaje) debe vivir en el arnés, no en el modelo. Así, si se acaban los tokens de Opus, se cambia a DeepSeek y el proyecto continúa sin perder contexto.

[24:50] Carlos — El Agent Loop en 3 fases Explica el corazón del arnés: Gather Context → Take Action → Verify. El loop se repite hasta cumplir el objetivo, agotar turnos o detectar fallos repetidos que requieran intervención del usuario.

[28:05] Carlos — Cloud Code como arnés de fábrica Aclara que cuando abres Cloud Code en terminal no estás hablando con un modelo, sino con un arnés completo. Anuncia que el modo auto (antes exclusivo de Opus 4.7) ya está disponible también en Sonnet 4.6.

[29:25] Tony — ¿El arnés se construye por el tema de la memoria? Solución: Carlos aclara que la memoria es una ventaja, pero no el motivo principal. El motivo central es tener consistencia en el trabajo, y entender que los arneses no son exclusivos de bytecoding: sirven para marketing, contenido, copy, SEO, campañas de Meta, etc.

[30:50] Álvaro — Diferencia entre Bypass Permissions y Auto Mode Solución: Bypass Permissions ejecuta sin pedir permiso pero te obliga a cambiar manualmente a Plan Mode. Auto Mode es un híbrido que detecta cuándo el usuario quiere planear, cambia a Plan Mode automáticamente y regresa a Bypass. Ya disponible en Sonnet 4.6.

[34:42] Iván — ¿Conviene activar Backup and Sync en VS Code? Solución: Sí. Permite sincronizar settings, atajos, MCPs y extensiones entre múltiples equipos con la misma sesión iniciada. Especialmente útil después del desastre de Antigravity 2.0 que reseteó configuraciones.

[37:50] Iván — MCP vs CLI: ¿cuál consume menos tokens? Solución: No es uno u otro, se pueden usar ambos. El MCP mantiene una conexión persistente (ideal para flujos interactivos como Playwright que requieren decisiones en cadena), pero consume tokens en cada mensaje porque se carga en el contexto. El CLI consume tokens solo cuando se ejecuta. Recomendación: desactivar MCPs no usados desde `/mcp` → disable, sin desinstalar.

[50:00] Charly — Confusión con Antigravity 2.0 vs Antigravity IDE Solución: Carlos muestra las dos versiones. Antigravity 2.0 es la nueva (parecida a Cloud Desktop, limitada, sin MCPs por proyecto). Antigravity IDE es el fork de VS Code de siempre. Google rectificó y permite importar la configuración previa al actualizar.

[53:50] Iván — ¿Para qué usar Antigravity 2.0 si está tan limitado? Solución: Para usuarios con suscripción Gemini que quieran aprovechar Gemini 3 Flash (rápido y potente). Funciona como un "Google AI Studio con esteroides" para crear MVPs rápidos sin configuraciones complejas.

[57:00] Carlos — Agents SDK (antes Cloud Code SDK) Explica que el SDK convierte al arnés en un subproceso invocable desde código. Permite construir web apps con un chat embebido conectado a Cloud Code de fondo, con acceso a MCPs, Skills y [Agents.md](http://Agents.md).

[59:15] Carlos — Demo de Agents SDK con Núcleo Muestra una web app local que ejecuta comandos sobre el repositorio Núcleo usando el SDK. Demuestra cómo desde la interfaz web puede pedirle a Cloud Code que cree archivos, ejecute comandos y trabaje el proyecto sin abrir el CLI. Caso de uso: integrar agentes en aplicaciones propias con todo el contexto del arnés.

[01:04:00] Carlos — ACP (Agent Communication Protocol) Define ACP como el estándar abierto creado por Zed que permite que un agente le pida a otro agente que trabaje. Aclara la diferencia con MCP: MCP conecta agente con herramientas; ACP conecta agente con agente. Actualmente solo Copilot lo tiene habilitado nativamente con Cloud Code.

[01:06:50] Carlos — Demo en vivo: Hermes hablando con Cloud Code Desde Discord, pide a Hermes que revise el repositorio de Núcleo y consulte a Cloud Code qué features faltan. Hermes ejecuta el comando en la Mac mini, recibe el JSON y devuelve el resumen. Explica que hay 3 formas de conectar arneses: PrintMode (lo que usa, batch sin tiempo real), Tmux (interactivo, como parche de ACP), y ACP nativo (aún no disponible en Cloud Code).

[01:13:30] Joaco — Cómo replicar el setup en un VPS sin Mac mini Aclara que en un VPS basta con instalar Cloud Code dentro del usuario donde corre Hermes (manteniendo aislamiento de seguridad), instalar GitHub CLI y configurar un script que mantenga los repositorios actualizados con `git pull` antes de cada sesión.

[01:17:30] Juan Carlos — ¿Cuánto se consume al mes con Hermes + opencode? Solución: Depende totalmente del uso. Carlos muestra su consumo real con DeepSeek V4 Pro vía opencode Plan Go (10 USD/mes): día pico de 10 USD pero distribuido en rolling weekly + monthly. Recomienda DeepSeek V4 Pro: rendimiento cercano a Opus 4.7 y GPT-5.5 pero 16 veces más barato.

[01:22:30] Iván — ¿Conviene opencode para programar en vez de pagar Cloud Code Pro? Solución: Carlos vuelve a aclarar la confusión entre arnés y modelo. Se puede usar el arnés Cloud Code con modelos de opencode, o el arnés opencode con modelos de Anthropic. Son decisiones independientes.

[01:30:00] Rodrigo — Seguridad de datos del cliente Solución: Todos los datos enviados a servidores se usan para entrenamiento salvo que se firme ZDR (Zero Data Retention) con Anthropic en plan Enterprise. Disponible como add-on en Enterprise Self-Serve y Enterprise Sales-Assisted, no incluido por defecto.

[01:34:00] Arturo — ¿Hermes puede robarme datos bancarios? Solución: Hermes en sí no, pero un Skill o plugin malicioso instalado sí podría comprometer el sistema. El riesgo es el mismo que instalar cualquier paquete npm o abrir un correo malicioso.

[01:35:00] Arturo — ¿Hermes es el arnés principal de Carlos? Solución: No. Cloud Code es el arnés principal. Sobre Cloud Code corre Forge (arnés propio con método, autoblindajes, Skills y comandos de alto nivel). Está desarrollando Forja, que sí está pensado para usar Hermes como puente con Skills específicos como Supervisor y Hermes Bridge.

[01:37:00] Juan Carlos — Si se acaban los tokens de Cloud, ¿puedo seguir con modelos de Cloud vía opencode? Solución: Sí, usando DeepCloud, que modifica el archivo de configuración para redirigir las peticiones de Cloud Code hacia los servidores de opencode. Leandro lo usa con DeepSeek V4 Pro dentro de Cloud Code + Forge.

[01:38:30] Mateo — ¿Hay video sobre cómo armar un orquestador de punta a punta? Solución: No existe aún, está pendiente como contenido. Recomendación: empezar con un buen arnés, entender Harness Engineering, crear Skills propios e investigar MCPs/CLIs según el dominio (no es lo mismo orquestar marketing que desarrollo de software).

[01:41:15] Arturo — ¿Forge sirve como orquestador? Solución: Sí, Forge es un orquestador que vive dentro de Cloud Code, con sub-agentes especializados en Frontend, Backend, Seguridad y Deploy. Desde la semana pasada es multi-CLI: funciona con opencode, Gemini, Cursor y Codex.

[01:42:30] Carlos — Cierre Reitera la importancia de dominar los arneses, crear los propios y no depender de un solo proveedor. Si Anthropic cambia límites o precios, quienes tengan su negocio basado en un solo arnés con un solo modelo se verán afectados.  
  
  
**Resumen: **  
Esta sesión de Vibecoding se centró en explicar el concepto de arnés en el ámbito de la inteligencia artificial, donde Carlos ofreció una explicación detallada sobre cómo los arnés actúan como la infraestructura que permite a los modelos lingüísticos (LLMs) realizar tareas del mundo real más allá de ser meros chatbots.   
La presentación abarcó los cinco componentes clave del entorno: BASH (comandos), Sistema de Archivos (lectura/escritura de archivos), Sandbox (entorno seguro), Legend Loop (ciclo de lectura-acción-verificación) y Habilidades/MCPs (extensibilidad).   
Carlos mostró cómo conectar Hermes con Cloud Code utilizando distintos protocolos, entre ellos Print Mount y TMUX como alternativas al ACAP (que actualmente no está disponible en Hermes). 

Durante la sesión también se abordaron temas prácticos como la configuración del entorno de desarrollo integrado (IDE) de AntiGravity, el uso de tokens en distintos modelos y la implementación de SDKs como los de N8N. Los asistentes plantearon preguntas sobre optimización de costos, seguridad de datos y creación de orquestadores personalizados, a las que Carlos respondió ofreciendo recomendaciones y ejemplos prácticos.
