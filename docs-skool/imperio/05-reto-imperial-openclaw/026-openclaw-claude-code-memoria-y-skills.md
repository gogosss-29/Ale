# 🧠 OpenClaw + Claude Code: Memoria y Skills

> Ruta: 🦞 Reto Imperial OpenClaw › 🧠 OpenClaw + Claude Code: Memoria y Skills

---

**Problemas que resuelve la sesión del 25 de Marzo:** Cómo gestionar la memoria en agentes de OpenClaw y Claude Code sin perder contexto, cómo organizar proyectos y carpetas para trabajar con múltiples clientes en paralelo, y cómo configurar y optimizar Skills para reducir el consumo de tokens.

---

**Intervenciones**

**[****00:00****] Joaco & Benjamín – Bienvenida y lanzamiento del curso de Claude Code** Anuncian el lanzamiento de un curso completo de Claude Code de 3,5 horas, sin cortes, que cubre desde las bases hasta conceptos avanzados. Benjamín explica la diferencia entre Cowork y Claude Code y por qué el curso muestra también los errores del proceso.

**[****07:00****] Carlos – Presentación del proyecto comunitario: repositorio personal de conocimiento** Explica que el objetivo de las próximas sesiones es construir en vivo una Web App tipo "Mission Control" donde cada miembro pueda centralizar recursos, videos y documentación, chatear con esa información vía RAG, y acceder desde cualquier dispositivo. Se deployará en VPS propio sin Vercel.

**[****09:30****] Jorge – Memoria en OpenClow con carga alta de información** Consulta sobre cómo manejar la memoria cuando el agente acumula demasiado contexto y empieza a fallar o confundirse. **Solución:** Usar 3 niveles de memoria — memoria de sesión, memoria de proyecto y memoria general del usuario. En OpenClow, iniciar sesión nueva con `/new` borra la memoria de sesión. Instalar plugins de memoria como MEM (disponible en el marketplace de OpenClow) para persistencia estructurada.

**[****13:14****] Luis – Cómo correr OpenClow sin usarlo en la PC personal** Pregunta si se puede instalar en otro dispositivo o de forma online. **Solución:** Opciones disponibles: VPS (recomendado, desde ~$6-8/mes en Hostinger, mínimo 4GB RAM), Mac Mini local o configuración híbrida VPS + local. Para comunicarse con el agente, lo más sencillo es Telegram; luego Discord para mayor organización por canales y subagentes.

**[****22:39****] Yoany – Agente que olvidó su configuración de voz (ElevenLabs)** El agente dejó de responder con voz después de una semana funcionando bien. **Solución:** No pasar la API key por chat sino guardarla en un archivo de variables de entorno. Configurar la regla de respuesta (texto → texto, audio → audio) directamente en el archivo `soul.md` del agente, no solo en la conversación, para que se cargue en cada sesión via prompt caching.

**[****30:52****] Jorge Monterde – Organización de Claude Code para agencia con 3 personas en distintas ciudades** Consulta cómo estructurar Claude Code para trabajar de forma consistente entre múltiples personas y clientes. **Solución:** Usar una carpeta raíz de agencia con subcarpetas por cliente, cada una con su propio `CLAUDE.md`. Skills en dos niveles: a nivel organización (compartidos) y a nivel proyecto (por cliente). Para sincronización: carpetas en Google Drive o repositorios GitHub por proyecto. Obsidian como cerebro compartido entre agentes.

**[****44:38****] Daniel – Herramienta de memoria compartida: Engram** Comparte la herramienta Engram como alternativa para compartir memoria entre múltiples desarrolladores trabajando en el mismo proyecto, con búsqueda por palabras clave tipo RAG y sincronización vía repositorio.

**[****49:17****] Carlos – Demo en vivo: configuración del **`user.md` en OpenClow Muestra mediante SSH al VPS cómo se ve un archivo de configuración real, incluyendo la regla de respuesta audio/texto, para que quede persistente y no se pierda con el crecimiento del contexto.

**[****51:22****] Tomás – Cómo abrir múltiples proyectos en paralelo y recuperar sesiones** Consulta si puede abrir varios proyectos al mismo tiempo en VS Code y cómo retomar conversaciones anteriores. **Solución:** Abrir una ventana separada (anti gravity o terminal) por cada proyecto. No abrir múltiples carpetas en una sola instancia porque el agente pierde foco y consume más tokens. Para recuperar sesiones: usar el comando `claude continue`, renombrar sesiones por proyecto, y apoyarse en archivos `memory.md` o `state.md` para que el contexto sobreviva a la compactación.

**[****01:01:03****] Jorge Monterde – Longitud de Skills y consumo de tokens** Pregunta si la longitud de un Skill afecta el consumo de tokens. **Solución:** Sí, cada Skill invocado se suma al prompt caching junto al `CLAUDE.md`, historial y herramientas. Mantener Skills bien delimitados y concisos. Usar el Skill Creator de Claude Code para generar y auto-optimizar Skills mediante prueba y comparación de resultados.

**[****01:12:15****] Cierre** Carlos resume la importancia de una buena arquitectura de memoria y carpetas antes de escalar. Joaco invita a ver el nuevo curso y anuncia próximas sesiones de construcción en vivo del repositorio comunitario.
