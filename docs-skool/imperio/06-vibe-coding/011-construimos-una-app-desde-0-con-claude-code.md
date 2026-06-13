# Construimos una app desde 0 con Claude Code

> Ruta: Vibe-Coding › Construimos una app desde 0 con Claude Code

**📎 Recursos:**
- Transcripcion
- Chat

---

---

**Problemas que resuelve la sesión del 1 de Abril:** Cómo planificar un proyecto de software desde 0 con Claude Code, cómo estructurar un repositorio para desarrollo con IA usando frameworks de agentes y documentación previa, y cómo construir un MVP sólido y escalable sin experiencia técnica profunda.

---

**Intervenciones**

**[****00:00****] Joaco – Intro y contexto de la sesión** Presenta la dinámica de la sesión de "Lifecoding" en vivo. Explica que el objetivo es desarrollar *Núcleo*, una herramienta personal de gestión del conocimiento que funcione offline, en múltiples dispositivos y con IA integrada.

**[****05:00****] Carlos – Qué es Núcleo y por qué construirlo** Describe el problema: consume mucho contenido (repositorios, posts, comandos, ideas) pero no tiene un lugar centralizado para guardarlo, buscarlo y analizarlo. Propone construir una app tipo PKM (Personal Knowledge Manager) con PWA, extensión de Chrome y chat con agente sobre la base de datos propia.

**[****08:00****] Carlos – Inicialización del proyecto con Anti Gravity y la Forja** Muestra cómo inicializar un proyecto desde 0 en Anti Gravity usando el comando Forge, que carga automáticamente el stack (Next.js, Supabase, Tailwind), agentes especializados, skills y hooks preconfigurados. Explica la diferencia entre configurar el proyecto con y sin este framework.

**[****20:00****] Carlos – Configuración de Claude Code y opciones de modelo** Muestra cómo seleccionar Opus con el flag `--plan` para que planee con el modelo más potente y ejecute con Sonnet, ahorrando tokens. Explica el modo bypass de permisos (modo yolo) y cuándo conviene activarlo.

**[****24:00****] Carlos – Viability Check: ¿vale la pena construir esto?** El agente analiza el scope del proyecto y detecta que son en realidad 4 o 5 productos distintos. Recomienda dividir en 3 fases: Fase 1 (captura + búsqueda básica), Fase 2 (offline, notas de voz, RAG), Fase 3 (análisis de videos, extensión de Chrome avanzada).

**[****31:00****] Carlos + comunidad – Definición del Happypath y features del MVP** En vivo, se construye el flujo ideal del usuario: pegar un link → elegir workspace → la IA analiza, resume, categoriza y genera tags automáticamente. Se agregan features sugeridos por la comunidad: bulk import desde CSV, carpetas anidadas (máximo 3 niveles), hasta 5 workspaces, y guardar reels/TikToks con transcripción y hooks.

**[****43:00****] Carlos – PDR (Product Definition Report)** El agente genera el documento central del MVP: problema, solución, flujo principal, alcance, riesgos, entidades de base de datos, KPIs y qué queda fuera (RAG, extensión Chrome, offline, colaboración). Muestra cómo cada nuevo documento referencia a los anteriores para mantener coherencia.

**[****51:00****] Carlos – Tech Spec y arquitectura** El agente define el stack técnico completo: Next.js, Supabase con 6 tablas e índices de búsqueda full-text, Open Router para llamadas a modelos (Haiku para categorización, Opus para resúmenes), deploy en VPS propio con Docker y Caddy. Explica por qué usa Open Router en lugar de conectarse directamente a cada modelo.

**[****01:00:00****] Carlos – User Stories y cierre de la fase de planeación** El agente genera los user stories con criterios de aceptación para cada flujo del MVP. Carlos propone un reto comunitario: quien desarrolle primero la Fase 2 a partir del repositorio publicado puede ganar acceso a la Forja. Cierre con cupón IMPERIO para la comunidad.

**[****01:41:00****] Joaco – Demo de Antomatic (bonus)** Muestra en vivo una herramienta propia que construyó con Claude Code: genera demos de chatbots para e-commerce scrapeando automáticamente la tienda, creando una base de conocimiento en Supabase y levantando una página réplica con el chat integrado. Demo en vivo con Cafeteros Chile.
