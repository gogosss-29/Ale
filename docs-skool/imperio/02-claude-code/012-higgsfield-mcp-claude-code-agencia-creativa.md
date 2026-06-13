# Higgsfield MCP + Claude Code = Agencia Creativa

> Ruta: Claude Code › Higgsfield MCP + Claude Code = Agencia Creativa

**🎬 Vídeo (44.8 min):** https://youtu.be/uYRRTLHPSWg?si=dIzkh6l9C_9PFVAO

---

## Lo que vas a poder construir cuando termines este post

Si sigues esto paso a paso, vas a salir con:

- ✅ **20 fotos profesionales** de un producto físico (estilo agencia premium)
- ✅ **3-8 videos cinematográficos animados** del mismo producto
- ✅ **3 videos UGC testimoniales** (estilo "creador grabándose con el celu")
- ✅ Una **landing page completa** desplegada online (URL pública en Vercel)
- ✅ **5-50 thumbnails de YouTube** para tus propios videos (mismo sistema que uso yo)

Todo orquestado desde **Claude Code**, conectado al **MCP recién lanzado de Higgsfield**, sin saltar de tab en tab.

---

## ⚙️ Lo que necesitas antes de empezar

Requisito Por qué Cuenta de **Claude** (Pro o equivalente) Para conectar el MCP custom Cuenta de **Higgsfield** (plan Plus recomendado, Starter alcanza para probar) Acceso a todos los modelos **Foto física del producto** que quieres vender Va como referencia al modelo **Claude Code** instalado en tu máquina Para correr los prompts

---

## 🔌 Paso 1: Conectar Higgsfield al MCP de Claude (60 segundos)

El MCP de Higgsfield es la pieza nueva que cambia el juego. Es lo que hace que Claude pueda generar, editar y mandar creativos directamente sin abrir tabs.

### Cómo conectarlo (vía Claude.ai)

1. Andá a `claude.ai` → **Settings**
2. En la barra lateral, **Connectors**
3. Arriba a la derecha, **Add custom connector** (botón "+")
4. Llenás 2 campos: - **Name**: `Higgsfield`
- **URL**: `https://mcp.higgsfield.ai/mcp`
5. Click **Add** → **Connect** → iniciar sesión con tu cuenta de Higgsfield → **Allow**

⚠️ **Atención: NO es **`cloud.higgsfield.ai` — esa es la app web para usar Higgsfield manualmente desde el browser.

✅ Es `mcp.higgsfield.ai/mcp` — el MCP, que es lo que conectamos a Claude para que opere por ti.

### Cómo conectarlo desde Claude Code (alternativa CLI)

Si prefieres Claude Code en lugar de Claude.ai, puedes decirle directamente:

```
Conéctame al MCP de Higgsfield.
URL: https://mcp.higgsfield.ai/mcp

```

Te va a pedir aprobar la conexión y listo. Una vez conectado, puedes verificar pidiéndole "muéstrame los modelos disponibles" o "consultame el balance de créditos".

---

## 📁 Paso 2: Armar el `CLAUDE.md` de tu agencia

Esto es lo que convierte a Claude en **"director creativo de tu agencia"**. El `CLAUDE.md` son las instrucciones permanentes que va a seguir mientras trabajás en este proyecto.

Creá un proyecto nuevo en Claude Code (yo le puse `agente-de-agencias`), y como primer mensaje le tiras:

```markdown
Eres el director creativo y ejecutor de una agencia de diseño de
branding muy elevado, bastante boutique.

Te conectas a Higgsfield y a distintos modelos de IA — siendo:
- ChatGPT Image 2 (gpt_image_2)
- Seedance 2.0 (seedance_2_0)
- Kling 3.0 (kling3_0)

Las mejores herramientas al momento de grabar este video.

Tu trabajo: redactar y mandar a generar los mejores prompts y los
mejores outputs de imagen y video para mi agencia, llamada
"Agencia Imperial".

Te voy a ir pasando productos y briefs. Tu trabajo:
1. Investigar buenas prácticas de marcas premium
2. Generar prompts que respeten esa estética
3. Por DEFAULT, generar todo en quality LOW + 1k resolution
4. Solo hacer upscale a alta cuando yo te diga "esta me gustó"
5. Por DEFAULT, usar Kling 3.0 para video y GPT Image 2 para imagen
6. Investigar buenas prácticas de Higgsfield MCP, Seedance y GPT Image 2

Procedé a crear tu archivo CLAUDE.md con estas instrucciones.

```

Cuando termine, vas a tener un `CLAUDE.md` en la raíz del proyecto con todo el contexto. **De ahora en adelante, en este proyecto, Claude trabaja con esta personalidad sin que se lo tengas que recordar.**

---

## 📸 Paso 3: Generar las fotos del producto (8-20 imágenes)

Esta es la primera pieza del entregable. Vamos a generar fotos profesionales que sirvan como hero de landing, ads de Meta, contenido orgánico, lo que sea.

### El prompt (copy-paste y adapta)

```
A continuación te paso fotos de un reloj. [Adjuntá 1-2 fotos del producto físico]

Necesito 8 fotos profesionales del producto en distintos contextos
para una campaña publicitaria.

- Modelo: gpt_image_2 vía Higgsfield MCP
- Calidad: low (queremos descubrir, después hacemos upscale)
- Resolución: 1k
- Aspect ratio: 16:9 horizontal

8 ángulos distintos:
1. Producto centrado, fondo blanco, luz cenital — estilo e-commerce
2. Macro de la corona y la esfera, cinematográfico
3. Sobre mármol negro, luz lateral dura
4. En la muñeca de un hombre con camisa blanca, ambiente
5. Junto a accesorios de cuero (cartera, llaves), lifestyle
6. Sobre escritorio de madera con MacBook desenfocado al fondo
7. Reloj sobre arena clara, luz de atardecer
8. Plano cenital con sombra dura geométrica

Mostrame los 8 prompts antes de generar para validar 2-3.
Después dale a generar todas en paralelo.

```

### Por qué generar en LOW + 1k

Modo Costo Cuándo usarlo `quality: low` + `1k` **0.5 créditos / imagen** **Default — descubrir qué te gusta** `quality: high` + `2k` 7 créditos / imagen Solo a las ganadoras `quality: high` + `4k` 15 créditos / imagen Premium / impresión

**Generar 50 imágenes en LOW = 25 créditos (~$1).**  
**Hacer upscale a 5 ganadoras en HIGH = 35 créditos (~$1.50).**

Si generas todo en HIGH desde el inicio: gastas ~$15 en lo mismo. **Filtra primero, escala después.**

### Iterar sobre las que te gustan

Una vez generadas, le dices a Claude:

```
Me gustaron estas: [lista de IDs / nombres de archivos].
Generame otras 8 más en el mismo estilo, vertical 9:16 esta vez,
para usar como contenido de Reels e Instagram Stories.

El brand vibe: Luxury Man · Relax · Healthy · Natural.

```

Y vas iterando. **No hay límite a cuántas veces puedes pedir más** — solo gastas créditos a 0.5 cada una.

### 💎 Cómo accedés a las generaciones

Las imágenes y videos se guardan en **dos lugares simultáneamente**:

1. **Local**: en la carpeta del proyecto Claude Code (donde lo abriste). Ve al Finder → carpeta del proyecto → vas a verlas como archivos individuales.
2. **Higgsfield Assets**: ve a `higgsfield.ai` → Assets → vas a ver todas las generaciones de tu cuenta historicamente. Útil si quieres hacer upscale manual desde la UI.

---

## 🎬 Paso 4: Animar las imágenes ganadoras a video

Ahora viene la pieza que más impacta visualmente: convertir las fotos en videos cinematográficos.

### Modelos disponibles y su precio

Modelo Costo (8 seg, 720p) Calidad Cuándo usarlo **Kling 3.0** ~10 créditos (~$0.49) ★★★★ **Default — buen ratio precio/calidad** Seedance 2.0 ~36 créditos (~$1.76) ★★★★★ Premium / hero shots de landing Seedance 2.0 Fast ~20 créditos ★★★★ Cuando quieres Seedance pero más barato

**Mi recomendación**: Kling 3.0 por defecto. Solo Seedance 2.0 cuando es el hero del producto y tiene que verse impecable.

### El prompt

```
Me gustaron estas imágenes que generaste:
- B308
- B208
- B207
- B206
- B306
- ATERNA-REF1
- ATERNA-REF2

Anima cada una con Kling 3.0 vía Higgsfield MCP.

Movimiento: SUTIL, no dramático. Esta marca es premium, calmo,
luxury. La cámara avanza muy lento (push in suave). Los elementos
del entorno tienen movimiento natural (luz que cambia, brisa, etc).
El producto siempre nítido y centrado.

- Duración: 6-8 segundos por video
- Resolución: 1080p
- Aspect ratio: 16:9
- Termina con frame casi igual al inicio (para loop suave)

Avisame cuando estén todas listas.

```

Claude las manda a generar en paralelo. **8 videos en ~5 minutos.**

### Cuando estén listos

Vuelves a `higgsfield.ai/assets/videos` y los revisas todos. Mi flujo:

1. Veo cuáles tienen movimiento bueno (la luz, el reflejo, la cámara)
2. Marco las 3-5 ganadoras
3. Esas son las que voy a usar en la landing y en los ads

---

## 🌐 Paso 5: Armar la landing page completa con Claude Design

Acá viene el clímax del flujo. **Tomamos todos los assets que generamos (fotos + videos) y le pedimos a Claude Code que arme la landing.**

### Sub-paso 5A: Buscar inspiración en Motion Sites

Antes de pasarle a Claude el prompt para la landing, le doy referencia visual de qué quiero. Yo uso **Motion Sites** (motionsites.com) — una colección de plantillas premium de páginas web animadas.

> 💎 **EXCLUSIVO PARA IMPERIO**: pagué el plan de agencia de Motion Sites para tener **derecho de reventa de las plantillas**. Eso significa que dentro del Classroom de Imperio, en la sección **Cloud Design**, te dejé **todas las plantillas premium** disponibles para que las uses sin pagar Motion Sites.
> 
> **Cómo accederlas**:
> 
> 1. Andá a Skool → Classroom
> 2. Buscá la sección **Cloud Design**
> 3. Ahí están todas las plantillas (Impressive Hero, Slam Dunk, Aterna, Coder Crest, etc.)
> 4. Cada plantilla tiene su prompt completo listo para pegar a Cloud Design

Si **NO sos miembro premium**, puedes copiar las plantillas gratuitas de Motion Sites o armar tu propio prompt visual.

### Sub-paso 5B: Pedirle a Claude el "one-shot" para Cloud Design

Una vez que elegiste tu plantilla de referencia, le dices a Claude Code:

```
Te paso una plantilla de referencia que me gustó (estilo + movimiento).

[Pegas el prompt de Motion Sites o de la plantilla Imperio]

Tomalo como inspiración, no como restricción del 100%. Adaptá al
brand vibe que ya conocés (Aterna · Luxury Man · Relax · Natural).

Tu output: un prompt único de "one-shot" para pegarle a Cloud Design.

El prompt debe:
- Mapear cada uno de los videos generados a la sección de la landing
  donde van (hero, galería, sección de beneficios, testimonios, CTA)
- Mapear las imágenes a las secciones que correspondan
- Incluir el copy de cada sección (headline, subheadline, CTA)
- Respetar la jerarquía premium del brand
- Estructura: Hero → Trust → Galería → Beneficios → Testimoniales → CTA → Footer

Pasamelo en formato listo para Cloud Design.

```

### Sub-paso 5C: Importar a Cloud Design

1. Andá a `claude.ai/design`
2. **Nuevo proyecto** → ponle un nombre (ej: "Aterna Campaign")
3. Subí los assets: - Subí los videos uno a uno (si te tira error subiéndolos en batch — hay un límite por subida)
- Sube las imágenes que quieres usar (también una a una si es necesario)
- Sube la foto del producto físico (siempre conviene tenerla)
4. Pega el prompt one-shot que te dio Claude Code
5. Dale a enter y esperá ~2-5 minutos

Cuando termine, vas a tener una landing página viva, scrolleable, con todos tus assets ensamblados.

### Sub-paso 5D: Iteración rápida

Casi siempre vas a querer ajustar algo. Dos formas:

**Opción A — Editar en Cloud Design directamente** (más rápido para texto/orden):

- Click en el texto que quieres cambiar → escribís encima → enter
- Para reordenar secciones, drag & drop
- Para reemplazar background, "type anywhere" + arrastra el video que quieres

**Opción B — Pedirle nuevo prompt** (cuando es cambio estructural):

- Vuelve a Claude Code
- "El gap entre la sección X y Y está muy grande, acortalo"
- "Muéveme el reloj a la derecha en la sección de venta final"
- Te da el prompt actualizado para volver a iterar en Cloud Design

---

## 🚀 Paso 6: Deploy en Vercel desde Claude Code (1 minuto)

Una vez que estás conforme con la landing, la publicas online así:

### Desde Cloud Design

1. Click en **Compartir** (arriba derecha)
2. Click en **"Hand to Cloud Code"**
3. Te da un comando estilo: ```
/handoff <tu-proyecto-id> ```
4. Copialo

### En Claude Code

1. Pegas el comando en el chat de Claude Code
2. Le dices: **"haz deploy de esta página web"**
3. Claude conecta con Vercel, sube los archivos, y te devuelve la URL pública

✅ **URL típica**: `tu-proyecto.vercel.app` — accesible para cualquiera con el link.

Si quieres conectar tu propio dominio:

```
Conectame mi dominio aterna.com a esta deploy de Vercel.

```

Y Claude te guía con los DNS records.

---

## 📲 Paso 7: Crear contenido UGC (testimoniales)

Ahora vamos a generar UGC testimoniales — videos verticales estilo "cliente real grabándose con el celular".

### Dos métodos para hacer UGC

**Método 1: Directo con Seedance 2.0** (más rápido, menos control):

```
Creame contenido UGC usando Seedance 2.0 para el reloj.

3 videos verticales (9:16) de nuestro personaje principal hablando
y mostrando el producto. Usá las imágenes de referencia del modelo
que ya generamos.

Cada video:
- 8 segundos
- Modelo: seedance_2_0
- Resolución: 720p (nos basta para Reels)
- Modo: std

Los 3 videos con angle distinto:
A) Antes/después emocional
B) Descubrimiento sorpresivo
C) Recomendación de amiga

```

**Método 2: Imagen primero + animar después** (más control):

```
1) Generá 5 imágenes verticales (9:16) usando GPT Image 2 con
   nuestro personaje principal hablando al cámara, sosteniendo
   el reloj. Settings distintos: oficina, bar, parque, atardecer,
   en su casa. Quality medium, resolución 1k.

2) Cuando estén las 5, mostrámelas y elijo cuáles animar.

3) Después animamos solo las que elijo con Seedance 2.0 (15 seg
   cada uno) para tener UGC más largo.

```

**Mi recomendación**: el método 2 te da más control sobre el casting (la persona, el setting, la ropa). El 1 es más rápido si necesitas algo "good enough" para testear.

### Tip para que el UGC se sienta más auténtico

Pídele a Claude que el personaje:

- Hable en tu acento regional (LATAM, español de España, etc)
- Use frases naturales y no "publicitarias" (en serio, no actuadas)
- Esté en setting espontáneo (no estudio)
- Sostenga el producto en cuadro pero sin que sea el foco visual obvio

---

## 🖼️ Paso 8: BONUS — Tu sistema de thumbnails de YouTube

Si tienes tu propio canal (o quieres ofrecerlo como servicio), este es el sistema que uso yo para mis thumbnails.

### Setup: el skill `bencord-thumbnails-pro`

Tengo un skill global de Claude Code que armé y publiqué para la comunidad. Se autotrigger con palabras "thumbnails", "miniaturas", "portadas".

> 💎 **EXCLUSIVO PARA IMPERIO**: dentro del Classroom, sección **Skills**, dejé el archivo `bencord-thumbnails-pro` para descargar. Lo arrastras a `~/.claude/skills/` y queda disponible para tu Claude Code.
> 
> **Estructura del skill**:
> 
> - SKILL.md con el flujo completo (outliers → 3-5 variantes → generación → upscale)
> - references/viral-patterns.md
> - references/title-formulas.md
> - references/image-prompts.md
> - references/higgsfield-mcp.md

### Cómo lo uso

Le digo a Claude Code:

```
Usá bencord-thumbnails-pro.

Generame 5 thumbnails para un video que se llama:
"Reemplacé Una Agencia Creativa COMPLETA Con Claude Code"

Tema: cómo reemplazar el trabajo de una agencia creativa con
Claude Code + Higgsfield MCP.

Emoción objetivo: incredulidad / desbloqueo.

Asegurate de usar mi cara de referencia (la del skill).
Generá en LOW + 1k. Después elegimos top 3 y hacemos upscale.

```

Y me devuelve 5 thumbnails con mi cara, mi estilo de canal, y distintos ángulos emocionales.

### Iteración

Si me gustan 3 de los 5:

```
Me gustaron las variantes 2, 4 y 5.
Hacé upscale a HIGH + 2k.
Las otras dos descartalas.

```

Y listo. **Costo total para 5 thumbnails de prueba + 3 upscale: ~$2 en créditos.**

---

## 💰 Costos reales: cuánto cuesta replicar todo esto

Esta es la sección más importante. Te paso los números exactos.

### Plan recomendado: Higgsfield Plus

- **$39/mes** (anual) o $49/mes (mensual)
- **1,000 créditos**
- Acceso a todos los modelos
- Hasta 8 generaciones simultáneas

> ⚠️ Si solo quieres probar el stack, el plan **Starter ($15/mes)** alcanza. Si vas a producción seria, Plus.

### Costo por generación (Plan Plus, $0.039 por crédito)

Operación Modelo Créditos USD Imagen LOW 1k (descubrir) GPT Image 2 0.5 **$0.02** Imagen HIGH 2k (upscale ganadora) GPT Image 2 7 **$0.27** Imagen HIGH 4k (premium / print) GPT Image 2 15 $0.59 Video 6-8 seg 1080p Kling 3.0 ~10 $0.39 Video 8 seg 720p Seedance 2.0 ~36 $1.76 Video 15 seg 1080p Seedance 2.0 ~68 $3.31

### Cálculo del video completo

Pieza Créditos USD 20 fotos del reloj (LOW + 3 upscale) ~31 $1.21 8 videos del reloj con Kling 3.0 ~80 $3.92 5 imágenes UGC verticales + 2 animadas con Seedance 2.0 ~75 $3.68 Assets adicionales para landing ~30 $1.17 5 thumbnails YouTube + 3 upscale ~31 $1.21 Iteraciones / retries / extras ~30 $1.17 **TOTAL** **~277 créditos** **~$10.80 USD**

**Comparativa vs agencia tradicional**:

- Sesión fotográfica de producto premium: $5,000 - $10,000
- Video cinematográfico de producto: $5,000 mínimo (he visto $20K)
- Landing page de agencia top: $5,000 - $15,000
- 4 UGC testimoniales con creators: $1,200
- Thumbnails de canal: $1,200/mes

**Total agencia mínimo**: **$17,400 - $35,000+**  
**Total con este sistema**: **~$11**

**Diferencia: ~1,500x más barato.**

---

## ⚠️ Lo que la IA NO reemplaza (limitaciones honestas)

Antes que pienses que esto es magia, dos cosas:

### 1. La IA no reemplaza la estrategia

Claude Code + Higgsfield no te dice **qué decir**. Te ejecuta lo que tú decidas. Si tu posicionamiento está mal, vas a generar 50 versiones de algo que no convence.

**Lo que reemplazás**: la **ejecución**.  
**Lo que sigue siendo tuyo**: la **estrategia**, el **ángulo**, el **insight del cliente**.

### 2. El ojo crítico sigue siendo tuyo

De cada batch que generas, una parte va a estar buena, otra mediana, y una basura. Tu trabajo cambia de **producir → curar**.

Si todavía no tienes ojo crítico, este stack te va a generar ruido más rápido. Si ya tienes ojo, te multiplica por veinte.

### 3. Garbage in, garbage out

Si le pasas briefs vagos a Claude, te devuelve outputs vagos. La calidad del prompt define la calidad del output. **Invierte el tiempo en el prompt, no en re-generar mil veces.**

---

## 💼 Cómo monetizar este sistema (servicio para clientes)

> 💎 **Esto es contenido de Imperio**: lo que viene es el modelo de negocio que estamos viendo funcionar en la comunidad para vender este servicio a marcas.

### Cómo cobrar este servicio

Servicio Precio sugerido Costo en créditos Margen Pack de 20 fotos producto $500-1,500 $1.21 ~99% 1 hero video animado (Kling/Seedance) $1,000-3,000 $0.39-3.31 ~99% Landing page completa con assets $2,500-7,500 $5-10 ~99% 4 UGC testimoniales $400-1,200 $3.68 ~99% **Pack agencia completa (todo)** **$5,000-15,000** **~$11** **99%+**

**Tu insight clave para vender**:

- No vendes la "IA". Vendés el **resultado** (ad cinematográfico premium).
- El cliente no necesita saber que usas IA. Si entrega calidad, valor de dólares y velocidad, el cliente paga.
- **Tu ventaja vs agencias**: turnaround de **3 días** vs **3 semanas** en agencias.

### Cómo conseguir el primer cliente

Ya cubrimos esto en Imperio en otro contenido — busca la sección **"Tu primer cliente"** en el Classroom. El sistema combina:

1. Outreach personalizado a marcas con landing pages malas
2. Mostrarles un mockup ya hecho (con IA, tarda 1 hora)
3. Cobrarles el 50% upfront
4. Entregarles en 3 días

---

## 📚 Recursos exclusivos para miembros de Imperio

Todo lo siguiente está disponible **dentro del Classroom de Skool**:

Recurso Dónde encontrarlo en Skool **Skill **`bencord-thumbnails-pro` (mi sistema de thumbnails) Classroom → Skills **Plantillas premium de Cloud Design** (incluye Motion Sites) Classroom → Cloud Design **Prompts del video** (los 8 prompts copy-paste) Classroom → Higgsfield MCP **Caso de éxito de David** (reemplazó agencia con OpenClaw) Classroom → Casos reales **Sistema de outreach para vender este servicio** Classroom → Tu primer cliente **Garantía Imperio**: tu primer sistema corriendo en 7 días o devolución 100% Página principal del Skool

---

## 🎯 Próximos pasos (orden recomendado)

Si estás empezando, haz esto en este orden:

1. **Hoy**: conectar Higgsfield al MCP (60 segundos) + crear cuenta si no la tienes
2. **Día 1-2**: generar las primeras 20 fotos de un producto tuyo (real o ficticio)
3. **Día 3**: animar 5 ganadoras con Kling 3.0
4. **Día 4-5**: armar la landing en Cloud Design + deploy en Vercel
5. **Día 6**: generar 3-4 UGC testimoniales
6. **Día 7**: tomar todo lo generado y armar tu primer pitch deck o demo para mostrarle a un cliente potencial

**Si tienes problemas en algún paso**, postéalo en el Skool con screenshot — la comunidad responde rápido (yo también).

---

## 🎬 Transcripción completa del video

A continuación la transcripción del video de YouTube tal cual quedó, con timestamps por capítulo. Útil para buscar momentos específicos o si prefieres leer en lugar de ver.

---

### 🎬 Capítulo 1: Intro — lo que vas a poder crear (0:00)

**0:00** Todas estas fotos que estás viendo las generé con inteligencia artificial. El video que estás viendo en este momento también está hecho con IA. Y fíjate los detalles, fíjate la luz, pausalo si quieres, mira cómo se mueve. Generado con IA.

**0:18** La landing page que estás viendo en este momento también se generó en un prompt. El hero, las fotos, el landing, absolutamente todo armado con IA. Y hasta el thumbnail o la miniatura de este video que entraste a ver fue generado con IA.

**0:27** Pero lo importante de este video no es eso, sino que te voy a enseñar un sistema para que puedas usarlo y crear este tipo de cosas en segundos con Cloud Code. Todo el proceso y el sistema para empezar a crear este tipo de cosas por tu cuenta, paso a paso y todo desde Cloud Code.

**0:45** Y lo importante también de este video es que vas a aprender cinco cosas concretas que puedes crear con Cloud Code sin estar saltando de pestaña en pestaña y de IA en IA.

**0:54** Primero vamos a ver cómo conectamos Higgsfield MCP, que literalmente acaba de salir esta semana, que hace todo el resto posible. Higgsfield lo usamos como intermediario para conectarnos a los mejores modelos de inteligencia artificial actuales.

**1:05** Segundo, ¿cómo podemos generar fotos profesionales desde Cloud Code? Vamos a hacer decenas de fotos del mismo reloj que viste y vamos a elegir las que más nos gusten.

**1:13** Tercero, vamos a darle vida y animar las que más nos gustaron para que después podamos usar como anuncios y puedas armar videos parecidos al que viste en el principio.

**1:22** Después, en cuarto lugar, vamos a ver cómo creamos testimonios UGC, es decir, gente también usando el mismo producto.

**1:31** Y finalmente, cómo agarraríamos todos esos assets y le pedimos a Cloud Code que nos cree una página increíble como la que te diseñaría una agencia top.

**1:39** Y como bonus al final también te voy a mostrar cómo creo mis thumbnails o mis miniaturas de YouTube usando este mismo sistema. Así es, los del thumbnail que apretaste de este mismo canal para ver el video.

**1:47** Te lo revelo también para el final porque sé que te intriga el cuánto cuesta. Vamos a desglosar los precios, lo que costó generar todo el contenido de este video y lo vamos a comparar con lo que te cobraría una agencia tradicional. Recomiendo que te quedes hasta el final porque esa cifra te va a sorprender.

**2:07** Pero antes de comenzar te agradecería mucho si me dejas un like en este video por todo el esfuerzo que le metimos, no solamente porque me ayudas a mí al canal, sino porque también le dices a tu YouTube y tu algoritmo que este estilo de videos te gustan y te empieza a recomendar más como estos. ¿Okay?

**2:25** Vamos, ahora sí, la primera pieza y la más importante: vamos a conectar Higgsfield al MSP de Cloud Code.

---

### 🔌 Capítulo 2: Conectando Higgsfield MCP a Claude Code (2:33)

**2:33** El stack que vamos a usar son dos cosas. Primero tenemos Cloud Code, que vendría siendo como el cerebro. Es el agente que está detrás orquestando el plan y mandando ejecutar cosas. Y efectivamente el que se comunica y que tiene los modelos de inteligencia artificial, en este caso es Higgsfield, que funciona como una pasarela.

**2:52** Y si es que entras acá, por ejemplo, tienes muchos modelos de inteligencia artificial que puedes usar. O sea, tienes los de imágenes, por ejemplo, el ChatGPT Image 2 o tienes en los videos los, no sé, los modelos como Seedance o Kling cualquiera.

**3:04** Lo interesante es que tenemos que hacer solamente una conexión. Entonces, en vez de estar conectándonos a cada API de manera independiente, es decir, a la de OpenAI, después a la de Seedance, por ejemplo, o Kling o lo que sea, podemos gastar un mismo sistema de créditos unificados en un mismo lugar.

**3:21** Existen otras aplicaciones que se pueden usar como Replicate o como Fal. Pero mi arma de preferencia en este caso es Higgsfield, así que vamos a ir con esa.

**3:30** Una de las razones también por la que este sistema lo encuentro tan cómodo es porque recientemente lanzaron el Higgsfield MCP, y simplemente entrando a Cloud y conectándolo y copiando y pegando este custom connector, tenemos acceso a Higgsfield para poder generar y acceso a los mejores modelos.

**3:45** De aquí arriba sale "turn into a creative engine". Entonces lo que vamos a hacer es justamente conectarlo acá, pero no vamos a hacer una llamada API como lo hacíamos antes, sino que ahora vamos a usar el MCP.

**4:00** El MCP vendría siendo este conector universal que nos ayuda a conectar distintas herramientas de inteligencia artificial entre sí. Entonces, es como este puente o este nexo entre los programas IA o los LLM y las herramientas externas.

**4:14** Entonces, tenemos acceso y tenemos derecho a estar mandando cosas y estar extrayendo cosas o recuperando ciertas cosas. En este caso, si le mandamos hacer 20 imágenes a Higgsfield de ChatGPT o con ChatGPT, va a mandar a hacerlas y después nos las va a devolver.

**4:30** Esa es como la lógica que está detrás. Y la instalación es bastante sencilla. Simplemente abres Cloud, abres un custom connector y entramos y nos conectamos.

---

### ⚙️ Capítulo 3: Instalación del custom connector paso a paso (4:37)

**4:41** Si nos queremos conectar a Cloud, en este caso, tenemos que abrir Cloud, tenemos que irnos aquí a donde sale configuración. En configuración nos vamos a conectores y bajamos y ponemos agregar conector personalizado.

**4:52** Después entramos acá, copiamos Higgsfield MCP, llegamos, lo pegamos y aquí le ponemos el nombre que queramos. Entonces, aquí le vas a dar a agregar, luego le vas a dar a conectar y después le vas a dar a permitir.

**5:08** Después te va a decir que quieres abrir Cloud y vas a darle a abrir y listo, ya está conectado. Es así de sencillo.

**5:17** Entonces ahora podemos decirle cosas como "crea a través de Higgsfield una imagen en ChatGPT Images 2 de una rana con corona teniendo un cartel que dice Cloud es lo mejor".

**5:25** Ahora, si nos damos cuenta, va a hacer un llamado vía Higgsfield MCP a el modelo de ChatGPT y listo, ahí nos generó la imagen. Ahora obviamente podríamos hacer cualquier cosa, podríamos decirle "anímalo con Seedance", etcétera.

**5:46** Pero ese no es el punto del video. El punto del video era ver cómo nos conectábamos con Cloud Code para tener un lugar y un canal all-in-one para poder hacer todas las funciones que haría una agencia.

**5:54** Es decir, crear múltiples imágenes de un producto, crear los videos, crear landing pages bonitas. Y eso lo vamos a hacer en Cloud Code. Vamos a entrar a Cloud Code y puedes hacerlo vía VS Code si es que te gusta más o te gusta usar algún tipo de CLI.

---

### 🏗️ Capítulo 4: Setup del proyecto agente de agencias (6:25)

**6:25** Y lo que vamos a hacer acá es podemos volver a conectarnos en el caso de que quisiéramos vía MCP. Entonces, supongamos que no quieres conectarte de esa manera, tienes otros métodos para conectarte. Simplemente puedes llegar acá y abres un nuevo proyecto.

**6:33** Le puse "agente de agencias" y le voy a decir, conéctame al MCP de Higgsfield. Estando acá, le paso el Higgsfield.MCP, o le paso el link directamente.

**6:48** Va a hacer la conexión, va a entrar a la cuenta y te va a pedir aprobar la cuenta. Le voy a poner omitir permisos, permitir siempre.

**6:59** Nos dice "estoy en un plan, nos quedan 406 créditos y vamos a empezar a crear cosas". Me interesa crear varias cosas: las imágenes, los videos, las landing pages. Vamos a crearlas todas, pero creo que la mejor base es crear las imágenes.

---

### 📸 Capítulo 5: Generando fotos de producto del reloj (7:14)

**7:14** Lo que le voy a decir es: a continuación te voy a pasar un par de fotos de un reloj. Lo que necesito es empezar a sacar varias fotos en distintos contextos. Vamos a sacar ocho fotos distintas. Vamos a usar ChatGPT Images 2, ese modelo específicamente, y vamos a generarlas en low para que nos gaste menos créditos.

**7:34** La idea de esto es poder elegir las que más nos van a gustar, prueba distintos ángulos, distintas cosas para iniciar y armar una campaña publicitaria.

**7:51** Voy a llegar y le voy a poner dos fotos. Le voy a adjuntar estas dos fotos que ya las generamos previamente para que tenga una referencia qué es lo que estamos creando.

**7:59** Le voy a dar enter y va a empezar a crear las imágenes. Hay muchas variables también con las que podemos jugar, obviamente, pero en este caso vamos a lanzarlo y vamos a ver qué es lo que nos está creando.

**8:21** Si te vas aquí arriba a la derecha donde sale assets, podemos ver que se van a empezar todas las cosas que generamos a través de Cloud Code se van a ir guardando acá. De hecho, estos son algunos de los thumbnails que he ido creando y he estado probándolo bastante y ha funcionado muy bien.

---

### 📝 Capítulo 6: Creando el CLAUDE.md de la agencia (9:09)

**9:09** Por mientras que se están creando las imágenes, voy a empezar a crear el cloud.md. Este es el archivo que van a ser como las instrucciones guías que tiene que seguir esta gente que estamos creando.

**9:25** Eres el director creativo y ejecutor de una agencia de diseño bastante específica de un branding muy elevado, bastante boutique. Y la idea es que te vas a conectar a Higgsfield y a distintos modelos de inteligencia artificial.

**9:34** Siendo ChatGPT Images 2 y Seedance 2.0 y Kling 3.0 las herramientas o las mejores herramientas de este momento o los modelos por lo menos al grabar este video.

**9:41** Y tu idea es que vas a redactar y vas a mandar a hacer los mejores prompts y los mejores imágenes y videos para la agencia que se llama agencia imperial.

**9:54** La idea es que te vamos a ir pasando ciertas cosas y tú vas a ir generando los mejores prompts y sacando los mejores modelos posibles. Tienes que tener y seguir una serie de guidelines premium.

**10:10** Vas a investigar también un poco cómo qué es lo que hace una marca premium y que se vean fotos de alta calidad y después vas a proceder a crear tu archivo cloud.md.

**10:44** Generemos siempre en low y baja resolución. Si nos gusta alguna, un upscale, vamos a hacerle en el caso de que te seleccionemos alguna.

**10:54** Esto es para que podamos ir generando más cosas, más volumen y después solamente hacer upscale de las que nos gustan.

**11:08** Vamos a mandarle este prompt por mientras para que vaya trabajando otro agente. Y tenemos ocho jobs. Por mientras vamos a esperar que se terminen.

**11:24** Entonces fíjate acá, las creamos. Acá tenemos una, tenemos dos, ya tenemos tres, esa está buena. Tenemos cuatro, esa también me gustó harto. Tenemos cinco, tenemos seis, tenemos siete, está perfecto, tenemos ocho.

**11:42** Entonces aquí tenemos ya las ocho que nos gustan. En el caso de que nos guste alguna, podemos decirle, "Oye, mira, me gustó esta imagen que está acá. Procedamos a generar el video".

**11:49** Vuelve a generar ocho más y vamos a generarlas todas en formato 16:9, horizontal, low quality. Piénsalas como fotos que podríamos usar tanto en Ads como fotos que podríamos usar en una landing page. El back de la marca es Luxury Man, Relax, Healthy Natural.

**12:34** Si es que entramos acá, nos vamos al Finder y nos vamos a la carpeta de agente de agencias, podemos ver que todos los archivos se van creando y se van guardando a nivel local.

**12:55** Las que nos gusten le podemos hacer upscale. Creo que están bastante buenas, la verdad. Hay varias que me gustan, cumplen el vibe.

**13:10** Y ahora le voy a pedir: dame ocho más solo de productos para luego elegir las finales y animarlas con Kling. Solo la selección que te diga.

---

### 🎞️ Capítulo 7: Animando las imágenes con Kling (13:25)

**13:25** Esto es una carpeta y tenemos varias opciones, pero tenemos que hacerle un upscale y tenemos que empezar a animarlas las que nos gustan. Y esto nos lleva al segundo caso de uso y es que podemos crear videos directamente acá.

**13:42** Vamos a hacer la selección y le voy a decir, "Okay, me gustaron las B308, B208, B207, B206, B306".

**15:03** Vamos a mandar a crear videos de todas estas que están acá. Idealmente hay otras maneras en las que podemos hacerlo mejor, claramente, como tomar un endframe y un startframe y animar la transición, pero creo que podría ser bueno.

**15:17** Le voy a decir: me gustaron todas estas que te dejé arriba. Lo que vamos a hacer es vamos a crear para cada una de ellas, vamos a crear una especie de animación y la animación la vamos a crear usando los modelos de Kling.

**15:30** Hagámoslo con movimiento sutil, no tiene que ser tanto. Es lento todo, esa es como un poco la vibra que me estoy imaginando.

**16:09** Quizás no tanto por Higgsfield en sí, sino por los modelos a los que tengo acceso y la facilidad de uso. Creo que es bastante buena y ahora que tenemos el MCP me lo hizo aún mejor.

**16:29** Estoy usando Kling en este caso por el precio. Por el precio, Kling está a 40 créditos y Seedance 2 está a 63. Hay otro que es Seedance 2 Fast que también funciona bastante bien.

---

### 🎥 Capítulo 8: Resultados de los videos cinematográficos (17:00)

**17:00** Cáchate, los resultados creo que están muy buenos. Aquí hay como un leve zoom que se nota, o sea, que no es una foto, sino que se ve como más un video.

**17:15** Aquí tenemos el minutero avanzando muy lento, muy lento. Creo que está bueno. Podríamos haberlo hecho quizás porque el logo no se ve como excelente, entonces quizás podría haber usado el ChatGPT en high quality, no en low quality.

**17:36** Estos como sueltos no se ven tan bien quizás, pero cuando lo juntamos en un video queda épico, épico, épico.

---

### 🌐 Capítulo 9: Armando la landing page con Cloud Design (17:58)

**17:58** Vamos a volver a Cloud y vamos a decirle: me encantó. Pasar las imágenes que me gustaron y los videos a una carpeta con todo. La idea es que le voy a subir esta carpeta a Cloud Design para armar un sitio web.

**18:33** En Cloud Design vamos a montar una página web que luego vamos a hacerle deploy acá. Necesito que me hagas el one shot del prompt de Cloud Design con la vibra y todo lo que tenemos que armar.

**19:05** Y bueno, aquí después de unos minutos fui a refilarme el café, volví, está buenísimo. O sea, creo que es una muy buena primera impresión.

**21:06** Una cosa también interesante para la gente que está en Imperio Digital, esto tiene un precio acá de $150. Nosotros al final lo que hicimos es pagamos el plan de agencia para poder regalar todas estas plantillas y tener, de hecho, el derecho de revenderlas.

**21:15** Así que para la gente que está en Imperio, si es que le interesa, puede entrar a Skool, puede irse aquí al Classroom, puede buscar en Cloud Design y en Cloud Design publiqué todas las plantillas, incluidas las premium que pueden usar.

---

### 📥 Capítulo 10: Importando assets y generando el sitio (22:01)

**22:07** Todo esto algo quitaría una agencia y te cobraría cientos de dólares, miles de dólares. Incluso la gente me dice que exagero cuando digo que es un trabajo que podría decir $10,000 fácil, pero si te fijas y ves lo que están cobrando las agencias boutique, te aseguro y te vas a dar cuenta que no.

**22:24** Una marca Rolex, por ejemplo, o en este caso la marca que estamos armando por sacar este tipo de imágenes, te puede pagar superbién. Y generalmente buscan agencias más chiquititas, pese a que son marcas supergrandes.

**22:55** Se puede pagar porque al final igual tienen un ROI clarísimo, o sea, un buen pedazo de creativo les va a generar el ROI suficiente como para poder pagarte esos 5K.

---

### 🚀 Capítulo 11: Deploy en Vercel desde Claude Code (28:55)

**28:55** Supongamos que nos gustó el diseño final. Ahora simplemente nos vamos a ir a compartir. Vamos a irnos acá a "hand to cloud code", vamos a copiar el comando y vamos a entrar a Cloud Code y le vamos a decir: hazme deploy de esta página web.

**29:08** Ahora si es que entras a esta página, "Aterna Odyssey Vercel App", vas a ver que literalmente está acá funcionando la página que acabamos de crear.

**29:24** Si le quisieras conectar un dominio, simplemente te vas acá y le dices "Okay, conectemos un dominio juntos". Y listo. O sea, algo que agencias te cobraban cientos y, incluso miles de dólares, ya lo podes empezar a hacer por tu cuenta con un poco de esfuerzo y dedicación a esto.

---

### 📲 Capítulo 12: Contenido UGC con Seedance 2.0 (29:39)

**29:39** Pero ¿qué pasa si es que ahora quieres empezar a sacar más tipos de creativo? Bueno, vamos a empezar y vamos a entrar con lo que es el contenido UGC y le voy a decir: créame contenido UGC usando Seedance 2.0 para el reloj.

**30:04** Créame tres videos verticales, porque vamos a hacerlos para Instagram, para Facebook, para ir promocionando.

**30:12** Le voy a pedir: créame contenido UGC usando Seedance 2.0 para el reloj. Créame tres videos verticales de nuestro carácter o personaje principal hablando y mostrando el reloj, es decir, usa las imágenes de referencia que tengas que usar.

**30:55** Y bueno, después de unos minutos podemos ver que ya nos dio el resultado. Aquí está reintentando uno porque directamente le bloqueó algo. Entonces, fíjate lo interesante: mandó hacerlo, detectó que lo bloqueó y volvió a mandarlo.

**32:18** Eh, creo que se nota super poco que es generado. Y esto es lo que hace que un reloj sea único.

**32:53** Bueno, aquí puedes empezar a jugar tú. O sea, recordemos que estamos usando aquí el Seedance 2.0, por ejemplo, y podemos elegir cuánto queremos que dure. Puede ser hasta 15 segundos en este caso.

---

### 🖼️ Capítulo 13: Bonus — cómo creo mis thumbnails de YouTube (33:43)

**33:43** Otra cosa que encuentro super interesante que podemos hacer y que también te haría una agencia directamente es el hecho de estar creando thumbnails. O sea, todas las miniaturas de los videos de YouTube que has visto, sobre todo las de mi canal, son generadas con inteligencia artificial.

**33:58** Hoy día yo llego y entro, por ejemplo, a Cloud, me voy aquí donde sale content creator y le pido: générame cinco thumbnails para un video que se llama "reemplacé una agencia completa creativa con cloud code".

**34:18** Asegúrate de usar tu skill. El skill que tengo en este caso es un skill directamente que le creé previamente, que se conecta a Higgsfield y nos crea los thumbnails o las miniaturas con cloud code en Higgsfield. Usando el modelo de ChatGPT.

**35:08** Por ejemplo, este fue 100% creado con IA. Este que estás viendo acá. Este también fue creado con IA. Este de "agentes en 18 minutos" también fue creado con IA. Llegó a los 160K.

**35:52** Aquí lo bueno es que podemos jugar a el volumen. No sé, puedo pedirle no cinco, sino que puedo pedirle 20 thumbnails, o 50, y ahí puedo llegar y recién elegir y empezar a pulir los que me gustan.

---

### 💰 Capítulo 14: Desglose completo de costos (36:19)

**36:19** Si es que nos vamos a images y entramos a GPT Image 2, podemos ver que nos salen aquí los precios de cuánto nos sale cada generación. Esto va a depender de cada uno de los criterios.

**36:36** Si es que vamos a generar en 4K, nos va a costar 12 créditos. Pero si lo vamos a generar en low y lo vamos a crear en 1K, nos va a costar 0.5, que este es el que me gusta usar a mí para prototipar.

**36:55** Si estamos creando acá en este caso 0.5 por 50, vamos a generar 50 thumbnails, me estaría solamente gastando 25 créditos.

**37:23** Yo estoy pagando el Plus en este momento que tiene $50 y viene con 1000 créditos. Siendo 49 y 1000 créditos, nos saldría algo como 49 dividido en 1000 es igual a 5 centavos por cada uno de los créditos.

**37:55** Entonces esos 5 centavos nos gastamos por las 50 que eran 25 + 21 eran 46. Nos gastamos 2.2 dólares en generar 50 thumbnails y hacerle el upscale después a tres para que queden en calidad alta.

**38:32** Para este caso, el video que generamos era de 8 segundos. Lo generamos en 720, nos sale 36. Pero ya si queremos crear alguno un poco más largo, como de 15 segundos, ya podemos ver que es harto más.

**38:48** Suponer que es un video de UGC, 15 segundos si queremos un video UGC ya un poco más largo, vamos a quedarnos mejor con este 68. Y nuevamente calculamos acá que era 0.049. Te sale $3.30 por video.

**39:15** A diferencia de lo que te saldría pagarle a alguien para que te grabe ese video, creo que es bastante bastante rentable. Pero es importante tenerlo en cuenta que este es el modelo más caro de todos.

**39:23** Si quisiéramos usar modelos un poco más económicos, no usaríamos el Seedance, sino que usaríamos el Kling. El Kling es el modelo que usamos de hecho, para justamente animar los videos que vimos previamente que usamos en la landing page.

**39:39** En este caso creamos ocho videos. Entonces 10 × 8 serían 80. 80 × 0.049 es igual a $4. Nos gastamos en crear todos estos videos.

**40:18** Yo lo uso, dejé de pagar ChatGPT porque uso Cloud, la verdad, el día de hoy, pero sí lo uso para poder acceder al modelo de ChatGPT Images 2, que encuentro que está muy bueno y me permite generar muchos videos a escala.

**40:29** Y bueno, todo lo que nos gastamos en este video al final no terminó siendo más de $10 en total.

---

### ⚠️ Capítulo 15: Lo que la IA NO puede reemplazar (40:39)

**40:47** Y ahora también un pequeño disclaimer porque no quiero que pienses que todo esto que está acá es magia y llega la IA y te hace todo por ti, porque no. También hay una serie de limitaciones y te voy a ser completamente honesto y transparente en ese sentido.

**40:55** Primero, la IA no reemplaza la estrategia. O sea, estamos conectando Cloud Code con Higgsfield, pero no te dice exactamente qué decir, no te da un buen criterio, no te va a dar gusto, por lo menos a la fecha en la que estamos hoy día.

**41:11** Si tu posicionamiento está mal o crees algo, eso te va a generar más versiones de algo que tú crees que está mal y que está mal directamente y te va a seguir generando versiones malas.

**41:19** Hay un concepto que se llama "garbage in, garbage out", es decir, si la alimentas al prompt pura mierda, te va a generar pura mierda.

**41:33** Lo que sí está reemplazando en este caso es la ejecución, ya no la estrategia. Entonces, en vez de tener que llegar y generar todas las cosas de manera manual en cada una de las aplicaciones, estamos mandándole en batch a Cloud Code y dejando que gaste así en masas.

**41:42** Segundo, la parte del gusto: el ojo crítico y todo lo que está detrás al final y tu criterio es tuyo. Tu criterio, tu capacidad de criticar, de diferenciar si algo es bueno, si algo es malo. Eres tú el crítico.

**41:57** El criterio es tuyo y el gusto es algo que la IA todavía no tiene bien. Pero ya teniendo eso en cuenta, al final esto va a poder ayudar a un solopreneur a crear mucho más rápido.

**42:14** Va a derribar las barreras de tener que gastar plata contratando una agencia para generar todo este tipo de cosas creativas o de contenido audiovisual o de páginas web.

**42:21** Yo creo que el día de mañana todos vamos a tener nuestra propia empresa, nuestra propia agencia, que va a pasar a ser como un poco también nuestra marca personal, pero eso ya da una tesis completa para otro video.

---

### 🎯 Capítulo 16: Recap final (42:52)

**42:56** Recapitulando todo lo que hicimos hoy día, vimos varias cosas:

- Vimos primero **cómo conectamos Higgsfield a Cloud Code**.
- Después **cómo empezamos a generar muchas imágenes distintas** y empezamos a usar los modelos de ChatGPT Image 2 o los modelos que están dentro de Higgsfield.
- Después aprendimos a **animar directamente todos los videos ganadores** solamente en contexto.
- Después vimos **cómo montábamos una landing page**, una landing page bastante buena, bastante decente. Vimos cómo la desplegábamos y la dejábamos online.
- Después vimos **cómo creabamos contenido UGC** para empezar a crear testimonios, reviews, literalmente lo que quieras usando el modelo de Seedance.
- Y como bonus también viste **mi sistema de creación de thumbnails**.

**43:41** Y todo esto al final nos terminamos gastando alrededor de **$10 en iterar y probar**.

**43:49** Si quieres probar el stack, también te dejo el link de Higgsfield abajo en la descripción por si quieres algunos créditos extra, ahí también me ayudas a mí. También te voy a dejar la URL exacta de la conexión a MCP.

**44:04** Si te interesa seguir aprendiendo sobre esto, también te recomiendo que te des una vuelta por **Imperio**. Tenemos casos como los de **David, que reemplazó una agencia completa usando solamente OpenClaw**.

**44:11** En Imperio también garantizamos tener corriendo tu primer sistema en 7 días o si no te devolvemos el 100% del dinero. Es actualmente la comunidad más activa y hispanohablante de automatizaciones e inteligencia artificial.

**44:22** Y por último, si les gustó toda la parte de construir páginas web, también tengo un video super bueno acá donde construimos páginas web animadas con Cloud Design y el curso más completo de Cloud Code en español. Acá son más de 3 horas completamente gratis en YouTube, así que recomiendo que lo veas.

**44:30** Ya, nos vemos.

---

## 💬 ¿Tienes preguntas? Posteá en el Skool

Si te trabaste en algún paso, postea en la comunidad con:

- Screenshot del problema
- En qué paso estás (1-8)
- Qué prompt usaste

Los respondo yo y la comunidad activa también ayuda. 

Nos vemos  🔥

— Benja
