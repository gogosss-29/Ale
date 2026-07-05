# Análisis del Rendimiento de Anuncios

> Ruta: Biblioteca de Prompts › Análisis del Rendimiento de Anuncios

---

**Análisis del Rendimiento de Anuncios:** Lee tus datos como un media buyer veterano. Estos prompts te ayudan a auditar, diagnosticar, optimizar y decidir dónde scalar o cortar.

**Recomendación de modelo:** **Claude (Opus o Sonnet)**. Conecta el **MCP de Meta Ads / Google Ads / TikTok Ads** y Claude analiza directo con tu data real. Si no, exporta CSV y pégalo.

**1. Auditoría completa del estado actual**

```jsx
Mis cuentas de ads: [plataformas]
Período a auditar: [últimos 30/60/90 días]
Objetivo del negocio: [conversiones / leads / awareness / sales]
CPA/CPL objetivo: [$X]

Audítame todo:

1. HEALTH CHECK por cuenta:
   - Spend total + tendencia
   - CPA promedio + tendencia
   - ROAS promedio + tendencia
   - Frequency (warning si > 3.5)
   - Account quality score / health (si la plataforma lo da)

2. ESTRUCTURA:
   - ¿Cuántas campañas activas vs deberían ser?
   - ¿Audience overlap detectable?
   - ¿Creative fatigue indicators?
   - ¿Naming convention consistente?

3. TOP / BOTTOM PERFORMERS:
   - Top 5 ad sets por ROAS
   - Bottom 5 ad sets (candidatos a pausar)
   - Top 5 creatives + por qué funcionan
   - Worst 5 creatives + qué tenían en común

4. ATRIBUCIÓN:
   - Configuración actual de Pixel/CAPI
   - Eventos clave configurados correctamente
   - View-through window adecuado
   - iOS impact (si aplica)

5. SEÑALES DE WARNING:
   - CPA subiendo M-o-M
   - Frequency subiendo sin scale
   - CTR cayendo más del 20%
   - Quality score bajando

Formato: ejecutivo de 1 página + tabla detallada para drill-down.
```

**2. Diagnóstico de problemas específicos**

```jsx
Mi problema concreto: [describe el síntoma—ej: "CPA subió 40% en 2 semanas" o "CTR cayó al 0.5%"]
Mi data adjunta: [pega tabla con cifras o screenshot del dashboard]

Diagnóstico estructurado:

1. POSIBLES CAUSAS (ranked por probabilidad):
   - Audience saturation / fatigue
   - Creative fatigue
   - Competition spike (otros entraron al mercado)
   - Algoritmo cambió (plataforma ajustó algo)
   - Tracking se rompió (iOS, Pixel, etc.)
   - Landing page degradada
   - Producto / oferta perdió atractivo
   - Cambio de estación / mercado

2. PARA CADA CAUSA, cómo verificarla:
   - Qué métrica específica mirar
   - Threshold que indica el problema
   - Cómo separar correlación vs causalidad

3. PLAN DE ACCIÓN por causa:
   - Hipótesis confirmada → acción inmediata
   - Hipótesis falsa → siguiente sospechosa

4. TIMELINE de recuperación:
   - Cuánto deberían tardar las acciones en mostrar impacto
   - Cuándo declarar que algo sí está rotto vs noise normal

IMPORTANTE: si no hay data suficiente para diagnosticar algo, dilo explícitamente. No inventes.
```

**3. Reporting ejecutivo (qué importa, qué no)**

```jsx
Necesito presentar resultados a [stakeholder: client / boss / team / partners].

Mi data: [pega resumen o conecta MCP]
Período: [días/semanas/mes]
Audiencia del reporte: [nivel de sofistic. del que lo lee—técnico vs business vs ambos]

Arma un reporte ejecutivo de 1 página con:

1. TL;DR (3 frases):
   - ¿Qué logramos?
   - ¿Dónde estamos vs objetivo?
   - ¿Qué harías próximamente?

2. MÉTRICAS CLAVE (máximo 5—no diluyas):
   - Total spend
   - Conversiones/leads/sales
   - CPA / CPL / ROAS
   - vs período anterior (% cambio)
   - vs objetivo (% sobre o bajo)

3. 3 WINS específicos:
   - Con números
   - Con causa identificada

4. 3 MISSES con plan de recuperación:
   - Diagnostic completo (no "no funcionó")
   - Acción específica para fix
   - Timeline esperado

5. PRÓXIMOS PASOS (prioritized):
   - Top 3 acciones para la próxima semana/mes
   - Resource needs (más budget, más creatives, tracking fix, etc.)

Reglas:
- Cero jerga sin explicar
- Cero gráfico que no aporte decisión
- Cifras absolutas + relativas ("vendimos $20k = 18% más que el mes pasado")
- Honestidad sobre lo que NO sabemos aún
```

**4. Optimización por palanca**

```jsx
Tengo presupuesto limitado de tiempo. Dime exactamente qué palancas mover esta semana para mejorar [métrica específica].

Mis datos: [pega o conecta MCP]
Métrica a mejorar: [CPA / CTR / ROAS / conversion rate / etc.]
Métrica objetivo: [$X o Y%]
Tiempo: [esta semana / próximas 2 semanas]

Dame las 4 palancas en orden de impacto esperado:

PALANCA 1: AUDIENCIAS
- Top 3 cambios específicos a probar
- Impacto esperado (rango)
- Cómo medir si funcionó
- Effort: bajo / medio / alto

PALANCA 2: CREATIVES
- Top 3 cambios específicos
- Idem

PALANCA 3: BUDGET / BIDDING
- Top 3 cambios específicos
- Idem

PALANCA 4: LANDING PAGE / FUNNEL
- Top 3 cambios específicos
- Idem (advertencia: cambios fuera del ad tardan más en mostrar impacto)

Después, dame mi TOP 3 ACCIONES (de las 12 propuestas):
- Lo que más mueve la aguja con menor esfuerzo
- En qué orden ejecutarlas
- Qué NO tocar (evitar tinkering destructivo)

Objetivo: salir del análisis con 3 acciones que voy a ejecutar HOY, no con un brief de 50 ideas.
```

**5. Decisiones: scaling, pausar, o mantener**

```jsx
Para cada campaña/ad set activo, ayúdame a decidir: SCALE / MANTENER / PAUSAR / MATAR.

Mis datos: [tabla con campañas activas + spend + ROAS + CPA + frequency + días activa]
Threshold de mi negocio:
- ROAS mínimo aceptable: [X]
- CPA máximo aceptable: [$Y]
- Frequency max: [3.5 / 4 / 5—depende de mi modelo]

Decision matrix por campaña:

1. SCALE (subir budget):
   - Criterios: ROAS > target Y%, frequency < 3, spend < 20% del budget total
   - Cuánto subir: regla de “máximo 20-30%/día” para no romper learning
   - Cuándo duplicar ad set vs subir budget

2. MANTENER (no tocar):
   - Criterios: dentro de threshold, learning phase, fresh creative
   - Por qué NO tocar (every change resets learning)

3. PAUSAR (parar temporalmente):
   - Criterios: degradación reciente pero recuperable
   - Por cuánto tiempo
   - Qué cambiar antes de relanzar

4. MATAR (cerrar definitivamente):
   - Criterios: ROAS < 50% del target sostenido por 7+ días, frequency alta sin escapatoria
   - Cómo "retirar" sin perder el learning de la cuenta

Para cada campaña en mi lista, dame:
- Decisión
- Justificación en 1 frase
- Acción específica
- Timeline de re-evaluación

Objetivo: salir con un checklist accionable, no con un "depende".
```

*Tip pro:* Crea un **scheduled task en Claude** que cada lunes a las 9am corra esta auditoría automáticamente con tu data del MCP de Meta/Google Ads. Llega a tu inbox antes del meeting de la semana.
