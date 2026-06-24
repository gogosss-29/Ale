# reel_cutter

Cortador inteligente de **reels en español**. Con un solo comando:

1. Transcribe el video con **timestamps a nivel de palabra** (faster-whisper).
2. Detecta **silencios** con `ffmpeg silencedetect`.
3. Calcula **cortes que nunca parten una palabra** (caen siempre en el medio de un silencio).
4. Exporta cada clip **re-encodeado frame-accurate** + un mapeo legible + `segments.json` con tiempos de palabra **relativos a cada clip** (para sincronizar animaciones).

---

## Requisitos

- **Python 3.9+**
- **ffmpeg** y **ffprobe** en el `PATH`:
  - macOS: `brew install ffmpeg`
  - Ubuntu/Debian: `sudo apt install ffmpeg`
  - Windows: https://www.gyan.dev/ffmpeg/builds/
- Dependencias Python:

```bash
cd reel_cutter
pip install -r requirements.txt
```

> La **primera ejecución descarga el modelo** de Whisper (`large-v3` ≈ 3 GB,
> `medium` ≈ 1.5 GB). Necesitas conexión y espacio en disco.
>
> GPU NVIDIA (CUDA) se usa automáticamente si `torch` la detecta; si no, corre
> en CPU con `int8` (más lento pero funciona).

---

## Uso

```bash
python reel_cutter.py "Mati, clip.mp4" --max 10 --min 4
```

Genera todo dentro de `salida/`.

### Flags

| Flag | Default | Qué hace |
|------|---------|----------|
| `--max` | `10` | Duración máxima de cada clip (s). |
| `--min` | `4` | Duración mínima deseada de cada clip (s). |
| `--noise` | `-32` | Umbral de silencio en dB para `silencedetect`. |
| `--min-silence` | `0.16` | Duración mínima de un silencio (s). |
| `--cortes` | — | Override manual: `"0,5.85,13.76,..."` (segundos). Solo valida que no partan palabras y avisa. |
| `--modelo` | `large-v3` | Modelo faster-whisper. Fallback automático a `medium`. |
| `--salida` | `salida` | Carpeta de salida. |

### Ejemplos

```bash
# Clips más cortos y silencios más sensibles
python reel_cutter.py video.mp4 --max 8 --min 3 --noise -35 --min-silence 0.2

# Cortes manuales (los defines vos; el script solo avisa si parten palabra)
python reel_cutter.py video.mp4 --cortes "0,5.85,13.76,21.40"

# Forzar modelo medium (más rápido)
python reel_cutter.py video.mp4 --modelo medium
```

---

## Salidas (`salida/`)

```
salida/
├── clips/
│   ├── seq_01_0.00-5.85s.mp4
│   ├── seq_02_5.85-13.76s.mp4
│   └── ...
├── segments.json      # por clip: índice, inicio, fin, duración, texto y palabras
│                       #   {word,start,end} con tiempos RELATIVOS al inicio del clip
├── mapeo_clips.md      # tabla: clip | rango | duración | texto exacto
├── transcript.srt      # subtítulos del video completo
├── transcript.txt      # transcripción plana del video completo
├── palabras.csv        # word,start,end de TODO el video (tiempos absolutos)
├── silencios.txt       # silencios detectados + si son corte válido
└── audio_16k_mono.wav  # audio extraído (intermedio)
```

### `segments.json` (ejemplo)

```json
[
  {
    "index": 1,
    "inicio": 0.0,
    "fin": 5.85,
    "duracion": 5.85,
    "texto": "Hola, soy Alexander y esto es una prueba.",
    "palabras": [
      { "word": "Hola,", "start": 0.12, "end": 0.41 },
      { "word": "soy",   "start": 0.55, "end": 0.78 }
    ]
  }
]
```

Los `start`/`end` de cada palabra están **relativos al inicio del clip**, así que
podés sincronizar animaciones directamente contra el clip exportado (que arranca
en 0).

---

## Cómo decide los cortes

- Cada **silencio** detectado define un punto de corte limpio = **su punto medio**.
- Se descartan los puntos que caigan **dentro de una palabra** (validados contra
  los word-timestamps). Solo quedan cortes que **no parten palabras**.
- Algoritmo **greedy** desde 0: dentro de la ventana `(inicio+min, inicio+max]`
  elige el silencio que mejor **balancea** entre estar cerca del máximo y ser una
  **pausa larga** (fin de frase). Si no hay silencio en la ventana, corta en el
  silencio más cercano por debajo del máximo.
- **Rebalanceo de la cola**: evita dejar un último clip más corto que `--min`.
- Con `--cortes`, usa tus puntos tal cual y **solo avisa** si alguno cae en palabra.

---

## Problemas comunes

| Síntoma | Solución |
|---------|----------|
| `ERROR: No se encontró 'ffmpeg'` | Instalá ffmpeg (ver Requisitos). |
| Se queda en "Transcribiendo..." mucho tiempo | En CPU `large-v3` es lento; probá `--modelo medium`. |
| No descarga el modelo | Revisá conexión y espacio en disco; reintentá. |
| Cortes en lugares raros | Ajustá `--noise` (más negativo = más estricto) y `--min-silence`. |
| Clips muy largos | Bajá `--max`; si avisa "no hay silencio dentro de --max", el video tiene tramos sin pausas. |
