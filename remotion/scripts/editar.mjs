#!/usr/bin/env node
// ─── editar.mjs · CLI del sistema de edición ────────────────────────────────
// Convierte un video crudo + una "receta" en un video editado, end-to-end.
//   node scripts/editar.mjs <video.mp4> <receta.json> [--out out.mp4] [--no-render]
//
// La receta declara "beats" ubicados por FRASE (o por segundo). El CLI:
//   1. copia el video a public/clips/  2. transcribe (whisper, cacheado)
//   3. arma captions  4. resuelve tiempos de cada beat por frase
//   5. segmenta la persona en las ventanas "detrás"  6. rinde con Remotion.
//
// Receta (JSON):
// {
//   "brand": "CEREBRO", "captionPreset": "marca", "lang": "es", "model": "medium",
//   "beats": [
//     {"kind":"overlay","type":"topLabel","atSec":0,"dur":4.5,"props":{"text":"Fondo Beltrán Briones"}},
//     {"kind":"overlay","type":"numberCallout","at":"juntó 45 millones","dur":3.4,"props":{"prefix":"US$","value":45,"suffix":"MILLONES"}},
//     {"kind":"overlay","type":"chip","at":"cada tres meses","lead":0.4,"dur":3.2,"props":{"text":"CADA 3 MESES","sub":"Alquileres"}},
//     {"kind":"behind","graphic":"risingLine","at":"suban de valor","dur":3.7,"props":{"curva":"ancha"}}
//   ]
// }
import {execFileSync, spawnSync} from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, '..'); // remotion/
const PUB = path.join(ROOT, 'public');
const CACHE = path.join(ROOT, 'out', 'edit-cache');
const BROWSER = ['--browser-executable=/opt/pw-browsers/chromium', '--chrome-mode=chrome-for-testing'];

const log = (m) => console.log(`[editar] ${m}`);
const die = (m) => {
  console.error(`\n[editar] ERROR: ${m}\n`);
  process.exit(1);
};
const norm = (s) =>
  s
    .toLowerCase()
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9ñ ]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();

function parseArgs() {
  const a = process.argv.slice(2);
  if (a.length < 2) die('uso: node scripts/editar.mjs <video.mp4> <receta.json> [--out out.mp4] [--no-render]');
  const [video, receta] = a;
  const out = a.includes('--out') ? a[a.indexOf('--out') + 1] : null;
  return {video, receta, out, render: !a.includes('--no-render')};
}

function ffprobeMeta(video) {
  const j = JSON.parse(
    execFileSync('ffprobe', ['-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=r_frame_rate:format=duration', '-of', 'json', video], {encoding: 'utf8'}),
  );
  const [n, d] = (j.streams?.[0]?.r_frame_rate || '30/1').split('/');
  return {durationSec: parseFloat(j.format.duration), srcFps: d ? +n / +d : 30};
}

// localiza la primera aparición de una frase en la lista de palabras
function findPhrase(words, phrase) {
  const tks = norm(phrase).split(' ').filter(Boolean);
  const W = words.map((w) => norm(w.word));
  for (let i = 0; i + tks.length <= W.length; i++) {
    let ok = true;
    for (let j = 0; j < tks.length; j++) if (W[i + j] !== tks[j]) {ok = false; break;}
    if (ok) return {startSec: words[i].start, endSec: words[i + tks.length - 1].end};
  }
  return null;
}

function buildPages(words, n = 3) {
  const pages = [];
  for (let i = 0; i < words.length; i += n) {
    const g = words.slice(i, i + n);
    pages.push({
      startMs: Math.round(g[0].start * 1000),
      endMs: Math.round(g[g.length - 1].end * 1000),
      tokens: g.map((x) => ({text: x.word.trim().replace(/^[¿¡]|[,.;:?!]+$/g, '').toUpperCase(), fromMs: Math.round(x.start * 1000), toMs: Math.round(x.end * 1000)})),
    });
  }
  return pages;
}

function main() {
  const {video, receta, out, render} = parseArgs();
  if (!fs.existsSync(video)) die(`no existe el video: ${video}`);
  if (!fs.existsSync(receta)) die(`no existe la receta: ${receta}`);
  const R = JSON.parse(fs.readFileSync(receta, 'utf8'));
  const fps = R.fps ?? 30;
  fs.mkdirSync(CACHE, {recursive: true});
  fs.mkdirSync(path.join(PUB, 'clips'), {recursive: true});

  // 1 · copiar video a public/clips
  const base = path.basename(video).replace(/[^\w.-]/g, '_');
  const slug = base.replace(/\.[^.]+$/, '');
  fs.copyFileSync(video, path.join(PUB, 'clips', base));
  const videoSrc = `clips/${base}`;
  const meta = ffprobeMeta(video);
  log(`video: ${base} · ${meta.durationSec.toFixed(1)}s @ ${meta.srcFps}fps → timeline ${fps}fps`);

  // 2 · transcribir (cacheado)
  const wordsJson = path.join(CACHE, `${slug}.words.json`);
  log('transcribiendo (whisper)…');
  const tr = spawnSync('python3', [path.join(HERE, 'py', 'transcribe.py'), video, wordsJson, R.model ?? 'medium', R.lang ?? 'es'], {stdio: 'inherit'});
  if (tr.status !== 0) die('falló la transcripción (¿faster-whisper + ffmpeg instalados?)');
  const {words, duration} = JSON.parse(fs.readFileSync(wordsJson, 'utf8'));

  // 3 · captions
  const pages = buildPages(words, R.captionWords ?? 3);

  // 4+5 · resolver beats
  const overlays = [];
  const behind = [];
  let bi = 0;
  for (const beat of R.beats ?? []) {
    let startSec = beat.atSec;
    if (startSec == null && beat.at) {
      const f = findPhrase(words, beat.at);
      if (!f) {log(`⚠️  frase no encontrada: "${beat.at}" (se omite el beat)`); continue;}
      startSec = f.startSec;
    }
    if (startSec == null) {log('⚠️  beat sin at/atSec (se omite)'); continue;}
    startSec = Math.max(0, startSec - (beat.lead ?? 0));

    if (beat.kind === 'overlay') {
      overlays.push({type: beat.type, fromSec: +startSec.toFixed(3), durSec: beat.dur ?? 3, props: beat.props ?? {}});
    } else if (beat.kind === 'behind') {
      const fromFrame = Math.round(startSec * fps);
      const frames = Math.round((beat.dur ?? 3.5) * fps);
      const personDir = `edit-person/${slug}-${bi}`;
      const dstAbs = path.join(PUB, personDir);
      log(`segmentando ventana "${beat.at ?? startSec}" → ${frames} cuadros…`);
      // extraer cuadros
      const tmp = path.join(CACHE, `frames-${slug}-${bi}`);
      fs.rmSync(tmp, {recursive: true, force: true});
      fs.mkdirSync(tmp, {recursive: true});
      const ex = spawnSync('ffmpeg', ['-y', '-i', video, '-ss', String(startSec), '-t', String(beat.dur ?? 3.5), '-r', String(fps), '-start_number', String(fromFrame), path.join(tmp, 'f-%04d.png')], {stdio: 'ignore'});
      if (ex.status !== 0) die('ffmpeg falló extrayendo cuadros');
      // segmentar
      fs.rmSync(dstAbs, {recursive: true, force: true});
      const sg = spawnSync('python3', [path.join(HERE, 'py', 'segment.py'), tmp, dstAbs], {stdio: 'inherit'});
      if (sg.status !== 0) die('falló la segmentación (¿rembg + modelo u2net_human_seg?)');
      behind.push({graphic: beat.graphic ?? 'risingLine', fromFrame, frames, personDir, props: beat.props ?? {}});
    }
    bi++;
  }

  // 6 · EditMap final
  const editMap = {
    videoSrc,
    durationMs: Math.round(duration * 1000),
    fps,
    brand: R.brand ?? 'CEREBRO',
    showBrandBug: R.showBrandBug ?? true,
    captionPreset: R.captionPreset ?? 'marca',
    pages,
    overlays,
    behind,
  };
  const propsPath = path.join(CACHE, `${slug}.props.json`);
  fs.writeFileSync(propsPath, JSON.stringify(editMap));
  log(`EditMap: ${overlays.length} overlays · ${behind.length} capas "detrás" · ${pages.length} páginas de captions`);
  log(`props → ${path.relative(ROOT, propsPath)}`);

  // 7 · render
  const outPath = out ?? path.join(ROOT, 'out', `${slug}-editado.mp4`);
  if (!render) {log('--no-render: listo (props escritas, sin renderizar)'); return;}
  fs.mkdirSync(path.dirname(outPath), {recursive: true});
  log(`renderizando → ${outPath} …`);
  const rd = spawnSync('npx', ['remotion', 'render', 'src/index.ts', 'EditedVideo', outPath, `--props=${propsPath}`, ...BROWSER, '--timeout=90000', '--log=error'], {stdio: 'inherit', cwd: ROOT});
  if (rd.status !== 0) die('falló el render de Remotion');
  log(`✅ listo: ${outPath}`);
}

main();
