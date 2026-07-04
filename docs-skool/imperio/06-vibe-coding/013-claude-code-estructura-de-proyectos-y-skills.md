# Claude Code: estructura de proyectos y skills

> Ruta: Vibe-Coding › Claude Code: estructura de proyectos y skills

**📎 Recursos:**
- Documentos de esta clase

---

**Problemas que resuelve la sesión del 18 de Marzo::** Cómo organizar carpetas y proyectos al trabajar con Claude Code, cómo entender las diferencias reales entre [Claude.ai](http://Claude.ai), Claude Cowork y Claude Code, y cómo usar herramientas como Skills, MCP, Remote Control y Aientation para desarrollar aplicaciones más rápido y con menos fricción.

---

**INTERVENCIONES**

**[****00:00****] Carlos – Estructura de carpetas recomendada para proyectos con Claude Code** Comparte su sistema de organización personal: una carpeta raíz `developer`, con subcarpetas `software` (proyectos activos), `tools` y `playground` (pruebas aisladas). Dentro de `software` vive la carpeta `templates`, que contiene MCPs, Skills, hooks y configuración de agentes preconfigurados. Con un solo comando inicializa cualquier proyecto nuevo clonando ese template. Regla práctica: sin mayúsculas ni espacios en nombres de carpetas, para evitar errores al ejecutar comandos en terminal.

**[****06:00****] Carlos – Diferencia entre **[**Claude.ai**](http://Claude.ai)**, Claude Cowork y Claude Code** Explica los tres productos del ecosistema Anthropic. [Claude.ai](http://Claude.ai) es la interfaz de chat web/móvil para preguntas, investigación y documentos. Claude Cowork (solo disponible en app de escritorio, recién llegado a Windows) usa el mismo motor que Claude Code pero sin terminal, permite interactuar con la computadora y crear archivos como presentaciones directamente. Claude Code es para codear, refactorizar y automatizar desde terminal o IDE. Importante: [Claude.ai](http://Claude.ai) y Cowork sí comparten contexto y Skills; Claude Code no.

**[****10:00****] Carlos – Remote Control: trabajar desde el celular mientras Claude Code corre en tu computadora** Muestra cómo activar Remote Control desde terminal con `/rc`, que crea un puente en la nube para ver y controlar en tiempo real lo que hace el agente desde el celular o el navegador. También presenta **Dispatch**, la nueva funcionalidad de Cowork para monitorear sesiones remotamente desde el celular.

**[****12:00****] Joaco – Pregunta de Sophie: cómo compartir contexto entre **[**Claude.ai**](http://Claude.ai)** y Claude Code** Carlos responde: lo ideal es chatear directamente desde Claude Code para mantener el contexto. Si se empieza en el celular, esas sesiones quedan guardadas en la nube y se pueden continuar desde el IDE. [Claude.ai](http://Claude.ai) y Claude Code no comparten memoria automáticamente.

**[****20:00****] Carlos – Cómo instalar una Skill en **[**Claude.ai**](http://Claude.ai)** y en Claude Code** Demuestra en vivo cómo tomar un archivo `.md` de Skill (en este caso, humanizador web), arrastrarlo al chat de [Claude.ai](http://Claude.ai) y pedirle que la instale. Claude genera la estructura de carpeta correcta y agrega un botón para copiarla a las habilidades del usuario. Diferencia clave: las Skills instaladas en [Claude.ai](http://Claude.ai) están disponibles también en Cowork, pero no en Claude Code; para ese caso hay que instalarlas directamente en el proyecto.

**[****26:00****] Carlos – Cómo usar la Skill en Claude Code dentro de un proyecto** Muestra cómo pasar el archivo `.md` directamente al agente en Claude Code con la instrucción de instalarlo solo para ese proyecto. Claude crea la carpeta oculta `.claude` con la Skill dentro. Las carpetas ocultas (que empiezan con punto) no son visibles por defecto; en Mac se accede con `Cmd + Shift + .`.

**[****36:00****] Carlos – Aientation: dar feedback visual exacto sin capturas de pantalla** Presenta la herramienta Aientation, que al activarse en el navegador permite seleccionar elementos específicos de la interfaz y escribir instrucciones sobre cada uno. Al finalizar, se copia todo el feedback estructurado y se pega en Claude Code. El agente recibe la posición, el viewport y el contexto exacto del elemento sin necesidad de interpretar imágenes. Se comparte el post de configuración en la comunidad.

**[****40:00****] Carlos – Playwright MCP: ver el resultado visual desde el agente** Demuestra cómo, teniendo el MCP de Playwright configurado, Claude puede abrir el navegador de forma autónoma y revisar el resultado visual del código generado. Útil para feedback de UI sin capturas de pantalla.

**[****50:00****] Carlos – Comando de inicialización de proyectos: el "template clone" personalizado** Muestra en vivo el comando que configuró para inicializar cualquier proyecto nuevo: en segundos copia todos los MCPs, Skills, hooks, agentes y componentes desde su template al nuevo directorio. Con un segundo comando (`/onboard`), el agente hace preguntas para entender qué se va a construir y guía el desarrollo desde cero. Otros comandos incluidos: ROI, copyright, landing page, lanzamiento y validación de mercado.

**[****54:00****] Daniel – Qué es el Viewport y por qué importa al desarrollar** Explica que el viewport es el tamaño visible de la pantalla según el dispositivo. Tip clave: siempre diseñar **mobile first**, es decir, empezar por el teléfono y escalar hacia tableta y escritorio. Es más fácil expandir que comprimir. Carlos agrega que el 95% del tráfico web viene del celular, por lo que esta práctica no es opcional.

**[****59:30****] Cierre – Joaco y Carlos** Se comparte el JSON de configuración del MCP de Chrome DevTools y el instructivo de Agentation en el chat. Se anuncia continuidad de sesiones: jueves para bienvenida a nuevos miembros, viernes con Franco.
