import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {FONT_MARCA, PALETA} from './marca';

// ─── Estilo #13 · Kinetic Typography Punch ─────────────────────────────────
// Parametrizable: línea 1, línea 2 y keyword (el punch, en rojo con flip de fondo).
export const estilo13Schema = z.object({
  linea1: z.string(),
  linea2: z.string(),
  keyword: z.string(),
});
type Props = z.infer<typeof estilo13Schema>;

export const estilo13Defaults: Props = {
  linea1: 'FACTURAR',
  linea2: 'NO ES',
  keyword: 'GANAR',
};

const BLACK = PALETA.negro;
const CREAM = PALETA.crema;
const WHITE = PALETA.blanco;
const RED = PALETA.rojo;

const FLIP_FRAME = 26;

// Auto-ajuste: que la palabra entre en 1080px de ancho
const fit = (texto: string, base: number) =>
  Math.min(base, Math.floor(1650 / Math.max(4, texto.length)));

export const Estilo13Punch: React.FC<Props> = ({linea1, linea2, keyword}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const w1 = spring({frame: frame - 2, fps, config: {damping: 10, stiffness: 200}});
  const w2 = spring({frame: frame - 13, fps, config: {damping: 10, stiffness: 200}});
  const w3 = spring({frame: frame - FLIP_FRAME, fps, config: {damping: 8, stiffness: 190}});

  const flipped = frame >= FLIP_FRAME;
  const bg = flipped ? CREAM : BLACK;
  const inkColor = flipped ? '#151310' : WHITE;
  const breathe = 1 + Math.sin(frame / 9) * 0.004;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: bg,
        fontFamily: FONT_MARCA,
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      <div
        style={{
          position: 'absolute',
          width: 900,
          height: 900,
          borderRadius: '50%',
          background: flipped
            ? 'radial-gradient(circle, rgba(226,53,43,0.10), transparent 65%)'
            : 'radial-gradient(circle, rgba(255,255,255,0.10), transparent 65%)',
          filter: 'blur(10px)',
        }}
      />
      <div style={{textAlign: 'center', transform: `scale(${breathe})`, lineHeight: 1.06}}>
        <div
          style={{
            fontSize: fit(linea1, 150),
            fontWeight: 800,
            color: inkColor,
            letterSpacing: 2,
            transform: `scale(${0.7 + w1 * 0.3}) translateY(${(1 - w1) * 40}px)`,
            opacity: Math.min(1, w1 * 1.5),
          }}
        >
          {linea1}
        </div>
        <div
          style={{
            fontSize: fit(linea2, 112),
            fontWeight: 700,
            color: inkColor,
            letterSpacing: 6,
            marginTop: 14,
            transform: `scale(${0.7 + w2 * 0.3}) translateY(${(1 - w2) * 40}px)`,
            opacity: Math.min(1, w2 * 1.5),
          }}
        >
          {linea2}
        </div>
        <div
          style={{
            fontSize: fit(keyword, 230),
            fontWeight: 900,
            color: RED,
            letterSpacing: 2,
            marginTop: 20,
            textShadow: '0 0 60px rgba(226,53,43,0.45)',
            transform: `scale(${0.55 + w3 * 0.45}) rotate(${(1 - w3) * -3}deg)`,
            opacity: Math.min(1, w3 * 1.6),
          }}
        >
          {keyword}
        </div>
      </div>

      <AbsoluteFill
        style={{
          backgroundColor: WHITE,
          opacity: interpolate(frame, [FLIP_FRAME, FLIP_FRAME + 2.5], [0.5, 0], {
            extrapolateLeft: 'clamp',
            extrapolateRight: 'clamp',
          }),
          pointerEvents: 'none',
        }}
      />
    </AbsoluteFill>
  );
};
