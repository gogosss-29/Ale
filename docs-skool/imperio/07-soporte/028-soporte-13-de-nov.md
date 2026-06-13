# Soporte - 13 de Nov

> Ruta: 🛠️ Soporte › Soporte - 13 de Nov

**🎬 Vídeo (59.0 min):** https://youtu.be/KqEfjIUrb-I

---

**Título:** Cómo corregir alucinaciones en IA, usar lógica antes que IA y elegir herramientas reales para WhatsApp e interfaces  
**Fecha:** 13 de noviembre 2025

**Problemas que resuelve:**  
Cómo evitar alucinaciones cuando la IA procesa datos cero, cómo decidir cuándo usar lógica o IA en flujos reales, cómo reducir latencia en asistentes de voz y cómo elegir entre WhatsApp Business, API, ManyChat, Kommo o Chatwood para armar interfaces con clientes.

---

## **Intervenciones**

**[****00:00****] Inicio – Sesión íntima para profundizar en casos reales**  
Franco abre la reunión explicando que al ser pocos se pueden revisar problemas a fondo y probar enfoques distintos.

---

**[****00:38****] Juan Felipe – Sistema de reportes para clínica odontológica**  
Describe su proyecto: digitalizar 13 planillas que antes eran manuales, guardar datos en Airtable y usar IA para generar informes automáticos.  
Problema: cuando un conteo da cero, la IA alucina valores como -3, 5 o 10.  
Solución: Franco explica que el error se genera porque la IA recibe el “0” como si fuera un dato significativo. Recomienda filtrar antes con lógica.

**Solución técnica:**  
• Insertar un filtro entre la herramienta y el agente IA,  
• Ignorar campos con cero,  
• Enviar al modelo solo planillas con datos reales.

Juan confirma que lo implementará y que eso resolverá las alucinaciones.

---

**[****10:33****] Javier – Primeros pasos, proyectos potenciales en una mueblería**  
Comparte que está terminando Make y quiere crear:  
• Un cotizador basado en inventario real.  
• Un agente de WhatsApp para pedidos.  
Franco aclara que debe separar lógica:  
• Productos ya fabricados, consulta directa del dato.  
• Productos a medida, cotización con parámetros.  
Recomendación: usar lógica siempre que sea posible para mantener estabilidad.

---

**[****14:50****] Javier – Pregunta sobre manejo de herramientas del cliente**  
Duda sobre si usar Airtable del cliente o de la agencia.  
Franco: recomienda alojar en la infraestructura propia de la agencia, por facilidad de control y calidad del servicio.

---

**[****16:22****] Raúl – Asistente de voz que no finaliza llamadas**  
Problema: la llamada se queda en silencio o se corta por timeout.  
Franco analiza en vivo el agente de voz: detecta latencia de 2 segundos, muy alta.  
Ajustes aplicados:  
• Cambiar modelo de voz.  
• Activar modo de baja latencia.  
• Reducir streaming delays.  
• Cambiar transcriber a Deepgram.  
Resultado: latencia baja de ~1800 ms a ~600 ms.  
Prueba pendiente: testear con micrófono limpio y red estable.

---

**[****34:03****] Raúl – Recomendación final**  
Sugiere probar desde número real, no tester, para validar comportamiento real del asistente.

---

**[****34:09****] Ale – Automatización para restaurante y dudas sobre interfaz humana**  
Ale quiere permitir que el dueño del local intervenga cuando el agente necesita ayuda.  
Busca unir WhatsApp e Instagram en una sola bandeja.

Franco explica diferencias:  
• ManyChat: soporta WhatsApp e Instagram, fácil de conectar, pero caro por contactos.  
• Chatwood: excelente para WhatsApp Business, funciona bien como inbox, pero no tiene Instagram.  
• Kommo: no recomendado para esto.

Recomendación:  
• Si el negocio usa WhatsApp Business, basta usar WhatsApp Business + automatización.  
• Para multicanal, ManyChat es la opción más práctica.

---

**[****43:59****] Ale – Cómo devolver respuestas desde Make**  
Franco explica que Kommo no espera respuestas de webhooks, por lo que se requiere:

1. Recibir mensaje, enviarlo a Make,
2. Guardar respuesta en Airtable,
3. Esperar,
4. ManyChat o Kommo obtiene el resultado y responde.  
Misma lógica que con ManyChat.

---

**[****51:03****] Ale – WhatsApp sin interfaz**  
Franco: usar WhatsApp Business directamente es suficiente para muchos negocios.  
Ventaja: cero costos, cero curva de aprendizaje, fácil intervención humana.

---

**[****53:02****] Jorge – Consulta sobre qué aprender de marketing para vender automatizaciones**  
Quiere vender servicios sin hacer un curso entero de marketing.  
Franco explica:  
• El mejor marketing es un buen producto funcionando.  
• Empieza implementando automatizaciones gratis a conocidos para ganar casos reales.  
• La estrategia de marketing del cliente la define el experto en marketing, no tú.  
• Tú te encargas de procesos y sistemas.  
• Apuntar siempre a un dolor específico de un nicho concreto funciona mejor que aprender marketing completo.

---

**[****57:35****] Cierre de la sesión**  
Franco reafirma que cada caso necesita diagnóstico y lógica antes que IA.  
Invita a actualizar avances en la comunidad y recuerda que la próxima sesión será el viernes.
