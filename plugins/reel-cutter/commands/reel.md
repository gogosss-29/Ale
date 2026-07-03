---
description: Cortar un video en clips en silencios, sin partir palabras (reel-cutter)
argument-hint: [ruta_al_video] [--max N] [--min N] [flags extra]
---

Corta el video indicado usando la herramienta reel_cutter del plugin.

Argumentos del usuario: $ARGUMENTS

Pasos:
1. Verifica que existan `ffmpeg`/`ffprobe` y el módulo `faster_whisper`
   (si faltan, instálalos: `apt-get install -y ffmpeg`, `pip3 install faster-whisper`).
2. Ejecuta:
   `python3 "${CLAUDE_PLUGIN_ROOT}/skills/reel-cutter/scripts/reel_cutter.py" $ARGUMENTS`
   (si el usuario no pasó flags, usa `--max 10 --min 4`; en CPU sugiere `--modelo medium`).
3. Al terminar, muestra la tabla de `salida/mapeo_clips.md` y lista los clips
   generados en `salida/clips/`.
