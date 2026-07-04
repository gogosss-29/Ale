# 🔥Desarrollo de Calendarios de Contenido

> Ruta: Biblioteca de Prompts › 🔥Desarrollo de Calendarios de Contenido

---

**Calendarios de Contenido Eficientes:** Construye un calendario editorial que conecte con tu audiencia, tus pillars de marca y tu calendario de negocio. Menos publicar por publicar, más contenido con propósito.

**Recomendación de modelo:** **Claude (Opus o Sonnet)**. Para mejores resultados, pega tu último mes de contenido publicado al inicio del chat para que Claude detecte patrones, huecos y temas saturados.

**1. Auditoría de tu pipeline actual**

```jsx
Aquí está el contenido que publiqué en [canal: blog/IG/YouTube/etc.] en los últimos [30/60/90] días:

[Pega títulos + 1 frase de descripción por pieza]

Analiza y dame:
1. Top 3 temas que ya saturamos (no repetir)
2. Top 3 temas que rinden y deberíamos doblar (con prueba: engagement/views/saves)
3. Huecos editoriales: qué deberíamos cubrir y no estamos
4. Mix actual de formatos (educativo / entretenimiento / venta / inspiración) en %
5. Recomendación de mix ideal para mi nicho [nicho] y audiencia [audiencia]
6. Red flags: ¿hay un patrón que está quemando audiencia?

Se brutalmente honesto. Si lo que estoy publicando es mediocre, dímelo.
```

**2. Calendario trimestral con pillars**

```jsx
Constrúyeme un calendario de contenido para el próximo trimestre con esta info:

- Nicho: [nicho]
- Audiencia: [audiencia específica]
- Objetivo de negocio del trimestre: [lanzar producto / generar leads / construir autoridad / etc.]
- Frecuencia: [X piezas por semana en Y canal]
- 3-5 pillars de contenido: [educativo, behind-the-scenes, casos de éxito, opinión, ventas]

Entregándome:
1. Tabla semana por semana con: fecha | pillar | título tentativo | formato | objetivo de esa pieza
2. Distribución: % de cada pillar en el trimestre
3. 3-4 series temáticas que se puedan repetir mensualmente (consistencia = autoridad)
4. Hitos del trimestre (lanzamientos, eventos, fechas clave)
5. Pieza ancla mensual (la más importante, donde más recursos invertimos)

Formato: tabla markdown que pueda copiar directo a Notion/Airtable.
```

**3. Mapeo a eventos y fechas estratégicas**

```jsx
Para mi nicho [nicho] y audiencia [audiencia], listándome los próximos 3 meses ([especificar meses]):

1. Eventos específicos de la industria (conferencias, lanzamientos, fechas fiscales, etc.)
2. Festividades culturales relevantes (no genericas—solo las que mi audiencia sí celebra)
3. Trending topics esperados (basado en patrones año anterior)
4. Aniversarios de marca o hitos del negocio que pueda celebrar

Para cada fecha:
- Día exacto
- Íngulo de contenido que encaje natural (no forzado)
- Formato sugerido
- Cuándo empezar a teasear (1 semana / 2 semanas / 1 mes antes)

Evita: Día de la Madre/Padre/San Valentín si no encaja con mi negocio. Quiero relevancia, no oportunismo.
```

**4. Distribución multi-canal de una pieza**

```jsx
Tengo una pieza pillar de contenido: [título + 2-3 frases de qué cubre + formato original: blog/video/podcast].

Dame un plan de distribución multi-canal para extraer máximo valor:

1. Versión nativa para cada canal:
   - Twitter/X: 1 thread (10-15 tweets) + 3 tweets sueltos
   - LinkedIn: 1 post largo + 1 carrusel
   - Instagram: 1 carrusel + 3 reels concepts
   - TikTok/Reels: 3 hooks distintos
   - YouTube Shorts: 2 concepts
   - Email/Newsletter: 1 versión

2. Para cada uno: hook de apertura + estructura + CTA específico del canal

3. Calendario sugerido de cuándo publicar cada uno (no todos el mismo día)

4. Qué partes son "evergreen" y puedo reciclar en 6 meses

Objetivo: una pieza = 10 outputs, sin sonar repetitivo.
```

**5. Calendario operativo listo para producción**

```jsx
Convierte el calendario que armamos en un plan operativo de producción con esta estructura por pieza:

| Fecha publicación | Pillar | Título | Canal | Formato | Fecha grabación/escritura | Fecha edición | Estado | Responsable | Objetivo medible |

Reglas:
- Trabaja 2 semanas adelantado (nunca publicar mismo día que produces)
- Marca dependencias (si A no se hace, B no sale)
- Para cada pieza, define UN KPI específico (no "engagement", algo como "50 saves" o "10 DMs")
- Incluye buffer days para imprevistos
- Identifica qué piezas requieren props/locaciones/colaboradores externos (más lead time)

Formato: tabla markdown lista para pegar en Notion/Airtable/Trello.
```

*Tip pro:* Conecta el **MCP de Notion** en Claude y dile "crea esta tabla como una base de datos en mi workspace de Notion". Te ahorra copy-paste y queda sincronizado.
