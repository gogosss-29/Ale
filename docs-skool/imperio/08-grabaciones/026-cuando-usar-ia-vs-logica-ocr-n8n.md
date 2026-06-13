# Cuándo Usar IA vs Lógica (OCR + n8n)

> Ruta: 🔴 Grabaciones › Cuándo Usar IA vs Lógica (OCR + n8n)

**🎬 Vídeo (58.4 min):** https://www.youtube.com/watch?v=HcGlEgqPSOQ

---

## Problemas que resuelve

Cómo **estructurar información desde PDFs/Word (CVs)** sin romper bases de datos, cómo **normalizar campos de selección fija** (carreras, instituciones, estado civil, moneda) cuando el input viene libre, y **decidir correctamente cuándo usar IA, OCR o lógica** para evitar alucinaciones y ganar robustez en automatizaciones.

---

## Intervenciones (cronológico)

[00:00] Franco – Apertura y formato de la sesión  
Sesión de viernes 9 de enero 2026, formato reducido y personalizado. Enfoque en ver **casos reales uno por uno** y aportar soluciones prácticas.

[01:02] Rosa – Avatares interactivos + control de accesos y tiempo de uso  
Rosa comenta avances con avatares interactivos. El reto actual es **controlar quién entra, cuánto tiempo usa el sistema** y además integrar **n8n + ManyChat** para responder mensajes en redes. Se aclara que las sesiones de viernes ahora también son de Q&A como los martes.

[03:03] Jorge – Flujo de CVs: problema con campos de selección fija  
Jorge muestra su flujo: convierte CVs (Word/PDF/imagen), extrae datos y los envía por webhook a un servidor. El problema aparece cuando ciertos campos (carrera, institución, estado civil, moneda) **no coinciden exactamente con las opciones del servidor**, y el webhook es rechazado.

[04:23] Jorge – Conversión Word → PDF con Google Drive  
Explica cómo resolvió la conversión usando Google Docs cuando los módulos nativos no alcanzaban. Implementó lógica adicional (HTTP + JS) para estandarizar el proceso antes de extraer datos.

[06:28] Franco – Diagnóstico del problema de datos estructurados  
Se confirma que el servidor espera **valores exactos tipo select**. Si el texto no coincide, el sistema falla. Se plantean dos caminos:

- Normalizar los datos antes de enviarlos
- O dejar esos campos vacíos para validación manual posterior

[07:56] Franco – Opción 1: segundo agente para normalización  
Propuesta: usar un **segundo agente** dedicado solo a revisar y corregir campos problemáticos (carrera, institución, etc.), sin tocar el agente principal que ya funciona.

[08:19] Jorge – Volumen y costo de tokens  
Jorge aclara que entran ~1000 CVs al mes, por lo que el uso intensivo de agentes podría elevar costos de tokens.

[12:16] Carlos – Solución avanzada: Vector Store + Reranker  
Carlos propone una solución más robusta:

- Crear un **vector store** con carreras e instituciones
- Usar **metadata** (por área: ingeniería, salud, ciencias, etc.)
- Aplicar un **reranker** para reducir de cientos de opciones a un top 3–10  
Esto minimiza alucinaciones y mejora la precisión.

[14:57] Jorge – Decisión práctica: simplificar  
Aclara que el sistema es un **apoyo al usuario**, no algo crítico. Decide que puede ser mejor **precargar lo seguro y dejar campos dudosos vacíos** para que la persona los complete manualmente.

[16:41] Franco – Validación del enfoque híbrido  
Se valida la decisión: intentar autocompletar solo cuando hay match claro; si no, dejar vacío. Evita complejidad innecesaria y mantiene confiabilidad.

---

[17:53] Henry – Automatización de comprobantes de pago (imágenes)  
Henry muestra un caso con **+1000 imágenes mensuales** de recibos de pago. Quiere extraer campos y generar reportes automáticos, pero la IA no devuelve JSON limpio y “alucina” datos.

[19:39] Franco – Error común: mal uso de system vs user message  
Se detecta que Henry puso todo el prompt en el **user message**. Corrección clave:

- **System message**: reglas, formato, rol, estructura
- **User message**: solo el input variable (imagen/archivo)

[22:46] Franco – Structured Output Parser y errores  
Se revisa el output parser, se reactiva y se detecta que el problema no es técnico sino de **inconsistencia del modelo** al interpretar imágenes.

[27:06] Franco – Insight clave: no todo necesita IA  
Se explica que Henry ya tiene un **código estructurado de 25 dígitos** dentro del “concepto” del comprobante. Para este caso:

- Usar IA es riesgoso (alucinaciones)
- Es mejor **OCR + lógica determinística** (regex, validaciones, longitud exacta, checks)

[33:35] Franco – Arquitectura recomendada (3 pasos)

1. **OCR**: imagen → texto
2. **Extracción / separación** de campos
3. **Normalización** (validación y reglas)  
La IA puede ayudar en algún paso, pero no debe controlar todo el flujo.

[38:51] Franco – Regla general

- IA = más rápida
- Lógica = más robusta y confiable  
Usar IA solo donde aporta valor real.

---

[46:20] Daniel – Caso práctico: extracción robusta con código + IA  
Daniel muestra cómo usa **containers (Docker)** y librerías para extraer información de Word/PDF a JSON limpio. Combina parsing por código con IA solo para enriquecer, logrando alta consistencia.

[54:24] Franco – Conclusión técnica  
Antes de meter un agente IA:

- Preguntarse si se puede resolver con **código, validaciones u OCR**
- La combinación **código + IA** suele ser superior a IA sola

[58:03] Cierre  
Se cierra la sesión, recordatorio de encuentros martes y viernes. Agradecimientos y seguimiento para próximos casos.
