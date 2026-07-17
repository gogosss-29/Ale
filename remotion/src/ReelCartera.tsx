import React from 'react';
import {
  AbsoluteFill,
  Audio,
  OffthreadVideo,
  Sequence,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {z} from 'zod';
import {FONT_MARCA, PALETA} from './marca';

// ─── Reel Cartera · ensamblado 9:16 para talking-head financiero ─────────────
// Lienzo 1080x1920 con el clip 1080x1560 centrado: la franja superior lleva el
// header persistente y las tarjetas de datos sincronizadas con la locución; la
// franja inferior lleva los captions palabra-por-palabra. Cierra con outro de
// marca (glifo + CTA). Los datos van por props: números exactos, cero regen.

const GRAPHITE = PALETA.grafito;
const BONE = PALETA.hueso;
const GOLD = PALETA.oro;
const INK = PALETA.ink;
const WHITE = PALETA.blanco;
const VERDE = PALETA.verde;

const tokenSchema = z.object({text: z.string(), fromMs: z.number(), toMs: z.number()});
const pageSchema = z.object({
  startMs: z.number(),
  endMs: z.number(),
  tokens: z.array(tokenSchema),
});

export const reelCarteraSchema = z.object({
  videoSrc: z.string(),
  videoDurationMs: z.number(),
  outroMs: z.number(),
  header: z.array(z.string()).length(3),
  pages: z.array(pageSchema),
  onCard: z.object({
    showMs: z.number(),
    hideMs: z.number(),
    chip: z.string(),
    titulo: z.string(),
    monto: z.string(),
    rentaMs: z.number(),
    renta: z.string(),
  }),
  compras: z.array(z.object({showMs: z.number(), label: z.string(), monto: z.string()})),
  totalMs: z.number(),
  totalLabel: z.string(),
  totalMonto: z.string(),
  hideComprasMs: z.number(),
  outro: z.object({linea: z.string(), cta: z.string(), cta2: z.string()}),
  musicSrc: z.string().nullable(),
});
export type ReelCarteraProps = z.infer<typeof reelCarteraSchema>;

export const reelCarteraDefaults: ReelCarteraProps = {
  videoSrc: 'clips/5mil-usd.mp4',
  videoDurationMs: 53340,
  outroMs: 2800,
  header: ['CARTERA REAL', 'USD 5.000', 'PERFIL MODERADO'],
  pages: [],
  onCard: {
    showMs: 4300,
    hideMs: 13800,
    chip: 'YA EN CARTERA',
    titulo: 'ON TELECOM · TLCMO',
    monto: 'AR$ 10.000.000',
    rentaMs: 10300,
    renta: 'RENTA 9% ANUAL EN USD',
  },
  compras: [],
  totalMs: 44900,
  totalLabel: 'TOTAL',
  totalMonto: 'USD 5.000',
  hideComprasMs: 50200,
  outro: {linea: 'SEGUIMIENTO · 6 MESES', cta: '¿VOS QUÉ LE SUMARÍAS?', cta2: 'COMENTÁ 👇'},
  musicSrc: null,
};

const VIDEO_TOP = 180;
const VIDEO_H = 1560;

export const ReelCartera: React.FC<ReelCarteraProps> = (props) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const tMs = (frame / fps) * 1000;
  const videoFrames = Math.round((props.videoDurationMs / 1000) * fps);

  return (
    <AbsoluteFill style={{backgroundColor: GRAPHITE, fontFamily: FONT_MARCA, overflow: 'hidden'}}>
      {/* Clip del avatar (con su audio) */}
      <Sequence from={0} durationInFrames={videoFrames}>
        <VideoLayer src={props.videoSrc} videoFrames={videoFrames} />
      </Sequence>

      {/* Música de fondo con ducking: baja bajo la voz, sube en el outro */}
      {props.musicSrc ? (
        <MusicBed src={props.musicSrc} videoFrames={videoFrames} hasOutro={props.outroMs > 0} />
      ) : null}

      {tMs < props.videoDurationMs ? (
        <>
          <Header header={props.header} frame={frame} fps={fps} />
          <OnCard card={props.onCard} tMs={tMs} frame={frame} fps={fps} />
          <ComprasStack
            compras={props.compras}
            totalMs={props.totalMs}
            totalLabel={props.totalLabel}
            totalMonto={props.totalMonto}
            hideMs={props.hideComprasMs}
            tMs={tMs}
            frame={frame}
            fps={fps}
          />
          <Captions pages={props.pages} tMs={tMs} frame={frame} fps={fps} />
        </>
      ) : null}

      {/* Outro de marca (opcional: outroMs = 0 lo desactiva) */}
      {props.outroMs > 0 ? (
        <Sequence from={videoFrames - 6}>
          <Outro outro={props.outro} fps={fps} />
        </Sequence>
      ) : null}

      {/* Viñeta global sutil */}
      <AbsoluteFill
        style={{
          pointerEvents: 'none',
          background:
            'radial-gradient(ellipse 95% 85% at 50% 48%, transparent 62%, rgba(0,0,0,0.32) 100%)',
        }}
      />
    </AbsoluteFill>
  );
};

const DUCK = 0.22; // nivel bajo la voz
const ALTO = 0.5; // nivel en el outro

const MusicBed: React.FC<{src: string; videoFrames: number; hasOutro: boolean}> = ({
  src,
  videoFrames,
  hasOutro,
}) => {
  const {durationInFrames} = useVideoConfig();
  const curva: [number[], number[]] = hasOutro
    ? [
        [0, 18, videoFrames - 6, videoFrames + 16, durationInFrames - 14, durationInFrames - 1],
        [0, DUCK, DUCK, ALTO, ALTO, 0],
      ]
    : [
        [0, 18, durationInFrames - 20, durationInFrames - 1],
        [0, DUCK, DUCK, 0],
      ];
  return (
    <Audio
      src={staticFile(src)}
      volume={(f) =>
        interpolate(f, curva[0], curva[1], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'})
      }
    />
  );
};

const VideoLayer: React.FC<{src: string; videoFrames: number}> = ({src, videoFrames}) => {
  const frame = useCurrentFrame();
  const fadeOut = interpolate(frame, [videoFrames - 8, videoFrames - 1], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  return (
    <div
      style={{
        position: 'absolute',
        left: 0,
        top: VIDEO_TOP,
        width: 1080,
        height: VIDEO_H,
        borderRadius: 30,
        overflow: 'hidden',
        boxShadow: '0 30px 80px rgba(0,0,0,0.55)',
        opacity: fadeOut,
      }}
    >
      <OffthreadVideo src={staticFile(src)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
    </div>
  );
};

// ─── Header persistente (franja superior) ───────────────────────────────────
// Zona segura IG: los íconos superiores viven en los ~130px de arriba; el
// header se apoya contra el borde del video, despejado de las esquinas.
const Header: React.FC<{header: string[]; frame: number; fps: number}> = ({header, frame, fps}) => {
  const inS = spring({frame: frame - 8, fps, config: {damping: 14, stiffness: 120}});
  return (
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        top: 92,
        height: VIDEO_TOP - 92,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        gap: 26,
        opacity: Math.min(1, inS * 1.4),
        transform: `translateY(${(1 - inS) * -24}px)`,
      }}
    >
      {header.map((part, i) => (
        <React.Fragment key={i}>
          {i > 0 ? (
            <div style={{width: 7, height: 7, borderRadius: '50%', background: GOLD, opacity: 0.8}} />
          ) : null}
          <span
            style={{
              color: i === 1 ? GOLD : BONE,
              fontWeight: i === 1 ? 900 : 700,
              fontSize: 33,
              letterSpacing: 4.5,
              opacity: i === 1 ? 1 : 0.85,
              textShadow: i === 1 ? '0 0 26px rgba(232,176,75,0.4)' : 'none',
            }}
          >
            {part}
          </span>
        </React.Fragment>
      ))}
    </div>
  );
};

// ─── Tarjeta ON (posición ya activa) ────────────────────────────────────────
const OnCard: React.FC<{
  card: ReelCarteraProps['onCard'];
  tMs: number;
  frame: number;
  fps: number;
}> = ({card, tMs, frame, fps}) => {
  if (tMs < card.showMs || tMs > card.hideMs + 400) return null;
  const showFrame = Math.round((card.showMs / 1000) * fps);
  const inS = spring({frame: frame - showFrame, fps, config: {damping: 13, stiffness: 130}});
  const out = interpolate(tMs, [card.hideMs, card.hideMs + 350], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const rentaFrame = Math.round((card.rentaMs / 1000) * fps);
  const rentaS = spring({frame: frame - rentaFrame, fps, config: {damping: 10, stiffness: 200}});

  return (
    <div
      style={{
        position: 'absolute',
        left: 70,
        top: 250,
        transform: `translateY(${(1 - inS) * -50}px)`,
        opacity: Math.min(1, inS * 1.4) * out,
      }}
    >
      <div
        style={{
          background: 'rgba(255,255,255,0.93)',
          border: '1.5px solid rgba(255,255,255,0.95)',
          borderRadius: 22,
          padding: '24px 30px 22px',
          boxShadow: '0 26px 60px rgba(0,0,0,0.35)',
          display: 'flex',
          flexDirection: 'column',
          gap: 12,
        }}
      >
        <div
          style={{
            alignSelf: 'flex-start',
            background: INK,
            color: WHITE,
            fontWeight: 800,
            fontSize: 23,
            letterSpacing: 2.5,
            padding: '7px 16px',
            borderRadius: 9,
          }}
        >
          {card.chip}
        </div>
        <div style={{color: INK, fontWeight: 900, fontSize: 40, letterSpacing: 0.5}}>{card.titulo}</div>
        <div style={{color: 'rgba(17,17,17,0.72)', fontWeight: 700, fontSize: 32}}>{card.monto}</div>
        {tMs >= card.rentaMs ? (
          <div
            style={{
              alignSelf: 'flex-start',
              background: VERDE,
              color: WHITE,
              fontWeight: 800,
              fontSize: 27,
              letterSpacing: 1,
              padding: '10px 18px',
              borderRadius: 11,
              boxShadow: '0 10px 26px rgba(31,184,91,0.4)',
              transform: `scale(${0.7 + Math.min(1, rentaS) * 0.3})`,
              opacity: Math.min(1, rentaS * 1.5),
            }}
          >
            {card.renta}
          </div>
        ) : null}
      </div>
    </div>
  );
};

// ─── Stack de compras (se construye la cartera) ─────────────────────────────
const ComprasStack: React.FC<{
  compras: ReelCarteraProps['compras'];
  totalMs: number;
  totalLabel: string;
  totalMonto: string;
  hideMs: number;
  tMs: number;
  frame: number;
  fps: number;
}> = ({compras, totalMs, totalLabel, totalMonto, hideMs, tMs, frame, fps}) => {
  const visibles = compras.filter((c) => tMs >= c.showMs);
  if (visibles.length === 0) return null;
  const out = interpolate(tMs, [hideMs, hideMs + 350], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        position: 'absolute',
        right: 44,
        top: 250,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'flex-end',
        gap: 14,
        opacity: out,
      }}
    >
      {visibles.map((c, i) => {
        const showFrame = Math.round((c.showMs / 1000) * fps);
        const s = spring({frame: frame - showFrame, fps, config: {damping: 11, stiffness: 170}});
        return (
          <div
            key={i}
            style={{
              display: 'flex',
              alignItems: 'baseline',
              gap: 16,
              background: 'rgba(17,17,17,0.88)',
              border: '1.5px solid rgba(242,238,230,0.18)',
              borderRadius: 14,
              padding: '15px 22px',
              boxShadow: '0 14px 34px rgba(0,0,0,0.4)',
              transform: `translateX(${(1 - s) * 90}px) scale(${0.75 + Math.min(1, s) * 0.25})`,
              transformOrigin: '100% 50%',
              opacity: Math.min(1, s * 1.4),
            }}
          >
            <span style={{color: BONE, fontWeight: 800, fontSize: 30, letterSpacing: 1}}>{c.label}</span>
            <span style={{color: GOLD, fontWeight: 900, fontSize: 30, letterSpacing: 0.5}}>{c.monto}</span>
          </div>
        );
      })}
      {tMs >= totalMs ? <TotalChip label={totalLabel} monto={totalMonto} totalMs={totalMs} frame={frame} fps={fps} /> : null}
    </div>
  );
};

const TotalChip: React.FC<{label: string; monto: string; totalMs: number; frame: number; fps: number}> = ({
  label,
  monto,
  totalMs,
  frame,
  fps,
}) => {
  const showFrame = Math.round((totalMs / 1000) * fps);
  const s = spring({frame: frame - showFrame, fps, config: {damping: 9, stiffness: 190}});
  return (
    <div
      style={{
        display: 'flex',
        alignItems: 'baseline',
        gap: 16,
        background: GOLD,
        borderRadius: 14,
        padding: '16px 24px',
        boxShadow: '0 0 40px rgba(232,176,75,0.45), 0 14px 34px rgba(0,0,0,0.35)',
        transform: `translateX(${(1 - s) * 90}px) scale(${0.7 + Math.min(1, s) * 0.3})`,
        transformOrigin: '100% 50%',
        opacity: Math.min(1, s * 1.5),
      }}
    >
      <span style={{color: GRAPHITE, fontWeight: 800, fontSize: 30, letterSpacing: 2}}>{label}</span>
      <span style={{color: GRAPHITE, fontWeight: 900, fontSize: 34}}>{monto}</span>
    </div>
  );
};

// ─── Captions palabra-por-palabra (franja inferior) ─────────────────────────
const Captions: React.FC<{
  pages: ReelCarteraProps['pages'];
  tMs: number;
  frame: number;
  fps: number;
}> = ({pages, tMs, frame, fps}) => {
  const page = pages.find((p) => tMs >= p.startMs && tMs < p.endMs + 150);
  if (!page) return null;
  const pageStartFrame = Math.round((page.startMs / 1000) * fps);
  const inS = spring({frame: frame - pageStartFrame, fps, config: {damping: 12, stiffness: 240}});
  const chars = page.tokens.map((t) => t.text).join(' ').length;
  const fontSize = Math.min(54, Math.floor(1360 / Math.max(14, chars)));

  // Zona segura IG: por encima de los ~420px inferiores (usuario/caption/audio)
  // y con margen derecho para el carril de botones.
  return (
    <div
      style={{
        position: 'absolute',
        left: 110,
        right: 110,
        top: 1320,
        height: 175,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        columnGap: 26,
        transform: `scale(${0.92 + inS * 0.08}) translateY(${(1 - inS) * 16}px)`,
        opacity: Math.min(1, inS * 1.7),
      }}
    >
      {page.tokens.map((tk, i) => {
        const active = tMs >= tk.fromMs && tMs < tk.toMs + 70;
        return (
          <span
            key={i}
            style={{
              fontWeight: 850 as never,
              fontSize,
              textTransform: 'uppercase',
              letterSpacing: 1.5,
              color: active ? GOLD : BONE,
              transform: active ? 'scale(1.07)' : 'scale(1)',
              textShadow: active
                ? '0 0 30px rgba(232,176,75,0.45), 0 3px 14px rgba(0,0,0,0.65), 0 1px 3px rgba(0,0,0,0.8)'
                : '0 3px 14px rgba(0,0,0,0.65), 0 1px 3px rgba(0,0,0,0.8)',
              whiteSpace: 'pre',
            }}
          >
            {tk.text}
          </span>
        );
      })}
    </div>
  );
};

// ─── Outro: glifo + seguimiento + CTA ───────────────────────────────────────
const Outro: React.FC<{outro: ReelCarteraProps['outro']; fps: number}> = ({outro, fps}) => {
  const frame = useCurrentFrame();
  const bgIn = interpolate(frame, [0, 8], [0, 1], {extrapolateRight: 'clamp'});
  const glyphS = spring({frame: frame - 4, fps, config: {damping: 9, stiffness: 130}});
  const lineaS = spring({frame: frame - 12, fps, config: {damping: 12, stiffness: 150}});
  const ctaS = spring({frame: frame - 20, fps, config: {damping: 10, stiffness: 160}});

  return (
    <AbsoluteFill style={{backgroundColor: GRAPHITE, opacity: bgIn, fontFamily: FONT_MARCA}}>
      <AbsoluteFill
        style={{
          background:
            'radial-gradient(ellipse 70% 45% at 50% 40%, rgba(232,176,75,0.12), transparent 70%)',
        }}
      />
      {/* Glifo Cerebro */}
      <svg
        width={240}
        height={240}
        viewBox="0 0 220 220"
        style={{
          position: 'absolute',
          left: 540 - 120,
          top: 620,
          transform: `scale(${0.7 + glyphS * 0.3})`,
          opacity: Math.min(1, glyphS * 1.4),
          filter: `drop-shadow(0 0 ${14 + glyphS * 22}px rgba(232,176,75,0.7))`,
        }}
      >
        <circle cx={110} cy={110} r={34} fill={GOLD} />
        <circle cx={110} cy={110} r={62} fill="none" stroke={GOLD} strokeWidth={2.5} opacity={0.65} />
        <circle cx={110} cy={110} r={88} fill="none" stroke={GOLD} strokeWidth={1.5} opacity={0.35} />
        {[0, 120, 240].map((deg) => {
          const rad = ((deg + frame * 1.2) * Math.PI) / 180;
          return (
            <circle key={deg} cx={110 + Math.cos(rad) * 62} cy={110 + Math.sin(rad) * 62} r={8} fill={GOLD} />
          );
        })}
      </svg>

      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 940,
          textAlign: 'center',
          color: BONE,
          fontWeight: 700,
          fontSize: 38,
          letterSpacing: 6,
          opacity: Math.min(1, lineaS * 1.4) * 0.85,
          transform: `translateY(${(1 - lineaS) * 30}px)`,
        }}
      >
        {outro.linea}
      </div>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 1030,
          textAlign: 'center',
          color: GOLD,
          fontWeight: 900,
          fontSize: 74,
          letterSpacing: 1,
          textShadow: '0 0 44px rgba(232,176,75,0.5)',
          opacity: Math.min(1, ctaS * 1.4),
          transform: `translateY(${(1 - ctaS) * 40}px) scale(${0.9 + ctaS * 0.1})`,
        }}
      >
        {outro.cta}
      </div>
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          top: 1160,
          textAlign: 'center',
          color: BONE,
          fontWeight: 800,
          fontSize: 46,
          letterSpacing: 3,
          opacity: Math.min(1, ctaS * 1.2) * 0.95,
          transform: `translateY(${(1 - ctaS) * 40}px)`,
        }}
      >
        {outro.cta2}
      </div>
    </AbsoluteFill>
  );
};
