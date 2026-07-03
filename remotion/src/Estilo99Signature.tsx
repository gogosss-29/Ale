import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';

// ─── Estilo #99 · Cerebro Signature (insignia de marca) ─────────────────────
// Spec: grafito + oro fundido. SIGNATURE MOVE: fragmentos caóticos del negocio
// son atraídos por líneas doradas que se dibujan solas y los ordenan en una
// estructura limpia. Glifo Cerebro late al cerrar el orden.
const GRAPHITE = '#14161A';
const BONE = '#F2EEE6';
const GOLD = '#E8B04B';
const FONT = "Arial, 'Liberation Sans', 'Helvetica Neue', sans-serif";

// Fragmentos: posición caótica inicial → slot ordenado en el panel
const FRAGS = [
  {cx: -380, cy: -640, rot: -28, slot: 0, label: '$ 1.240'},
  {cx: 420, cy: -580, rot: 22, slot: 1, label: 'VENTAS'},
  {cx: -460, cy: 180, rot: 14, slot: 2, label: 'COSTOS'},
  {cx: 470, cy: 260, rot: -18, slot: 3, label: '37%'},
  {cx: -330, cy: 620, rot: 24, slot: 4, label: 'CLIENTES'},
  {cx: 400, cy: 660, rot: -12, slot: 5, label: 'MARGEN'},
];
// Slots ordenados (grilla 2×3 dentro del panel, coords relativas al centro)
const SLOTS = [
  {x: -150, y: -120},
  {x: 150, y: -120},
  {x: -150, y: 0},
  {x: 150, y: 0},
  {x: -150, y: 120},
  {x: 150, y: 120},
];

export const Estilo99Signature: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const camScale = interpolate(frame, [0, 96], [1.04, 1.1]);
  const panelIn = spring({frame: frame - 20, fps, config: {damping: 14, stiffness: 90}});
  const glyphPulse = spring({frame: frame - 52, fps, config: {damping: 7, stiffness: 160}});
  const textIn = spring({frame: frame - 58, fps, config: {damping: 10, stiffness: 150}});
  const lineDraw = interpolate(frame, [14, 46], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const CX = 540;
  const CY = 820; // centro del panel

  return (
    <AbsoluteFill style={{backgroundColor: GRAPHITE, fontFamily: FONT, overflow: 'hidden'}}>
      {/* Glow ambiente dorado + viñeta cálida */}
      <AbsoluteFill
        style={{
          background: `radial-gradient(ellipse 70% 45% at 50% 42%, rgba(232,176,75,0.10), transparent 70%),
                       radial-gradient(ellipse 90% 80% at 50% 50%, transparent 55%, rgba(0,0,0,0.5) 100%)`,
        }}
      />
      {/* Partículas de tinta flotando */}
      {[...Array(14)].map((_, i) => {
        const px = (i * 397) % 1080;
        const py = (i * 641) % 1920;
        const drift = Math.sin((frame + i * 31) / 40) * 14;
        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              left: px,
              top: py + drift,
              width: 3 + (i % 3) * 2,
              height: 3 + (i % 3) * 2,
              borderRadius: '50%',
              background: 'rgba(232,176,75,0.22)',
              filter: 'blur(1px)',
            }}
          />
        );
      })}

      <AbsoluteFill style={{transform: `scale(${camScale})`, transformOrigin: '50% 45%'}}>
        {/* Líneas doradas que se dibujan (del centro hacia cada slot) */}
        <svg
          width={1080}
          height={1920}
          viewBox="0 0 1080 1920"
          style={{position: 'absolute', inset: 0}}
        >
          {SLOTS.map((s, i) => {
            const x2 = CX + s.x;
            const y2 = CY + s.y;
            const len = Math.hypot(s.x, s.y) * 1.4;
            const drawn = Math.max(0, Math.min(1, lineDraw * 1.6 - i * 0.1));
            return (
              <path
                key={i}
                d={`M ${CX} ${CY - 320} Q ${CX + s.x * 0.4} ${CY - 160 + s.y * 0.3}, ${x2} ${y2}`}
                stroke={GOLD}
                strokeWidth={3.5}
                fill="none"
                strokeLinecap="round"
                strokeDasharray={len}
                strokeDashoffset={len * (1 - drawn)}
                style={{filter: 'drop-shadow(0 0 8px rgba(232,176,75,0.65))'}}
                opacity={0.9}
              />
            );
          })}
        </svg>

        {/* Panel de orden (estructura limpia) */}
        <div
          style={{
            position: 'absolute',
            left: CX - 285,
            top: CY - 200,
            width: 570,
            height: 400,
            borderRadius: 26,
            border: `2px solid rgba(232,176,75,${0.35 + panelIn * 0.5})`,
            background: 'rgba(232,176,75,0.05)',
            boxShadow: `0 0 ${30 + panelIn * 40}px rgba(232,176,75,0.16), inset 0 0 40px rgba(232,176,75,0.05)`,
            opacity: Math.min(1, panelIn * 1.3),
          }}
        />

        {/* Fragmentos: caos → orden */}
        {FRAGS.map((f, i) => {
          const move = spring({frame: frame - (8 + i * 3), fps, config: {damping: 13, stiffness: 70}});
          const slot = SLOTS[f.slot];
          const x = interpolate(move, [0, 1], [CX + f.cx, CX + slot.x]);
          const y = interpolate(move, [0, 1], [CY + f.cy, CY + slot.y]);
          const rot = interpolate(move, [0, 1], [f.rot, 0]);
          const settled = move > 0.92;
          return (
            <div
              key={i}
              style={{
                position: 'absolute',
                left: x - 118,
                top: y - 42,
                width: 236,
                height: 84,
                borderRadius: 14,
                background: settled ? 'rgba(242,238,230,0.10)' : 'rgba(242,238,230,0.06)',
                border: `1.5px solid ${settled ? 'rgba(232,176,75,0.75)' : 'rgba(242,238,230,0.30)'}`,
                boxShadow: settled ? '0 0 24px rgba(232,176,75,0.25)' : '0 10px 26px rgba(0,0,0,0.4)',
                transform: `rotate(${rot}deg)`,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: settled ? BONE : 'rgba(242,238,230,0.55)',
                fontWeight: 700,
                fontSize: 30,
                letterSpacing: 2,
              }}
            >
              {f.label}
            </div>
          );
        })}

        {/* Glifo Cerebro (nodo + órbitas) que late */}
        <svg
          width={220}
          height={220}
          viewBox="0 0 220 220"
          style={{
            position: 'absolute',
            left: CX - 110,
            top: CY - 320 - 110,
            transform: `scale(${1 + glyphPulse * 0.22})`,
            opacity: 0.4 + Math.min(0.6, glyphPulse),
            filter: `drop-shadow(0 0 ${10 + glyphPulse * 26}px rgba(232,176,75,0.8))`,
          }}
        >
          <circle cx={110} cy={110} r={34} fill={GOLD} />
          <circle cx={110} cy={110} r={62} fill="none" stroke={GOLD} strokeWidth={2.5} opacity={0.65} />
          <circle cx={110} cy={110} r={88} fill="none" stroke={GOLD} strokeWidth={1.5} opacity={0.35} />
          {[0, 120, 240].map((deg) => {
            const rad = ((deg + frame * 1.2) * Math.PI) / 180;
            return (
              <circle
                key={deg}
                cx={110 + Math.cos(rad) * 62}
                cy={110 + Math.sin(rad) * 62}
                r={8}
                fill={GOLD}
              />
            );
          })}
        </svg>

        {/* Texto firma */}
        <div
          style={{
            position: 'absolute',
            left: 0,
            right: 0,
            top: CY + 300,
            textAlign: 'center',
            transform: `translateY(${(1 - textIn) * 40}px)`,
            opacity: Math.min(1, textIn * 1.5),
          }}
        >
          <span style={{color: BONE, fontWeight: 800, fontSize: 74, letterSpacing: 3}}>
            DEL CAOS AL{' '}
          </span>
          <span
            style={{
              color: GOLD,
              fontWeight: 900,
              fontSize: 74,
              letterSpacing: 3,
              textShadow: '0 0 40px rgba(232,176,75,0.55)',
            }}
          >
            ORDEN
          </span>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
