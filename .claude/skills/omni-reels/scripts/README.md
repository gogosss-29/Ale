# `reel_cutter.py` — cortar un video en clips ≤10s para Omni

Trocea un talking-head en clips que **cortan en silencios** (nunca a mitad de
palabra) y exporta, junto a cada clip, el **texto real** y los **timestamps de
palabra** para clavar las animaciones de Omni a la locución.

## Requisitos

- **Python 3.9+**
- **ffmpeg + ffprobe** en el PATH (dependencia de sistema).
- `pip install -r requirements.txt` (instala `faster-whisper`).

La primera corrida descarga el modelo de Whisper (`large-v3`, con fallback a
`medium`). Detecta GPU (CUDA) automáticamente; si no hay, corre en CPU.

## Uso

```bash
python reel_cutter.py "mi-video.mp4" --max 10 --min 4
```

### Flags principales

| Flag | Default | Qué hace |
|------|---------|----------|
| `video` | — | Ruta al video (mp4/mov). Posicional, obligatorio. |
| `--max` | `10` | Duración máxima por clip (s). Es el límite de Omni. |
| `--min` | `4` | Duración mínima deseada por clip (s). |
| `--noise` | `-32` | Umbral de silencio (dB) para `silencedetect`. |
| `--min-silence` | `0.16` | Duración mínima de un silencio (s) para ser corte candidato. |
| `--cortes` | — | Override manual: `"0,5.85,13.76,..."`. Solo valida que no partan palabras. |
| `--modelo` | `large-v3` | Modelo faster-whisper (fallback `medium`). |
| `--device` | `auto` | `auto` / `cpu` / `cuda`. |
| `--fade` | `0.008` | Micro-fade de audio en bordes (s) para evitar clicks. `0` = off. |
| `--salida` | `salida` | Directorio de salida. |
| `--force` | — | Re-transcribe aunque exista caché. |

## Qué genera (en `salida/`)

| Archivo | Contenido |
|---------|-----------|
| `clips/seq_NN_<ini>-<fin>s.mp4` | Los clips ≤10s, re-encodeados frame-accurate. |
| **`segments.json`** | Por clip: `index, start, end, duration, text` y `words` con **timestamps relativos al inicio del clip** → la fuente para los cues por tiempo de Omni. |
| **`mapeo_clips.md`** | Tabla legible: clip → rango → duración → texto. |
| `transcript.json` | Transcripción completa cacheada (para re-cortar sin re-transcribir). |
| `transcript.srt` | SRT palabra por palabra del video entero. |
| `transcript.txt` | Texto plano por segmentos. |
| `palabras.csv` | `word, start, end` de todo el video. |
| `silencios.txt` | Silencios detectados (`start, end, dur, medio`). |

## Cómo encaja en la skill `omni-reels`

Este es el **paso 2** del flujo (ver `../SKILL.md`): produce los clips + el
`segments.json` con el que se escriben los prompts de Omni **disparando cada
animación por tiempo** (`"At ~4.3s slide in…"`), nunca con "when I say [palabra]".

## Notas de diseño

- **Los cortes salen de los gaps entre palabras** (garantizan no partir palabra),
  afinados al punto medio de un silencio de `silencedetect` cuando cae dentro del
  gap. El algoritmo es greedy: cubre el video con segmentos ≤`--max`, idealmente
  ≥`--min`, prefiriendo pausas largas y clips llenos (pesos `PAUSE_WEIGHT` /
  `CLOSE_WEIGHT`), y rebalancea la cola final para no dejar un clip corto.
- Si no hay silencios utilizables, avisa y cae a una grilla por tiempo (puede
  partir palabras) — situación a evitar.
- La transcripción se cachea por `(ruta, tamaño, mtime, modelo)`; iterar los
  cortes es instantáneo. Usá `--force` para re-transcribir.
