# 🎭 Roles, canales y memoria

> Ruta: 🦞 Reto Imperial OpenClaw › 🎭 Roles, canales y memoria

---

Esta lección entra al detalle del Gran Consejo: quiénes son los consejeros, cómo se hablan entre ellos, cada cuánto se despiertan y dónde guardan información.

## Roles propuestos

Empieza con dos consejeros (Canciller + uno más) y crece desde ahí. La regla es la misma de la lección del primer caso de uso: pocos consejeros, bien hechos.

- **Canciller** — Coordinador general. Único punto de contacto contigo. Asigna tareas al resto, revisa correo y calendario, hace briefings diarios.
- **Estratega** — Inteligencia y análisis. Investiga tendencias, analiza competencia y métricas, propone movimientos. Útil para contenido, redes y producto.
- **Embajador** — Comunicación y comunidad. Patrulla foros y redes, da bienvenida a nuevos miembros, responde preguntas frecuentes con la voz de la marca.
- **Cronista** — Contenido y newsletter. Redacta newsletters, transcribe ideas, prepara borradores de posts y guiones, investiga noticias relevantes.

---

## Canales de comunicación entre consejeros

El equipo se coordina por **tres canales**, cada uno con un propósito distinto:

1. `sessions_send` → mensaje directo entre agentes. Inmediato pero no persistente: si el agente está dormido cuando llega, se pierde.
2. **Notificaciones en Supabase** → cola persistente. Sobrevive reinicios. Cada agente revisa su bandeja al despertar. Tipos típicos: `task_assigned`, `help_requested`, `task_completed`, `info`.
3. **Canal **`#gran-consejo` en Discord → coordinación visible. Cada consejero tiene su propia cuenta de Discord; tú ves todo en tiempo real.

---

## Heartbeats por consejero

Cada agente tiene su propio ritmo:

- **Canciller:** cada 7 minutos.
- **Embajador:** cada 30 minutos.
- **Cronista:** cada 30 min + CronJob diario a las 9 AM.
- **Estratega:** configurable según tu carga.

En cada heartbeat el consejero:

1. Actualiza su "último visto" en Supabase.
2. Revisa notificaciones pendientes.
3. Consulta su dashboard de tareas.
4. Ejecuta lo que toque.

---

## Ciclo de vida de una tarea

`inbox` → `in_progress` → `done`

- Si se traba → pide ayuda → vuelve a `in_progress`.
- Tareas sin asignar → quedan en `backlog`.
- Prioridades: `urgent` > `high` > `medium` > `low`.

**Flujo típico:**

1. Se crea la tarea en Supabase (manual o automáticamente).
2. Se asigna a un consejero y se le notifica.
3. El consejero trabaja y deja comentarios con avances.
4. Al terminar, marca la tarea como `done`, deja un comentario con el resultado y un *deliverable* si aplica.
5. Notifica al Canciller, que revisa y reporta.

> 📌 **Regla de oro:** el resultado de una tarea siempre va como comentario. Si no hay comentario con el resultado, la tarea no se considera terminada.

---

## Memoria de cada consejero

Cada agente tiene su propio workspace (ej. `/workspace-cronista/`) con:

- `SOUL.md` → personalidad y tono del consejero.
- `MEMORY.md` → memoria a largo plazo, curada.
- `memory/YYYY-MM-DD.md` → notas diarias en bruto.
- `HEARTBEAT.md` → checklist que ejecuta en cada latido.
- `TOOLS.md` → notas locales, credenciales (con cuidado) y configuraciones específicas.

> 🔒 La memoria de cada consejero es independiente. **No comparten archivos entre sí**: para eso está Supabase.

---

## Tablas Supabase clave

A nivel resumen, estas son las tablas que vas a necesitar:

- `agents` → registro de cada consejero, su rol, estado y `last_seen_at`.
- `tasks` → el kanban del equipo (status, priority, tags, asignación).
- `subtasks` → desglose de tareas grandes.
- `comments` → discusión vinculada a cada tarea.
- `notifications` → cola persistente de mensajes entre consejeros.
- `knowledge` → base de conocimiento compartida.
- `activity_log` → auditoría de quién hizo qué.
- `standups` → reportes diarios generados por el Canciller.
- `deliverables` → entregables (documentos, análisis, código, reportes).
