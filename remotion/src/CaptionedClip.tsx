import React from 'react';
import {
  AbsoluteFill,
  OffthreadVideo,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {z} from 'zod';
import {loadFont} from '@remotion/fonts';
import {FONT_MARCA, PALETA} from './marca';

// ─── Fase 2 · Captions del avatar ────────────────────────────────────────────
// Quema subtítulos animados sobre un clip. Dos presets:
//  - "marca":       páginas de ~3 palabras, MAYÚSCULAS, Archivo 900 con contorno
//                   tinta, palabra activa en rojo, abajo. (estilo Cerebro)
//  - "minimal-top": UNA palabra por vez, minúsculas, tipografía redondeada blanca
//                   con sombra suave, arriba del encuadre. (estilo creator clean)
loadFont({
  family: 'Nunito',
  url: staticFile('fonts/Nunito-Variable.ttf'),
  weight: '200 1000',
}).catch(() => undefined);

const FONT_REDONDEADA = "'Nunito', 'Arial Rounded MT Bold', Arial, sans-serif";

const tokenSchema = z.object({
  text: z.string(),
  fromMs: z.number(),
  toMs: z.number(),
});
export const captionedClipSchema = z.object({
  videoSrc: z.string(),
  durationMs: z.number(),
  preset: z.enum(['marca', 'minimal-top']).default('marca'),
  pages: z.array(
    z.object({
      startMs: z.number(),
      endMs: z.number(),
      tokens: z.array(tokenSchema),
    }),
  ),
});
export type CaptionedClipProps = z.infer<typeof captionedClipSchema>;

export const captionedClipDefaults: CaptionedClipProps = {
  videoSrc: 'clips/piloto.mp4',
  durationMs: 6550,
  preset: 'marca',
  pages: [],
};

const INK = PALETA.ink;
const RED = PALETA.rojo;
const WHITE = PALETA.blanco;

export const CaptionedClip: React.FC<CaptionedClipProps> = ({videoSrc, pages, preset}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const tMs = (frame / fps) * 1000;

  const page = pages.find((p) => tMs >= p.startMs && tMs < p.endMs + 120);

  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      <OffthreadVideo src={staticFile(videoSrc)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
      {page ? (
        preset === 'minimal-top' ? (
          <MinimalTopPage key={page.startMs} page={page} frame={frame} fps={fps} />
        ) : (
          <MarcaPage key={page.startMs} page={page} tMs={tMs} frame={frame} fps={fps} />
        )
      ) : null}
    </AbsoluteFill>
  );
};

// ─── Preset "minimal-top": una palabra, minúscula, redondeada, arriba ───────
const MinimalTopPage: React.FC<{
  page: CaptionedClipProps['pages'][number];
  frame: number;
  fps: number;
}> = ({page, frame, fps}) => {
  const pageStartFrame = Math.round((page.startMs / 1000) * fps);
  const pop = spring({frame: frame - pageStartFrame, fps, config: {damping: 13, stiffness: 320}});
  const word = page.tokens.map((t) => t.text).join(' ').toLowerCase();

  return (
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        top: 210,
        display: 'flex',
        justifyContent: 'center',
        transform: `scale(${0.88 + pop * 0.12})`,
        opacity: Math.min(1, pop * 1.8),
      }}
    >
      <span
        style={{
          fontFamily: FONT_REDONDEADA,
          fontWeight: 1000 as never,
          fontSize: 88,
          color: WHITE,
          letterSpacing: 0.5,
          textShadow: '0 6px 22px rgba(0,0,0,0.55), 0 2px 6px rgba(0,0,0,0.45)',
          whiteSpace: 'pre',
        }}
      >
        {word}
      </span>
    </div>
  );
};

// ─── Preset "marca": páginas con palabra activa resaltada ───────────────────
const MarcaPage: React.FC<{
  page: CaptionedClipProps['pages'][number];
  tMs: number;
  frame: number;
  fps: number;
}> = ({page, tMs, frame, fps}) => {
  const pageStartFrame = Math.round((page.startMs / 1000) * fps);
  const inSpring = spring({frame: frame - pageStartFrame, fps, config: {damping: 12, stiffness: 220}});

  return (
    <div
      style={{
        position: 'absolute',
        left: 40,
        right: 40,
        top: 1390,
        display: 'flex',
        flexWrap: 'wrap',
        justifyContent: 'center',
        alignItems: 'center',
        columnGap: 38,
        rowGap: 8,
        fontFamily: FONT_MARCA,
        transform: `scale(${0.9 + inSpring * 0.1}) translateY(${(1 - inSpring) * 22}px)`,
        opacity: Math.min(1, inSpring * 1.6),
      }}
    >
      {page.tokens.map((tk, i) => {
        const active = tMs >= tk.fromMs && tMs < tk.toMs + 60;
        const said = tMs >= tk.toMs + 60;
        return (
          <span
            key={i}
            style={{
              fontWeight: 900,
              fontSize: 76,
              lineHeight: 1.12,
              textTransform: 'uppercase',
              letterSpacing: 1,
              color: active ? RED : WHITE,
              transform: active ? 'scale(1.09)' : 'scale(1)',
              opacity: said || active ? 1 : 0.92,
              textShadow: `0 4px 0 ${INK}, 0 -3px 0 ${INK}, 3px 0 0 ${INK}, -3px 0 0 ${INK}, 4px 5px 0 ${INK}, 0 10px 34px rgba(0,0,0,0.65)`,
              transition: 'none',
              whiteSpace: 'pre',
            }}
          >
            {tk.text}
          </span>
        );
      })}
    </div>
  );
};
