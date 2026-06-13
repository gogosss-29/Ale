# Evolution API vs YCloud

> Ruta: 🔴 Grabaciones › Evolution API vs YCloud

**🎬 Vídeo (56.7 min):** https://www.youtube.com/watch?v=OnGBKQWs6YM

---

**Problemas que resuelve:** Cómo migrar de Evolution API a Whitecloud ante los bloqueos de Meta, cómo funciona el método de coexistencia para no perder capacidades de WhatsApp Business, y cómo conectar múltiples números de clientes a N8N desde una sola cuenta de Whitecloud.

---

**Intervenciones**

**[00:00] Franco – Contexto: por qué Evolution API está fallando** Explica que Meta comenzó a bloquear conexiones no oficiales usadas por servicios como Evolution API y Wapi. Describe que la agencia llegó a tener 50 números conectados y tuvo que iniciar una migración controlada. Introduce Whitecloud como alternativa estable basada en la API oficial de Meta.

**[04:00] Franco – Qué es el método de coexistencia** Explica que la coexistencia permite tener WhatsApp Business en el celular y la API oficial activa al mismo tiempo. A diferencia de antes, no se pierde acceso al celular. Se pueden mandar mensajes masivos, recibir webhooks y operar por N8N sin sacrificar las funciones del teléfono.

**[10:00] Franco – Qué no soporta la API en coexistencia** Detalla las limitaciones: no se pueden gestionar grupos desde la API, no funcionan mensajes que desaparecen, localizaciones en vivo ni llamadas. Todo lo que no soporta la API sigue disponible desde el celular. Caso real: un cliente perdió la función de mandar mensajes a grupos al migrar.

**[13:00] Franco – Cómo funciona el sistema de plantillas (templates)** Para iniciar conversaciones con usuarios nuevos o después de 24 horas sin respuesta, se requiere una plantilla aprobada por Meta, que tiene costo. Una vez que el usuario responde, se abre una ventana de conversación libre de 24 horas desde el último mensaje del cliente.

**[29:00] Carlos – Extensión a 72 horas con campañas pagas** Aporta que si el usuario llega desde una campaña de Meta con link a WhatsApp, la ventana de conversación se extiende a 72 horas. El primer mensaje tiene un tratamiento diferente y debe manejarse de forma especial en el flujo.

**[30:00] Franco – Costos de mensajes según país** Muestra la calculadora de precios de Whitecloud. Los costos varían por país y tipo de mensaje. Ejemplo: 100 mensajes de marketing a Argentina cuestan más que a México. Los mensajes de notificación cuestan aproximadamente un 30% de los de marketing.

**[32:00] Franco – Cómo conectar Whitecloud a N8N con múltiples clientes** Problema: Whitecloud solo permite un webhook por cuenta, no por número. Solución: recibir todo en un solo webhook y usar una tabla en Supabase que mapea número de teléfono → webhook del cliente. N8N reenvía el mensaje al flujo correcto según el número. Recomienda Supabase sobre Airtable por velocidad y límites.

**[40:00] Carlos – Alternativa por cliente: cuenta propia de Whitecloud** Comenta que en su caso cada cliente tiene su propia cuenta de Whitecloud, lo que elimina el problema del webhook único. Franco explica que en su agencia optaron por centralizar todo para facilitar el desarrollo, cobrando una mensualidad que cubre los costos.

**[42:00] Franco – Uso del nodo Execution Data en N8N para debugging** Muestra cómo usar este nodo para guardar el número de usuario, tipo de evento y dirección del mensaje (entrante/saliente). Permite filtrar ejecuciones por número de teléfono y debugar problemas de clientes específicos de forma mucho más eficiente.

**[45:00] Tomás – Cómo usar Whitecloud para envíos masivos y conversaciones** Consulta si puede usar el agente de WhatsApp para mandar cold messages y luego tener conversaciones automáticas. Franco explica que para envíos masivos solo se necesita un nodo HTTP con la plantilla, no un agente. El agente entra cuando hay respuesta y se quiere continuar la conversación. Recomienda empezar solo con el envío y agregar el agente en una segunda etapa.

**[50:00] Carlos – Send Message vs Enqueue Message** Plantea la diferencia entre mandar el mensaje directamente (send message directly) versus enviarlo al servidor de Meta para que él lo procese (enqueue message). La segunda opción permite reintentos automáticos si falla y gestiona los estados de enviado/leído. Franco reconoce que no lo habían probado y lo deja como punto a explorar.

**[54:00] Carlos – Cómo usar la documentación de Whitecloud para construir requests** Comparte que la API Reference de Whitecloud permite construir el request completo con parámetros, testearlo en vivo y copiar el CURL resultante. En N8N se puede pegar directamente con "Import CURL" y queda configurado. Caso de uso: envío automático de PDF de pago vía WhatsApp cuando un cliente confirma un pago.

**[56:30] Cierre – Franco** Resume la sesión destacando la migración de Evolution a Whitecloud como respuesta a los bloqueos de Meta, el valor del método de coexistencia y los puntos técnicos clave para conectar múltiples clientes. Cierra invitando a continuar el martes.
