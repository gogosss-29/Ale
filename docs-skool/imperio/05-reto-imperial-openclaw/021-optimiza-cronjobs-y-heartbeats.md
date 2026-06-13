# 💙 Optimiza CronJobs y HeartBeats

> Ruta: 🦞 Reto Imperial OpenClaw › 💙 Optimiza CronJobs y HeartBeats

---

A esta altura del módulo ya tienes un sistema multi-agente con dashboard y backups. Es muy probable que **estés gastando más recursos de los necesarios**. Hoy vamos a auditar y a optimizar.

## El problema típico

Los conceptos de **CronJob** y **HeartBeat** son fáciles de confundir, y por eso muchos sistemas terminan con:

- Heartbeats demasiado frecuentes que queman tokens sin necesidad.
- CronJobs que disparan tareas redundantes.
- Acciones programadas que ya nadie usa pero siguen ejecutándose.
- Consejeros del Gran Consejo "despertándose" mucho más seguido de lo necesario.

Resultado: la cuenta de la API se infla, el VPS trabaja más de lo que debería y la calidad de las respuestas baja por exceso de contexto.

---

## Plan de auditoría

### Paso 1 — Refresca la teoría

Pásale a tu agente este documento de la documentación oficial y pídele que te explique con tus palabras la diferencia exacta entre CronJob y HeartBeat:

📖 [docs.openclaw.ai/automation/cron-vs-heartbeat](http://docs.openclaw.ai/automation/cron-vs-heartbeat)

### Paso 2 — Pídele que se audite a sí mismo

Pídele al Canciller (o al agente principal si todavía no escalaste a multi-agente) que te dé:

- La lista completa de CronJobs configurados, con su frecuencia y la última vez que se ejecutaron.
- La frecuencia de HeartBeat de cada consejero.
- Para cada uno, una recomendación de si está bien, si puede bajar de frecuencia o si se puede eliminar.

### Paso 3 — Aplica los cambios uno por uno

No optimices todo de golpe. Cambia una cosa, observa 24 horas, ajusta. Algunas preguntas guía:

- ¿Necesito que el Canciller despierte cada 7 minutos, o cada 15 minutos sería suficiente?
- ¿El CronJob diario realmente entrega valor todos los días, o sería mejor cada 3 días?
- ¿Hay tareas programadas que ya no uso?

---

## Resultado esperado al cerrar esta lección

- CronJobs y HeartBeats entendidos a nivel concepto.
- Lista completa auditada y depurada.
- Frecuencias optimizadas según tu uso real.
- Costo mensual de la API bajando (o al menos no subiendo).

> ⚡ **Tip Imperial:** ponle al Canciller un CronJob mensual que vuelva a hacer esta auditoría sola. Lo que no se mide se descontrola.
