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
import {FONT_MARCA, PALETA, injectFont} from './marca';

// ─── Fase 2 · Captions del avatar ────────────────────────────────────────────
// Quema subtítulos animados sobre un clip. Dos presets:
//  - "marca":       páginas de ~3 palabras, MAYÚSCULAS, Archivo 900 con contorno
//                   tinta, palabra activa en rojo, abajo. (estilo Cerebro)
//  - "minimal-top": UNA palabra por vez, minúsculas, tipografía redondeada blanca
//                   con sombra suave, arriba del encuadre. (estilo creator clean)
injectFont('Nunito', 'fonts/Nunito-Variable.ttf', '200 1000');
injectFont('Fraunces', 'fonts/Fraunces-Variable.ttf', '100 900');

const FONT_REDONDEADA = "'Nunito', 'Arial Rounded MT Bold', Arial, sans-serif";
const FONT_SOFT_SERIF = "'Fraunces', Georgia, serif";

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

// Capa de SOLO captions (sin video/fondo) — para componer encima de otras capas
// (p. ej. sobre el recorte de persona en CrudosEnhanced).
export const CaptionsLayer: React.FC<{
  pages: CaptionedClipProps['pages'];
  preset: CaptionedClipProps['preset'];
}> = ({pages, preset}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const tMs = (frame / fps) * 1000;
  const page = pages.find((p) => tMs >= p.startMs && tMs < p.endMs + 120);
  if (!page) return null;
  return preset === 'minimal-top' ? (
    <MinimalTopPage key={page.startMs} page={page} frame={frame} fps={fps} />
  ) : (
    <MarcaPage key={page.startMs} page={page} tMs={tMs} frame={frame} fps={fps} />
  );
};

export const CaptionedClip: React.FC<CaptionedClipProps> = ({videoSrc, pages, preset}) => {
  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      <OffthreadVideo src={staticFile(videoSrc)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
      <CaptionsLayer pages={pages} preset={preset} />
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
  const pop = spring({frame: frame - pageStartFrame, fps, config: {damping: 10, stiffness: 380}});
  const word = page.tokens.map((t) => t.text).join(' ').toLowerCase();

  // pop con leve overshoot (1.14 -> 1) como la referencia
  const scale = 1.14 - pop * 0.14;

  return (
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        top: 350,
        display: 'flex',
        justifyContent: 'center',
        transform: `scale(${scale})`,
        opacity: Math.min(1, pop * 2.2),
      }}
    >
      <span
        style={{
          fontFamily: FONT_SOFT_SERIF,
          fontWeight: 640 as never,
          fontVariationSettings: "'SOFT' 90, 'WONK' 0, 'opsz' 40",
          fontSize: 128,
          color: '#FFF6E9',
          letterSpacing: -1,
          textShadow: '0 3px 10px rgba(0,0,0,0.5), 0 10px 34px rgba(0,0,0,0.38)',
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
