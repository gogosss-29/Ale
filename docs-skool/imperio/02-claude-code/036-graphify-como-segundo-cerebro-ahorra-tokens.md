# Graphify como segundo cerebro. Ahorra tokens.

> Ruta: Claude Code › Graphify como segundo cerebro. Ahorra tokens.

**🎬 Vídeo (40.9 min):** https://www.youtube.com/watch?v=v9PreCpgVkU

---

## **LO QUE VAS A ENCONTRAR EN ESTE POST**

1. Qué es Graphify en 30 segundos
2. Instalación (la vía fácil y la manual)
3. Los 2 únicos comandos que tienes que saber
4. Los modos de extracción (elige bien y ahorra)
5. El truco para creadores: mete tus comentarios al grafo
6. El número HONESTO de tokens (y por qué el "70x" es mentira)
7. ¿Cuánto cuesta mantenerlo actualizado?
8. Graphify + Obsidian: cómo se complementan
9. El Motor Agéntico (descarga)
10. Mini-FAQ
11. Recursos

---

## **1. QUÉ ES GRAPHIFY EN 30 SEGUNDOS**

Claude Code (o Codex, o el arnés que uses), por debajo, busca información en tu proyecto haciendo **grep** — abre archivos, lee, descarta, abre otro. Es Ctrl+F a ciegas. Funciona, pero quema tokens y a veces se pierde.

Graphify le construye un **mapa** antes: un grafo con nodos (tus archivos, conceptos, ideas), conexiones (qué se relaciona con qué) y comunidades (grandes temas, agrupados con el algoritmo de Leiden). En vez de leer todo de cero, el agente mira el mapa y va directo.

Lo hace en **3 fases**:

- **Fase 1 — código (gratis, sin IA)**: tree-sitter parsea tus archivos local. Clases, funciones, imports, llamadas. 25 lenguajes, SQL con tratamiento especial. Cero tokens.
- **Fase 2 — audio/video (gratis, sin API)**: faster-whisper transcribe local tus audios y videos. Las transcripciones quedan en caché.
- **Fase 3 — documentos/imágenes (la única que cuesta tokens)**: subagentes de Claude leen PDFs, imágenes y docs en paralelo y hacen el análisis semántico — qué significa esto y dónde encaja en el mapa.

Inspirado en el LLM Wiki de Andrej Karpathy. No es un RAG (no hay embeddings ni base vectorial): es el punto medio entre Obsidian (puro markdown) y un RAG (puro vector).

---

## **2. INSTALACIÓN**

**La vía fácil (la del video):** copia el link del repo → pégalo en Claude Code → dile *"investígame esto y después instálalo con las mejores prácticas"*. Lo hace solo, detecta tu arnés y listo.

Repo: [https://github.com/safishamsi/graphify](https://github.com/safishamsi/graphify)

**La vía manual:**

```
uv tool install graphify
```

graphify install

Esto registra la **skill** en tu proyecto (carpeta `.claude/` + `CLAUDE.md`): tu agente aprende solo cuándo y cómo usar Graphify según lo que le pidas en lenguaje natural.

**Es agnóstico de plataforma**: Claude Code, Codex, OpenCode, Kilo Code, Cursor, Gemini, GitHub Copilot, VS Code, Hermes, OpenClaw — hay flag para cada uno (`graphify install --platform codex`, etc.).

**Extras opcionales** (te los pregunta al instalar — di que sí a lo que uses): faster-whisper (audio/video), yt-dlp (videos de YouTube), PDFs/Office, Postgres, SVG export, Neo4j, MCP server, Bedrock...

---

## **3. LOS 2 ÚNICOS COMANDOS QUE TIENES QUE SABER**

Hay decenas de comandos, pero NO te los aprendas — la skill se los enseña a tu agente. Tú solo necesitas dos:

**ComandoQué hace**`/graphify .`Construye el grafo de la carpeta actual (el `.` = "todo esto"). Tarda 5-30 min según el tamaño.`graphify update`Re-extrae SOLO los archivos que cambiaron (incremental, tipo changelog — no reindexar todo).

Bonus para preguntar: `graphify query "tu pregunta"` responde usando el grafo, sin releer archivos. También existen `explain`, `path` (el camino entre dos cosas) y `graphify obsidian` (sección 8).

---

## **4. LOS MODOS DE EXTRACCIÓN (elige bien y ahorra)**

Al correr `/graphify .` te pregunta qué tan profundo ir:

- **Solo código** → lo más rápido y barato. Para explorar repos.
- **Código + documentación** → para material de texto (apuntes, transcripciones, PDFs). *El que usé yo.*
- **Extracción completa (con imágenes/audio)** → la más cara (puede irse a cientos de miles de tokens). Solo si lo multimodal te aporta.

Regla simple: incluye únicamente lo que de verdad vas a consultar. Yo le dije "los videos de YouTube sí, el resto no" y procesó 4 millones de palabras sin quemar de más.

---

## **5. EL TRUCO PARA CREADORES: TUS COMENTARIOS AL GRAFO**

No metas solo tus transcripciones. **Baja también los comentarios de tus videos** y ponlos en la misma carpeta antes de correr Graphify. Así el grafo no solo sabe lo que TÚ dices — sabe lo que tu AUDIENCIA pregunta.

Después:

```
graphify query "según los comentarios de mis videos, ¿cuáles son las dudas que mi audiencia repite más?"
```

Esa lista es, literal, tus próximos videos. Tu audiencia ya te dijo qué quiere; el grafo solo te lo ordena.

> Tip: para bajar los comentarios usa la API de YouTube, yt-dlp, o pídeselo a un agente. Lo importante es que queden como texto plano en la carpeta.

---

## **6. EL NÚMERO HONESTO DE TOKENS (el "70x" es mentira)**

Vas a ver por todos lados que Graphify ahorra "70 veces" los tokens. **Está inflado.** Lo medí sobre mi propio vault (294 archivos, 4M de palabras), misma pregunta, dos formas:

**EscenarioTokensSin Graphify** (Claude leyó los ~35 archivos relevantes completos)~67.000**Con Graphify** (Claude leyó solo el mapa)~16.000**Resultado4,2x menos · 76% de ahorro**

¿Por qué no 70x? Porque ese número asume que leerías TODO tu contenido en cada pregunta. Ni el techo teórico de mi vault llega ahí: leer absolutamente todo (caso imposible) serían ~52x. En una pregunta real, son ~4x.

**Lo honesto completo:**

- Preguntas **amplias** (síntesis sobre mucho material) → ahorro grande, como el 76% de arriba.
- Preguntas **muy puntuales** → ahorro chico, a veces hasta cuesta un poco más.
- Lo mejor es el **acumulado**: el mapa se construye una vez y cada pregunta siguiente sale barata.

Y la matemática Fable 5: si cuesta 2x que Opus pero gasta 4x menos → **≈ mitad de costo que Opus pelado**. "Teóricamente", porque depende del tipo de pregunta — pero la dirección es esa.

---

## **7. ¿CUÁNTO CUESTA MANTENERLO ACTUALIZADO?**

La crítica #1 que vas a leer: "el grafo se queda obsoleto apenas cambias archivos". Verdadero a medias:

- `graphify update` es **incremental**: solo procesa la diferencia (tu video nuevo, tu archivo nuevo), no la base entera. Para mí: un update por video subido, costo mínimo.
- Si tu material es **estático** (apuntes, PDFs, transcripciones): lo construyes una vez y listo. La objeción casi no aplica.
- Si tienes un **equipo grande con un repo que cambia 10 veces al día**: el mantenimiento sí tiene costo. Existe el **Team Setup** (una persona corre graphify, commitea `graphify-out/`, el resto lo lee) — pero evalúa si te conviene.

---

## **8. GRAPHIFY + OBSIDIAN: NO COMPITEN, SE COMPLEMENTAN**

Si viste mi video de Obsidian + Claude Code, armamos el wiki de Karpathy puro: markdown interconectado, mantenido a mano por el agente.

Graphify es el primo automático: extrae el grafo solo. Y con un comando — `graphify obsidian` — **te genera un vault de Obsidian** a partir de tu contenido.

- **Obsidian** = el wiki legible que tú mantienes.
- **Graphify** = el motor que lo extrae y mapea por ti.

Y del mismo grafo también puedes sacar: SVG, export a Neo4j, o levantar un **servidor MCP** para que cualquier modelo lo consulte desde cualquier lado.

---

## **9. EL MOTOR AGÉNTICO (descarga)**

En el video lo usé para trackear cuánto gasté en Fable 5 (~$900 en equivalencia API, hoy cubierto por la suscripción... hasta el 22 de junio).

El **Motor Agéntico** es la capa visual sobre tu stack de IA: gastos y equivalencia suscripción↔API, sesiones por día, tareas agendadas, sistema de memoria, skill de "soñar" (mejoras automáticas), y se conecta con Claude Code, Codex, Hermes y OpenClaw.

⚙️ **Descárgalo acá**: [LINK_POST_MOTOR_AGENTICO]

Y si quieres el video desglosando cómo lo armamos por dentro: comenta **"motor agéntico"** en el video de YouTube — estoy midiendo el interés ahí.

---

## **10. MINI-FAQ**

**"¿No es lo mismo que grep / el AST del IDE?"** Para código puro, en parte sí. La diferencia: Graphify es multimodal (transcripciones, PDFs, audios, imágenes) y te da relaciones explícitas. El grep encuentra texto; el grafo lo conecta.

**"¿No es solo otro RAG?"** No usa embeddings ni base vectorial. Fases 1 y 2 son 100% locales y deterministas. Es el punto medio: más estructura que Obsidian, menos infraestructura que un RAG. Para millones de docs sin estructura, un RAG sigue ganando; para tu carpeta o proyecto, esto es más simple y suficiente.

**"¿Esto es exactamente lo de Karpathy?"** Es un primo, no el gemelo: lo de Karpathy era markdown con punteros; Graphify le mete un grafo encima (nodos, aristas, comunidades). El espíritu es el mismo: sacar la memoria fuera del modelo.

**"¿Por qué no uso solo Obsidian?"** Sección 8 — se complementan, y Graphify exporta a Obsidian.

**"¿Se queda obsoleto?"** Sección 7 — update incremental; para material estático casi no aplica.

---

## **11. RECURSOS**

- 🎬 El video completo: [https://www.youtube.com/watch?v=v9PreCpgVkU](https://www.youtube.com/watch?v=v9PreCpgVkU)
- ⚙️ Graphify (repo, gratis): [https://github.com/safishamsi/graphify](https://github.com/safishamsi/graphify)
- 🧠 LLM Wiki de Karpathy: [https://x.com/karpathy/status/2039805659525644595](https://x.com/karpathy/status/2039805659525644595)
- 📺 Mi video de Obsidian + Claude Code: [https://www.skool.com/imperio/classroom/3204e11c?md=2a9ac5134a9a48bc9e10910379fbe329](https://www.skool.com/imperio/classroom/3204e11c?md=2a9ac5134a9a48bc9e10910379fbe329)
- 🚀 Motor Agéntico (descarga): [https://www.skool.com/imperio/classroom/3204e11c?md=dbdde7a862c444aead1a7a56c7530589](https://www.skool.com/imperio/classroom/3204e11c?md=dbdde7a862c444aead1a7a56c7530589)
