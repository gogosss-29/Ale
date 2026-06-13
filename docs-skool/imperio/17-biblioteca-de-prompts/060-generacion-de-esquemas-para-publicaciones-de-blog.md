# Generación de Esquemas para Publicaciones de Blog

> Ruta: Biblioteca de Prompts › Generación de Esquemas para Publicaciones de Blog

---

**Esquemas de Blog Eficientes:** Construye outlines de blog post que rankean en Google, retienen al lector y mueven la aguja del negocio. No más blogs que nadie lee.

**Recomendación de modelo:** **Claude (Opus o Sonnet)** para razonamiento y estructura. Si quieres SEO data en vivo, conecta el MCP de Ahrefs/SimilarWeb o pega los top 3 resultados que aparecen al buscar tu keyword.

**1. Research del topic + intent del lector**

```jsx
Topic: [tema/keyword principal]
Audiencia: [a quién le escribo]
Objetivo del post: [SEO ranking / autoridad / generar leads / nurture / educar]

Paso previo a outline. Ayúdame con:

1. Search intent real para [keyword principal]:
   - ¿Buscan cómo hacer algo? ¿Comparar? ¿Decidir compra? ¿Entender concepto?
   - ¿Están en awareness, consideration o decision?

2. Análisis competitivo: [pega los títulos de los top 5 resultados de Google o pásame screenshots]
   - Qué estructura usan
   - Largo promedio
   - Ángulo que dominan

3. "Information gap": qué NO están cubriendo los top resultados que mi audiencia sí quiere

4. Preguntas relacionadas (people also ask): top 5 con respuesta corta cada una

5. Mi diferenciador: basándote en [mi credencial/experiencia/data propia], qué ángulo único puedo tomar

Objetivo: que el outline siguiente NO sea otro post más del montón.
```

**2. Outline SEO-friendly basado en el research**

```jsx
Basándote en el research anterior, dame el outline completo del post con esta estructura:

TITULO PRINCIPAL (H1):
- 3 variantes: clickeable / SEO-friendly / contrarian
- Máximo 60 caracteres cada una
- Una con número, una con pregunta, una con beneficio

META DESCRIPTION:
- 150-160 caracteres
- Incluye keyword principal + beneficio claro + CTA suave

ESTRUCTURA H2/H3:
- Hook de apertura (qué promesa o pregunta abre)
- 5-8 secciones H2 (cada una resuelve UNA pregunta)
- H3s donde aplique (subdivisiones)
- TL;DR al inicio (50-70 palabras)
- FAQ al final (4-5 preguntas con respuestas cortas)

Para cada H2:
- Search intent que resuelve
- 1 frase de qué cubre
- Si aplica: ejemplo / data / quote / visual

Largo objetivo: [800-1500] palabras según competencia.

Formato: markdown listo para CMS.
```

**3. Hooks de apertura (5 variantes)**

```jsx
Para el post [título], escribe 5 hooks de apertura (intro de 2-4 frases), cada uno en un estilo distinto:

1. ESTADÍSTICA: empieza con un dato sorprendente (marca [VERIFICAR] si no estás 100% seguro)
2. CONTRARIAN: una afirmación que va contra el consenso del nicho
3. HISTORIA: 2-3 frases narrativas (ej: "Llevé 6 meses intentando X hasta que...")
4. PREGUNTA: una pregunta provocadora que el lector ya se hizo en voz baja
5. PROBLEMA + PROMESA: nombra el dolor específico y promete la salida en 1 frase

Para cada hook:
- Bullet de por qué funciona psicológicamente
- Score 1-10 de retención esperada

Mi voto + tu recomendación al final.
```

**4. Outline detallado por sección con bullets**

```jsx
Tomá el outline base y expandí cada H2 con esta plantilla:

H2: [título de la sección]
- Promesa de esta sección (qué sabrá el lector al terminar)
- 4-6 bullets de contenido a desarrollar
- 1 ejemplo concreto o caso real (puedes inventarlo plausible, marca [EJEMPLO])
- 1 quote o stat para citar (marca [VERIFICAR] si dudoso)
- Visual recomendado: ¿diagrama? ¿tabla? ¿screenshot? ¿imagen suelta?
- Transición a la siguiente sección (1 frase)

Reglas:
- Cada bullet debe ser accionable, no abstracto
- Si una sección no aporta nada único, marcala [REDUNDANTE] y propón quitarla
- Apunta a que el lector pueda hacer algo concreto al terminar cada sección

Después del outline expandido, identifica las 2 secciones que serán las más memorables y propón cómo amplificarlas aún más.
```

**5. CTAs internos y conversión**

```jsx
Mi negocio detrás de este post: [qué vendo + a quién + producto/servicio principal].
Mi lead magnet relevante (si tengo): [nombre + URL].

Diseña la estrategia de conversión del post:

1. CTA principal (uno solo, claro): ¿qué quiero que haga el lector al terminar?
   - Suscribirse al newsletter
   - Bajar lead magnet específico
   - Agendar llamada
   - Comprar producto
   (Elige UNO basado en el intent del lector)

2. 3 puntos de inserción de CTA dentro del post:
   - Después de qué sección
   - Qué mini-CTA (ej: "Si esto te resuena, te dejo aquí [recurso]")
   - Cómo evitar que se sienta forzado

3. Internal linking: ¿a qué otros 3 posts míos puedo linkear y desde qué sección exacta?

4. Cierre del post:
   - Para resumir SIN sonar a resumen escolar
   - Pregunta final que invite a comentar/responder
   - CTA principal específico (no "si te gustó comparte")

5. Promoción post-publicación:
   - 1 hilo de Twitter para anunciarlo
   - 1 post de LinkedIn distinto
   - 1 email para la lista (subject + body corto)

Objetivo: el post no termina cuando se publica—ahí empieza.
```

*Tip pro:* Conecta el **MCP de Ahrefs o Google Search Console** para que Claude analice qué keywords ya ranqueas y proponga clusters de contenido. Cambia el juego.
