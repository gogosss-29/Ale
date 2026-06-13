# Cómo escalar automatizaciones sin romper flujos

> Ruta: 🔴 Grabaciones › Cómo escalar automatizaciones sin romper flujos

**🎬 Vídeo (55.5 min):** https://www.youtube.com/watch?v=3Iqn15W6XZo

---

## Problemas que resuelve

Cómo manejar envíos masivos sin bloquear cuentas de email, cómo configurar correctamente nodos y community nodes en N8N, cómo evitar errores comunes en webhooks y respuestas HTTP, cómo elegir entre Make y N8N según volumen de operaciones y cómo diseñar agentes simples que no fallen por tiempos de espera o mala arquitectura.

---

## 🧠 Intervenciones

---

### [00:00] Franco – Introducción y dinámica de la sesión

Explica el formato de preguntas y respuestas de los viernes, enfocado en resolver obstáculos reales de implementación, dudas técnicas y casos concretos que los participantes están desarrollando.

---

### [01:03] Jorge – Envío masivo de emails desde N8N para ofertas laborales

Presenta una plataforma con más de 100.000 currículums. Busca enviar emails automáticos a perfiles que coincidan con nuevas ofertas laborales.

**Problema**  
Enviar grandes volúmenes de correos directamente desde Gmail puede:

- Bloquear la cuenta
- Romper límites de envío
- Generar problemas de reputación

**Solución**  
No usar Gmail para envíos masivos.  
Utilizar servicios de envío especializados (marketing o transactional email) integrados a N8N mediante API. Se sugiere evaluar alternativas a Mailchimp por costo y usar servicios enfocados solo en envío, que protegen la cuenta de correo.

---

### [04:59] Daniel – Diferencia entre transactional email y marketing email

Aclara la diferencia conceptual entre tipos de emails.

**Problema**  
Confundir envíos operativos con campañas de marketing genera bloqueos y mala configuración legal y técnica.

**Solución**

- Transactional: notificaciones, avisos, acciones puntuales
- Marketing: campañas, newsletters  
Recomienda servicios económicos con alto volumen mensual que se integran fácilmente a N8N y evitan problemas con Gmail.

---

### [07:42] Tomás – Nodos de Evolution API que desaparecen al importar workflows

Explica que al migrar de una cuenta de prueba a una cuenta paga de N8N, los nodos de Evolution API no aparecen.

**Problema**  
Los workflows importados muestran nodos “no instalados” porque faltan community nodes.

**Solución**  
Instalar los **Community Nodes** en la nueva cuenta.  
Eliminar el workflow importado incorrectamente e importar nuevamente el JSON una vez instalados los nodos. No es un problema de configuración de Evolution, sino de instalación de nodos.

---

### [12:10] Carlos – Uso de un solo proyecto en Easy Panel

Aclara dudas sobre usar múltiples servicios (Evolution, Chatwoot, Postgres, Redis) dentro de un mismo proyecto.

**Problema**  
Creer que cada servicio requiere un proyecto separado genera complejidad innecesaria.

**Solución**  
Se puede usar un solo proyecto sin problemas.  
Recomendaciones:

- Separar tablas en Postgres
- No reutilizar las mismas tablas de Redis
- Considerar limpieza periódica de memoria para evitar acumulación de datos

---

### [14:59] Gabriel – Error en automatización de Instagram DMs con Make y ChatGPT

Presenta una automatización donde MiniChat envía mensajes a Make, pero no recibe respuesta del modelo.

**Problema**  
El flujo usa nodos HTTP incorrectos y no devuelve respuesta al webhook, por lo que MiniChat queda sin output.

**Solución**  
Usar **Webhook Response** en lugar de HTTP Request.  
Mapear correctamente el resultado del completion y devolver un status 200 con el body adecuado. Se corrige el flujo en vivo y se explica cómo funcionan los webhooks que esperan respuesta.

---

### [19:12] Franco – Explicación técnica de webhooks y tiempos de espera

Explica el comportamiento de servicios que esperan respuesta (como MiniChat).

**Problema**  
Si el flujo tarda más de 10 segundos, la plataforma corta la comunicación.

**Solución**

- Flujos simples funcionan bien
- Agentes complejos no deben depender de respuesta inmediata  
Se recomienda otra arquitectura para sistemas más pesados.

---

### [33:06] Gabriel – Escalabilidad, calificación de leads y uso de IA

Describe su objetivo de calificar leads desde Instagram y automatizar agenda y postventa.

**Problema**  
Make cobra por operación, lo que vuelve inviable un flujo con alto volumen de mensajes.

**Solución**  
Migrar a **N8N**:

- No cobra por operación
- Más flexible
- Mejor para agentes complejos y alto tráfico

---

### [38:42] Franco – Comparación Make vs N8N

**Problema**  
Usar Make para flujos con muchas interacciones genera costos altos.

**Solución**  
Make para flujos simples y bajo volumen.  
N8N para:

- Alto volumen
- Agentes de IA
- Sistemas escalables

---

### [45:05] Consulta sobre productos vendibles para empezar

Un participante consulta qué tipo de producto vender con conocimientos básicos de chatbots.

**Problema**  
No saber por dónde empezar ni cómo escalar.

**Solución**  
Crear un producto simple, replicable y confiable:

- Agente calificador
- Chatbot de atención básica  
Luego escalar funcionalidades y precio. El valor está en resolver dolores recurrentes, no en la herramienta.

---

### [49:23] Franco – Estrategia de producto y escalabilidad

Explica la diferencia entre solución y dolor.

**Solución**  
Una solución bien diseñada puede atacar múltiples dolores en un mismo nicho. Recomienda crear una base sólida y luego iterar con el mismo cliente.

---

### [52:15] Consulta sobre plataformas para chatbots

**Solución**  
Los agentes pueden construirse en Make o N8N.  
Se recomienda N8N por costo, flexibilidad y escalabilidad.  
Aclara la diferencia entre chatbots tradicionales y agentes de IA modernos.

---

### [53:18] José / Carlos – Uso de herramientas externas para redes sociales

Consulta sobre una herramienta para publicar en redes integrada a N8N.

**Solución**  
Se confirma que es confiable, económica y que existe un community node funcional para N8N, probado en Instagram sin inconvenientes.

---

### [54:02] Franco – Anuncio de próxima sesión especial

Anticipa una sesión enfocada en ventas y consultoría:

- Cómo vender
- Cómo preguntar
- Cómo detectar oportunidades  
Se anunciará oficialmente en la comunidad.

---

### [55:00] Cierre

Franco cierra la sesión, recuerda la dinámica de martes y viernes, invita a estar atentos a la comunidad y despide a los participantes.
