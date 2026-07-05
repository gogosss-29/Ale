"""Extractor de un curso/comunidad de Skool a Markdown organizado.

Fase 1: estructura + notas (desc) + recursos + links de vídeo de cada lección.
Salida en docs-skool/<community>/ (texto, se versiona) y un videos.jsonl con los
links para la Fase 2 (transcripciones).

Uso:
    SKOOL_COOKIE_FILE=/tmp/skool_cookie.txt \
        python -m skool.extract imperio --out docs-skool
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from pathlib import Path

from .api import SkoolClient, iter_tree
from .prosemirror import desc_to_markdown


def slug(text: str, maxlen: int = 50) -> str:
    text = text or "sin-titulo"
    text = "".join(
        c for c in unicodedata.normalize("NFKD", text) if not unicodedata.combining(c)
    )
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    text = re.sub(r"[\s_-]+", "-", text)
    return (text[:maxlen].strip("-")) or "x"


def parse_resources(raw: str | None) -> list[dict]:
    if not raw:
        return []
    try:
        data = json.loads(raw)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, TypeError):
        return []


def lesson_markdown(meta: dict, path_titles: list[str]) -> str:
    title = meta.get("title", "Sin título")
    lines = [f"# {title}", ""]
    lines.append(f"> Ruta: {' › '.join(path_titles)}")
    vid = meta.get("videoLink")
    if vid:
        ms = meta.get("videoLenMs", 0) or 0
        mins = round(ms / 60000, 1) if ms else "?"
        lines += ["", f"**🎬 Vídeo ({mins} min):** {vid}"]
    res = parse_resources(meta.get("resources"))
    if res:
        lines += ["", "**📎 Recursos:**"]
        for r in res:
            label = r.get("label") or r.get("title") or r.get("name") or r.get("url", "recurso")
            url = r.get("url") or r.get("link") or ""
            lines.append(f"- [{label}]({url})" if url else f"- {label}")
    body = desc_to_markdown(meta.get("desc"))
    if body:
        lines += ["", "---", "", body]
    return "\n".join(lines) + "\n"


def run(community: str, out_dir: str) -> None:
    client = SkoolClient(community)
    base = Path(out_dir) / community
    base.mkdir(parents=True, exist_ok=True)
    courses = client.list_courses()
    print(f"build={client.build}  cursos={len(courses)}")

    structure: list[dict] = []
    videos_fh = (base / "videos.jsonl").open("w", encoding="utf-8")
    index_lines = [f"# Índice — comunidad «{community}»", ""]
    total = 0

    for ci, co in enumerate(courses, 1):
        ctitle = co["metadata"].get("title") or co.get("name") or co["id"]
        try:
            short, first = client.resolve_course(co["id"])
            tree = client.course_view(short, first)
        except Exception as e:  # noqa: BLE001
            print(f"  !! curso {ctitle!r}: {e}")
            continue
        cdir = base / f"{ci:02d}-{slug(ctitle)}"
        cdir.mkdir(exist_ok=True)
        index_lines.append(f"\n## {ci:02d}. {ctitle}")
        course_entry = {"id": co["id"], "short": short, "title": ctitle, "lecciones": []}

        nodes = [n for _d, n in iter_tree(tree)]
        lessons = [n for n in nodes if n.get("unitType") == "module"]
        print(f"  [{ci:02d}/{len(courses)}] {ctitle[:38]:40} {len(lessons)} lecciones")

        for li, node in enumerate(lessons, 1):
            lid = node["id"]
            ltitle = node["metadata"].get("title") or node.get("name") or lid
            try:
                meta = client.lesson_meta(short, lid)
            except Exception as e:  # noqa: BLE001
                print(f"      !! lección {ltitle!r}: {e}")
                meta = node.get("metadata", {})
            fname = f"{li:03d}-{slug(ltitle)}.md"
            (cdir / fname).write_text(
                lesson_markdown({**node.get("metadata", {}), **meta}, [ctitle, ltitle]),
                encoding="utf-8",
            )
            vid = meta.get("videoLink") or node["metadata"].get("videoLink")
            if vid:
                videos_fh.write(
                    json.dumps(
                        {
                            "course": ctitle,
                            "lesson": ltitle,
                            "lesson_id": lid,
                            "video": vid,
                            "len_ms": meta.get("videoLenMs", 0),
                            "file": str((cdir / fname).relative_to(base)),
                        },
                        ensure_ascii=False,
                    )
                    + "\n"
                )
            index_lines.append(f"- [{ltitle}]({cdir.name}/{fname})")
            course_entry["lecciones"].append(
                {"id": lid, "title": ltitle, "video": vid, "file": str((cdir / fname).relative_to(base))}
            )
            total += 1
        structure.append(course_entry)

    videos_fh.close()
    (base / "estructura.json").write_text(
        json.dumps(structure, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (base / "INDICE.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    print(f"\nOK — {total} lecciones escritas en {base}")


def main() -> None:
    ap = argparse.ArgumentParser(description="Extractor de Skool (Fase 1)")
    ap.add_argument("community", help="slug de la comunidad, p.ej. imperio")
    ap.add_argument("--out", default="docs-skool", help="directorio de salida")
    args = ap.parse_args()
    run(args.community, args.out)


if __name__ == "__main__":
    main()
