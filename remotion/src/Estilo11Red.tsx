import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {FONT_MARCA, PALETA} from './marca';

// ─── Estilo #11 · "Red que colapsa" (BR1: todo depende de una persona) ──────
// Panel con un nodo-persona central conectado a chips; el nodo se arranca y
// los chips caen a "?" con glitch. Tag rojo final.
export const estilo11RedSchema = z.object({
  titulo: z.string(),
  chips: z.array(z.string()).length(4),
  tag: z.string(),
});
type Props = z.infer<typeof estilo11RedSchema>;
export const estilo11RedDefaults: Props = {
  titulo: 'TU NEGOCIO',
  chips: ['PROCESOS', 'CLIENTES', 'PROVEEDORES', 'CLAVES'],
  tag: 'TODO EN UNA SOLA PERSONA',
};

const GRID = PALETA.grid;
const INK = PALETA.ink;
const RED = PALETA.rojo;
const WHITE = PALETA.blanco;

const YANK_FRAME = 34; // cuando se arranca el nodo persona

export const Estilo11Red: React.FC<Props> = ({titulo, chips, tag}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const camScale = interpolate(frame, [0, 96], [1, 1.06]);
  const panelIn = spring({frame, fps, config: {damping: 14, stiffness: 130}});
  const yank = spring({frame: frame - YANK_FRAME, fps, config: {damping: 12, stiffness: 160}});
  const tagIn = spring({frame: frame - 50, fps, config: {damping: 9, stiffness: 170}});
  const dead = frame >= YANK_FRAME + 4;

  const CX = 540;
  const CY = 830;
  const chipPos = [
    {x: CX - 250, y: CY - 260},
    {x: CX + 250, y: CY - 260},
    {x: CX - 250, y: CY + 240},
    {x: CX + 250, y: CY + 240},
  ];

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
            top: 340,
            height: 1050,
            borderRadius: 36,
            background: 'rgba(255,255,255,0.62)',
            border: '1.5px solid rgba(255,255,255,0.9)',
            boxShadow: '0 40px 80px rgba(0,0,0,0.13)',
            transform: `translateY(${(1 - panelIn) * 80}px)`,
            opacity: Math.min(1, panelIn * 1.4),
          }}
        >
          <div style={{position: 'absolute', left: 60, top: 46, background: INK, color: WHITE, fontWeight: 800, fontSize: 34, letterSpacing: 1.5, padding: '12px 26px', borderRadius: 12}}>
            {titulo}
          </div>
        </div>

        {/* Conexiones */}
        <svg width={1080} height={1920} style={{position: 'absolute', inset: 0}}>
          {chipPos.map((c, i) => (
            <line
              key={i}
              x1={CX}
              y1={CY}
              x2={c.x}
              y2={c.y}
              stroke={dead ? 'rgba(17,17,17,0.15)' : 'rgba(17,17,17,0.45)'}
              strokeWidth={4}
              strokeDasharray={dead ? '10 14' : '2 0'}
            />
          ))}
        </svg>

        {/* Chips */}
        {chipPos.map((c, i) => {
          const chipIn = spring({frame: frame - (6 + i * 3), fps, config: {damping: 12, stiffness: 140}});
          const shake = dead ? Math.sin((frame - YANK_FRAME) * 2 + i) * Math.max(0, 6 - (frame - YANK_FRAME) * 0.3) : 0;
          return (
            <div
              key={i}
              style={{
                position: 'absolute',
                left: c.x - 150,
                top: c.y - 48 + shake,
                width: 300,
                height: 96,
                borderRadius: 16,
                background: dead ? '#D9D9D9' : WHITE,
                border: `2px solid ${dead ? RED : 'rgba(17,17,17,0.25)'}`,
                boxShadow: '0 14px 30px rgba(0,0,0,0.12)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontWeight: 800,
                fontSize: 34,
                letterSpacing: 1,
                color: dead ? RED : INK,
                transform: `scale(${0.8 + chipIn * 0.2})`,
                opacity: Math.min(1, chipIn * 1.5),
              }}
            >
              {dead ? '?' : chips[i]}
            </div>
          );
        })}

        {/* Nodo persona (se arranca) */}
        <div
          style={{
            position: 'absolute',
            left: CX - 110,
            top: CY - 110 - yank * 900,
            width: 220,
            height: 220,
            borderRadius: '50%',
            background: INK,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            boxShadow: '0 24px 50px rgba(0,0,0,0.25)',
            transform: `rotate(${yank * -14}deg)`,
            opacity: 1 - yank * 0.15,
          }}
        >
          {/* silueta persona simple */}
          <svg width={110} height={110} viewBox="0 0 100 100">
            <circle cx={50} cy={34} r={20} fill={WHITE} />
            <path d="M 15 95 Q 15 60 50 60 Q 85 60 85 95 Z" fill={WHITE} />
          </svg>
        </div>

        {/* Tag */}
        <div
          style={{
            position: 'absolute',
            left: 0,
            right: 0,
            top: 1520,
            display: 'flex',
            justifyContent: 'center',
            transform: `scale(${0.6 + tagIn * 0.4})`,
            opacity: Math.min(1, tagIn * 1.5),
          }}
        >
          <div style={{background: RED, color: WHITE, fontWeight: 800, fontSize: 54, padding: '24px 48px', borderRadius: 20, boxShadow: '0 24px 50px rgba(226,53,43,0.35)', whiteSpace: 'nowrap'}}>
            {tag}
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
