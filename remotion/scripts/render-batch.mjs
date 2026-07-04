#!/usr/bin/env node
// Render batch: todos los b-rolls de un reel con un solo comando.
// Uso: node scripts/render-batch.mjs reels/reel-003.json
import {execSync} from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';

const cfgPath = process.argv[2];
if (!cfgPath) {
  console.error('Uso: node scripts/render-batch.mjs <config.json>');
  process.exit(1);
}
const cfg = JSON.parse(fs.readFileSync(cfgPath, 'utf8'));
const outDir = path.join('out', cfg.reel);
fs.mkdirSync(outDir, {recursive: true});

const BROWSER =
  process.env.REMOTION_BROWSER === 'default'
    ? ''
    : '--browser-executable=/opt/pw-browsers/chromium --chrome-mode=chrome-for-testing';

for (const job of cfg.jobs) {
  const propsFile = path.join(outDir, `.props-${job.out}.json`);
  fs.writeFileSync(propsFile, JSON.stringify(job.props ?? {}));
  const dest = path.join(outDir, `${job.out}.mp4`);
  console.log(`\n▶ ${cfg.reel}/${job.out}  (${job.composition})`);
  execSync(
    `npx remotion render src/index.ts ${job.composition} ${dest} --props=${propsFile} ${BROWSER} --log=error`,
    {stdio: 'inherit'},
  );
  fs.rmSync(propsFile);
}
console.log(`\n✅ ${cfg.jobs.length} b-rolls renderizados en ${outDir}/`);
