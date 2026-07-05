# Escribir Artículos de Invitado

> Ruta: Biblioteca de Prompts › Escribir Artículos de Invitado

---

**Escritura de Artículos de Invitado:** Genera ideas, ángulos, pitches y borradores listos para publicar artículos de invitado en blogs y publicaciones de tu industria.

**Recomendación de modelo:** Estos prompts rinden mejor con **Claude (Opus o Sonnet)** por razonamiento y manejo de contexto largo. Antes de usarlos, pega tu nicho, tu audiencia ideal y 1-2 ejemplos de artículos que admires.

**1. Generador de ángulos únicos**

```jsx
Eres un editor experto en contenido para [industria/nicho]. Quiero pitchear un artículo de invitado sobre [tema] a [publicación o tipo de blog].

Mi audiencia es [audiencia específica].
Mi objetivo es [objetivo: posicionarme como experto / generar leads / construir backlinks].

Dame 10 ángulos únicos y creativos que no se hayan agotado en este nicho. Para cada ángulo:
1. Título tentativo (clickeable, máx 70 caracteres)
2. Hook de apertura (2 frases)
3. Por qué este ángulo es contrarian, sorprendente o poco explorado
4. Qué tipo de publicación lo recibiría mejor

Evita ángulos genéricos tipo "X razones para..." o "Cómo hacer Y en N pasos". Apunta a lo que un editor diría "esto sí me lo leo".
```

**2. Email de pitch al editor**

```jsx
Escribe un email de pitch para el editor de [publicación]. El artículo propuesto es:

- Título: [título]
- Ángulo: [ángulo en una frase]
- Audiencia: [audiencia]
- Por qué ahora: [timing, hook o data point reciente]
- Sobre mí: [tu credencial relevante en una línea]

Reglas del email:
- Máximo 150 palabras
- Empieza con una observación específica sobre la publicación (no genérica, demuestra que la lees)
- Muestra que entiendo su línea editorial
- Incluye 3 sub-puntos del outline propuesto
- Cierra con un CTA claro (cuándo puedo enviar el draft completo)

Tono: profesional pero humano. Sin frases hechas tipo "espero que estés bien" ni "soy un gran fan de tu trabajo".
```

**3. Investigación con datos verificables**

```jsx
Necesito [número] estadísticas, estudios o datos recientes (idealmente últimos 12-18 meses) para respaldar un artículo de invitado sobre [tema], dirigido a [audiencia].

Para cada dato dame:
1. La estadística exacta + fuente + año
2. Cómo se conecta con el ángulo del artículo
3. Una frase lista para citar directamente
4. Link a la fuente original (si tienes acceso a web)

Prioriza fuentes confiables: papers académicos, reportes de industria reconocidos (Gartner, McKinsey, etc.), encuestas con muestra grande (N>1000).

Si no estás seguro de una fuente o el dato podría ser inventado, dilo explícitamente con [VERIFICAR]. Prefiero menos datos pero reales.
```

**4. Auditoría de errores comunes y clichés**

```jsx
Voy a escribir un artículo de invitado sobre [tema] para [audiencia/publicación].

Antes de empezar, hazme esta auditoría:

1. Lista los 7 errores más comunes que comete la gente al escribir sobre este tema (de cliché a contraproducente).
2. Para cada error, dame una versión corregida o un ángulo opuesto.
3. Identifica 5 frases o palabras sobreusadas en este nicho y propón alternativas más frescas.
4. Lista 3 supuestos que la mayoría de autores asume y que vale la pena cuestionar.

Sé brutalmente honesto. Mi objetivo es destacar, no sonar como todos los demás.
```

**5. Borrador completo del artículo**

```jsx
Escribe un borrador completo de artículo de invitado con estas specs:

- Título: [título]
- Ángulo: [ángulo en una frase]
- Audiencia: [audiencia]
- Publicación: [publicación] (tono y estilo: [casual / técnico / business / etc.])
- Largo: [800-1500] palabras
- Estructura: hook fuerte + 3-5 secciones con subtítulos + conclusión accionable

Reglas:
- Usa ejemplos concretos y específicos, no genéricos. Si necesitas un ejemplo, inventa uno plausible y dilo.
- Incluye 1-2 datos o estadísticas (marca con [VERIFICAR] si no estás 100% seguro de la fuente).
- Evita: introducciones largas que no van al grano, frases hechas, listas numeradas innecesarias, sub-encabezados tipo "En conclusión".
- Cierra con una idea que dé que pensar al lector, no con un resumen.

Después del borrador, dame:
- 3 títulos alternativos
- 2 ideas de CTA para el bio del autor
- 1 sugerencia de tweet/post para promover el artículo
```

*Tip pro:* Si vas a usar estos prompts seguido, crea un **Project en Claude** con tu nicho, audiencia y ejemplos cargados como contexto. Así cada conversación ya empieza con todo lo tuyo.
