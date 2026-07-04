// ─── ReelAssembly · Fase 3 ──────────────────────────────────────────────────
// Monta el reel final: clips de avatar (voz = espina de audio) + b-rolls como
// cutaway a pantalla completa + textos + (opcional) música con ducking.
// El montaje es data-driven: editar MONTAJE reordena/retima sin tocar el render.
import React from 'react';
import {
  AbsoluteFill,
  Audio,
  OffthreadVideo,
  Sequence,
  Series,
  interpolate,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from 'remotion';
import {z} from 'zod';
import {FONT_MARCA, PALETA} from './marca';

// Componentes de b-roll ya existentes (se componen como cutaways)
import {Estilo11Red, estilo11RedDefaults} from './Estilo11Red';
import {Estilo11Deriva, estilo11DerivaDefaults} from './Estilo11Deriva';
import {BR3GanasOFacturas, estilo11ChartDefaults} from './BR3GanasOFacturas';
import {Estilo99Signature, estilo99Defaults} from './Estilo99Signature';
import {Estilo13Punch, estilo13Defaults} from './Estilo13Punch';

const FPS = 24;
const s = (seg: number) => Math.round(seg * FPS); // segundos → frames

// Mapa componente-de-broll por nombre (para el mapa de montaje)
const BROLLS = {
  estilo13: Estilo13Punch,
  estilo11red: Estilo11Red,
  estilo11deriva: Estilo11Deriva,
  estilo11chart: BR3GanasOFacturas,
  estilo99: Estilo99Signature,
} as const;

// ─── Mapa de montaje del reel-003 "3 señales" ───────────────────────────────
// frames a 24fps. Clips = espina; overlays por encima con `from` absoluto.
export const MONTAJE = {
  // Espina de avatar (orden = timeline). frames = duración a mostrar del clip.
  clips: [
    {src: 'clips/c1.mp4', frames: s(6)}, // C1 HOOK
    {src: 'clips/c2.mp4', frames: s(8)}, // C2 SEÑAL 1
    {src: 'clips/c3.mp4', frames: s(8)}, // C3 SEÑAL 2
    {src: 'clips/c4.mp4', frames: s(8)}, // C4 SEÑAL 2b
    {src: 'clips/c5.mp4', frames: s(8)}, // C5 SEÑAL 3
    {src: 'clips/c6.mp4', frames: s(6)}, // C6 CIERRE
    {src: 'clips/c7.mp4', frames: s(4)}, // C7 CTA
  ],
  // B-rolls como cutaway (pantalla completa, mudos). from = frame absoluto.
  brolls: [
    {comp: 'estilo13', from: s(0), frames: s(3), props: {linea1: '3 SEÑALES', linea2: 'DE QUE TU NEGOCIO', keyword: 'NO ESTÁ ESTRUCTURADO'}},
    {comp: 'estilo11red', from: s(9.5), frames: s(4), props: estilo11RedDefaults},
    {comp: 'estilo11deriva', from: s(17.5), frames: s(4), props: estilo11DerivaDefaults},
    {comp: 'estilo11chart', from: s(33.5), frames: s(4), props: estilo11ChartDefaults},
    {comp: 'estilo99', from: s(40), frames: s(4), props: estilo99Defaults},
  ],
  // Textos lower-third (cuando el avatar está en pantalla, sin pisar b-rolls).
  textos: [
    {text: '1 · El conocimiento vive en las cabezas', from: s(6), frames: s(3.5)},
    {text: '2 · No se trabaja sobre objetivos', from: s(14), frames: s(3.5)},
    {text: '3 · ¿Ganás o solo facturás?', from: s(30), frames: s(3.5)},
  ],
  // Música opcional (Suno). null = sin música (la voz de los clips ya suena).
  musica: null as null | {src: string; volumen: number},
};

export type Montaje = typeof MONTAJE;

export const reelAssemblySchema = z.object({
  bg: z.string(),
});
export const reelAssemblyDefaults: z.infer<typeof reelAssemblySchema> = {
  bg: '#000000',
};

const totalFrames = (m: Montaje) => m.clips.reduce((a, c) => a + c.frames, 0);

// Duración dinámica: la compo dura lo que sumen los clips
export const calcReelMetadata = () => ({durationInFrames: totalFrames(MONTAJE)});

// ─── Lower-third de marca ────────────────────────────────────────────────────
const LowerThird: React.FC<{text: string}> = ({text}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({frame, fps, config: {damping: 200}, durationInFrames: 12});
  const y = interpolate(enter, [0, 1], [40, 0]);
  const op = interpolate(enter, [0, 1], [0, 1]);
  return (
    <AbsoluteFill style={{justifyContent: 'flex-end', alignItems: 'center', paddingBottom: 220}}>
      <div
        style={{
          transform: `translateY(${y}px)`,
          opacity: op,
          background: PALETA.ink,
          color: PALETA.blanco,
          fontFamily: FONT_MARCA,
          fontWeight: 800,
          fontSize: 46,
          lineHeight: 1.1,
          padding: '18px 30px',
          borderRadius: 14,
          maxWidth: 900,
          textAlign: 'center',
          boxShadow: '0 12px 40px rgba(0,0,0,0.35)',
        }}
      >
        {text}
      </div>
    </AbsoluteFill>
  );
};

export const ReelAssembly: React.FC<z.infer<typeof reelAssemblySchema>> = ({bg}) => {
  return (
    <AbsoluteFill style={{backgroundColor: bg}}>
      {/* Espina: clips de avatar back-to-back (su audio es la voz del reel) */}
      <Series>
        {MONTAJE.clips.map((c, i) => (
          <Series.Sequence key={i} durationInFrames={c.frames}>
            <OffthreadVideo src={staticFile(c.src)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
          </Series.Sequence>
        ))}
      </Series>

      {/* B-rolls como cutaway a pantalla completa (mudos, con su propio texto) */}
      {MONTAJE.brolls.map((b, i) => {
        const Comp = BROLLS[b.comp as keyof typeof BROLLS] as React.FC<any>;
        return (
          <Sequence key={`br${i}`} from={b.from} durationInFrames={b.frames} name={`broll:${b.comp}`}>
            <Comp {...b.props} />
          </Sequence>
        );
      })}

      {/* Textos lower-third */}
      {MONTAJE.textos.map((t, i) => (
        <Sequence key={`tx${i}`} from={t.from} durationInFrames={t.frames} name="texto">
          <LowerThird text={t.text} />
        </Sequence>
      ))}

      {/* Música opcional con ducking simple (si se define en el montaje) */}
      {MONTAJE.musica && (
        <Audio src={staticFile(MONTAJE.musica.src)} volume={MONTAJE.musica.volumen} />
      )}
    </AbsoluteFill>
  );
};
