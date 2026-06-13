# 💚 9. Workflows: Reseñas, Cumples & Fidelización

> Ruta: GHL desde Cero › 💚 9. Workflows: Reseñas, Cumples & Fidelización

**🎬 Vídeo (16.5 min):** https://www.loom.com/share/7b58410f311f40669526758b17ab645e

---

# **Workflows: Reseñas, Cumpleaños & Fidelización**

**Curso: Go High Level Desde Cero · Sección 9 de 12**

> *El paciente que regresa vale 10 veces más que el nuevo.*

Los workflows de la sección anterior resuelven el **antes** de la cita. Ahora vamos con el **después** — donde la mayoría de los negocios pierden dinero sin saberlo. Construimos 3 automatizaciones que convierten un paciente de una sola visita en un cliente de por vida: reseña post-cita, felicitación de cumpleaños con cupón y recordatorio semestral.

## **📚 Qué vas a aprender**

- Crear un **cupón** de descuento dentro de GHL (`CUMPLE10`)
- Diferenciar plantillas de WhatsApp **utility** vs. **marketing**
- Workflow 3 — Solicitar **reseña de Google** 2h después del servicio
- Workflow 4 — **Felicitación de cumpleaños** con cupón
- Workflow 5 — **Recordatorio de limpieza semestral** (genera revenue pasivo)

## **🛠️ Paso a paso**

### **1. Crear el cupón CUMPLE10**

Ir a **Payments → Coupons → + Create Coupon**.

- **Nombre:** `CUMPLE10`
- **Código:** `CUMPLE10` (mayúsculas)
- **Tipo:** Porcentaje
- **Descuento:** 10%
- **Inicio:** hoy
- **Caducidad:** sin expiración
- **Aplica a:** producto `Limpieza Dental`
- **Uso por cliente:** ilimitado

![CleanShot 2026-04-27 at 10.03.37.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6090bd3879504880877b8fdeea82bcec103dca7a4cee4733be81a421544334e8.png)

### **2. Utility vs. Marketing templates en WhatsApp**

Antes de los workflows, entender la diferencia:

UtilityMarketingMensaje transaccionalMensaje promocionalConfirmar/recordar/actualizarOfertas, descuentos, promos**Más barato**Substancialmente más caroRequiere interacción previa del clientePermite iniciar conversación

> ⚠️ **Cuidado:** si Meta detecta que estás enviando plantillas de marketing como utility, **te penaliza** y cambia TODAS tus plantillas a marketing (precios más altos).

**Regla práctica:**

- "Tu cita está confirmada" → **utility** ✅
- "Agenda tu limpieza esta semana con 10% de descuento" → **marketing** ✅
- "Gracias por tu visita, déjanos una reseña" → **utility** ✅ (no mencionas promo)
- "Reseñanos y te damos 10% de descuento" → **marketing** ❌ (y va contra políticas de Google)

> 💡 **Nunca ofrezcas descuentos a cambio de reseñas en Google.** Viola las políticas de Google y te pueden bajar todas las reseñas.

### **3. Crear las plantillas de WhatsApp (ahora o mientras esperas aprobaciones)**

Ir a **Settings → WhatsApp → Templates → + Create Template**.

#### **📋 Plantilla WhatsApp — Solicitud de reseña (UTILITY)**

```
Hola {{1}}, gracias por tu visita hoy en Sonrisa Perfecta.

Si tu experiencia fue buena, nos ayudaría mucho una reseña en Google 
(toma 30 segundos): {{2}}

¡Gracias!

```

- `{{1}}` → first_name
- `{{2}}` → link de Google Reviews

#### **📋 Plantilla WhatsApp — Cumpleaños (MARKETING)**

```
¡Feliz cumpleaños, {{1}}! 🎂

En Sonrisa Perfecta queremos celebrar contigo. Agenda tu próxima visita 
esta semana y obtén 10% de descuento con el código CUMPLE10.

Agenda aquí: {{2}}
```

- `{{1}}` → first_name
- `{{2}}` → link del calendario

#### **📋 Plantilla WhatsApp — Limpieza semestral (MARKETING)**

```
Hola {{1}}, ha pasado medio año desde tu última limpieza en Sonrisa Perfecta.

Es momento de agendar tu revisión preventiva. Una limpieza cada 6 meses 
previene caries y problemas mayores.

Agenda aquí: {{2}}
```

### **4. Workflow 3 — Solicitud de reseña de Google**

**Automation → + Create Workflow → Start from Scratch → **`Reseña de Google`

#### **Trigger**

**+ Add Trigger → Opportunity → Opportunity Status Change**

- **Pipeline:** Nuevos Pacientes
- **Stage:** Cliente Ganado

> 💡 Cuando mueves manualmente (o automáticamente) una oportunidad a "Cliente Ganado", se dispara.

#### **Acción 1 — Wait 2 horas**

**+ Add → Wait → 2 hours**

> 💡 **Por qué 2 horas:** que el paciente ya salió de la clínica, tuvo tiempo de llegar a casa, procesar la visita. No pidas reseña mientras aún está en la sala de espera.

#### **Acción 2 — Send WhatsApp**

**+ Add → Send WhatsApp → Template → **`solicitud_resena`

Llenar variables:

- `{{1}}` → `{{contact.first_name}}`
- `{{2}}` → `{{custom_value.google_review_link}}` (crear este custom value con el link real del Business Profile)

#### **Acción 3 — Tag + Retry opcional**

**+ Add → If/Else → Delivered?**

- **Si sí:** add tag `review-solicitada`
- **Si no:** wait 1 día, intentar 1 vez más, luego terminar

![CleanShot 2026-04-27 at 10.05.05.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8a0d00a327604e5194700cb0d2a8f685613fbfadd79a4773a7e5549a647c9628.png)

**Publish.**

### **5. Workflow 4 — Felicitación de cumpleaños**

**Automation → + Create Workflow → Start from Scratch → **`Cumpleaños`

#### **Trigger**

**+ Add Trigger → Contact → Birthday Reminder**

- **Día:** 0 (el día del cumpleaños)

#### **Acción — Send WhatsApp (o SMS como fallback)**

**Send WhatsApp → Template → **`felicitacion_cumpleanos`

Llenar variables:

- `{{1}}` → `{{contact.first_name}}`
- `{{2}}` → link del calendario (custom value o hard-coded)

**Publish.**

> 💡 **¿Tiempo de envío?** Puedes agregar un delay inicial para que se envíe a las 10am (no a medianoche). Usa **Wait until specific time of day**.

### **6. Workflow 5 — Recordatorio de limpieza semestral**

**Automation → + Create Workflow → Start from Scratch → **`Limpieza Semestral`

#### **Trigger**

**+ Add Trigger → Opportunity Status Change → Pipeline "Nuevos Pacientes" → Stage "Cliente Ganado"**

Igual que el de reseñas, pero con distinta acción.

#### **Acción 1 — Wait 6 meses**

**+ Add → Wait → 180 días** (o "6 months")

> 💡 Este es el wait más largo del curso. El sistema literalmente espera 6 meses.

#### **Acción 2 — Send WhatsApp (plantilla limpieza semestral)**

Ver plantilla arriba.

#### **Acción 3 — If/Else — ¿El contacto respondió?**

- **Si **`contact_reply = true`: terminar (ya está en conversación, escalar a humano)
- **Si **`contact_reply = false`: enviar un segundo mensaje de follow-up 3 días después

#### **📋 Plantilla — Follow-up limpieza**

```
Hola {{contact.first_name}}, sabemos que es fácil que el tiempo se pase.

Si quieres agendar tu revisión preventiva (y evitar problemas mayores 
a futuro), aquí te dejamos el link directo: [LINK CALENDARIO]

Te esperamos 😊
```

**Publish.**

### **7. Probar los 3 workflows**

#### **Probar reseña de Google**

1. Crear oportunidad para "Carlos Domínguez" (o tú)
2. Moverla manualmente a **Cliente Ganado**
3. Automation → [workflow Reseña] → **Execution Logs** → verificar que entró
4. Manualmente empujar desde el nodo Wait → siguiente paso
5. Verificar que llegó el WhatsApp

#### **Probar cumpleaños**

1. Cambiar la fecha de cumpleaños de tu contacto a **hoy**
2. El trigger se dispara una vez al día — para test manual, ir a **[workflow] → Run For Selected Contact** → seleccionar tu contacto

#### **Probar limpieza semestral**

1. Crear oportunidad nueva para el contacto
2. Moverla a "Cliente Ganado"
3. Empujar manualmente desde el wait de 6 meses al siguiente nodo

> 💡 **Truco:** GHL te permite **seleccionar el contacto en el wait y empujarlo manualmente** para probar sin esperar el tiempo real. Es la mejor herramienta de debugging para workflows.

### **8. Recordatorio — Un contacto puede tener múltiples oportunidades**

Como vimos en la Sección 5, un mismo contacto puede tener varias oportunidades activas simultáneamente:

Al crear la segunda oportunidad, GHL te preguntará **"¿Enable duplicate?"** — responde **sí**. Esto permite que el workflow de reseña/limpieza semestral se dispare por cada tratamiento, no solo una vez por paciente.

## **📎 Recursos**

### **🎯 Los 3 workflows de esta sección (resumen)**

#NombreTriggerWaitAcción3Reseña GoogleOpp. Status = Cliente Ganado2hWhatsApp con link review4CumpleañosBirthday Reminder—WhatsApp con cupón CUMPLE105Limpieza SemestralOpp. Status = Cliente Ganado6 mesesWhatsApp con link calendario + follow-up

### **📋 Plantilla — SMS equivalente (por si WhatsApp no está aprobado)**

**SMS Reseña:**

```
Hola {{contact.first_name}}, gracias por visitarnos. ¿Te gustó la experiencia? Déjanos una reseña (30 seg): [LINK] ⭐
```

**SMS Cumpleaños:**

```
¡Feliz cumpleaños {{contact.first_name}}! 🎂 En Sonrisa Perfecta te regalamos 10% con código CUMPLE10. Agenda: [LINK]
```

**SMS Limpieza semestral:**

```
{{contact.first_name}}, hace 6 meses que no te vemos. Tu sonrisa necesita una revisión. Agenda aquí: [LINK] 😊

```

### **💰 ¿Por qué estos workflows generan revenue pasivo?**

- **Reseñas:** cada reseña nueva mejora el ranking local en Google → más leads orgánicos. **Cero costo marginal.**
- **Cumpleaños:** el cupón trae de vuelta a clientes dormidos — al menos 15-20% convierte.
- **Limpieza semestral:** es el más potente. Cada paciente que atendiste hoy tiene un recordatorio automático en 6 meses. **Multiplica eso por cientos de pacientes al año**.

## **⚠️ Troubleshooting común**

- **No puedo seleccionar la plantilla de WhatsApp:** aún no está aprobada por Meta. Espera 24-72h y vuelve a intentar.
- **Workflow de cumpleaños no se dispara:** el campo `Date of Birth` del contacto debe estar lleno. Si usas una fecha sin año, GHL puede tener problemas — usa año completo (ej: 1990-04-22).
- **Reseña llega vacía:** el custom value `google_review_link` no está configurado. Créalo en Settings → Custom Values → agrega la URL completa del link de reseña de tu Google Business Profile.

## **✅ Checklist antes de avanzar a la Sección 10**

- [ ] Cupón `CUMPLE10` creado
- [ ] 3 plantillas de WhatsApp enviadas a aprobación (reseña / cumpleaños / limpieza)
- [ ] Workflow "Reseña de Google" activo
- [ ] Workflow "Cumpleaños" activo
- [ ] Workflow "Limpieza Semestral" activo
- [ ] Al menos 1 test manual de cada workflow

## **➡️ Siguiente sección**

**Sección 10 — Workflows: Rescate de No-Shows & Nurturing.** Ya tenemos 5 workflows corriendo 24/7, pero hay un escenario que todavía no resolvimos: el paciente que **agendó y no vino**. En la siguiente sección construimos el workflow más complejo del curso — una secuencia de rescate en 3 pasos con tono empático que intenta recuperar ese paciente antes de que se pierda.
