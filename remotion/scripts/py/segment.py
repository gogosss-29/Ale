#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recorta la persona de cada cuadro (rembg u2net_human_seg) -> PNG con alpha.
Uso: python segment.py <dir_src> <dir_dst>
Genera, por cada f-*.png de src, un recorte con fondo transparente en dst.
El modelo u2net_human_seg vive en ~/.u2net (si falta, rembg lo descarga)."""
import glob, os, sys

def main():
    src, dst = sys.argv[1], sys.argv[2]
    os.makedirs(dst, exist_ok=True)
    from rembg import remove, new_session
    from PIL import Image
    sess = new_session("u2net_human_seg")
    files = sorted(glob.glob(os.path.join(src, "*.png")))
    for i, f in enumerate(files):
        out = remove(Image.open(f).convert("RGBA"), session=sess)
        out.save(os.path.join(dst, os.path.basename(f)))
        if i % 20 == 0:
            print(f"  {i+1}/{len(files)}", flush=True)
    print(f"OK {len(files)} recortes")

if __name__ == "__main__":
    main()
