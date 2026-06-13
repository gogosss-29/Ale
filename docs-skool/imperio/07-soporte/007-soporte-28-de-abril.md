# Soporte - 28 de Abril

> Ruta: 🛠️ Soporte › Soporte - 28 de Abril

**🎬 Vídeo (63.5 min):** https://www.youtube.com/watch?v=xATpuRWwHMw

---

**Problemas que resuelve esta sesión:** Cómo integrar sistemas de agendamiento cerrados sin API, cómo armar automatizaciones robustas con agentes en lugar de flujos rígidos, cómo gestionar credenciales con clientes desconfiados, cuándo usar Obsidian vs. base de datos estructurada para análisis clínico, cómo evitar reanalizar datos completos en cada corrida (token hashing y timestamps), cómo agendar con Gmail como gatillo y cuándo conviene mantener un sistema que ya funciona.

---

**Intervenciones**

**[00:04] Franco – Apertura y mecánica de la sesión** Contextualiza la dinámica: levantamiento de mano, fila ordenada, espacio abierto para dudas, obstáculos y opiniones.

**[01:37] Participante (Juaco) – Integración con sistema de agendamiento médico cerrado** Ayuda a su hermana con chatbots para clientes. Un médico usa un sistema de agendamiento clínico sin API disponible. Solución: (1) Contactar soporte del sistema para buscar integraciones no documentadas. (2) Evaluar fricción de migrar a sistema nuevo. (3) Si todo falla, usar Claude Code + Playwright o Chrome DevTools para analizar el HTML interno, detectar APIs internas y automatizar el acceso. El captcha no es impedimento: Playwright lo resuelve. Alternativa: armar un actor en Apify para dejar el proceso en la nube.

**[08:31] Pablo – Workflow de facturación automatizada por Telegram/Gmail** Empresa que distribuye productos del Reino Unido necesita generar facturas personalizadas según tipo de cliente (hotel o retail) con distintos precios y plantillas. Tiene un flujo parcial en N8N. Solución: El flujo actual extrae información pero no es suficientemente robusto. Hay que convertirlo en un agente de IA con herramientas: una para obtener clientes, otra para obtener productos (dos tablas separadas). El agente debe poder hacer preguntas si faltan datos, no solo extraer y generar. Se muestra en vivo la diferencia entre un nodo de extracción y un agente completo con memoria y herramientas.

**[20:00] Pablo – Cómo manejar clientes que no quieren dar credenciales** Preocupación al vender automatizaciones: el cliente no quiere compartir contraseñas. Solución: Sin credenciales no hay integración posible. Opciones: tokens de acceso limitado (lectura), acuerdo de confidencialidad firmado antes de empezar, o flujo OAuth para que el cliente autorice sin compartir contraseña (aplica para Google). La realidad es que en la práctica no suele ser el problema más frecuente — cuando aparece, se negocia caso a caso.

**[24:06] Participante (VS Code) – Claude Code como alternativa a N8N para el caso de Pablo** Pregunta si Claude Code no sería más directo que N8N para este tipo de sistema. Respuesta: Depende del stack de cada uno. CMA (Claude Multi-Agent o MAS), Claude Code, N8N o Supabase son opciones válidas. La simplicidad está en dónde tenés más experiencia acumulada.

**[36:45] Juan Felipe – Análisis de historias clínicas odontológicas para campañas de marketing** 1.000+ historias clínicas con notas clínicas (por ejemplo: "se sugiere ortodoncia"). Sistema cerrado sin API. Quiere filtrar pacientes por tratamientos sugeridos para campañas segmentadas. Consideró Obsidian. Solución: Obsidian sirve para conectar conceptos relacionados (wiki), no para análisis de registros separados. Lo óptimo es: (1) pasar cada historia clínica a una fila de Excel/Supabase con columnas por categorías clave, (2) usar IA para leer cada historial y completar los campos, (3) después consultar o armar dashboard con ese dataset estructurado. Un paciente no tiene relación con otro — son registros independientes, no nodos de un grafo.

**[48:04] Carlos – Sistema de verificación por hash para evitar reanalizar todo en cada corrida** Al tener historias clínicas que se actualizan constantemente, releer todo siempre es ineficiente y costoso en tokens. Solución: Agregar un campo de hash (tipo SHA-256) que se genera cada vez que hay un cambio en el historial. Antes de cada corrida, el agente compara el hash actual con el guardado. Si son iguales, lo omite. Si difieren, lo procesa. Esto reduce drásticamente el consumo de tokens.

**[1:01:13] Daniel – Alternativa más simple: timestamp de última modificación** Complementa la solución de Carlos. En lugar de comparar hashes registro por registro, agregar un campo `fecha_modificacion` a la base de datos. En cada corrida, el agente filtra solo los registros actualizados desde la última ejecución. Más directo, más barato, sin recorrer todos los registros.

**[50:04] Alma – Sistema de agendamiento con Gmail como gatillo + historias clínicas en Drive** Usa Doctoralia + Google Calendar + Gmail. El mail nuevo es el trigger de sus automatizaciones. Tiene historias clínicas en Drive con sistema de doble cuenta para proteger datos (una cuenta con datos, otra con nombres). Respuesta: Si la conexión de Gmail ya está funcionando, no hay razón para cambiarla — es un traje a medida para su negocio, más útil que una solución enlatada. Todo lo que esté en Google Drive es accesible desde cualquier cuenta con credenciales. Se agenda mostrar el sistema en detalle el martes siguiente.

**[57:58] Glenda – Permiso "skip permissions" en Claude Code (VS Code)** No le aparece la opción para evitar confirmaciones manuales en cada acción de Claude Code. Solución: Ir a extensión de Claude → Settings → marcar la opción correspondiente en User Settings (no Workspace). Una vez activada, no requiere ninguna confirmación adicional.

**[1:03:00] Franco – Cierre** Sesión variada. Próximas sesiones: mañana coding, martes siguiente soporte general. Invita a continuar el trabajo.
