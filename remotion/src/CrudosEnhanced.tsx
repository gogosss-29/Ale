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

// Ventanas "detrás" (línea verde creciente). Recortes segmentados en
// public/crudos-person/f-<abs>.png (30fps).
const W1_START_ABS = 519, W1_COUNT = 111;   // 17.3s · "las propiedades suban de valor"
const W2_START_ABS = 1587, W2_COUNT = 126;  // 52.9s · "van a subir / subieron un montón"

type Curve = {p0: {x: number; y: number}; p1: {x: number; y: number}; p2: {x: number; y: number}; p3: {x: number; y: number}};
const CURVE_1: Curve = {p0: {x: 90, y: 1300}, p1: {x: 520, y: 1180}, p2: {x: 720, y: 760}, p3: {x: 1000, y: 540}};
const CURVE_2: Curve = {p0: {x: 110, y: 1360}, p1: {x: 440, y: 1300}, p2: {x: 780, y: 900}, p3: {x: 1000, y: 500}};

// ─── Línea verde creciente con aura de glow (va DETRÁS de la persona) ─────────
const RisingLineBehind: React.FC<{count: number; curve: Curve; id: string}> = ({count, curve, id}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const draw = spring({frame, fps, config: {damping: 200}, durationInFrames: Math.round(count * 0.62)});
  const op = interpolate(frame, [0, 8, count - 12, count], [0, 1, 1, 0], {extrapolateRight: 'clamp'});
  const {p0, p1, p2, p3} = curve;
  const bez = (t: number) => {
    const u = 1 - t;
    return {
      x: u * u * u * p0.x + 3 * u * u * t * p1.x + 3 * u * t * t * p2.x + t * t * t * p3.x,
      y: u * u * u * p0.y + 3 * u * u * t * p1.y + 3 * u * t * t * p2.y + t * t * t * p3.y,
    };
  };
  const tip = bez(draw);
  const d = `M${p0.x} ${p0.y} C${p1.x} ${p1.y} ${p2.x} ${p2.y} ${p3.x} ${p3.y}`;
  return (
    <AbsoluteFill style={{opacity: op}}>
      <svg width="1080" height="1920" viewBox="0 0 1080 1920" style={{position: 'absolute', inset: 0}}>
        <defs>
          <filter id={`glow-${id}`} x="-30%" y="-30%" width="160%" height="160%">
            <feGaussianBlur stdDeviation="9" result="b" /><feMerge><feMergeNode in="b" /><feMergeNode in="SourceGraphic" /></feMerge>
          </filter>
        </defs>
        {/* aura ancha, muy transparente */}
        <path d={d} fill="none" stroke={PALETA.verde} strokeWidth={44} strokeLinecap="round" opacity={0.16}
          pathLength={1} strokeDasharray={1} strokeDashoffset={1 - draw} style={{filter: `blur(6px)`}} />
        {/* línea principal */}
        <path d={d} fill="none" stroke={PALETA.verde} strokeWidth={13} strokeLinecap="round"
          pathLength={1} strokeDasharray={1} strokeDashoffset={1 - draw} filter={`url(#glow-${id})`} />
        {/* punta */}
        <circle cx={tip.x} cy={tip.y} r={15} fill="#EAFFF2" stroke={PALETA.verde} strokeWidth={6} filter={`url(#glow-${id})`} />
      </svg>
    </AbsoluteFill>
  );
};

// ─── Recorte de persona (para un tramo) ──────────────────────────────────────
const PersonCutout: React.FC<{startAbs: number; count: number}> = ({startAbs, count}) => {
  const frame = useCurrentFrame();
  const idx = Math.min(count - 1, Math.max(0, frame));
  const name = `crudos-person/f-${String(startAbs + idx).padStart(4, '0')}.png`;
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

      {/* 2+3 · gráfico DETRÁS + recorte de persona encima · ventana 1 "suban de valor" */}
      <Sequence from={W1_START_ABS} durationInFrames={W1_COUNT} name="detras:suban-de-valor">
        <RisingLineBehind count={W1_COUNT} curve={CURVE_1} id="w1" />
        <PersonCutout startAbs={W1_START_ABS} count={W1_COUNT} />
      </Sequence>
      {/* ventana 2 "van a subir / subieron un montón" */}
      <Sequence from={W2_START_ABS} durationInFrames={W2_COUNT} name="detras:van-a-subir">
        <RisingLineBehind count={W2_COUNT} curve={CURVE_2} id="w2" />
        <PersonCutout startAbs={W2_START_ABS} count={W2_COUNT} />
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
