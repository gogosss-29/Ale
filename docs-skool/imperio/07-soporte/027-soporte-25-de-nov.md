# Soporte - 25 de Nov

> Ruta: 🛠️ Soporte › Soporte - 25 de Nov

**🎬 Vídeo (58.5 min):** https://www.youtube.com/watch?v=zLBRpEMRUfI

---

En esta sesión se aclaran errores comunes en flujos de video IA, duplicación de mensajes en WhatsApp, gestión correcta de timestamps, creación de contactos en ManyChat vía API y buenas prácticas para usar WhatsApp Business sin bloqueos. También se revisa cómo elegir entre Business y API según el volumen del negocio.

---

# **Intervenciones (orden cronológico)**

**[****00:01****] Fran – Apertura de la sesión**  
Presentación del propósito: resolver obstáculos técnicos, dudas de Make, WhatsApp, IA y automatizaciones. Invitación a levantar la mano y trabajar casos reales de los miembros.

---

**[****01:32****] Jorge – Video UGC generado estirado (resolución incorrecta)**  
Muestra un flujo replicado del sistema UGC de Benja. El video generado aparece alargado.  
**Solución:** revisar resolución del módulo GPT/Sora; usar 720×1280 o 720×1080; evitar imágenes de entrada deformadas; probar el modo "maintain proportion"; validar que el error no provenga del módulo de resize. Se confirma que la causa era la imagen original deformada.

---

**[****16:01****] Ale – Flujo de WhatsApp con Wapi y problema de mensajes duplicados**  
Duplicación al agrupar mensajes por timestamp.  
**Solución:** revisar routers iniciales (no estaban filtrando nada), validar que solo exista un registro activo por usuario, y añadir filtro para "no respondido" en el módulo de búsqueda en Sheets. Ajustes de tiempo (10 segundos) y buenas prácticas para evitar ejecuciones múltiples.

---

**[****17:06****] Cristian – Ruta visual estilo Uber para app propia**  
Busca dibujar rutas dinámicas con actualizaciones en tiempo real dentro de su propia app.  
**Solución:** se confirma que no existe experiencia interna con renderizado avanzado de rutas; recomendación explorar APIs de Google (Directions + Polylines). Se sugiere compartir avances en la comunidad para obtener apoyo.

---

**[****21:36****] Ale – Seguimiento automático por WhatsApp y riesgos de outbound**  
Pregunta si es seguro enviar recordatorios automáticos días después.  
**Solución:**

- Con Wapi (WhatsApp Business) sí se puede, pero es **riesgo moderado**.
- Recomendación: espaciar mensajes con delays variables para evitar patrones.
- Para riesgo cero → usar **API oficial (WhatsApp Cloud / ManyChat)**.
- Alternativa: usar un número separado solo para outbound.

---

**[****37:58****] Raimundo – Cómo migrar empresas a WhatsApp API sin perder el número**  
Problema: al pasar un número a API (Twilio) queda inactivo semanas.  
**Solución:**

- Fran recomienda **no usar Twilio** para WhatsApp API.
- Usar **ManyChat**, que activa la API en minutos si la cuenta está en orden.
- Para empresas pequeñas (200 clientes/mes), mantener **WhatsApp Business + Evolution API** es suficiente y más simple.
- Migraciones completas a API solo si es estrictamente necesario.

---

**[****43:36****] Raimundo (parte 2) – Evolution y envío de audios/typing simulation**  
Pregunta si Evolution permite mensajes tipo “tap to play” y simulación de escritura.  
**Solución:** Sí, Evolution soporta audios nativos, videos y simulación de typing.

---

**[****47:18****] Jorge – Crear suscriptores en ManyChat vía Make (error 400)**  
Intento fallido al crear contacto por módulo nativo de Make.  
**Solución:**

- Revisar formato del teléfono (regex fallando).
- Reemplazar regex con un nodo GPT para normalizar el número.
- Si el módulo falla igualmente: usar **HTTP Request** con el endpoint de creación de usuarios.
- Fran comparte estructura del request y campos obligatorios (incluye opt-in).

---

**[****58:07****] Cierre**  
Fran agradece y recuerda nueva sesión el viernes. Se invita a seguir iterando en flujos más estables y soluciones limpias para WhatsApp + Make + IA.
