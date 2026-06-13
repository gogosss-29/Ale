# Método de acceso y extracción — comunidad de Skool «imperio»

> **Qué es esto:** registro técnico, honesto y reproducible de **cómo se accedió y
> extrajo** el contenido del curso de la comunidad de pago *Imperio Digital* (Skool),
> para tu transparencia y para poder repetirlo. Es el equivalente al post-mortem que
> ya tenías del curso de Whop (`METODOACCESOCURSO.md`), pero esta vez **el método sí
> quedó guardado como código** en `skool/`.

## ⚠️ Avisos antes de nada
- **Seguridad:** el acceso usó tu **cookie de sesión de Skool** (con el `auth_token`
  JWT vivo de tu cuenta). Cuando termines, **cierra sesión en Skool y vuelve a entrar**
  para invalidarla. La cookie nunca se guardó en el repo (vivió en `/tmp`, fuera del
  árbol de git).
- **Términos de uso:** archivar el contenido de un curso de pago —aunque seas miembro
  y sea para uso personal— probablemente **infringe los términos de Skool y del
  creador**. Compartir o redistribuir el material sería una infracción clara. Úsalo
  bajo tu criterio y responsabilidad. Esto **no elude ningún pago ni paywall**: reusa
  tu acceso legítimo de miembro, pero por API en vez de por la web.

## Requisito imprescindible
Tu **cookie de sesión de Skool**, que autentica las peticiones **como tú** (miembro que
pagó). La pieza esencial es la cookie `auth_token` (un JWT). Sin ella nada funciona.

Cómo obtenerla: navegador logueado → DevTools (F12) → Network → recargar → clic en la
petición a `www.skool.com` → Request Headers → copiar el valor completo de `cookie:`.

## Cómo está construido Skool (lo que descubrimos en vivo)
Skool es una app **Next.js**. El truco central: **todo el contenido del classroom
viaja en el JSON del servidor**, no hay que "ver" la web ni reproducir vídeos.

1. **Autenticación.** Se carga la cookie en la cabecera `Cookie` de cada petición
   (`skool/session.py`). Con eso las páginas y los endpoints internos responden como
   si fueras tú.

2. **`buildId` de Next.js.** Se lee del HTML de la home de la comunidad
   (`"buildId":"..."`). Es la clave para llamar a los endpoints de datos.

3. **Lista de cursos.** En `GET /imperio/classroom`, dentro de `__NEXT_DATA__`, el
   campo `pageProps.allCourses` trae los **30 cursos** (id, título, nº de módulos…).

4. **Árbol de cada curso.** El endpoint de datos de Next
   `GET /_next/data/<buildId>/imperio/classroom/<courseId>.json` responde con un
   **redirect** a `/imperio/classroom/<short>?md=<primeraLección>`. De ahí se saca el
   `short` (id corto del curso) y la primera lección.

5. **Contenido de las lecciones.**
   `GET /_next/data/<buildId>/imperio/classroom/<short>.json?md=<lessonId>` devuelve el
   **árbol completo del curso** (módulos→lecciones anidados en `course.children[].course`)
   y, **solo para la lección `md` seleccionada**, su `metadata.desc` y `resources`
   poblados. Por eso se hace 1 petición por lección. Cada nodo lección trae:
   - `title`
   - `desc` → notas en **Prosemirror JSON** (prefijo `[v2]`), se parsean a Markdown
     (`skool/prosemirror.py`), conservando negritas, listas, citas y **enlaces**.
   - `videoLink` → URL del vídeo (en imperio: **YouTube** y **Loom**).
   - `videoLenMs`, `videoThumbnail`, `resources`, `hasAccess`.

6. **Transcripciones de los vídeos (sin descargar el vídeo).** Con `yt-dlp` se bajan
   **solo las pistas de subtítulos** (`--skip-download --write-subs --write-auto-subs`),
   en español preferente. Se limpia el `.vtt` a texto plano (`skool/transcripts.py`) y
   se anexa a cada lección bajo "🎙️ Transcripción". *(Igual que en Whop con los `.vtt`
   de Mux: subtítulos oficiales en vez de transcribir audio con Whisper.)*
   - Nota de entorno: la red usa un **CA propio (proxy)**, así que yt-dlp necesita
     `--no-check-certificates`.
   - **Loom (≈145 vídeos):** ✅ se transcriben sin problema desde el servidor.
   - **YouTube (≈261 vídeos):** ❌ **no** desde este servidor — YouTube responde
     `HTTP 429 / "Sign in to confirm you're not a bot"` porque bloquea las IPs de
     datacenter (no es un problema de login; ni con cookies se evita). Probé `yt-dlp`
     y `youtube-transcript-api`: ambos dan `IpBlocked`.
   - **Solución para YouTube:** correr el mismo script **en tu máquina** (IP
     residencial, no bloqueada). Es resumible: salta lo ya transcrito (los Loom) y
     solo baja los YouTube:
     ```bash
     # en tu ordenador, con el repo clonado y yt-dlp instalado:
     python -m skool.transcripts imperio --out docs-skool --hosts youtube,youtu.be
     # si aún te pide "confirm you're not a bot", añade tus cookies del navegador:
     python -m skool.transcripts imperio --out docs-skool --hosts youtube,youtu.be \
         --cookies-from-browser chrome
     ```

## Resumen en una frase
**Scraping autenticado vía los endpoints `_next/data` de Skool:** con tu sesión, se
pide a Skool el árbol del classroom y el contenido de cada lección (notas Prosemirror +
links de vídeo), y a YouTube/Loom solo los subtítulos — en lugar de hacer clic por la web.

## Piezas clave (referencia)
| Pieza | Para qué |
|---|---|
| `GET /imperio/classroom` → `pageProps.allCourses` | Lista de los 30 cursos |
| `_next/data/<build>/imperio/classroom/<courseId>.json` | Redirect → `short` + primera lección |
| `_next/data/<build>/imperio/classroom/<short>.json?md=<id>` | Árbol del curso + `desc`/recursos de esa lección |
| `desc` (Prosemirror `[v2]` JSON) | Notas escritas → Markdown |
| `yt-dlp --skip-download --write-subs` (YouTube/Loom) | Transcripciones `.vtt` |

## Reproducir
```bash
export SKOOL_COOKIE_FILE=/ruta/cookie.txt   # o export SKOOL_COOKIE='auth_token=...; ...'
python -m skool.extract     imperio --out docs-skool   # Fase 1: estructura + notas + links
python -m skool.transcripts imperio --out docs-skool   # Fase 2: transcripciones de vídeo
```

## Cifras de la extracción
- **30 cursos**, **826 lecciones**, **~245 horas** de vídeo.
- Vídeos: ~261 en YouTube, ~145 en Loom; el resto de lecciones son de solo texto
  (p. ej. «Biblioteca de Prompts», 178 lecciones).
