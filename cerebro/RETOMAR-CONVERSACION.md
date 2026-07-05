# Prompt maestro para retomar (pegar en un chat nuevo)

> Copia TODO el bloque de abajo y pégalo en el chat nuevo.
> _Última actualización: refleja el sistema de edición Remotion ya construido._

---

Hola, retomamos un proyecto en curso. Lee este contexto entero antes de actuar. Estás en el
repo `gogosss-29/Ale`; **la rama con lo más reciente es `claude/funny-shannon-u9f2u9`**
(ver "Ramas" abajo). Abrí también `CLAUDE.md`, `cerebro/` (sobre todo `PENDIENTES.md`) y
`remotion/scripts/README-sistema.md`. Respondeme en español (rioplatense).

## Qué es el proyecto
Crear y operar el contenido de la marca **Cerebro** (avatar digital de Alexander): un sistema
que **escribe guiones, genera y EDITA reels** con su identidad (cara + voz). Dos capacidades:
1. **Identidad** entrenada en Higgsfield (Soul + voz clonada) → imágenes y video hablado.
2. **Máquina de contenido**: guiones en su voz → producción por 3 rutas → edición automatizada.

## Dónde está todo (fuente de verdad = el repo)
- `cerebro/` — el brain: `00-vision`, `02-playbook`, `03-activos` (IDs), `04-estado`,
  **`PENDIENTES.md` (backlog vivo, EMPEZÁ POR ACÁ)**, `maquina-contenido/` (guiones/ejemplos/escenarios).
- `.claude/skills/` — capacidades operativas:
  - `cerebro-guiones` — escribir guiones + prompts de avatar/b-rolls (+ `references/motor-produccion.md` = el router de herramientas).
  - `crear-estilo-broll` — estilos nuevos de b-roll desde una referencia.
  - `omni-reels` — editar con Omni (motion graphics sobre footage real) + `scripts/reel_cutter.py`.
  - `avatarhype` — metodología del curso (ruta APImart/Veo).
- `remotion/` — **el sistema de edición de video (lo más valioso, ver abajo)**.
- `docs/` (curso AvatarHype, vía Whop) y `docs-skool/` (curso Imperio, vía Skool) — archivo de
  estudio; NO es el core del avatar.

## ⚙️ Sistema de edición Remotion (CONSTRUIDO — "la máquina entrega .mp4, no prompts")
Motor genérico data-driven: `video crudo + receta.json → video editado .mp4`.
- `remotion/src/EditedVideo.tsx` — composición genérica (lee un `EditMap`).
- `remotion/src/overlays.tsx` — biblioteca de overlays (numberCallout, chip, topLabel, barsLabel,
  arrowChips, bigBadge, risingLine).
- `remotion/scripts/editar.mjs` — CLI end-to-end: transcribe → captions → **resuelve los efectos
  por la FRASE que se dice** → segmenta ventanas "detrás" (recorte de persona) → render.
- `remotion/scripts/py/{transcribe,segment}.py`, `remotion/recetas/crudos.json`, `README-sistema.md`.
- Uso: `cd remotion && node scripts/editar.mjs <video.mp4> <receta.json>`.
- Efecto "detrás de la persona" = segmentación con rembg (`u2net_human_seg`) por ventana.
- Además hay composiciones de reels del avatar: `ReelAssembly` (reel completo), estilos de b-roll
  #11/#12/#13/#99, `CaptionedClip` (captions).

## Activos vivos en Higgsfield (cuenta de Alexander, válidos entre sesiones)
- Soul "Alexander v2" (USAR): `9ffc9c16-eeb2-465d-b2b5-03a7b14a227d`
- Retrato base v2: `43c9b6e8-e08c-47af-b8b7-94b61bae1b2e`
- Voz clip 12 s: `41bd653e-a16f-4089-baea-60cbcfba1d18` · Voz completa 3:27: `efc51158-010b-4a2f-ae28-a9b1d4026f90`
- Imagen: `generate_image` model `soul_2` + `soul_id`. Video: `generate_video` seedance_2_0.

## ⚠️ Setup del entorno (NO persiste — reinstalar en cada sesión nueva)
El código está en git, pero las dependencias del sistema y los pesados NO. Para correr el sistema
de edición:
1. `apt-get update && apt-get install -y --no-install-recommends ffmpeg`
2. `pip install faster-whisper` (transcripción) y, si hay efectos "detrás", `pip install "rembg[cpu]"`.
3. Modelo de segmentación: **GitHub está bloqueado por el proxy (403)**; bajar de Hugging Face:
   `curl -L https://huggingface.co/tomjackson2023/rembg/resolve/main/u2net_human_seg.onnx -o ~/.u2net/u2net_human_seg.onnx`
4. `cd remotion && npm install`. Render usa el Chromium del contenedor:
   `--browser-executable=/opt/pw-browsers/chromium --chrome-mode=chrome-for-testing`.
5. **Fix de fuentes:** las fuentes se cargan con `injectFont` (no `loadFont`) porque `loadFont`
   colgaba el render en este Chromium — no revertir.

## ⚠️ Material pesado que NO está en git (pedírselo a Alexander)
Los `.mp4` (clips del avatar, videos crudos), los renders y los recortes de segmentación están
en `.gitignore`. Si hay que re-editar, pedirle a Alexander que **suba de nuevo el/los videos**
(arrastrándolos al chat: aterrizan en `/root/.claude/uploads/...`; para >100 MB, link de Drive y
bajar con `curl`).

## Ramas (IMPORTANTE)
- **`claude/funny-shannon-u9f2u9`** = lo más nuevo (sistema de edición Remotion, skill omni-reels,
  CrudosEnhanced, este análisis). **Trabajar acá.**
- `claude/funny-shannon-2c94fg` = tiene el archivo de cursos (docs-skool) + Remotion viejo; su PR #1
  (`→ upbeat-lamport-ec6bjh`) sigue **sin mergear**. Pendiente: **consolidar** ambas ramas.

## Estado (resumen — detalle en cerebro/PENDIENTES.md)
- ✅ Identidad (Soul v2 + voz), guiones, sistema de edición Remotion, skill omni-reels.
- 🟡 Pendiente de veredicto de Alexander: elegir versión del reel-003 (v1/v2) + música; generar
  C3–C7 de Omni; ok del crudo editado.
- 🟠 Cuello de botella real: **mucho construido, nada publicado.** Falta CERRAR y subir un reel.

## Bloqueos y lecciones clave
1. **Dos metodologías sin reconciliar:** ruta Cerebro (Higgsfield + Remotion) vs ruta del curso
   (APImart/Veo/Omni Flash). Falta decidir el estándar.
2. **Omni al editar:** puede regenerar voz/personaje si el prompt no es benigno + por tiempo
   (ver skill `omni-reels`). Nunca "when I say", nunca hex en el prompt.
3. **Seguridad:** en sesiones previas se pegaron cookies con tokens vivos (Whop/Skool). No volver
   a pegar credenciales en chat; invalidar sesiones tras usarlas.

## Cómo continuar
Preguntame el rumbo; no asumas. Opciones abiertas: (a) **cerrar y publicar un reel** end-to-end
(lo más importante), (b) consolidar las ramas, (c) integrar el CLI `editar.mjs` a la skill de
guiones, (d) sumar música/overlays al sistema. Confirmá antes de acciones que consuman créditos
o escriban en sitios externos.
