import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';

// ─── Estilo #12 · Dark Tech Reveal (variante UI exacta) ─────────────────────
// Spec: void azul-noche, panel glass con bordes glow cian inclinado en 3D,
// tipografía fina futurista blanca con keyword cian, fragmentos de datos que
// se ensamblan en el dashboard (una sola fuente de verdad).
const VOID = '#0B1A2C';
const CYAN = '#2FD3E3';
const WHITE = '#FFFFFF';
const FONT = "Arial, 'Liberation Sans', 'Helvetica Neue', sans-serif";

export const Estilo12TechReveal: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const panelIn = spring({frame: frame - 4, fps, config: {damping: 15, stiffness: 80}});
  const textIn = spring({frame: frame - 48, fps, config: {damping: 10, stiffness: 150}});
  const glowPulse = 0.5 + Math.sin(frame / 7) * 0.2 + panelIn * 0.3;
  const camDrift = interpolate(frame, [0, 96], [0, -26]);

  return (
    <AbsoluteFill style={{backgroundColor: VOID, fontFamily: FONT, overflow: 'hidden'}}>
      {/* Glow central + viñeta */}
      <AbsoluteFill
        style={{
          background: `radial-gradient(ellipse 65% 40% at 50% 44%, rgba(47,211,227,0.10), transparent 70%),
                       radial-gradient(ellipse 100% 90% at 50% 50%, transparent 55%, rgba(0,0,0,0.55) 100%)`,
        }}
      />
      {/* Partículas */}
      {[...Array(12)].map((_, i) => (
        <div
          key={i}
          style={{
            position: 'absolute',
            left: (i * 431) % 1080,
            top: ((i * 733) % 1920) + Math.sin((frame + i * 20) / 35) * 10,
            width: 3,
            height: 3,
            borderRadius: '50%',
            background: 'rgba(47,211,227,0.30)',
          }}
        />
      ))}

      <AbsoluteFill style={{transform: `translateY(${camDrift}px)`}}>
        {/* Panel glass 3D */}
        <div style={{position: 'absolute', left: 90, top: 560, width: 900, height: 640, perspective: 1400}}>
          <div
            style={{
              width: '100%',
              height: '100%',
              borderRadius: 30,
              background: 'rgba(16,32,50,0.72)',
              border: `2px solid rgba(47,211,227,${0.55 + glowPulse * 0.3})`,
              boxShadow: `0 0 ${40 + glowPulse * 50}px rgba(47,211,227,0.28), 0 60px 110px rgba(0,0,0,0.55), inset 0 0 60px rgba(47,211,227,0.05)`,
              transform: `rotateY(${-16 + panelIn * 6}deg) rotateX(6deg) translateX(${(1 - panelIn) * 420}px)`,
              transformStyle: 'preserve-3d',
              opacity: Math.min(1, panelIn * 1.4),
              padding: 42,
            }}
          >
            {/* Header del dashboard */}
            <div style={{display: 'flex', alignItems: 'center', gap: 16, marginBottom: 34}}>
              <div style={{width: 18, height: 18, borderRadius: '50%', background: CYAN, boxShadow: `0 0 14px ${CYAN}`}} />
              <div style={{color: WHITE, fontWeight: 300, fontSize: 34, letterSpacing: 6}}>TU NEGOCIO</div>
              <div style={{marginLeft: 'auto', display: 'flex', gap: 10}}>
                {[0, 1, 2].map((d) => (
                  <div key={d} style={{width: 44, height: 8, borderRadius: 4, background: 'rgba(255,255,255,0.18)'}} />
                ))}
              </div>
            </div>
            {/* Tiles de datos que se ensamblan */}
            <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 22}}>
              {['VENTAS', 'MARGEN', 'CAJA', 'CLIENTES'].map((label, i) => {
                const tileIn = spring({frame: frame - (14 + i * 5), fps, config: {damping: 12, stiffness: 120}});
                return (
                  <div
                    key={label}
                    style={{
                      height: 150,
                      borderRadius: 16,
                      background: 'rgba(47,211,227,0.07)',
                      border: '1px solid rgba(47,211,227,0.35)',
                      padding: '18px 22px',
                      transform: `translateY(${(1 - tileIn) * 60}px) scale(${0.85 + tileIn * 0.15})`,
                      opacity: Math.min(1, tileIn * 1.5),
                    }}
                  >
                    <div style={{color: 'rgba(255,255,255,0.55)', fontSize: 24, letterSpacing: 4, fontWeight: 300}}>{label}</div>
                    {/* mini barras */}
                    <div style={{display: 'flex', gap: 8, alignItems: 'flex-end', height: 64, marginTop: 14}}>
                      {[0.4, 0.7, 0.55, 0.9, 1].map((h, j) => {
                        const bh = h * 64 * Math.min(1, Math.max(0, tileIn * 1.3 - j * 0.08));
                        return (
                          <div
                            key={j}
                            style={{
                              width: 22,
                              height: bh,
                              borderRadius: 4,
                              background: j === 4 ? CYAN : 'rgba(47,211,227,0.45)',
                              boxShadow: j === 4 ? `0 0 12px rgba(47,211,227,0.7)` : 'none',
                            }}
                          />
                        );
                      })}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>

        {/* Marcador flecha cian + label */}
        <div
          style={{
            position: 'absolute',
            left: 120,
            top: 470,
            display: 'flex',
            alignItems: 'center',
            gap: 14,
            opacity: Math.min(1, spring({frame: frame - 34, fps, config: {damping: 12, stiffness: 140}}) * 1.4),
          }}
        >
          <div
            style={{
              width: 0,
              height: 0,
              borderTop: '14px solid transparent',
              borderBottom: '14px solid transparent',
              borderLeft: `22px solid ${CYAN}`,
              filter: `drop-shadow(0 0 8px ${CYAN})`,
            }}
          />
          <span style={{color: 'rgba(255,255,255,0.75)', fontWeight: 300, fontSize: 30, letterSpacing: 5}}>
            todos tus datos en un solo lugar
          </span>
        </div>

        {/* Texto principal */}
        <div
          style={{
            position: 'absolute',
            left: 0,
            right: 0,
            top: 1300,
            textAlign: 'center',
            transform: `translateY(${(1 - textIn) * 40}px)`,
            opacity: Math.min(1, textIn * 1.5),
            fontWeight: 300,
            fontSize: 62,
            letterSpacing: 8,
            color: WHITE,
          }}
        >
          UNA SOLA FUENTE
          <br />
          DE{' '}
          <span style={{color: CYAN, fontWeight: 600, textShadow: `0 0 34px rgba(47,211,227,0.65)`}}>
            VERDAD
          </span>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
