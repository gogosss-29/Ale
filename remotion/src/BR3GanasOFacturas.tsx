import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
import {z} from 'zod';
import {FONT_MARCA, PALETA} from './marca';

// ─── Estilo #11 · Premium Data Motion — chart "barras vs línea plana" ────────
// Parametrizable: chip, meses, alturas, label de la línea y tag final.
export const estilo11ChartSchema = z.object({
  chipLabel: z.string(),
  meses: z.array(z.string()).length(6),
  alturas: z.array(z.number().min(0.05).max(1)).length(6),
  lineaLabel: z.string(),
  tag: z.string(),
});
type Props = z.infer<typeof estilo11ChartSchema>;

export const estilo11ChartDefaults: Props = {
  chipLabel: 'FACTURACIÓN',
  meses: ['ENE', 'FEB', 'MAR', 'ABR', 'MAY', 'JUN'],
  alturas: [0.42, 0.53, 0.64, 0.75, 0.87, 1],
  lineaLabel: 'GANANCIA',
  tag: '¿GANÁS O SOLO FACTURÁS?',
};

const GRID_BG = PALETA.grid;
const INK = PALETA.ink;
const RED = PALETA.rojo;
const WHITE = PALETA.blanco;

export const BR3GanasOFacturas: React.FC<Props> = ({chipLabel, meses, alturas, lineaLabel, tag}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();

  const camScale = interpolate(frame, [0, 96], [1, 1.055]);
  const panelIn = spring({frame, fps, config: {damping: 14, stiffness: 120}});
  const lineDraw = interpolate(frame, [16, 36], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const arrowIn = spring({frame: frame - 38, fps, config: {damping: 11, stiffness: 150}});
  const tagIn = spring({frame: frame - 46, fps, config: {damping: 9, stiffness: 170}});
  const goboX = interpolate(frame, [0, 96], [-80, 60]);

  // Tag: achica la fuente si el texto es largo
  const tagSize = Math.min(58, Math.floor(1750 / Math.max(10, tag.length)));

  return (
    <AbsoluteFill style={{backgroundColor: GRID_BG, fontFamily: FONT_MARCA, overflow: 'hidden'}}>
      <AbsoluteFill
        style={{
          backgroundImage: `
            linear-gradient(to right, rgba(0,0,0,0.055) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(0,0,0,0.055) 1px, transparent 1px),
            linear-gradient(to right, rgba(0,0,0,0.10) 2px, transparent 2px),
            linear-gradient(to bottom, rgba(0,0,0,0.10) 2px, transparent 2px)`,
          backgroundSize: '54px 54px, 54px 54px, 270px 270px, 270px 270px',
        }}
      />
      <div
        style={{
          position: 'absolute',
          top: -300,
          left: goboX,
          width: 1400,
          height: 900,
          background:
            'radial-gradient(ellipse 45% 60% at 40% 40%, rgba(0,0,0,0.10), transparent 70%)',
          filter: 'blur(30px)',
          transform: 'rotate(-18deg)',
        }}
      />
      <AbsoluteFill
        style={{
          background:
            'radial-gradient(ellipse 75% 65% at 50% 46%, transparent 60%, rgba(0,0,0,0.10) 100%)',
        }}
      />

      <AbsoluteFill style={{transform: `scale(${camScale})`, transformOrigin: '50% 46%'}}>
        <Pushpin x={950} y={150} />
        <Paperclip x={70} y={1690} />

        <div
          style={{
            position: 'absolute',
            left: 70,
            right: 70,
            top: 330,
            height: 1100,
            borderRadius: 36,
            background: 'rgba(255,255,255,0.62)',
            border: '1.5px solid rgba(255,255,255,0.9)',
            boxShadow: '0 40px 80px rgba(0,0,0,0.13), 0 6px 18px rgba(0,0,0,0.07)',
            backdropFilter: 'blur(6px)',
            transform: `translateY(${(1 - panelIn) * 90}px)`,
            opacity: Math.min(1, panelIn * 1.4),
            padding: '54px 60px 40px',
          }}
        >
          <Chip bg={INK} color={WHITE} inAt={4} frame={frame} fps={fps} style={{position: 'absolute', left: 60, top: 48}}>
            {chipLabel}
          </Chip>

          <Chart frame={frame} fps={fps} lineDraw={lineDraw} arrowIn={arrowIn} meses={meses} alturas={alturas} lineaLabel={lineaLabel} />
        </div>

        <div
          style={{
            position: 'absolute',
            left: 0,
            right: 0,
            top: 1510,
            display: 'flex',
            justifyContent: 'center',
            transform: `scale(${0.6 + tagIn * 0.4})`,
            opacity: Math.min(1, tagIn * 1.5),
          }}
        >
          <div
            style={{
              background: RED,
              color: WHITE,
              fontWeight: 800,
              fontSize: tagSize,
              letterSpacing: 0.5,
              padding: '26px 52px',
              borderRadius: 20,
              boxShadow: '0 24px 50px rgba(226,53,43,0.35)',
              whiteSpace: 'nowrap',
            }}
          >
            {tag}
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

const Chart: React.FC<{
  frame: number;
  fps: number;
  lineDraw: number;
  arrowIn: number;
  meses: string[];
  alturas: number[];
  lineaLabel: string;
}> = ({frame, fps, lineDraw, arrowIn, meses, alturas, lineaLabel}) => {
  const chartW = 820;
  const chartH = 760;
  const baseY = 900;
  const barW = 92;
  const gap = (chartW - barW * 6) / 5;
  const lineY = baseY - 64;

  return (
    <div style={{position: 'absolute', left: 60, top: 150, width: chartW, height: baseY + 70}}>
      {alturas.map((h, i) => {
        const grow = spring({frame: frame - (6 + i * 3), fps, config: {damping: 13, stiffness: 110}});
        const barH = h * chartH * grow;
        return (
          <div key={i}>
            <div
              style={{
                position: 'absolute',
                left: i * (barW + gap),
                top: baseY - barH,
                width: barW,
                height: barH,
                background: INK,
                borderRadius: '10px 10px 4px 4px',
                boxShadow: '14px 18px 28px rgba(0,0,0,0.18)',
              }}
            />
            <div
              style={{
                position: 'absolute',
                left: i * (barW + gap),
                top: baseY + 18,
                width: barW,
                textAlign: 'center',
                fontWeight: 700,
                fontSize: 30,
                color: 'rgba(17,17,17,0.55)',
                letterSpacing: 1,
              }}
            >
              {meses[i]}
            </div>
          </div>
        );
      })}

      <div
        style={{
          position: 'absolute',
          left: 0,
          top: lineY,
          width: chartW * lineDraw,
          height: 10,
          background: RED,
          borderRadius: 6,
          boxShadow: '0 0 22px rgba(226,53,43,0.55)',
        }}
      />
      <div
        style={{
          position: 'absolute',
          left: 0,
          top: lineY + 24,
          opacity: lineDraw > 0.35 ? 1 : 0,
          background: RED,
          color: WHITE,
          fontWeight: 800,
          fontSize: 30,
          padding: '8px 18px',
          borderRadius: 10,
          letterSpacing: 1,
        }}
      >
        {lineaLabel}
      </div>

      <svg
        width={150}
        height={620}
        viewBox="0 0 150 620"
        style={{
          position: 'absolute',
          left: chartW - 275,
          top: baseY - alturas[5] * chartH - 10,
          opacity: Math.min(1, arrowIn * 1.4),
          transform: `scale(${0.7 + arrowIn * 0.3})`,
          transformOrigin: '50% 50%',
        }}
      >
        <defs>
          <marker id="ah" markerWidth="9" markerHeight="9" refX="4.5" refY="4.5" orient="auto">
            <path d="M0,0 L9,4.5 L0,9 z" fill={RED} />
          </marker>
        </defs>
        <line x1={75} y1={30} x2={75} y2={560} stroke={RED} strokeWidth={11} markerStart="url(#ah)" markerEnd="url(#ah)" strokeDasharray="2 0" />
      </svg>
    </div>
  );
};

const Chip: React.FC<{
  bg: string;
  color: string;
  inAt: number;
  frame: number;
  fps: number;
  style?: React.CSSProperties;
  children: React.ReactNode;
}> = ({bg, color, inAt, frame, fps, style, children}) => {
  const s = spring({frame: frame - inAt, fps, config: {damping: 12, stiffness: 140}});
  return (
    <div
      style={{
        background: bg,
        color,
        fontWeight: 800,
        fontSize: 34,
        letterSpacing: 1.5,
        padding: '12px 26px',
        borderRadius: 12,
        display: 'inline-block',
        transform: `translateY(${(1 - s) * -30}px)`,
        opacity: Math.min(1, s * 1.4),
        boxShadow: '0 10px 24px rgba(0,0,0,0.15)',
        ...style,
      }}
    >
      {children}
    </div>
  );
};

const Pushpin: React.FC<{x: number; y: number}> = ({x, y}) => (
  <div style={{position: 'absolute', left: x, top: y}}>
    <div
      style={{
        width: 46,
        height: 46,
        borderRadius: '50%',
        background: `radial-gradient(circle at 35% 30%, #F0655B, ${RED} 60%, #A32017)`,
        boxShadow: '10px 22px 26px rgba(0,0,0,0.30)',
      }}
    />
    <div
      style={{
        position: 'absolute',
        left: 20,
        top: 42,
        width: 5,
        height: 26,
        background: 'linear-gradient(to bottom, #999, #555)',
        transform: 'rotate(14deg)',
      }}
    />
  </div>
);

const Paperclip: React.FC<{x: number; y: number}> = ({x, y}) => (
  <div
    style={{
      position: 'absolute',
      left: x,
      top: y,
      width: 46,
      height: 110,
      border: '7px solid #A9ACB2',
      borderRadius: 26,
      transform: 'rotate(-24deg)',
      boxShadow: '8px 14px 18px rgba(0,0,0,0.16)',
      opacity: 0.9,
    }}
  />
);
