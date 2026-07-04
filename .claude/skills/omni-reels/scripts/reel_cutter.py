#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reel_cutter.py — Transcribe un video en español a nivel de palabra, calcula
cortes inteligentes que caen en silencios (nunca dentro de una palabra) y
exporta los clips listos para editar + el texto y los word-timestamps de cada
clip para sincronizar animaciones.

Objetivo:
    Un comando -> clips cortados en pausas + mapeo_clips.md con el texto real
    de cada uno + segments.json con timestamps de palabra relativos al clip.

Pipeline:
    1. Extraer audio a WAV mono 16 kHz (ffmpeg).
    2. Transcribir con faster-whisper (large-v3, fallback medium), es,
       word_timestamps=True. Se cachea en transcript.json para iterar cortes
       sin re-transcribir.
    3. Detectar candidatos de corte: gaps entre palabras (fuente primaria),
       confirmados/afinados con ffmpeg silencedetect.
    4. Algoritmo greedy de cortes (<= max, idealmente >= min), todos en el
       medio de una pausa, validados contra los word-timestamps.
    5. Exportar clips re-encodeados frame-accurate + reportes.

Uso:
    python reel_cutter.py "Mati, clip.mp4" --max 10 --min 4
"""

import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field

# --------------------------------------------------------------------------- #
# Constantes de scoring del algoritmo de cortes (explícitas, no escondidas)
# --------------------------------------------------------------------------- #
PAUSE_WEIGHT = 0.6   # preferir pausas largas = límites de frase
CLOSE_WEIGHT = 0.4   # preferir cortes cercanos al máximo (clips más llenos)


# --------------------------------------------------------------------------- #
# Utilidades de proceso / errores
# --------------------------------------------------------------------------- #
class ReelError(Exception):
    """Error de usuario con mensaje claro (no stacktrace)."""


def die(msg):
    print(f"\n[ERROR] {msg}\n", file=sys.stderr)
    sys.exit(1)


def info(msg):
    print(f"[*] {msg}")


def warn(msg):
    print(f"[!] {msg}")


def check_ffmpeg():
    if shutil.which("ffmpeg") is None:
        raise ReelError(
            "No se encontró 'ffmpeg' en el PATH. Instalalo desde "
            "https://ffmpeg.org/download.html y volvé a intentar."
        )
    if shutil.which("ffprobe") is None:
        raise ReelError(
            "Se encontró ffmpeg pero falta 'ffprobe' (viene en el mismo "
            "paquete). Reinstalá ffmpeg completo."
        )


def run(cmd, capture_stderr=False):
    """Ejecuta un comando. Devuelve stderr si capture_stderr (silencedetect)."""
    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except FileNotFoundError:
        raise ReelError(f"No se pudo ejecutar: {cmd[0]}")
    if proc.returncode != 0 and not capture_stderr:
        raise ReelError(
            f"Falló el comando:\n  {' '.join(cmd)}\n\n{proc.stderr[-1500:]}"
        )
    return proc.stderr if capture_stderr else proc.stdout


# --------------------------------------------------------------------------- #
# ffprobe: metadatos del video
# --------------------------------------------------------------------------- #
def probe_video(path):
    out = run([
        "ffprobe", "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=r_frame_rate,width,height",
        "-show_entries", "format=duration",
        "-of", "json", path,
    ])
    data = json.loads(out)
    fmt = data.get("format", {})
    streams = data.get("streams", [])
    if not streams:
        raise ReelError(f"El archivo no tiene pista de video: {path}")
    s = streams[0]
    # r_frame_rate viene como "30000/1001"
    num, _, den = s.get("r_frame_rate", "0/1").partition("/")
    fps = float(num) / float(den) if den and float(den) else 0.0
    duration = float(fmt.get("duration", 0.0))
    if duration <= 0:
        raise ReelError("No se pudo determinar la duración del video.")
    return {
        "duration": duration,
        "fps": round(fps, 4),
        "width": int(s.get("width", 0)),
        "height": int(s.get("height", 0)),
    }


# --------------------------------------------------------------------------- #
# 1) Extracción de audio
# --------------------------------------------------------------------------- #
def extract_audio(video_path, wav_path):
    info("Extrayendo audio a WAV mono 16 kHz...")
    run([
        "ffmpeg", "-y", "-i", video_path,
        "-vn", "-ac", "1", "-ar", "16000",
        "-c:a", "pcm_s16le", wav_path,
    ])
    if not os.path.exists(wav_path) or os.path.getsize(wav_path) == 0:
        raise ReelError(
            "ffmpeg no produjo audio. ¿El video tiene pista de audio?"
        )


# --------------------------------------------------------------------------- #
# 2) Transcripción (con caché)
# --------------------------------------------------------------------------- #
def detect_device():
    """Devuelve (device, compute_type) según haya GPU disponible."""
    try:
        import ctranslate2
        if ctranslate2.get_cuda_device_count() > 0:
            return "cuda", "float16"
    except Exception:
        pass
    return "cpu", "int8"


def cache_key(video_path, model_name):
    st = os.stat(video_path)
    return f"{os.path.abspath(video_path)}|{st.st_size}|{int(st.st_mtime)}|{model_name}"


def transcribe(video_path, wav_path, transcript_json, model_name, device_flag,
               force):
    # ¿Caché válida? (transcribir es lo lento; cortar es lo que se itera)
    key = cache_key(video_path, model_name)
    if not force and os.path.exists(transcript_json):
        try:
            with open(transcript_json, encoding="utf-8") as f:
                cached = json.load(f)
            if cached.get("_cache_key") == key:
                info("Usando transcripción cacheada (transcript.json). "
                     "Usá --force para re-transcribir.")
                return cached
        except (json.JSONDecodeError, OSError):
            pass

    try:
        from faster_whisper import WhisperModel
    except ImportError:
        raise ReelError(
            "Falta el paquete 'faster-whisper'. Instalá las dependencias:\n"
            "  pip install -r requirements.txt"
        )

    if device_flag == "auto":
        device, compute_type = detect_device()
    elif device_flag == "cuda":
        device, compute_type = "cuda", "float16"
    else:
        device, compute_type = "cpu", "int8"

    info(f"Cargando modelo '{model_name}' en {device} ({compute_type})...")
    models_to_try = [model_name]
    if model_name == "large-v3":
        models_to_try.append("medium")  # fallback

    model = None
    last_err = None
    used_model = model_name
    for m in models_to_try:
        try:
            model = WhisperModel(m, device=device, compute_type=compute_type)
            used_model = m
            if m != model_name:
                warn(f"No se pudo cargar '{model_name}', usando fallback '{m}'.")
            break
        except Exception as e:  # descarga fallida / sin VRAM / etc.
            last_err = e
            if device == "cuda":
                warn(f"Falló en GPU ({e}); reintentando en CPU...")
                device, compute_type = "cpu", "int8"
                try:
                    model = WhisperModel(m, device=device,
                                         compute_type=compute_type)
                    used_model = m
                    break
                except Exception as e2:
                    last_err = e2
    if model is None:
        raise ReelError(
            "No se pudo cargar/descargar ningún modelo de Whisper.\n"
            f"Último error: {last_err}\n"
            "Verificá conexión a internet (la primera vez descarga el modelo) "
            "y espacio en disco."
        )

    info("Transcribiendo (es, word_timestamps=True)... esto puede tardar.")
    segments_gen, tinfo = model.transcribe(
        wav_path,
        language="es",
        word_timestamps=True,
        beam_size=5,            # fijo -> más reproducible
        vad_filter=False,
    )

    words = []
    seg_texts = []
    for seg in segments_gen:
        seg_texts.append({
            "start": float(seg.start),
            "end": float(seg.end),
            "text": seg.text.strip(),
        })
        if seg.words:
            for w in seg.words:
                token = w.word.strip()
                if not token:
                    continue
                words.append({
                    "word": token,
                    "start": round(float(w.start), 3),
                    "end": round(float(w.end), 3),
                })
        print(f"\r    ...{len(words)} palabras", end="", flush=True)
    print()

    if not words:
        warn("No se detectaron palabras (¿video sin habla?). "
             "Los cortes caerán por tiempo, no por silencio.")

    result = {
        "_cache_key": key,
        "model": used_model,
        "language": "es",
        "duration": float(getattr(tinfo, "duration", 0.0)),
        "segments": seg_texts,
        "words": words,
    }
    with open(transcript_json, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    return result


# --------------------------------------------------------------------------- #
# 3) Candidatos de corte (gaps de palabras + silencedetect)
# --------------------------------------------------------------------------- #
@dataclass
class Cut:
    time: float       # punto de corte (medio de la pausa)
    pause: float      # duración de la pausa asociada (s)


def detect_silences(wav_path, noise_db, min_silence):
    """Devuelve lista de (start, end) de silencios detectados por ffmpeg."""
    stderr = run([
        "ffmpeg", "-i", wav_path,
        "-af", f"silencedetect=noise={noise_db}dB:d={min_silence}",
        "-f", "null", "-",
    ], capture_stderr=True)

    silences = []
    cur_start = None
    for line in stderr.splitlines():
        m = re.search(r"silence_start:\s*(-?\d+\.?\d*)", line)
        if m:
            cur_start = float(m.group(1))
            continue
        m = re.search(r"silence_end:\s*(-?\d+\.?\d*)", line)
        if m and cur_start is not None:
            silences.append((max(0.0, cur_start), float(m.group(1))))
            cur_start = None
    return silences


def build_candidates(words, silences, duration, min_silence):
    """
    Fuente primaria de cortes = gaps entre palabras (garantizan no partir
    palabra). Cada silencio detectado que cae dentro de un gap AFINA el punto
    de corte a su punto medio (corte más limpio). Silencios sin palabra
    alrededor (intro/outro) también se agregan si no caen dentro de palabra.
    """
    candidates = {}  # time -> pause

    def add(t, pause):
        t = round(max(0.0, min(duration, t)), 3)
        if t not in candidates or pause > candidates[t]:
            candidates[t] = pause

    # Gaps entre palabras consecutivas
    for a, b in zip(words, words[1:]):
        gap = b["start"] - a["end"]
        if gap >= min_silence:
            mid = (a["end"] + b["start"]) / 2.0
            pause = gap
            # ¿Hay un silencio detectado dentro del gap? -> afinar al medio
            for s_start, s_end in silences:
                if s_start >= a["end"] - 0.05 and s_end <= b["start"] + 0.05:
                    mid = (s_start + s_end) / 2.0
                    pause = max(pause, s_end - s_start)
                    break
            add(mid, pause)

    # Silencios que no quedaron asociados a un gap (p.ej. antes de la 1a palabra
    # o después de la última). Se aceptan si su punto medio no cae dentro de una
    # palabra.
    for s_start, s_end in silences:
        mid = (s_start + s_end) / 2.0
        if not inside_word(mid, words):
            add(mid, s_end - s_start)

    cuts = [Cut(t, p) for t, p in candidates.items()]
    cuts.sort(key=lambda c: c.time)
    return cuts


def inside_word(t, words):
    """True si t cae dentro del intervalo [start, end] de alguna palabra."""
    for w in words:
        if w["start"] < t < w["end"]:
            return True
    return False


def nearest_valid_cut(t, candidates, words):
    """Devuelve el corte candidato válido más cercano a t (para overrides)."""
    valid = [c for c in candidates if not inside_word(c.time, words)]
    if not valid:
        return None
    return min(valid, key=lambda c: abs(c.time - t))


# --------------------------------------------------------------------------- #
# 4) Algoritmo de cortes
# --------------------------------------------------------------------------- #
def score_cut(cut, lo, hi):
    """Mayor score = mejor. Combina pausa larga + cercanía al máximo."""
    span = max(hi - lo, 1e-6)
    closeness = 1.0 - (hi - cut.time) / span        # 1 = pegado al máximo
    pause_norm = min(cut.pause, 2.0) / 2.0           # satura a 2 s
    return PAUSE_WEIGHT * pause_norm + CLOSE_WEIGHT * closeness


def compute_cuts(candidates, duration, min_s, max_s):
    """Greedy: cubre [0, duration] con segmentos <= max, idealmente >= min."""
    times = [c.time for c in candidates]
    cut_times = [0.0]
    cur = 0.0
    forced = 0

    # Si el video entero entra en un clip, no hay nada que cortar
    while duration - cur > max_s + 1e-3:
        lo = cur + min_s
        hi = cur + max_s
        in_window = [c for c in candidates if lo < c.time <= hi]
        if in_window:
            chosen = max(in_window, key=lambda c: score_cut(c, lo, hi)).time
        else:
            below = [c for c in candidates if cur + 0.1 < c.time <= hi]
            if below:
                chosen = max(below)   # el más cercano al máximo
            else:
                chosen = hi           # forzado: una palabra cruza el máximo
                forced += 1
        cut_times.append(round(chosen, 3))
        cur = chosen
    cut_times.append(round(duration, 3))

    cut_times = rebalance_tail(cut_times, times, min_s, max_s)
    return cut_times, forced


def rebalance_tail(cut_times, cand_times, min_s, max_s):
    """Evita dejar una cola final < min moviendo el penúltimo corte."""
    if len(cut_times) < 3:
        return cut_times
    last_len = cut_times[-1] - cut_times[-2]
    if last_len >= min_s:
        return cut_times
    prev = cut_times[-3]
    end = cut_times[-1]
    # Buscar un corte que deje AMBOS segmentos válidos (>= min, <= max)
    lo = prev + min_s
    hi = min(prev + max_s, end - min_s)
    options = [t for t in cand_times if lo <= t <= hi]
    if options:
        # el que mejor balancea las dos duraciones finales
        target = (prev + end) / 2.0
        cut_times[-2] = round(min(options, key=lambda t: abs(t - target)), 3)
    else:
        warn(f"Cola final corta ({last_len:.2f}s < min {min_s}s) y no hay "
             "silencio para rebalancear; se deja como está.")
    return cut_times


def parse_manual_cuts(spec, duration):
    out = []
    for tok in spec.split(","):
        tok = tok.strip()
        if not tok:
            continue
        try:
            out.append(float(tok))
        except ValueError:
            raise ReelError(f"Valor de corte inválido en --cortes: '{tok}'")
    out = sorted(set(out))
    if out and out[0] > 0.0:
        out.insert(0, 0.0)
    if not out or out[-1] < duration - 1e-3:
        out.append(round(duration, 3))
    return out


def validate_manual_cuts(cut_times, words):
    for t in cut_times[1:-1]:
        if inside_word(t, words):
            offending = next(w for w in words if w["start"] < t < w["end"])
            warn(f"El corte manual en {t:.2f}s cae DENTRO de la palabra "
                 f"'{offending['word']}' [{offending['start']:.2f}"
                 f"-{offending['end']:.2f}]. Se respeta igual (override).")


# --------------------------------------------------------------------------- #
# Construcción de segmentos con texto y palabras relativas
# --------------------------------------------------------------------------- #
@dataclass
class Segment:
    index: int
    start: float
    end: float
    words: list = field(default_factory=list)

    @property
    def duration(self):
        return round(self.end - self.start, 3)

    @property
    def text(self):
        return " ".join(w["word"] for w in self.words).strip()


def build_segments(cut_times, words):
    segs = []
    for i in range(len(cut_times) - 1):
        s, e = cut_times[i], cut_times[i + 1]
        seg = Segment(index=i + 1, start=round(s, 3), end=round(e, 3))
        for w in words:
            center = (w["start"] + w["end"]) / 2.0
            if s <= center < e:
                seg.words.append({
                    "word": w["word"],
                    "start": round(w["start"] - s, 3),   # relativo al clip
                    "end": round(w["end"] - s, 3),
                })
        segs.append(seg)
    return segs


# --------------------------------------------------------------------------- #
# 5) Export de clips + reportes
# --------------------------------------------------------------------------- #
def export_clips(video_path, segments, fps, clips_dir, fade):
    info(f"Exportando {len(segments)} clips (re-encode frame-accurate)...")
    for seg in segments:
        name = f"seq_{seg.index:02d}_{seg.start:.2f}-{seg.end:.2f}s.mp4"
        out = os.path.join(clips_dir, name)
        dur = seg.duration
        cmd = [
            "ffmpeg", "-y",
            "-ss", f"{seg.start:.3f}",     # input seeking: resetea timestamps a 0
            "-i", video_path,             # (accurate con re-encode) y deja el
            "-t", f"{dur:.3f}",           # audio alineado, evitando que afade lo ataque
            "-c:v", "libx264", "-crf", "18", "-preset", "veryfast",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac", "-b:a", "160k",
        ]
        if fps > 0:
            cmd += ["-r", f"{fps}"]
        if fade > 0 and dur > 2 * fade:
            cmd += ["-af",
                    f"afade=t=in:st=0:d={fade},"
                    f"afade=t=out:st={dur - fade:.3f}:d={fade}"]
        cmd += [out]
        run(cmd)
        print(f"\r    {seg.index}/{len(segments)}  {name}", end="", flush=True)
    print()


def safe_write(fn, *args):
    """Ejecuta un writer de reporte; si el archivo está bloqueado, avisa y sigue.
    El último argumento es el path (todos los writers son (data..., path))."""
    path = args[-1]
    try:
        fn(*args)
    except PermissionError:
        warn(f"No se pudo escribir '{path}' (¿abierto en otro programa?). "
             "Se omite ese archivo; cerralo y volvé a correr si lo necesitás.")


def fmt_ts(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")


def write_srt(words, path):
    """SRT del video completo, una línea por palabra (sub-clip preciso)."""
    with open(path, "w", encoding="utf-8") as f:
        for i, w in enumerate(words, 1):
            f.write(f"{i}\n{fmt_ts(w['start'])} --> {fmt_ts(w['end'])}\n"
                    f"{w['word']}\n\n")


def write_txt(segments_text, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(s["text"] for s in segments_text if s["text"]))
        f.write("\n")


def write_words_csv(words, path):
    with open(path, "w", encoding="utf-8", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["word", "start", "end"])
        for w in words:
            wr.writerow([w["word"], w["start"], w["end"]])


def write_silences(silences, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Silencios detectados (posibles cortes)\n")
        f.write("# start_s\tend_s\tdur_s\tmedio_s\n")
        for s, e in silences:
            f.write(f"{s:.3f}\t{e:.3f}\t{e - s:.3f}\t{(s + e) / 2:.3f}\n")


def write_segments_json(segments, path):
    data = [{
        "index": seg.index,
        "start": seg.start,
        "end": seg.end,
        "duration": seg.duration,
        "text": seg.text,
        "words": seg.words,
    } for seg in segments]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def write_mapeo(segments, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Mapeo de clips\n\n")
        f.write("| Clip | Rango | Duración | Texto |\n")
        f.write("|------|-------|----------|-------|\n")
        for seg in segments:
            text = seg.text.replace("|", "\\|") or "_(sin texto)_"
            f.write(f"| seq_{seg.index:02d} | {seg.start:.2f}–{seg.end:.2f}s "
                    f"| {seg.duration:.2f}s | {text} |\n")


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def parse_args():
    p = argparse.ArgumentParser(
        description="Corta un video en reels en silencios, sin partir palabras, "
                    "con texto y word-timestamps por clip.")
    p.add_argument("video", help="Ruta al video (mp4/mov).")
    p.add_argument("--max", type=float, default=10.0,
                   help="Duración máxima por clip (s). Default 10.")
    p.add_argument("--min", type=float, default=4.0,
                   help="Duración mínima deseada por clip (s). Default 4.")
    p.add_argument("--noise", default="-32",
                   help="Umbral de silencio en dB para silencedetect. Default -32.")
    p.add_argument("--min-silence", type=float, default=0.16,
                   help="Duración mínima de silencio (s). Default 0.16.")
    p.add_argument("--cortes", default=None,
                   help='Override manual: "0,5.85,13.76,...". Solo se valida '
                        "que no partan palabras.")
    p.add_argument("--modelo", default="large-v3",
                   help="Modelo faster-whisper. Default large-v3 (fallback medium).")
    p.add_argument("--device", choices=["auto", "cpu", "cuda"], default="auto",
                   help="Dispositivo. Default auto (detecta GPU).")
    p.add_argument("--fade", type=float, default=0.008,
                   help="Micro-fade de audio en bordes (s) para evitar clicks. "
                        "Default 0.008. 0 = desactivado.")
    p.add_argument("--salida", default="salida",
                   help="Directorio de salida. Default 'salida'.")
    p.add_argument("--force", action="store_true",
                   help="Re-transcribir aunque exista caché.")
    return p.parse_args()


def main():
    args = parse_args()

    if not os.path.exists(args.video):
        die(f"No existe el archivo: {args.video}")
    if args.min >= args.max:
        die(f"--min ({args.min}) debe ser menor que --max ({args.max}).")

    try:
        check_ffmpeg()

        out_dir = args.salida
        clips_dir = os.path.join(out_dir, "clips")
        os.makedirs(clips_dir, exist_ok=True)
        wav_path = os.path.join(out_dir, "audio_16k.wav")
        transcript_json = os.path.join(out_dir, "transcript.json")

        meta = probe_video(args.video)
        info(f"Video: {meta['width']}x{meta['height']} @ {meta['fps']}fps, "
             f"{meta['duration']:.2f}s")
        duration = meta["duration"]

        extract_audio(args.video, wav_path)

        tr = transcribe(args.video, wav_path, transcript_json,
                        args.modelo, args.device, args.force)
        words = tr["words"]

        info("Detectando silencios (silencedetect)...")
        silences = detect_silences(wav_path, args.noise, args.min_silence)
        write_silences(silences, os.path.join(out_dir, "silencios.txt"))
        info(f"  {len(silences)} silencios detectados.")

        candidates = build_candidates(words, silences, duration, args.min_silence)

        # --- Calcular cortes -------------------------------------------------
        if args.cortes:
            cut_times = parse_manual_cuts(args.cortes, duration)
            validate_manual_cuts(cut_times, words)
            info(f"Usando cortes manuales: {len(cut_times) - 1} clips.")
        else:
            if not candidates and duration > args.max:
                warn("No hay silencios candidatos; se cortará por tiempo "
                     "(puede partir palabras).")
                # caer a una grilla regular por tiempo
                cut_times = [0.0]
                t = args.max
                while t < duration - 1e-3:
                    cut_times.append(round(t, 3))
                    t += args.max
                cut_times.append(round(duration, 3))
                forced = len(cut_times) - 2
            else:
                cut_times, forced = compute_cuts(
                    candidates, duration, args.min, args.max)
            if forced:
                warn(f"{forced} corte(s) forzado(s) por falta de silencio "
                     "dentro de la ventana.")

        segments = build_segments(cut_times, words)

        # --- Export (lo importante; no debe depender de un reporte bloqueado) -
        export_clips(args.video, segments, meta["fps"], clips_dir, args.fade)

        # --- Reportes (resilientes a archivos abiertos en otro programa) ------
        safe_write(write_segments_json, segments,
                   os.path.join(out_dir, "segments.json"))
        safe_write(write_mapeo, segments, os.path.join(out_dir, "mapeo_clips.md"))
        safe_write(write_srt, words, os.path.join(out_dir, "transcript.srt"))
        safe_write(write_txt, tr["segments"],
                   os.path.join(out_dir, "transcript.txt"))
        safe_write(write_words_csv, words, os.path.join(out_dir, "palabras.csv"))

        # --- Resumen ---------------------------------------------------------
        print()
        info(f"Listo. {len(segments)} clips en {clips_dir}")
        for seg in segments:
            flag = "" if args.min <= seg.duration <= args.max else "  <-- fuera de [min,max]"
            preview = (seg.text[:60] + "…") if len(seg.text) > 60 else seg.text
            print(f"    seq_{seg.index:02d}  {seg.start:6.2f}–{seg.end:6.2f}s "
                  f"({seg.duration:4.2f}s)  {preview}{flag}")
        print(f"\n    Mapeo:    {os.path.join(out_dir, 'mapeo_clips.md')}")
        print(f"    Timings:  {os.path.join(out_dir, 'segments.json')}")

    except ReelError as e:
        die(str(e))
    except KeyboardInterrupt:
        die("Cancelado por el usuario.")


if __name__ == "__main__":
    main()
