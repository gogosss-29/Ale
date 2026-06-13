# Vende IA sin ser programador, dashboard y agentes

> Ruta: 🔴 Grabaciones › Vende IA sin ser programador, dashboard y agentes

**🎬 Vídeo (65.7 min):** https://www.youtube.com/watch?v=KjEOB954wrk

---

**Problemas que resuelve la sesión 29 de Mayo:** Cómo estructurar proyectos y dashboards para negocios locales usando Claude Code, cómo empaquetar y vender agentes de IA como servicio, y cómo gestionar infraestructura propia (VPS, Docker, administración multi-cliente) sin comprometer la estabilidad del servicio.

---

**Intervenciones**

**[00:00] Franco – Apertura de sesión de soporte** Introduce el formato de la sesión: espacio abierto para dudas, obstáculos y preguntas de negocio o desarrollo. Indica el mecanismo de levantar la mano para gestionar el orden.

**[01:35] Adrián – Quiere construir dashboards para negocios locales** Emprendedor mexicano (Querétaro) que cerró su primer cliente de IA por $300. Quiere armar dashboards financieros para negocios como gimnasios que no tienen sus datos organizados en ningún lado.

Solución: antes de pensar en el dashboard hay que estructurar el dato. Franco recomienda empezar con el framework de auditoría de la comunidad, hacer práctica con el amigo del gimnasio sin cobrar, y enfocarse primero en aprender Claude Code antes de salir a prospectar.

**[07:56] Franco – La planificación como habilidad core** Refuerza que el 90% del éxito hoy está en planificar bien, no en ejecutar. La ejecución ya no es el cuello de botella. Recomienda la skill Grillmi para profundizar la planificación y alcanzar claridad antes de arrancar cualquier desarrollo.

**[13:25] Marvin (Tony) – ¿Cómo empaquetar agentes de IA para venderlos?** Regresa a la comunidad después de dos años. Ya tiene experiencia con Make, agentes de atención al cliente y Firebase. Quiere saber cómo empaquetar y comercializar lo que desarrolla con Claude Code y N8N.

Solución: Franco explica el modelo de su agencia — todo en infraestructura propia, cobro mensual, optimización continua de prompts y costos, y foco en que el cliente no tenga ninguna fricción técnica. El valor está en la consultoría y en entender el negocio antes de desarrollar.

**[17:26] Juan Diego – ¿Qué aprender para modernizar un ERP propio?** Peruano con un ERP legacy (Visual Basic + .NET) con clientes reales. Ya conectó Claude Code con su base de datos y armó un login funcional. Quiere saber qué stack priorizar para modernizarlo y agregar IA.

Solución: Claude Code es suficiente como núcleo. N8N y Claude Design son complementos opcionales según la tarea. Lo más importante es tener la visión clara primero — usar Claude para planificar cada funcionalidad antes de ejecutar. Se menciona Forge (herramienta de Carlos) como acelerador para ir de idea a MVP.

**[28:22] Carlos – Qué es Forge y cómo funciona** Explica que Forge es un arnés de subagentes, skills y configuraciones que guía al usuario con preguntas para pasar de idea a MVP en días. Aclara que no es una varita mágica: si no tenés el qué y el por qué claros, no puede ayudar. Sirve cuando ya tenés definido qué querés construir.

**[31:31] Marvin (Tony) – vuelve: ¿cómo empaquetar lo que vendés?** Pregunta más concreta sobre el packaging del servicio. Franco detalla: infraestructura propia, dashboards de métricas para el cliente, interfaces simples y funcionales. No se invierte tiempo en frontends complejos — el cliente quiere que funcione, no que sea bonito.

**[34:42] Iván – **[**CLAUDE.md**](http://CLAUDE.md)** vs **[**MEMORY.md**](http://MEMORY.md)** y gestión de proyectos en Claude Code** Pregunta la diferencia entre los dos archivos y cómo organizar múltiples proyectos locales (agente IA, ERP, infraestructura VPS).

Solución: [CLAUDE.md](http://CLAUDE.md) es la personalidad y las reglas permanentes del agente. [MEMORY.md](http://MEMORY.md) son los hechos y decisiones que se van acumulando durante el proyecto. La organización recomendada: cada proyecto en su propia carpeta. Para compartir contexto de infraestructura entre proyectos, generar un MD exportable desde esa carpeta y consultarlo cuando se necesite.

**[42:48] Iván – ¿Cliente con su propia API o vos gestionás todo?** Duda sobre si es mejor que el cliente administre su propio consumo de tokens o si la agencia absorbe ese costo.

Solución: Franco gestiona todo internamente para eliminar fricción al cliente. El riesgo es no prever bien los costos al cambiar modelos. Se recomienda modelar bien los costos antes de fijar precios al cliente.

**[46:08] Iván – VPS, Easy Panel, Coolify y Tailscale** Duda sobre cómo administrar múltiples clientes en infraestructura propia: ¿panel visual o consola?

Solución: Carlos recomienda Coolify como alternativa a Easy Panel — instancias ilimitadas, integración con Claude Code vía MCP, permite duplicar proyectos entre clientes. Riesgo principal: una mala configuración puede tumbar todos los servicios a la vez. Franco trabaja directo por consola. Carlos prefiere VPS separado por cliente para aislar riesgos. Tailscale es útil para uso personal pero genera fricción en producción con múltiples clientes.

**[55:23] Álvaro – Cómo conectar WhatsApp a un sistema de logística** Desarrollador PHP/Laravel que quiere agregar consultas de estado de paquetes por WhatsApp para los clientes de su cliente.

Solución: dos opciones — API oficial de Meta (engorrosa) o conectar mediante un BSP (Business Solution Provider) como Wcloud, que simplifica la integración a 5 clics con embedded sign-in. Plan gratuito disponible para hasta 2 números.

**[58:58] Yasma – Agente de research de productos para Amazon con scraping** Está armando un sistema para buscar y evaluar productos para venta en Amazon. Usa Hermes con Playwright en su VPS, conectado a Airtable y Discord. El problema: muchas páginas lo bloquean y el consumo de API fue excesivo (usó GPT en un día).

Solución: acotar las páginas objetivo y armar un scrapper específico por página, manteniéndolo ante cambios de HTML. Para scraping masivo usar herramientas como Bright Data o Apify. APIs no oficiales como alternativa. Priorizar las páginas donde se obtienen mejores resultados antes de escalar.
