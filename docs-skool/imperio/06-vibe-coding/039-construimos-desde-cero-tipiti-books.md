# Construimos desde cero TIPITI BOOKS

> Ruta: Vibe-Coding › Construimos desde cero TIPITI BOOKS

---

La mayoría de los proyectos de vibe coding fallan no porque la IA sea mala, sino porque no existe una base de planificación sólida. Sin documentos maestros, el agente pierde contexto, empieza a alucinar y el proyecto se desintegra.

En esta sesión hicimos algo diferente: tomamos la idea ganadora del primer **Tanque Imperial** de la comunidad y construimos toda la arquitectura de planificación en vivo, desde cero.

---

**Problema que resuelve esta sesión:**

Cómo estructurar un proyecto de vibe coding para que el agente nunca pierda contexto, cómo generar los documentos maestros que guían el desarrollo fase a fase y cómo pasar de una idea en la cabeza a un repositorio listo para desarrollar.

---

**Intervenciones**

**[****00:00****] Presentación del Tanque Imperial** Max y Joaco explican el origen de esta nueva dinámica: un "Shark Tank" de la comunidad donde un proyecto ganador recibe sesión completa de planificación y acompañamiento. Se presenta a Sofía González, ganadora de esta primera edición, quien acaba de renunciar a su trabajo corporativo para apostar por su emprendimiento.

**[****06:15****] Pitch de Sofía – TipityBooks** Sofía presenta su idea: una plataforma web que genera libros infantiles personalizados con ilustraciones estilo acuarela usando IA. Tres pilares: conexión familiar a través de la lectura, personalización del personaje (pelo, piel, lentes, nombre) e idioma. El mercado objetivo son familias latinoamericanas, incluyendo familias bilingües que hoy deben importar libros a más de 60 dólares con semanas de espera.

**[****09:17****] Carlos – La metodología de planificación** Explica el framework de 6 a 7 documentos maestros que usa para desarrollar apps con vibe coding: PRD, User Stories, Wireframes, UI/UX, TechSpec, guías de generación de imágenes y Master Blueprint. El objetivo es que el agente tenga una "biblia" del proyecto y nunca pierda contexto al abrir nuevas sesiones.

**[****16:30****] La herramienta del Tanque Imperial** Carlos construyó una interfaz en vivo con 3 vistas: administrador, participante y stream. Sofía responde preguntas por voz, el sistema transcribe y corrige automáticamente, y las respuestas se envían directamente al agente para alimentar los documentos.

**[****20:00****] Entrevista en vivo – Generando el PRD** Carlos conduce la entrevista con Sofía: happy path del usuario, precio y competencia, usuario objetivo, inputs y outputs del sistema, método de pago, KPIs de éxito y definición del MVP vs fases futuras. El agente procesa cada respuesta y hace preguntas de seguimiento que ni el equipo había anticipado.

**[****49:00****] Revisión del PRD generado** Se muestra en vivo el documento final: propuesta de valor, flujo principal, especificaciones de impresión, persona de usuario, TAM estimado, modelo de negocio, arquitectura de datos, KPIs, hitos temporales, riesgos e incluso recomendaciones de marketing con influencers y estrategia de lanzamiento. Sofía queda impactada con la profundidad del documento.

**[****01:21:00****] TechSpec – Stack tecnológico completo** El agente analiza el PRD y recomienda el stack completo: Next.js 15 con App Router, TypeScript, Tailwind, shadcn/ui, Supabase, Mercado Pago, Resend para emails transaccionales, Vercel para deploy, Sentry para monitoreo, upscaling de imágenes para impresión y Playwright para testing automatizado. Todo justificado en función del proyecto.

**[****01:30:00****] Insight arquitectónico clave – Las 3 capas** Sofía propone una idea brillante: en lugar de generar imágenes por demanda (44 centavos por pedido), pre-generar las 96 combinaciones de personajes una sola vez (42 dólares total) y separar el libro en 3 capas independientes: capa de escena, capa de personaje y capa de texto con variable de nombre. El agente confirma que es una mejora arquitectónica fundamental y actualiza los 3 documentos en tiempo real.

**[****01:48:00****] Q&A – Cómo continúa el desarrollo** Carlos explica el flujo completo: una vez terminados los documentos maestros, se instalan los skills necesarios, se inicializa el repositorio en GitHub y el agente trabaja fase por fase, hace sus propias pruebas y avisa cuando está listo para avanzar. Sofía solo necesita orquestar.

**[****01:58:00****] Cierre** Recap del proceso, anuncio de seguimiento del proyecto y próximos pasos de la comunidad.
