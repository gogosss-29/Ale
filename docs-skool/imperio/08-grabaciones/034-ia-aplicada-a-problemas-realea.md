# IA aplicada a problemas realea

> Ruta: 🔴 Grabaciones › IA aplicada a problemas realea

**🎬 Vídeo (59.0 min):** https://youtu.be/KqEfjIUrb-I

---

**Problemas que resuelve:**  
Cómo decidir entre lógica y IA en automatizaciones reales, cómo evitar errores comunes al procesar datos en Make y N8N y cómo diseñar soluciones más estables en escenarios con carga alta de información o criterios blandos.

---

### **Intervenciones**

**[00:00] Daniel – Optimización de procesos en empresa HVAC**  
Comparte el caso real de una compañía en Estados Unidos que manualiza payroll, presupuestos e intercambio de información. Explica cómo reemplazar flujos ineficientes con IA, transcripción, traducción y OCR. Logran reducir procesos de días a minutos y detectan un costo oculto de más de 5.000 dólares mensuales por tareas repetitivas.

**[07:00] Franco – Análisis del caso y foco en diseño de sistemas**  
Explica por qué el valor hoy está en detectar procesos, no en ejecutar lo técnico. Recalca la importancia de aprender a analizar necesidades antes de armar flujos. Marca la diferencia entre herramientas lógicas y herramientas de IA dentro de cualquier arquitectura.

**[10:50] María – Asistente con WhatsApp, IA y AirTable que no guarda datos**  
Explica que su agente identifica datos, pero los sobrescribe o borra. El flujo no registra nombre, correo ni clasificación. También busca enviar enlaces distintos según tipo de cliente.  
**Solución:** revisar el uso incorrecto del record ID, eliminar el uso de thread ID, corregir búsqueda con Search Records y asegurar que AirTable actualice cada campo sin borrar datos. Ajuste completo del flujo.

**[18:40] Franco – Diagnóstico técnico del flujo de María**  
Aclara la diferencia entre update y upsert, muestra cómo el thread ID generaba registros duplicados, cómo mantener persistencia y cómo evitar que AirTable reemplace campos vacíos. Caso aplicado y resuelto en vivo.

**[22:00] Franco – Votación de dinámica y cambio a bloque técnico**  
Deciden avanzar con contenido técnico para reforzar conceptos clave.

**[24:00] Franco – Cuándo usar lógica y cuándo usar IA**  
Explica ejemplos claros:  
• Cálculos, promedios, conteos o condiciones, siempre lógica.  
• Análisis de conversaciones, selección de mejores opciones o decisiones con criterios blandos, IA.  
Muestra cómo un mal uso de IA puede fallar con cargas grandes.

**[28:30] Ejemplo práctico: Inmobiliaria y selección de propiedades**  
Cómo pasar de 80 propiedades a 10 usando filtros lógicos y después dejar que la IA decida las mejores tres según conversación.  
**Clave:** primero filtrar con lógica, luego IA. Nunca al revés.

**[35:00] Franco – Context Engineering y reducción de carga para el modelo**  
Muestra cómo dividir respuestas en tres ítems para mejorar precisión y cómo evitar pasar listas enormes que hacen fallar el modelo.

**[39:00] Daniel – La lógica primero, siempre**  
Explica la mentalidad de programador: pensar en uno o cero, diseñar flujo primero y sólo después meter IA. Enfatiza por qué copiar plantillas ajenas es mala práctica si no entiendes el flujo.

**[43:00] Franco – Guardarrails y agentes verificadores**  
Muestra cómo agregar un segundo agente que revisa si el primero derivó a humano. Explica por qué los agentes largos fallan y cómo un verificador pequeño soluciona el problema con más estabilidad.

**[47:30] Diana – Diferencia entre usar un agente de GPT o un completion**  
Pregunta si hay diferencias entre usar un agente del constructor de GPT y un módulo simple de completion en Make.  
**Respuesta:** el agente tiene rol, memoria y herramientas. El completion es un mensaje suelto. Cada uno sirve para tareas distintas.

**[51:00] Franco – Ejemplo final: detección de barrios con IA o lógica**  
Muestra cuándo conviene usar matching lógico (upper-case, keywords) y cuándo usar IA por variabilidad del lenguaje.  
• Si el usuario escribe siempre igual, lógica.  
• Si no se puede garantizar consistencia, IA.

**[57:00] Orlando – Por qué no usar Make para todo**  
Pregunta por qué el ejemplo se desarrolló en N8N.  
**Respuesta:** menor costo, más flexibilidad para desarrolladores y mejor manejo de código.

**[58:30] Cierre**  
Franco resume decisiones técnicas, importancia de entender procesos y diferencia entre herramientas. Finaliza invitando a seguir el trabajo el martes.
