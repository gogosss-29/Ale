# Vibe Coding: Anti Gravity, Claude Code y OpenClaw

> Ruta: Vibe-Coding › Vibe Coding: Anti Gravity, Claude Code y OpenClaw

---

**Problemas que resuelve la sesión del 4 de Marzo:** Cómo arrancar con vibe coding sin saber programar, cómo elegir y gestionar agentes dentro de entornos de desarrollo como Anti Gravity o Visual Studio Code, y cómo usar Skills para no perder contexto entre sesiones y proyectos.  


---

**[****00:00****] Joaco & Carlos – Qué es el Vibe Coding y por dónde empezar** Carlos explica el concepto de vibe coding: crear aplicaciones con lenguaje natural, sin escribir una sola línea de código.   
Más de 10 apps desarrolladas con este método sin tocar el código directamente. Se recomienda el curso de Anti Gravity en el classroom como punto de entrada, junto con nociones básicas de Github y deploy local.

**[****10:00****] Joaco & Carlos – Anti Gravity, Visual Studio Code y los agentes integrados**   
Se explica que Anti Gravity es un fork de VS Code creado por Google.   
La gran diferencia frente al flujo tradicional es que los agentes viven dentro del entorno, ven el directorio completo, escriben el código y corrigen errores sin que el usuario tenga que ir y venir entre herramientas. También se muestra la extensión Kilo, que permite usar modelos de OpenAI (Codex) dentro de Anti Gravity.

**[****21:00****] Jorge – Duda: ¿Es lo mismo usar Cloud Code en VS Code que en Anti Gravity?**   
La funcionalidad de Cloud Code es idéntica en ambos entornos.   
La ventaja de Anti Gravity es poder tener agentes adicionales (Gemini, Kilo) que revisen o auditen lo que hizo Cloud Code. Las conversaciones entre agentes no se comparten automáticamente; se requiere exportar contexto en archivos Markdown para que otro agente lo lea.

**[****28:00****] Carlos & Daniel – Qué son los Skills y cómo crearlos**   
Un Skill es un archivo Markdown con instrucciones paso a paso que le dice al agente cómo ejecutar una tarea específica.   
Se pueden crear desde cero con Skill Creator, adaptarse de repositorios públicos o construirse a partir de investigaciones con Perplexity.   
Existen tres niveles de alcance: proyecto, usuario y organización. Recomendación: no tener más de 70-80 Skills activos simultáneamente para no sobrecargar el contexto del modelo.

**[****36:00****] Tomás – ¿Dónde buscar Skills de terceros y cómo validarlas?**   
Se recomiendan repositorios en Github y páginas especializadas.   
Buena práctica: pasarle la URL del repositorio al agente antes de instalar, pedirle que analice el contenido y detecte vulnerabilidades.   
Instalar primero a nivel proyecto en carpeta aislada; si funciona bien, mover a nivel usuario.

**[****44:00****] Daniel – Filosofía práctica: crear Skills propias antes de buscar las de otros** Recomendación de construir Skills simples y propias desde el inicio, e ir iterando.   
Se puede conversar con el agente usando la opción "Ask" antes de pedirle que ejecute, para refinar el plan. La calidad del input determina la calidad del output.

**[****51:00****] Carlos – Demostración: cómo creó su Skill de PDR con **[**Claude.ai**](http://Claude.ai) Muestra en vivo la conversación donde construyó un Skill completo usando documentos de investigación y otros Skills como insumo.   
Todo generado por el agente; el usuario solo guía la conversación. Versiones guardadas como V1, V2 para poder revertir si una iteración rompe el resultado.

**[****53:00****] Joaco – Spoiler: bundle de Skills de la comunidad** Se anuncia que próximamente se pondrán a disposición Skills curadas para los miembros de la comunidad.

**[****54:00****] Ronda Open Klow – Dificultades y experiencias reales** Jorge comparte que al cambiar de modelo a mitad del proceso, el agente tocó el archivo de configuración JSON y rompió la instalación. Carlos muestra cómo cambiar modelos de forma segura desde Telegram con el comando `/models`, sin que el agente edite código. Se mencionan modelos alternativos más económicos como Minimax M2.5 y opciones con suscripción de ChatGPT Plus.

**[****01:05:00****] Daniel – Advertencia de seguridad y experiencia con tecnologías nuevas** Con años de experiencia en implementación tecnológica, Daniel recomienda cautela: el agente puede borrar archivos sin que el usuario lo note. Preferible dejar que otros pasen las primeras etapas de estabilización antes de implementar en producción.

**[****01:07:00****] Joaco – Buenas prácticas de seguridad con Open Klow** Relato de instalación en VPS aislado, sin acceso a archivos sensibles, con usuario sin permisos de root. Los tokens de conexión se configuran directamente en el archivo JSON desde el IDE, sin pasarlos por el chat del agente. Uso de Notion con permisos solo de lectura para información de contexto.

**[****01:09:00****] Tomás – ¿Se puede migrar Cloud Code entre computadoras?** Las sesiones de Cloud Code a nivel terminal viven en el equipo local. La solución es mantener archivos de documentación dentro del proyecto ([Claude.md](http://Claude.md), [Agents.md](http://Agents.md)) donde el agente registra decisiones y errores resueltos. También se menciona Remote Control como opción para continuar una sesión desde el celular.

**[****01:13:00****] Cierre** Carlos invita a dejar feedback en la comunidad sobre el nivel técnico esperado para calibrar las próximas sesiones. Se confirma continuidad del espacio cada miércoles.
