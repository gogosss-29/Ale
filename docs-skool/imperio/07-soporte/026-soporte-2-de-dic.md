# Soporte - 2 de Dic

> Ruta: 🛠️ Soporte › Soporte - 2 de Dic

**🎬 Vídeo (57.6 min):** https://www.youtube.com/watch?v=8V2LpIZTsaw

---

## **Problemas que resuelve:**

Cómo estructurar automatizaciones reales con WhatsApp (Business, Meta API y Evolution), cuándo usar lógica vs IA, cómo evitar bloqueos al enviar mensajes, cómo integrar audio de ElevenLabs, y cómo diseñar flujos seguros para pedidos, reservas y sistemas de cotización.

---

# **Resumen cronológico de intervenciones**

### **[****02:05****] Ale – Envío de 30–40 mensajes diarios y tiempos aleatorios**

**Problema:** Necesita mandar mensajes por WhatsApp Business en rangos horarios sin que parezcan automatizados.  
**Solución:** Fran recomienda usar *slips aleatorios* entre 3 y 6 minutos, evitando repeticiones fijas. Ajustar el primer slip a 200–240 segundos para abrir rango, y aplicar la función random de Make para variación real.

---

### **[****07:10****] Ale – Problemas con etiquetas en Wapi**

**Problema:** Wapi no detecta etiquetas agregadas manualmente, pero sí las aplicadas por la automatización.  
**Solución:** Ya existen fallas conocidas con etiquetas manuales. Alternativas:

- Detectar cambios por mensaje enviado por humano vs bot usando diferencias en payload del webhook.
- Aplicar "handoff" automático cuando el usuario humano envía un mensaje.

---

### **[****10:48****] Ale – Cómo identificar mensajes enviados por humano vs bot en Wapi**

**Problema:** Quiere que el sistema detecte cuándo un humano responde para detener la IA.  
**Solución:**  
Comparar payload del webhook cuando:

1. el bot responde,
2. el humano envía mensaje.  
Luego aplicar un **router** para cambiar de modo IA ↔ humano con una etiqueta o un estado en base de datos.  
Si ambos mensajes entregan la misma estructura, no es posible diferenciar.

---

### **[****13:30****] Ale – Notificaciones internas para el restaurante**

**Problema:** Quiere que suene el teléfono cuando llega una notificación.  
**Soluciones recomendadas:**

1. Usar dos WhatsApp en el mismo teléfono (Business + personal).
2. Crear un número extra con Wapi/Evolution para reenviarse notificaciones con un emoji detonador.
3. Mandar avisos a un grupo donde un bot responda para activar sonido.

---

### **[****17:00****] Ale – Flujo ideal para quitar mando a IA sin etiquetas**

**Solución:**

- Detectar diferencias de payload y automatizar el “handoff” sin intervención manual.
- Con Evolution API es más simple porque distingue mejor mensajes enviados por dispositivo.

---

### **[****21:04****] Ale – ¿Puede la IA calcular precios?**

**Problema:** Tiene un menú con múltiples variaciones (ej. hamburguesas, extras).  
**Conclusión de Fran:** **Nunca delegar cálculos sensibles a IA.**  
**Solución:**

- Que la IA solo cargue datos.
- El precio final debe venir de un Excel, tabla o lógica.
- Crear un subworkflow tipo "CalcularPrecio" que recibe ingredientes → consulta base → devuelve precio.  
La IA no hace matemáticas, solo envía datos estructurados.

---

### **[****28:05****] Ale – Cómo estructurar agentes con sub-flujos**

**Solución:**  
Crear un agente principal con un *tool* que llame a un subworkflow:  
IA Principal → Subworkflow (Carga datos + Excel + cálculo) → Retorna precio.  
La IA solo ve una herramienta “obtener precio”, no las operaciones internas.

---

### **[****29:01****] Raimundo – Enviar audio de ElevenLabs a WhatsApp con Evolution API**

**Problema:** Error 500/400 al hacer POST del archivo.  
**Solución:**

- Revisar token y headers.
- Asegurar `Content-Type: application/json`.
- Enviar número en `number`.
- Usar `audio` como field.
- Probar primero enviar un mensaje de texto simple para confirmar autenticación.  
El fallo probablemente está en el archivo o formato, no en la API.

---

### **[****45:10****] Mauricio – Envío automático de 5,000 mensajes para rifas**

**Problema:** Enviar masivamente con WhatsApp sin ser bloqueado.  
**Advertencia de Fran:**

- WhatsApp Business y Meta API te pueden bloquear por volumen anómalo.
- Meta API exige documentos legales.  
**Solución:**
- Hacer que **los usuarios inicien la conversación** para evitar costos y bloqueos.
- Alternativa segura: usar SMS con Twilio.

---

### **[****53:33****] Julián – Integración de Chatwoot con Instagram**

**Problema:** No encuentra opción de conectar Instagram a Chatwoot.  
**Solución:**  
La función aparece como “futura” en muchas instalaciones. Algunos miembros lo han logrado, pero depende de versión y configuración del server. Recomendación: consultar a Carlos (mencionado en comunidad), quien ya lo implementó.

---

### **[****56:02****] Cierre de sesión**

Fran recuerda:

- Los martes se resuelven casos uno a uno.
- Los viernes se profundiza en un tema (agentes de IA, WhatsApp, Make, auditorías).
- Recomienda usar la plantilla de agentes IA recientemente subida y el tutorial de levantar Evolution API en 3 minutos.
