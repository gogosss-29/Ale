import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {FONT_MARCA, PALETA} from './marca';

// ─── Estilo #11 · "A la deriva" (BR2: sin objetivos, dependés del contexto) ─
// Línea que avanza hacia un target vacío "?" mientras una flecha CONTEXTO la
// zarandea arriba y abajo. Tag rojo final.
export const estilo11DerivaSchema = z.object({
  labelLinea: z.string(),
  labelFlecha: z.string(),
  tag: z.string(),
});
type Props = z.infer<typeof estilo11DerivaSchema>;
export const estilo11DerivaDefaults: Props = {
  labelLinea: 'SIN OBJETIVOS',
  labelFlecha: 'CONTEXTO',
  tag: 'A LA DERIVA',
};

const GRID = PALETA.grid;
const INK = PALETA.ink;
const RED = PALETA.rojo;
const WHITE = PALETA.blanco;

export const Estilo11Deriva: React.FC<Props> = ({labelLinea, labelFlecha, tag}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const camScale = interpolate(frame, [0, 96], [1, 1.06]);
  const panelIn = spring({frame, fps, config: {damping: 14, stiffness: 130}});
  const tagIn = spring({frame: frame - 52, fps, config: {damping: 9, stiffness: 170}});
  const draw = interpolate(frame, [6, 80], [0, 1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});

  // Trayectoria zarandeada: sube y baja errática mientras avanza
  const X0 = 170;
  const X1 = 830;
  const baseY = 850;
  const pts: Array<[number, number]> = [];
  const N = 60;
  for (let i = 0; i <= N * draw; i++) {
    const p = i / N;
    const x = X0 + (X1 - X0) * p;
    const wob = Math.sin(p * 9) * 90 * Math.min(1, p * 3) + Math.sin(p * 23) * 34;
    pts.push([x, baseY + wob]);
  }
  const path = pts.length > 1 ? 'M ' + pts.map(([x, y]) => `${x} ${y}`).join(' L ') : '';
  const head = pts[pts.length - 1] ?? [X0, baseY];

  // Flecha CONTEXTO que "empuja" (alterna arriba/abajo)
  const push = Math.sin(frame / 9);
  const arrowY = baseY + (push > 0 ? -260 : 210);
  const arrowFlip = push > 0 ? 1 : -1;

  return (
    <AbsoluteFill style={{backgroundColor: GRID, fontFamily: FONT_MARCA, overflow: 'hidden'}}>
      <AbsoluteFill
        style={{
          backgroundImage: `
            linear-gradient(to right, rgba(0,0,0,0.055) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(0,0,0,0.055) 1px, transparent 1px)`,
          backgroundSize: '54px 54px',
        }}
      />
      <AbsoluteFill style={{background: 'radial-gradient(ellipse 75% 65% at 50% 46%, transparent 60%, rgba(0,0,0,0.10) 100%)'}} />

      <AbsoluteFill style={{transform: `scale(${camScale})`, transformOrigin: '50% 45%'}}>
        {/* Panel */}
        <div
          style={{
            position: 'absolute',
            left: 70,
            right: 70,
            top: 380,
            height: 950,
            borderRadius: 36,
            background: 'rgba(255,255,255,0.62)',
            border: '1.5px solid rgba(255,255,255,0.9)',
            boxShadow: '0 40px 80px rgba(0,0,0,0.13)',
            transform: `translateY(${(1 - panelIn) * 80}px)`,
            opacity: Math.min(1, panelIn * 1.4),
          }}
        >
          <div style={{position: 'absolute', left: 60, top: 46, background: INK, color: WHITE, fontWeight: 800, fontSize: 34, letterSpacing: 1.5, padding: '12px 26px', borderRadius: 12}}>
            {labelLinea}
          </div>
        </div>

        {/* Target vacío con ? */}
        <div
          style={{
            position: 'absolute',
            left: X1 - 10,
            top: baseY - 70,
            width: 140,
            height: 140,
            borderRadius: '50%',
            border: `5px dashed ${RED}`,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontWeight: 900,
            fontSize: 74,
            color: RED,
            opacity: 0.4 + 0.6 * Math.abs(Math.sin(frame / 8)),
          }}
        >
          ?
        </div>

        {/* Línea errática */}
        <svg width={1080} height={1920} style={{position: 'absolute', inset: 0}}>
          {path ? <path d={path} stroke={INK} strokeWidth={10} fill="none" strokeLinecap="round" /> : null}
          <circle cx={head[0]} cy={head[1]} r={16} fill={INK} />
        </svg>

        {/* Flecha CONTEXTO que zarandea */}
        <div
          style={{
            position: 'absolute',
            left: Math.min(head[0], 700) - 100,
            top: arrowY,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: 8,
            opacity: draw > 0.15 ? 1 : 0,
          }}
        >
          <div style={{background: RED, color: WHITE, fontWeight: 800, fontSize: 34, letterSpacing: 2, padding: '10px 22px', borderRadius: 12}}>
            {labelFlecha}
          </div>
          <svg width={60} height={72} viewBox="0 0 60 72" style={{transform: `scaleY(${arrowFlip})`}}>
            <path d="M30 72 L2 30 L20 30 L20 0 L40 0 L40 30 L58 30 Z" fill={RED} />
          </svg>
        </div>

        {/* Tag */}
        <div
          style={{
            position: 'absolute',
            left: 0,
            right: 0,
            top: 1470,
            display: 'flex',
            justifyContent: 'center',
            transform: `scale(${0.6 + tagIn * 0.4})`,
            opacity: Math.min(1, tagIn * 1.5),
          }}
        >
          <div style={{background: RED, color: WHITE, fontWeight: 800, fontSize: 60, padding: '24px 52px', borderRadius: 20, boxShadow: '0 24px 50px rgba(226,53,43,0.35)', whiteSpace: 'nowrap'}}>
            {tag}
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
