# RUNBOOK Fase D — El agente 24/7 (Coordinador de marketing en VPS)

> Extraído fielmente del curso (2026-07-06): reto OpenClaw 005-009 y 012-016,
> curso Hermes 2026 (4,5 h), sesiones vibe-coding 005 y grabaciones 006.
> ⚠️ marca pasos que requieren ver el vídeo de la lección al ejecutar.
> **Objetivo:** un agente que vive en un VPS, lee este repo como cerebro,
> y cada mañana trabaja solo para el equipo de marketing (empezando por Mati).

## 0. Decisión de arnés: HERMES (con OpenClaw como plan B)

Fundamento (del propio curso, no opinión mía):
- El curso más reciente (Hermes 2026) lo posiciona como la evolución: open
  source MIT (Nous Research), **self-improving** (crea skills solo tras cada
  tarea; "OpenClaw rara vez se auto-mejoraba"), **memoria SQLite integrada de
  fábrica**, crons 24/7 fiables, y **pide autorización antes de ejecutar**.
- Síntesis oficial de las sesiones: *"Claude Code es el arnés para desarrollar
  con vos presente; Hermes y OpenClaw son para correr 24/7 cuando no estás.
  Hermes puede llamar a Claude Code para resolver tareas."*
- Instalación MÁS SIMPLE: Hostinger tiene **app Docker "Hermes Agent" de 1
  clic** en su marketplace.
- Si Hermes falla, existe migración documentada en ambos sentidos
  (`hermes claw` migra OpenClaw→Hermes) y todo el cerebro son archivos .md
  portables. No nos casamos con la herramienta.

## 1. Lista de compras de Ale (~30-45 min, una sola vez)

| # | Qué | Dónde | Costo |
|---|---|---|---|
| 1 | **VPS Hostinger plan KVM2**, Ubuntu 24.04 LTS, ubicación más cercana (USA) | hostinger.com | ~$10/mes (mes a mes) — cupón del curso: BENJAMIN10 anual |
| 2 | **API key dedicada** para el agente: Anthropic (console.anthropic.com) **o** OpenRouter | — | presupuesto inicial $5-10. 🚨 Anthropic ya NO permite usar la suscripción Pro/Max por OAuth: es API key sí o sí |
| 3 | **Bot de Telegram**: @BotFather → `/newbot` → nombre + username terminado en `bot` → guardar el token | Telegram | $0 |
| 4 | **Cuenta Tailscale** (login con Google) | tailscale.com | $0 (hasta 100 dispositivos) |
| 5 | **Repo GitHub PRIVADO** para backup del agente + Personal Access Token granular (solo ese repo, contents read/write) | github.com | $0 |
| 6 | (opcional, audio por Telegram) API key de OpenAI para Whisper | platform.openai.com | ~$0-2/mes |

**Reglas de oro de seguridad (del curso, no negociables):**
- Correo dedicado para el agente; keys EXCLUSIVAS con expiración; **nunca
  pegar keys en el chat** (van al `.env` del entorno).
- Nunca instalar/operar como root; usuario dedicado.
- Empezar con permisos de **solo lectura** en todo lo sensible.

## 2. Instalación (ruta principal: Hermes vía Docker en Hostinger)

1. Contratar el VPS (KVM2, Ubuntu 24.04 LTS). Crear password root → password
   manager. SSH key: no por ahora · Docker manager: sí (esta ruta lo usa).
2. En el panel de Hostinger → administrador de Docker → buscar app
   **"Hermes Agent"** → Implementar → Abrir. ⚠️ Clics exactos: vídeo del curso
   (youtu.be/FQZGoSwdS_0, cap. 0:37–0:56).
3. Onboarding de Hermes: **Quick setup** → proveedor de modelo (ver §3) →
   entorno **local** (default) → canal **Telegram** (pegar token de BotFather;
   Hermes pide tu Telegram User ID y un `/start` al bot para vincularte SOLO
   a vos) → dejarlo **como servicio persistente** cuando pregunte.
4. Verificar: `hermes doctor` (autorreparación) · mandar "Hola" por Telegram.

**Ruta alternativa (OpenClaw manual — comandos completos por si Hermes falla):**
```
ssh root@IP_DEL_VPS
adduser openclaw            # password propio, fuerte
usermod -aG sudo openclaw
su - openclaw
curl -fsSL https://clawd.bot/install.sh | bash    # Quick Start
# servicio persistente: /etc/systemd/system/openclaw-gateway.service
# (bloque systemd completo en la lección 008; gateway --bind loopback --port 18789)
```

## 3. El modelo (cerebro alquilado)

- **Opción A (recomendada):** Anthropic **API key dedicada** (Opus/Sonnet) con
  presupuesto bajo — calidad máxima, costo por uso.
- **Opción B:** **OpenRouter** pay-per-use — una key, muchos modelos, permite
  cambiar barato (Carlos en la comunidad corre Hermes con DeepSeek ~$10/mes).
- **Opción C (el "truco" del curso):** OAuth de la suscripción ChatGPT
  Plus/Codex (~$20/mes fijo) — funciona hoy pero es frágil (Anthropic ya cerró
  el suyo; OpenAI puede cerrarlo). No basar el sistema en esto.

## 4. Blindaje (obligatorio ANTES de cargarle nada sensible)

En el VPS (como root) y en tu compu (misma cuenta):
```
# VPS
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up            # abre link → login → autorizar
tailscale status             # anotar IP 100.x.x.x

# Firewall (después de confirmar acceso por Tailscale):
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow in on tailscale0
sudo ufw enable
sudo ufw status              # el puerto del panel NO debe estar ALLOW Anywhere
```
Prueba final: desde el celular con datos (sin WiFi), `http://IP_PUBLICA:puerto`
**NO debe cargar**; Telegram debe seguir respondiendo.
⚠️ Acceso al panel vía Tailscale con gateway en loopback: el detalle
(`tailscale serve`) se resuelve en el vídeo de la lección 007.
Si te quedás afuera: guía de rescate en la lección 009.

## 5. El cerebro del agente = ESTE REPO (acá se conecta todo lo construido)

1. **Clonar este repo en el VPS** (deploy key de solo lectura primero;
   escritura cuando el flujo esté probado):
   `git clone git@github.com:gogosss-29/Ale.git` (rama
   `claude/agentic-systems-course-4kh9sr`).
2. **AGENTS.md del agente** (regla del curso: **<200 líneas**, se precarga en
   cada sesión): define el rol "Coordinador del equipo de marketing de la
   consultora Cerebro" y APUNTA al repo — leer
   `cerebro-agentico/02-SISTEMA-CONTENIDO-MARKETING.md`, expedientes en
   `equipo-marketing/clientes/`, reglas en `01-voz-de-marca.md` de cada
   cliente. No duplicar contenido: referenciar.
3. **Soul.md** (<50 líneas): personalidad — argentino, directo, sin humo;
   nunca inventa datos; registra todo en la bitácora.
4. **user.md**: quién es Ale (consultora Cerebro, clientes, cómo trabaja).
5. **memory.md / SQLite**: la memoria conversacional la maneja Hermes; el
   conocimiento de negocio vive en el repo (fuente de verdad).
6. **Onboarding real (la S de SOUL — "sin esto todo rinde al 10%"):** primera
   sesión larga por Telegram: que lea el repo entero, haga preguntas, y
   escriba su memoria. Instrucción del curso: *"no te quedes con lo primero
   que encuentres; seguí investigando hasta conocerme mejor que yo"*.
7. **Backup automático** (lección 015): repo GitHub privado + PAT granular +
   cron diario con commit timestampeado; `.gitignore` con `.env`, `*.key`,
   `secrets/`. Revisar QUÉ va a versionar antes del primer push.

## 6. Primer caso de uso: el Coordinador de marketing (empezar CHICO)

Regla del curso: la versión más sencilla que igual aporta valor; solo lectura
primero; 3-4 casos sólidos máximo.

**Cron 1 — Briefing matutino (lunes a viernes, 9:00 AR = 12:00 UTC):**
lee el calendario y bitácora de `equipo-marketing/clientes/invertir-sin-vueltas/`
→ manda por Telegram: qué piezas están en qué estado, qué falta (grabación,
captura, datos), y UNA propuesta del día. **No ejecuta nada: informa.**

**Cron 2 — Vigía de tendencias (lunes 8:00 AR):** investiga (Brave Search)
2-3 temas del mercado argentino de la semana (dólar, tasas, noticias de
inversión) y propone el ángulo para las piezas "momento del mercado" del
calendario (piezas 3 y 12).

**Cron 3 — Backup diario (23:00)** del sistema a GitHub (§5.7).

**Escalada (solo cuando 1-3 funcionen una semana sin fallas):** proponer
borradores de guiones directamente (siguiendo la skill del repo) → aprobación
tuya por Telegram → commit al repo. Después: segundo agente (Guionista) y
recién ahí el Gran Consejo (Supabase + Discord, lecciones 017-022).

## 7. División del trabajo para el despliegue

- **Ale:** compras de §1 · correr los comandos guiado (30-45 min) · el
  onboarding conversacional por Telegram.
- **Claude (sesión en este repo):** redactar AGENTS.md/Soul.md/user.md del
  agente ANTES del despliegue · los textos de los 3 crons listos para pegar ·
  troubleshooting en vivo (me pegás el error, te doy el paso).
- **El agente (Hermes):** una vez vivo, el mantenimiento de su propia config
  se le pide a él por Telegram (así enseña el curso).

## Referencias exactas (⚠️ vídeos para los pasos visuales)
- Instalación VPS: Loom 426a6b03… (lección 006) · Telegram/onboarding: Loom
  7cd64940… (008) · Tailscale: Loom 7f64fa4d… (007) + gist de comandos ·
  Hermes completo: youtu.be/FQZGoSwdS_0 · SOUL: youtu.be/M8kOnNLL-3E ·
  Docs: docs.hermes.nousresearch.com · docs.openclaw.ai
