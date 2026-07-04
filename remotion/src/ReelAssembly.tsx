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

type TextoItem = {text: string; from: number; frames: number; hook?: boolean};
export type Montaje = {
  clips: {src: string; frames: number}[];
  brolls: {comp: string; from: number; frames: number; props: Record<string, unknown>}[];
  textos: TextoItem[];
  musica: null | {src: string; volumen: number};
};

// ─── Variante V2: te ves desde el segundo 0; el hook entra como TEXTO ─────────
// (sin el b-roll #13 tapando la cara). Mismos clips, b-rolls de datos y timings.
const MONTAJE_V2: Montaje = {
  clips: MONTAJE.clips,
  brolls: MONTAJE.brolls.filter((b) => b.comp !== 'estilo13'),
  textos: [
    {text: '3 señales de que tu negocio NO está estructurado', from: s(0.6), frames: s(4.6), hook: true},
    ...MONTAJE.textos,
  ],
  musica: MONTAJE.musica,
};

const MONTAJES: Record<string, Montaje> = {v1: MONTAJE, v2: MONTAJE_V2};

export const reelAssemblySchema = z.object({
  bg: z.string(),
  variant: z.enum(['v1', 'v2']),
});
export const reelAssemblyDefaults: z.infer<typeof reelAssemblySchema> = {
  bg: '#000000',
  variant: 'v1',
};

const totalFrames = (m: Montaje) => m.clips.reduce((a, c) => a + c.frames, 0);

// Duración dinámica: la compo dura lo que sumen los clips (igual en v1/v2)
export const calcReelMetadata = () => ({durationInFrames: totalFrames(MONTAJE)});

// ─── Texto de marca: lower-third (default) o hook (grande, arriba) ───────────
const TextoMarca: React.FC<{text: string; hook?: boolean}> = ({text, hook}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const enter = spring({frame, fps, config: {damping: 200}, durationInFrames: 12});
  const y = interpolate(enter, [0, 1], [hook ? 24 : 40, 0]);
  const op = interpolate(enter, [0, 1], [0, 1]);
  return (
    <AbsoluteFill
      style={{
        justifyContent: hook ? 'flex-start' : 'flex-end',
        alignItems: 'center',
        paddingTop: hook ? 180 : 0,
        paddingBottom: hook ? 0 : 220,
        paddingLeft: 40,
        paddingRight: 40,
      }}
    >
      <div
        style={{
          transform: `translateY(${y}px)`,
          opacity: op,
          background: hook ? PALETA.rojo : PALETA.ink,
          color: PALETA.blanco,
          fontFamily: FONT_MARCA,
          fontWeight: hook ? 900 : 800,
          fontSize: hook ? 62 : 46,
          lineHeight: 1.05,
          padding: hook ? '22px 34px' : '18px 30px',
          borderRadius: 16,
          maxWidth: hook ? 940 : 900,
          textAlign: 'center',
          textTransform: hook ? 'uppercase' : 'none',
          letterSpacing: hook ? '-0.01em' : 0,
          boxShadow: '0 12px 40px rgba(0,0,0,0.35)',
        }}
      >
        {text}
      </div>
    </AbsoluteFill>
  );
};

export const ReelAssembly: React.FC<z.infer<typeof reelAssemblySchema>> = ({bg, variant}) => {
  const M = MONTAJES[variant] ?? MONTAJE;
  return (
    <AbsoluteFill style={{backgroundColor: bg}}>
      {/* Espina: clips de avatar back-to-back (su audio es la voz del reel) */}
      <Series>
        {M.clips.map((c, i) => (
          <Series.Sequence key={i} durationInFrames={c.frames}>
            <OffthreadVideo src={staticFile(c.src)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
          </Series.Sequence>
        ))}
      </Series>

      {/* B-rolls como cutaway a pantalla completa (mudos, con su propio texto) */}
      {M.brolls.map((b, i) => {
        const Comp = BROLLS[b.comp as keyof typeof BROLLS] as React.FC<any>;
        return (
          <Sequence key={`br${i}`} from={b.from} durationInFrames={b.frames} name={`broll:${b.comp}`}>
            <Comp {...b.props} />
          </Sequence>
        );
      })}

      {/* Textos: lower-third (señales) o hook grande arriba (v2) */}
      {M.textos.map((t, i) => (
        <Sequence key={`tx${i}`} from={t.from} durationInFrames={t.frames} name={t.hook ? 'hook' : 'texto'}>
          <TextoMarca text={t.text} hook={t.hook} />
        </Sequence>
      ))}

      {/* Música opcional con ducking simple (si se define en el montaje) */}
      {M.musica && <Audio src={staticFile(M.musica.src)} volume={M.musica.volumen} />}
    </AbsoluteFill>
  );
};
