import React from 'react';
import {
  AbsoluteFill,
  Img,
  OffthreadVideo,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {z} from 'zod';
import {loadFont} from '@remotion/fonts';
import {FONT_MARCA} from './marca';

// ─── Captions EDITORIALES (estilo agencia) ───────────────────────────────────
// Frases compuestas tipográficamente (sans limpia + serif itálica gigante),
// posiciones que cambian por frase y TEXTO DETRÁS DE LA PERSONA (oclusión con
// secuencia de recortes generada por segmentación IA).
loadFont({
  family: 'PlayfairIt',
  url: staticFile('fonts/PlayfairDisplay-Italic.ttf'),
  weight: '400 900',
  style: 'italic',
}).catch(() => undefined);

const SERIF_IT = "'PlayfairIt', 'Times New Roman', serif";

const elemSchema = z.object({
  text: z.string(),
  tipo: z.enum(['sans', 'serif']),
  size: z.number(),
  y: z.number(),
  x: z.number().optional(), // si falta: centrado
  detras: z.boolean().default(false),
  delayMs: z.number().default(0),
  peso: z.number().optional(),
});
export const editorialSchema = z.object({
  videoSrc: z.string(),
  personSeqDir: z.string(), // carpeta en public/ con f-%03d.png (recorte persona)
  personSeqCount: z.number(),
  durationMs: z.number(),
  frases: z.array(
    z.object({
      fromMs: z.number(),
      toMs: z.number(),
      elems: z.array(elemSchema),
    }),
  ),
});
export type EditorialProps = z.infer<typeof editorialSchema>;

export const editorialDefaults: EditorialProps = {
  videoSrc: 'clips/piloto.mp4',
  personSeqDir: 'clips/piloto-person',
  personSeqCount: 196,
  durationMs: 6550,
  frases: [],
};

const Elem: React.FC<{e: z.infer<typeof elemSchema>; fraseStartMs: number}> = ({e, fraseStartMs}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const startFrame = Math.round(((fraseStartMs + e.delayMs) / 1000) * fps);
  const s = spring({frame: frame - startFrame, fps, config: {damping: 16, stiffness: 130}});
  const isSerif = e.tipo === 'serif';

  return (
    <div
      style={{
        position: 'absolute',
        top: e.y,
        left: e.x ?? 0,
        right: e.x != null ? undefined : 0,
        display: 'flex',
        justifyContent: e.x != null ? 'flex-start' : 'center',
        transform: `translateY(${(1 - s) * 34}px) scale(${isSerif ? 0.94 + s * 0.06 : 1})`,
        opacity: Math.min(1, s * 1.5),
        pointerEvents: 'none',
      }}
    >
      <span
        style={{
          fontFamily: isSerif ? SERIF_IT : FONT_MARCA,
          fontStyle: isSerif ? 'italic' : 'normal',
          fontWeight: (e.peso ?? (isSerif ? 600 : 600)) as never,
          fontSize: e.size,
          color: '#FFFFFF',
          letterSpacing: isSerif ? 0 : 2,
          lineHeight: 1.05,
          whiteSpace: 'pre',
          textShadow: '0 4px 18px rgba(0,0,0,0.35), 0 1px 4px rgba(0,0,0,0.25)',
        }}
      >
        {e.text}
      </span>
    </div>
  );
};

export const EditorialCaptions: React.FC<EditorialProps> = ({
  videoSrc,
  personSeqDir,
  personSeqCount,
  frases,
}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const tMs = (frame / fps) * 1000;

  const activas = frases.filter((f) => tMs >= f.fromMs && tMs < f.toMs);
  const personFrame = Math.min(personSeqCount, Math.max(1, frame + 1));
  const personSrc = `${personSeqDir}/f-${String(personFrame).padStart(3, '0')}.png`;

  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      {/* 1 · Video base */}
      <OffthreadVideo src={staticFile(videoSrc)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />

      {/* 2 · Textos DETRÁS de la persona */}
      {activas.map((f, i) =>
        f.elems.filter((e) => e.detras).map((e, j) => <Elem key={`b${i}-${j}`} e={e} fraseStartMs={f.fromMs} />),
      )}

      {/* 3 · Recorte de la persona (oclusión) */}
      <Img src={staticFile(personSrc)} style={{position: 'absolute', inset: 0, width: '100%', height: '100%'}} />

      {/* 4 · Textos DELANTE */}
      {activas.map((f, i) =>
        f.elems.filter((e) => !e.detras).map((e, j) => <Elem key={`f${i}-${j}`} e={e} fraseStartMs={f.fromMs} />),
      )}
    </AbsoluteFill>
  );
};
