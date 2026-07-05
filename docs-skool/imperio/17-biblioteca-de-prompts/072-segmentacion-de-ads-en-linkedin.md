# Segmentación de Ads en LinkedIn

> Ruta: Biblioteca de Prompts › Segmentación de Ads en LinkedIn

---

**Ads en LinkedIn:** LinkedIn es la plataforma B2B más cara pero con el mejor LTV. La clave no es segmentar por demografías, es por comportamiento profesional + ABM. Estos prompts están hechos para sacarle el mejor ROI a la plataforma más premium.

**Recomendación de modelo:** **Claude (Opus o Sonnet)**. Si vendes B2B, conecta el **MCP de HubSpot/Salesforce** para que Claude tenga tu CRM y proponga targeting basado en tus mejores clientes reales.

**1. Definición del ICP para LinkedIn**

```jsx
Mi producto/servicio: [qué vendo]
Mercado: [B2B / B2C-premium / SaaS / consultoría / etc.]
Precio promedio: [ticket size aprox]
Ciclo de venta: [días/semanas/meses]

Necesito definir mi ICP (Ideal Customer Profile) para LinkedIn Ads. NO me des perfiles genéricos—quiero precisión.

Dame:

1. EMPRESA OBJETIVO:
   - Tamaño (employees): rango exacto
   - Revenue: rango exacto
   - Industrias prioritarias (top 3, no "todas")
   - Tecnologías que usan (LinkedIn permite targetearlo)
   - Stage de crecimiento (startup, scale-up, enterprise)

2. DECISION MAKERS:
   - Job titles exactos (no familias amplias)
   - Seniority: VP / Director / Manager / IC con poder
   - Function: marketing / sales / ops / product / engineering

3. INFLUENCERS dentro de la cuenta (los que NO firman pero recomiendan):
   - Job titles
   - Por qué importan para mi ciclo de venta

4. ANTI-PERSONA (a quien NO quiero alcanzar):
   - Titles a excluir
   - Industrias a excluir
   - Tamaños de empresa a excluir

5. SEÑALES DE INTENT:
   - Skills que indican intent de compra
   - Groups que sigue mi ICP
   - Activity reciente que predice compra (job change, funding raise, etc.)

Formato: tabla + bullets. Si tienes acceso a mi CRM (MCP), valida contra mis customers reales.
```

**2. Targeting B2B: matched audiences + ABM**

```jsx
Basándote en el ICP, estructura el targeting de LinkedIn Ads. Budget: [$X]. Duración: [X semanas].

1. ABM (ACCOUNT-BASED MARKETING):
   - Lista de 50-100 cuentas target (¿las tengo o necesito construir?)
   - Subida como Matched Audience
   - Estructura: una campaña por tier de cuenta (tier 1 = top 20, tier 2 = mid 30, etc.)
   - Frecuencia objetivo por cuenta (saturation cap)

2. MATCHED AUDIENCES (warm):
   - Customer list (uploaded)
   - Website retargeting (windows: 30/90/180)
   - Engagers de mis posts orgánicos
   - Video viewers de mis videos orgánicos

3. LOOKALIKES:
   - LAL de customers de más alto LTV
   - LAL de engagers (cuidado: a veces atrae fans, no buyers)

4. ATTRIBUTE TARGETING (cold):
   - Combina: Industry + Job Function + Seniority + Company Size
   - 3-4 variantes para A/B testing
   - JUSTIFICA por qué cada combo

5. EXCLUSIONES OBLIGATORIAS:
   - Customers actuales
   - Competencia (employees de tus competidores)
   - Otros países (si aplicable)

6. PRESUPUESTO SUGERIDO POR CAMPAÑA:
   - LinkedIn requiere mínimos relativamente altos para que el algoritmo aprenda
   - Recomienda spend mínimo por ad set para que sea estadísticamente significativo

Dame todo en una tabla estructurada.
```

**3. Document Ads + Lead Gen Forms (los formatos más rentables)**

```jsx
LinkedIn tiene dos formatos que rinden muchísimo más que el resto: Document Ads (PDFs en el feed) y Lead Gen Forms (formularios in-app sin landing).

Para mi oferta [oferta/asset]:

1. DOCUMENT AD (10-15 páginas, PDF nativo en feed):
   - Concepto del documento (ej: "State of [industry] 2026")
   - Outline página por página:
     * Pág 1: cover impactante
     * Pág 2: índice / TL;DR
     * Pág 3-12: contenido valioso (no venta—genuine value)
     * Pág 13-14: case study/social proof
     * Pág 15: CTA suave
   - Estilo visual: corporativo pero legíble
   - Copy del post que acompaña el ad (máx 100 palabras)

2. LEAD GEN FORM:
   - Form pre-filled (LinkedIn rellena con info de perfil):
     * Campos mínimo viables: name, email, company, title
     * Pregunta custom para qualifier
   - Headline del form
   - Sub-headline
   - Privacy policy disclaimer
   - Thank you message + next step
   - Auto email post-submit (subject + body corto)

3. MÉTRICAS REALISTAS:
   - CPL esperado para mi nicho
   - Conversion rate del lead gen form
   - Lead quality score

4. SECUENCIA POST-LEAD:
   - Email 1 (instantáneo): entrega + CTA suave
   - Email 2 (día 2): valor adicional
   - Email 3 (día 5): caso de éxito + CTA a llamada
   - SDR/sales handoff (cuándo y cómo)
```

**4. Copy para LinkedIn (long-form, profesional)**

```jsx
LinkedIn no es Twitter/IG. La gente lee más, scrolea más lento, espera contenido sustancial. Escríbeme 3 variantes de copy para Sponsored Content:

Mi oferta: [oferta]
Angle: [argumento principal]
Audiencia: [perfil profesional]

1. STYLE "INSIGHT + DATA" (350-500 palabras):
   - Hook: insight contrarian o data point sorprendente
   - Desarrollo: 2-3 puntos clave con respaldo
   - Bridge a mi oferta
   - CTA suave

2. STYLE "STORY" (400-600 palabras):
   - Hook: "Llevábamos [tiempo] intentando..."
   - Narrativa: situación → conflicto → cambio → resultado
   - Lesson learned
   - Conexión con mi oferta

3. STYLE "CHECKLIST" (200-300 palabras):
   - Hook: pregunta
   - 5-7 bullets de criterio
   - CTA: "si reconociste 3+ de estos, hablemos"

Reglas para LinkedIn 2026:
- Primeras 2 líneas tienen que parar el scroll
- Saltos de línea generosos
- Máximo 1 emoji
- Cero "¡Hola comunidad!" o "Espero que estén bien"
- Cero hashtags al inicio (al final, 3-5 máximo)
- Cero disculpas por publicar
- Mencionar @ a alguien relevante si suma valor real

Para cada variante: predicción de engagement esperado + cuándo usar.
```

**5. ABM + sales handoff coordinado**

```jsx
El error típico en LinkedIn Ads B2B es no coordinar con sales/outbound. Diseñemos un playbook integrado:

Mi setup: [solo ads / ads + SDR / ads + sales team / ads + me]

1. AIR COVER (LinkedIn Ads):
   - 4-6 semanas de exposición a cuentas target ANTES del outbound
   - Contenido: educativo + social proof + thought leadership
   - Frecuencia objetivo: 5-8 impresiones por cuenta

2. INTENT DATA (qué mirar antes de outreach):
   - ¿Quién vio el ad?
   - ¿Quién hizo engagement?
   - ¿Quién descargó el lead magnet?
   - ¿Quién visitó mi pricing/contacto después?

3. SDR/SALES HANDOFF:
   - Trigger: account ha tenido X impresiones AND Y persona ha hecho engagement
   - Mensaje personalizado al engagement
   - Template del primer mensaje
   - Cadencia: 4-6 touches en 2 semanas

4. RETARGETING DE NO-CIERRES:
   - Si tuvieron meeting pero no cerraron: campaña con case study
   - Si abrieron pero no respondieron: campaña de agitation

5. MÉTRICAS DEL PIPELINE:
   - Cost per Influenced Pipeline
   - Cost per Meeting Set
   - Cost per Opportunity
   - Cost per Closed Won
   - Sales velocity con vs sin air cover

Objetivo: que cuando el SDR mande el primer mensaje, la persona ya sienta que conoce a la marca.
```

*Tip pro:* Si conectas el **MCP de HubSpot/Salesforce** + LinkedIn Sales Navigator en Claude, puedes pedirle "de mis 50 cuentas target, dime cuáles tuvieron actividad reciente que indique intent". Claude lo cruza y prioriza el outreach de tu SDR.
