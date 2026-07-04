import {
  installWhisperCpp,
  downloadWhisperModel,
  transcribe,
  toCaptions,
} from '@remotion/install-whisper-cpp';
import path from 'path';
import fs from 'fs';

const to = path.join(process.cwd(), 'whisper.cpp');
const version = '1.5.5';
const model = 'medium'; // buena precisión en español
const wav = path.join(process.cwd(), 'audio', 'voice16k.wav');

console.log('Instalando whisper.cpp...');
await installWhisperCpp({to, version});

console.log('Descargando modelo', model, '...');
await downloadWhisperModel({model, folder: to});

console.log('Transcribiendo (es)...');
const {transcription} = await transcribe({
  inputPath: wav,
  whisperPath: to,
  whisperCppVersion: version,
  model,
  tokenLevelTimestamps: true,
  language: 'es',
  printOutput: false,
});

const {captions} = toCaptions({whisperCppOutput: {transcription}});
fs.mkdirSync(path.join(process.cwd(), 'src', 'data'), {recursive: true});
const out = path.join(process.cwd(), 'src', 'data', 'captions.json');
fs.writeFileSync(out, JSON.stringify(captions, null, 2));
console.log('OK ->', out, '| tokens:', captions.length);
console.log('Texto:', captions.map((c) => c.text).join(''));
