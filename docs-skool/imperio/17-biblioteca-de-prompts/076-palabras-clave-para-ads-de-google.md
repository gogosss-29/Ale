# Palabras Clave para Ads de Google

> Ruta: Biblioteca de Prompts › Palabras Clave para Ads de Google

---

**Palabras Clave para Google Ads:** Google Ads en 2026 es 80% Performance Max + AI. Pero las keywords siguen importando para Search campaigns. Estos prompts están hechos para el Google Ads actual, no el de 2020.

**Recomendación de modelo:** **Claude (Opus o Sonnet)**. Si conectas el **MCP de Google Ads / Search Console**, Claude trabaja con tu data real (queries que ya te impresionan, CTR, conversiones).

**1. Match types + modificadores estratégicos**

```jsx
Mi negocio: [qué vendo + a quién]
Ubicación: [país/regiones objetivo]
Language targeting: [Español / Español Latam / Español España / Multiidioma]
Budget: [$X mensual]
Objetivo: [conversions / leads / calls / store visits]

Dame un plan de keywords completo según los match types actuales de Google Ads 2026:

1. EXACT MATCH (top intent):
   - 15 keywords con bracket [exact]
   - Para cada una: estimate volumen mensual, CPC esperado, intent score 1-10

2. PHRASE MATCH (mid intent):
   - 15 keywords con "phrase"
   - Idem datos

3. BROAD MATCH (descubrimiento, con audience signals):
   - 10 keywords broad
   - Audience signals a combinar (Google ahora REQUIERE esto para broad)
   - Cómo evitar que se desboque

4. NEGATIVE KEYWORDS (crítico para no desperdiciar plata):
   - 30 negatives obligatorios
   - Categorías: gratis, DIY, jobs, definición, queja, competencia
   - Match type para cada

5. CAMPAIGN STRUCTURE recomendada:
   - Cuántas campañas separar y por qué
   - Cuántos ad groups dentro de cada

Si tengo MCP de Google Ads/Search Console activo, valida volumen contra mi data real.
```

**2. SKAG y STAG: estructura de high-performance**

```jsx
SKAGs (Single Keyword Ad Groups) y STAGs (Single Theme Ad Groups) siguen siendo lo más rentable para Search en 2026.

Para mi top 10 keywords de mayor intent, arma:

Por cada SKAG:
- Ad group name
- Keyword única + match types
- Negative keywords específicos
- 3 Responsive Search Ads (con 15 headlines + 4 descriptions cada uno)
- Sitelinks recomendados (4)
- Callouts recomendados (4)
- Structured snippets

Formato de los Responsive Search Ads:
- 15 HEADLINES (30 chars max):
  * 3 con keyword exacta
  * 3 con beneficio
  * 3 con CTA
  * 3 con prueba/social proof
  * 3 con urgencia/oferta
- 4 DESCRIPTIONS (90 chars max):
  * 1 con propuesta de valor
  * 1 con beneficio específico
  * 1 con prueba/garantía
  * 1 con CTA fuerte
- PINS estratégicos

Objetivo: Quality Score 8-10 en cada keyword principal.
```

**3. Negative keywords (donde se ahorra/pierde la plata)**

```jsx
Negatives mal hechos te queman dinero. Vamos a hacerlos bien.

Mi negocio: [qué vendo]
Lo que NO vendo: [exclusiones explícitas]
Mi audiencia: [perfil]

Dame:

1. NEGATIVE KEYWORDS POR CATEGORÍA:
   - GRATIS/CHEAP: 15 keywords
   - DIY/HAZLO TÚ: 10 keywords
   - JOBS/EMPLEO: 10 keywords
   - DEFINICIÓN: 10 keywords
   - QUEJA/PROBLEMA: 10 keywords
   - COMPETENCIA: nombres + sus productos

2. NEGATIVE LIST master compartida:
   - 100+ negativos para aplicar transversalmente

3. NEGATIVES DINÁMICOS (revisar semanal):
   - Cómo identificar nuevos del Search Terms Report
   - Threshold: 100 impresiones sin conversión
   - Workflow semanal: 30 min de mantenimiento

4. NEGATIVES PARA SHOPPING/PMAX:
   - Diferencias vs Search
   - Cómo se aplican (query exclusions)

Si tengo MCP de Google Ads, análizame los search terms actuales y propone negativos específicos.
```

**4. Quality Score: cómo subir de 4 a 8+**

```jsx
Quality Score es la palanca más subestimada. Subir de 4 a 8 puede bajar tu CPC 50%.

Mi data: [pega tabla con keywords + actual QS + actual CPC]

Para cada keyword con QS <6, análizame los 3 componentes:

1. EXPECTED CTR (33% del peso):
   - Cómo mejorar: ad copy más relevante, keyword en headline, oferta clara
   - Acción específica

2. AD RELEVANCE (33% del peso):
   - Cómo mejorar: keyword en headline 1, SKAG/STAG
   - Acción específica

3. LANDING PAGE EXPERIENCE (33% del peso):
   - Cómo mejorar: LP específica por keyword, velocidad, mobile, content match
   - Acción específica

Plan de 4 semanas:
- Semana 1: fix los 5 keywords más caros con QS bajo
- Semana 2: refactor ad copy (más SKAGs)
- Semana 3: mejorar landing pages
- Semana 4: A/B test + medir QS shift

ROI esperado: subir QS promedio 2 puntos = CPC baja 25-40%.
```

**5. Performance Max + AI en 2026**

```jsx
Performance Max (PMax) ya no es opcional. Pero hay que dominarlo:

Mi setup: [solo Search / Search + PMax / migrando a PMax]
Objetivo: [conversions / leads / sales]

1. CUÁNDO USAR PMAX vs SEARCH:
   - PMax: data alta de conversiones, mültiples assets, omnicanal
   - Search: intent alto puro, control granular, ABM
   - Hybrid: PMax + Brand Search separado

2. ASSETS QUE PMAX NECESITA:
   - 5+ headlines (30 chars)
   - 5+ long headlines (90 chars)
   - 5+ descriptions (90 chars)
   - 5+ imágenes (1.91:1, 1:1)
   - 1+ logo
   - 1+ video (30 seg mínimo)
   - Final URL list

3. AUDIENCE SIGNALS:
   - Customer list
   - In-market audiences
   - Custom segments
   - Affinity audiences
   - Lookalikes

4. EXCLUSIONS:
   - Brand keywords
   - Geos, content categories problemáticos

5. SEÑALES PARA EL ALGORITMO:
   - Eventos de conversión correctos
   - Enhanced Conversions activado
   - Value-based bidding
   - Offline conversions imported

6. WARNINGS:
   - Spend yendo a Display/YouTube sin conversión
   - Brand search canibalizando
   - CPA volatility (30+ días para estabilizar)

Dame mi roadmap específico de 60 días.
```

*Tip pro:* Conecta el **MCP de Google Ads** + el **MCP de Google Sheets**. Pide a Claude que cada lunes exporte tus search terms a un sheet, identifique nuevos negativos, y te diga los top 3 cambios a hacer. 15 min semanales = miles ahorrados al año.
