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
