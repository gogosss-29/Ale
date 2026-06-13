"""Fase 2: transcripciones de los vídeos de las lecciones (YouTube + Loom).

Lee docs-skool/<community>/videos.jsonl y, para cada vídeo, baja SOLO los
subtítulos (no el vídeo) con yt-dlp, los limpia a texto plano y los añade al
fichero .md de la lección bajo una sección "🎙️ Transcripción". Resumible.

Requiere: yt-dlp instalado. El entorno usa un CA propio → --no-check-certificates.

Uso:
    python -m skool.transcripts imperio --out docs-skool
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import tempfile
from pathlib import Path

MARK = "## 🎙️ Transcripción"
SUB_LANGS = "es,es-419,es-ES,en,en-US"


def vtt_to_text(vtt: str) -> str:
    lines: list[str] = []
    last = None
    for raw in vtt.splitlines():
        ln = raw.strip()
        if (
            not ln
            or ln == "WEBVTT"
            or ln.isdigit()
            or "-->" in ln
            or ln.startswith(("Kind:", "Language:", "NOTE"))
        ):
            continue
        ln = re.sub(r"<[^>]+>", "", ln)  # quita <v 0>, <c>, timestamps inline
        ln = ln.replace("&nbsp;", " ").strip()
        if ln and ln != last:
            lines.append(ln)
            last = ln
    # une en párrafos legibles
    text = " ".join(lines)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fetch_subs(url: str, workdir: Path, cookies_browser: str | None = None) -> str | None:
    """Devuelve el texto del subtítulo (es preferente) o None.

    cookies_browser: p.ej. "chrome"/"firefox" → pasa --cookies-from-browser a
    yt-dlp. Útil en local para YouTube (esquiva el "confirm you're not a bot").
    """
    out = workdir / "s"
    cmd = [
        "yt-dlp", "--no-check-certificates", "--skip-download",
        "--write-subs", "--write-auto-subs",
        "--sub-langs", SUB_LANGS, "--sub-format", "vtt",
        "-o", f"{out}.%(ext)s", url,
    ]
    if cookies_browser:
        cmd[1:1] = ["--cookies-from-browser", cookies_browser]
    subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    vtts = sorted(workdir.glob("*.vtt"))
    if not vtts:
        return None
    # prioriza español
    vtts.sort(key=lambda p: (0 if ".es" in p.name else 1, len(p.name)))
    text = vtt_to_text(vtts[0].read_text(encoding="utf-8", errors="ignore"))
    return text or None


def append_transcript(md_path: Path, text: str) -> None:
    content = md_path.read_text(encoding="utf-8")
    if MARK in content:
        content = content.split(MARK)[0].rstrip() + "\n"
    md_path.write_text(content + f"\n{MARK}\n\n{text}\n", encoding="utf-8")


def run(
    community: str,
    out_dir: str,
    limit: int | None = None,
    hosts: list[str] | None = None,
    cookies_browser: str | None = None,
) -> None:
    base = Path(out_dir) / community
    videos = [
        json.loads(l) for l in (base / "videos.jsonl").read_text().splitlines() if l.strip()
    ]
    if hosts:
        videos = [v for v in videos if any(h in v["video"] for h in hosts)]
    if limit:
        videos = videos[:limit]
    done = ok = 0
    for v in videos:
        md_path = base / v["file"]
        if not md_path.exists():
            continue
        if MARK in md_path.read_text(encoding="utf-8"):
            ok += 1
            continue  # ya transcrita (resumible)
        with tempfile.TemporaryDirectory() as td:
            try:
                text = fetch_subs(v["video"], Path(td), cookies_browser)
            except Exception as e:  # noqa: BLE001
                print(f"  !! {v['lesson'][:40]}: {e}")
                text = None
        done += 1
        if text:
            append_transcript(md_path, text)
            ok += 1
            print(f"  [{done}/{len(videos)}] ✓ {v['course'][:20]} › {v['lesson'][:35]} ({len(text)} ch)")
        else:
            print(f"  [{done}/{len(videos)}] ∅ sin subs: {v['lesson'][:40]} {v['video']}")
    print(f"\nTranscripciones OK: {ok}/{len(videos)}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Skool transcripciones (Fase 2)")
    ap.add_argument("community")
    ap.add_argument("--out", default="docs-skool")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument(
        "--hosts",
        default=None,
        help="filtra por host de vídeo, coma-separado. p.ej. 'loom.com' o 'youtube,youtu.be'",
    )
    ap.add_argument(
        "--cookies-from-browser",
        dest="cookies_browser",
        default=None,
        help="navegador para sacar cookies (chrome/firefox/edge). Útil en local para YouTube.",
    )
    args = ap.parse_args()
    hosts = [h.strip() for h in args.hosts.split(",")] if args.hosts else None
    run(args.community, args.out, args.limit, hosts, args.cookies_browser)


if __name__ == "__main__":
    main()
