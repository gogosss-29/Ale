#!/usr/bin/env python3
"""Shim de compatibilidad: la implementación canónica de reel_cutter vive en
el plugin, en plugins/reel-cutter/skills/reel-cutter/scripts/reel_cutter.py.

Este archivo mantiene funcionando el comando documentado originalmente:
    python reel_cutter/reel_cutter.py video.mp4 --max 10 --min 4
"""
import os
import runpy
import sys

_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_SCRIPT = os.path.join(
    _REPO, "plugins", "reel-cutter", "skills", "reel-cutter", "scripts",
    "reel_cutter.py",
)

if not os.path.isfile(_SCRIPT):
    sys.exit(f"[reel_cutter] ERROR: no encuentro el script canónico en {_SCRIPT}")

sys.argv[0] = _SCRIPT
runpy.run_path(_SCRIPT, run_name="__main__")
