// ─── Biblioteca de overlays del sistema de edición ──────────────────────────
// Overlays parametrizados y reutilizables para CUALQUIER video (ver EditedVideo).
// Todos montan dentro de una <Sequence>, así que su frame 0 = inicio del overlay.
// Convención: texto exacto viene del editmap; nada hardcodeado de un video puntual.
import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {FONT_MARCA, PALETA} from './marca';

// ── brandBug · wordmark persistente arriba-izquierda ────────────────────────
export const BrandBug: React.FC<{text?: string}> = ({text = 'CEREBRO'}) => (
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
    {text}
  </div>
);

// ── topLabel · pill de tema arriba-centro ───────────────────────────────────
export const TopLabel: React.FC<{text: string}> = ({text}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({frame, fps, config: {damping: 16, stiffness: 180}, durationInFrames: 14});
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'flex-start', paddingTop: 130}}>
      <div
        style={{
          transform: `translateY(${interpolate(enter, [0, 1], [-24, 0])}px)`,
          opacity: Math.min(1, enter * 1.6),
          background: 'rgba(20,22,26,0.66)',
          backdropFilter: 'blur(8px)',
          border: '1px solid rgba(255,255,255,0.16)',
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

// ── numberCallout · dato clave con count-up ─────────────────────────────────
export const NumberCallout: React.FC<{
  prefix?: string;
  value: number;
  suffix?: string;
  color?: string;
}> = ({prefix = '', value, suffix = '', color = PALETA.verde}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({frame, fps, config: {damping: 13, stiffness: 200}, durationInFrames: 16});
  const count = spring({frame, fps, config: {damping: 200}, durationInFrames: 26});
  const val = Math.round(interpolate(count, [0, 1], [0, value]));
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'flex-start', paddingTop: 250}}>
      <div
        style={{
          transform: `scale(${interpolate(enter, [0, 1], [0.8, 1])})`,
          opacity: Math.min(1, enter * 1.8),
          background: 'rgba(255,255,255,0.10)',
          backdropFilter: 'blur(10px)',
          border: `2px solid ${color}`,
          borderRadius: 22,
          padding: '18px 30px',
          textAlign: 'center',
          boxShadow: '0 16px 50px rgba(0,0,0,0.4)',
          fontFamily: FONT_MARCA,
        }}
      >
        <div style={{color, fontWeight: 900, fontSize: 96, lineHeight: 1, letterSpacing: -1, fontVariantNumeric: 'tabular-nums'}}>
          {prefix} {val}
        </div>
        {suffix ? (
          <div style={{color: PALETA.blanco, fontWeight: 800, fontSize: 34, letterSpacing: 4, marginTop: 4}}>{suffix}</div>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};

// ── chip · dato secundario arriba-derecha ───────────────────────────────────
export const Chip: React.FC<{text: string; sub?: string}> = ({text, sub}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({frame, fps, config: {damping: 14, stiffness: 200}, durationInFrames: 14});
  return (
    <AbsoluteFill style={{alignItems: 'flex-end', justifyContent: 'flex-start', paddingTop: 300, paddingRight: 44}}>
      <div
        style={{
          transform: `translateX(${interpolate(enter, [0, 1], [40, 0])}px)`,
          opacity: Math.min(1, enter * 1.8),
          background: 'rgba(20,22,26,0.72)',
          backdropFilter: 'blur(8px)',
          border: '1px solid rgba(255,255,255,0.16)',
          borderRadius: 16,
          padding: '12px 20px',
          textAlign: 'right',
          fontFamily: FONT_MARCA,
        }}
      >
        <div style={{color: PALETA.blanco, fontWeight: 900, fontSize: 40, letterSpacing: 1}}>{text}</div>
        {sub ? (
          <div style={{color: PALETA.verde, fontWeight: 800, fontSize: 22, letterSpacing: 3, textTransform: 'uppercase'}}>{sub}</div>
        ) : null}
      </div>
    </AbsoluteFill>
  );
};

// ── barsLabel · mini gráfico de barras + pill (ej. "propiedades · BA") ──────
export const BarsLabel: React.FC<{label: string; heights?: number[]}> = ({label, heights = [70, 120, 92]}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const e = spring({frame, fps, config: {damping: 16, stiffness: 180}, durationInFrames: 14});
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'flex-start', paddingTop: 230}}>
      <div style={{opacity: Math.min(1, e * 1.7), transform: `translateY(${(1 - e) * -18}px)`, textAlign: 'center'}}>
        <svg width={heights.length * 70 + 30} height="130" viewBox={`0 0 ${heights.length * 70 + 30} 130`}>
          {heights.map((h, i) => (
            <rect key={i} x={20 + i * 70} y={130 - h * e} width={50} height={h * e} rx={6} fill={PALETA.blanco} opacity={0.92} />
          ))}
        </svg>
        <div
          style={{
            marginTop: 8,
            background: 'rgba(20,22,26,0.66)',
            border: '1px solid rgba(255,255,255,0.16)',
            borderRadius: 999,
            padding: '10px 20px',
            display: 'inline-block',
            fontFamily: FONT_MARCA,
            fontWeight: 800,
            fontSize: 30,
            letterSpacing: 2,
            color: PALETA.blanco,
            textTransform: 'uppercase',
          }}
        >
          {label}
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ── arrowChips · pares tipo ENTRAR/SALIR ────────────────────────────────────
export const ArrowChips: React.FC<{items: {label: string; dir: 'in' | 'out'; color?: string}[]}> = ({items}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const e = spring({frame, fps, config: {damping: 15, stiffness: 200}, durationInFrames: 14});
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'flex-start', paddingTop: 250}}>
      <div style={{opacity: Math.min(1, e * 1.8), display: 'flex', gap: 16}}>
        {items.map((it, i) => {
          const color = it.color ?? (it.dir === 'in' ? PALETA.verde : PALETA.rojo);
          return (
            <div
              key={i}
              style={{
                background: 'rgba(20,22,26,0.72)',
                border: `1px solid ${color}`,
                borderRadius: 14,
                padding: '10px 18px',
                display: 'flex',
                alignItems: 'center',
                gap: 10,
                fontFamily: FONT_MARCA,
                fontWeight: 900,
                fontSize: 34,
                color: PALETA.blanco,
              }}
            >
              <span style={{color}}>{it.dir === 'in' ? '↘' : '↗'}</span>
              {it.label}
            </div>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

// ── bigBadge · badge grande centrado (ej. "US$ ↑") ──────────────────────────
export const BigBadge: React.FC<{text: string; color?: string}> = ({text, color = PALETA.verde}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const e = spring({frame, fps, config: {damping: 13, stiffness: 210}, durationInFrames: 14});
  return (
    <AbsoluteFill style={{alignItems: 'center', justifyContent: 'flex-start', paddingTop: 250}}>
      <div
        style={{
          opacity: Math.min(1, e * 1.8),
          transform: `translateY(${interpolate(e, [0, 1], [30, 0])}px)`,
          background: 'rgba(255,255,255,0.10)',
          backdropFilter: 'blur(10px)',
          border: `2px solid ${color}`,
          borderRadius: 20,
          padding: '14px 26px',
          fontFamily: FONT_MARCA,
          fontWeight: 900,
          fontSize: 64,
          color,
          letterSpacing: 1,
        }}
      >
        {text}
      </div>
    </AbsoluteFill>
  );
};

// ── risingLine · línea creciente con glow (para capa "detrás") ──────────────
export type CurvePoints = {x: number; y: number}[]; // 4 puntos bezier [p0,p1,p2,p3]
export const CURVAS: Record<string, CurvePoints> = {
  ancha: [
    {x: 90, y: 1300},
    {x: 520, y: 1180},
    {x: 720, y: 760},
    {x: 1000, y: 540},
  ],
  empinada: [
    {x: 110, y: 1360},
    {x: 440, y: 1300},
    {x: 780, y: 900},
    {x: 1000, y: 500},
  ],
};

export const RisingLine: React.FC<{
  durationInFrames: number;
  curva?: string | CurvePoints;
  color?: string;
  id?: string;
}> = ({durationInFrames, curva = 'ancha', color = PALETA.verde, id = 'rl'}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const pts = typeof curva === 'string' ? CURVAS[curva] ?? CURVAS.ancha : curva;
  const [p0, p1, p2, p3] = pts;
  const draw = spring({frame, fps, config: {damping: 200}, durationInFrames: Math.round(durationInFrames * 0.62)});
  const op = interpolate(frame, [0, 8, durationInFrames - 12, durationInFrames], [0, 1, 1, 0], {
    extrapolateRight: 'clamp',
  });
  const u = 1 - draw;
  const tip = {
    x: u * u * u * p0.x + 3 * u * u * draw * p1.x + 3 * u * draw * draw * p2.x + draw * draw * draw * p3.x,
    y: u * u * u * p0.y + 3 * u * u * draw * p1.y + 3 * u * draw * draw * p2.y + draw * draw * draw * p3.y,
  };
  const d = `M${p0.x} ${p0.y} C${p1.x} ${p1.y} ${p2.x} ${p2.y} ${p3.x} ${p3.y}`;
  return (
    <AbsoluteFill style={{opacity: op}}>
      <svg width="1080" height="1920" viewBox="0 0 1080 1920" style={{position: 'absolute', inset: 0}}>
        <defs>
          <filter id={`glow-${id}`} x="-30%" y="-30%" width="160%" height="160%">
            <feGaussianBlur stdDeviation="9" result="b" />
            <feMerge>
              <feMergeNode in="b" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>
        </defs>
        <path d={d} fill="none" stroke={color} strokeWidth={44} strokeLinecap="round" opacity={0.16} pathLength={1} strokeDasharray={1} strokeDashoffset={1 - draw} style={{filter: 'blur(6px)'}} />
        <path d={d} fill="none" stroke={color} strokeWidth={13} strokeLinecap="round" pathLength={1} strokeDasharray={1} strokeDashoffset={1 - draw} filter={`url(#glow-${id})`} />
        <circle cx={tip.x} cy={tip.y} r={15} fill="#EAFFF2" stroke={color} strokeWidth={6} filter={`url(#glow-${id})`} />
      </svg>
    </AbsoluteFill>
  );
};
