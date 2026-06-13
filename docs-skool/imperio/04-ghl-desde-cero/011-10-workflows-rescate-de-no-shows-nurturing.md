# 🚑 10. Workflows: Rescate de No-Shows & Nurturing

> Ruta: GHL desde Cero › 🚑 10. Workflows: Rescate de No-Shows & Nurturing

**🎬 Vídeo (9.4 min):** https://www.loom.com/share/729c75e2609c40568b0600d1aa4c2c49

---

**Curso: Go High Level Desde Cero · Sección 10 de 12**

> *No los dejes ir sin pelear — pero con empatía, no con reclamos.*

El no-show es el **enemigo silencioso** de cualquier negocio de servicios. Un paciente que agendó y no vino es dinero que se fue, un hueco en la agenda que nadie llenó, y un paciente que probablemente no va a volver por vergüenza o porque simplemente se le olvidó. En esta sección construimos el workflow **más complejo del curso**: una secuencia de rescate en 3 pasos con el tono correcto — empático, no agresivo.

## **📚 Qué vas a aprender**

- Por qué el **tono** importa más que el mensaje
- Workflow 6 — Secuencia de rescate en 3 touchpoints (Día 0, Día 2, Día 7)
- Usar **Task** (tarea interna) para que alguien del equipo llame al paciente
- **Zaman Goal / Exit Goal:** terminar el workflow automáticamente si el paciente reagenda
- Mapa completo de los **6 workflows** que tenemos corriendo

## **🎯 Por qué el tono importa**

Regla de oro antes de construir:

> **El tono debe ser empático, no de cobro.**
> 
> ❌ "No viniste a tu cita, te cobramos..." ❌ "Perdiste tu lugar..."
> 
> ✅ "Vimos que no pudiste venir hoy, ¿está todo bien?" ✅ "Te guardamos un lugar si quieres regresar."

La gente **no vuelve** a un negocio que la hace sentir mal. El objetivo es **abrir la puerta**, no cerrarla.

## **🛠️ Paso a paso**

### **1. Crear el cupón VUELVE15**

Ir a **Payments → Coupons → + Create Coupon**.

- **Nombre:** `VUELVE15`
- **Tipo:** Porcentaje
- **Descuento:** 15%
- **Caducidad:** 7 días (urgencia leve)
- **Aplica a:** producto Limpieza Dental

> 💡 **15% es más que el 10% de cumpleaños** para recuperar un no-show — tiene sentido porque ya hay fricción.

### **2. Crear el workflow**

**Automation → + Create Workflow → Start from Scratch → **`Rescate No-Show`

### **3. Trigger**

**+ Add Trigger → Opportunity → Opportunity Status Change**

- **Pipeline:** Nuevos Pacientes
- **Stage:** No Asistió

Cada vez que alguien mueva una oportunidad a "No Asistió" (manualmente o automáticamente), arranca esta secuencia.

### **4. Día 0 — SMS/WhatsApp empático**

**+ Add → Send WhatsApp → Template → **`no_show_dia0` (Utility)

#### **📋 Plantilla WhatsApp — Día 0 (UTILITY)**

```
Hola {{1}}, notamos que no pudiste asistir a tu cita en Sonrisa Perfecta hoy.

Esperamos que todo esté bien. Si deseas reagendar, puedes hacerlo aquí: {{2}}

Quedamos a tu servicio.
```

- `{{1}}` → first_name
- `{{2}}` → `{{appointment.reschedule_link}}`

> 💡 Fíjate: nada de "no viniste", nada de "perdiste tu cita". El tono es "estamos aquí para ti".

### **5. Día 2 — Crear Task + enviar oferta**

#### **Nodo Wait**

**+ Add → Wait → 2 días**

#### **Nodo Create Task (interno)**

**+ Add → Create/Assign Task**

- **Título:** `Llamar a {{contact.first_name}} para rescatar`
- **Descripción:** `El paciente fue no-show el {{appointment.start_date}}. Favor de llamarlo personalmente para rescate.`
- **Asignado a:** el owner del contacto o tú
- **Due date:** un día después
- **Due time:** 8:00 AM (para que sea lo primero del día)

> 💡 **Por qué un Task aquí:** el Día 2 es el mejor momento para una llamada personal. Que alguien del equipo se comunique directamente tiene más peso que otro mensaje automático.

#### **Nodo Send WhatsApp (Marketing — oferta)**

**+ Add → Send WhatsApp → Template → **`no_show_dia2` (Marketing)

#### **📋 Plantilla WhatsApp — Día 2 (MARKETING)**

```
Hola {{1}}, sabemos que a veces la vida se complica.

En Sonrisa Perfecta sigues siendo prioridad. Te ofrecemos 15% de descuento 
si reagendas esta semana. Código: VUELVE15

Agenda aquí: {{2}}

```

- `{{1}}` → first_name
- `{{2}}` → link del calendario

> ⚠️ Esta plantilla es **marketing** (incluye oferta), más cara que utility, pero vale la pena para recuperar un lead perdido.

### **6. Día 7 — Último intento**

#### **Nodo Wait**

**+ Add → Wait → 5 días** (total 7 desde el no-show)

#### **Nodo Send WhatsApp (Marketing — último intento)**

**+ Add → Send WhatsApp → Template → **`no_show_dia7` (Marketing)

#### **📋 Plantilla WhatsApp — Día 7 (MARKETING)**

```
{{1}}, último recordatorio: tu cita con 15% de descuento (código VUELVE15) 
está disponible hasta el viernes.

Agenda aquí: {{2}}

Si necesitas algo más, estamos para ayudarte.
```

> 💡 **Urgencia leve, no presión.** Ponemos una fecha límite al descuento, pero sin sonar desesperados.

### **7. El truco: Exit Goal (Zaman Goal)**

**¿Qué pasa si el paciente reagenda en el Día 2? No queremos enviar el mensaje del Día 7.**

Solución: **Exit Goal** (también llamado Zaman Goal).

**+ Add Goal → Goal Condition:**

- **Opportunity status changes** → pipeline `Nuevos Pacientes` → stage `Cita Agendada` (o "Confirm")

Cuando se cumpla la condición (el paciente reagendó → la opp vuelve a "Cita Agendada"), el workflow lo **saca automáticamente**, sin importar en qué etapa del rescate esté.

**Config del Goal:**

- Acción: **Remove from workflow**

Así, el paciente que reagenda:

1. Mueve su opportunity a "Cita Agendada"
2. Se dispara el **workflow de confirmación** de la Sección 8 (auto-confirmación)
3. El workflow de rescate lo **saca automáticamente** → deja de molestarlo

**Todo conectado, sin intervención manual.**

### **8. Test en vivo**

1. Ir a **Opportunities** → Carlos Domínguez (oportunidad existente)
2. Cambiar stage a **No Asistió**
3. También cambiar el appointment status a **No Asistió** en Appointments
4. Ir al workflow → **Execution Logs** → ver que entró
5. En el nodo Wait → seleccionar el contacto → **Push to next step** para forzar cada paso y probar sin esperar días

### **Impacto calculado**

Si la recepcionista gastaba **2 horas al día** en confirmaciones, recordatorios y seguimiento manual:

```
2 hr × 5 días = 10 hr/semana
10 hr × 4 semanas = 40 hr/mes
```

**Acabamos de automatizar 40 horas al mes. Para siempre.**

Eso equivale a una persona medio tiempo que ya no necesitas, o medio tiempo que esa persona puede dedicar a **atender mejor** a los pacientes en lugar de perseguirlos por teléfono.

## **🧠 Concepto: Nurturing**

Lo que acabamos de construir tiene un nombre en marketing: **nurturing** — nutrir al lead, cuidarlo, acompañarlo en el proceso.

- No es **vender agresivamente**.
- Es **estar presente** en los momentos correctos con el mensaje correcto.
- Cuando lo automatizas → **imparable**.

## **📎 Recursos**

### **📋 Las 3 plantillas de WhatsApp del rescate (resumen)**

DíaTipoTonoIncluye0UtilityEmpáticoLink reschedule2MarketingOferta + humanoCupón VUELVE15 (15%) + Task interno de llamada7MarketingUrgencia leveDeadline del cupón

### **🎯 Reglas del rescate**

1. **Primer mensaje = empatía pura.** Ninguna oferta. Ningún reclamo.
2. **Segunda oportunidad = valor añadido.** Cupón + llamada personal.
3. **Último intento = urgencia suave.** Deadline claro pero sin presión.
4. **Si reagenda → Exit Goal saca del flujo.** No persigas a alguien que ya volvió.

## **⚠️ Troubleshooting común**

- **El Exit Goal no dispara:** verifica que la condición sea exactamente la etapa correcta. Si el paciente reagenda pero la opp queda en una etapa intermedia, el Goal no se activa.
- **La Task no llega a nadie:** verifica que asignaste owner al contacto o al workflow.
- **Se envían los 3 mensajes al mismo tiempo:** los waits no están configurados en "Since previous action" — revisa el tipo de wait.

## **✅ Checklist antes de avanzar a la Sección 11**

- [ ] Cupón `VUELVE15` creado
- [ ] 3 plantillas WhatsApp del rescate enviadas a aprobación
- [ ] Workflow "Rescate No-Show" activo con los 3 touchpoints
- [ ] Exit Goal configurado (elimina del flujo si reagenda)
- [ ] Task interno en Día 2
- [ ] Test manual completo (cambia oportunidad a No Asistió y verifica secuencia)
- [ ] Los 6 workflows del curso están corriendo y activos

## **➡️ Siguiente sección**

**Sección 11 — AI: Chatbot, AI Studio & Claude Code con MCP.** Tenemos 6 automatizaciones corriendo sin parar. La clínica confirma, recuerda, pide reseñas, felicita cumpleaños, recuerda limpiezas y rescata no-shows — todo sola. Ahora vamos a agregarle un **cerebro**: AI chatbot para la landing, AI Studio para generar contenido, y — para los más avanzados — **Claude Code conectado directamente a GHL vía MCP**.
