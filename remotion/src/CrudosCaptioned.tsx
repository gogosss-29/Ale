// ─── CrudosCaptioned ────────────────────────────────────────────────────────
// Edición Remotion del crudo real (talking-head): captions de marca (CaptionedClip)
// + capas por código encima: label de tema, callout del dato "US$45M" con count-up,
// chip "CADA 3 MESES" y bug de marca. Nunca toca el footage ni la voz.
import React from 'react';
import {
  AbsoluteFill,
  Sequence,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {CaptionedClip, captionedClipSchema, captionedClipDefaults} from './CaptionedClip';
import {FONT_MARCA, PALETA} from './marca';

const FPS = 30;
const s = (seg: number) => Math.round(seg * FPS);

export const crudosSchema = captionedClipSchema; // mismas props que CaptionedClip
export const crudosDefaults = {...captionedClipDefaults, videoSrc: 'clips/crudos.mp4'};

// Bug de marca: wordmark de texto, arriba-izquierda, persistente.
export const BrandBug: React.FC = () => (
  <div
    style={{
      position: 'absolute',
      top: 60,
      left: 44,
      fontFamily: FONT_MARCA,
      fontWeight: 900,
      fontSize: 30,
      letterSpacing: 2,
      color: PALETA.blanco,
      textShadow: '0 2px 8px rgba(0,0,0,0.6)',
    }}
  >
    CEREBRO
  </div>
);

// Label de tema (pill arriba-centro).
export const TopLabel: React.FC<{text: string}> = ({text}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({frame, fps, config: {damping: 16, stiffness: 180}, durationInFrames: 14});
  const y = interpolate(enter, [0, 1], [-24, 0]);
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'flex-start', paddingTop: 130}}>
      <div
        style={{
          transform: `translateY(${y}px)`,
          opacity: Math.min(1, enter * 1.6),
          background: 'rgba(20,22,26,0.66)',
          backdropFilter: 'blur(8px)',
          border: `1px solid rgba(255,255,255,0.16)`,
          color: PALETA.blanco,
          fontFamily: FONT_MARCA,
          fontWeight: 800,
          fontSize: 30,
          letterSpacing: 1.5,
          textTransform: 'uppercase',
          padding: '12px 22px',
          borderRadius: 999,
        }}
      >
        {text}
      </div>
    </AbsoluteFill>
  );
};

// Callout del dato con count-up: "US$ 45 MILLONES".
export const NumberCallout: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({frame, fps, config: {damping: 13, stiffness: 200}, durationInFrames: 16});
  const count = spring({frame, fps, config: {damping: 200}, durationInFrames: 26});
  const val = Math.round(interpolate(count, [0, 1], [0, 45]));
  const scale = interpolate(enter, [0, 1], [0.8, 1]);
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'flex-start', paddingTop: 250}}>
      <div
        style={{
          transform: `scale(${scale})`,
          opacity: Math.min(1, enter * 1.8),
          background: 'rgba(255,255,255,0.10)',
          backdropFilter: 'blur(10px)',
          border: `2px solid ${PALETA.verde}`,
          borderRadius: 22,
          padding: '18px 30px',
          textAlign: 'center',
          boxShadow: '0 16px 50px rgba(0,0,0,0.4)',
          fontFamily: FONT_MARCA,
        }}
      >
        <div style={{color: PALETA.verde, fontWeight: 900, fontSize: 96, lineHeight: 1, letterSpacing: -1, fontVariantNumeric: 'tabular-nums'}}>
          US$ {val}
        </div>
        <div style={{color: PALETA.blanco, fontWeight: 800, fontSize: 34, letterSpacing: 4, marginTop: 4}}>
          MILLONES
        </div>
      </div>
    </AbsoluteFill>
  );
};

// Chip arriba-derecha (dato secundario).
export const Chip: React.FC<{text: string; sub: string}> = ({text, sub}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({frame, fps, config: {damping: 14, stiffness: 200}, durationInFrames: 14});
  const x = interpolate(enter, [0, 1], [40, 0]);
  return (
    <AbsoluteFill style={{alignItems: 'flex-end', justifyContent: 'flex-start', paddingTop: 300, paddingRight: 44}}>
      <div
        style={{
          transform: `translateX(${x}px)`,
          opacity: Math.min(1, enter * 1.8),
          background: 'rgba(20,22,26,0.72)',
          backdropFilter: 'blur(8px)',
          border: `1px solid rgba(255,255,255,0.16)`,
          borderRadius: 16,
          padding: '12px 20px',
          textAlign: 'right',
          fontFamily: FONT_MARCA,
        }}
      >
        <div style={{color: PALETA.blanco, fontWeight: 900, fontSize: 40, letterSpacing: 1}}>{text}</div>
        <div style={{color: PALETA.verde, fontWeight: 800, fontSize: 22, letterSpacing: 3, textTransform: 'uppercase'}}>{sub}</div>
      </div>
    </AbsoluteFill>
  );
};

export const CrudosCaptioned: React.FC<import('zod').infer<typeof crudosSchema>> = (props) => {
  return (
    <AbsoluteFill>
      {/* base: video + captions de marca */}
      <CaptionedClip {...props} />

      {/* capas por código encima */}
      <BrandBug />
      <Sequence from={0} durationInFrames={s(4.5)} name="tema"><TopLabel text="Fondo Beltrán Briones" /></Sequence>
      <Sequence from={s(2.0)} durationInFrames={s(3.4)} name="dato-45M"><NumberCallout /></Sequence>
      <Sequence from={s(28.4)} durationInFrames={s(3.2)} name="cada-3-meses"><Chip text="CADA 3 MESES" sub="Alquileres" /></Sequence>
    </AbsoluteFill>
  );
};
