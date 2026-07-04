import fs from 'fs';
import path from 'path';

const dir = path.join(process.cwd(), 'src', 'data');
const tokens = JSON.parse(fs.readFileSync(path.join(dir, 'captions.json'), 'utf8'));

// Fusiona tokens sub-palabra (los que NO empiezan con espacio) en la palabra previa.
const words = [];
for (const t of tokens) {
  const startsNewWord = t.text.startsWith(' ') || words.length === 0;
  const isPunctOnly = /^[\s]*[.,!?¿¡:;…]+$/.test(t.text);
  if (startsNewWord && !isPunctOnly) {
    words.push({
      text: t.text,
      startMs: t.startMs,
      endMs: t.endMs,
      timestampMs: t.timestampMs,
      confidence: t.confidence ?? null,
    });
  } else {
    // continuación de palabra o puntuación pegada a la palabra anterior
    const w = words[words.length - 1];
    if (!w) {
      words.push({...t});
      continue;
    }
    w.text += t.text;
    w.endMs = t.endMs;
    w.timestampMs = t.timestampMs;
  }
}

// Normaliza: trim de texto pero conservando un solo espacio inicial para separación
const cleaned = words.map((w) => ({
  text: w.text.replace(/\s+/g, ' ').replace(/^ /, ' ').trimEnd(),
  startMs: w.startMs,
  endMs: w.endMs,
  timestampMs: w.timestampMs,
  confidence: w.confidence,
}));

fs.writeFileSync(
  path.join(dir, 'words.json'),
  JSON.stringify(cleaned, null, 2),
);
console.log('Palabras:', cleaned.length);
console.log('Muestra:', cleaned.slice(0, 12).map((w) => w.text.trim()).join(' | '));
