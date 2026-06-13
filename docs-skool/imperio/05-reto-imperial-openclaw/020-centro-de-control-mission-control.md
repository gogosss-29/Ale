# 🖥️ Centro de Control (Mission Control)

> Ruta: 🦞 Reto Imperial OpenClaw › 🖥️ Centro de Control (Mission Control)

---

Ya tienes el Gran Consejo (o al menos dos consejeros) trabajando entre sí. Ahora vamos a construir el **panel de mando**: un dashboard visual desde donde monitorear todo en tiempo real, sin tener que abrir Supabase ni leer logs.

## Por qué necesitas un dashboard

- **Visibilidad inmediata.** Saber, de un vistazo, qué consejero está activo, qué tareas están en curso y cuáles están bloqueadas.
- **Decisiones más rápidas.** Cuando todo lo importante está a la vista, dejas de "interrogar" al sistema y pasas a actuar sobre él.
- **Confianza.** Si delegas tareas reales en un equipo de agentes, necesitas poder mirarlos trabajar.

---

## Stack recomendado

Como todos los datos del Gran Consejo ya viven en **Supabase**, lo único que falta es conectar una capa visual encima.

### Opción A — Lovable *(rápido, sin programar)*

[Lovable](https://lovable.dev/) te permite generar interfaces visuales conectadas a Supabase en minutos, describiendo lo que quieres ver. Ideal si no quieres meterte a programar.

### Opción B — Claude Code *(más control, más poder)*

Si quieres una app totalmente personalizada, levanta un proyecto con Claude Code (o tu IDE de IA preferido) y deploya en Vercel. Te da control total del diseño, los gráficos y la lógica.

---

## Qué visualizar como mínimo

- **Estado de cada consejero**: idle, active, busy, blocked, último heartbeat.
- **Tablero kanban de tareas**: backlog, in_progress, done, blocked.
- **Notificaciones recientes** y bandeja pendiente de cada consejero.
- **Standup del día**: el reporte que genera el Canciller cada mañana.
- **Actividad reciente**: quién hizo qué en las últimas 24 horas.

## Plan de acción

1. Define las 4-5 vistas que más te servirían a ti (no las que se ven bonitas, las que de verdad usarías).
2. Elige Lovable o Claude Code según tu nivel de comodidad.
3. Conéctalo a Supabase con permisos **solo de lectura** al inicio.
4. Solo agrega permisos de escritura (cancelar tarea, reasignar, etc.) cuando ya viste cómo se comporta.

## Resultado esperado al cerrar esta lección

- Dashboard accesible desde tu navegador (en Vercel o Lovable).
- Conectado a Supabase en lectura.
- Las 4-5 vistas mínimas funcionando.
- Probado con datos reales de tus consejeros.
