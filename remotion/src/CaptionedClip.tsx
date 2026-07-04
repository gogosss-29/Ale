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
import {FONT_MARCA, PALETA} from './marca';

// ─── Fase 2 · Captions del avatar ────────────────────────────────────────────
// Quema subtítulos animados palabra-por-palabra (estilo marca) sobre un clip.
// Props: el video (en public/) + las páginas de caption generadas por whisper.
const tokenSchema = z.object({
  text: z.string(),
  fromMs: z.number(),
  toMs: z.number(),
});
export const captionedClipSchema = z.object({
  videoSrc: z.string(),
  durationMs: z.number(),
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
  pages: [],
};

const INK = PALETA.ink;
const RED = PALETA.rojo;
const WHITE = PALETA.blanco;

export const CaptionedClip: React.FC<CaptionedClipProps> = ({videoSrc, pages}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const tMs = (frame / fps) * 1000;

  const page = pages.find((p) => tMs >= p.startMs && tMs < p.endMs + 120);

  return (
    <AbsoluteFill style={{backgroundColor: '#000', fontFamily: FONT_MARCA}}>
      <OffthreadVideo src={staticFile(videoSrc)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />

      {page ? <CaptionPage key={page.startMs} page={page} tMs={tMs} frame={frame} fps={fps} /> : null}
    </AbsoluteFill>
  );
};

const CaptionPage: React.FC<{
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
