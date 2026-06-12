"""Tests del filtro de realismo ffmpeg + ensamblado real con ffmpeg sintético."""
import sys, os, subprocess, shutil, tempfile
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from avatarhype.assembly.realism_grade import build_eq_filter, build_full_vf
from avatarhype.assembly.compositor import ensamblar, ffmpeg_disponible


def test_filtro_contiene_componentes():
    vf = build_full_vf()
    assert "colortemperature" in vf
    assert "eq=" in vf and "contrast=" in vf and "saturation=" in vf
    assert "colorbalance" in vf
    assert "noise=" in vf  # grano / partículas


def test_valores_curso_mapeados():
    # contraste +12 -> >1.0 ; saturación -6 -> <1.0
    vf = build_eq_filter()
    import re
    contrast = float(re.search(r"contrast=([0-9.]+)", vf).group(1))
    saturation = float(re.search(r"saturation=([0-9.]+)", vf).group(1))
    assert contrast > 1.0
    assert saturation < 1.0


def test_ensamblado_real_ffmpeg():
    """Genera 2 clips de color sintéticos y los ensambla -> valida el pipeline ffmpeg."""
    if not ffmpeg_disponible():
        print("SKIP: ffmpeg no disponible"); return
    tmp = tempfile.mkdtemp(prefix="avhype_test_")
    try:
        clips = []
        for i, color in enumerate(["red", "blue"]):
            c = os.path.join(tmp, f"c{i}.mp4")
            subprocess.run([
                "ffmpeg", "-y", "-f", "lavfi",
                "-i", f"color=c={color}:s=320x568:d=1:r=30",
                "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
                "-shortest", "-c:v", "libx264", "-c:a", "aac", c,
            ], capture_output=True, check=True)
            clips.append(c)
        out = os.path.join(tmp, "anuncio.mp4")
        ensamblar(clips, out, grano=False)
        assert os.path.exists(out) and os.path.getsize(out) > 0
        # verificar que es un mp4 válido con ffprobe
        probe = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", out], capture_output=True, text=True)
        assert probe.returncode == 0, probe.stderr
        print(f"  anuncio ensamblado: {out} dur={probe.stdout.strip()}s")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn(); print(f"PASS {name}")
    print("OK")
