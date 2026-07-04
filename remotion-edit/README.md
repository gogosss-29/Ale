# Edición del vídeo de Alexander con Remotion

Proyecto [Remotion](https://www.remotion.dev/) para editar el vídeo talking-head
vertical (9:16) de Alexander y convertirlo en un Reel/Short con:

- **Subtítulos animados** estilo TikTok/Reels, sincronizados palabra por palabra
  (resaltado en verde de la palabra que se está diciendo).
- **Hook / título inicial** animado en los primeros 3 s (`JUNTÓ 45 MILLONES`).
- **Música de fondo** ambiental suave y libre de derechos (pad de acordes).
- **Barra de progreso** superior, viñeta sutil, zoom lento (Ken Burns) y handle de marca.

Vídeo fuente: `Crudos copilado.mp4` (1080×1920, 30 fps, 63.7 s, H.264 + AAC).
Tema: el fondo común de inversión de Beltrán Briones que juntó 45 M USD.

## Estructura

```
src/
  Root.tsx              # Registro de la composición VideoEdit
  VideoEdit.tsx         # Escena principal (vídeo + capas)
  config.ts             # Parámetros: fps, tamaño, duración, textos
  components/
    Captions.tsx        # Subtítulos animados (word highlight)
    Hook.tsx            # Gancho / título inicial animado
    ProgressBar.tsx     # Barra de progreso superior
  data/
    captions.json       # Salida cruda de Whisper (tokens)
    words.json          # Captions fusionadas a nivel palabra (las que usa el vídeo)
scripts/
  transcribe.mjs        # Transcribe la voz con whisper.cpp (modelo medium, es)
  clean_captions.mjs    # Fusiona sub-tokens en palabras -> words.json
  make_music.sh         # Sintetiza la música de fondo (ffmpeg)
public/
  source.mp4            # Vídeo fuente (NO versionado; ver abajo)
  music.mp3             # Música de fondo generada
```

## Requisitos

- Node 18+ y `ffmpeg` en el PATH.
- `npm install`

## Preparar los activos

El vídeo fuente no se versiona (107 MB). Descárgalo desde Drive a `public/source.mp4`:

```bash
# El archivo original está en el Drive de Alexander (Crudos copilado.mp4)
# Colócalo en public/source.mp4
```

Regenerar transcripción y música (opcional, ya vienen incluidas `words.json` y `music.mp3`):

```bash
# 1) Audio para whisper
ffmpeg -i public/source.mp4 -ar 16000 -ac 1 -c:a pcm_s16le audio/voice16k.wav
# 2) Transcribir (descarga whisper.cpp + modelo medium)
node scripts/transcribe.mjs
# 3) Limpiar a nivel palabra
node scripts/clean_captions.mjs
# 4) Música de fondo
bash scripts/make_music.sh
```

## Editar en vivo

```bash
npm run dev      # abre Remotion Studio para ajustar textos, tiempos y estilos
```

## Renderizar

```bash
npx remotion render src/index.ts VideoEdit out/ale_editado.mp4 --codec=h264 --crf=18
```

## Personalizar

- Textos del hook y handle: `src/config.ts`.
- Estilo/colores de subtítulos (color de resaltado `#7CF86B`, tamaño, posición): `src/components/Captions.tsx`.
- Volumen de la música: `defaultProps.musicVolume` en `src/Root.tsx` (por defecto 0.12).
