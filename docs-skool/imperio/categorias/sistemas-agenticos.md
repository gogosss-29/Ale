# Sistemas Agénticos — ficha ampliada

> Profundización de la **categoría B** del [índice](../INDICE-POR-CATEGORIA.md): qué son
> los sistemas agénticos según Imperio Digital, qué construyes y el resultado al
> aplicarlo. Basado en el **Reto Imperial OpenClaw** (27 lecciones), el curso **Hermes
> 2026** (4,5 h), las lecciones agénticas de **Claude Code/Vibe-Coding** y el **Motor
> Agéntico**.

## Qué es (y qué NO es)
Un **sistema agéntico** no es un chatbot. Un chatbot **responde** cuando le hablas; un
**agente** tiene un *loop* propio, **memoria persistente**, **herramientas** y trabaja
**de forma proactiva 24/7** — aunque no lo estés mirando. La diferencia clave de
**OpenClaw**: cuando no puede hacer algo, **se crea las herramientas** para lograrlo
(instala librerías, conecta APIs, toma el navegador).

**El marco mental — las 4 eras de la automatización (de Imperio):**
1. **No-code visual** → Make
2. **Low-code híbrido** → n8n
3. **Agentes autónomos** → Claude Code, OpenClaw, Antigravity
4. **OpenClaw/Hermes** = la capa siguiente: un agente que vive en *tu* servidor, te
   conoce, se conecta a tus apps y trabaja por ti.

> El valor ya no está en saber *cómo* se implementa, sino en saber *qué* poner a
> trabajar 24/7.

## Los fundamentos (del curso Hermes 2026)
- **Chatbot vs Agente** · **el Agent Loop** · los **4 elementos**: loop, contexto,
  memoria y herramientas.
- **El "Arnés" (harness) importa más que el modelo**: la infraestructura que rodea al
  LLM (contexto + memoria + herramientas + loop) es lo que lo convierte en agente útil.
- El cerebro del agente se define con **`AGENTS.md` + `soul.md` + memoria persistente**.
- **Skills** = SOPs digitales que el agente acumula como ventaja competitiva.

## El framework SOUL (sacarle el 100% a un agente)
- **S — Setup:** onboarding real. Darle contexto hasta que te conozca mejor que tú
  (correos, conversaciones, canal de YouTube, redes).
- **O — Orquestar:** ejecutar comandos en terminal, crear sus propias herramientas,
  controlar el navegador (extensión Chrome), instalar skills desde **CloudHub** (un
  "App Store" de skills: Trello, Slack, Whisper, Google…).
- **U — Unificar:** el mismo agente, mismo contexto, por Telegram/Slack/Discord/WhatsApp;
  y agentes que hablan **entre sí** en paralelo.
- **L — Libertad:** **heartbeat** (revisa tareas pendientes y las ejecuta solo) +
  **CronJobs** (acciones programadas) → de reactivo a **proactivo** (ej. resumen
  matutino + borrador de newsletter antes de despertar).

## Construir un agente (OpenClaw, paso a paso)
1. **Qué es OpenClaw**, opinión tras un mes, **decisiones/requisitos/costos**.
2. **Despliegue:** instalación en **VPS Hostinger (~$5/mes)**, en **Mac Mini**, o
   **gratis con Ollama** (IA local, sin coste de API).
3. **Seguridad:** **Tailscale** (red privada). ⚠️ Sin esto quedas expuesto — *Shodan*
   escanea internet y lista miles de instancias con IP/puerto público.
4. **Conexión y uso por Telegram**, **memoria persistente**, **backups automáticos a
   GitHub**, conectarlo a Internet, primer caso de uso real.

## De 1 agente a un equipo: el "Gran Consejo" (multi-agente)
Cuando ya tienes un agente sólido, montas un **sistema multi-agente** que se coordina:
- **Un solo punto de contacto:** tú hablas con un **coordinador (el Canciller)** que
  **delega** en los demás. No abres cinco chats.
- **Memoria compartida en base de datos:** conversaciones, tareas, conocimiento e
  historial viven en **Supabase** (el "sistema nervioso central").
- **Stack:** **OpenClaw** (motor de cada agente) + **Supabase** (BD compartida) +
  **Discord** (donde ves la actividad del equipo). Cada agente = instancia independiente
  con su **workspace, memoria y personalidad**.
- Se cubre: **roles, canales y memoria**, **Mission Control** (centro de control),
  **CronJobs/HeartBeats**, **identidad/cuentas** para los agentes, **correo y calendario**
  (Google Cloud) y **acceso web con Playwright**.

## Las dos "casas" de agentes: Claude Code vs OpenClaw
| | **Agentes de Claude Code** | **Agentes de OpenClaw** |
|---|---|---|
| Dónde viven | dentro de Claude Code (una carpeta) | en el **VPS** donde lo instalas |
| Modelo | configurable (Haiku/Sonnet/Opus) | el que conectes (OAuth ChatGPT/Codex, Ollama…) |
| Invocación | dentro de una sesión de Claude Code | siempre activo, por tus canales |
| Proactividad | bajo demanda + sub-agentes | **24/7** con heartbeat/cron |
| Orquestación | **misma lógica**: hablas con el principal, él **delega** en sub-agentes especializados |

> Truco de productividad: conectarse al VPS con **Remote SSH** (Antigravity/VS Code) para
> editar la config de OpenClaw de forma visual, sin terminal.

## El Motor Agéntico (panel de control de tu operación con IA)
Un **dashboard 100% local y de solo lectura** que lee tu actividad real de Claude Code y
demás herramientas IA y te muestra lo invisible: **cuánto gastas vs. cuánto trabajo
extraes (tu ROI real)**, tiempo ahorrado por skills, qué recuerda tu memoria y qué hacen
tus asistentes. Se **autoinstala**: le pasas `INSTALAR.md` a tu agente y escribes
`instalalo` (corre en `localhost:8081`, con un análisis "Sueño" cada mañana a las 7:00).
- **Instaladores descargados:** [`recursos/02-claude-code/`](../recursos/02-claude-code/)
  (`MAC_…` y `WINDOWS_motor_agentico_local_v0.1.0.zip`).

## ✅ Resultado al aplicarlo
Pasas de "usar IA cuando te acuerdas" a tener un **equipo de agentes autónomos
trabajando 24/7** en tu propio servidor: te conocen, se conectan a tus herramientas,
ejecutan tareas mientras duermes, se coordinan entre sí y te reportan. Y, con el Motor
Agéntico, **mides el ROI real** de toda esa operación. Es la base para automatizar tu
negocio entero — o para ofrecerlo como servicio.

## Dónde está en el archivo
- **[05 · 🦞 Reto Imperial OpenClaw](../05-reto-imperial-openclaw/)** (27) — el curso central.
- **[02 · Claude Code](../02-claude-code/)** — "Instala tu Motor Agéntico", Playwright, Skills/MCP, sub-agentes + Hermes 2026.
- **[06 · Vibe-Coding](../06-vibe-coding/)** — Hermes vs OpenClaw, Claude Code + n8n (Kit/MCP/Skills), Ollama local.
- **[13 · Agentes de WhatsApp](../13-agentes-de-whatsapp/)** (18) — agentes conversacionales.
- **[29 · (Obsoleto) Agentes IA: Relevance](../29-curso-obsoleto-agentes-ia-relevance-desde-0/)** (17) — versión antigua.
- **Recursos:** instaladores del **Motor Agéntico** (Mac/Windows) en [`recursos/02-claude-code/`](../recursos/02-claude-code/).
