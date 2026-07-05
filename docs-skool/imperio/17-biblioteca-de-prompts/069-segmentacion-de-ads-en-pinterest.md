# Segmentación de Ads en Pinterest

> Ruta: Biblioteca de Prompts › Segmentación de Ads en Pinterest

---

**Ads en Pinterest:** Pinterest no es Facebook. Es visual-first, intent-driven y largo plazo. Estos prompts te ayudan a hacer ads que encajen con cómo realmente busca y compra la gente en Pinterest.

**Recomendación de modelo:** **Claude (Opus o Sonnet)** para estrategia y copy. Si conectas el **MCP de Pinterest Ads**, Claude puede analizar tus campañas actuales y proponer optimizaciones con data real.

**1. Audit del Pinterest visual culture para tu nicho**

```jsx
Mi nicho: [nicho]
Mi producto/servicio: [qué vendo]
Mi audiencia: [demografías + comportamiento]

Ayudame a entender el visual culture de Pinterest para mi nicho:

1. Estilos visuales que dominan tu nicho en Pinterest (ej: aesthetic minimalista, lifestyle aspiracional, infografías educativas, etc.)
2. Tamaños y formatos más exitosos (vertical 2:3, video, carruseles, Idea Pins)
3. Tipos de pin que se repinean más: ¿listas? ¿tutoriales? ¿antes-después? ¿producto en uso?
4. Paleta de colores que rinde en mi nicho (warm/cool/monochromatic/high-contrast)
5. Tipografía y overlay de texto: cuánto texto soporta el feed sin sentirse pesado
6. Hooks visuales: ¿qué hace que un pin pare el scroll en Pinterest específicamente?

Si tienes acceso al MCP de Pinterest, análizame mis pins orgánicos top 10 y dime qué tienen en común.

Dame ejemplos específicos de cuentas/marcas que están haciendo esto bien.
```

**2. Buyer journey + search intent en Pinterest**

```jsx
A diferencia de IG/FB (interrupción), Pinterest es search-driven y aspiracional. Mapéame el buyer journey de mi audiencia en Pinterest:

Mi producto: [producto/servicio]
Audiencia: [perfil]
Precio aprox: [rango]

Fases del journey:

1. INSPIRACIÓN (top of funnel)
   - ¿Qué buscan en Pinterest? (5 búsquedas específicas)
   - ¿Qué boards crean? (5 nombres típicos de board)
   - Tono del contenido a mostrar: aspiracional, no vendedor

2. CONSIDERACIÓN (mid funnel)
   - ¿Qué comparaciones hacen?
   - ¿Qué dudas o objeciones típicas?
   - Contenido ideal: educativo/comparativo

3. INTENT DE COMPRA (bottom funnel)
   - ¿Qué búsquedas con intención alta? (incluye "best", "how to buy", "vs")
   - ¿Qué formato de pin convierte mejor en este punto?

4. POST-COMPRA
   - ¿Buscan tutoriales, hacks, complementos?
   - Oportunidad para upsell/community building

Para cada fase: 3 ejemplos específicos de pins/ads que ya rinden.
```

**3. Targeting con keywords + intereses + audiencias custom**

```jsx
Voy a lanzar una campaña en Pinterest Ads para [producto/servicio] con objetivo [conversiones / awareness / traffic].

Dame un plan de targeting completo:

1. KEYWORDS (Pinterest es keyword-driven):
   - 20 keywords de alto intent (que indiquen compra cercana)
   - 20 keywords de awareness/inspiración
   - 10 keywords "long-tail" muy específicas (menos competencia, más conversión)
   - Para cada grupo: match type recomendado (broad / phrase / exact)

2. INTERESES:
   - 8-12 intereses a targetear
   - 5 intereses a excluir (gente que se ve similar pero NO compra)

3. DEMOGRAFÍAS:
   - Edad, género, ubicación con justificación (no "todos")

4. AUDIENCIAS CUSTOM:
   - Visitor retargeting (qué windows: 7/14/30/90 días)
   - Lookalikes recomendadas (de qué fuente: customers, lista de email, engagers)
   - Engagement audience (gente que ya interactuó con mis pins)

5. EXCLUSIONES estratégicas: qué audiencias NO quiero ver tu ad

6. ESTRUCTURA DE CAMPAÑA:
   - Cuántos ad groups
   - Qué separar por (intent, demografías, formato)
   - Por qué esa estructura es óptima

Objetivo: que cada dólar gastado esté atribuible a un targeting específico.
```

**4. Generador de creatives + copy para 5 ad formats**

```jsx
Para mi campaña [producto], genérame creatives + copy para los 5 formatos más rentables de Pinterest:

1. STANDARD PIN (vertical 2:3)
   - 3 conceptos visuales distintos (descripción de qué mostrar)
   - Título (máx 100 chars, optimizado SEO)
   - Descripción (500 chars, keywords incluidas natural)
   - Texto en overlay (opcional, máx 6 palabras)

2. VIDEO PIN (6-15 segundos)
   - Storyboard: segundo a segundo
   - Hook visual en los primeros 2s (crítico—la gente NO escucha)
   - Texto en pantalla
   - CTA visual

3. CARRUSEL (2-5 imágenes)
   - Estructura: hook + 3 pasos + CTA
   - Texto de cada slide

4. IDEA PIN (Pinterest's native vertical story)
   - 5-10 páginas
   - Mix de vídeo, foto, texto
   - Educativo o demostrativo

5. COLLECTIONS AD (1 hero + 3-4 productos)
   - Hero image concept
   - 3-4 productos a mostrar como cross-sell

Para cada creative: predicción cualitativa de qué métrica va a rendir mejor (CTR / save rate / outbound clicks / conversiones).
```

**5. Budget, KPIs y plan de optimización**

```jsx
Definámos métricas y presupuesto para la campaña de Pinterest [objetivo]:

Mi budget total: [$X]
Duración: [X semanas]
Objetivo de negocio: [leads / ventas / awareness]
CPA objetivo (si lo sé): [$Y]

Dame:

1. SPLIT DE BUDGET por ad group/audiencia (% y $)
   - Cuánto para retargeting vs prospecting
   - Cuánto para cada formato

2. BENCHMARKS DE PINTEREST para mi nicho:
   - CTR esperado
   - CPM esperado
   - CPC esperado
   - Save rate esperado
   - Conversion rate esperado

3. KPIs por fase del journey:
   - Awareness: impressions, reach, video views, save rate
   - Consideración: CTR, outbound clicks
   - Conversión: ROAS, CPA, conversion rate

4. PLAN DE TESTING (primeras 2 semanas):
   - Qué variables A/B (creative / copy / targeting / formato)
   - Cuándo declarar ganador (umbral de clicks/impresiones)
   - Qué pausar y cuándo

5. PLAN DE OPTIMIZACIÓN (semana 3 en adelante):
   - Scaling: cómo subir budget sin romper el CPA
   - Refresh de creative (Pinterest tiene más long-tail, pero igual fatiga—4-8 semanas)
   - Negative targeting iterativo

Formato: tabla y bullets, listo para llevarse al meeting de team.
```

*Tip pro:* Conecta el **MCP de Pinterest Ads** en Claude y dile "analiza mi cuenta y dime qué ad group está quemando plata sin convertir". Te ahorra horas en el ads manager.
