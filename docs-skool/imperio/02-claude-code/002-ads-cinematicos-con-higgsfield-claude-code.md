# Ads Cinemáticos con Higgsfield + Claude Code

> Ruta: Claude Code › Ads Cinemáticos con Higgsfield + Claude Code

**🎬 Vídeo (33.6 min):** https://youtu.be/Q0ITE2jdl1M

**📎 Recursos:**
- v3_imperio_ads_cinematicos_claudec

---

Si viste el video, acá te dejo **todo lo que prometí**, sin filtros, listo para que lo descargues y lo corras esta misma tarde.

La skill `ads-cabrones-ia` es lo que uso yo para generar los comerciales cinematográficos que les enseño en el video. La botella Nalgene completa, las 8 escenas extremas (Sahara, Mars, Ártico…) todo eso sale **con un solo prompt**.

No es teoría. Es la **skill exacta**, las **guías exactas** para conectar Higgsfield, ElevenLabs y Airtable, y los **casos de estudio reales** con direction.json incluido para que clones lo que te guste.

Lo único que necesitas hacer es **descargar el skill** que está al final de este post, descomprimirlo en tu carpeta de skills de Claude Code, y correr el wizard de onboarding. El resto del flujo está explicado paso a paso en el video.

Si te saltaste el video — [velo acá primero](LINK_AL_VIDEO). Este post es el complemento.

---

## LO QUE VAS A ENCONTRAR EN ESTE POST

1. La skill `ads-cabrones-ia-v2.3.tar.gz` (descargable) — el activo más importante
2. Las **plantillas** que necesitas: concept board en blanco + ejemplos llenos
3. Las **3 guías de conexión** paso a paso (Higgsfield MCP, ElevenLabs API, Airtable PAT)
4. La **base de Airtable** lista para clonar (con todos los campos pre-armados)
5. **2 casos de estudio completos**: "El viejo oeste" (Ford F150) y "El Tritan" (Nalgene 32oz) — con direction.json, prompts exactos y MP4 finales
6. El bonus: **8 escenas extremas** del mismo Nalgene en lugares imposibles (Sahara, Mars, Ártico, etc.) — para que veas que el método aguanta cualquier vibe
7. Un mini-FAQ con los **bugs reales** que vas a encontrarte y cómo los resolvés (los aprendí en carne propia)
8. Cómo sumarte a la próxima sesión donde construimos un ad de un miembro en vivo

---

## 1. LA SKILL `ads-cabrones-ia-v2.3`

El archivo comprimido que descargas y descomprimes en `~/.claude/skills/`. Convierte a Claude Code en tu director creativo + productor + editor.

**Qué hace**:

- Recibe tus 3 inputs (money shot + concept board + brief en texto libre)
- Invoca al **Director Creativo** (sub-agente interno) que genera un JSON estructurado con las 6-8 escenas, prompts de imágenes, prompts de videos, guion del voiceover y prompt de música
- Te pide aprobación **una sola vez**
- Después se va: genera todas las imágenes en paralelo con GPT Image 2 vía Higgsfield, anima cada escena con Seedance 2.0, saca la voz con ElevenLabs, junta todo con ffmpeg y persiste el proyecto en Airtable
- Te entrega 2 versiones: **FULL** (narrativa lineal, 30-50s) + **CUTS** (cortes intercalados ritmo social, 20-30s)

**Cómo usarlo (resumen)**:

1. Descomprimes la skill en tu carpeta global de skills: ```bash
mkdir -p ~/.claude/skills
tar -xzf ads-cabrones-ia-v2.3.tar.gz -C ~/.claude/skills ```
2. Reinicias Claude Code (cierras y vuelves a abrir)
3. Abres Claude Code en tu carpeta de proyectos: ```bash
cd ~/Documents/ads-cabrones-proyectos
claude ```
4. Le dices: *"vamos a hacer un ad cinematográfico"*
5. La primera vez te corre el **wizard de onboarding** (5 preguntas, ~2 min)
6. Después de eso, le pasas tus 3 inputs y a los 6 minutos tienes el ad listo

**Versión**: 2.3  
**Última actualización**: 2026-05-04  
**Tamaño**: ~30 KB (es liviano porque solo es la lógica — los assets se generan al vuelo)

---

## 2. LAS 3 PIEZAS QUE TÚ CREAS A MANO

Aunque la skill hace el 90% del trabajo, hay 3 cosas que **siempre** las creas tú. Sí o sí. Acá entra el criterio humano.

### 2.1 — Money Shot

La escena que captura la esencia del ad. La imagen "wow" que define todo el tono. Generalmente una composición wide cinematográfica.

**Cómo crearla**:

- Generala con ChatGPT (Imagen 4) o Gemini (Nano Banana)
- O sube una foto real si ya la tienes
- Si tu producto es real (auto, perfume, fashion), usa una foto profesional del producto en su contexto ideal

**Ejemplo del video** — el money shot de la Nalgene:

- Wide cinematográfica del Nalgene en una cumbre al amanecer, mountains de fondo, golden hour

### 2.2 — Concept Board

El grid donde defines 3 cosas: **Personaje + Entorno + Producto**.

**La plantilla en blanco**: [concept-board-template.png](ADJUNTAR_PLANTILLA)

**Cómo llenarla**:

- **Personaje** (si tu ad tiene): 1 imagen principal + 4 vistas (cabeza frontal/lateral, 2 poses)
- **Entorno**: 1 imagen principal + 2 vistas alternas
- **Producto**: 1 imagen principal + 2 vistas alternas

⚠️ **TIP CRÍTICO** — para evitar el flag de Seedance ("ip_detected" / "sensitive content"):

- Las vistas frontales del rostro tienen que tener **blur ligero** (Gaussian 8-15px) o estar en tres cuartos
- No subas closeups perfectos del rostro — el modelo se asusta y rechaza el job
- Para productos no hay drama, sube las vistas que quieras

**Ejemplo del video** — el concept board del Ford F150 ("El viejo oeste"):

### 2.3 — Brief / dirección creativa

Texto libre. Le dices a la skill de qué va el ad. Lo más simple posible.

**Template mínimo**:

```
Target: [quién es el espectador / personaje del ad]
Producto: [qué vendes]
Setting: [dónde se graba]
Tono emocional: [opcional]
Tagline: [opcional, si ya tienes]
Script: [opcional, si ya tienes]

```

**Ejemplo real del video — Nalgene "El Tritan"**:

```
Target: outdoorsy, aventurero, alguien que valora durabilidad por encima de todo.
Producto: botella Nalgene 32oz wide-mouth Tritan plastic.
Setting: situaciones extremas — laboratorio, mountains, desierto, océano.
Tono emocional: cinematográfico high-tech futurista. Apple meets Ridley Scott meets Patagonia.
Tagline: "Hecha para durar más que tú."

```

**Ejemplo real del video previo — Ford F150 "El viejo oeste"**:

```
Target: hombre 40 años, redneck con estilo, masculino y elegante.
Producto: Ford F150.
Setting: Wild West americano, desierto al atardecer.

```

Eso es todo. Dos a cinco líneas. La skill lee el brief, mira tu money shot, mira tu concept board, y arma el resto.

---

## 3. LAS 3 GUÍAS DE CONEXIÓN

Para que la skill funcione, necesitas conectar 3 servicios. Cada guía toma 2-3 minutos.

### 3.1 — Higgsfield MCP

Higgsfield es donde se generan las imágenes (GPT Image 2) y los videos (Seedance 2.0). Lo conectas a Claude Code vía MCP.

**Plan necesario**: Plus o superior. El plan Plus te da ~600 créditos/mes que alcanza para ~3 ads completos. Si vas a hacer más, te conviene Pro o Ultra.

**Cómo conectarlo**:

1. Vas a [higgsfield.ai](https://higgsfield.ai) y creas cuenta
2. Activas el plan
3. Vas a la sección MCP / API
4. Copias el comando que te dan y lo pegas en tu terminal: ```bash
claude mcp add --transport http higgsfield https://mcp.higgsfield.ai/mcp ```
5. Reinicias Claude Code

### 3.2 — ElevenLabs API

ElevenLabs es donde se genera la voz (y opcionalmente la música). La skill se conecta vía API key.

**Plan necesario**: Free funciona OK para empezar (10K caracteres/mes). Si vas a hacer muchos ads, el plan Starter de $5/mes te da 30K caracteres, suficiente.

**Cómo conectarlo**:

1. Vas a [elevenlabs.io](https://elevenlabs.io) y creas cuenta
2. Vas a Settings → API Keys → Create New Key
3. Copias la key
4. Cuando corras el wizard de la skill, te la va a pedir y la pega ahí
5. La skill la guarda encriptada en `.env` con permisos 600 (solo tú la lees)

**Guía completa con screenshots**: [06-guia-elevenlabs.md](ADJUNTAR_GUIA_ELEVENLABS)

### 3.3 — Airtable PAT

Airtable guarda el proyecto entero (cada prompt, cada link, cada escena) como una base de datos. Te sirve para revisar ads pasados y pedirle a Claude que aprenda de ellos al armar uno nuevo.

**Plan necesario**: Free está bien.

**Cómo conectarlo**:

1. Vas a [airtable.com/create/tokens](https://airtable.com/create/tokens) y creas un Personal Access Token
2. Le das los scopes: `data.records:read`, `data.records:write`, `schema.bases:read`, `schema.bases:write`
3. Copias el token
4. Cuando corras el wizard, te lo va a pedir
5. El wizard te da 2 opciones: **clonar mi base lista** (recomendado) o **crear una desde cero**
6. Si eliges clonar la mía, te uso este link: [Clonar base Airtable Ads Cabrones IA](LINK_BASE_AIRTABLE)

**Guías completas con screenshots**: [05-guia-airtable-pat.md](ADJUNTAR_GUIA_PAT) + [03-airtable-template.md](ADJUNTAR_TEMPLATE_BASE)

---

## 4. LOS 2 CASOS DE ESTUDIO COMPLETOS

Para que veas que el método funciona con cualquier producto, acá tienes 2 ads enteros con todo el material crudo.

### 4.1 — Caso "El viejo oeste" (Ford F150)

El primer ad que hice cuando armé la skill. Hombre redneck masculino, F150, desierto al atardecer.

**Qué incluye**:

- `direction.json` (la dirección creativa completa que generó el Director Creativo)
- 8 imágenes 2K
- 4 videos 8s
- voiceover.mp3 (voz José Borda — ElevenLabs)
- music_prompt para Suno (si quieres tu propia música)
- nalgene-FULL.mp4 (versión narrativa lineal)
- nalgene-CUTS.mp4 (versión cortes social)

**Descargar**: [caso-el-viejo-oeste.zip](ADJUNTAR_CASO_F150)

**Detalle paso a paso**: [07-caso-estudio.md](ADJUNTAR_CASO_DETALLE)

### 4.2 — Caso "El Tritan" (Nalgene 32oz)

El ad que viste en el video del canal. Vibe high-tech futurist. 8 escenas, duraciones variables, voz Brian, música ambient cinematográfica.

**Qué incluye**:

- `direction.json` con las 8 escenas (5,5,6,5,7,5,8,5 segundos = 44s total)
- 16 imágenes (8 starts + 8 ends con cambio mínimo)
- 8 videos Seedance
- voiceover.mp3 (voz Brian, narrador profundo)
- soundtrack.mp3 (música future-tech ambient generada con ElevenLabs Music API)
- nalgene-FULL.mp4 (44s narrativa lineal)
- nalgene-CUTS.mp4 (28s cortes intercalados con patrón narrativo `[1,1,2,3,2,4,5,4,6,7,5,7,8]`)

**Descargar**: [caso-el-tritan-nalgene.zip](ADJUNTAR_CASO_NALGENE)

### 4.3 — BONUS: 8 escenas extremas del Nalgene

Después del ad principal le dije a la skill: *"pongamos la misma botella en 8 lugares imposibles, mismo encuadre"*. Esto es lo que salió:

1. **Sahara** — desierto + heat haze + dunas naranjas + sol cenital
2. **Ártico** — glaciar + aurora boreal + escarcha en el cap
3. **Volcán** — lava + ceniza + cielo rojo + reflejos naranjas en el plástico
4. **Pista bajo camión** — Ford F250 alejándose + dust cloud + golden hour
5. **Selva tropical** — Amazonas + lluvia torrencial + relámpago + agua escurriendo
6. **Cumbre Everest 8000m** — viento huracanado + snow streaks + cloud sea abajo
7. **Fondo oceánico** — peces bioluminiscentes + columna de luz + bubbles del cap
8. **Marte** — tormenta de polvo rojo + dust devils + atmósfera tóxica

**Lo interesante**: la botella siempre está en el **mismo encuadre, mismo ángulo, mismo tamaño**. Lo único que cambia es el universo a su alrededor + reacciones ambientales sutiles (escarcha en frío, condensación en calor, burbujas bajo agua, polvo en Mars).

**Descargar pack completo (8 imágenes + 8 videos)**: [bonus-8-extremas.zip](ADJUNTAR_BONUS_EXTREMAS)

---

## 5. FAQ — los bugs reales que vas a encontrarte

Estos son los problemas que YO me encontré armando los ads. Te los listo para que los reconozcas en el momento y los resuelvas en 30 segundos en vez de en 2 horas.

### ¿Por qué Seedance me marcó "ip_detected" o "nsfw" en una escena?

Pasa con escenas que tienen mucha cara cerca, o brand reveals con logos grandes, o transiciones tipo "muerte/dolor" emocional. La skill ya tiene un workaround: si una escena falla, automáticamente la genera con **ffmpeg + xfade** desde las imágenes start/end. Te queda casi igual de bien y no consumes créditos extra.

Si te pasa, vas a ver en el log un mensaje *"Seedance flag — generando con ffmpeg fallback"* y sigue de largo.

### ¿Qué hago si las imágenes me salen con orden mal?

Esto me pasó con el Nalgene. Las 8 imágenes se generaron pero un bug interno de la skill las nombró con un offset de 1 (scene-2-start era duplicado de scene-1, etc). Si te pasa: avisame por DM con el log de la sesión, lo arreglo y subo update de la skill.

**Cómo detectarlo rápido**: si ves que `scene-1-start.png` y `scene-2-start.png` tienen exactamente el mismo tamaño en bytes, hubo bug. Renombras manualmente o regeneras esa escena.

### ¿Por qué los videos salen a 720p y no a 1080p?

Default de Seedance 2.0 es 720p `std`. Si quieres 1080p, edita el direction.json antes de aprobar y pone `"resolution_video": "1080p"`. Cuesta el doble de créditos pero queda mejor.

### ¿La música autogenerada por Seedance suena mal, qué hago?

Por eso la skill **fuerza SFX-only en los videos** (sufijo *"Ambient SFX only — NO music"* en cada transition_prompt). La música la pones tú aparte:

**Opciones**:

1. **ElevenLabs Music API** — la skill puede generarla automáticamente con `scripts/elevenlabs_music.sh`. Sale OK para vibes ambient.
2. **Suno** — más cara pero queda mejor para épico. La skill te da el `music_prompt` exacto, lo pegas en Suno y descargas el MP3.
3. **Epidemic Sound** — música humana profesional. Es lo que recomiendo si tienes la suscripción.

### ¿Cuánto cuesta hacer un ad?

Costo real medido (caso Nalgene "El Tritan"):

- Higgsfield: ~250 créditos = ~$3.75
- ElevenLabs: ~$0.20 (voz) + $0 si usas free tier
- Claude Code: incluido en tu plan Pro/Max
- **Total: ~$4 por ad completo**

Considerando que campañas similares cuestan $5K-$10K en agencias, son **1000x más barato**.

### ¿Cuánto tiempo toma?

De cero a 2 MP4s listos: **6-8 minutos** una vez que tienes los 3 inputs hechos.

Lo que toma tiempo es preparar los 3 inputs (concept board + money shot + brief). Mi promedio:

- Primera vez: ~30-45 min total (descubriendo)
- Después: ~10 min de prep + 6 min de pipeline = **15-20 min total**

### ¿Funciona en Windows?

Sin probar. Los scripts son bash + Python, debería funcionar en WSL2 (Windows Subsystem for Linux). Si lo intentas y encuentras issues, repórtalo en el canal de Imperio Digital.

### ¿Puedo usar la skill comercialmente con clientes?

Sí. La skill es tuya para usar mientras tengas acceso a Imperio Digital. Lo único que **no puedes hacer** es:

- Revender la skill por fuera
- Redistribuir el .tar.gz a no-miembros
- Subirla a un repo público

Lo que sí puedes hacer:

- Usarla en proyectos tuyos y de tus clientes
- Cobrar por los ads que generes
- Modificar la skill localmente para tus necesidades

### ¿Cuántas escenas debería tener mi ad?

La skill por default sugiere **6-8 escenas**. Funciona bien para ads de 30-50 segundos. Si quieres algo más emocional tipo Cannes Lions, puedes ir hasta 10-12 escenas (más largo, ~60-80s, requiere más créditos).

Caso real: el ad **"El Abrigo"** que hice antes era de **11 escenas** (storytelling emocional). El Nalgene fue de 8. El Ford F150 inicial fue de 4. Depende del producto y del tono.

### ¿Mi música tiene que ser cinematográfica?

No necesariamente. La skill genera el `music_prompt` adecuado al tono del ad. Si tu ad es energético (deportivo, fitness), te va a sugerir música electrónica. Si es emocional, va a sugerir orquestal cinematográfico. Si es producto premium, va a sugerir ambient minimal.

Confía en lo que te sugiere, o cámbialo en el direction.json antes de aprobar.

## 🎙️ Transcripción

Este anuncio que vas a ver a continuación es de esta botella y lo creé con un solo prompt. En 1949, [música] un científico la inventó para sobrevivir al laboratorio. Resistente a [música] 60º bajo cer y al peso de un camión. Sin BPA, sin metales, sin compromisos. Solo un material que sobrevive lo que tú vivas, cumbres, [música] desiertos, décadas, generaciones. Nalgin hecha para durar más que tú. Y esto que acabas de ver, el comercial completo, fue hecho 100% con cloud code, la voz, la música, las imágenes, los videos, el tagline final, las escenas e incluso también nos juntó y editó el video. Todo esto sin tocar Premiere, sin sacar cada imagen o animar cada imagen manualmente, sin grabar la voz, sin absolutamente nada. Lo único que le dije fue, "Necesito crear un anuncio de esta botella." Aquí tienes la imagen. Le pasé tres referencias visuales de la botella en distintos ángulos y en 6 minutos ya me tenía este video completamente listo. [aplausos] Y en este video te voy a enseñar exactamente eso, cómo puedes replicar este sistema para que en un solo prompt te cree este tipo de videos por tu cuenta y vamos a desglosar absolutamente todo, los costos, los detalles, la ejecución, absolutamente todo. Así que para el final de este video vas a ser capaz de crear tus propios videos usando este sistema en tan solo unos minutos. Pero antes de comenzar te agradecería un montón si es que me dejas un like en este video, no solo porque me ayudas a mí y todo el esfuerzo que le metí en la producción de este video, sino porque también le dices a tu YouTube que este tipo de contenido te gusta, te sirve y te empieza a mostrar más contenido de este estilo. Ahora sí, pongamos manos a la obra. Hace unos meses mostré cómo creábamos eh ads cinemáticos usando NHN y orquestando distintos modelos de inteligencia artificial. Y el video era bastante largo y bastante complejo, es decir, era un setup que funcionaba, pero costaba bastante hacerlo andar. Hoy día el sistema que acabo de crear funciona prácticamente en automático y tú no tienes que hacer nada, literalmente le puedes dar un solo prompt. Pero vamos un poco más a las bases. Pensemos qué teníamos que hacer cuando queríamos crear videos manualmente. Lo que hacíamos era abríamos chat GPT, sacábamos las imágenes, usábamos algún generador de música como Suno, por ejemplo. Animábamos las imágenes con los videos o los modelos de guía como BO3 o como Sidans 2.0. Le dábamos la voz con Eleven Labs, ¿verdad? Y con Premiere teníamos que llegar y juntar todos estos videos. Al final teníamos que estar orquestando todo manualmente y teníamos que juntar todo en algún programa de edición. Era bastante lento y era super poco escalable. Hoy día lo que podemos hacer es orquestar todo a través de Cloud Code. Literalmente usamos Hixfield para las imágenes y los videos. Usamos fmp para juntar todo y levels para la voz y la música y air table si es que quieres trackar tus proyectos y tenerlos en algún lado. Aquí hice una gráfica que está un poco más bonito en Canva, pero es básicamente lo mismo. Cloud Code está orquestando char GPT, Sidans E y Level Labs para la creación. Lo único que tienes que hacer, que es completamente opcional, pero si quieres tener un poco de gusto, es eh crear tú un concept board, un money shot, un brief y después pasárselo a Cloud Code. Pero es completamente opcional y esto es en el caso de que quieras tener más control de lo que estamos creando. Ahora sí, vamos a ver cómo se vería esto en la práctica y desclosemos el cómo funciona. Vamos a abrir una nueva conversación en Cloud Code y vamos a decirle, quiero crear ads cinemáticos. Puedes estar usando Cloud Code directamente en la aplicación de escritorio de cloud, que es lo que estoy haciendo yo. O podrías estar usando PS Code o Antigravity o incluso podrías estar usando Codex. Da exactamente igual, el sistema es lo mismo. Voy a abrir una nueva conversación y le voy a decir lo siguiente. Vamos a crear un sistema donde yo te voy a ir pasando distintos archivos, es decir, te voy a ir pasando distintas fotos de productos y tú vas a idear ads cinemáticos, los anuncios cinemáticos. El stack que vamos a usar es Higfield. HiField lo vamos a usar para crear las imágenes y después animar esas imágenes. Vamos a usar los modelos de Char GPT Image 2 y vamos a usar el modelo de eh Sidans 2.0 para animar estas imágenes que creamos previamente. Luego vamos a usar Elevenlabs y nos vamos a conectar a Elevenlabs para eh sacar la música y también para crear la voz. Y después con fmeepgar y unir las distintas piezas que vayamos creando. Eh, te vamos a dar una foto de lo que sea y tú vas a, en este caso, empezar con todo lo que es el proceso de dirección creativa. Una buena dirección creativa tiene que tener, no sé, eh una buena historia que contar, tiene que ilustrar un punto bastante bien. Tienes que preguntarle quizás al usuario qué es lo que quiere destacar, qué es lo que quiere referenciar, cuál es el estilo que quiere hacer. Y luego tú vas a concatenar todo esto y lo vas a juntar en un video de música o digamos como con la música, con la voz, ¿verdad?, del mensaje que se quiere mandar con los videos ultra realistas y fidedignos a las eh a la foto del producto que se te entregó y eh vas a juntar todo esto y vamos a crear el mejor ad cinemático de el planeta. Okay, ahí acabamos de mandarle un prompt y vamos a empezar a hacer todo eso, pero creo que eso también ilustró bastante bien qué es lo que vamos a hacer y qué es lo que vamos a usar. Eh, lo único que no me detectó bien aquí era sedans, porque el resto creo que se ve bastante bien. Y le vamos a dar aquí a enter. Ahora lo que va a empezar a hacer es va a empezar a conectarse a Higfield, ¿verdad? a 11 Labs, eh a bueno, todos los servicios que necesitamos directamente. FFMPG no necesitamos nada porque está corriendo ahí en un script de eh Python, si es que no me equivoco. Y lo que sí necesitamos es entrar a Eleven Labs a sacar nuestra AP key. Aquí simplemente le damos a login, vamos, nos vamos a la sección de developers, vamos a AP Key y buscamos nuestra API Key y entramos a Hicksfield que recientemente lanzó su MSP y la verdad es que está muy bueno, muy bueno. A mí me encanta, me gusta mucho porque es como un lugar donde hay muchas herramientas de inteligencia artificial y si te fijas cada generación va quedando aquí arriba a la derecha en assets. Entonces son como distintas cosas. Esto es un intento de automatizar un canal de YouTube que estoy preparando, pero eh los hac el fan quedando ahí arriba y si te vas aquí donde sale Higfield MSP, te das cuenta que conectarlo a Cloud es bastante sencillo. Simplemente te vas aquí a donde sale settings, perdón, esto le voy a dar acá. omitir permisos y permitir siempre en esta sesión. Eh, simplemente te vas aquí donde sale configuración, te vas donde sale conectores y vas a ir a eh copiar esta parte que sale mp. Acá vas a bajar acá y te vas a ir a agregar conector personalizado. Vas a poner aquí el nombre que quieras, el URL del servidor MSP remoto, nombre, y listo, le das a agregar. Después reinicias Cloud Code y ya está agregado. Vamos a ver aquí qué está pasando, qué tipo de ads vas a generar principalmente con este sistema. Bueno, aquí ya puedes empezar a seguir y puedes seguir el onboarding, así ya eh para hacerlo aún un poco más fácil, ¿ya? Porque este proceso ahora simplemente sería como seguir un poco las cosas. Yo ya me reventé la cabeza haciendo miles y miles de generaciones y refiné en un mismo lugar una skill superútil que se las puedo dejar acá. De hecho, se las dejé publicada para la gente de Imperio Digital. Si es que entran aquí al Classroom, se van a la sección de Cloud Code, van a ver que ahora estaría publicado esto que sale Ads Cinemáticos. Aquí está toda la guía de todo lo que hicimos. Pero si es que se descargan este archivo, eh, aquí van a encontrar absolutamente todo. O sea, es una serie de archivos que los voy a descomprimir aquí para que se vea lo que estamos haciendo. Eh, que es como una capacitación de Cloud Code de cómo estaría generando este tipo de videos, ¿verdad? sería la instalación del skill, eh cómo lo vamos a estar instalando, eh cómo se conecta a Higfield MSP, cómo se conecta a Airta Table, a Eleven Labs, un caso de estudio y casos reales. Incluso también aquí tenemos la plantilla del concept s super útil s super buena. Eh, y esto lo hice al final para entregárselo a la gente de Imperio para ahorrarse el tiempo de tener que estar preparando y creando todo. Ya aquí hay muchas prácticas, muchas refinaciones que estuve haciendo, así que eh creo que le puede servir bastante a la gente que está aquí metida en Imperio. Bueno, vale decir que Imperio es un lugar donde estamos literalmente creando este tipo de cosas todo el día. Entonces, es una es una genialidad y nos gusta mucho al final usar Higfield y este tipo de herramientas para crear estas cosas. Entonces, estando acá, eh vamos a ver que lo que queremos hacer es crear los productos físicos, pero voy a proceder a arrastrarle el skill que eh tengo o que creamos de buenas prácticas. Entonces, simplemente voy a irme acá, voy a volver a Cloud Code, voy a darle a más, voy a agregarle un archivo y le voy a agregar el archivo de la skill de las buenas prácticas al momento de crear anuncios. ¿Ya? Eh, ¿qué tiene este skill? También en el caso de que no quieras importarlo y quieras crearlo por tu cuenta. Este skill tiene buenas prácticas como eh maneja y juega con los parámetros de la duración de los videos, ¿ya? Eh, por ejemplo, cuando empieza a crearlos, vas a ver que crea videos de 8 segundos, pero no queremos tantos videos de 8 segundos, quizás queremos videos de tres o videos de 10. Entonces ahí llega y los crea. Eh, entonces cuando empieza a crear toda la parte de la dirección creativa en todo ese sentido, es s super útil porque está dándole al final cuáles son buenas prácticas en el proceso de dirección creativa. Ya es un pequeño atajo para afinar el gusto en el caso de que no de que no quieras crear todo este sistema de tero. Pero aún así, si es que lo quieres crear desde cero, tienes que seguir estos pasos, decirle, esto es lo que quiero hacer, lo que le pusimos aquí arriba, ¿verdad? Y si te fijas, este archivo no es nada más que eso, es eh el Rey. Aquí lo vamos a abrir y va a hacer eh si ya conoces Cloud Code, eh créate una cuenta en Higpel, cacháis, tenéis estos archivos, eh necesitamos un director creativo. Después vamos a aprobarlo como usuario, en el caso de que quieras y eh te explica como qué son los distintos archivos. Ya esto al final todo lo todo mi proceso de iteración y todo mi mi ¿cómo se llama? Eh, todo mi proceso de razonamiento al final lo transcribí acá un poco para poder hacérselas más fácil, pero no es más que eso. Ya importado, listo. Skill ya está instalado. Deliverables están. Higfield tenemos los créditos. FMPG ya está listo y el onboarding ya está listo. Sigamos con el wizard. Lo único que necesitamos es la API key. Entonces vamos a ir acá. AP Keys. Nuevamente las vamos a crear. Vamos a crear una nueva piqu y va a ser cloud code versión 4 porque ya le he dado varias. Le voy a dar los permisos que quiera. Yo simplemente, en verdad, lo único que necesitamos es eh textech nada más. Pero supongamos que quiero hacer, no sé, sound effects, ¿verdad? La generación de música también la necesitamos en este caso y el resto de los agentes también, porque siento que al final no no es que se vaya a perder algo, los permisos de administración no son estrictamente necesarios. Entonces, eh si quieres no se los das, pero para este caso le voy a dar libertad completa, me da igual. Y voy a copiar esta API Key que acabamos de generar. Voy a volver aquí a Cloud Code. Voy a abrir nuestro archivo, voy a decirle esta es mi APQ y se lo voy a pegar. O alternativamente, si es que te gusta la confidencialidad, voy a abrir la ubicación del proyecto. Alternativamente, si es que no la tienes, eh, puedes decirle, "Ábreme la carpeta del ENV." El es el environment o el lugar donde eh archivamos nuestras claves secretas y le vas a decir, "Créame el M para desplegar de manera segura mis AP keys." Esto he visto mucha gente que no sigue esta práctica, pero al final creo que es super bueno siempre tenerlo en cuenta porque muchas veces también se filtran nuestras API kiss, eh, cuando, no sé, pues a veces pegamos con textos de conversaciones en otros clouds, ¿verdad? Es cosa mía. A mí yo soy super mañoso con eso, pero yo prefiero al final ser eh precavido en ese sentido. Si es que no te aparecen aquí los M, vas a abrirlo, vas a apretar comando, shift y punto. Y ahora sí, vas a ver que te va a aparecer. Vas a abrir el punto m y vas a llegar y vas a pegar tu llave. ¿Listo? La vas a pegar, le vas a dar a guardar. Y bueno, yo aquí te la estoy mostrando obviamente, pero lo que voy a hacer apenas termine este video es rotar esta llave por la zona lógica, ¿verdad? Eh, le vas a dar a guardar y le vas a dar a cerrar y le vas a decir, "Ya la puse. Continuemos con el onboarding." Eh, ¿qué son los pasos que siguen? Necesitamos conectar la cuenta de Higfield, ¿verdad? Para hacer las generaciones. Necesitamos conectar e nuestra cuenta de Airta Table. En el caso de que queramos algún lugar donde podamos ver las cosas que estamos creando. Este es un paso opcional, pero yo lo voy a hacer igual porque me gusta tener un lugar donde puedo ver las cosas. Eh, te va a pedir crear una token en el table. Simplemente le vas a abrir el table, estando acá, vas a crear una nueva token y le vas a decidir algo como cloud token. Vas a darle los scopes que necesites, no son muchos en este caso, data records read, data records, write, ¿okay? Vas a ponerle aquí literalmente los que necesites. Skima bases, read, skima, bases, write. Vamos a verlo acá. Skima, bases, read, skima, bases, write. Perfecto. Y no deberíamos necesitar nada más. Respecto a los workspaces que puede agregar aquí simplemente puedes elegir alguna de las bases o puedes darle acceso a todas. Yo le voy a dar los acceso a todas y vas a copiar el Airta Table Token y vas a volver previamente a tu cloud. Acá vamos a nuevamente decirle, "Ábreme la carpeta del o" o puedes hacer algo por el estilo de eh, ¿cómo se llama esto? Clic derecho, mostrar en Finder y abrir la carpeta. Si no te sale en Windows, tienes que asegurarte de que veas los archivos que están ocultos. Si no te salen Mac, tienes que asegurarte de ver los archivos que están ocultos en Mac, que se hace con control, no, command shift puntos. Así, sí. Eh, Air table pad, voy a llegar, voy a copiar mi token acá. Pum, enter. Ups, le puse un espacio. Ahora sí. Y guardar. Le voy a decir listo. Pegado. Procede. Ahora, eh, ¿qué es lo que vamos a hacer ahora? Vamos a conectarnos probablemente a Hixfield, que es el último paso que nos falta, ¿verdad? Eh, ya estamos conectados a Higfield vía MSP. Ya es s sencillo. Nuevamente hay que llegar, tenemos que poner acá Hixfield MSP, pum, listo. Eh, y agregamos el conector. Alternativamente también le puedes decir a Cloud Code, conéctate a Higfield MCP, ¿verdad? Y le pegas aquí el link. Eh, me dice, "¿Cuál de tus bases existentes quieres usar para este sistema?" Ninguna. Yo le voy a decir, crea una base nueva, porque al final estamos creando una base nueva. Yo ya he probado mucho con este sistema, por eso ya me reconoce distintas, pero le voy a decir que cree una base nueva. Ya. Entonces, aquí dos puntitos, conéctate a Higfield y le vamos a poner conéctate a Higfield de MSP. En el caso de que no nos hayamos conectado a Higfield previamente. Aquí me va a preguntar cuál es la voz que quiero como default. Le voy a poner cualquiera. Y listo, ya acabamos de completar el onboarding. Ahora sí voy a llegar literalmente voy a mostrarte los casos de uso. Voy a Aquí tengo la foto de la botella que la acabo de sacar. La voy a pegar, ¿verdad? Literalmente le voy a sacar hasta un pantallazo y la voy a pegar. Eh, y para que tenga referencia también de los tamaños, creo que le voy a pegar una que vendría siendo esta, ¿verdad? Entonces, ahí debería tener ya como un poco más de referencia de los distintos tamaños. 1, dos, 3. Acá esa foto está buena. Aquí tenemos otra, ¿verdad? Pero en fin, creo que eso debería ya bastar como para entender un poco como la idea de la botella. Ya. Entonces, acá voy a pedirte tres cosas para la dirección creativa, el monishot, ¿verdad? El concept board o un brief libre. ¿Ya? Entonces es como al final el money shot podríais generarlo en el caso de que quieras tú tener una fuerte dirección creativa. Esto yo lo recomiendo para la gente que sí le interesa tener control sobre esto. Eh, hay una plantilla super buena que también es la que te dejamos aquí adentro. Eh, donde la dejé. Voy a abrir el archivo para mostrarte simplemente que es esta plantilla que está acá. También te la dejo publicada. Puedes sacarlo un pantallazo, lo que quieras, pero es como para crear consistencia entre personajes. Entonces, yo voy a llegar acá, le voy a sacar un pantallazo, voy a abrir aquí directamente char GPT, o sabéis que mejor lo voy a hacer aquí en Hickfield, que es un poco más rápido. Eh, char GPT manch todo lo vamos a dejar en high. Vamos a dejarlo con el auto y le voy a pegar la imagen y le voy a decir, créame este concept board para, ¿verdad? Eh, ¿para qué cosa? Para la imagen que estamos creando. Entonces, le digo, "Créame este concept board para la botella. La idea es tener consistencia. generemos un personaje eh como con la cara levemente borrosa, pero el setting todo se mantiene. Unas personas escalando en Yosemite super alto colgadas en un multilargo. Escalada deportiva como no escalando, sino reposados en la pared, ¿ya? eh con la botella por ahí colgada quizás en su arnés o en la mano. Ya esta es la idea como que se me acaba de ocurrir. Eh, vamos a generarlo. Sabéis que lo voy a generar un poquito menos resolución e simplemente por el hecho de que quiero generarlo como rápido, rápido, ¿verdad? Para hacer como el testing. Esto es lo que me gusta también de generar las imágenes en Hickfield. Puedo generar como varias cosas de una. Ya. Entonces, aquí, por ejemplo, también voy a aprovechar de generar el money shot. Y esto lo hago simplemente porque quiero ver si es que como está entendiendo un poco la vibra que estoy intentando de como de rescatar. Ya. Entonces, aquí voy a seguir generando, generando, eh, y después cuando ya encuentre alguna vibra más o menos de lo que me gusta y de lo que quiero lograr, vamos a pasar a generarlo en en este caso en Cloud Code le va a pasar el concept. Esta parte es completamente opcional, pero a mí igual me gusta, me gusta porque creo que es el momento que tenemos como de empezar a meter un poco de criterio, ¿ya? Entonces, fíjate acá, ya creo que tenemos este concept board. Está bueno. Al final como que lo que quiero es como que esté escalando y se le caiga la botella y esté cayendo como exageradamente, no sé, me lo acabo de imaginar. esté cayendo como exageradamente y después se rescate, se rescate. Entonces, mira, ya colaboración entre Black Diamond y Nalgin. Eh, aquí mira, más concept board está sigue tomando las cosas. Aquí está super bien encajado en esto. Eh, sabéis que vamos por el otro, vamos por el otro, vamos por este de acá y le va a pegar este concept. Ya como que va a rechazar un poco esto y va a ser como vamos a pasar ahora a crear una narración. Vamos a exagerar lo dura que es la botella y lo resistente que es. Eh, vamos a generar varias o como las escenas, ¿verdad?, de una persona como en un multilargo escalando, eh, y después se cae la botella y se ve que cae cientos de metros, eh, muchísimos metros. se ve como s super, no sé, exagerado, digamos, todo lo que está cayendo de la botella, eh, toda la cantidad que cae y se ve como no tan cerca cuando se cae la botella, sino como desde muy lejos se ve como una pequeña distancia que se cae o se ve que se cae al vacío y después cuando los chicos terminan de escalar, eh, bajan, bajan, eh terminan su jornada de escalada y encuentran la botella prácticamente intacta. Y ahí tenemos que tener algún tagline como, no sé, pues que destaque como la resistencia como eh hecha para durar o no sé, no sé, algo algo que destaque como un poco como la resistencia y la calidad de la botella. Entonces aquí le acabo de dar un poco el prompting de lo que queremos hacer. Es super importante tener storyboard para armar bien el seteo. Ah, le voy a decir paréntesis se pronuncia nalgin y la marca de la botella, botella es nalgene. Ya, aquí está la botella. La tenemos acá. Es como lo primero que se me ocurrió. Entonces fue como que generemos esto con esto ya. Eh, preguntas o procedemos. lo voy a poner acá porque igual todo esto generalmente yo lo hago bastante más rápido, pero al final creo que igual es importante entender un poco el proceso y el razonamiento creativo que tengo detrás porque creo que entrando en el momento de que estamos entrando donde la IA es capaz de generar este tipo de cosas también es super importante tener un buen gusto y un buen criterio. A diferencia de no sé, no sé de del AI slop, ¿verdad? Hay gente que hace cosas muy lindas, hay gente que hace cosas muy malas con IA o que se ven muy feas. Es la única diferencia que tienen es el criterio nada más, nada más. O sea, como que necesitamos tener el criterio y la capacidad de hablar y comunicarnos de una manera eficiente con lo que queremos lograr, ¿cachá? Como con la visión final que tenemos, porque la otra parte técnica se está ejecutando directamente acá. Entonces, fíjate, están bastante buenos. Están bastante buenos. Creo que cumple un poco la función. Los concept board me gustaron. Me gustaron como que el personaje yo lo mantengo porque me gusta como mantenerle el como la consistencia de los characters, ¿verdad? Y aunque este igual podría haber estado bueno, podría haber sido algo así porque ahí se ven como ya también las dos personas, pero aquí está como medio raro porque hay dos botellas. Entonces este igual está bueno, pero también tiene como la parte como media atrás, no tiene cuerda, pero bueno, igual lo estoy desafiando y lo estoy llevando un poco más al límite, ¿no? No está entrenado tamban bien con cosas de escalada, pero vamos a ver y veamos cómo resulta esto. Para eso estamos, para ir jugando y crear estas cosas por nuestra cuenta. Vamos a esperar unos minutos y ya vuelvo para ver qué es lo que nos creó. Ah, espérate, antes de esto me dijo, "Popongo las escenas aquí también. Si hay algo que no te gusta, puedes llegar, puedes cambiarlo. Hero hook, botella clip alarnés, primer rayo climbers en multipeach, eh, botella se balancea. Eh, sí, pongamos ahí como se balancea la botella. Voy a ponerle Se balancea la botella, pero no porque se rompe, sino porque se cae. Eh, perfecto. Y después hecha para construcha para durar, construida para el vacío. El tagline que sea como build for the world. Me gusta ese. Sí. Está bueno. Eh, vamos siguiente. Aquí tenemos registro de la voz de Brian para el script. Reflexivo, pausado, épico trailer, sin voice over, solo esfx más música. Eh, puede ser como reflexivo, pausado. Sí, sí, reflexivo pasado. Sí, ya me gusta, me gustaría más sin efecto de sonido, pero creo que por fines de este video vale más la pena mostrar que cómo se integra también y crea los modelos y las imágenes de sonido. tipo de música para eleven laps. Eh, cinemática, tensión dramática, cinemática, streams, percusión, eh, climax de la caída, estilo Himer minimal, tensión dramática, tipo Norface, Patagonats, sí, un poco más por acá. Eh, número de escenas que estamos buscando, eh, ocho escenas, seis escenas, 10 escenas. Probemos con las ocho escenas, pues veamos qué tal cómo le funciona. Eh, vamos a dejarlo ahora. Ahora sí vamos a generarlo y ya están todas las conexiones hechas y veamos cómo quedó el final. Unos momentos después. Okay, después de unos segundos ya vemos que eh acaba de terminar, acaba de hacer esto. Aquí me pregunta alguna escena quedó rara. ¿Quieres que la regeneremos? No sé. Vamos a ver. Vamos a verlo. Primera vez que lo estoy viendo. Así que veamos qué tal. Algunos lugares [música] no perdonan errores aquí. Perdón, perdón, pero fíjate lo bien que queda colgando ahí como como Oh, está muy bueno. La verdad es que es super bueno. Sor voy de nuevo. Ahora sí que [risas] [música] algunos lugares no perdonan errores. [música] Aquí a 800 met del suelo, cada gramo cuenta. Cada [música] agarre, cada movimiento. Algunas cosas se sueltan. [música] Y caen, caen muy lejos. Pero no todo lo que [música] cae se rompe. Lo que está hecho para la pared resiste la pared. [música] Me encantó. Está buenísimo, buenísimo. Ya. Obviamente siempre hay un par de detalles que se pueden refinar, ¿verdad? Como que haya un poco más de pausa, pero fíjate todas las tomas. Ya esta quizás está como que podríamos cambiar, la verdad, pero a ver, ya partiendo la fiabilidad del producto. Mira, está exactamente igual. Nalgin made in USA. Ya, la colaboración con Black Timon, que me gustó que sea una idea de colaboración. Fíjate cómo pendule acá, ¿verdad? Cómo está escalando. Tenéis Black Diamond, que son la marca de los mosquetones. Aquí tenía esto, cómo está enganchado en el rack directamente. Después tenemos, bueno, ahí como que justo como que se cae. Se nota que se cae, pero ya está bien. Esa como que Pero mira esta, mira esta como va cayendo y como va golpeando con la roca, cacháis que era como un poco lo que queríamos lograr. y después ya están bajando y están volviéndose y se vuelve a encontrar la botella y al final tenéis como como este slogan. Ya si quisiera actualizarlo ahora, lo que voy a hacer es eh entrar acá y decirle como que esté más distanciada la voz. Entonces como que no se acabe al principio, sino más pausa entre frases. El resto está perfecto. Entonces ahí me empezaría a hacer estos cambios. Otra cosa, a mí me gusta trabajar con el table, entonces si es que me voy acá y me voy a table, me gusta trabajar ahí porque puedo visualizar un poco como las cosas que hemos estado haciendo. Y después vamos a tener los distintos proyectos. Entonces, acá, por ejemplo, en el caso de que tenemos el viejo este, tenemos la dirección creativa, el music prompt, telescript, todas las cosas y si nos vamos a la escena, tenemos cada una de las escenas. Podemos ver cada una de las escenas, suponiendo eh como no sé pues el proyecto en el que estamos y podemos decirle si es que hay alguna que nos gustó y que queremos cambiar. Yo trabajo en el table, por eso me gusta tenerlo acá, pero alternativamente también lo puedes encontrar acá. Si te vas justamente acá, eh, images, vas a ver que tenemos como la imagen inicial, las imágenes finales, ¿verdad? Tenemos los inputs, que son como las fotos que le pusimos, tenemos la música, que es la música que creó, ¿verdad? Con el 11 laps, tenemos los outputs, que es esta versión de acá, tenemos los videos y tenemos el eh la post. Y bueno, esto es algo que se me olvidó mencionar, pero cuando vamos al output, acá tenemos dos versiones, una versión que es un poco más corta y una versión que es un poco más larga. La versión corta era como la idea de que vaya como mezclando distintas escenas de distintos lugares y la versión larga al final es la versión un poco más extendida. Veamos si es que nos hizo caso acá, porque acaba de decirnos que acaba de terminar. Y veamos cómo quedó sincronizada la voz. Vamos a ver. [música] Algunos lugares no perdonan errores. [música] Aquí a 800 met del suelo, cada gano encuentro, cada agarre, [música] cada movimiento. Algunas cosas se sueltan [música] y caen, caen muy, pero no todo lo que cae se rompe. Lo que está hecho [música] para la pared resiste la pared. Bien, bien. Creo que al final que siempre se puede refinar un poco más, pero en fin, creo que creamos una estructura bastante buena, bastante sencilla. Eh, todo literalmente con un solo prompt que fue este prompt que leímos acá. Eh, vamos a crear esto, ¿verdad? Esta es la historia que quiero contar. Este es el elemento que quiero exagerar. Quiero que exagerar qué tan duro es al final una botella o el material de una botella que estamos creando. No existe un mejor momento para ir a crear que hoy día. O sea, hoy día con las herramientas que tenemos podemos crear cosas realmente geniales si es que le damos un poco más de pausa quizás a cada una de las imágenes, creamos una mejor dirección, eh nos tomamos el tiempo de refinar, entramos acá y refinamos cada una de estas imágenes. Por ejemplo, esta. Supongamos que no sé, pues yo me hubiese gustado quizás refinar esta. Creo que eh no quedó tan bien esa, ¿cachá? Pero todo el resto sí. Entonces, quizás eso lo hubiese refinado y nos damos el tiempo. Realmente podemos hacer direcciones creativas que están así ya a otro nivel. Aquí le voy a pedir ahora que nos descomponga el precio de cuánto nos costó todo esto en créditos, en API, etcétera. Y bueno, aquí tenemos el desglose de los costos, tenemos todas las escenas, eh cuánto las sacamos y los créditos que estuvieron acá. Si sumamos también eso al 11 Laps, eh, y hacemos una equivalencia entre los créditos que gastamos en Higsfield, terminandían siendo $24. Ya. Eh, algo muy importante para la gente que quiera y le interese ahorrar. Si te fijas acá gastamos, por ejemplo, en este segundo o 10 segundos de video, gastamos 90 créditos, lo que es bastante, pero si es que nos vamos acá y nos vamos al video, también todos estos parámetros los podemos jugar y podemos controlarlos. Entonces, si usamos otros modelos como Clink 3.0, va a ser harto más barato. Y, incluso, si es que usamos el Sidans 2.0 y jugamos con los 10 segundos, podemos jugar con otra calidad. por ejemplo, bajarlo solamente de 1080 a 720 nos baja el costo a la mitad. Fíjate, de 10 de 720 a 1080 nos baja el costo a la mitad. De 90 literalmente a 720 baja a la mitad. Por lo que si quisiéramos volver a crear esto, los créditos que gastaríamos acá, si lo creamos en 720 en vez de 1080, sería 225 y nos bajaría el precio a la mitad y habríamos creado este anuncio por $10. Y mira, sé que va a saltar un millón de personas y me van a decir, "Venga, es que es muy caro y todo, pero creo que la gente que realmente sabe aprovechar este tipo de oportunidades como que va a darse el tiempo de crearlo, de refinar su gusto y estoy seguro de que este tipo de anuncios puede cargar y puede convertir muy bien sea el objetivo que tengas y que quieras lograr, obviamente, ¿verdad? Ahí también tenemos que ver el marketing de cada persona, de cada empresa, si queremos generar awareness, si queremos generar eh conversión, si queremos generar, no sé, retargeting, por ejemplo. Todo eso va a depender de la estrategia que estemos siguiendo. Y si estamos siguiendo una estrategia y tenemos a los clientes en ciertas etapas de los embudos, tenemos que ver cuál es el creativo o el gráfico, la pieza de comunicación que hacemos para cada persona, ¿verdad? Entonces, si yo tengo un producto y quiero marketearlo para la gente que le gusta escalar, voy a crear este tipo de anuncios para la escalada, ¿verdad? Si tengo un producto y quiero lanzar una oferta para el día de la madre, quizás voy a lanzar una campaña de este estilo, pero para el día de la madre y nos vamos a demorar 5 minutos en hacerlo. Si quiero hacer lo mismo para Halloween, voy a hacer una campaña nuevamente para Halloween, porque la IA nos está permitiendo crear a velocidades nunca antes vistas y poder adaptarnos y personalizar para las masas, ¿verdad? Y personalizar rápido y poder hacer volumen. Eso de eso se trata al final. Entonces, nada, creo que vay a tener dos tipos de personas que van a ver este video, que va a ser la gente que me va a decir, "Benja, esto es muy caro. ¿Cómo voy a pagar $10 por un video así o $ por un video? Eh, si es que el video, no sé, pues, eh, se nota que es IA, no tengo idea." Y después vay a tener la gente que va a ser como, "Okay, esto es una pieza comunicacional, ¿cómo puedo tomarle la mayor ventaja posible a esto para cumplir mis objetivos y usar la IA como un medio, ¿verdad? No como una justificación. para no hacer algo. Tenemos esos dos tipos de personas al final. Si te gustó este video, espero que eh me dejes un buen like aquí abajo en este video porque me sirve mucho a mí todo el esfuerzo que le metí al final, eh te lo agradecería un montón, no solamente porque me ayudas a mí, sino que también ayudas a tu algoritmo a que te aparezcan videos de valor como dicho y hecho eso, espero que este video te haya servido y ya nos vemos. Te recomiendo estos dos videos que te van a salir por [música] acá. [música]
