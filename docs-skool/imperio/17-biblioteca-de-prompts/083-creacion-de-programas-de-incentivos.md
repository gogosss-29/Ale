# Creación de Programas de Incentivos

> Ruta: Biblioteca de Prompts › Creación de Programas de Incentivos

---

**Programas de Incentivos para Afiliados:** Diseña programas que muevan a tu top 10% de afiliados (los que generan el 80% del revenue) y motiven al resto a subir de nivel. No más programas planos que aburren a todos.

**Recomendación de modelo:** **Claude (Opus o Sonnet)**. Si conectas el **MCP de tu plataforma de afiliados** (Refersion, Impact, Tapfiliate, GHL, etc.), Claude analiza tus afiliados reales y propone incentivos personalizados por segmento.

**1. Audit del programa actual + benchmark**

```jsx
Mi programa actual: [comisión base / estructura / qué ofrezco hoy]
Mi industria: [nicho]
Número de afiliados activos: [X]
Revenue del programa: [últimos 30/90/365 días]

Audítame:

1. PERFORMANCE actual:
   - 80/20: ¿qué % de revenue viene de mi top 10%?
   - Afiliados activos vs dormidos (>30 días sin venta)
   - Comisión promedio por afiliado por mes
   - LTV de un afiliado promedio en el programa

2. BENCHMARK de industria:
   - Comisión estándar en mi nicho (rango: bajo / promedio / agresivo)
   - Estructuras más rentables en industrias similares
   - Qué hacen los programas top (qué los hace ganadores)

3. SEÑALES DE WARNING:
   - Si mi comisión está below market
   - Si mi conversión de afiliado a venta está baja
   - Si mi churn de afiliados es alto
   - Si dependo demasiado de pocos afiliados

4. GAPS DEL PROGRAMA:
   - ¿Hay tiers? ¿Bonificaciones? ¿Contests?
   - ¿Qué motivaciones no-monetarias estoy usando (early access, co-marketing, etc.)?
   - ¿Qué reciben los top performers que el resto no?

Formato: ejecutivo + tabla detallada por afiliado.
```

**2. Tier structure: incentivos por nivel**

```jsx
Programas planos no funcionan. Vamos a tierearlo.

Mi producto: [precio + comisión actual %]
Mi affiliate revenue mensual: [$X]

Diseña una tier structure de 4 niveles:

TIER 1: BRONZE (entry level)
- Requisitos: $0-500/mes en ventas referidas
- Comisión base: [%]
- Incentivos extras: ninguno (aún)
- Soporte: self-serve resources
- Objetivo: que cualquiera pueda empezar

TIER 2: SILVER
- Requisitos: $500-2000/mes
- Comisión: +2-3 puntos sobre base
- Incentivos: acceso a creatives premium, swipe files exclusivos
- Soporte: monthly group call
- Objetivo: el 60% debería llegar acá en 90 días

TIER 3: GOLD
- Requisitos: $2000-5000/mes
- Comisión: +5 puntos
- Incentivos: bonificaciones por hitos, co-branded content, early access a lanzamientos
- Soporte: bi-weekly 1:1 con affiliate manager
- Objetivo: el 20% del programa

TIER 4: PLATINUM/PARTNER
- Requisitos: $5000+/mes O top 10% del programa
- Comisión: customizada (revenue share, bonos masivos)
- Incentivos: viajes anuales, mastermind exclusivo, productos físicos, mention en mi marketing
- Soporte: priority, custom landing pages, có-creación
- Objetivo: el 5-10% del programa, 60%+ del revenue

Para cada tier:
- Beneficios específicos (no vagos)
- Cómo se promueve la persona (criterios objetivos, no subjetivos)
- Cómo se mantiene el tier (degradación si cae performance?)
- Comunicación del upgrade (email + Slack + manual)

Dame el playbook completo del onboarding + upgrade flow.
```

**3. Lanzamiento + comunicación del programa**

```jsx
Voy a anunciar el nuevo programa de incentivos a [Número] afiliados actuales y captar [Número] nuevos.

Diseña la campaña de lanzamiento:

1. PRE-LAUNCH (1-2 semanas antes):
   - Email teaser (subject + body, máx 100 palabras)
   - Post en Slack/Discord/Facebook group
   - DM personalizada a top 10 afiliados (template + customización por persona)

2. LAUNCH DAY:
   - Email main con el nuevo programa
     * Subject (3 variantes)
     * Hook que muestre el upside máximo ("Top affiliates pueden ganar $X/mes")
     * Estructura clara de los 4 tiers
     * CTA: "Calcular cuánto puedes ganar" (linkea a calculadora interactiva)
   - Video corto de 60-90 seg (script incluido)
   - Webinar de Q&A en vivo (agenda + preguntas anticipadas)

3. POST-LAUNCH (siguientes 30 días):
   - Email 1 (día 3): caso de un afiliado top y cómo este nuevo programa lo beneficíaria
   - Email 2 (día 7): leaderboard semanal de quienes ya hicieron upgrade
   - Email 3 (día 14): "¿Aún no aplicaste?" recordatorio
   - Email 4 (día 21): contest/incentivo limitado para empujar a inactivos
   - Email 5 (día 30): celebrar el mes 1 con números del programa

4. ASSETS QUE AFILIADOS NECESITAN:
   - 5 swipe emails para que ellos promuevan
   - 5 social posts plug-and-play
   - 3 videos cortos demo del producto
   - Banners (varias dimensiones)
   - Landing page co-branded template

Reglas: zero "¡Hola comunidad!". Máximo 1 emoji. Foco en lo que ELLOS ganan, no en lo que yo gano.
```

**4. Tracking + reporting + dashboards**

```jsx
Si los afiliados no ven sus números fácilmente, no se enganchan. Diseñemos el reporting:

1. DASHBOARD PARA EL AFILIADO (lo que ven en su login):
   - Ventas este mes vs mes anterior
   - Comisión ganada / pendiente / pagada
   - Conversion rate de sus referidos
   - Próximo tier (cuánto les falta + qué desbloquean)
   - Leaderboard (top 10 del mes, anónimo o público)

2. REPORTING SEMANAL POR EMAIL (a cada afiliado activo):
   - Subject: "Tu semana en [Programa]: [número de ventas / $X comisión]"
   - Headlines: revenue + ventas + tier progress
   - 1 tip personalizado basado en su performance
   - 1 oportunidad inmediata (lanzamiento, contest, etc.)

3. REPORTING MENSUAL EJECUTIVO PARA MÍ:
   - Top 10 afiliados por revenue
   - Bottom 10 afiliados activos (¿candidatos a reactivar o cortar?)
   - Tier movements (quién subió, quién bajó)
   - Programa health score (revenue total, # activos, conversion rate global)
   - 3 acciones específicas para el próximo mes

4. ALERTS AUTOMÁTICAS:
   - Si un top afiliado tiene 14 días sin venta → outreach
   - Si un afiliado nuevo NO hace su primera venta en 30 días → onboarding adicional
   - Si alguien sube de tier → felicitación + bono inmediato

Si conectas el MCP de mi plataforma de afiliados, configura todo esto automático. Dame el flow exacto.
```

**5. Gamification + contests + retention**

```jsx
Programas planos mueren. Gamifiquemos:

Mi situación: [#afiliados, revenue, principal queja]
Objetivo del trimestre: [crecer 30% / activar dormidos / aumentar order value]

1. CONTESTS RECURRENTES:
   - Mensual: top 3 del mes (premios: cash bonus / producto físico / dinero adicional)
   - Semanal: "semana relampago" con comisión bumped
   - Trimestral: contest mayor (viaje, tech, dinero significativo)

2. SPRINTS DE LANZAMIENTO:
   - Cada launch: 7-14 días con boost de comisión
   - Top 3 de ese launch reciben bonus extra
   - Daily leaderboard durante el sprint

3. BADGES Y RECONOCIMIENTOS:
   - Primer venta
   - Primera $1000 acumulada
   - 100 ventas totales
   - Tier upgrade
   - Featured affiliate del mes (en tu newsletter, social)

4. RETENTION PLAYBOOK:
   - Cuándo y cómo activar a un afiliado dormido (Email + DM + llamada en este orden)
   - Re-onboarding para afiliados que llevan 60 días inactivos
   - Exit interview: cuando alguien se baja del programa, qué preguntar

5. EVENTOS COMUNITARIOS:
   - Mastermind trimestral solo para Gold+
   - Annual partner summit (presencial o virtual)
   - Office hours mensuales con el founder

Dame el calendar completo del trimestre con timing, mecánicas, premios sugeridos y comunicación.
```

*Tip pro:* Conecta el **MCP de Slack/Discord** en Claude. Cada lunes Claude puede anunciar el leaderboard de la semana anterior automáticamente en tu canal de afiliados. Mantiene la energía alta sin que tú lo hagas a mano.
