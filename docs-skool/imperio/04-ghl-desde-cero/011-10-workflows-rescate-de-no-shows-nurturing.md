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

## 🎙️ Transcripción

Muy bien, continuemos con las automatizaciones. El no show es el enemigo silencioso de cualquier negocio de servicio. Es un paciente que agendó y no vino, es dinero que se fue, un hueco en la agenda, que nadie lleno y un paciente que probablemente no va a volver por vergüenza o porque simplemente se ha olvidado. En esa sección construimos el workflow más complejo el curso. Una secuencia de rescate en tres pasos que intenta recuperar este paciente con el tono correcto que es empático no agresivo. Al final cerramos todo con una vista panonómica de todas las automataciones construympos. ¿Por qué tono importa? El tono en estos mensajes tiene que ser empático y no de cobro, no le está reclamando al cliente o al paciente caso, el no haber venido. Le estás diciendo, hoy notamos que no pudiste venir. Está todo bien, la gente no vuelve un negocio que las es sentir mal. Así que, manos a la obra. Vamos a crear un nuevo flujo, Starform Scratch y nuestro trigger va a seguir cuando una oportunidad cambia en el pipeline de nuevos pacientes, siempre cuando el stage del pipeline sea no asistió. Esto va a disparar el trigger. Muy bien. Vamos a renombrarlo, a ponerle rescate no show. Nuestro siguiente nodo, vamos a cambiarlo para que sea de estilo, nuestro siguiente nodo va a ser enviar un whatsapp, vamos a ponerle aquí whatsapp, las plantillas, mira, vemos que ya nos notician, nos activaron las plantillas, así que vamos a regresar rápido para acá esta vista, vamos a settings, fue bastante rápido, no pasaron ni dos horas y whatsapp no las aprobó plantillas, de hecho nuevo que es independiente, pendiente, pendiente, pero ya me salen las plantillas, hechitos, no importa, para efectos de esta práctica lo podemos usar. En el caso de la plantilla sería de no show, déjame ver donde tengo o no puedo buscar aquí no show, asign user calendar notification user numbers utility n, por mi tan ser el calendario de notifición de programming confirma asign user dictionary numbers, calendario notification contact one, Pues hay en un formato diferente, no me están saliendo como tal las plantillas y simplemente me están saliendo. No, esto es algo un error del sistema, vamos a volver a darle. Vamos a ponerle free porque la plantilla está en un sancido, validadas. Así que vamos a la plantilla que cree que es un show de acero. Como pueden ver, esta plantilla es de utilidad porque no le estamos ofreciendo nada, simplemente le estamos diciendo que todo bien porque no llegó, así que la pegamos. y estos valores son exclusivos de la plantilla, así que en caso vamos a cambiarlo aquí con contacto first name, vamos a hacer esto un poco más grande y se notamos que no pudiste asistir a tu citado insorriza perfectas, esperamos que todo este bien, si deseas rejendar puedes hacerlo aquí y lo vamos a pasar el appointment for scheduling list y lo mismo deliver on deliver y lo siguiente va a ser día dos, vamos a mandarle una oferta, dice, lo mandamos esto, luego nos esperamos a día dos, vamos a poner aquí un weight de dos días, que es on the liver, algo que no lo hemos visto, pero podremos crear como un task, el task era como que llamar a paciente y confirmar, reajendamiento, Vamos a poner como que, hola, y aquí vamos a poner user, estos untas que la vamos a signar anusuario. El paciente fue un no-show el día y vamos a ponerle aquí a appointment, date, favor de llamarlo para rescatarlo. En ese caso solo soy yo, más sé que me lo voy a signar a mí, y do date, vamos a decirle que sea un día, la hora que sea ocho de la mañana para que sea las primeras cosas y safe patch. Muy bien. Entonces aquí una es que esperamos dos días, vamos a mandarle lo que es un segundo mensaje. El mensaje va a ser de whatsapp, vamos a darle que no el template porque no lo teníamos validados, hacemos esto grande y vamos a copiar ya sería de marketing porque le estamos dando una oferta. Hola, el nombre, sabemos que a veces la vida se complica solo en tal sigues siendo sorprendida que no sorprenden que es por tres cuantos y regendas esta semana. Código vuelve 15, validaste a él, en caso de sería Stone Fields, H.A.V. y Cimito Cupon, agenda aquí, appointment, schedule link, esperamos. Muy bien. Y aquí, vamos a poner otra vez otro wait de dos días, bueno, mejor de cinco días, o sea que sea una semana del todo el inicio y en caso de que esto voy a darle copiar pop action la pego y la rastro y con esto lo puedo hacer bonito y por fin nos da error aquí y de aquí voy a darle pop action from here y pego y se fijó en el pego todo esto y puedo unir robo esto para enlazarlo a mover esto manualmente entonces muy bien vamos a darle ese action para que se active y la de aquí es como un bug del sistema porque si por pie no me deja editarlo así que vamos a cambiar una vista para ver de donde viene el error simplemente el error de vista aquí el whatsapp ok y si después de 5 días es verdad y le puedo cambiar esperar 5 días y vamos a copiar la ultima plantilla y vamos a cambiar la plantilla aquí después de los 5 días muy parecida por la el nombre contact first name vuelve disponible el mismo custom fields fetch havens y me te ocupó, agenda aquí appointment schedule link perfect. Ahora te hubo lo estarás pensando, pero ¿qué pasa si responde el mensaje? Te la vas a ir enviando esto, tenemos una opción que podemos hacer, te les voy a enseñar. La mejor forma de ligar con esto es utilizar acción zaman goal, que básicamente es cuando se cumple subjetivo, que lo queremos hacer, que termine el workflow. No importa en qué parte del flujo estés y se cumple el objetivo, lo van a mandar hasta aquí que es donde termine. Entonces, por ejemplo, aquí vamos a ponerle que, si la pueden ver en status, el limpieza dental es confirm, entonces paramos el workflow, la vamos a safe action. Entonces, no importa en qué etapa esté, si en eso él reace, hace el rescal, la agenda va a cambiar a confirmado y automáticamente lo van a mandar hasta acá, y nada más para que vean podríamos hacer esto como remove from workflow y save action. Entonces en este caso, si responde aquí o aquí o acá, lo va a mandar hasta acá y va a terminar y ya no se lo va a mandar los cincs. Así que vamos a darle publish, vamos a darle save y por lo tanto algo muy importante, si nos vamos aquí a los eventos, Carlos Domínguez, ahorita vamos a hacer el cambio a no show, aquí ustedes lo van a tener que cambiar a no show, para asegurarse que cuando haga la regendamiento, regresa confirmado y se dispara esto y se vaya al goal y lo saque del fluj. Entonces regresamos a oportunidades, vamos a ver Carlos Dominguez, esto que teníamos como ejemplo, vamos a cambiar a no asistir, vamos a abrir esto y en Appointments es importante que lo cambiamos a no asistir, digamos, guardar, ok, que va a ser esto, y nos regresamos a nuestro flujo, nos vamos en Romain History, aquí vemos que se disparo, ok, y nos vamos a Builder, yo estoy en el punto del way, ya se me tuvo que haber mandado mi primer mensaje de WhatsApp, así que vamos para acá, y aquí dice, hola Carlos, notamos que no pusiste a tu estado hoy, en sonrisa perfecta, esperamos que todo este bien, si se arregendar puede hacerlo aquí, quedamos a tu soleno, yo creo que no está mandando el link de regendamiento, pero no pasa nada, vamos para acá y vamos a evaluar el mensaje, appointment, schedule link y vamos a ver qué carlos domingues si tenga el appointment, nos damos calendars, appointment list view, como no os show si es mas carlos domingues, ok, ahorita reviso porque no y regres, listo, regresamos, entonces y se ahorita unas pruebas moviendo la siguiente y ahorita estoy en la parte de esperar 5 días. Muy bien. Entonces en un punto lo que acabamos de construir, tiene un nombre en marketing a manufacturing, que es decir que es nutrir al lit, cuidarlo, acompañarlo en el proceso. No es vender agresivamente estar presente en los momentos correctos con el mensaje correcto. Y eso cuando estás automatizando es imparable. Tenemos entonces seis automataciones escorriendo, sin parar, la clínica confirma, recuerda, pide reseñas, feliciten cumpleaños, recuerda limpiezas y rescata no shows, todo de manera autónoma. Ahora vamos a agregarle un cerebro. En la siguiente sección le ponemos inteligencia artificial, vamos a crear un AI chatbot, ya les enseñé cómo utilizar AI Studio y algo que les va a gustar mucho, les voy a enseñar cómo poder conectar con Cloud Code para que desde Cloud Code ustedes le puedan pedir que haga diferentes cosas y vamos a ver casos de uso prácticamente que nos vemos ahí
