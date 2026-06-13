"""Descarga TODOS los adjuntos descargables del classroom de Skool.

Los recursos de cada lección son `{title, file_id, file_name, file_content_type}`
(archivos: skills .zip/.tar.gz, plantillas n8n/Make .json, bases Airtable, etc.) o
`{title, link}` (enlaces externos). Los archivos se sirven firmados; se obtienen con
`SkoolClient.download_resource` (POST /files/<id>/download-url).

Recorre estructura.json, re-pide cada lección para leer sus `resources`, descarga los
archivos a docs-skool/<community>/recursos/<NN-curso>/ y registra los enlaces y un
manifest. Resumible (salta lo ya descargado) y educado con el WAF (pausa + backoff 403).

Uso:
    SKOOL_COOKIE_FILE=/tmp/skool_cookie.txt \
        python -m skool.resources imperio --out docs-skool
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from .api import SkoolClient
from .extract import parse_resources, slug


def _meta_with_retry(client: SkoolClient, short: str, lid: str, tries: int = 8) -> dict | None:
    """lesson_meta con backoff largo ante 403 del WAF. Devuelve None si no se logra."""
    for i in range(tries):
        try:
            return client.lesson_meta(short, lid)
        except Exception as e:  # noqa: BLE001
            if "403" in str(e):
                time.sleep(min(60, 10 * (i + 1)))  # 10,20,30,40,50,60,60,60s — deja enfriar al WAF
                continue
            if i < tries - 1:
                time.sleep(2 ** i)
                continue
            return None
    return None


def run(community: str, out_dir: str, pace: float = 0.7, start: int = 1) -> None:
    base = Path(out_dir) / community
    rdir = base / "recursos"
    rdir.mkdir(parents=True, exist_ok=True)
    struct = json.loads((base / "estructura.json").read_text())
    client = SkoolClient(community)
    client.s.pause = pace

    manifest: list[dict] = []
    links: list[dict] = []
    n_files = n_dl = n_skip = n_links = n_err = 0

    # cargar manifest previo si existe (para no perder lo ya registrado al reanudar)
    mpath = rdir / "resources-manifest.json"
    if mpath.exists():
        try:
            prev = json.loads(mpath.read_text())
            manifest.extend(prev.get("files", []))
            links.extend(prev.get("links", []))
        except Exception:  # noqa: BLE001
            pass

    for ci, co in enumerate(struct, 1):
        if ci < start:
            continue
        short = co["short"]
        cslug = f"{ci:02d}-{slug(co['title'])}"
        for les in co["lecciones"]:
            meta = _meta_with_retry(client, short, les["id"])
            if meta is None:
                n_err += 1
                print(f"  !! {cslug} | lección sin acceso (WAF): {les['title'][:40]}")
                continue
            res = parse_resources(meta.get("resources"))
            if not res:
                continue
            for r in res:
                fid = r.get("file_id")
                fname = r.get("file_name") or r.get("title") or fid
                if not fid:
                    link = r.get("link") or r.get("url")
                    if link:
                        links.append({"course": co["title"], "lesson": les["title"],
                                      "title": r.get("title"), "link": link})
                        n_links += 1
                    continue
                n_files += 1
                safe = f"{slug(les['title'],40)}__{fname}".replace("/", "_")
                dest = rdir / cslug / safe
                rel = str(dest.relative_to(base))
                entry = {"course": co["title"], "lesson": les["title"],
                         "file_id": fid, "file_name": fname, "path": rel}
                if dest.exists() and dest.stat().st_size > 0:
                    n_skip += 1
                    manifest.append(entry)
                    continue
                try:
                    client.download_resource(fid, str(dest))
                    sz = dest.stat().st_size
                    n_dl += 1
                    manifest.append(entry)
                    print(f"  ✓ {cslug} | {fname} ({sz//1024} KB)")
                except Exception as e:  # noqa: BLE001
                    n_err += 1
                    entry["error"] = str(e)[:120]
                    manifest.append(entry)
                    print(f"  !! {cslug} | {fname}: {e}")

    (rdir / "resources-manifest.json").write_text(
        json.dumps({"files": manifest, "links": links}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(
        f"\nArchivos: {n_files} (descargados {n_dl}, ya estaban {n_skip}, errores {n_err}) "
        f"| enlaces externos: {n_links}"
    )


def main() -> None:
    ap = argparse.ArgumentParser(description="Descarga adjuntos de Skool")
    ap.add_argument("community")
    ap.add_argument("--out", default="docs-skool")
    ap.add_argument("--pace", type=float, default=0.7)
    ap.add_argument("--start", type=int, default=1, help="empezar en el curso N (1-based)")
    args = ap.parse_args()
    run(args.community, args.out, args.pace, args.start)


if __name__ == "__main__":
    main()
