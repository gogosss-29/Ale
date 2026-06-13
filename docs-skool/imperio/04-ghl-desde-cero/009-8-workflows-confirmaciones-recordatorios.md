# 🤖 8. Workflows: Confirmaciones & Recordatorios

> Ruta: GHL desde Cero › 🤖 8. Workflows: Confirmaciones & Recordatorios

**🎬 Vídeo (27.2 min):** https://www.loom.com/share/59628a7f89464e1384397ef422ec1581

---

**Curso: Go High Level Desde Cero · Sección 8 de 12**

> *Tu primer robot trabajando para ti.*

Bienvenido a la parte del curso que cambia todo: **las automatizaciones**. Esto es por lo que GHL es realmente poderoso. En esta sección construimos los 2 primeros workflows — confirmación automática de cita + recordatorio 24h/2h antes — y dejamos a la clínica confirmando y recordando citas **24/7 sin intervención manual**.

## **📚 Qué vas a aprender**

- Qué es un **workflow** (comparado con N8N / Make)
- Anatomía: **Trigger → Acciones → Esperas (Wait) → Condiciones**
- Construir el workflow **"Confirmación de Cita"**
- Construir el workflow **"Recordatorio 24h + 2h antes"**
- Usar **variables dinámicas** (`{{contact.first_name}}`, `{{appointment.start_time}}`)
- Crear **plantillas de email** y **plantillas de WhatsApp** aprobadas por Meta
- Probar workflows con un contacto real (Jorge Rodríguez)

## **🎯 Nota previa: afinación de la landing**

Entre la Sección 6 y esta, ajustamos la landing para que se vea más profesional (CTAs mejor posicionados, sección "Por qué elegirnos", mapa, contacto por WhatsApp). Si tu landing necesita un pulido, es buen momento.

## **🛠️ Paso a paso**

### **1. Entender qué es un workflow**

Un **workflow** = instrucción automatizada. "Si pasa X → haz Y".

Muy similar a N8N o Make, pero integrado nativamente con el CRM, calendario, pagos y canales de GHL.

**Componentes:**

- **Trigger (disparador):** el evento que lo activa (cita creada, contacto creado, opportunity cambió de etapa, etc.)
- **Acciones:** enviar email/SMS/WhatsApp, agregar tag, crear tarea, mover opportunity, etc.
- **Esperas (Wait):** pausar X tiempo antes de la siguiente acción
- **Condiciones (If/Else):** ramificar el flujo

### **2. Desactivar las notificaciones nativas del calendario**

**Antes** de crear el workflow, ir a **Settings → Calendars → [tu calendario] → Edit → Notifications**.

Apagar todas las notificaciones de email, SMS, in-app (los checkboxes deben estar en gris, no verde).

![CleanShot 2026-04-27 at 09.54.53.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/24dbf789c40e4f58b4bdc9b16a68c1891bf595406ecc46038467ba2d7cf19c1d.png)

> 💡 **¿Por qué apagarlas?** Para que las notificaciones vengan únicamente del workflow que vamos a construir. Si las dejas activas, el paciente recibe notificaciones duplicadas.

### **3. Crear el primer workflow — "Confirmación de Cita"**

Ir a **Automation → + Create Workflow → Start from Scratch**.

**Renombrar:** `Confirmación Cita - Limpieza Dental $499`

### **4. Configurar el trigger**

**+ Add Trigger → Appointment → Customer Booked Appointment**

Configuración:

- **Name:** `Cita reservada - Limpieza Dental`
- **Filters:** Calendar = `Limpieza Dental`
- **Invitee:** Contact only (no invitados)

![CleanShot 2026-04-27 at 09.55.27.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/46254e0ffa7744618d9449111d56df70a2a2fa888c404e6d80a3d57f839bb875.png)

> 💡 **Best practice:** siempre agrega el filtro de calendario. Si más adelante creas más calendarios, el workflow no se disparará accidentalmente para todos.

### **5. Cambiar a vista horizontal (opcional)**

Arriba del canvas tienes un toggle **Standard** / **Advanced**.

- **Standard:** flujo vertical (clásico)
- **Advanced:** flujo horizontal, izquierda a derecha, tipo N8N

Recomiendo Advanced si vienes de N8N — es más cómodo para workflows complejos.

![CleanShot 2026-04-27 at 09.55.48.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/66c606d8075b43bd86bd1206ed0c72a9072eeabe7f70419ab37ce11649f72c96.png)

### **6. Acción 1 — Email de confirmación**

**+ Add Action → Send Email**

- **From name:** dejar vacío (usa el default de Email Services)
- **From email:** dejar vacío
- **Subject:** `Tu cita en Sonrisa Perfecta está confirmada, {{contact.first_name}}`
- **Preview text:** `Detalles de tu cita y link para reagendar`
- **Body:** elegir **Select Template** → crear una nueva plantilla (ver paso 7)

### **7. Crear plantilla de email**

Ir (en otra pestaña) a **Marketing → Email → Templates → + Create Template → Plain Text Editor**.

> ⚠️ **Regla de oro:** para emails transaccionales (confirmaciones, recordatorios) usa **texto plano**, NO diseño visual con imágenes. Los correos transaccionales con muchas imágenes tienden a caer en SPAM.

**Nombre de la plantilla:** `Confirmación cita dental`

#### **📋 Plantilla — Email de confirmación**

```
Hola {{contact.first_name}},

Tu cita en Clínica Dental Sonrisa Perfecta está confirmada:

📅 Fecha: {{appointment.start_time}}
📍 Dirección: {{company.address}}

Te pedimos llegar 10 minutos antes para tu registro.

Si necesitas reagendar, puedes hacerlo aquí:
{{appointment.reschedule_link}}

¡Te esperamos!
— Equipo Sonrisa Perfecta

```

Guardar. Volver al workflow y seleccionarla.

### **8. Acción 2 — Plantilla de WhatsApp (utilidad)**

WhatsApp **solo permite iniciar conversación con plantillas aprobadas por Meta**. Hay que crearla primero.

Ir a **Settings → WhatsApp → Templates → + Create Template → Blank Template**.

Configuración:

- **Nombre:** `confirmacion_cita`
- **Tipo:** Utility (transaccional)
- **Idioma:** Español (México)
- **Encabezado:** Texto → `Sonrisa Perfecta - Cita confirmada`

#### **📋 Plantilla — WhatsApp de confirmación**

```
Hola {{1}}, tu cita en Sonrisa Perfecta está confirmada para {{2}}.

Te esperamos. Para reagendar: {{3}}

```

Variables (al crear la plantilla GHL te pide ejemplos):

- `{{1}}` → nombre del contacto (ej: Jorge)
- `{{2}}` → fecha/hora de la cita (ej: martes 21 de abril a las 11 AM)
- `{{3}}` → link de reagendamiento (ej: [https://clinicasonrisaperfecta.site/reschedule](https://clinicasonrisaperfecta.site/reschedule))

Submit a Meta → aprobación tarda **entre minutos y 24-72 horas**.

### **9. Acción 3 — Agregar tag**

**+ Add Action → Add Contact Tag → **`cita-agendada`

> 💡 Si la tag no existe, el campo te deja crearla al escribirla.

Esta tag servirá para filtros y reportes más adelante.

### **10. Publicar y probar**

Guardar → **Publish**.

Para probar:

- Agendar una cita desde el funnel (como hicimos en la Sección 6/7) con un contacto de prueba, ej. **Jorge Rodríguez**.
- Ir a **Automation → [workflow] → Execution Logs**
- Ver que el trigger se disparó, el email se envió, la tag se agregó.

### **11. Workflow 2 — "Recordatorio de Cita"**

Volver a **Automation → + Create Workflow → Start from Scratch**.

Aquí vamos a usar **AI** para acelerar: **Create with AI** y escribir el prompt:

> 📋 Prompt — Create Workflow AI
> 
> "Quiero crear una automatización cuando haya una nueva cita confirmada. Definir la fecha de la cita, esperar 24 horas y enviar un correo de confirmación si la cita sigue activa (opportunity status = confirm). Luego esperar 2 horas antes de la cita y enviar un segundo correo Y una plantilla de WhatsApp."

La IA genera el esqueleto del workflow automáticamente. Después lo revisamos y ajustamos manualmente.

#### **Ajustes manuales al workflow generado por IA**

**Trigger:** `Customer Booked Appointment` con filtro calendario = Limpieza Dental.

**Nodo 1 — Set Appointment Date:** usa el campo `{{appointment.start_date}}`. Sirve de referencia para los waits siguientes.

**Nodo 2 — Wait 24h antes de la cita:**

- **Wait Type:** Wait until specific date/time
- **Base:** Appointment start date (del contacto)
- **Offset:** -24 horas
- **Si ya pasó esa fecha:** Next Step (skip)

**Nodo 3 — Send Email (24h antes):**

#### **📋 Plantilla — Email recordatorio 24h**

```
Asunto: Mañana es tu cita, {{contact.first_name}} 🦷

Hola {{contact.first_name}},

Te recordamos que mañana tienes cita en Sonrisa Perfecta:

📅 {{appointment.start_time}}
📍 {{company.address}}

Tips para tu visita:
• Llega 10 minutos antes
• Trae tu identificación
• Si tomaste algún medicamento, avísanos

¿Necesitas reagendar? {{appointment.reschedule_link}}

¡Nos vemos mañana!
— Equipo Sonrisa Perfecta

```

**Nodo 4 — Wait 2h antes de la cita:** mismo esquema, offset `-2 horas`.

**Nodo 5 — Send SMS/WhatsApp (2h antes):**

#### **📋 Plantilla — SMS/WhatsApp recordatorio 2h**

```
{{contact.first_name}}, te recordamos tu cita HOY a las {{appointment.start_time_only}} en Sonrisa Perfecta. Te esperamos 📍 {{company.address}}

```

> 💡 **Copy-paste de nodos:** click derecho sobre un nodo → **Copy Action** → pegar. Útil para replicar estructura similar.

### **12. Test en vivo con Jorge Rodríguez**

- Agendar una cita mañana a las 10 AM
- **Execution Logs** → ver el primer workflow disparado (confirmación)
- Esperar el wait del segundo workflow o **forzar manualmente** (click en el contacto en el wait → Push to next step)
- Verificar que llegaron: email de confirmación, email 24h antes, SMS/WhatsApp 2h antes

## **📎 Recursos**

### **📋 Variables más usadas en workflows**

```
{{contact.first_name}}
{{contact.last_name}}
{{contact.email}}
{{contact.phone}}

{{appointment.start_time}}         — fecha + hora completa
{{appointment.start_time_only}}    — solo la hora
{{appointment.start_date}}         — solo la fecha (para condiciones/waits)
{{appointment.reschedule_link}}
{{appointment.cancel_link}}

{{company.name}}
{{company.address}}
{{company.phone}}
```

### **🎯 Regla de oro de workflows**

**SIEMPRE haz un test antes de activar en producción.**

- Crea un contacto "Test Jorge"
- Dispara el trigger manualmente o con una cita real
- Verifica que lleguen todos los mensajes en los tiempos correctos
- Revisa el **Execution Log** para confirmar que no haya errores

### **⚡ Upgrade avanzado (opcional)**

En vez del SMS 2 horas antes, conecta un **agente de voz** de GHL que marque al paciente:

> "Hola {{contact.first_name}}, soy el asistente de Sonrisa Perfecta. Te marco para recordarte que tu cita es en una hora. ¿Ya vienes en camino? Presiona 1 para confirmar, 2 para reagendar."

Esto reduce aún más los no-shows.

## **⚠️ Troubleshooting común**

- **Plantilla de WhatsApp no se aprueba:** revisa que el tono sea transaccional (no marketing). Una plantilla que diga "Aprovecha 10% de descuento" no se aprueba como utility — tiene que ir como **marketing** (más caras).
- **El email no se envía:** verifica que el dominio de email esté verificado (Sección 3) y que el template esté seleccionado en el nodo.
- **Wait se dispara inmediatamente:** el offset está mal configurado. Revisa que `start_date` venga del contacto, no de la fecha actual.

## **✅ Checklist antes de avanzar a la Sección 9**

- [ ] Workflow "Confirmación Cita" activo y probado
- [ ] Workflow "Recordatorio 24h + 2h" activo y probado
- [ ] Plantilla de email de confirmación creada
- [ ] Plantilla de email de recordatorio 24h creada
- [ ] Plantilla de WhatsApp `confirmacion_cita` enviada a aprobación
- [ ] Tag `cita-agendada` creada
- [ ] Al menos un test real con Jorge Rodríguez (o contacto de prueba)

## **➡️ Siguiente sección**

**Sección 9 — Workflows: Reseñas, Cumpleaños & Fidelización.** Acabamos de automatizar el **antes** de la cita. Ahora vamos con el **después**: pedir reseñas de Google automáticamente, felicitar cumpleaños con cupón y recordar limpiezas semestrales. Estas son las automatizaciones que convierten un paciente de una visita en un cliente de por vida.
