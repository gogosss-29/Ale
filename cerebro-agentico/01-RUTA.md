# Ruta de ejecución — de curso a sistemas agénticos propios

> Ruta propuesta para el objetivo de Alexander: **sistemas agénticos independientes
> que trabajen 24/7**. Sale del propio curso (ruta "quiero construir": A → B → …,
> ficha `categorias/sistemas-agenticos.md`) adaptada a lo que Alexander ya tiene
> (Claude Code funcionando, proyecto avatar, consultora Cerebro).
>
> **Protocolo:** al ejecutar cada fase, abrir las lecciones reales del curso
> (capa 2) — no trabajar solo de memoria ni de los resúmenes. Fidelidad ante todo
> (ver `docs-skool/imperio/AGENTS.md`).

## Marco del curso (lo que no cambia)
- **Automatizar = Input → Output, Trigger → Acción.** Detectar el problema
  repetitivo correcto vale más que la herramienta.
- **Agente ≠ chatbot:** loop + contexto + memoria + herramientas, proactivo 24/7.
- **El arnés importa más que el modelo.**
- **Skills = SOPs digitales** que se acumulan como ventaja competitiva.
- **Framework SOUL:** Setup (que te conozca) → Orquestar (herramientas) →
  Unificar (canales) → Libertad (heartbeat + cron).

## Fase 0 — Fundamentos ✅ (ya cubierta)
La capa curada de `docs-skool/imperio/` está leída. Mentalidad: cursos 01 y 19
si hace falta repasar.

## Fase 1 — Dominar el motor: Claude Code a fondo
**Curso:** `02-claude-code/` (36 lecciones; el vídeo maestro de 3 h es la espina).
**Qué sacar:** CLAUDE.md, Skills, MCP, hooks, sub-agentes, context management,
sesiones, Playwright.
**Entregable:** un primer proyecto piloto real de Alexander construido con el
método del curso (candidatos: automatizar algo de la consultora Cerebro o del
pipeline del avatar — decidir juntos).

## Fase 2 — Primer agente autónomo 24/7 (OpenClaw)
**Curso:** `05-reto-imperial-openclaw/` (27 lecciones) + lecciones Hermes en
`02`/`06`.
**Qué sacar:** desplegar un agente en VPS (~$5/mes Hostinger) o local, con
Tailscale (seguridad obligatoria), Telegram como canal, memoria persistente,
backups a GitHub, heartbeat + cron.
**Entregable:** UN agente vivo que trabaje para Alexander mientras duerme
(ej.: resumen matutino, vigilancia de tareas, contenido).

## Fase 3 — Multi-agente: el "Gran Consejo"
**Curso:** lecciones del Gran Consejo (en `02`/`05`).
**Qué sacar:** coordinador (Canciller) que delega + agentes especializados,
memoria compartida en Supabase, actividad visible en Discord, Mission Control.
**Entregable:** equipo de 2-4 agentes coordinados para un dominio concreto
(consultora / contenido / avatar).

## Fase 4 — Flujos de soporte (n8n) — en paralelo, según necesidad
**Cursos:** `09-n8n-desde-0/`, `12-automatizaciones-n8n/`, `13-agentes-de-whatsapp/`.
Para lo que es flujo puro (webhooks, CRM, WhatsApp) n8n sigue siendo la pieza justa.

## Fase 5 — Monetizar (opcional, cuando el sistema funcione)
**Cursos:** `16-como-vender-automatizaciones/`, `18-crea-conecta-convierte/`,
`17-biblioteca-de-prompts/` (valor inmediato, texto puro).
Convertir lo construido en oferta: la consultora Cerebro ya es el vehículo natural.

## Reglas de trabajo entre sesiones
1. Cada sesión empieza leyendo `CLAUDE.md` → `cerebro-agentico/00-ESTADO.md`.
2. Cada avance se registra en `00-ESTADO.md` y se committea. Git es la memoria.
3. Lo construido se codifica como **skill** (`.claude/skills/`) cuando sea
   repetible — así el "cómo" queda ejecutable, no solo documentado.
