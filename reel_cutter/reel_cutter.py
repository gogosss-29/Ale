#!/usr/bin/env python3
"""reel_cutter.py — Cortador inteligente de reels en español.

Transcribe un video con timestamps a nivel de palabra (faster-whisper),
detecta silencios (ffmpeg silencedetect), calcula cortes que NUNCA parten
una palabra y exporta cada clip re-encodeado frame-accurate, más un mapeo
legible y un segments.json con tiempos de palabra relativos a cada clip
(para sincronizar animaciones).

Uso:
    python reel_cutter.py "Mati, clip.mp4" --max 10 --min 4

Ver README.md para detalles.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, asdict, field
from typing import List, Optional, Tuple


# --------------------------------------------------------------------------- #
# Utilidades de salida
# --------------------------------------------------------------------------- #

def log(msg: str) -> None:
    print(f"[reel_cutter] {msg}", flush=True)


def warn(msg: str) -> None:
    print(f"[reel_cutter] AVISO: {msg}", file=sys.stderr, flush=True)


def die(msg: str, code: int = 1) -> "NoReturn":  # type: ignore[name-defined]
    print(f"[reel_cutter] ERROR: {msg}", file=sys.stderr, flush=True)
    sys.exit(code)


def fmt_ts(seconds: float, decimals: int = 2) -> str:
    """0.00 -> '0.00' (para nombres de archivo)."""
    return f"{seconds:.{decimals}f}"


def srt_ts(seconds: float) -> str:
    """Formato HH:MM:SS,mmm para SRT."""
    if seconds < 0:
        seconds = 0.0
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3600 * 1000)
    m, ms = divmod(ms, 60 * 1000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


# --------------------------------------------------------------------------- #
# Estructuras de datos
# --------------------------------------------------------------------------- #

@dataclass
class Word:
    word: str
    start: float
    end: float


@dataclass
class Silence:
    start: float
    end: float

    @property
    def mid(self) -> float:
        return (self.start + self.end) / 2.0

    @property
    def duration(self) -> float:
        return max(0.0, self.end - self.start)


@dataclass
class Segment:
    index: int
    inicio: float
    fin: float
    duracion: float
    texto: str
    palabras: List[dict] = field(default_factory=list)


# --------------------------------------------------------------------------- #
# Comprobaciones de entorno
# --------------------------------------------------------------------------- #

def require_ffmpeg() -> Tuple[str, str]:
    ffmpeg = shutil.which("ffmpeg")
    ffprobe = shutil.which("ffprobe")
    if not ffmpeg:
        die(
            "No se encontró 'ffmpeg' en el PATH. Instálalo:\n"
            "  - macOS:   brew install ffmpeg\n"
            "  - Ubuntu:  sudo apt install ffmpeg\n"
            "  - Windows: https://www.gyan.dev/ffmpeg/builds/"
        )
    if not ffprobe:
        die("Se encontró ffmpeg pero falta 'ffprobe' (viene en el mismo paquete de ffmpeg).")
    return ffmpeg, ffprobe


def run(cmd: List[str], capture: bool = True) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(
            cmd,
            check=True,
            capture_output=capture,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        cmd_str = " ".join(cmd[:6]) + (" ..." if len(cmd) > 6 else "")
        stderr = (e.stderr or "").strip()
        die(f"Falló el comando: {cmd_str}\n{stderr[-1500:]}")


# --------------------------------------------------------------------------- #
# Sondas de medios
# --------------------------------------------------------------------------- #

def probe_duration(ffprobe: str, path: str) -> float:
    cp = run([
        ffprobe, "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        path,
    ])
    try:
        return float(cp.stdout.strip())
    except ValueError:
        die(f"No pude leer la duración de '{path}'. ¿Es un video válido?")


def extract_audio(ffmpeg: str, video: str, wav_out: str) -> None:
    log("Extrayendo audio a WAV mono 16 kHz...")
    run([
        ffmpeg, "-y", "-i", video,
        "-vn", "-ac", "1", "-ar", "16000",
        "-acodec", "pcm_s16le",
        wav_out,
    ])


# --------------------------------------------------------------------------- #
# Transcripción (faster-whisper)
# --------------------------------------------------------------------------- #

def pick_device_and_compute() -> Tuple[str, str]:
    """Autodetecta GPU/CPU y un compute_type razonable."""
    try:
        import torch  # type: ignore
        if torch.cuda.is_available():
            return "cuda", "float16"
    except Exception:
        pass
    return "cpu", "int8"


def load_model(model_name: str, device: str, compute_type: str):
    try:
        from faster_whisper import WhisperModel  # type: ignore
    except ImportError:
        die(
            "Falta 'faster-whisper'. Instálalo con:\n"
            "  pip install -r requirements.txt"
        )

    def _try(name: str, ct: str):
        log(f"Cargando modelo '{name}' (device={device}, compute_type={ct})...")
        return WhisperModel(name, device=device, compute_type=ct)

    # Intento principal -> fallback de compute_type (cpu) -> fallback de modelo.
    try:
        return _try(model_name, compute_type), model_name
    except Exception as e1:
        warn(f"No pude cargar '{model_name}' con compute_type={compute_type}: {e1}")
        # Reintento con compute_type seguro en CPU.
        if device == "cpu" and compute_type != "int8":
            try:
                return _try(model_name, "int8"), model_name
            except Exception:
                pass
        # Fallback a 'medium' si el principal no era ya medium/menor.
        if model_name != "medium":
            warn("Probando fallback a modelo 'medium'...")
            try:
                return _try("medium", "int8" if device == "cpu" else compute_type), "medium"
            except Exception as e2:
                die(
                    "No pude descargar/cargar ni el modelo solicitado ni el fallback 'medium'.\n"
                    f"Detalle: {e2}\n"
                    "Revisa tu conexión (la primera vez se descarga el modelo) y el espacio en disco."
                )
        die(f"No pude cargar el modelo de transcripción: {e1}")


def transcribe(model, wav_path: str) -> Tuple[List[Word], list]:
    log("Transcribiendo (idioma=es, word_timestamps=True)... puede tardar.")
    segments_iter, _info = model.transcribe(
        wav_path,
        language="es",
        word_timestamps=True,
        vad_filter=False,
    )
    words: List[Word] = []
    raw_segments: list = []
    for seg in segments_iter:
        raw_segments.append({
            "start": float(seg.start),
            "end": float(seg.end),
            "text": (seg.text or "").strip(),
        })
        for w in (seg.words or []):
            if w.start is None or w.end is None:
                continue
            token = (w.word or "").strip()
            if not token:
                continue
            words.append(Word(word=token, start=float(w.start), end=float(w.end)))
    if not words:
        warn("La transcripción no devolvió palabras con timestamps. "
             "Los cortes se calcularán solo con silencios.")
    log(f"Transcripción lista: {len(words)} palabras, {len(raw_segments)} segmentos de frase.")
    return words, raw_segments


# --------------------------------------------------------------------------- #
# Detección de silencios
# --------------------------------------------------------------------------- #

def detect_silences(ffmpeg: str, wav_path: str, noise_db: float, min_sil: float) -> List[Silence]:
    log(f"Detectando silencios (noise={noise_db}dB, min_silence={min_sil}s)...")
    # silencedetect escribe a stderr; capturamos.
    proc = subprocess.run(
        [
            ffmpeg, "-i", wav_path,
            "-af", f"silencedetect=noise={noise_db}dB:d={min_sil}",
            "-f", "null", "-",
        ],
        capture_output=True, text=True,
    )
    out = proc.stderr or ""
    starts = [float(m.group(1)) for m in re.finditer(r"silence_start:\s*([0-9.]+)", out)]
    ends = [float(m.group(1)) for m in re.finditer(r"silence_end:\s*([0-9.]+)", out)]
    silences: List[Silence] = []
    for i, s in enumerate(starts):
        e = ends[i] if i < len(ends) else None
        if e is None:
            continue
        if e > s:
            silences.append(Silence(start=s, end=e))
    log(f"Silencios detectados: {len(silences)}")
    return silences


# --------------------------------------------------------------------------- #
# Validación contra palabras
# --------------------------------------------------------------------------- #

def inside_word(t: float, words: List[Word], pad: float = 0.0) -> Optional[Word]:
    """Devuelve la palabra cuyo intervalo [start,end] contiene t (con pad), o None."""
    for w in words:
        if (w.start - pad) <= t <= (w.end + pad):
            return w
    return None


def valid_cut_candidates(silences: List[Silence], words: List[Word],
                         total: float) -> List[Tuple[float, float]]:
    """Puntos de corte válidos = punto medio de cada silencio que NO cae dentro
    de una palabra. Devuelve lista de (tiempo_corte, duracion_silencio)."""
    cands: List[Tuple[float, float]] = []
    for s in silences:
        mid = s.mid
        if mid <= 0 or mid >= total:
            continue
        if inside_word(mid, words) is not None:
            # El medio cae en palabra (raro): intentamos un punto del silencio
            # que quede libre, si existe.
            adj = _free_point_in_silence(s, words)
            if adj is None:
                continue
            cands.append((adj, s.duration))
        else:
            cands.append((mid, s.duration))
    cands.sort(key=lambda c: c[0])
    return cands


def _free_point_in_silence(s: Silence, words: List[Word]) -> Optional[float]:
    """Busca un instante dentro del silencio que no caiga en ninguna palabra."""
    step = 0.02
    t = s.start
    best = None
    while t <= s.end:
        if inside_word(t, words) is None:
            # preferimos el más centrado
            if best is None or abs(t - s.mid) < abs(best - s.mid):
                best = t
        t += step
    return best


def nearest_valid_cut(t: float, candidates: List[Tuple[float, float]]) -> Optional[float]:
    if not candidates:
        return None
    return min(candidates, key=lambda c: abs(c[0] - t))[0]


# --------------------------------------------------------------------------- #
# Algoritmo de cortes automáticos
# --------------------------------------------------------------------------- #

def auto_cuts(total: float, candidates: List[Tuple[float, float]],
              min_s: float, max_s: float) -> List[float]:
    """Cortes greedy desde 0 que cubren todo el video.

    Devuelve la lista de fronteras internas (sin incluir 0 ni total).
    """
    if total <= max_s:
        return []

    # Referencia para "pausa larga" (límite de frase): usamos un valor fijo
    # razonable; las pausas >= LONG_REF se consideran fin de frase.
    LONG_REF = 0.6
    LONG_WEIGHT = 0.6  # cuánto pesa la longitud de la pausa frente a la cercanía al max

    cut_times = sorted(c[0] for c in candidates)
    dur_by_time = {c[0]: c[1] for c in candidates}

    cuts: List[float] = []
    start = 0.0
    used = set()

    while (total - start) > max_s:
        win_lo = start + min_s
        win_hi = start + max_s

        # Candidatos dentro de la ventana ideal (inicio+min, inicio+max].
        in_window = [t for t in cut_times
                     if win_lo < t <= win_hi and t not in used and t > start]

        chosen: Optional[float] = None
        if in_window:
            def score(t: float) -> float:
                seg_len = t - start
                # cercanía al máximo: 1 en el max, 0 en el min
                closeness = (seg_len - min_s) / max(1e-6, (max_s - min_s))
                closeness = max(0.0, min(1.0, closeness))
                long_pause = min(dur_by_time.get(t, 0.0) / LONG_REF, 1.0)
                return closeness + LONG_WEIGHT * long_pause
            chosen = max(in_window, key=score)
        else:
            # Sin silencio en la ventana: el más cercano por debajo del máximo.
            below = [t for t in cut_times
                     if start < t <= win_hi and t not in used]
            if below:
                chosen = max(below)  # el más cercano al max
            else:
                # Ningún silencio antes del max: tomamos el primero disponible
                # más allá del max (evita partir palabra aunque exceda max).
                beyond = [t for t in cut_times if t > start and t not in used]
                if beyond:
                    chosen = min(beyond)
                    warn(f"No hay silencio dentro de --max tras {fmt_ts(start)}s; "
                         f"corto en {fmt_ts(chosen)}s (segmento > max).")
                else:
                    # No quedan silencios: el resto va en un solo clip final.
                    break

        cuts.append(chosen)
        used.add(chosen)
        start = chosen

    # Rebalanceo de la cola final: evitar último clip < min.
    cuts = _rebalance_tail(cuts, total, cut_times, used, min_s, max_s)
    return cuts


def _rebalance_tail(cuts: List[float], total: float, cut_times: List[float],
                    used: set, min_s: float, max_s: float) -> List[float]:
    if not cuts:
        return cuts
    last_cut = cuts[-1]
    tail = total - last_cut
    if tail >= min_s:
        return cuts

    prev = cuts[-2] if len(cuts) >= 2 else 0.0
    region = total - prev  # zona a recubrir tras quitar el último corte

    # Si toda la región cabe en un clip, eliminamos el último corte.
    if region <= max_s:
        cuts.pop()
        return cuts

    # Si no cabe en un clip, reubicamos el último corte para que la cola final
    # quede entre min y max. Ventana del nuevo corte: [total-max, total-min].
    lo = max(prev, total - max_s)
    hi = total - min_s
    options = [t for t in cut_times if lo <= t <= hi and t != last_cut]
    if options:
        # Preferimos opciones donde el trozo previo también quede en [min, max];
        # entre ellas (o todas), la que deje el primer trozo más cerca del max.
        ideal = [t for t in options if min_s <= (t - prev) <= max_s]
        pool = ideal if ideal else options
        target = min(prev + max_s, hi)
        new_cut = min(pool, key=lambda t: abs(t - target))
        cuts[-1] = new_cut
    else:
        warn("No pude rebalancear la cola final sin partir palabras; "
             "el último clip puede quedar más corto que --min.")
    return cuts


def parse_manual_cuts(spec: str, total: float, words: List[Word]) -> List[float]:
    raw = []
    for tok in spec.split(","):
        tok = tok.strip()
        if not tok:
            continue
        try:
            raw.append(float(tok))
        except ValueError:
            die(f"Valor de --cortes inválido: '{tok}' (deben ser segundos, ej: 0,5.85,13.76)")
    cuts = sorted(t for t in raw if 0.0 < t < total)
    for t in cuts:
        w = inside_word(t, words)
        if w is not None:
            warn(f"El corte manual {fmt_ts(t)}s cae dentro de la palabra "
                 f"'{w.word}' [{fmt_ts(w.start)}-{fmt_ts(w.end)}]. Se usa igual.")
    return cuts


# --------------------------------------------------------------------------- #
# Construcción de segmentos y asignación de palabras
# --------------------------------------------------------------------------- #

def build_segments(boundaries: List[float], total: float,
                   words: List[Word]) -> List[Segment]:
    edges = [0.0] + boundaries + [total]
    segments: List[Segment] = []
    for i in range(len(edges) - 1):
        a, b = edges[i], edges[i + 1]
        # Palabra pertenece al clip si su centro cae en [a, b).
        seg_words = []
        texto_parts = []
        for w in words:
            center = (w.start + w.end) / 2.0
            if a <= center < b:
                seg_words.append({
                    "word": w.word,
                    "start": round(w.start - a, 3),
                    "end": round(w.end - a, 3),
                })
                texto_parts.append(w.word)
        texto = _join_words(texto_parts)
        segments.append(Segment(
            index=i + 1,
            inicio=round(a, 3),
            fin=round(b, 3),
            duracion=round(b - a, 3),
            texto=texto,
            palabras=seg_words,
        ))
    return segments


def _join_words(parts: List[str]) -> str:
    text = ""
    for p in parts:
        if not text:
            text = p
        elif p and p[0] in ".,;:!?…)":
            text += p
        else:
            text += " " + p
    return text.strip()


# --------------------------------------------------------------------------- #
# Exportadores
# --------------------------------------------------------------------------- #

def export_clips(ffmpeg: str, video: str, segments: List[Segment], clips_dir: str) -> None:
    os.makedirs(clips_dir, exist_ok=True)
    log(f"Exportando {len(segments)} clips (re-encode frame-accurate)...")
    for seg in segments:
        name = f"seq_{seg.index:02d}_{fmt_ts(seg.inicio)}-{fmt_ts(seg.fin)}s.mp4"
        out = os.path.join(clips_dir, name)
        run([
            ffmpeg, "-y",
            "-i", video,
            "-ss", f"{seg.inicio:.3f}",
            "-to", f"{seg.fin:.3f}",
            "-c:v", "libx264", "-crf", "18", "-preset", "veryfast",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "160k",
            "-movflags", "+faststart",
            out,
        ])
        log(f"  ✓ {name}  ({seg.duracion:.2f}s)  «{seg.texto[:60]}{'…' if len(seg.texto) > 60 else ''}»")


def write_segments_json(segments: List[Segment], path: str) -> None:
    data = [asdict(s) for s in segments]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def write_mapeo_md(segments: List[Segment], path: str, video_name: str) -> None:
    lines = [
        f"# Mapeo de clips — {video_name}",
        "",
        "| Clip | Rango | Duración | Texto |",
        "|------|-------|----------|-------|",
    ]
    for s in segments:
        texto = s.texto.replace("|", "\\|") or "(sin texto)"
        rango = f"{s.inicio:.2f}s → {s.fin:.2f}s"
        lines.append(f"| seq_{s.index:02d} | {rango} | {s.duracion:.2f}s | {texto} |")
    lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_srt(raw_segments: list, path: str) -> None:
    lines = []
    for i, seg in enumerate(raw_segments, 1):
        lines.append(str(i))
        lines.append(f"{srt_ts(seg['start'])} --> {srt_ts(seg['end'])}")
        lines.append(seg["text"])
        lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_txt(raw_segments: list, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(seg["text"] for seg in raw_segments).strip() + "\n")


def write_words_csv(words: List[Word], path: str) -> None:
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["word", "start", "end"])
        for word in words:
            w.writerow([word.word, f"{word.start:.3f}", f"{word.end:.3f}"])


def write_silences_txt(silences: List[Silence], candidates: List[Tuple[float, float]],
                       path: str) -> None:
    cand_times = {round(c[0], 3) for c in candidates}
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Silencios detectados (posibles puntos de corte)\n")
        f.write("# start  end  duracion  punto_medio  corte_valido\n")
        for s in silences:
            valido = "sí" if round(s.mid, 3) in cand_times else "no(palabra)"
            f.write(f"{s.start:.3f}  {s.end:.3f}  {s.duration:.3f}  "
                    f"{s.mid:.3f}  {valido}\n")


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def parse_args(argv: List[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="reel_cutter.py",
        description="Transcribe un video en español, calcula cortes en silencios "
                    "sin partir palabras y exporta los clips listos para editar.",
    )
    p.add_argument("video", help="Ruta al video de entrada (mp4/mov).")
    p.add_argument("--max", type=float, default=10.0,
                   help="Duración máxima de cada clip en segundos (default 10).")
    p.add_argument("--min", type=float, default=4.0,
                   help="Duración mínima deseada de cada clip en segundos (default 4).")
    p.add_argument("--noise", type=float, default=-32.0,
                   help="Umbral de silencio en dB para silencedetect (default -32).")
    p.add_argument("--min-silence", type=float, default=0.16, dest="min_silence",
                   help="Duración mínima de un silencio en segundos (default 0.16).")
    p.add_argument("--cortes", type=str, default=None,
                   help="Override manual de cortes: \"0,5.85,13.76,...\" (segundos).")
    p.add_argument("--modelo", type=str, default="large-v3",
                   help="Modelo faster-whisper (default large-v3; fallback medium).")
    p.add_argument("--salida", type=str, default="salida",
                   help="Carpeta de salida (default 'salida').")
    return p.parse_args(argv)


def main(argv: List[str]) -> int:
    args = parse_args(argv)

    if args.min <= 0 or args.max <= 0 or args.min >= args.max:
        die(f"--min ({args.min}) debe ser > 0 y menor que --max ({args.max}).")

    video = args.video
    if not os.path.isfile(video):
        die(f"No existe el archivo de video: '{video}'")

    ffmpeg, ffprobe = require_ffmpeg()

    out_dir = args.salida
    clips_dir = os.path.join(out_dir, "clips")
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(clips_dir, exist_ok=True)

    video_name = os.path.basename(video)
    log(f"Procesando: {video_name}")

    # 1) Duración + audio
    total = probe_duration(ffprobe, video)
    log(f"Duración total: {total:.2f}s")
    wav_path = os.path.join(out_dir, "audio_16k_mono.wav")
    extract_audio(ffmpeg, video, wav_path)

    # 2) Transcripción
    device, compute_type = pick_device_and_compute()
    log(f"Dispositivo: {device} | compute_type: {compute_type}")
    model, used_model = load_model(args.modelo, device, compute_type)
    words, raw_segments = transcribe(model, wav_path)

    # 3) Silencios
    silences = detect_silences(ffmpeg, wav_path, args.noise, args.min_silence)
    candidates = valid_cut_candidates(silences, words, total)
    log(f"Puntos de corte válidos (silencio sin palabra): {len(candidates)}")

    # 4) Cortes
    if args.cortes:
        log("Usando cortes manuales (--cortes).")
        boundaries = parse_manual_cuts(args.cortes, total, words)
    else:
        if not candidates:
            warn("No hay silencios válidos para cortar; se generará un único clip.")
        boundaries = auto_cuts(total, candidates, args.min, args.max)
    log(f"Cortes internos: {[round(b, 2) for b in boundaries]}")

    # 5) Segmentos + asignación de palabras
    segments = build_segments(boundaries, total, words)
    log(f"Total de clips: {len(segments)}")

    # 6) Exportar clips + artefactos
    export_clips(ffmpeg, video, segments, clips_dir)

    write_segments_json(segments, os.path.join(out_dir, "segments.json"))
    write_mapeo_md(segments, os.path.join(out_dir, "mapeo_clips.md"), video_name)
    write_srt(raw_segments, os.path.join(out_dir, "transcript.srt"))
    write_txt(raw_segments, os.path.join(out_dir, "transcript.txt"))
    write_words_csv(words, os.path.join(out_dir, "palabras.csv"))
    write_silences_txt(silences, candidates, os.path.join(out_dir, "silencios.txt"))

    log("¡Listo! Archivos en:")
    log(f"  {clips_dir}/  (clips .mp4)")
    log(f"  {out_dir}/segments.json")
    log(f"  {out_dir}/mapeo_clips.md")
    log(f"  {out_dir}/transcript.srt | transcript.txt | palabras.csv | silencios.txt")
    if used_model != args.modelo:
        warn(f"Se usó el modelo de fallback '{used_model}' en lugar de '{args.modelo}'.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        die("Interrumpido por el usuario.", code=130)
