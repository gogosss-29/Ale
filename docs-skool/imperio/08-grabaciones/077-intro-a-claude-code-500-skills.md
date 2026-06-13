# Intro a Claude Code + 500 skills

> Ruta: 🔴 Grabaciones › Intro a Claude Code + 500 skills

---

**Problemas que resuelve:** Qué es Claude Code y cómo diferenciarlo de Claude Chat y Cowork, cómo estructurar proyectos con archivos [Claude.md](http://Claude.md) y Skills para mantener contexto sin perder tokens, cómo levantar páginas web y aplicaciones sin saber programar, y cuándo usar Claude Code vs OpenClaude vs Cursor según el objetivo.

---

**Intervenciones**

**[****00:00****] Benja – Introducción y mito del "code"** Rompe el mito de que Claude Code es solo para programadores. Explica que cualquier persona puede usarlo hablando en español, y que el nombre "Code" genera una barrera mental innecesaria. Presenta el índice de la sesión: qué es Anthropic, qué modelos existen, las 3 herramientas (Chat, Cowork, Claude Code) y cómo funcionan en la práctica.

---

**[~****05:00****] Benja – Los 3 modelos y las 3 herramientas** Explica los modelos Haiku, Sonnet y Opus. Para uso cotidiano: Sonnet. Para tareas complejas con razonamiento profundo: Opus. Describe las 3 herramientas disponibles en la app de Claude: Chat (con conectores MCP), Cowork (acceso a carpetas del computador, ideal para el 90% de los casos de automatización empresarial) y Claude Code (ejecución de código a nivel de terminal, más potente pero más técnico).

---

**[~****10:00****] Benja – IDEs: VS Code y Windsurf (Antigravity)** Explica que Claude Code se corre dentro de un IDE como VS Code o Windsurf, no de forma aislada. Windsurf es un fork de VS Code con pequeñas modificaciones. Aclara la confusión frecuente: no se "usa Windsurf o se usa Claude Code", sino que Claude Code corre dentro del IDE. Muestra cómo instalar la extensión de Claude Code en VS Code.

---

**[****12:55****] Max – Claude Code en VPS** Pregunta si tiene sentido instalar VS Code dentro de un VPS. Respuesta: no es necesario porque en el VPS se puede correr desde terminal. VS Code es solo una interfaz visual para quienes trabajan en su computador local. Joaco añade que existe una forma de conectar VS Code remotamente al VPS, tema tratado en la sesión del miércoles anterior.

---

**[~****18:00****] Benja – Demo en vivo: página web desde cero** Con un prompt de voz de 30 segundos, Claude Code crea una landing page completa para "Malik Studios", una agencia de recepcionistas virtuales para clínicas estéticas y dentales. Muestra el proceso de razonamiento del modelo, la creación de archivos HTML en la carpeta asignada y la visualización en el navegador. Demuestra cómo ajustar colores y estilos con prompts simples.

---

**[~****30:00****] Benja – Modos de trabajo y configuración de permisos** Explica los 4 modos disponibles: preguntar antes de cada cambio, edición automática, modo planificación (solo pensar, no ejecutar) y "bypass permissions" (mayor autonomía). Muestra cómo activar la opción de saltar permisos en la configuración para no estar aprobando cada paso. Recomienda arrancar simple antes de planificar en exceso.

---

**[~****36:00****] Benja – El archivo **[**Claude.md**](http://Claude.md) Explica que [Claude.md](http://Claude.md) es el equivalente al system prompt de los GPTs: un archivo Markdown que se antepone automáticamente a cada interacción y mantiene el contexto del proyecto sin perderse aunque la ventana de contexto se comprima. Buena práctica: mantenerlo bajo 200 líneas para no consumir tokens innecesarios.

---

**[~****41:00****] Benja – Skills: superpoderes del agente** Introduce los Skills como archivos Markdown con buenas prácticas especializadas que alimentan el contexto del modelo. Muestra Skills de N8N, Facebook Ads, humanizador web, y otros. Explica que se pueden usar tanto en Claude Code como en Claude Chat (subiéndolos en la sección de Habilidades). Anuncia el lanzamiento de más de 500 Skills dentro de la comunidad, recopilados y organizados por el equipo.

---

**[~****50:00****] Benja – Cómo crear y personalizar Skills propios** Muestra cómo usar el Skill Creator para adaptar un Skill genérico al negocio propio. Conectar Skills con Notion vía MCP permite superar el límite de contexto para generar guiones largos, guías completas, etc. Menciona el concepto de "context engineering" como la habilidad clave actual, por encima del prompt engineering.

---

**[~****55:00****] Benja – Comandos avanzados: /compact, /loop y multitarea** Explica el comando /compact para comprimir contexto manualmente, y el comando /loop para que Claude Code se autoevalúe y repita un proceso hasta alcanzar un objetivo visual. Ejemplo: comparar la página generada con una referencia y seguir ajustando hasta que coincidan. También muestra cómo trabajar en múltiples sesiones de Claude Code en paralelo.

---

**[****01:06:08****] Gonzalo – Pregunta sobre conflicto entre Skills** Consulta si tener 2 Skills con funciones similares puede generar conflicto. Respuesta: Claude elige el Skill más adecuado según el contexto del prompt. Si hay ambigüedad, puede preguntar. Recomendación: simplificar y no duplicar; mantener el [Claude.md](http://Claude.md) como base siempre activa.

---

**[****01:10:36****] Óscar – Organización de carpetas y Skills** Pregunta cómo estructurar carpetas con contexto general, Skills y subagentes. Respuesta: depende del uso. Para un proyecto puntual, una sola carpeta. Para un agente complejo, subcarpetas por proyecto con archivos [agents.md](http://agents.md), rules, etc. Claude Code escanea la estructura con /init para entender el entorno antes de ejecutar.

---

**[****01:12:49****] Daniel – Claude Code vs OpenClaude vs Cursor** Pregunta cuál elegir para meterse de fondo. Respuesta: Cursor funciona igual como IDE. OpenClaude es ideal como asistente personal 24/7 corriendo en un Mac Mini o VPS, conectado a herramientas como Meta, calendario, correo. Claude Code es mejor para proyectos aislados con contextos separados. Un cliente paga 2.000 USD/mes por tener OpenClaude integrado en su flujo de marketing.

---

**[****01:17:46****] Leandro – Pedido de onboarding gradual ante la avalancha de información** Comenta que el ritmo de novedades (OpenClaude, Claude Code, 500 Skills) genera sobrecarga cognitiva y pide que se armen "paquetitos" de aprendizaje progresivo. Benja reconoce que el panorama cambió radicalmente en enero-febrero, que el onboarding anterior quedó desactualizado y que están trabajando en una nueva sección de inicio estructurada.

---

**[****01:21:27****] Yobanis – Seguridad al usar Claude Code en el computador principal** Pregunta sobre riesgos de seguridad al usar Claude Code con datos de RRHH. Respuesta: Claude Code es más seguro que OpenClaude porque tiene guardarrails nativos y solo accede a las carpetas que uno le asigna explícitamente. OpenClaude tiene más autonomía y por eso más riesgo si no se configura bien. Recomendación: ir de menos a más en los accesos y empezar en un entorno acotado.

---

**[****01:26:36****] Cierre – Joaco** Recuerda que en la sesión del miércoles anterior se profundizó en las diferencias entre Claude Code y OpenClaude, e invita a ver esa grabación. Anuncia la próxima sesión de ByteCoding el miércoles siguiente.
