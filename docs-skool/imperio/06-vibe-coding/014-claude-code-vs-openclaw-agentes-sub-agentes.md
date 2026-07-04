# Claude Code vs OpenClaw: Agentes, Sub-agentes.

> Ruta: Vibe-Coding › Claude Code vs OpenClaw: Agentes, Sub-agentes.

---

**Problemas que resuelve la sesión del 11 de Marzo:** Cómo entender la diferencia entre agentes de Claude Code y agentes de OpenClaw, cómo crear y configurar agentes especializados dentro de Claude Code, y cómo conectarse remotamente a un VPS para gestionar OpenClaw desde un editor visual.

---

**Intervenciones**

**[****00:00****] Joaco y Carlos – Votación y definición del tema de sesión** Se presentan tres opciones a la comunidad: profundizar en Claude Code, construir una app en vivo desde cero, o explorar OpenClaw. Tras dos rondas de votación, se elige OpenClaw con arquitectura de agentes como tema central.

**[****08:12****] Joaco – Casos de uso personales de OpenClaw** Comparte cómo usa 5 subagentes: uno orquestador y cuatro especializados en contenido, desarrollo web, seguimiento a clientes y creación de scripts. Todo se centraliza en Notion. Diferencia entre la proactividad de OpenClaw frente a las automatizaciones programadas con cron jobs.

**[****16:02****] Carlos – Diferencia entre agentes de Claude Code y agentes de OpenClaw** Explica que los agentes de Claude Code viven dentro del entorno de Claude Code, pueden configurarse con modelos específicos (Haiku, Sonnet, Opus) y se invocan dentro de sesiones de Claude Code. Los agentes de OpenClaw viven en el VPS donde se instalan. La lógica de orquestación es similar: siempre se habla con el agente principal, que delega a los subagentes.

**[****18:40****] Carlos – Demostración en vivo: creación de un agente en Claude Code** Muestra paso a paso cómo crear un agente especializado en SEO y copywriting: nombre, herramientas disponibles, modelo recomendado (Sonnet), memoria a nivel proyecto, y cómo el agente orquestador lo invoca automáticamente según el contexto de la conversación.

**[****26:10****] Jorge – Preguntas sobre orquestación y creación de subagentes** Consulta cómo el agente principal sabe a quién llamar y si los subagentes se crean igual que el principal. Solución: el proceso de creación es idéntico. El agente principal delega en base a las instrucciones configuradas. El usuario nunca habla directamente con los subagentes.

**[****29:45****] Sofía – De dónde saca conocimiento un agente especializado** Pregunta cómo un agente sabe de un tema si solo se le da un nombre genérico. Solución: hay que alimentarlo con archivos, documentación, investigación e instrucciones específicas. La creación en vivo fue solo demostrativa; en la práctica requiere mucho más contexto.

**[****35:28****] Joaco y Carlos – Conexión remota al VPS desde Antigravity o VS Code** Muestran cómo instalar la extensión Remote SSH de Microsoft en Antigravity para conectarse directamente al VPS y editar los archivos de configuración de OpenClaw de forma visual, sin usar la terminal manualmente. Esto elimina la fricción de copiar y pegar comandos.

**[****40:39****] Carmina – ¿Claude Code ve lo que hago en mi computadora?** Consulta si los agentes actúan de forma autónoma mientras trabaja normalmente. Solución: Claude Code no monitorea el sistema operativo. Vive dentro de una carpeta específica. Para control del navegador o escritorio se requieren MCPs adicionales como Playwright. Demostración en vivo con apertura y navegación de una landing page.

**[****53:51****] Jorge – Cómo desinstalar OpenClaw limpiamente** Tiene el VPS compartido con otros scripts y quiere borrar OpenClaw sin afectar el resto. Solución: borrar la carpeta `opencloud` (no solo `.opencloud`). Si el usuario es compartido, hacer auditoría primero. Carlos demuestra cómo pedirle al propio agente que analice las carpetas y guíe el proceso de desinstalación usando el comando oficial de OpenClaw.

**[****01:00:19****] Sofía – Avance de Tipty Books y problema con LoRAs** Comparte que la app está funcional pero el front necesita trabajo. Tiene dos LoRAs entrenados (estilo y personaje) pero no logra combinarlos bien en la generación de imágenes. Solución de Carlos: no intentar fusionar imágenes con IA. Generar el fondo y el personaje por separado (personaje como PNG sin fondo) y usar código para superponer imágenes con coordenadas de posición. Así se evita que el modelo alucine y mezcle estilos.

**[****01:02:57****] Cierre** Joaco despide la sesión invitando a seguir participando en las sesiones semanales de vibecoding.
