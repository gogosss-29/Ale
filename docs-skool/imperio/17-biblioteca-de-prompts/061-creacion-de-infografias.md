# Creación de Infografías

> Ruta: Biblioteca de Prompts › Creación de Infografías

---

**Infografías Impactantes:** Crea infografías que cuenten una historia clara y que la gente quiera guardar y compartir. No más imágenes con 10 stats que nadie lee.

**Recomendación de modelo:** **Claude (Opus o Sonnet)** es king para infografías porque puede generarte la infografía completa como un **Artifact de SVG/HTML**, lista para exportar. Para versiones más artísticas: ChatGPT con DALL-E o Midjourney.

**1. Estructura narrativa de la infografía**

```jsx
Antes de diseñar, planeemos la narrativa.

Tema: [tema]
Audiencia: [a quién se la mostraré]
Objetivo: [educar / convencer / shareable / autoridad / sales asset]
Canal: [LinkedIn / Instagram / blog / print / pitch deck]

Dame el storyboard narrativo:

1. UN solo big idea (lo que la persona debe recordar al día siguiente)
2. Hook visual (el primer elemento que ve—debe parar el scroll)
3. Estructura narrativa (5-7 secciones máximo):
   - Título de cada sección
   - Mensaje clave en 1 frase
   - Tipo de visual recomendado (chart / icono / numeral / quote / proceso)
4. Final/CTA: qué hace la persona después de verla
5. "Test del vértigo": si la persona la ve 5 segundos y no recuerda nada, fallamos—¿qué debe quedar?

Reglas:
- Máximo 7 piezas de info (más = nadie lee)
- Cada sección debe poder explicarse sola sin contexto
- Prioriza simplicidad sobre completitud
```

**2. Data + jerarquía visual**

```jsx
Tengo estos datos/info para la infografía [tema]:

[pega tu data raw: stats, hechos, números, quotes]

Dame:

1. CURACIÓN: cuáles de estos datos SÍ entran en la infografía (max 7) y cuáles fuera (con justificación)
2. JERARQUÍA visual (1 = héroe, 7 = mínimo):
   - 1 stat héroe (la más impactante, va GRANDE)
   - 2-3 stats de soporte
   - 2-3 puntos contextuales
3. CÓMO MOSTRAR cada dato:
   - Bar chart / pie / línea / numeral gigante / icono multiplicado / mapa / timeline
   - Justificación del por qué ese formato
4. TEXTO MÍNIMO: para cada visual, dame el label final (máximo 5 palabras)
5. FUENTE de cada dato: marca [VERIFICAR] si no está 100% confirmada
6. Si algún dato es más shareable que otro, dimelo—ese va arriba.

Objetivo: que cada elemento gane su lugar en la infografía, no solo "meta todo".
```

**3. Generación directa como Artifact SVG/HTML**

```jsx
Basándote en el storyboard y la jerarquía visual, genérame la infografía COMPLETA como un Artifact HTML.

Specs técnicas:
- Dimensión: [vertical 1080x1920 para IG Story / 1080x1350 para IG post / 1200x628 para LinkedIn / 1080x1080 cuadrada]
- Estilo: [minimalista / corporate / playful / data-heavy / editorial]
- Paleta de colores: [3 hex codes de marca, o pedíme una paleta que combine con mi marca]
- Tipografía: [moderna sans-serif / serif editorial / mix]
- Densidad: [aire abundante / más compacta]

Requisitos del HTML:
- Self-contained (CSS inline, sin librerías externas)
- Responsive a la dimensión indicada
- Usable en cualquier navegador
- Si necesitas charts: usar SVG nativo, no Canvas
- Iconos: usar SVG inline o emoji (no librerías externas)

Después del Artifact:
- Explicame las 3 decisiones de diseño más importantes que tomaste
- Sugerime 2 variantes (cambio de paleta / cambio de layout)
- Dame instrucciones para exportar como PNG (recortar y screenshot, o método más pro)
```

**4. Prompt para image-gen (Midjourney/DALL-E/Ideogram)**

```jsx
Para una versión más artística/ilustrada de mi infografía sobre [tema], escríbeme prompts optimizados para image-gen:

Necesito:
1. PROMPT MASTER para Midjourney (largo, descriptivo, con parámetros --ar 9:16 --style raw o el que sirva)
2. PROMPT para DALL-E (más conversacional, descriptivo de composición)
3. PROMPT para Ideogram (óptimo si lleva texto legíble dentro de la imagen)

En cada prompt incluye:
- Estilo visual (flat / isométrico / hand-drawn / 3D / editorial)
- Composición (centrado / dividido en cuadrantes / vertical fluido)
- Paleta (cita 3 colores o ambient: "warm earth tones" / "high-contrast monochrome")
- Iconografía (qué elementos sí mostrar literalmente)
- Mood (profesional / juguetón / sofístico)
- Lo que NO quiero (negative prompt)

Dame 3 variantes de cada prompt para A/B testear.

Limite: el texto legíble en la imagen es difícil para image-gen—si requiero textos específicos, adviérteme que mejor lo haga en post-producción.
```

**5. Variantes multi-canal**

```jsx
Tengo la infografía master en formato [dimensión original]. Adaptémosla a otros canales sin perder claridad:

Para cada canal, dame: layout adaptado + qué cortar + qué destacar + caption sugerido.

1. INSTAGRAM CARRUSEL (10 slides 1080x1350):
   - Slide 1: hook visual + título
   - Slides 2-9: una idea por slide
   - Slide 10: CTA

2. LINKEDIN POST (imagen 1200x628 + caption largo):
   - Versión estática simplificada
   - Caption profesional (300-500 palabras) con storytelling

3. TWITTER/X THREAD (10 tweets con imagen cada uno):
   - Tweet 1 hook + 9 con micro-versiones de la info
   - Último tweet: CTA

4. PRINT/PDF (A4 vertical):
   - Layout más tradicional, con márgenes
   - Sin animación, todo legible

5. STORY/REEL (formato vertical 9:16, estática o animada):
   - Animación mínima sugerida (build-up secuencial)
   - Texto BIG, mínimo

Objetivo: una infografía master = 5 piezas listas para distribuir esta semana.
```

*Tip pro:* Con Claude en modo Artifacts, puedes iterar en tiempo real diciendo "cambia la paleta a azules", "haz la stat principal más grande", "agregá un ícono aquí". No necesitas Canva ni Figma para la primera versión.
