# Soporte - 16 de Dic

> Ruta: 🛠️ Soporte › Soporte - 16 de Dic

**🎬 Vídeo (58.5 min):** https://www.youtube.com/watch?v=405Jre442wA

---

## Problemas que resuelve la sesión

- Cómo **agendar eventos correctamente con IA** cuando los usuarios hablan en lenguaje natural (“mañana a las 4”).
- Por qué los **agentes fallan cuando están sobrecargados** de herramientas, memoria y prompt.
- Cómo **evitar errores comunes en N8N y Make** al manejar fechas, variables, filtros y grandes volúmenes de datos.
- Cuándo usar **lógica tradicional** y cuándo usar **IA**, sin romper flujos ni perder performance.
- Cómo diseñar **arquitecturas más simples, estables y escalables** para WhatsApp, calendarios y bases de datos.

---

# 🧩 Intervenciones (planteo de problema → solución)

---

### [00:00] Contexto inicial de la sesión

**Planteo del problema:**  
Las herramientas cambian muy rápido y muchos flujos dejan de funcionar si no se entienden los fundamentos.

**Solución / Enfoque:**  
Se aclara la fecha (16 de diciembre) y se plantea la dinámica: grupo reducido, resolución de problemas reales y foco en criterio técnico, no solo ejecución.

---

### [00:35] Enzo – Agente con WhatsApp que no agenda eventos correctamente

**Problema:**  
El agente:

- Interpreta fechas como “mañana a las 4”, pero
- Google Calendar crea eventos en el horario actual o directamente falla
- La tool de calendario se llama mal, múltiples veces o no toma el output correcto
- El flujo está lleno de tools y memoria innecesaria

**Solución:**

- Detectar que **el problema no es Calendar**, sino: - Formato de fecha
- Uso incorrecto de tools
- Exceso de contexto
- Pausar el debug fino y **simplificar la arquitectura**
- Forzar: - Tool description en **manual**
- Formato **ISO 8601**
- Duración fija (10 minutos)
- Quitar tools innecesarias y reducir carga cognitiva del agente

---

### [07:15] Diagnóstico general del error de fechas

**Problema:**  
El agente entiende el texto, pero:

- No transforma correctamente “mañana a las 4”
- El output existe, pero no llega al nodo correcto
- El modelo no sabe cuándo usar cada herramienta

**Solución:**

- Dejar de “parchar” con más tools
- Explicitar cuándo usar la tool
- Definir claramente: - Fecha de inicio
- Fecha de fin relativa
- Priorizar claridad > complejidad

---

### [12:30] Franco – El verdadero problema: agentes sobrecargados

**Problema:**  
Cuantas más tools, prompts y memoria:

- Menor probabilidad de ejecución correcta
- Más errores impredecibles

**Solución:**

- Borrar herramientas que no se usan
- Separar responsabilidades
- Usar **sub-workflows**
- Un agente = una tarea clara

---

### [19:30] Alternativa práctica: usar [Cal.com](http://Cal.com)

**Problema:**  
Google Calendar directo genera fricción innecesaria.

**Solución:**

- Usar [Cal.com](http://Cal.com)
- Copiar una solución ya probada
- Menos errores, mismo impacto final en Google Calendar

---

### [23:00] Bug de WhatsApp con Evolution

**Problema:**  
Mensajes enviados desde:

- Celular → un ID
- Desktop → otro ID  
Esto rompe las respuestas automáticas.

**Solución:**

- Actualizar Evolution a versión **2.3.7**
- Usar siempre `remoteJID`
- O manipular el ID con un nodo de código

---

### [25:20] Participante – Error al usar Replicate en Make

**Problema:**

- Flujo importado de la comunidad
- API Key mal configurada
- Error en autenticación Bearer

**Solución:**

- Crear API Token en Replicate
- Usar: ```
Authorization: Bearer TU_API_KEY ```
- Verificar espacios y formato

---

### [36:00] Raimundo – Variables que “desaparecen” en N8N

**Problema:**  
Variables existen, pero no llegan al nodo final.

**Solución:**

- El problema es la **unión de múltiples rutas**
- Usar: - Nodo `Set`
- Nodo `Code`
- Consolidar variables cerca del uso final

---

### [47:00] Juan Felipe – Airtable trae demasiados datos

**Problema:**

- Cada nodo trae 10.000 a 100.000 registros
- El flujo se vuelve lento o se rompe

**Solución:**

- Filtrar **en Airtable**, no en N8N
- Crear vistas: - Últimos 30 días
- Mes calendario anterior
- Reducir carga y mejorar performance

---

### [54:30] Debate: Airtable vs bases de datos

**Problema:**  
Airtable no escala bien con alto volumen y llamadas frecuentes.

**Solución:**

- Usar: - PostgreSQL / Supabase / Redis para volumen
- Airtable solo para visualización
- Arquitectura híbrida recomendada

---

### [58:00] Cierre

**Síntesis final:**

- Pensar procesos antes que herramientas
- Lógica primero, IA después
- Menos complejidad = más estabilidad

Invitación a próximas sesiones y continuidad del trabajo.
