# Escribir Propuestas de Artículos de Invitado

> Ruta: Biblioteca de Prompts › Escribir Propuestas de Artículos de Invitado

---

**Propuestas de Artículos de Invitado:** Crea pitches de guest post que pasen el filtro del editor y consigan respuesta. Más ratio de aceptación, menos correos al vacío.

**Recomendación de modelo:** Estos prompts rinden mejor con **Claude (Opus o Sonnet)**. Si la publicación tiene un sitio web público, puedes pegar la URL o screenshots de artículos recientes para que Claude lea su línea editorial.

**1. Research previa de la publicación**

```jsx
Analiza esta publicación: [URL del sitio o nombre + descripción + 2-3 artículos de ejemplo pegados].

Dame en formato bullet:
1. Línea editorial (tono, sesgo, qué cubren y qué NO)
2. Audiencia real (no la que dicen, la que se ve en los comentarios)
3. Formato preferido (long-form, listicle, opinión, tutorial)
4. Largo promedio de artículos
5. 5 temas que YA cubrieron en exceso (no pitchear esto)
6. 3 huecos editoriales que detecté (oportunidades reales)
7. Estilo de subtítulos (clickbait, descriptivo, pregunta, etc.)

Objetivo: que mi pitch encaje natural, no parezca spray-and-pray.
```

**2. Generador de ideas de pitch que sí encajen**

```jsx
Basándote en el research que acabamos de hacer de [publicación], genérame 10 ideas de guest post sobre [tema/área] que:

- Encajen con la línea editorial detectada
- No repitan los 5 temas saturados
- Aprovechen 1 de los 3 huecos editoriales
- Tengan un ángulo contrarian, data-driven o experiencial (no opinión genérica)

Para cada idea:
1. Título tentativo (máx 70 chars, estilo de la publicación)
2. Ángulo en una frase
3. Por qué a su audiencia le importa
4. Qué los califica a mí para escribirlo ([credencial relevante])
5. Score 1-10 de probabilidad de aceptación (con justificación)

Ordena por score, más alto primero.
```

**3. Email de pitch corto y memorable**

```jsx
Escribe el email de pitch para [nombre del editor, si lo sabes] de [publicación].

Idea elegida: [título + ángulo de la lista anterior]
Mi credencial: [una línea: quién soy, qué hago, prueba relevante]

Reglas estrictas:
- Máximo 120 palabras
- Apertura: una observación específica sobre un artículo reciente de la publicación (con título)
- Segundo párrafo: el pitch en 2 frases (ángulo + por qué ahora)
- Tercer párrafo: outline en 3 bullets (qué va a cubrir el artículo)
- Cierre: CTA claro y honesto ("¿Te sirve que te envíe el draft completo para [fecha]?")

Prohibido:
- "Espero que estés bien"
- "Soy un gran fan de tu trabajo"
- "Te quería compartir una idea"
- Cualquier adjetivo super genial / increíble / fantástico

Objetivo: el editor lo lee completo en 30 segundos y sabe si dice sí o no.
```

**4. Subject lines optimizados**

```jsx
Para el pitch que acabamos de escribir, genérame 8 variantes de subject line:

2 estilo "directo" (Pitch: [título del artículo])
2 estilo "curiosity gap" (un dato o pregunta que abra)
2 estilo "referencia específica" (menciona un artículo suyo)
2 estilo "contrarian" (opinión que sorprende)

Reglas:
- Máximo 60 caracteres (visibles en preview de email)
- Nada de URGENT, !!!, o emojis (van a spam)
- Cada uno con una predicción de open rate vs. el promedio (3-5%, 5-10%, 10%+)

Dame mi top 3 con justificación de por qué ganarían en A/B test.
```

**5. Follow-up que no suena desesperado**

```jsx
El editor de [publicación] no respondió al pitch que envié hace [X días]. Escríbeme un follow-up.

Contexto del pitch original: [pega el pitch].

Reglas del follow-up:
- Máximo 60 palabras
- NO empezar con "Solo quería hacer follow-up"
- Aporta algo nuevo: un dato extra, un ángulo alternativo, o un artículo reciente que refuerza la idea
- Cierra con una salida elegante ("Si no es para ustedes ahora, sin problema—me avisas")
- Cero culpa, cero ansiedad

Dame 2 variantes: una más warm, una más business.
```

*Tip pro:* Crea un **Project en Claude** llamado "Guest Post Pipeline" donde guardes: tu bio, credenciales, 2-3 artículos tuyos como writing sample, y la lista de publicaciones objetivo con su research. Después cada pitch nuevo se hace en minutos.
