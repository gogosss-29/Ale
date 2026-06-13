# Optimización para Conversiones

> Ruta: Biblioteca de Prompts › Optimización para Conversiones

---

**Optimización para Conversiones (Afiliados):** Aumenta el conversion rate de tu programa de afiliados sin necesidad de tráfico extra. Cambios específicos en copy, landing, oferta y secuencia que mueven la aguja.

**Recomendación de modelo:** **Claude (Opus o Sonnet)**. Conecta el **MCP de tu plataforma de afiliados + analytics** para que Claude trabaje con tu funnel data real.

**1. Audit del funnel actual**

```jsx
Mi setup:
- Producto: [qué vendo + precio]
- Tipo de tráfico de afiliados: [bloggers, YouTubers, email, social, cupones, etc.]
- Comisión: [%]
- Conversion rate actual: [%]
- EPC (Earnings Per Click): [$X]

Audítame el funnel completo:

1. CLICKS → LANDING:
   - ¿Qué % de clicks llegan realmente? (clicks fantasmas / bots)
   - Match score entre ad/post del afiliado y landing
   - Mobile vs desktop conversion gap

2. LANDING → ADD TO CART / SIGN UP:
   - Bounce rate y tiempo en página
   - Heatmap de dónde clickean / leen
   - Friction points (formularios largos, info confusa, oferta poco clara)

3. CART → CHECKOUT:
   - Abandono de carrito %
   - Razones típicas (precio, shipping, trust)

4. CHECKOUT → PURCHASE:
   - Conversion rate final
   - Pagos fallidos

5. BENCHMARKS por industria:
   - ¿Mi conversion rate está below/avg/above para mi tipo de producto?
   - Cuál es el target realista

Dame TOP 5 leaks del funnel ordenados por impacto en revenue si los arreglo.
```

**2. Landing pages por tipo de afiliado**

```jsx
Un afiliado bloguero envía tráfico distinto a uno de YouTube o uno de email. Misma landing = conversion subpar.

Mi producto: [producto]
Tipos de afiliados en mi programa: [lista]

Diseña 3 variantes de landing para los 3 segmentos más comunes:

LANDING A: TRÁFICO DE CONTENIDO LARGO (bloggers, newsletters):
- Asume más contexto (ya leyeron del producto)
- Hook: ir directo al beneficio específico
- Hero copy: 50-80 palabras
- Estructura: beneficios → social proof → oferta → CTA
- Length: 1 pantalla principal + scroll para detalles

LANDING B: TRÁFICO DE VIDEO (YouTubers, TikTokers):
- Asume contexto mínimo (vieron 30 seg)
- Hook: replica el angle del video
- Hero copy: muy corto, mostly visual
- Estructura: video corto + 3 bullets + CTA + FAQ
- Length: very short, mobile-first

LANDING C: TRÁFICO DE EMAIL (lista del afiliado):
- Asume warmth alta (confianza ya construida)
- Hook: referencia al afiliado ("[Nombre] te envía esto porque...")
- Hero copy: personal, no corporativo
- Estructura: preámbulo personal + oferta + CTA + reassurance
- Length: medium, copy-heavy ok

Para cada landing:
- Wireframe en markdown
- Copy completa de hero, beneficios, CTA
- Variables a personalizar por afiliado: [PLACEHOLDER]
- A/B test sugerido para cada uno
```

**3. Copy de ads/posts para afiliados (swipe files)**

```jsx
Los afiliados rinden cuando tienen copy listo para copiar/adaptar. Créame swipe files completos.

Mi producto: [producto + propuesta de valor]
Mi oferta actual: [precio + bonos + garantía]

Generáme swipe files por canal:

1. EMAIL SWIPES (5 emails listos):
   - 1 hook-style (curiosidad)
   - 1 storytelling ("así me cambió esto")
   - 1 problema/solución directo
   - 1 "3 razones" listicle
   - 1 último día / urgencia
   Cada uno: subject + body 200-400 palabras + CTA con link de afiliado [PLACEHOLDER]

2. SOCIAL POSTS (10 listos para cada red):
   - Twitter/X: 10 tweets (single + threads)
   - LinkedIn: 5 posts long-form + 5 short
   - Instagram: 5 captions + 5 ideas de Reel
   - TikTok: 5 hooks de video + outline

3. BLOG POSTS / ARTICLES:
   - 3 outlines de review largo (1500+ words)
   - 2 outlines de "X vs Y" comparison
   - 1 outline de "best of" listicle donde mi producto rankea top 3

4. SCRIPTS DE VIDEO (YouTube/TikTok):
   - 3 hooks de apertura (15 seg)
   - 2 scripts de review completo (5-8 min)
   - 1 script de "unboxing" demo

Reglas:
- Cero hype barato
- Honesto: incluir 1 desventaja del producto en cada review (genera confianza)
- Variables para personalizar: [TU EXPERIENCIA AQUÍ], [PARTE QUE MÁS TE GUSTÓ], etc.
- Compliance: incluye disclosure de afiliación donde requerido
```

**4. Ofertas + bonos exclusivos para afiliados**

```jsx
Las mejores conversiones de afiliados vienen de ofertas exclusivas que ELLOS pueden ofrecer y nadie más.

Mi producto base: [producto + precio]

Diseña 5 ofertas exclusivas que puedo dar a mis afiliados (no a tráfico directo):

1. BONUS BUNDLE (mismo precio, más valor):
   - 2-3 bonos específicos que cuesten poco crearlos pero parezcan high-value
   - Por qué son irresistibles
   - Cómo entregarlos técnicamente (auto-delivery o manual)

2. DESCUENTO LIMITADO (precio menor):
   - % de descuento sostenible para mi margen
   - Duración (24-72 horas funcionan mejor que 7 días)
   - Cómo evitar canibalizar mi precio principal

3. ACCESO ANTICIPADO:
   - A lanzamientos, features, o nuevos productos
   - Hace que la audiencia del afiliado se sienta VIP

4. GARANTÍA EXTENDIDA:
   - Mi garantía normal + X días adicionales
   - Reduce fricción de compra drásticamente

5. CONSULTA/COACHING INCLUIDO:
   - 30-60 min de tu tiempo o de tu team
   - Valor percibido alto, costo real bajo
   - Límite por mes para no morir de éxito

Para cada oferta:
- Mensaje sugerido para que el afiliado la promueva
- Conversion lift esperado vs oferta base
- Tipo de afiliado que más la aprovechará
- Costo real para mí (no asuma cero)
```

**5. Secuencia de retargeting de no-cierres**

```jsx
El 95% de los clicks de afiliados NO compran en la primera visita. Capturarlos con retargeting puede duplicar mi revenue del programa.

Mi tracking actual: [Pixel / GA / Server-side]
Mi pop-up/lead magnet: [sí/no, cuál]

Diseña la secuencia completa:

1. CAPTURA EN LANDING (pre-purchase):
   - Pop-up de salida con lead magnet (idea de cuál)
   - Form: solo email (sin nombre, sin teléfono)
   - Promesa: descuento, guía, o herramienta
   - Copy del pop-up (máx 30 palabras)

2. EMAIL SEQUENCE post-captura (no compraron aún):
   - Email 0 (instantáneo): entrega lead magnet + bridge a producto
   - Email 1 (día 2): caso de éxito de alguien parecido a ellos
   - Email 2 (día 4): manejo de la objeción más común (precio / tiempo / si funciona)
   - Email 3 (día 7): oferta exclusiva con timer
   - Email 4 (día 10): última oportunidad + plan B (si no compran, qué más pueden hacer)

3. RETARGETING ADS:
   - Audiencia: visitors de landing que NO compraron en 30 días
   - 3 creatives: testimonial / objection-handling / oferta
   - Budget sugerido (% del revenue por mes)

4. POR QUÉ NO COMPRARON (encuesta de 1 click):
   - Email con "¿Por qué no compraste aún?" 
   - 4 botones: precio / no era para mí / dudas / otro
   - Cómo accionar cada respuesta

Reglas: cero spam, cero falsa urgencia. Si la oferta es real, no necesita inventarse.
```

*Tip pro:* Conecta el **MCP de Klaviyo/Mailchimp + Google Analytics** en Claude. Cada lunes pide "qué mensaje del email sequence está con peor performance esta semana" y Claude detecta + sugiere el fix. CRO automático.
