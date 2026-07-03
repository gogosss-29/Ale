# Plugin reel-cutter

Plugin de Claude Code para cortar videos hablados en español en clips listos
para editar: transcripción con timestamps a nivel de palabra (faster-whisper),
cortes en silencios que **nunca parten palabras**, clips mp4 frame-accurate,
mapeo legible del texto de cada clip y `segments.json` con tiempos de palabra
relativos (para sincronizar animaciones).

## Instalación (en cualquier proyecto)

```
/plugin marketplace add gogosss-29/Ale
/plugin install reel-cutter@ale-tools
```

O por CLI: `claude plugin install reel-cutter@ale-tools --scope user`

## Qué incluye

| Componente | Qué hace |
|---|---|
| **Skill** `reel-cutter` | Claude la activa solo cuando pedís cortar un video/reel; sabe los flags, interpreta las salidas y responde en español. |
| **Comando** `/reel-cutter:reel <video> [flags]` | Atajo explícito para cortar un video. |
| **Hook SessionStart** | Verifica ffmpeg + faster-whisper; en sesiones remotas (web) los instala en segundo plano. |
| **Script** `skills/reel-cutter/scripts/reel_cutter.py` | La herramienta CLI (fuente canónica). |

## Uso directo (sin Claude)

```bash
pip install -r skills/reel-cutter/scripts/requirements.txt
python3 skills/reel-cutter/scripts/reel_cutter.py video.mp4 --max 10 --min 4
```

Documentación completa de flags y salidas: ver [`../../reel_cutter/README.md`](../../reel_cutter/README.md)
(en este repo) o el propio `--help` del script.

## Notas

- Requiere `ffmpeg`/`ffprobe` en el sistema y Python 3.9+.
- La primera transcripción descarga el modelo Whisper (~1.5–3 GB).
- En CPU conviene `--modelo medium`; `large-v3` es para máxima calidad.
- Integración con el pipeline AvatarHype de este repo:
  `python -m avatarhype.cli cortar video.mp4` (usa este mismo script vía
  `avatarhype/assembly/reel_cutter_bridge.py`).
