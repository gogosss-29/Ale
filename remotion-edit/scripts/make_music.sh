#!/usr/bin/env bash
set -e
cd "$(dirname "$0")/.."
mkdir -p /tmp/music_chords
OUT=public/music.mp3

# Progresión de acordes (Hz). Cada acorde = 3 sinusoides + sub-grave del fundamental.
# Am: 220 261.63 329.63 | F: 174.61 220 261.63 | C: 261.63 329.63 392.00 | G: 246.94 293.66 392.00
chords=(
  "220:261.63:329.63:110"
  "174.61:220:261.63:87.31"
  "261.63:329.63:392.00:130.81"
  "246.94:293.66:392.00:98.00"
)

i=0
for c in "${chords[@]}"; do
  IFS=':' read -r f1 f2 f3 sub <<< "$c"
  # Pad cálido: 3 voces + sub, envolvente suave con afade para evitar clicks
  ffmpeg -v error -y \
    -f lavfi -i "sine=frequency=$f1:duration=4" \
    -f lavfi -i "sine=frequency=$f2:duration=4" \
    -f lavfi -i "sine=frequency=$f3:duration=4" \
    -f lavfi -i "sine=frequency=$sub:duration=4" \
    -filter_complex "[0]volume=0.32[a];[1]volume=0.26[b];[2]volume=0.20[c];[3]volume=0.22[d];\
[a][b][c][d]amix=inputs=4:normalize=0,\
tremolo=f=5:d=0.18,\
lowpass=f=1100,\
afade=t=in:st=0:d=0.6,afade=t=out:st=3.4:d=0.6[out]" \
    -map "[out]" -ac 2 "/tmp/music_chords/chord_$i.wav"
  i=$((i+1))
done

# Concatenar la progresión (16s) y repetirla 4 veces (~64s)
printf "file '%s'\n" /tmp/music_chords/chord_0.wav /tmp/music_chords/chord_1.wav \
  /tmp/music_chords/chord_2.wav /tmp/music_chords/chord_3.wav > /tmp/music_chords/list.txt
ffmpeg -v error -y -f concat -safe 0 -i /tmp/music_chords/list.txt -c copy /tmp/music_chords/prog.wav

printf "file '%s'\n" /tmp/music_chords/prog.wav /tmp/music_chords/prog.wav \
  /tmp/music_chords/prog.wav /tmp/music_chords/prog.wav /tmp/music_chords/prog.wav > /tmp/music_chords/loop.txt
ffmpeg -v error -y -f concat -safe 0 -i /tmp/music_chords/loop.txt \
  -af "aecho=0.8:0.85:60:0.25,highpass=f=60,volume=0.9,afade=t=in:st=0:d=1.2" \
  -t 66 -ar 44100 -b:a 192k "$OUT"

echo "Música creada: $OUT"
ffprobe -v error -show_entries format=duration -of default=nk=1:nw=1 "$OUT"
