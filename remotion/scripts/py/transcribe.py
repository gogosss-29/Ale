#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Transcribe un video a nivel de palabra (faster-whisper) -> words.json.
Uso: python transcribe.py <video> <out.json> [modelo] [idioma]
Cachea por (ruta,tam,mtime,modelo). Requiere ffmpeg + faster-whisper."""
import json, os, sys

def cache_key(path, model):
    st = os.stat(path)
    return f"{os.path.abspath(path)}|{st.st_size}|{int(st.st_mtime)}|{model}"

def main():
    video, out = sys.argv[1], sys.argv[2]
    model = sys.argv[3] if len(sys.argv) > 3 else "medium"
    lang = sys.argv[4] if len(sys.argv) > 4 else "es"
    key = cache_key(video, model)
    if os.path.exists(out):
        try:
            if json.load(open(out)).get("_cache_key") == key:
                print("cache hit"); return
        except Exception:
            pass
    from faster_whisper import WhisperModel
    m = WhisperModel(model, device="cpu", compute_type="int8")
    segs, info = m.transcribe(video, language=lang, word_timestamps=True, beam_size=5)
    words, seg_texts = [], []
    for s in segs:
        seg_texts.append({"start": round(s.start, 3), "end": round(s.end, 3), "text": s.text.strip()})
        for w in (s.words or []):
            t = w.word.strip()
            if t:
                words.append({"word": t, "start": round(w.start, 3), "end": round(w.end, 3)})
    json.dump({"_cache_key": key, "duration": round(info.duration, 3), "words": words, "segments": seg_texts},
              open(out, "w"), ensure_ascii=False, indent=1)
    print(f"OK {len(words)} palabras, {round(info.duration,1)}s")

if __name__ == "__main__":
    main()
