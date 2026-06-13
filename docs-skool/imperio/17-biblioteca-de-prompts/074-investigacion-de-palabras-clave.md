# 🔥 Investigación de Palabras Clave

> Ruta: Biblioteca de Prompts › 🔥 Investigación de Palabras Clave

---

**Investigación de Palabras Clave:** No más listas de 100 keywords sueltas que nadie usa. Estos prompts arman clusters por intent, encuentran huecos competitivos y dejan listo el plan de contenido SEO de los próximos 3 meses.

**Recomendación de modelo:** **Claude (Opus o Sonnet)**. Si conectas el **MCP de Ahrefs, SimilarWeb o Google Search Console**, Claude trabaja con volumen real, KD, traffic, y data competitiva—no estimates inventados.

**1. Buyer persona + search intent real**

```jsx
Mi negocio: [qué vendo + a quién]
Mi sitio actual: [URL si aplica]
Objetivo del SEO: [traffic top funnel / leads / sales / autoridad]

Antes de tirar keywords, ayúdame a entender qué busca realmente mi audiencia:

1. PERSONA DE BÚSQUEDA:
   - 3 perfiles que buscan mi solución (no demográficos—situacionales)
   - Para cada uno: en qué momento del día buscan, qué contexto emocional, qué device

2. SEARCH INTENT POR FASE:
   - AWARENESS: 8 búsquedas "recién se enteran del problema"
   - CONSIDERATION: 8 búsquedas "comparando opciones"
   - DECISION: 8 búsquedas "listos para comprar"
   - POST-COMPRA: 5 búsquedas "ya compraron, buscan optimizar"

3. LENGUAJE REAL del cliente:
   - 10 frases exactas que dirían al buscar (no marketing-speak)
   - 5 sinónimos del problema (la gente lo nombra distinto)
   - 3 jergas/abreviaciones del nicho

4. PREGUNTAS TÍPICAS (formato natural):
   - 10 preguntas con "cómo", "por qué", "cuándo", "dónde"
   - 5 "X vs Y" comparaciones
   - 5 "mejor X para [contexto]"

Si tengo acceso al MCP de Google Search Console, valida contra mis queries reales.
```

**2. Cluster de keywords por intent**

```jsx
Basándote en el research anterior, genérame clusters de keywords (no listas sueltas):

Formato por cluster:
- NOMBRE del cluster (en una frase descriptiva)
- INTENT de búsqueda (informational / commercial / transactional / navigational)
- FASE del funnel
- KEYWORD PRINCIPAL del cluster (la más buscada del grupo)
- 5-10 keywords secundarias agrupadas (variaciones, sinónimos, long-tails)
- ESTIMATE de volumen mensual (rango si no es exacto)
- KD (keyword difficulty) aproximado
- TIPO DE CONTENIDO que rankearía (guide, listicle, comparison, tool, etc.)
- VALOR comercial 1-10 (qué tan cerca está de mi venta)

Objetivo: 8-12 clusters, ordenados por OPPORTUNITY SCORE (volumen alto, KD razonable, valor comercial alto).

Descarta clusters de gente que NUNCA me compraría (curiosos sin intent, estudiantes, etc.).

Si tienes el MCP de Ahrefs/SimilarWeb activo, usa data real. Si no, estima y marca [ESTIMATE].
```

**3. Long-tail mining + preguntas específicas**

```jsx
El SEO en 2026 vive en long-tails. Para mi nicho [nicho] y mis keywords principales, expandé a long-tails:

Para cada keyword principal (top 5):

1. 15-20 long-tails (4+ palabras):
   - Con "cómo + verbo"
   - Con "para [audiencia específica]"
   - Con "en [año/situación]"
   - Con modificadores: mejor / barato / rápido / sin / con / vs / cerca de

2. 10 preguntas "People Also Ask" estilo:
   - "¿Qué es...?"
   - "¿Cómo se...?"
   - "¿Cuánto...?"
   - "¿Cuándo...?"

3. 5 keywords "zero search volume" pero alta intención:
   - Frases muy específicas que casi nadie busca pero que CUANDO se buscan, convierten alto

4. Voice-search style:
   - 5 queries conversacionales (como hablamos, no como escribimos)

Para cada long-tail: estimate de volumen, KD, valor comercial.

Objetivo: 50-80 long-tails realistas para perseguir en los próximos 3-6 meses.
```

**4. Análisis competitivo de keywords**

```jsx
Quiero atacar las keywords donde mi competencia ya rankea pero puedo superarlos.

Mis competidores principales: [3-5 URLs]
Mis fortalezas (qué me hace diferente): [credenciales, experiencia, recursos]

Dame:

1. KEYWORDS QUE ELLOS RANKEAN Y YO NO:
   - Top 30 keywords donde tienen tráfico
   - Para cada una: posición promedio, volumen, KD
   - Mi probabilidad realista de superarlos (1-10) con justificación

2. KEYWORDS "WEAK CONTENT" DE LA COMPETENCIA:
   - Dónde rankean en top 10 con contenido mediocre/desactualizado
   - Qué mejorar yo para superarlos

3. KEYWORDS QUE "DEBERÍAN" RANKEAR Y NO LO HACEN:
   - Topics donde nadie está cubriendo bien
   - Hueco editorial real

4. ESTRATEGIA DE ATAQUE:
   - Quick wins (1-3 meses): keywords con KD bajo y traffic decent
   - Medium-term (3-6 meses): KD medio, traffic alto
   - Long-term/moonshots (6-12 meses): KD alto pero brand value

Si tengo MCP de Ahrefs/SimilarWeb activo, usa data real. Si no, marca [ESTIMATE].
```

**5. Plan de contenido SEO basado en gaps**

```jsx
Convierte los clusters y long-tails que armamos en un plan de contenido ejecutable para los próximos 3 meses:

Formato del plan por pieza:

| Mes | Semana | Título | Cluster | KW principal | KWs secundarias | Tipo (guide/listicle/comparison/tool) | Largo objetivo | KD | Volumen | Valor comercial 1-10 | Status | Internal links sugeridos |

Reglas:
- 2-3 piezas por semana (realista, no fantasioso)
- Mix de quick-wins (KD bajo) + autoridad (KD más alto)
- Cada pieza debe servir 1 keyword principal + 3-5 secundarias del mismo cluster
- Internal linking: cada nueva pieza linkea a 2-3 piezas existentes
- Pilar pages (1 por mes, gran cluster) + supporting articles (resto)

Además, dame:
- 5 ideas de "refresh" (posts míos viejos que actualizar)
- 3 ideas de "merger" (dos posts míos similares que combinar)
- 5 keywords para optimizar páginas que ya rankean en posición 11-20 (low-hanging fruit)

Formato: tabla markdown lista para pegar en Notion/Airtable.
```

*Tip pro:* Si tienes el **MCP de Google Search Console** conectado, dile a Claude "díme 10 queries donde aparezco en posición 11-15 con buen CTR". Esos son tus mejores quick-wins—ya casi rankeas y la gente sí clickea.
