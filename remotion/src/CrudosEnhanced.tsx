// ─── CrudosEnhanced ─────────────────────────────────────────────────────────
// Edición Remotion del crudo real con animaciones CONTEXTUALES sincronizadas.
// Capas (de atrás hacia adelante): video → gráfico "detrás" → recorte de persona
// (te pone al frente) → apoyos al frente → captions. El recorte se genera con
// segmentación (rembg u2net_human_seg) solo en la ventana del gráfico "detrás".
import React from 'react';
import {
  AbsoluteFill,
  Img,
  OffthreadVideo,
  Sequence,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {captionedClipSchema, captionedClipDefaults, CaptionsLayer} from './CaptionedClip';
import {BrandBug, TopLabel, NumberCallout, Chip, crudosSchema} from './CrudosCaptioned';
import {FONT_MARCA, PALETA} from './marca';

const FPS = 30;
const s = (seg: number) => Math.round(seg * FPS);

export const crudosEnhancedSchema = crudosSchema;
export const crudosEnhancedDefaults = {...captionedClipDefaults, videoSrc: 'clips/crudos.mp4'};

// Ventana "detrás": línea verde creciente cuando dice "las propiedades suban de valor".
// Recortes segmentados en public/crudos-person/f-0519..0629.png (30fps).
const W1_START_ABS = 519;   // 17.3s
const W1_COUNT = 111;       // ~3.7s

// ─── Línea verde creciente (va DETRÁS de la persona) ─────────────────────────
const RisingLineBehind: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const draw = spring({frame, fps, config: {damping: 200}, durationInFrames: 70});
  const op = interpolate(frame, [0, 8, W1_COUNT - 12, W1_COUNT], [0, 1, 1, 0], {extrapolateRight: 'clamp'});
  const tipT = draw;
  // curva ascendente aprox (bezier) evaluada para el punto de la punta
  const p0 = {x: 90, y: 1300}, p1 = {x: 520, y: 1180}, p2 = {x: 720, y: 760}, p3 = {x: 1000, y: 560};
  const bez = (t: number) => {
    const u = 1 - t;
    return {
      x: u * u * u * p0.x + 3 * u * u * t * p1.x + 3 * u * t * t * p2.x + t * t * t * p3.x,
      y: u * u * u * p0.y + 3 * u * u * t * p1.y + 3 * u * t * t * p2.y + t * t * t * p3.y,
    };
  };
  const tip = bez(tipT);
  return (
    <AbsoluteFill style={{opacity: op}}>
      <svg width="1080" height="1920" viewBox="0 0 1080 1920" style={{position: 'absolute', inset: 0}}>
        <defs>
          <linearGradient id="area" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stopColor={PALETA.verde} stopOpacity="0.42" />
            <stop offset="100%" stopColor={PALETA.verde} stopOpacity="0" />
          </linearGradient>
          <filter id="glow"><feGaussianBlur stdDeviation="7" result="b" /><feMerge><feMergeNode in="b" /><feMergeNode in="SourceGraphic" /></feMerge></filter>
        </defs>
        {/* área bajo la curva (se revela con la línea) */}
        <path
          d={`M${p0.x} ${p0.y} C${p1.x} ${p1.y} ${p2.x} ${p2.y} ${p3.x} ${p3.y} L${tip.x} 1920 L${p0.x} 1920 Z`}
          fill="url(#area)"
          opacity={draw}
        />
        {/* línea creciente */}
        <path
          d={`M${p0.x} ${p0.y} C${p1.x} ${p1.y} ${p2.x} ${p2.y} ${p3.x} ${p3.y}`}
          fill="none"
          stroke={PALETA.verde}
          strokeWidth={14}
          strokeLinecap="round"
          pathLength={1}
          strokeDasharray={1}
          strokeDashoffset={1 - draw}
          filter="url(#glow)"
        />
        {/* punta */}
        <circle cx={tip.x} cy={tip.y} r={16} fill={PALETA.verde} filter="url(#glow)" />
      </svg>
    </AbsoluteFill>
  );
};

// ─── Recorte de persona (para ese tramo) ─────────────────────────────────────
const PersonCutout: React.FC = () => {
  const frame = useCurrentFrame();
  const idx = Math.min(W1_COUNT - 1, Math.max(0, frame));
  const name = `crudos-person/f-${String(W1_START_ABS + idx).padStart(4, '0')}.png`;
  return <Img src={staticFile(name)} style={{position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover'}} />;
};

// ─── Apoyos al frente ────────────────────────────────────────────────────────
const PropsBA: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const e = spring({frame, fps, config: {damping: 16, stiffness: 180}, durationInFrames: 14});
  const heights = [70, 120, 92];
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'flex-start', paddingTop: 230}}>
      <div style={{opacity: Math.min(1, e * 1.7), transform: `translateY(${(1 - e) * -18}px)`, textAlign: 'center'}}>
        <svg width="220" height="130" viewBox="0 0 220 130">
          {heights.map((h, i) => (
            <rect key={i} x={20 + i * 70} y={130 - h * e} width={50} height={h * e} rx={6} fill={PALETA.blanco} opacity={0.92} />
          ))}
        </svg>
        <div style={{marginTop: 8, background: 'rgba(20,22,26,0.66)', border: '1px solid rgba(255,255,255,0.16)', borderRadius: 999, padding: '10px 20px', display: 'inline-block', fontFamily: FONT_MARCA, fontWeight: 800, fontSize: 30, letterSpacing: 2, color: PALETA.blanco}}>
          PROPIEDADES · BUENOS AIRES
        </div>
      </div>
    </AbsoluteFill>
  );
};

const arrowChip = (label: string, color: string, dir: 'in' | 'out') => (
  <div style={{background: 'rgba(20,22,26,0.72)', border: `1px solid ${color}`, borderRadius: 14, padding: '10px 18px', display: 'flex', alignItems: 'center', gap: 10, fontFamily: FONT_MARCA, fontWeight: 900, fontSize: 34, color: PALETA.blanco}}>
    <span style={{color}}>{dir === 'in' ? '↘' : '↗'}</span>
    {label}
  </div>
);
const Liquidity: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const e = spring({frame, fps, config: {damping: 15, stiffness: 200}, durationInFrames: 14});
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'flex-start', paddingTop: 250}}>
      <div style={{opacity: Math.min(1, e * 1.8), display: 'flex', gap: 16}}>
        {arrowChip('ENTRAR', PALETA.verde, 'in')}
        {arrowChip('SALIR', PALETA.rojo, 'out')}
      </div>
    </AbsoluteFill>
  );
};

const Dolar: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const e = spring({frame, fps, config: {damping: 13, stiffness: 210}, durationInFrames: 14});
  const rise = interpolate(e, [0, 1], [30, 0]);
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'flex-start', paddingTop: 250}}>
      <div style={{opacity: Math.min(1, e * 1.8), transform: `translateY(${rise}px)`, background: 'rgba(255,255,255,0.10)', backdropFilter: 'blur(10px)', border: `2px solid ${PALETA.verde}`, borderRadius: 20, padding: '14px 26px', fontFamily: FONT_MARCA, fontWeight: 900, fontSize: 64, color: PALETA.verde, letterSpacing: 1}}>
        US$ ↑
      </div>
    </AbsoluteFill>
  );
};

export const CrudosEnhanced: React.FC<import('zod').infer<typeof crudosEnhancedSchema>> = ({videoSrc, pages, preset}) => {
  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      {/* 1 · video de base */}
      <OffthreadVideo src={staticFile(videoSrc)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />

      {/* 2+3 · gráfico DETRÁS + recorte de persona encima (ventana "suban de valor") */}
      <Sequence from={W1_START_ABS} durationInFrames={W1_COUNT} name="detras:linea-verde">
        <RisingLineBehind />
        <PersonCutout />
      </Sequence>

      {/* 4 · apoyos al frente */}
      <BrandBug />
      <Sequence from={0} durationInFrames={s(4.5)} name="tema"><TopLabel text="Fondo Beltrán Briones" /></Sequence>
      <Sequence from={s(2.0)} durationInFrames={s(3.4)} name="dato-45M"><NumberCallout /></Sequence>
      <Sequence from={s(6.7)} durationInFrames={s(3.3)} name="buenos-aires"><PropsBA /></Sequence>
      <Sequence from={s(28.4)} durationInFrames={s(3.2)} name="cada-3-meses"><Chip text="CADA 3 MESES" sub="Alquileres" /></Sequence>
      <Sequence from={s(46.2)} durationInFrames={s(4.0)} name="liquidez"><Liquidity /></Sequence>
      <Sequence from={s(57.5)} durationInFrames={s(2.2)} name="dolar"><Dolar /></Sequence>

      {/* 5 · captions arriba de todo */}
      <CaptionsLayer pages={pages} preset={preset} />
    </AbsoluteFill>
  );
};
