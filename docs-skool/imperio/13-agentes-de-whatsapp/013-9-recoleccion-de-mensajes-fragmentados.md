# 🔄 9. Recolección de mensajes fragmentados

> Ruta: Agentes de WhatsApp › 🔄 9. Recolección de mensajes fragmentados

**🎬 Vídeo (5.9 min):** https://www.loom.com/share/a54887e7ef0c4c5b9327fc62f4aa6812

---

En este módulo resolvemos un problema muy común en WhatsApp: los usuarios escriben en varios mensajes seguidos. Si tu agente procesara cada uno por separado, perdería contexto y las respuestas serían incoherentes.

Este bloque evita eso agrupando los mensajes fragmentados antes de enviarlos a la IA. Lo que para el usuario son 3, 5 o 10 mensajes escritos rápido, para el modelo se convierte en un único mensaje claro y coherente.

---

### **Cómo funciona**

Cada vez que llega un mensaje:

1. El sistema revisa cuánto pasó desde el mensaje anterior del mismo usuario.  
Si son solo unos segundos, se considera parte de la misma idea.
2. El mensaje se guarda en la tabla **messageBuffer**, registrando: - ID del usuario
- Texto recibido
- Fecha y hora
- Estado (pendiente o procesado)
3. Mientras el usuario sigue escribiendo, el agente no responde todavía; solo acumula.
4. Cuando pasa el tiempo límite sin nuevos mensajes, el sistema: - Une todos los fragmentos
- Forma un único *input* limpio
- Marca la conversación como lista para procesar

Así, la IA recibe algo como:

> “Hola Benja, tengo una duda.  
> Estoy tratando de conectar mi base de Airtable con Make, pero no se me actualiza el estado.  
> Te paso un ejemplo…”

Y no cinco mensajes independientes que cortarían la coherencia.

---

### **Por qué importa tanto**

Este módulo mejora de forma directa:

- La coherencia de las respuestas
- La experiencia del usuario
- La calidad del contexto entregado a la IA
- La estabilidad del flujo completo

También evita problemas como:

- Responder antes de que el usuario termine
- Cortar ideas a la mitad
- Mensajes fuera de orden
- Conversaciones que se sienten “rotas”

---

### **Qué aporta este módulo**

- Un sistema que entiende cómo escriben las personas, no cómo deberían escribir.
- Un agente que espera, escucha y unifica antes de responder.
- La base para conversaciones más naturales, largas y fluidas.

En resumen: convierte escritura humana desordenada en *dato limpio*, para que tu agente responda con la mayor claridad y precisión posible.
