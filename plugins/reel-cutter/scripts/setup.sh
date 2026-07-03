#!/usr/bin/env bash
# SessionStart hook del plugin reel-cutter.
# Comprueba dependencias (ffmpeg + faster-whisper). En sesiones remotas
# (contenedor efímero) lanza la instalación en segundo plano para no
# bloquear el arranque. En local solo informa, no toca el sistema.
set -u

DATA_DIR="${CLAUDE_PLUGIN_DATA:-$HOME/.reel-cutter}"
LOG="$DATA_DIR/setup.log"
mkdir -p "$DATA_DIR" 2>/dev/null || true

have_ffmpeg() { command -v ffmpeg >/dev/null 2>&1 && command -v ffprobe >/dev/null 2>&1; }
have_fw() { python3 -c "import faster_whisper" >/dev/null 2>&1; }

if have_ffmpeg && have_fw; then
  echo "reel-cutter: dependencias OK (ffmpeg + faster-whisper)."
  exit 0
fi

MISSING=""
have_ffmpeg || MISSING="ffmpeg"
have_fw || MISSING="$MISSING faster-whisper"

if [ "${CLAUDE_CODE_REMOTE:-}" = "true" ]; then
  # Entorno remoto/efímero: instalar en background (no bloquear la sesión).
  nohup bash -c '
    if ! command -v ffmpeg >/dev/null 2>&1; then
      (apt-get update -qq && apt-get install -y -qq ffmpeg) || sudo apt-get install -y -qq ffmpeg
    fi
    python3 -c "import faster_whisper" 2>/dev/null || pip3 install -q faster-whisper
    echo "done $(date -Is)"
  ' >>"$LOG" 2>&1 &
  echo "reel-cutter: instalando en segundo plano:$MISSING (log: $LOG)." \
       "Antes de usar la skill, verificar con: command -v ffmpeg && python3 -c 'import faster_whisper'"
else
  echo "reel-cutter: faltan dependencias:$MISSING." \
       "Instalar con: apt/brew install ffmpeg && pip install faster-whisper"
fi
exit 0
