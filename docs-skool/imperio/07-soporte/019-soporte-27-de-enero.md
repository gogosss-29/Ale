# Soporte - 27 de Enero

> Ruta: 🛠️ Soporte › Soporte - 27 de Enero

**🎬 Vídeo (59.8 min):** https://www.youtube.com/watch?v=KSAK3eFjoKc

---

## Problemas que resuelve la sesión

Cómo pasar de usar plantillas copiadas a diseñar **sistemas de automatización escalables**, cómo estructurar agentes con memoria real sin errores comunes, cómo integrar WhatsApp de forma estable sin bloqueos y cómo pensar la automatización como un producto modular que se puede vender y replicar en distintos clientes.

---

## [00:53] Posimi – De automatizar “por automatizar” a diagnosticar primero

**Problema**  
Muchos proveedores intentan implementar IA y automatizaciones sin entender el negocio, generando fricción, errores o incluso rompiendo procesos existentes.

**Solución**  
Se propone un **diagnóstico pago** como primer paso:

- Auditoría completa del negocio
- Identificación de procesos automatizables reales
- Evaluación de riesgos (incluida ciberseguridad)
- Definición de qué automatizar y qué no  
Resultado: más valor percibido, más autoridad y menos errores técnicos.

---

### [08:19] Javier – Uso de plantillas sin claridad de arquitectura

**Problema**  
Seguir plantillas sin entender el “por qué” del flujo genera bloqueos, confusión y sistemas difíciles de mantener.

**Solución**  
Se valida la estructura general, pero se enfatiza:

- Entender cada nodo antes de copiarlo
- Separar entrada, procesamiento y respuesta
- Pensar el flujo como un sistema, no como un parche  
La plantilla sirve como guía, no como solución final.

---

### [13:55] Franco – Memoria inestable en agentes de N8N

**Problema**  
La memoria simple de N8N:

- Se traba
- No escala
- Genera inconsistencias en conversaciones largas

**Solución**  
Implementar **memoria persistente con Supabase + Postgres**:

- Mayor estabilidad
- Persistencia real
- Mejor manejo de contexto  
Se explica paso a paso cómo crear credenciales y conectar correctamente.

---

### [20:48] Eventos erróneos en Evolution (WhatsApp)

**Problema**  
Eventos que se disparan sin lógica clara (historias de WhatsApp activando agentes), generando mensajes no deseados.

**Solución**  
No es un problema de actualización, sino de conexión:

- Resetear instancias
- Eliminar configuraciones fantasmas
- Aplicar filtros defensivos  
Conclusión: Evolution puede fallar silenciosamente si no se controla.

---

### [25:53] Daniel – Automatizaciones no escalables para múltiples clientes

**Problema**  
Crear soluciones únicas por cliente limita el crecimiento y obliga a rehacer todo desde cero.

**Solución**  
Pensar el sistema como **bloques tipo LEGO**:

- Funcionalidades activables/desactivables
- Un core común
- Configuración por cliente  
Resultado: el mismo sistema se vende varias veces con mínimos ajustes.

---

### [31:15] Franco – Agentes duplicados y prompts rígidos

**Problema**  
Tener un agente distinto por cliente o por caso genera:

- Más mantenimiento
- Más errores
- Menos escalabilidad

**Solución**  
Prompts dinámicos desde base de datos:

- Un solo agente
- Comportamiento variable según datos
- Configuración por cliente (ej. ramas legales)  
Escalabilidad real sin duplicar flujos.

---

### [37:20] Daniel – Sobrecargar a la IA con información innecesaria

**Problema**  
Pasar grandes volúmenes de datos al modelo genera:

- Lentitud
- Respuestas imprecisas
- Mayor costo

**Solución**  
Consultar por **ID y estados específicos**:

- JSON estructurado
- Bases de datos vivas
- IA solo interpreta, no busca  
Menos carga, más precisión.

---

### [47:30] Carlos – Bloqueos y riesgos en WhatsApp no oficial

**Problema**  
WhatsApp es crítico para los clientes. Perder una cuenta implica:

- Pérdida de ventas
- Caos operativo
- Daño al negocio

**Solución**  
Uso de **WhatsApp Cloud (WCloud)**:

- Partner oficial de Meta
- Sin emulación humana
- Mensajes asincrónicos
- Coexistencia con WhatsApp Business  
Más estabilidad, menos riesgo.

---

### [56:00] Flujo final con WCloud + Airtable + N8N

**Problema**  
Flujos largos, complejos y frágiles usando herramientas no oficiales.

**Solución**  
Arquitectura simplificada:

- Validación de número
- Envío de plantilla oficial
- Apertura de conversación
- Gestión desde N8N  
Menos nodos, más control, mayor confiabilidad.

---

### [59:30] Cierre

**Aprendizaje central**  
No se trata de automatizar más, sino de **automatizar mejor**:

- Diagnóstico primero
- Lógica antes que IA
- Sistemas antes que flujos
- Oficial antes que improvisado
