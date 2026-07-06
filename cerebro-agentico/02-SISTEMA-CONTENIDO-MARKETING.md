# Sistema de contenido y equipo de marketing multi-cliente

> **Qué es:** el diseño del sistema automático de creación de contenido + equipo
> de marketing de Alexander, para usar con todos los clientes de la consultora
> Cerebro. Sale 100% del curso Imperio Digital (extracciones fieles hechas el
> 2026-07-05/06) + los activos que Alexander ya construyó (`cerebro-guiones`).
>
> **Fuentes primarias usadas** (releer ante cualquier duda, NO improvisar):
> - Modelo CCC: `docs-skool/imperio/18-crea-conecta-convierte/` (001–007)
> - Gran Consejo (multi-agente): `docs-skool/imperio/05-reto-imperial-openclaw/` (017–022)
> - Agencia creativa + skills: `docs-skool/imperio/02-claude-code/` (008, 010–013, 015, 019, 032, 034)
> - Prompts: `docs-skool/imperio/17-biblioteca-de-prompts/` (~90 relevantes)
> - Máquina existente: `.claude/skills/cerebro-guiones/` + `cerebro/maquina-contenido/`

## 1. El método que implementamos (CCC, tal cual el curso)

**Premisa:** "A la gente le encanta comprar pero odia que le vendan." La atención
es el oro; el contenido se crea con propósito, no con fórmulas de algoritmo.

**El flujo maestro por cliente:**
1. **CREA** — reels de 3 tipos: **viralidad** (alcance; replicar formatos que ya
   funcionan — "roba como un artista"), **autoridad** (expertise, historia,
   resultados) y **conversión** (CTA "comenta X"). Estructura AIDA a macro y
   micro escala. Regla: NUNCA vender el producto al final del reel; el CTA lleva
   al lead magnet. Todo reel lleva CTA de interacción.
2. **CONECTA** — ManyChat: comentario con palabra clave → DM automático → link a
   opt-in page → lead magnet de alto valor a cambio del **email**. (Gratis hasta
   1000 contactos; $15/mes después.)
3. **CONVIERTE** — MailerLite: opt-in page (responde "¿qué obtengo?" + "¿cuál es
   el beneficio?") → Email #1 inmediato (misión + entrega del lead magnet) →
   secuencia común con 2 días entre correos: #2 problema → #3 solución →
   #4 errores comunes → #5 CTA/oferta. Venta suave sobre las **3 creencias**
   (creer en ti / en el sistema / en sí mismos).
4. **ESCALA** — retargeting Meta Ads a quien no compró (CPA ~$2 según el curso),
   país por país con los winning ads, renovando creativos cada ~2 semanas.
   Sistema circular: los ads devuelven al orgánico.

## 2. El equipo — humanos del curso → agentes nuestros

El curso usa un equipo humano (guionista, editor, publicador, media buyer) y
enseña la arquitectura multi-agente "Gran Consejo" (Canciller + consejeros,
Supabase como memoria compartida, Discord como sala). **Nuestro equipo:**

| Rol (agente) | Basado en | Qué hace | Con qué |
|---|---|---|---|
| **Coordinador** ("Canciller") | Gran Consejo 017 | Único punto de contacto con Ale; asigna, revisa, reporta | Claude Code (fase 1) → OpenClaw (fase 4) |
| **Estratega** | Gran Consejo 018 + prompts B | Tendencias, competencia, calendario mensual por cliente | Prompts 143/178/058 + skill `Calendario Contenido` |
| **Guionista** ("Cronista") | cerebro-guiones + CCC | Guiones de reels (3 tipos) con el pipeline de 7 estaciones | Skill `cerebro-guiones` **parametrizada por cliente** |
| **Productor** | Agencia creativa (lección 012) | Fotos producto, videos, UGC, thumbnails, landings | Higgsfield MCP (`gpt_image_2`, `kling3_0`, `seedance_2_0`), LOW+1k → upscale ganadoras |
| **Copywriter** | Biblioteca prompts + skills 019 | Captions, ads copy A/B, emails de la secuencia, landings | Prompts C/D/E/F + skills `Copia Ad`, `Escritor Captions` |
| **Media Buyer** ("Matías") | Lección 008 | Analiza/pausa/crea campañas Meta por API, CPA, presupuestos | Proyecto Node + Meta Marketing API (One Prompt Setup) |

Regla del Gran Consejo que adoptamos desde el día 1: **el resultado de una tarea
siempre queda registrado** (en fase 1: en el expediente del cliente en git; en
fase 4: como comentario en Supabase).

## 3. Arquitectura multi-cliente (lo nuestro)

Lo que ya existe (`cerebro-guiones`) sirve a 2 marcas con datos hardcodeados.
Para N clientes, **separamos motor de datos**:

- **Motor (compartido, agnóstico):** pipeline de 7 estaciones con gates,
  segmentador a 10s (2,8 palabras/seg, tope 28), plantilla de 3 bloques, router
  de herramientas (persona→Omni/Flow · texto/dato→Remotion · escena→Flow),
  estilos de B-roll, modelo CCC, prompts del curso.
- **Expediente por cliente (datos):** `equipo-marketing/clientes/<cliente>/` con
  perfil, voz de marca, buyer persona, pilares + calendario, lead magnets,
  activos (fotos/escenarios/avatar si tiene), ejemplos aprobados (few-shot) y
  bitácora. La plantilla está en `clientes/_plantilla/`.

**Onboarding de un cliente nuevo** (una sesión, con los prompts del curso):
1. Perfil y oferta → prompt `170` (propuesta) como guía de preguntas.
2. Buyer persona → prompts `172` + `014` (dolores y deseos).
3. Voz de marca → prompt `177` (+ `163` para personalizar después).
4. Competencia y tendencias → prompts `178` + `143`.
5. Pilares y calendario 30 días → prompt `058` + skill `Calendario Contenido`.
6. Definir el lead magnet #1 y la palabra clave del CTA.

**Ciclo mensual por cliente** (el "turno" del equipo):
Estratega propone calendario → Ale aprueba (gate) → Guionista produce guiones
por lotes → Ale aprueba → Productor genera creativos (LOW+1k, upscale ganadoras)
→ publicación + ManyChat activo → secuencia de emails corriendo → Media Buyer
reporta y ajusta → los aprobados realimentan el few-shot del cliente.

## 4. Plan de construcción (Ley de Gall: simple → MVP → iterar)

- **Fase A — Fundación (en curso):** estructura multi-cliente en el repo,
  plantilla de expediente, onboarding del primer cliente, parametrizar
  `cerebro-guiones` para aceptar N clientes. Sin cuentas nuevas: todo en
  Claude Code + git.
- **Fase B — Producción:** Higgsfield MCP como Productor (flujo lección 012:
  fotos → videos → UGC → landing → deploy Vercel). Primer paquete de contenido
  real del cliente 1 de punta a punta.
- **Fase C — Embudo CCC:** ManyChat (DM + palabra clave) y MailerLite (opt-in +
  secuencia de 5 correos) del cliente 1. ⚠️ Requiere crear cuentas (gratis hasta
  1000). Los 5 emails se redactan con la estructura del curso (§1.3).
- **Fase D — Autonomía 24/7:** Media Buyer "Matías" (API Meta) + migrar el
  equipo al Gran Consejo real (OpenClaw en VPS ~$5/mes + Tailscale, Supabase,
  Discord, heartbeats). Empezar con 2 agentes (Coordinador + Guionista) como
  manda la lección 019, no 5 de golpe.

**Criterio para avanzar de fase:** la anterior funcionó con un cliente real de
punta a punta. No construir infraestructura antes de necesitarla.

## 5. Huecos conocidos (no inventar — resolver cuando toque)

- ⚠️ Plantillas descargables de los 5 emails: están en Skool, no en el archivo.
  Se redactan desde la estructura documentada (§4.2 de la extracción CCC).
- ⚠️ Pasos visuales de ManyChat/MailerLite/Meta Developers: ver vídeos
  (links en las lecciones) al ejecutar la fase C/D.
- ⚠️ SQL exacto de las 9 tablas de Supabase: el curso da tablas y campos clave,
  no el DDL — se define al ejecutar la fase D.
- ⚠️ ZIPs de skills del bundle (Contenido, Redes, Ads): descargar de Skool
  cuando haga falta un skill puntual; mientras, la biblioteca de prompts cubre.
