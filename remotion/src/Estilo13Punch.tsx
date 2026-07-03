import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';

// ─── Estilo #13 · Kinetic Typography Punch ─────────────────────────────────
// Spec: fondo sólido que flipea (negro→crema) en el punch, texto bold,
// keyword en rojo con glow, reveal palabra por palabra, muy punchy.
const BLACK = '#000000';
const CREAM = '#F5F1E6';
const WHITE = '#FFFFFF';
const RED = '#E2352B';
const FONT = "Arial, 'Liberation Sans', 'Helvetica Neue', sans-serif";

const FLIP_FRAME = 26; // el fondo flipea cuando cae "GANAR"

export const Estilo13Punch: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const w1 = spring({frame: frame - 2, fps, config: {damping: 10, stiffness: 200}});
  const w2 = spring({frame: frame - 13, fps, config: {damping: 10, stiffness: 200}});
  const w3 = spring({frame: frame - FLIP_FRAME, fps, config: {damping: 8, stiffness: 190}});

  const flipped = frame >= FLIP_FRAME;
  const bg = flipped ? CREAM : BLACK;
  const inkColor = flipped ? '#151310' : WHITE;

  // Micro-respiración al final para que no quede muerto
  const breathe = 1 + Math.sin(frame / 9) * 0.004;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: bg,
        fontFamily: FONT,
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      {/* Glow suave detrás del texto */}
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
            fontSize: 150,
            fontWeight: 800,
            color: inkColor,
            letterSpacing: 2,
            transform: `scale(${0.7 + w1 * 0.3}) translateY(${(1 - w1) * 40}px)`,
            opacity: Math.min(1, w1 * 1.5),
          }}
        >
          FACTURAR
        </div>
        <div
          style={{
            fontSize: 112,
            fontWeight: 700,
            color: inkColor,
            letterSpacing: 6,
            marginTop: 14,
            transform: `scale(${0.7 + w2 * 0.3}) translateY(${(1 - w2) * 40}px)`,
            opacity: Math.min(1, w2 * 1.5),
          }}
        >
          NO ES
        </div>
        <div
          style={{
            fontSize: 230,
            fontWeight: 900,
            color: RED,
            letterSpacing: 2,
            marginTop: 20,
            textShadow: '0 0 60px rgba(226,53,43,0.45)',
            transform: `scale(${0.55 + w3 * 0.45}) rotate(${(1 - w3) * -3}deg)`,
            opacity: Math.min(1, w3 * 1.6),
          }}
        >
          GANAR
        </div>
      </div>

      {/* Flash de 2 frames en el flip (golpe visual) */}
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
