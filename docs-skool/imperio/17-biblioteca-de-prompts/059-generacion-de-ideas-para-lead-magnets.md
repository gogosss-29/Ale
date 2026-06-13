# Generación de Ideas para Lead Magnets

> Ruta: Biblioteca de Prompts › Generación de Ideas para Lead Magnets

---

**Imanes de Prospectos (Lead Magnets):** Crea lead magnets que la gente sí quiera bajar y que filtren a tu cliente ideal. Menos PDFs genéricos, más herramientas que demuestren valor en 5 minutos.

**Recomendación de modelo:** **Claude (Opus o Sonnet)**. Si tienes data de tu audiencia (encuestas, DMs frecuentes, preguntas en comentarios), pégala al inicio del chat—cambia todo el resultado.

**1. Auditoría de pain points reales**

```jsx
Mi negocio: [qué vendo y a quién]
Mi audiencia ideal: [demografías + comportamiento + en qué etapa están]

Ayudame a mapear lo siguiente:

1. Los 7 problemas más urgentes que tiene mi audiencia HOY (no en general, ahorita)
2. Para cada uno: ¿qué ya intentaron y no funcionó? (esto es oro para el ángulo)
3. Las 5 preguntas que escriben más en Google sobre estos problemas
4. Los 3 miedos tácitos que no dicen pero les frenan (ej: miedo al ridículo, miedo a perder dinero, miedo a empezar tarde)
5. Las 3 transformaciones más deseadas (lo que quieren conseguir, en sus palabras, no en marketing-speak)

IMPORTANTE: si tengo pegada data real arriba (encuestas/DMs/comentarios), basándote en eso. Si no, dilo y trabaja con asumptions claros.
```

**2. Generador de lead magnets de alta conversión**

```jsx
Basado en los pain points que detectamos, genérame 10 ideas de lead magnet con esta estructura por idea:

1. Nombre del lead magnet (clickeable, específico, no genérico)
2. Formato (PDF / calculadora / checklist / Notion template / video corto / mini-curso / herramienta interactiva)
3. Pain point que resuelve (de la lista anterior)
4. Promesa concreta: "En [tiempo] consigues [resultado específico]"
5. Tiempo estimado para producirlo (horas, no fantasías)
6. Score 1-10 de conversión esperada con justificación
7. Score 1-10 de filtro de cliente ideal (alta = atrae compradores, baja = atrae curiosos)

Reglas:
- Mínimo 3 ideas que NO sean PDF
- Mínimo 2 ideas interactivas (calculadora, quiz, herramienta)
- Mínimo 1 idea que se pueda generar 100% con IA en tiempo real

Ordena por conversión esperada × filtro de cliente ideal.
```

**3. Outline detallado del lead magnet elegido**

```jsx
Eligí este lead magnet: [nombre + formato]

Dame el outline completo para producirlo, con:

1. Promesa de portada (la frase que va en la landing): máximo 12 palabras
2. Sub-promesa (qué incluye específicamente): 3 bullets de máximo 10 palabras
3. Estructura interna (secciones/capítulos/pasos) con:
   - Título de cada sección
   - Objetivo de aprendizaje (qué sabrán hacer al terminar)
   - Contenido en bullets (qué explicar, qué ejemplos usar)
   - Acción concreta al final de cada sección
4. "Quick win" en los primeros 2 minutos: ¿qué entrega valor instantáneo?
5. CTA final dentro del lead magnet: cómo dirigirlos al siguiente paso con mi producto/servicio
6. Disclaimer/limitaciones (qué NO incluye, para gestionar expectativa)

Objetivo: que se pueda producir esta semana, no "algún día".
```

**4. Landing page de captura**

```jsx
Escribe la landing page de captura para el lead magnet [nombre]:

- Headline (máx 12 palabras, claim específico)
- Sub-headline (1 frase, amplía el cómo)
- 3-5 bullets de lo que incluye (en lenguaje de beneficios, no features)
- Bloque "para quién es esto" (3 bullets)
- Bloque "NO es para ti si" (2-3 bullets, filtro honesto)
- Mini bio + foto: "Por qué yo" (máx 60 palabras)
- 2-3 social proofs/testimonios cortos (con [PLACEHOLDER] si no los tengo)
- Formulario: cuántos campos pedir y por qué cada uno (no pedas más de 3)
- CTA del botón (no "Descargar"—algo específico al resultado)
- FAQ con 4 objeciones típicas + respuestas

Entrégame como markdown listo para pasarle al disenador.
```

**5. Email de entrega + secuencia de nurture**

```jsx
Diseña la secuencia de emails post-descarga del lead magnet [nombre]:

EMAIL 0 (instantáneo): Entrega del lead magnet
- Subject (máx 50 chars)
- Body con: link de descarga + 1 instrucción clara de qué hacer primero + pregunta abierta para responder (alto open de respuesta = warmth)

EMAIL 1 (día 2): Implementación
- Tip o atajo que NO está en el lead magnet (sorpresa positiva)
- CTA suave a contestar cómo les fue

EMAIL 2 (día 4): Caso o resultado
- Historia corta de un cliente/yo mismo aplicando esto
- Lección extraída
- CTA al próximo paso (otro recurso, no venta aún)

EMAIL 3 (día 7): Pivot a oferta
- Conexión entre el lead magnet y el problema mayor que resuelve mi producto/servicio
- Oferta concreta con timer corto o bonus
- CTA a llamada/compra

EMAIL 4 (día 10): Last call + plan B
- Cierre de oferta
- Alternativa para los que no compran (más contenido, otro recurso)

Reglas globales:
- Cada email máx 150 palabras
- Un solo CTA por email
- Tono: como si fuera de un amigo, no de una marca
- NO usar "hola" o "hi" genérico—abre con algo específico
```

*Tip pro:* Si conectas el **MCP de Gmail/Mailchimp/ConvertKit** en Claude, dile "crea estos emails como drafts en mi cuenta" y los deja listos para revisar y programar.
