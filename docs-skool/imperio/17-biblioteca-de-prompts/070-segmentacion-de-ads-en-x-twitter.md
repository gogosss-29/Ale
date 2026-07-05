# Segmentación de Ads en X (Twitter)

> Ruta: Biblioteca de Prompts › Segmentación de Ads en X (Twitter)

---

**Ads en X (antes Twitter):** X cambió mucho desde 2023. Algoritmo nuevo, formatos nuevos, audiencias premium. Estos prompts están hechos para el X de 2026, no para el Twitter viejo.

**Recomendación de modelo:** **Claude (Opus o Sonnet)**. Si conectas el **MCP de X Ads** o le pegas screenshots de tu dashboard, análisis y propone optimizaciones con tu data real.

**1. Cómo entiende X tu audiencia en 2026**

```jsx
Mi producto/servicio: [qué vendo]
Mi audiencia: [perfil]
Objetivo: [conversiones / leads / awareness / followers / engagement]

Dame primero el panorama actualizado de cómo X targetea en 2026:

1. Tipos de audiencia disponibles en X Ads 2026:
   - Keywords (search + timeline)
   - Followers de @cuentas específicas
   - Lookalikes de followers
   - Eventos en vivo
   - Conversation topics
   - Custom audiences (uploaded list, retargeting)
   - Premium subscriber audience (X Premium users)

2. Para mi nicho [nicho], cuáles de estos rinden mejor y por qué

3. Particularidades 2026:
   - El feed "For You" vs "Following" —qué cambia para ads
   - El peso de las views vs replies vs bookmarks
   - Cómo X Premium afecta el costo y el reach
   - Algoritmo: ¿qué amplifica? ¿qué sup rime?

4. Lo que ya NO funciona como antes:
   - Promotion de tweets puramente promocionales
   - Hashtags spammeados
   - URLs sin contexto

Si sabes algo desde 2023 que NO aplica en 2026, dime explícitamente.
```

**2. Targeting completo: keywords + cuentas + lookalikes**

```jsx
Para mi campaña [producto/objetivo], dame un plan de targeting con esta estructura:

1. KEYWORDS (lo más potente de X):
   - 25 keywords con intent de compra alto
   - 25 keywords "consideration" (gente investigando)
   - 15 keywords contrarias (negative keywords)
   - Para cada uno: ¿en tweets o en search? ¿match broad o exact?

2. CUENTAS A TARGETEAR (followers de):
   - 15 cuentas competidoras directas
   - 15 cuentas adyacentes (mismo perfil de audiencia, distinto producto)
   - 10 thought leaders del nicho
   - 5 medios/publicaciones del nicho
   Justifica cada elección y descartá cuentas con audiencia inflada o fake.

3. CONVERSATION TOPICS:
   - 8-12 topics relevantes (de la lista que X ofrece)
   - 5 topics a evitar (afines pero erróneos)

4. CUSTOM AUDIENCES:
   - Email list (si tengo)
   - Visitor retargeting (window: 7/30/90 días)
   - Engagers de mis tweets orgánicos

5. EXCLUSIONES estratégicas (cuáles y por qué)

6. ESTRUCTURA DE CAMPAÑA:
   - Cuántos ad groups separar
   - Por qué esa estructura
   - Qué audiencia es "hero" y cuáles son test
```

**3. Ad formats y copy que rinde en X 2026**

```jsx
Producto: [producto/servicio]
Angle: [el argumento principal de venta]

Generáme ads en los formatos más rentables de X 2026:

1. PROMOTED TWEET (single):
   - 3 variantes de copy (máx 280 chars)
   - Cada una: hook + valor + CTA
   - Estilo: native (debe sentirse como tweet orgánico, no ad)

2. PROMOTED THREAD (los hilos largos rinden muchísimo en 2026):
   - Tweet 1: hook que pare scroll (max 280 chars)
   - Tweets 2-7: argumentos/historia/valor
   - Tweet 8: CTA + link
   - Tweet 9: "Si te gustó..." engagement bait pero elegante

3. VIDEO AD (15-60 segundos):
   - Storyboard segundo a segundo
   - Hook visual primeros 2 segundos
   - Texto en pantalla (la gente ve sin sonido)
   - CTA visual

4. AMPLIFY (sponsoreas a un creador):
   - Brief para el creador
   - 3 angles que el creador puede usar (no script ce rrado)
   - Disclosure obligatoria

5. TAKEOVER (premium, para lanzamientos):
   - Para qué momento usar este formato
   - Copy del top-of-timeline ad

Reglas universales para X 2026:
- Cero hashtags genericos (#growth, #marketing)
- Máximo 1 emoji
- Url al final, NUNCA al inicio
- Cero "Hilo 🧵" como apertura (clié saturado)
- Hook tiene que ser opinion, contradicción o dato específico
```

**4. Hooks de tweets que paran el scroll**

```jsx
Para [producto/servicio] y mi angle [angle principal], escríbeme 20 hooks de apertura, 4 de cada uno de estos 5 estilos:

1. CONTRARIAN: opinión contraria al consenso del nicho
   Ej: "X estrategia que todos recomiendan es la peor para [problema]"

2. CONFESIÓN: vulnerabilidad credíble
   Ej: "Llevé [tiempo] cometiendo este error en [tema]. Hoy lo veo claro:"

3. STAT IMPACTANTE: dato + interpretación
   Ej: "[Dato puntual]. Lo que nadie cuenta es por qué pasa esto:"

4. PREGUNTA RETÓRICA: pregunta que el lector ya se hizo
   Ej: "¿Por qué [problema común] te sigue pasando aunque hagas [solución popular]?"

5. LISTA + HOOK NUMÉRICO:
   Ej: "3 cosas que aprendí después de [logro/fracaso] que cambiaron mi visión sobre [tema]:"

Para cada hook:
- Máx 240 chars (deja espacio para reply/retweet)
- Sin emojis ni hashtags
- Score 1-10 de probabilidad de viralidad orgánica (justificado)

Dame mi top 5 con prueba de A/B sugerida.
```

**5. Budget, KPIs y atribución en X Ads**

```jsx
Atribución en X es complicada. Ayúdame a armar el plan completo:

Budget total: [$X]
Duración: [X semanas]
Objetivo: [conversiones / leads / awareness / followers]
CPA/CPL objetivo: [$Y si lo sé]

Dame:

1. SPLIT DE BUDGET (% y $):
   - Prospecting vs Retargeting (recomendado 70/30 o 60/40)
   - Por formato (qué % a single tweets vs threads vs video)
   - Por audiencia (hero audience vs test audiences)

2. BENCHMARKS X 2026 PARA MI NICHO:
   - CPM esperado
   - CTR esperado
   - Engagement rate
   - CPA esperado
   - Si no sabes el benchmark exacto para mi nicho, dime el rango.

3. KPIs por objetivo (cuáles SI mirar, cuáles ignorar):
   - Para conversiones: ROAS, CPA, conversion rate
   - Para leads: CPL, lead quality score
   - Para awareness: reach, video views (3s/15s/completes), brand lift
   - Para followers: cost per follower + follower quality (no bots)

4. ATRIBUCIÓN:
   - X Pixel: cómo configurarlo bien (eventos clave)
   - UTM parameters: estructura sugerida
   - View-through window recomendado
   - Cómo manejar el "dark social" de X (la gente comparte vía DM, screenshot, sin link directo)

5. PLAN DE OPTIMIZACIÓN por semana:
   - Semana 1: setup + baseline data
   - Semana 2: pausar bottom 30% performers
   - Semana 3+: scaling de winners + refresh creative

Forma de entrega: tabla + checklist accionable.
```

*Tip pro:* X Premium ($8/mes) te da impressions extra orgánicas que reducen tu costo de adquirir followers en 40-60%. Vale la pena combinarlo con tus campañas de ads.
