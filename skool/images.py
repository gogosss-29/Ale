"""Archiva las imágenes ESTÁTICAS embebidas en las notas (capturas/diagramas) en local
y reescribe sus enlaces. Los GIF (grabaciones de pantalla, muy pesados y que una IA no
procesa bien) NO se descargan: se dejan como URL original.

- Captura todas las variantes de URL `assets.skool.com` (con/sin extensión, `-md/-sm`).
- Salta `.gif` (deja el enlace remoto).
- Descarga el resto; si resultan GIF por magic bytes, también se dejan como enlace.
- Reescala las estáticas a máx 1600px y las guarda en `imagenes/` (peso contenido).
- Reescribe en los .md solo los enlaces de las imágenes guardadas en local. Resumible.

Uso: SKOOL_COOKIE_FILE=/tmp/skool_cookie.txt python -m skool.images imperio --out docs-skool
"""
from __future__ import annotations

import argparse
import io
import re
from pathlib import Path

from PIL import Image

from .session import SkoolSession

URL_RX = re.compile(r"https://assets\.skool\.com/f/[^\s)\"'<>]+")
MAX_DIM = 1600


def _name_for(url: str) -> str:
    seg = url.rsplit("/", 1)[1].split("?")[0]
    return re.sub(r"[^A-Za-z0-9._-]", "_", seg)


def run(community: str, out_dir: str) -> None:
    base = Path(out_dir) / community
    imgdir = base / "imagenes"
    imgdir.mkdir(parents=True, exist_ok=True)
    s = SkoolSession()
    mds = [p for p in base.rglob("*.md") if "/recursos/" not in str(p)]

    urls: set[str] = set()
    for p in mds:
        urls.update(u.rstrip(".,);") for u in URL_RX.findall(p.read_text(encoding="utf-8")))

    url2local: dict[str, str] = {}
    saved = skipped_gif = err = 0
    for i, u in enumerate(sorted(urls), 1):
        if u.lower().split("?")[0].endswith(".gif"):
            skipped_gif += 1
            continue
        name = _name_for(u)
        # destino con extensión correcta (se ajusta tras conocer el formato)
        try:
            existing = list(imgdir.glob(Path(name).stem + ".*"))
            if existing:
                url2local[u] = existing[0].name
                continue
            r = s.s.get(u, timeout=60)
            r.raise_for_status()
            data = r.content
            if data[:4] == b"GIF8":  # GIF sin extensión en la URL → dejar enlace
                skipped_gif += 1
                continue
            img = Image.open(io.BytesIO(data))
            fmt = (img.format or "PNG").upper()
            ext = {"JPEG": "jpg", "PNG": "png", "WEBP": "webp"}.get(fmt, "png")
            if max(img.size) > MAX_DIM:
                img.thumbnail((MAX_DIM, MAX_DIM))
            stem = Path(name).stem
            dest = imgdir / f"{stem}.{ext}"
            save_kw = {"optimize": True}
            if ext == "jpg":
                img = img.convert("RGB")
                save_kw["quality"] = 85
            img.save(dest, **save_kw)
            url2local[u] = dest.name
            saved += 1
            if saved % 50 == 0:
                print(f"  {i}/{len(urls)} procesadas… ({saved} guardadas)")
        except Exception as e:  # noqa: BLE001
            err += 1
            print(f"  !! {u[-40:]}: {e}")
    print(f"capturas guardadas {saved}, GIFs dejados como enlace {skipped_gif}, errores {err}")

    rewritten = 0
    for p in mds:
        txt = p.read_text(encoding="utf-8")
        new = txt
        depth = len(p.relative_to(base).parts) - 1
        prefix = "../" * depth + "imagenes/"
        for u, name in url2local.items():
            if u in new:
                new = new.replace(u, prefix + name)
        if new != txt:
            p.write_text(new, encoding="utf-8")
            rewritten += 1
    sz = sum(f.stat().st_size for f in imgdir.glob("*")) / 1048576
    print(f"reescritos {rewritten} .md | tamaño imagenes/: {sz:.0f} MB")


def main() -> None:
    ap = argparse.ArgumentParser(description="Archiva imágenes estáticas de Skool")
    ap.add_argument("community")
    ap.add_argument("--out", default="docs-skool")
    args = ap.parse_args()
    run(args.community, args.out)


if __name__ == "__main__":
    main()
