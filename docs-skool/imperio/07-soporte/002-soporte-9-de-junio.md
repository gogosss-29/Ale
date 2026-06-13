# Soporte - 9 de Junio

> Ruta: 🛠️ Soporte › Soporte - 9 de Junio

**🎬 Vídeo (77.9 min):** https://www.youtube.com/watch?v=eThMCKgIVh4

---

**Problemas que resuelve la sesión 9 de junio:** Cómo estructurar proyectos en Claude Code con [CLAUDE.md](http://CLAUDE.md), [memory.md](http://memory.md) y carpetas por cliente. Cómo dinamizar prompts de agentes IA para que diferentes clientes puedan editar su propia información sin tocar el flujo. Cómo estandarizar entregas de agentes WhatsApp a escala. Cómo decidir si usar Hermes o una arquitectura de agentes más escalable según el modelo de negocio. Cómo conectar aplicaciones con API en lugar de construir un MCP innecesario. Cómo limpiar y organizar bases de datos de clientes con Cowork o Excel.

---

## Intervenciones

**[00:00] Franco – Apertura y espacio de soporte** Contextualiza la sesión para nuevos miembros. Explica que este es el espacio para traer dudas específicas sobre proyectos en desarrollo, obstáculos técnicos o ideas sin dirección clara. Recuerda levantar la mano para hacer fila.

---

**[01:42] Jaime – Claude Code + WordPress + WooCommerce** Está construyendo webs rápidas con Claude Code y quiere integrarlas en WordPress con WooCommerce. Generó el HTML pero no sabe cómo pasarlo correctamente a WordPress/Elementor.

Solución: WordPress puede importar el código; recomienda hablar con Henry Infante en la comunidad, que domina ese flujo. Para futuros proyectos, no poner el manual de marca dentro del [CLAUDE.md](http://CLAUDE.md) sino en una carpeta separada accesible desde el proyecto.

---

**[06:50] Andrés – Hermes + CRM con agentes por dependencias** Está diseñando un ERP/CRM con agentes que aprenden los procesos de cada empresa, se conectan a sus fuentes de datos y se adaptan a medida que la operación cambia. Pensó en Hermes por su capacidad de retroalimentación continua.

Solución: Hermes no es escalable para un modelo de agencia uno-a-muchos. Cada instalación requiere credenciales, servidores y configuración propia. Alternativa recomendada: arquitectura con agents-as-code o sistemas similares, donde las variaciones entre cliente y cliente (acceso a Drive, AirTable, etc.) se manejan por autenticación diferenciada. Recomendación clave: antes de elegir tecnología, priorizar product-market fit y conseguir clientes reales que guíen las decisiones técnicas.

---

**[13:00] Tomás – Dinamizar prompt de agente para que el cliente lo edite** Tiene un agente de WhatsApp + WooCommerce funcionando para un cliente (confirmó que el cambio de modelo a Haiku mejoró drásticamente la calidad). Ahora quiere que el cliente pueda editar cierta información del prompt (promociones, productos, contexto) sin necesitar su intervención.

Solución: dinamizar el prompt usando expresiones en N8N que apunten a variables almacenadas en AirTable (o cualquier base de datos). El cliente edita sus campos directamente en AirTable y eso llega al agente en tiempo real. Franco muestra su implementación en vivo: una sección de "data collection" previa al agente que obtiene toda la información del cliente desde tablas diferenciadas. Para estandarizar el proceso entre clientes: recomendación de esperar a tener al menos 10 clientes similares antes de armar un sistema de templates; si se hace antes, es más un problema que una ventaja.

---

**[35:35] María José – Estructura de proyectos en Claude Code + entregables + integración con Agenda Pro** Ingeniera comercial desarrollando un sistema de gestión para una clínica dental (procesos operativos, costos, inventario, seguimiento comercial). Pregunta sobre estructura de proyectos, cuántos [CLAUDE.md](http://CLAUDE.md) usar, cómo manejar manuales de marca, si las skills de [Claude.ai](http://Claude.ai) se comparten con VS Code, y cómo entregar el sistema al cliente.

Solución: un [CLAUDE.md](http://CLAUDE.md) por proyecto (más un [CLAUDE.md](http://CLAUDE.md) global de usuario). El manual de marca conviene generarlo desde Claude Design como archivo de código, no como PDF. Las skills cargadas en la app de [Claude.ai](http://Claude.ai) no se comparten con VS Code: hay que cargarlas directamente desde el editor. Para conectar con Agenda Pro: tiene API disponible, no hace falta crear un MCP, simplemente pasarle la documentación a Claude y que genere las integraciones. Para la base de datos de 3.500 pacientes en Excel: Cowork puede limpiarla y organizarla directamente.

---

**[48:06] Gerardo – Cómo arrancar con Claude Code para desarrollar una extensión de browser** Hizo el roadmap, el MVP scope y el mapeo del flujo de datos con ayuda de IA. Acaba de desbloquear la cuenta de Claude y quiere saber cómo configurar bien el entorno antes de arrancar.

Solución: instalar según el video de 3 horas de la comunidad, arrancar con Opus en modo planificación, pasar a Sonnet en ejecución. No es necesario configurar memorias desde el inicio: después de tener algo de conversación y archivos, ejecutar `/init` para que Claude genere un [CLAUDE.md](http://CLAUDE.md) automático con lo acumulado. Plan Pro de $20 necesario para usar Claude Code.

---

**[54:08] Pablo – Hermes multiusuario en Telegram y Slack** Tiene un sistema de multiagentes con Hermes conectado a Telegram y Slack. El agente le responde a él, pero no a otros usuarios, aunque les dio acceso y configuró los permisos.

Solución (por Carlos): el problema son los **bindings** de Hermes. Por defecto, al configurar el canal inicial, Hermes queda vinculado solo a ese canal y ese ID. Para que responda a más personas: o se agregan manualmente los user IDs en la configuración de bindings, o se deshabilita el binding completamente para que responda a todos. En Discord específicamente, desactivar el binding también requiere deshabilitar threads. Depende de la plataforma si necesita o no que el bot sea invitado ("robado").

---

**[58:01] Euclides – Modelo de cobro para automatizaciones + migración a WhatsApp Cloud** Pregunta cómo estructurar el cobro cuando entrega una automatización a un cliente. También hizo una integración directa con la API de Facebook (sin WhiteCloud) y quiere saber si vale la pena migrar.

Solución: modelo recomendado = setup único (costo de desarrollo) + mensualidad por servicio continuo (mantenimiento, mejoras, integración progresiva al negocio del cliente). Para WhatsApp: migrar a WhiteCloud para nuevos clientes evita los dolores de cabeza de la integración directa con Meta. La funcionalidad es equivalente pero la conexión es mucho más simple y estable.

---

## Novedad de la sesión

**[16:09 / 1:02:54] Lanzamiento de Claude Fable 5** Benja informó en vivo el lanzamiento de Claude Fable 5, modelo de la familia Mythos que Anthropic describe como el más potente que han lanzado públicamente. Benchmarks: supera a Mythos Preview en agentic coding (80 vs 77.8) y dobla el rendimiento de Opus 4.8 en coding (29.3% vs 13.4%). Es el mismo modelo base que Mythos Limit, diferenciado solo por las capas de seguridad. Costo: el doble que Opus 4.8. Disponible en los planes hasta el 22 de junio; a partir del 23 pasa a ser solo consumo por API.

---

## Sneak peek — Nueva plataforma de WhatsApp para agencias

**[1:14:06] Carlos – Preview del sistema WhatsApp multitenant** Carlos mostró en vivo la aplicación web (Next.js) que lanzará al final de la semana para la comunidad. Permite gestionar todos los clientes desde un dashboard de agencia con workspaces separados. Incluye: inbox unificado con etiquetas, handoff a humano con notas contextuales, configuración de agentes (nombre, avatar, modelo, autoetiquetado, resúmenes automáticos, prompt, modo setter con preguntas de calificación), integraciones con WhiteCloud, Open Router, GoHighLevel y Meta templates, knowledge base por archivos o preguntas frecuentes, y automatizaciones por palabra clave o evento. Multitenant: cada cliente accede solo a su workspace; el agente ve todo desde su cuenta de agencia.
