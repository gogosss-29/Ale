---
name: reel-cutter
description: Corta un video hablado en español en clips listos para editar. Transcribe con timestamps a nivel de palabra (faster-whisper), detecta silencios con ffmpeg y calcula cortes que nunca parten palabras. Exporta clips mp4 frame-accurate, mapeo_clips.md con el texto exacto de cada clip y segments.json con tiempos de palabra relativos para sincronizar animaciones.
when_to_use: Cuando el usuario pida cortar/trocear un video o reel en clips, cortar en silencios/pausas, transcribir con timestamps de palabra, o preparar clips para sincronizar animaciones o subtítulos.
allowed-tools: Bash(python3 *) Bash(ffmpeg *) Bash(ffprobe *) Bash(pip3 *)
argument-hint: [ruta_al_video] [--max N] [--min N]
---

# Reel Cutter — cortar reels sin partir palabras

Herramienta CLI bundleada en `${CLAUDE_PLUGIN_ROOT}/skills/reel-cutter/scripts/reel_cutter.py`.

## Antes de ejecutar

1. Verifica dependencias (el hook SessionStart puede seguir instalándolas en background):
   - `command -v ffmpeg && command -v ffprobe`
   - `python3 -c "import faster_whisper"`
   - Si faltan: `apt-get install -y ffmpeg` (o brew) y `pip3 install faster-whisper`.
2. La primera transcripción descarga el modelo (~1.5–3 GB). En CPU, `large-v3` es
   lento: si el usuario no exige máxima calidad, usa `--modelo medium`.

## Ejecutar

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/reel-cutter/scripts/reel_cutter.py" VIDEO \
  --max 10 --min 4 --salida salida
```

Flags: `--max` (s, default 10), `--min` (s, default 4), `--noise` (dB, default -32),
`--min-silence` (s, default 0.16), `--cortes "0,5.85,..."` (override manual; solo
valida y avisa si un corte parte palabra), `--modelo` (default large-v3, fallback
automático a medium), `--salida` (default `salida`).

## Salidas (en `--salida`)

- `clips/seq_XX_INICIO-FINs.mp4` — clips re-encodeados frame-accurate.
- `segments.json` — por clip: texto y palabras `{word,start,end}` con tiempos
  **relativos al inicio del clip** (para sincronizar animaciones).
- `mapeo_clips.md` — tabla clip | rango | duración | texto exacto.
- `transcript.srt` / `transcript.txt` / `palabras.csv` — del video completo.
- `silencios.txt` — silencios detectados y si son corte válido.

## Después de ejecutar

- Muestra al usuario la tabla de `mapeo_clips.md` (o un resumen) para que vea
  qué dice cada clip.
- Si los cortes salen raros: ajustar `--noise` (más negativo = más estricto) y
  `--min-silence`. Si avisa "no hay silencio dentro de --max", el video tiene
  tramos largos sin pausas.
- Responde siempre en el idioma del usuario (típicamente español).
