# Soporte - 3 de Marzo

> Ruta: 🛠️ Soporte › Soporte - 3 de Marzo

**🎬 Vídeo (55.8 min):** https://www.youtube.com/watch?v=9TG1YiCb02M

---

**Problemas que resuelve**

**-Qué es realmente el vibe coding y qué queda oculto detrás de sus resultados.**  
-**Cómo gestionar los límites de tokens en Claude Code y Cursor sin perder productividad.**  
-**Cómo rotar modelos según complejidad de la tarea para optimizar costos y rendimiento.**  
-**Cómo identificar y corregir problemas de performance (N+1 calls, espaguetti de código) -generados por IA sin supervisión.**  
-**Alternativas a Claude para desarrollo con IA: modelos, herramientas y configuraciones.**  


---

  
  
**[00:00] Franco & Daniel – Apertura: OpenClow y agentes multi-canal**

**Presentan el contexto de la sesión (martes 3 de marzo de 2026).**

Conversan sobre OpenClow corriendo en VPS: tareas autónomas, reconfiguracion de archivos y potencial multiagente. Daniel menciona que lo integraron con N8N en un minuto. Se discute la arquitectura de subagentes por canal en Discord para proteger el contexto y asignar skills específicas.

**[05:00]  Tomás – Sistema de outreach con páginas web personalizadas**

**Automatización de marketing: creativos, copies, programación y reportes de métricas por mail.**

Tomás describe su sistema: carga creativos desde un dashboard, genera copies automáticamente, programa publicaciones y envía reportes. Comparte su búsqueda de mejor diseño visual para las páginas de demo que envía a clientes. Se recomienda usar la plataforma [21st.dev](http://21st.dev) para referencias de componentes y copiar prompts hacia Claude Code.

**Solución: **Para el outreach, se recomienda priorizarWhatsApp (audio incluido) sobre mail por mayor tasa de apertura. Con Evolution API se pueden enviar 20-30 mensajes/día sin riesgo. Con la API oficial de WhatsApp Cloud, hasta 2000/día con costo por mensaje.

**[20:00]  Tomás & Franco – Automatización de publicaciones en Instagram**

**Consulta sobre herramientas para publicar en redes sociales de forma automática.**

Se mencionan Metricool (plan Advanced ~$70/mes con acceso a API), Publer y el nodo nativo de Make. Conexión directa a la API oficial de Instagram requiere autorizaciones complejas de Meta. Se sugiere buscar skills disponibles en OpenClow para Instagram.

**Solución: **Explorar skill de OpenClow para Instagram y evaluar Publer. Si el volumen lo justifica, pagar el plan Advanced de Metricool para integrar vía API.

**[25:00]  Ricardo (chat) – Problema instalando OpenClow en VPS**

**No logra instalar OpenClow en VPS (Piensa Solutions, España) tras múltiples intentos.**

Se menciona que Hostinger facilita la instalación y que con 4 GB de RAM debería funcionar. Sin ver los logs de error no es posible diagnosticar. Se recomienda publicar el error completo en la comunidad (School) para soporte detallado.

**[30:00]  Paloma – Límites de tokens en Claude Code (VS Code)**

**Primera sesión. Está construyendo un CRM propio con Claude Code en VS Code y se queda sin créditos.**

Actualmente en plan de $20/mes, se queda sin tokens en 30-45 minutos de trabajo. Pregunta si existe alternativa más accesible.

**[33:00]  Daniel – Estrategia de rotación de modelos en Cursor**

**Explicación práctica de cómo gestionar límites de IA cambiando modelos según la tarea.**

Daniel muestra cómo en Cursor (plan Ultra $200/mes) rota entre modelos: Haiku o auto para tareas simples (cambiar colores, buscar referencias), Sonnet para razonamiento intermedio, Opus para tareas complejas. Esto extiende el límite mensual considerablemente. En Claude Code se accede al selector con '/' en la caja de chat.

**[38:00]  Tomás – Experiencia con límites de Claude y recomendación al plan $100**

**Comparte cómo agotó hasta el crédito semanal con el plan de $20.**

Con el plan de $100, una semana después de inicio, con tres proyectos simultáneos corriendo toda la noche, lleva solo un 19% de uso. Recomienda el salto si el uso es intensivo y productivo.

**Solución: **Para uso profesional intensivo: plan de $100/mes en Claude. Para proyectos simples o poca carga: rotar a modelos más pequeños dentro del mismo plan.

**[44:00]  Daniel – Vibe coding y el espaguetti oculto**

**Muestra en vivo un proyecto propio con problemas de performance generados por IA sin supervisión.**

Daniel corre su backend (.NET + Dapper) y detecta que hay múltiples llamadas API redundantes (problema N+1) generadas por el frontend en Next.js. El vibe coding construye rápido, pero si no se supervisa el código, el sistema escala mal. Lo diagnostica en vivo con Claude: pide análisis en español, obtiene respuesta estructurada, luego cambia a ChatGPT dentro del mismo agente para obtener la documentación técnica explicada de otra forma.

**[50:00]  Franco – Paralelismo con prompts espaguetti en agencias**

**Relata el caso de un desarrollador que usaba IA sin supervisión para promptear, generando prompts extremadamente largos e ineficientes.**

El prompt terminó siendo enorme por capas de instrucciones acumuladas sin revisión. Al detectarlo, rearmaron el prompt de cero con IA supervisada y quedó al 30% del tamaño original, funcionando 10 veces mejor. El problema ocurre en cualquier contexto (código o prompts) si se deja actuar a la IA sin criterio previo.

**[53:00]  Franco – Cierre y próximos pasos: equipo multiagente en la agencia**

**Resumen de la sesión y anuncio de trabajo con OpenClow multiagente.**

La agencia está implementando OpenClow como equipo multiagente con skills diferenciadas. Investigando alternativas para reducir dependencia de Claude y activar el modelo solo cuando sea necesario. Se documentará el proceso para compartirlo en la comunidad.
