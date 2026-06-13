# Notebook LM + N8N

> Ruta: 🔴 Grabaciones › Notebook LM + N8N

**🎬 Vídeo (62.0 min):** https://www.youtube.com/watch?v=KJ6WTBakr38

---

Esta sesión muestra cómo usar Notebook LM como asistente de construcción y análisis de flujos complejos en N8N. Resuelve la dificultad de crear prompts consistentes, estructurar agentes multiagente y acelerar el desarrollo técnico sin depender exclusivamente del conocimiento manual del desarrollador.

---

# **Intervenciones cronológicas**

### **[00:00] Fran – Inicio y contexto de la sesión**

Explica que la sesión del viernes estará dedicada a profundizar en Notebook LM tras la demo previa de Juaco. Presenta el objetivo: analizar la herramienta y ponerla a prueba para construir agentes IA en N8N, incluso sin conocer de antemano la respuesta correcta.

### **[01:00] Fran – Qué es Notebook LM y por qué es distinta**

Describe la interfaz, el enfoque en fuentes, el uso tipo RAG, y cómo permite cargar documentos, audios e imágenes para generar análisis, ideas o contenido.

### **[03:30] Fran – Primer vistazo técnico: Cuadernos, fuentes y uso para N8N**

Abre un notebook con flujos reales de N8N (plantillas, agentes complejos y subagentes) y explica cómo entiende la herramienta el contenido estructurado. Muestra el análisis automático del flujo y la creación de mapas mentales.

### **[06:00] Fran – Profundizando en un agente complejo**

Explora un agente inmobiliario que incluye WhatsApp, múltiples ramificaciones y troubleshooting. Explica qué partes son claves y cuáles se repiten entre proyectos.

### **[09:40] Fran – Ventajas del panel lateral: notas, resúmenes y análisis de nodos**

Prueba la función de “explicar el nodo”, cómo Notebook LM puede redactar un análisis claro de partes del flujo, y la importancia del botón de “reset chat”.

### **[12:40] Juaco – Tips de uso: añadir notas y convertirlas en fuentes**

Juaco explica cómo guardar respuestas del chat como notas permanentes y añadirlas como fuentes del cuaderno para mantener la información siempre disponible.

### **[16:00] Fran – Creando un notebook nuevo para prompting de agentes**

Carga una plantilla completa de N8N y la convierte en fuente. Explica que Notebook LM no admite JSON directo, por lo que debe pegarse como texto plano.

### **[18:00] Fran – Primer test: “Crea un agente multiagente para un estudio jurídico”**

Pide un JSON completo. Notebook LM genera una plantilla funcional, respetando estructura, roles y subagentes. Se sorprende de la calidad del resultado vs. el tiempo invertido.

### **[22:00] Fran – Importación en N8N y primeros errores esperables**

Importa la plantilla generada en N8N. El import funciona, pero aparecen errores de variables y expresiones. Explica que es normal por lo rápido del proceso.

### **[24:40] Fran – Comparación estructural del prompt generado**

Compara el prompt original vs. el generado. La estructura es extraordinariamente similar: rol, objetivo, contexto, herramientas, principios. Reconoce que el resultado es mucho mejor de lo esperado.

### **[28:00] Fran – Primera prueba conversacional del agente**

Prueba el agente en vivo. Detecta la intención correctamente, llama al subagente adecuado y reproduce el comportamiento esperado, pese a pequeños fallos de memoria o herramientas.

### **[31:00] Fran & Juaco – Análisis del error: memoria principal faltante**

Notebook LM omitió el nodo de memoria. Juaco propone un prompting más estricto basado en fuentes y plantillas de referencia para evitar omisiones.

### **[37:00] Fran – Segunda prueba: problema laboral**

El agente reconoce la intención (“derecho laboral”), deriva al subagente, aplica preguntas correctas y reproduce la máquina de estados. Se confirman las capacidades del multiagente.

### **[41:00] Fran – Detección de un error: creación automática de tablas inexistentes**

Notebook LM inventó un nombre de tabla (“Lexi chat histories”). Explica por qué ocurre: prompting ambiguo + fuentes insuficientes.

### **[47:00] Fran & Juaco – Mejor estrategia: cargar instrucciones como fuentes**

Crean fuentes separadas para tres subagentes con instrucciones reales de un proyecto MTM: compras, alquileres, tasaciones. Explican por qué esto mejora la precisión.

### **[52:00] Fran – Segundo gran test: recrear una plantilla completa con cambios reales**

Notebook LM genera un JSON completo, incluyendo nodos, memorias y herramientas. El output es extenso y funcional.

### **[56:00] Fran – Importación final y evaluación**

Importa la plantilla generada y valida: estructura sólida, coherencia, nodos completos y prompting funcional. Reconoce mejoras respecto a la versión anterior.

### **[59:00] Fran – Conclusión**

Notebook LM demuestra ser útil para:

- Crear prompts complejos y consistentes
- Documentar flujos
- Analizar agentes IA
- Replicar plantillas a escala
- Prototipar en minutos lo que antes llevaba horas

Juaco anuncia un próximo taller exclusivo de Notebook LM dentro de Imperio Digital.
