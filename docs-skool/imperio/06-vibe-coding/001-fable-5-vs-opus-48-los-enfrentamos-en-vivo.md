# Fable 5 vs Opus 4.8: los enfrentamos en vivo

> Ruta: Vibe-Coding › Fable 5 vs Opus 4.8: los enfrentamos en vivo

---

**Problemas que resuelve la sesión 10 de Junio: **Cómo construir una web app completa con un solo comando usando Claude Code, cómo comparar modelos en condiciones reales (misma tarea, mismo blueprint), y cómo el arnés y la planeación previa impactan el resultado final.

---

**Intervenciones**

**[****00:00****] Carlos – Contexto y arranque del experimento** Presenta el reto: construir un módulo de control de inventario (dashboard con KPIs, CRUD de productos, movimientos, alertas de stock) con un único comando one-shot. Lanza el mismo prompt en paralelo para cuatro instancias: Opus 4.8 sin arnés, Opus 4.8 con arnés (Forge), Claude 4 Fable 5 sin arnés y Fable 5 con arnés.

**[****03:00****] Carlos – El Golden Path** Mientras los modelos trabajan, explica el stack recomendado para construir web apps: Next.js 19 + TypeScript, Tailwind + shadcn/ui, Supabase (Postgres), Zod + Zustand, y Vercel para deploy. Marca la diferencia entre tener Front y Back en un solo proyecto versus tener que armarlos por separado.

**[****07:00****] Joaco – Contexto para la audiencia de YouTube** Explica la diferencia entre la sesión de Zoom (comunidad interna) y el live de YouTube. Contextualiza qué es el bytecoding, qué es un arnés agéntico y por qué dedicar el 80% del tiempo a planeación reduce errores y alucinaciones en la etapa de construcción.

**[****13:00****] Carlos – Supabase vs otras alternativas de backend** Compara Supabase con Firebase, Postgres puro y opciones self-hosted. Explica cuándo conviene cada uno, cómo levantarlo local para pruebas y cómo conectarlo al agente vía MCP para que escriba queries y cree tablas directamente.

**[****22:00****] Carlos – Vercel, shadcn y herramientas de apoyo** Cierra la explicación del Golden Path con Vercel (auto-deploys vía GitHub), shadcn (componentes listos para copiar, no una librería que se instala), Zod para validación en runtime y Zustand para estado global. Aclara por qué Next.js y Vercel van naturalmente de la mano (mismo creador: Guillermo Rauch).

**[****39:00****] Carlos – Fable 5 con Forge termina primero** El último modelo en lanzarse es el primero en entregar. La app abre en el browser con animaciones, alertas de stock funcionales y dashboard completo. El agente usó Playwright para hacer sus propias validaciones según la rúbrica del blueprint.

**[****47:00****] Carlos – Comparativa en vivo de las cuatro versiones** Recorre cada build en el browser probando: búsqueda, filtros por categoría, exportar CSV, creación de productos (detección de SKU duplicado), movimientos con control de stock mínimo y alertas en dashboard. Resultados clave:

- Opus sin arnés y Fable sin arnés dejaron el campo de "unidad" como texto libre (no dropdown) — error de UX importante.
- Fable con arnés ocupó toda la pantalla sin scroll horizontal innecesario.
- Opus (ambas versiones) puso dropdown de unidades correctamente.
- Fable sin arnés tardó más que los otros tres pese a ser el modelo más nuevo.

**[****01:20:00****] Daniel – Importancia de especificar mobile-first** Señala que ninguna versión quedó bien optimizada para móvil porque el blueprint no lo especificó. Explica la diferencia entre table y card layout en distintos viewports y por qué es una instrucción que siempre debe ir en el documento.

**[****01:25:00****] Carlos – Agnitation para feedback visual al agente** Muestra cómo, en vez de describir con texto qué componente hay que ajustar, la herramienta Agnitation permite hacer clic sobre el elemento en el browser y generar automáticamente el fragmento de código que el agente necesita para ubicar exactamente qué modificar.

**[****01:46:00****] Votación y resultado** La comunidad vota en YouTube: gana **Opus 4.8 con arnés Forge** con ~48% de los votos. Carlos publica el repositorio en GitHub como recurso abierto para la comunidad.

**[****01:53:00****] Bonus: vídeo generado con Hyper Frames + Claude Code** Carlos muestra un video en loop generado 100% con Claude Code usando Hyper Frames, sin herramientas de generación de imágenes ni video externas, corriendo local en su Mac Mini. La sesión cierra con una votación informal para dedicar el próximo miércoles a ese tema.  
  
**Resumen: **  
**Carlos y Joaco realizaron una sesión en vivo de Vibe Coding en la que compararon la efectividad de distintos modelos de inteligencia artificial (IA) para desarrollar una aplicación de inventario en tiempo real. **  
**La sesión incluyó la ejecución simultánea de cuatro comandos utilizando Opus 4.8 y Facebook 5 con y sin el arnés Forge desarrollado por Carlos, midiendo el tiempo de ejecución y el consumo de tokens. Los participantes observaron que Opus 4.8 con arnés completó el proyecto en aproximadamente 18 minutos, mientras que Facebook 5 sin arnés fue el primero en finalizarlo en menos de 15 minutos. **  
  
**Durante la presentación, Carlos explicó el "Golden Path" recomendado para desarrollar aplicaciones web utilizando Next.js, Tailwind CSS, Supabase y Vercel, destacando la importancia de una correcta planificación y de la metodología "feature-first". **  
**La sesión también incluyó una demostración de cómo el mismo Blueprint podría adaptarse para crear distintas aplicaciones, y los asistentes realizaron una votación en YouTube para determinar qué resultado era el mejor; Opus 4.8 con arnés obtuvo la mayoría de los votos.**
