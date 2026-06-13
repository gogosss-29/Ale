# Ideas para Textos Publicitarios

> Ruta: Biblioteca de Prompts › Ideas para Textos Publicitarios

---

**Textos Publicitarios:** Crea ad copy que convierte, no que solo "se escucha bien". Estos prompts están estructurados para que cada palabra trabaje a favor de tu funnel.

**Recomendación de modelo:** **Claude (Opus o Sonnet)**. Si tienes datos de campañas previas (CTR, CPA, qué funcionó), pégalos al inicio para que Claude aprenda tu marca.

**1. Mensaje central + ángulos**

```jsx
Mi producto/servicio: [qué es y a quién sirve]
Audiencia: [perfil específico, no "todos"]
Punto de dolor principal: [problema que resuelve]
Diferenciador: [por qué yo y no la competencia]
Objetivo del ad: [click / lead / venta directa / awareness]

Antes de escribir copy, ayúdame a clarificar:

1. UN solo mensaje central (lo que mi audiencia debe internalizar). Máximo 12 palabras.
2. 5 ángulos creativos distintos para vender este mensaje:
   - Ángulo TRANSFORMACIÓN (antes vs después)
   - Ángulo AUTORIDAD (por qué saber esto)
   - Ángulo PROBLEMA AGITADO (qué pasa si no lo resuelves)
   - Ángulo CONTRARIAN (contra el consenso del nicho)
   - Ángulo URGENCIA (timing/escasez/oportunidad)
3. Para cada ángulo:
   - Mensaje en 1 frase
   - Estado emocional que despierta
   - Plataforma donde funciona mejor
4. Mi top 2 ángulos con justificación (cuáles explotar primero).

Objetivo: que el copy posterior tenga un norte claro, no improvisación.
```

**2. Hooks que paran scroll (5 estilos)**

```jsx
Para mi ángulo elegido [ángulo], escríbeme 15 hooks de apertura, 3 de cada uno de estos 5 estilos:

1. PREGUNTA ESPEJO: pregunta que el lector ya se hizo en voz baja
2. STAT IMPACTANTE: dato concreto + interpretación (marca [VERIFICAR] si dudoso)
3. CONFESIÓN: vulnerabilidad credíble ("Llevé X tiempo cometiendo este error...")
4. CONTRARIAN: opinión que va contra el consenso
5. PROMESA ESPECÍFICA: "En [tiempo] consigues [resultado concreto]"

Reglas para cada hook:
- Máximo 12 palabras
- Sin clichés (¿Ya probaste todo? ¿Te sientes atascado? ¿Quieres resultados?)
- Cero emojis
- Cero signos de exclamación
- Debe poder funcionar solo, sin contexto

Para cada uno, dame:
- Score 1-10 de probabilidad de detener el scroll
- Predicción de en qué plataforma rendirá mejor

Dame mi top 5 con justificación + recomendación de A/B test.
```

**3. Variantes A/B/C de ad body**

```jsx
Para mi mejor hook [hook elegido], escríbeme el cuerpo del ad en 3 longitudes para A/B testear:

VERSIÓN CORTA (50-80 palabras, para feeds rápidos como IG/TikTok):
- Hook (1 frase)
- 1-2 beneficios concretos
- 1 prueba (cifra, ejemplo, testimonial corto)
- CTA único

VERSIÓN MEDIA (120-180 palabras, estándar para Facebook/IG feed):
- Hook
- Storytelling micro (problema → cambio → resultado)
- 2-3 beneficios específicos
- Prueba más sustancial
- CTA

VERSIÓN LARGA (300-500 palabras, para LinkedIn/email/sales pages):
- Hook potente
- Identificación con el problema
- Por qué los métodos comunes fallan (sin atacar competencia directa)
- Mi propuesta diferente
- Beneficios + caso de éxito
- Manejo de 1-2 objeciones
- Garantía/risk reversal
- CTA con urgencia legítima

Reglas universales:
- Cero "¡Hola!" o "¿Qué tal?"
- Frases cortas (máximo 18 palabras)
- Lenguaje del cliente, no del marketer
- Una idea por párrafo

Marca con [VARIABLE: explicación] todo lo que requiera dato específico mío (precio, fechas, números).
```

**4. CTAs + disclaimers que convierten**

```jsx
Para el ad que escribimos, dame:

1. CTAS PRINCIPALES (5 variantes):
   - 1 directo ("Comprar ahora")
   - 1 de bajo compromiso ("Ver demo de 2 min")
   - 1 con beneficio implícito ("Obtener mi guía gratis")
   - 1 con urgencia ("Asegurar mi cupo antes del [fecha]")
   - 1 conversacional ("Hablemos 15 minutos")

Para cada uno:
- Cuándo usarlo (frialdad de audiencia, fase del funnel)
- Predicción de CTR vs el resto
- En qué plataforma encaja

2. MICRO-COPY de soporte (lo que va alrededor del CTA):
   - 2-3 variantes de "trust signal" ("Sin tarjeta", "Cancela cuando quieras", "Garantía 30 días")
   - 1 variante de remover fricción ("Solo 2 minutos", "No requiere instalación")

3. DISCLAIMERS NECESARIOS:
   - Para ofertas: ¿qué letra pequeña es obligatoria?
   - Para garantías: cómo redactarlas sin generar dudas
   - Para datos/resultados: cómo respaldar sin sonar a abogado

Objetivo: que el CTA sea el más natural para esa audiencia en esa fase—no el más agresivo.
```

**5. Adaptación multi-plataforma del mismo mensaje**

```jsx
Tomá el ad copy que escribimos y adaptalo nativo a cada plataforma. UN solo mensaje, 6 packagings distintos:

1. META (FB/IG) FEED IMAGE AD:
   - Headline (40 chars)
   - Primary text (125 chars visible, hasta 500 expand)
   - Description (30 chars)

2. META REELS/STORIES:
   - Texto en pantalla (5-8 palabras)
   - Hook visual (qué mostrar en segundo 1)
   - Voz/script (15-30 segundos)

3. TIKTOK NATIVE:
   - Hook (primeras 1.5 segundos)
   - Caption corto (max 150 chars)
   - Trend audio sugerido

4. LINKEDIN SPONSORED CONTENT:
   - Versión long-form profesional (200-300 palabras)
   - Tono: más data y autoridad, menos hype

5. GOOGLE SEARCH AD:
   - 3 headlines de 30 chars
   - 2 descripciones de 90 chars
   - 4 sitelinks

6. EMAIL SUBJECT + PREVIEW:
   - 3 subjects de 40 chars
   - 3 preview texts de 90 chars
   - First sentence del email que enganche

Reglas:
- Mensaje central NUNCA cambia
- Tono se adapta al canal
- Cero copy-paste literal entre plataformas (cada una su sabor)
- Marca con [VERIFICAR LIMITS] si los caracteres exactos cambiaron en la plataforma
```

*Tip pro:* Conecta el **MCP de Meta Ads o Google Ads** en Claude y dile "crea estos 6 ads como drafts en mi cuenta". Te ahorra la mitad del trabajo manual.
