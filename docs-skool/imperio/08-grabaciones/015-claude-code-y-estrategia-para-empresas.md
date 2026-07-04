# Claude Code y Estrategia para Empresas

> Ruta: 🔴 Grabaciones › Claude Code y Estrategia para Empresas

---

**Problemas que resuelve:** Cómo presentar y vender soluciones de IA a empresas que parten desde cero, cómo estructurar agentes con copiloto humano en contextos de alta responsabilidad, cómo gestionar costos de tokens y modelos en proyectos reales, y cómo usar Claude Code para automatizar flujos complejos como extracción de PDFs y desarrollo de aplicaciones web.

---

**Intervenciones**

**[00:00] Franco – Apertura y mecánica de la sesión** Introduce la dinámica de preguntas y respuestas semanal. Contextualiza que la sesión viene después de 2 horas de trabajo con Claude Code junto a Benja y Max.

---

**[02:28] Natalia – Cómo abordar la primera reunión con una empresa que quiere implementar IA** Consulta sobre una empresa de nutrición infantil que quiere adoptar IA pero parte desde cero. Pregunta cómo estructurar la primera reunión y cómo gestionar la adopción cultural interna.

Solución: No partir desde la solución sino desde el problema. Identificar la tarea que más tiempo consume, arrancar con algo tangible y de bajo riesgo. Para la adopción interna: buscar un aliado empleado (no el dueño), usar interfaces amigables como Airtable, hacer demostraciones en vivo y enfatizar que la IA es herramienta, no reemplazo.

---

**[10:44] Juan Estevan – Cómo vender un clasificador de fracciones arancelarias con IA para una maquiladora** Desarrolló un agente experto en clasificación aduanera. Ahora la empresa quiere comprarlo pero tiene dudas sobre el riesgo de alucinaciones y cómo fijar el precio.

Solución: Implementar sistema de copiloto semáforo (verde/amarillo/rojo) donde la IA hace el trabajo pesado y un humano revisa los casos dudosos. Agregar un segundo agente verificador para reducir alucinaciones. Para el precio: investigar a la competencia, no calcular en la reunión, y posicionar el valor como multiplicador de productividad del clasificador humano ya existente.

---

**[22:34] Jorge Monterde – Cómo implementar IA en una agencia de marketing de 15-40K/mes** Agencia con 3 personas que usa ChatGPT y Claude de forma básica. Quiere automatizar análisis de métricas, reporting y auditorías de Meta Ads.

Solución: Arrancar con Claude Bot con acceso de solo lectura a las fuentes de datos. Usar modelos alternativos (como Minimax) para iteración cotidiana y reservar modelos más potentes para tareas complejas. Empezar por 1 o 2 tareas concretas antes de escalar.

---

**[33:59] Natalia – ¿Vale la pena migrar automatizaciones de Make a N8N?** Tiene automatizaciones antiguas en Make funcionando sin problemas. Pregunta si conviene migrarlas todas a N8N.

Solución: Equipo que gana no se cambia. Migrar solo los flujos que están generando problemas o los que más consumen operaciones. Mantener en Make lo que funciona sin costo significativo. Claude Code puede ayudar a traducir flujos de Make a N8N si se necesita.

---

**[39:03] Jenn – Flujo de extracción de PDF de 21 páginas que solo procesa la primera** Tiene un flujo en Make que extrae datos de PDFs de un hotel (llegados por Slack) y los envía a Google Sheets, pero solo procesa la primera página y no extrae imágenes.

Solución: Pasar el caso completo a Claude Code con Opus, incluyendo el código actual y el resultado de ejecución. Evaluar migrar a N8N y considerar una API especializada como ILovePDF o SmallPDF para el procesamiento de documentos complejos.

---

**[48:09] Ángel Loría – ¿Se puede construir una app de control de obras con Claude Code?** Está desarrollando una web app de gestión de obras de construcción con frontend en progreso. Pregunta si puede usar Claude Code para el backend y representar datos con dashboards.

Solución: Sí, Claude Code es capaz. Usar un IDE como Cursor, VS Code o Windsurf como entorno. Dedicar tiempo a la planificación antes de ejecutar. No sesgar al modelo durante el desarrollo.

---

**[52:46] Jorge Arrau – Cómo trabajar con dos carpetas de proyecto separadas en Claude Code** Tiene una app dividida: una parte en Claude Code terminal (scrapper) y otra en Windsurf (web). Quiere que ambas se comuniquen.

Solución (Carlos): Usar GitHub para mantener ambos proyectos sincronizados. Tener una carpeta madre con subcarpetas por proyecto. Abrir sesiones separadas de Windsurf para cada proyecto. Claude Code puede referenciar archivos de otras carpetas cuando se le indica explícitamente, sin necesidad de mezclar los contextos.

---

**[58:50] Cierre – Franco** Resume la sesión, anuncia que el viernes habrá una nueva sesión profundizando en Claude Code. Invita a la comunidad a votar temas con anticipación.
