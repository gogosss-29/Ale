# 🤖 Agente de WhatsApp que Agenda y Recuerda 24/7

> Ruta: Automatizaciones n8n › 🤖 Agente de WhatsApp que Agenda y Recuerda 24/7

**🎬 Vídeo (246.2 min):** https://www.loom.com/share/0759eadf82c94ff9b10a98806fba1299

**📎 Recursos:**
- PLANTILLA Agente WA
- Mejores Practicas WhatsApp

---

Hoy les traigo la automatización más completa que he construido hasta ahora. Más de 4 horas de grabación. Fue la idea más votada en la comunidad. Voy a etiquetar a Lorena porque ella propuso este tema.

  
Se trata de un **agente de WhatsApp totalmente autónomo para agendar citas**, con memoria, buffer de mensajes, CRM, calendario y control anti-baneo.

Stack completo:

- n8n como orquestador
- Evolution API para WhatsApp
- Redis como buffer de mensajes
- PostgreSQL como memoria larga
- Airtable como base de datos de clientes
- [Cal.com](http://Cal.com) para agendar reuniones
- OpenAI + Gemini como cerebros del agente

El flujo es:  
Cliente escribe por WhatsApp → Mensajes se agrupan en Redis → Se validan con guardrails → Se consulta base de datos → El agente responde → Agenda en [Cal.com](http://Cal.com) → Guarda memoria en Postgres → Actualiza CRM en Airtable.  
Todo 100% automático.

---

## 🔧 Cómo funciona

### 1. Conexión de WhatsApp con Evolution API

- Vinculas tu número vía QR (WhatsApp Business).
- Configuras webhooks de producción en n8n.
- Bloqueas llamadas, grupos y activas sincronización de historial.

![CleanShot 2025-12-04 at 18.57.41.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a615fa586c17463fb5dbd6ba15f1a9802f241c967a7f4719a72eebcc87e221f3-md.png)

---

### 2. Entrada de mensajes en n8n

- Webhook recibe todos los mensajes.
- Filtro `fromMe` evita que el bot se responda a sí mismo.
- Se crea clave en Redis para bloquear auto-respuestas humanas.

![CleanShot 2025-12-04 at 18.58.17.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7672e67967484d2bb19b5c54cacac21cdc285452888542ff963006c2ac128c3d.png)

---

### 3. Buffer de Mensajes con Redis

- Cada mensaje se hace **PUSH** a una lista por número.
- Se espera dinámicamente hasta que el usuario deje de escribir.
- Se consolidan todos los mensajes en uno solo.  
Resultado: el agente recibe *una sola intención limpia*, no 5 mensajes sueltos.

![CleanShot 2025-12-04 at 18.58.41.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/125e831ef151479f981460c4f30bd091972111d87a1e4cc0bfcf9285fe4ab9b2.png)

---

### 4. Soporte Multimodal

- Texto directo.
- Audio → transcripción automática con OpenAI/Gemini.
- Imagen → análisis visual con IA.
- Video → rechazo automático con mensaje humano. ![CleanShot 2025-12-04 at 18.59.08.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9789d95de880447295b7dafdae271090d53cb3d85fc3456f8f7f56d77d25a41d.png)

### 5. Guardrails de Seguridad

Antes de que el mensaje llegue al agente:

- Jailbreak detection
- NSFW detection
- Bloqueo de contraseñas, tokens y datos sensibles
- Respuesta automática segura si algo falla

Esto **reduce baneos y riesgos legales** de forma brutal.

![CleanShot 2025-12-04 at 18.59.36.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/00dc275de857448db03471ecf6ceb9c735a1313dc67a42078f7cf8765028c51c.png)

### 6. Memoria en PostgreSQL

- Se guarda historial completo por teléfono.
- Window de contexto configurable.
- El agente recuerda conversaciones pasadas.

---

### 7. Base de Datos en Airtable

Campos usados:

- Nombre
- Teléfono
- WhatsApp ID
- Status (activo / inactivo)
- Historial
- Último mensaje

El agente crea o actualiza registros automáticamente.

![CleanShot 2025-12-04 at 19.00.14.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3dfe4034210c4640aa461dc0e4f94afed7776d1bfb8f496abd37006b01bce282.png)

---

### 8. Agenda Inteligente con [Cal.com](http://Cal.com)

El agente puede:

- Consultar disponibilidad
- Agendar reuniones
- Reprogramar
- Cancelar

Todo vía API.  
Eventos usados: 30 min y 120 min.  
Confirmación automática por WhatsApp.

![CleanShot 2025-12-04 at 19.01.04.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/18631476b1fa4a87bbca42a85100d3643a716506ad9340a0a5be19a34e8295ee.png)

---

### 9. Control Anti-Baneo

- Delay dinámico entre respuestas.
- Simulación de “escribiendo…”.
- Respuestas humanas ante errores.
- Reglas de uso seguro exactamente como en la infografía que les dejé.

![CleanShot 2025-12-04 at 19.01.25.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/eee33dc3458646b2a661355028cb74122866be70cdd14277af9b7f7b7889bd8f.png)

---

## 🧩 Qué incluye el material del post

- ✅ JSON completo de n8n
- ✅ Plantilla de Airtable [Link](https://airtable.com/appRbt0qoF8pdJXib/shr4ENHz9RaeFyaPP)
- ✅ Configuración de Redis y Postgres
- ✅ Estructura completa del Agente
- ✅ Prompts de sistema listos
- ✅ Flujo de [Cal.com](http://Cal.com)
- ✅ Reglas anti-baneo

Todo listo para **copiar, pegar y adaptar**.

---

## 🚀 Por qué este sistema es tan potente

- Atiende clientes 24/7 por WhatsApp
- Agenda automáticamente sin intervención humana
- Tiene memoria real
- Evita baneos
- Se puede vender como servicio
- Se puede convertir en SaaS
- Escala sin contratar personal

Esto no es un bot simple.  
Esto es **un agente comercial completo en producción**.

![Recomendaciones Whatsapp.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/fe6e23b97fdf4cb3bb0923d820d198fa0ff1ec54b24944cc8c67e74c0c778100-md.png)
