# Auditoría, modelos locales y primer cliente

> Ruta: 🔴 Grabaciones › Auditoría, modelos locales y primer cliente

**🎬 Vídeo (72.2 min):** https://www.youtube.com/watch?v=DmRVWEdL0nQ

---

**Problemas que resuelve la sesión 8 de Mayo:** Cómo auditar procesos antes de automatizarlos, cómo estructurar proyectos en Claude Code con el repo de Carlos, cómo gestionar modelos locales en hardware limitado, y cómo escalar soluciones de automatización sin perder rentabilidad.

---

**Intervenciones**

**[00:00] Franco – Introducción y dinámica de la sesión** Explica el formato de Q&A abierto. Invita a levantar la mano para participar. Menciona que si hay tiempo se avanza con un workshop de auditoría.

**[01:20] Pablo (España) – Organización de proyectos en Claude Code** Duda sobre si abrir nuevas conversaciones o crear carpetas por proyecto dentro del asistente de N8N.

Solución: armar un directorio desde Claude con carpeta de conocimiento general y subcarpetas por proyecto. Abrir siempre Visual Studio Code desde la carpeta del repo de Carlos para no perder el contexto prearmado.

**[07:16] Dorian – Primera reunión con una clínica: demo, precio y escalabilidad** Compartió su experiencia en su primera reunión de ventas. Presentó un asistente virtual con agendamiento, calificación de leads y dashboard. El cliente preguntó si podía integrarse con "Agenda Pro" y exigió comprobante de transferencia antes de agendar.

Solución: verificar la API de Agenda Pro buscando "[nombre] API reference" y pasando la documentación a Claude para listar qué acciones permite. La detección de comprobantes por imagen es posible. Para el precio: Franco recomienda priorizar la primera experiencia y el caso de éxito sobre el monto cobrado. Primer cliente puede ser a precio reducido o gratuito para ganar confianza y prueba social.

**[19:43] Daniel – Aporte sobre duplicación de proyectos y precio** Comparte su experiencia de 20 años como desarrollador en EE.UU. Explica cómo usar ramas en Git (clone, master, branch) para duplicar proyectos sin reescribir desde cero. Refuerza la idea de que el primer cliente absorbe el costo de aprendizaje y que con cada proyecto el tiempo se reduce y la rentabilidad sube.

**[24:22] Pablo (Chile) – Automatización de prospección en LinkedIn para inmobiliaria** Realtor en Chile que quiere automatizar la búsqueda de clientes de locales comerciales vía LinkedIn para validar el modelo y luego ofrecerlo a otros corredores via Go High Level.

Solución: Franco advierte que se está automatizando un proceso que aún no fue validado manualmente, lo cual es arriesgado. Recomienda empezar con LinkedIn Sales Navigator ($100/mes, con mes gratis) para hacer listas filtradas y prospectar de forma manual primero. Para automatizar: evaluar Lemlist o Galaxy antes de construir algo propio. Riesgo de shadowban si se automatiza mal o a alto volumen (+10/20 mensajes por día).

**[32:39] Mauricio – Modelos locales en Mac Mini y arquitectura con OpenClaw + Claude Code** Quiere armar un orquestador "Chief of Staff" con OpenClaw, usando Claude Code para desarrollar, con modelos locales en un Mac Mini 16GB dentro de Docker.

Solución: los modelos buenos locales requieren máquinas potentes. Con 16GB se pueden correr modelos chicos o algunos medianos sacrificando velocidad. Para sincronizar Claude Code con OpenClaw: usar Sync para compartir carpeta entre entornos. Carlos aclara la diferencia clave: OpenClaw orquesta, Claude Code desarrolla; no mezclarlos. El MCP conecta ambos sin que OpenClaw toque el código.

**[42:32] Franco – Framework de auditoría de procesos (workshop)** Presenta el framework interno que usa en su agencia ROB para evaluar si un proceso es candidato a automatización o incorporación de IA.

**Mitos a romper:**

- La IA no arregla procesos rotos, los amplifica.
- No todo proceso debe automatizarse.

**5 criterios de evaluación:**

1. **Repetitividad** – ¿Cuántas veces ocurre? ¿Diario, semanal, anual?
2. **Estructurabilidad** – ¿Existe un input y output predecible? ¿Se puede explicar por qué se toma cada decisión?
3. **Datos disponibles** – ¿Está el conocimiento documentado o solo en la cabeza de alguien?
4. **Costo de oportunidad humano** – ¿Hay una persona valiosa haciendo tareas repetitivas?
5. **Costo del error** – ¿Qué pasa si la IA se equivoca? ¿Es recuperable o catastrófico?

**3 modalidades de solución:**

- **100% humano** – Cierres de alto valor, negociaciones sensibles, decisiones estratégicas.
- **Copiloto (la mayoría)** – La IA prepara, sugiere o redacta; el humano revisa y aprueba.
- **Agente autónomo** – Solo para procesos de bajo riesgo donde un error es recuperable.

Recomendación: empezar siempre en modo copiloto y aumentar autonomía gradualmente con métricas.

**5 pasos del framework:**

1. Mapear el proceso (quién, cuándo, qué entra, qué sale)
2. Detectar cuellos de botella y fricciones
3. Priorizar el dolor más fuerte
4. Definir modalidad (humano / copiloto / agente)
5. Establecer métricas de éxito antes de lanzar

**[1:01:41] Carlos – Sistema tipo Lego para reutilizar desarrollos** Pregunta si Franco tiene un sistema para reutilizar componentes entre clientes.

Respuesta: en ROB el 90% de los desarrollos parten de una template existente. Se elige la más parecida, se duplica y se personaliza. Daniel agrega que él lo hace dinámicamente desde una base de datos, al estilo Tesla: todo el código está disponible y se "activan" módulos según el cliente.

**[1:05:53] Agustín – Costos de API y personalización de soluciones** Pregunta cómo se manejan los costos de API (OpenAI, Anthropic) y si las soluciones son custom o genéricas.

Respuesta: todas las soluciones en ROB son personalizadas, aunque parten de templates. Los costos se prevén durante el discovery estimando volumen de conversaciones y optimizando el uso de tokens. La economía de tokens es una habilidad clave en la etapa actual donde las APIs tienen costos elevados.

**[1:09:23] Vincent – Infraestructura propia vs. del cliente, y servicio mensual** Consulta si el cliente debe tener su propia VPS o si Franco gestiona todo, y cómo manejar el soporte mensual.

Respuesta: ROB gestiona todo en su propia infraestructura y cubre los costos dentro del precio del servicio. Franco advierte que llevar un buen servicio mensual consume más energía que desarrollar, y que funciona mejor cuando se apunta a negocios grandes que pagan bien, no a emprendedores pequeños que huyen del pago recurrente.

**[1:12:00] Cierre** Franco resume los temas del día y confirma próxima sesión el martes.
