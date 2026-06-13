# Context Engineering

> Ruta: 🔴 Grabaciones › Context Engineering

**🎬 Vídeo (67.7 min):** https://youtu.be/BAf_lzJqxdI

---

Esta sesión enseña a estructurar el **contexto completo de un agente de IA** (system prompt, user prompt, tools, variables y RAG) para que responda de manera precisa y consistente. Resuelve problemas comunes como salidas poco confiables, prompts mal interpretados y dificultades para integrar herramientas, logrando agentes más inteligentes y útiles en procesos de negocio.

---

### Cronología de la sesión (12 de septiembre de 2025)

[00:00] Franco – **Introducción a la sesión**  
Explica el objetivo de la reunión: abordar un tema en profundidad y dejar un recurso atemporal. Presenta el concepto de **prompt engineering** y la transición hacia **context engineering**.

[02:00] Franco – **Diferencia entre Prompt y Context Engineering**  
Aclara que el prompt es solo una parte del contexto. El contexto incluye tools, instrucciones, RAG y más, lo que permite guiar mejor a la IA.

[06:00] Franco – **Importancia del contexto en los LLMs**  
Ejemplifica cómo un mayor contexto mejora la predicción de respuestas de la IA, comparándolo con patrones lógicos.

[08:50] Franco – **System Prompt vs User Prompt**  
Detalla qué rol cumple cada uno. El **system prompt** define objetivos, tono, personalidad y reglas; mientras que el **user prompt** son las entradas del usuario.

[15:00] Franco – **Naming y descripción de Tools**  
Explica la importancia de nombrar y describir las herramientas de forma clara para que la IA las use correctamente.

[19:30] Franco – **Variables en las Tools**  
Muestra cómo aprovechar al máximo las variables para que la IA complete tareas complejas sin necesidad de lógica adicional.

[22:00] Franco – **RAG y bibliotecas de calidad**  
Describe cómo estructurar bien un RAG (retrieval augmented generation) para mejorar precisión, relevancia y accesibilidad de datos.

[25:00] Jorge – **Pregunta sobre aprendizaje del RAG**  
Consulta si el RAG aprende dinámicamente. Franco explica que puede hacerse con feedback loops, pero que en la práctica lo mantienen fijo con buena organización.

[26:00] Juaco – **Importancia del Markdown**  
Recuerda usar Markdown en los prompts para jerarquizar información. Franco lo confirma como un factor clave para que la IA interprete bien la estructura.

[30:00] Franco – **Ejemplo práctico en N8N**  
Muestra cómo se ve un system prompt real dentro de la plataforma y la importancia de estructurarlo en Markdown.

[41:00] Franco – **Ejemplos y reglas en prompts**  
Explica cómo usar ejemplos en prompts para la toma de decisiones (no para respuestas) y cómo crear reglas finales para evitar errores.

[50:00] Carlos – **Problema con outputs JSON**  
Consulta cómo estandarizar outputs en JSON. Franco recomienda repetir instrucciones tanto en la tool como en el agente para evitar inconsistencias.

[53:00] Jorge – **Uso de etiquetas en agentes**  
Pregunta cómo se aplican las etiquetas. Franco explica que sirven para categorizar respuestas y convertirlas luego en lógica de negocio.

[1:01:00] Roma – **Consulta sobre métricas en conversaciones**  
Pregunta si los agentes almacenan datos útiles para métricas. Franco responde que sí, mediante etiquetado y guardado en bases, aunque depende del uso que haga cada negocio.

[1:05:00] Juaco – **Tip sobre Canvas en GPT**  
Explica que al usar la función de “copiar desde Canvas” en GPT se obtiene directamente el prompt en formato Markdown.

[1:06:00] Jonas – **Impacto de cambios de modelo**  
Pregunta si al actualizar modelos cambian los prompts. Franco explica que sí, los estilos y reglas suelen requerir ajustes según el modelo.

[1:07:30] Franco – **Cierre de la sesión**  
Recapitula que lo más importante es escribir prompts en Markdown, estructurar bien el contexto y testear exhaustivamente.
