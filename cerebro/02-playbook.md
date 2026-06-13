# 02 — Playbook técnico (los "cómo" exactos)

Procedimientos concretos y verificados. Higgsfield es un conector MCP.

## A. Subir un archivo a Higgsfield (flujo del agente)
El widget solo acepta medios y sube de a uno; para subir bytes desde un entorno de
código se usa el flujo de 3 pasos:
1. `media_upload` con el `filename` → devuelve `upload_url` + `media_id`.
2. PUT de los bytes al `upload_url` con curl:
   `curl -X PUT -H "Content-Type: <mime>" --data-binary @archivo "<upload_url>"`
   (esperar HTTP 200).
3. `media_confirm` con el `media_id` y el `type` (`image` / `video` / `audio`).

## B. Entrenar un Soul
- `show_characters action=train`, `type=soul_2`, `name=<nombre>`.
- Pasar las imágenes como **URLs https** (CloudFront `d2ol7oe51mr4n9.cloudfront.net/...`),
  NO los UUID en bruto → el validador devuelve error con UUID.
- Obtener las URLs con `show_medias type=image` tras confirmarlas.
- 15–20 imágenes. Tarda ~10 min. Consultar con `show_characters action=status soul_id=<id>`.

## C. Extraer fotogramas de vídeos (para entrenar el Soul)
- Descargar el vídeo (desde el CDN de Higgsfield o Drive).
- Muestreo: `ffmpeg -ss <t> -i video.mp4 -frames:v 1 -q:v 2 frame.jpg` (fotograma puntual)
  o `ffmpeg -i video.mp4 -vf fps=2 -q:v 2 f_%03d.jpg` (2 por segundo).
- Revisar visualmente y quedarse con caras nítidas, frontales/perfil, variadas.
- Recortar planos generales a cabeza-hombros:
  `ffmpeg -i frame.jpg -vf "crop=720:720:<x>:<y>" out.jpg`.

## D. Convertir audio de WhatsApp (.mp4) a mp3
`ffmpeg -i voice.mp4 -vn -acodec libmp3lame -q:a 2 voice.mp3`
Recortar 12 s: `ffmpeg -i voice.mp3 -t 12 -acodec libmp3lame -q:a 2 voice_12s.mp3`

## E. Generar imagen con el Soul
`generate_image` → `model: soul_2`, `soul_id: <id>`, `aspect_ratio`, `prompt`.
Mostrar/recuperar resultado: `job_display id=<job_id>`. La `minUrl` (webp) se puede
descalar a jpg con ffmpeg para inspeccionar.

## F. Generar el vídeo hablado
`generate_video`:
```
model: seedance_2_0      # alternativa: veo3_1 (ultra), kling3_0, wan2_7
medias:
  - { role: start_image, value: <media_id del retrato> }
  - { role: audio,       value: <media_id del clip de voz 12s> }
aspect_ratio: 9:16
duration: 12
resolution: 720p
prompt: lipsync natural, ver texto en 03-activos.md
```
Modelos de vídeo con audio/lipsync disponibles: seedance_2_0, wan2_7 (audio role),
kling3_0/kling2_6 (sound), veo3/veo3_1 (audio), grok_video.

## G. Google Drive (origen de material)
- El conector falla al **descargar archivos > ~10 MB** ("session expired"). Para
  vídeos grandes, que el usuario los suba por el **widget de Higgsfield** (uno a uno).
- Descarga de archivos pequeños: `download_file_content` → base64 → decodificar.
- No sirve la descarga por URL pública si el archivo no es público (pide login).

## H. Diagnóstico de "requires approval"
- Operaciones de **escritura** MCP (generate_video, crear páginas Notion) fallan en
  entornos automáticos con `MCP tool call requires approval`.
- NO es el archivo de permisos de Claude (revisado: el tool puede estar en `allow` y
  aun así fallar). Es la imposibilidad de aceptar el diálogo de aprobación aquí.
- Solución: ejecutar esa acción en una **sesión interactiva** (app/escritorio/web).
