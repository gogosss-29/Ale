# Claude Code + N8N : Kit, MCP y Skills desde 0

> Ruta: Vibe-Coding › Claude Code + N8N : Kit, MCP y Skills desde 0

**📎 Recursos:**
- [Recurso de la Clase](https://github.com/Carlos-Dominguez-faber/n8n-automation-kit)

---

**Problemas que resuelve la sesión del 29 de Abril:** Cómo integrar Claude Code con N8N usando MCP para automatizar flujos sin escribir código, cómo migrar automatizaciones de Make a N8N con IA, y cómo estructurar un kit de proyecto reutilizable con Skills, agentes especializados y memoria persistente.

---

**Intervenciones**

**[00:00] Joaco – Bienvenida y contexto de la sesión** Presenta la sesión de Bytecoding con Carlos. Aclara que no existe un único flujo de trabajo en el desarrollo agéntico y que la sesión documentará el workflow que Carlos usa como programador con experiencia previa a la IA.

**[02:00] Carlos – Demostración de resultados: flujo de creación de Reels automatizados** Muestra en vivo un flujo completo construido con Claude Code y N8N que genera Reels desde cero: guión, imagen de referencia con GPT Image, clips con Sora/Kling, voz clonada con ElevenLabs, merge de video y audio con FFmpeg en VPS, subtítulos estilo Hormozi y watermark. Todo construido de forma autónoma por Claude Code. Costo estimado: ~$1.50 por video, ~$130/mes por 60 creativos.

**[11:50] Carlos – Presentación del N8N Automation Kit** Comparte el repositorio público con todo lo necesario para integrar Claude Code con N8N: MCPs configurados para N8N, Playwright y Coolify, Skills especializadas (incluyendo una propia), [CLAUDE.md](http://CLAUDE.md) tipo cuestionario, [MEMORY.md](http://MEMORY.md) con aprendizaje acumulativo, agentes especializados y configuración de sesión de Chrome para doble validación visual.

**[17:00] Carlos – Instalación desde cero del kit** Muestra el proceso completo: clonar el repositorio, copiar las Skills al nivel de usuario o de proyecto (con explicación de cuándo conviene cada uno), configurar el MCP.json con credenciales reales de N8N, Coolify y Playwright. Recomendación clave: no instalar cientos de Skills a nivel global porque consumen input context en cada sesión.

**[24:00] Joaco y Carlos – Skills a nivel usuario vs. nivel proyecto** Discusión sobre cuándo conviene cada enfoque. Las Skills muy específicas de N8N convienen a nivel proyecto si no se usa N8N en todo el trabajo. Las Skills de uso general o de múltiples clientes convienen a nivel usuario.

**[28:00] Carlos – Workflow determinístico vs. no determinístico con IA** Explica qué tipo de flujos puede construir bien Claude Code con N8N y cuáles no. Recomendación: usar este sistema para flujos de lógica cerrada (si pasa esto, haz esto). Para nodos de agente, tools y prompts complejos, es mejor que el humano orqueste y Claude Code ejecute partes específicas.

**[35:00] Carlos – Descarga de workflows existentes desde N8N vía MCP** Muestra cómo pedirle a Claude Code que se conecte al N8N vía API, liste todos los workflows y los guarde como archivos JSON en el repositorio local. Esto le da contexto al agente sobre cómo trabaja el usuario y qué nodos utiliza.

**[43:00] Joaco y Carlos – Tip de ahorro de tokens: Rewind (Escape + Escape)** Explican el comando de rewind en Claude Code: si el agente comete un error, en lugar de acumular más mensajes de corrección (que aumentan el input context acumulado), se usa Escape dos veces para volver al mensaje anterior y reescribir la instrucción desde ese punto limpio.

**[50:00] Carlos – Conversión de flujo Make → N8N en vivo** Toma un blueprint JSON exportado desde Make (flujo de ebooks personalizados) y se lo pasa a Claude Code con el kit configurado. Claude Code analiza el flujo, lo mapea a N8N y lo construye de forma autónoma. El único nodo que requirió intervención fue el trigger de Google Sheets, que Claude corrigió vía Playwright abriendo el navegador y ajustando el nodo correcto.

**[01:05:00] Carlos – Uso de Playwright en modo visual y headless** Diferencia entre Playwright con navegador visible (para validación y corrección en vivo) y Playwright headless (para ejecución en VPS sin interfaz). Explica que es una herramienta open source de Microsoft y que Claude Code la usa para ver y operar N8N como si fuera un humano.

**[01:20:00] Carlos – Configuración del trigger de Google Sheets y cierre del flujo** Conecta credenciales de Google en N8N, ajusta el trigger correcto y deja el flujo listo para pruebas. Nota técnica: su N8N corre en modo Workers (modo cola), lo que genera un delay visible solo en entornos con múltiples clientes. Claude Code detecta el error de configuración vía MCP de Coolify y reinicia el servicio de forma autónoma.

**[01:35:00] Joaco y Carlos – Make vs. N8N: recomendación de la comunidad** N8N es casi gratuito (solo costo del VPS), tiene mejor integración con Claude Code y es más flexible que Make. La comunidad de Imperio Digital dejó de crear contenido de Make hace meses. Los blueprints de Make se pueden exportar como JSON y migrar a N8N directamente con este kit.

**[01:38:00] Carlos – Cómo vender automatizaciones en N8N** Dos modelos: (1) correr el flujo en el VPS de la agencia y darle al cliente solo el resultado final, (2) instalar todo en el VPS del cliente con documentación completa de credenciales y accesos, cobrando un fee mensual por mantenimiento, actualizaciones y corrección de errores.

**[01:42:00] Cierre** Carlos se compromete a subir el flujo de ebooks al repositorio. Joaco y Carlos resumen: el kit es reutilizable, el [MEMORY.md](http://MEMORY.md) va acumulando errores y patrones, y en el futuro se puede generar una Skill específica de migración Make → N8N para hacerlo cada vez más rápido y con menos errores.  


---

  
**Actualización post-sesión:** El flujo de ebooks personalizados que construimos en la sesión quedó 100% funcional después de la transmisión: desde el trigger en Webhook hasta la generación del PDF final, todo automatizado en N8N.

El repositorio N8N Automation Kit tiene todo lo que configuramos en clase: MCPs, Skills especializadas, el agente workflow-architect y plantillas listas para usar.   
Disponible en [github.com/Carlos-Dominguez-faber/n8n-automation-kit](http://github.com/Carlos-Dominguez-faber/n8n-automation-kit). Para quienes tengan problema clonando, hay un ZIP directo: lo descomprimen y abren Claude Code desde esa carpeta.

También se sumó una Skill nueva al repositorio: `make-to-n8n`, que mapea ~80 módulos de Make a sus equivalentes en N8N, convierte las expresiones `{{1.campo}}` a sintaxis N8N y guía todo el proceso de migración. Para instalarla: `cp -r skills/make-to-n8n ~/.claude/skills/`
