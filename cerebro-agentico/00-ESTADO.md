# Estado vivo — Imperio Agéntico

> **Actualizar este archivo en cada sesión de trabajo.** Es el punto de retorno:
> qué se hizo, qué sigue. La ruta completa está en [`01-RUTA.md`](01-RUTA.md).

## Última actualización
- **Fecha:** 2026-07-06
- **Rama:** `claude/agentic-systems-course-4kh9sr`

## Proyecto piloto ELEGIDO por Alexander
**Sistema automático de creación de contenido + equipo de marketing para todos
sus clientes.** Diseño completo: [`02-SISTEMA-CONTENIDO-MARKETING.md`](02-SISTEMA-CONTENIDO-MARKETING.md).

## Hecho
- ✅ Curso extraído completo en `docs-skool/imperio/` (hecho en rama
  `funny-shannon-2c94fg`, traído a esta rama). 30 cursos / 826 lecciones.
- ✅ Capa curada leída y aprendida (RESUMEN-MAESTRO, INDICE-POR-CATEGORIA,
  ficha sistemas-agenticos). El "mapa mental" del curso está asimilado.
- ✅ CLAUDE.md actualizado: cualquier sesión nueva encuentra el curso y el
  protocolo de lectura sin perderse.
- ✅ Extracción fiel (4 lecturas profundas, 2026-07-05/06): modelo CCC completo,
  arquitectura Gran Consejo, agencia creativa Higgsfield + skills bundle +
  Matías Meta Ads, inventario de ~90 prompts útiles + máquina existente.
- ✅ Diseño del sistema en `02-SISTEMA-CONTENIDO-MARKETING.md` (roles, fases A-D).
- ✅ Activos reutilizables traídos de funny-shannon: `.claude/skills/`
  (cerebro-guiones, avatarhype, crear-estilo-broll) + `cerebro/maquina-contenido/`.
- ✅ Esqueleto multi-cliente: `equipo-marketing/clientes/_plantilla/` (expediente
  de 5 archivos: perfil, voz, pilares+calendario, activos, bitácora).

## Siguiente paso
- ✅ Cliente 1 operativo: **Invertí sin vueltas**. Expediente completo (buyer
  persona validado, voz real de Mati desde 4 reels transcritos, regla de
  cumplimiento "sin estimaciones").
- ✅ **Guion 001 aprobado y con paquete de producción completo**: narración en
  bloques de 10s + 5 prompts de B-rolls para Omni (con texto ✅, plantilla 8
  bloques) + 3 imágenes nano_banana de respaldo en Higgsfield.
- ✅ Lecciones de producción registradas: Veo por API deforma texto; Omni SÍ
  renderiza texto (dato de Ale); ruta validada = Omni/Flow manual.
- ⏳ **Del lado de Ale/Mati:** grabar la narración, pegar los 5 prompts en
  Omni, aportar la captura real de resultados, confirmar vencimientos de bonos.
- ✅ Calendario mensual v1 propuesto (Ale indicó que el contenido ya existe).
- ✅ Embudo CCC redactado completo (5 emails + spec ManyChat/MailerLite).
- ✅ **FASE D INICIADA:** runbook completo en `03-RUNBOOK-FASE-D.md`
  (decisión: Hermes en VPS Hostinger vía Docker; OpenClaw plan B). Extraído
  de las lecciones reales (instalación, Tailscale, SOUL, backups, crons).
- ⏭️ **Ale ejecuta la lista de compras del runbook** (VPS, API key, bot
  Telegram, Tailscale, repo backup) → despliegue guiado → onboarding del
  Coordinador → 3 crons iniciales (briefing, tendencias, backup).

## Decisiones tomadas
- El conocimiento permanente vive en git (este repo), no en la memoria de sesión:
  capa curada del curso + este cerebro + CLAUDE.md como traspaso.
- Objetivo de Alexander (sus palabras): *"construir sistemas agénticos
  independientes capaces de hacer muchas cosas"* → la pista central del curso es
  **B (Claude Code / agentes)** + ficha **sistemas-agenticos** (OpenClaw, Hermes,
  multi-agente), con D (n8n) como complemento para flujos.
