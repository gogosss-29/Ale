# Análisis de Métricas de Rendimiento

> Ruta: Biblioteca de Prompts › Análisis de Métricas de Rendimiento

---

**Análisis de Métricas de Rendimiento (Afiliados):** Lee los números como un media buyer veterano. Identifica qué afiliados rinden, cuáles queman recursos, y dónde escalar.

**Recomendación de modelo:** **Claude (Opus o Sonnet)**. Conecta el **MCP de tu plataforma de afiliados + Google Sheets** para que Claude analice tu data real.

**1. Dashboard maestro de métricas clave**

```jsx
Mi plataforma: [Refersion/Impact/Tapfiliate/GHL/etc.]
Período: [últimos 30/90/365 días]

Diseñame el dashboard ejecutivo:

1. MÉTRICAS DE VOLUMEN:
   - Total clicks generados
   - Total ventas atribuidas
   - Revenue total / pagado / pendiente
   - # afiliados activos vs total

2. MÉTRICAS DE EFICIENCIA:
   - EPC (Earnings Per Click) promedio
   - CR (Conversion Rate) global y por afiliado
   - AOV (Average Order Value) por afiliado
   - LTV de un cliente referido vs cliente directo

3. MÉTRICAS DE SALUD:
   - % afiliados activos (venta en últimos 30 días)
   - Churn rate mensual
   - Concentración: % revenue del top 10%
   - Tiempo promedio de primera venta

4. MÉTRICAS DE CALIDAD:
   - Refund rate por afiliado
   - Chargeback rate
   - LTV de referidos vs directos
   - Fraud signals (clicks anómalos, conversiones sospechosas)

5. COMPARACIÓN vs período anterior:
   - % cambio en cada métrica
   - Trends (subiendo / bajando / estable)

Formato: tabla markdown, máximo 1 página.
```

**2. Segmentación por tipo de afiliado**

```jsx
No todos los afiliados son iguales. Segmenta:

1. POR TIER DE PERFORMANCE:
   - Top 10% (héroes): qué hacen distinto, cómo replicarlo
   - Top 11-30%: qué los frena de subir
   - Bottom 70%: ¿reactivar o cortar?

2. POR CANAL DEL AFILIADO:
   - YouTube creators: CR, EPC, LTV
   - Bloggers/SEO
   - Email/Newsletter
   - Social (IG/TikTok/X)
   - Comunidad/Mastermind

3. POR TIEMPO EN EL PROGRAMA:
   - 0-3 meses: % que hace primer venta
   - 3-12 meses: growth rate
   - 12+ meses: retention vs churn

4. POR GEOGRAFÍA:
   - Top 5 países
   - CR + AOV por geografía

5. POR TIPO DE CONTENIDO:
   - Reviews / comparison / tutorial / listicle
   - Cuál convierte mejor

IDENTIFICA insights accionables: "el canal X tiene EPC 3x mayor" → acción: reclutar más de X.
```

**3. Análisis de outliers (top + bottom)**

```jsx
El 80/20 es real. Estudia tu top 10%.

Para TOP 10 afiliados:

1. PERFIL DETALLADO:
   - Plataforma + audiencia
   - Tipo de contenido sobre tu producto
   - Frecuencia de menciones
   - Tiempo en programa
   - Comisión actual

2. PATRONES en común:
   - 4-6 cosas que hacen igual
   - Lo que NO hace el resto

3. PLAYBOOK REPLICABLE:
   - 5-7 best practices
   - Cómo entrenar al middle pack

Para BOTTOM 10 (60+ días activos sin venta):

1. ¿Por qué no convierten?:
   - Audiencia mismatch
   - Promoción inconsistente
   - Asset/educación inadecuada
   - Tracking issues

2. ROI de reactivar vs cortar:
   - Costo de reactivar
   - Upside realista
   - Cuándo decir "se acabó" elegante

Plan accionable: top 5 a duplicar, bottom 5 a cortar.
```

**4. Detección de fraude**

```jsx
El fraude puede quemar 10-20% del programa sin que te des cuenta.

1. PATRONES SOSPECHOSOS:
   - Spikes de clicks sin contenido publicado
   - CTR >30% en posts orgánicos (signal de bots)
   - Conversiones desde geografías raras
   - Refund rate >20% en un afiliado
   - Múltiples cuentas desde mismo IP
   - Cookies stuffing patterns

2. INVESTIGACIÓN por sospechoso:
   - Source de su tráfico
   - Quality de audiencia (engagement vs followers)
   - Histórico: ¿consistente o spikes raros?

3. POLÍTICAS de fraud prevention:
   - Min holding period antes de pagar (30/60/90 días)
   - Auditoría automatizada con thresholds
   - Penalizaciones claras en T&C
   - Proceso de disputa justo

4. ACCIONES por nivel:
   - Sospecha leve: warning + monitoreo
   - Moderada: hold pagos + investigación
   - Confirmado: ban + reverse payouts

5. PROTECCIÓN legal en T&C

Si conectas MCP de plataforma, identifica top 5 sospechosos AHORA.
```

**5. Forecasting + budget allocation**

```jsx
Predecí los próximos 90 días y decidí dónde invertir.

Mi data histórica: [últimos 6-12 meses]
Target del trimestre: [$X o Y% growth]

1. FORECAST realista:
   - Revenue proyectado según tendencia
   - Range: pesimista / realista / optimista
   - Assumptions críticos

2. GAP ANALYSIS:
   - Distancia entre forecast y target
   - Cómo cerrarla (más afiliados / mejor performance / mejor oferta / mix)

3. BUDGET ALLOCATION para el trimestre:
   - $ / tiempo para reclutamiento
   - $ / tiempo para retention de existing
   - $ / tiempo para creative/asset dev
   - $ / tiempo para contests/incentives
   - $ / tiempo para tech (plataforma, MCPs)

4. KPIs DEL TRIMESTRE:
   - Top 3 métricas weekly
   - Threshold para celebrar / corregir / cambiar

5. RIESGOS Y MITIGACIONES:
   - ¿Qué podría salir mal?
   - Plan B si revenue cae 30%
   - Plan C si top afiliado se va

Formato: 1 página para partner meeting.
```

*Tip pro:* Crea un **scheduled task en Claude** que cada lunes a las 8am extraiga métricas del MCP de afiliados y te mande el dashboard ejecutivo + top 3 acciones de la semana. Cero esfuerzo manual.
