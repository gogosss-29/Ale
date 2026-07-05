# ⚙️ Sistema de edición de video (Remotion, data-driven)

Convierte **un video crudo + una receta** en un **video editado**, de punta a punta.
La máquina entrega el `.mp4` — no prompts. Reemplaza las composiciones ad-hoc
(hardcodeadas) por un motor genérico que lee un `EditMap`.

```
video.mp4 + receta.json  ─▶  node scripts/editar.mjs  ─▶  video editado .mp4
```

## Uso

```bash
cd remotion
node scripts/editar.mjs <video.mp4> <receta.json> [--out out.mp4] [--no-render]
# ejemplo (reproduce la edición del crudo):
node scripts/editar.mjs /ruta/crudos.mp4 recetas/crudos.json
```

Qué hace en orden: copia el video a `public/clips/` → **transcribe** (whisper,
cacheado en `out/edit-cache/`) → arma **captions** por palabra → **resuelve los
tiempos de cada beat por frase** → **segmenta** la persona en las ventanas
"detrás" (rembg) → **renderiza** con Remotion (composición `EditedVideo`).

## La receta

Lista de **beats** ubicados por **frase** (`at`) o por **segundo** (`atSec`).
`lead` adelanta el arranque; `dur` es la duración en segundos.

```json
{
  "brand": "CEREBRO",
  "captionPreset": "marca",          // "marca" (abajo, bold) | "minimal-top"
  "lang": "es", "model": "medium",
  "beats": [
    {"kind":"overlay","type":"topLabel","atSec":0,"dur":4.5,"props":{"text":"Fondo Beltrán Briones"}},
    {"kind":"overlay","type":"numberCallout","at":"45 millones","dur":3.4,"props":{"prefix":"US$","value":45,"suffix":"MILLONES"}},
    {"kind":"overlay","type":"chip","at":"cada tres meses","lead":0.4,"dur":3.2,"props":{"text":"CADA 3 MESES","sub":"Alquileres"}},
    {"kind":"behind","graphic":"risingLine","at":"suban de valor","dur":3.7,"props":{"curva":"ancha"}}
  ]
}
```

### Overlays disponibles (biblioteca `src/overlays.tsx`)

| `type` | Qué es | `props` |
|---|---|---|
| `topLabel` | Pill de tema arriba-centro | `text` |
| `numberCallout` | Dato clave con count-up | `prefix`, `value`, `suffix`, `color?` |
| `chip` | Dato secundario arriba-derecha | `text`, `sub?` |
| `barsLabel` | Mini barras + pill | `label`, `heights?` |
| `arrowChips` | Pares tipo ENTRAR/SALIR | `items:[{label,dir:"in"|"out",color?}]` |
| `bigBadge` | Badge grande centrado | `text`, `color?` |

### Beats "detrás" (occlusión con la persona)

`{"kind":"behind","graphic":"risingLine","at":"<frase>","dur":<s>,"props":{"curva":"ancha"|"empinada","color?":"#hex"}}`

Requiere **segmentación** de esa ventana (rembg `u2net_human_seg`). El CLI extrae
los cuadros, los recorta y compone *video → gráfico → recorte de persona*, así el
gráfico queda **por detrás** del sujeto. Los recortes van a `public/edit-person/`
(fuera de git).

## Dependencias del entorno
- **ffmpeg + ffprobe** (sistema).
- **faster-whisper** (pip) — transcripción.
- **rembg** + modelo `u2net_human_seg.onnx` en `~/.u2net/` — solo si hay beats "detrás".
- Chromium del contenedor para el render (`--chrome-mode=chrome-for-testing`).

## Piezas del sistema
- `src/overlays.tsx` — biblioteca de overlays parametrizados.
- `src/EditedVideo.tsx` — motor genérico (lee el `EditMap`).
- `scripts/editar.mjs` — CLI orquestador end-to-end.
- `scripts/py/transcribe.py`, `scripts/py/segment.py` — helpers.
- `recetas/*.json` — recetas por video.
