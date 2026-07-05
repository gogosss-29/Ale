// ─── EditedVideo · el motor del sistema de edición ──────────────────────────
// Composición GENÉRICA data-driven: recibe un EditMap (JSON) y monta el video
// editado: base + captions + overlays + capas "detrás" (con recorte de persona).
// No hay nada casado a un video puntual — todo viene del editmap.
// Uso: registrada en Root; se rinde con --props=<editmap.json>.
import React from 'react';
import {
  AbsoluteFill,
  Img,
  OffthreadVideo,
  Sequence,
  staticFile,
  useCurrentFrame,
} from 'remotion';
import {z} from 'zod';
import {CaptionsLayer} from './CaptionedClip';
import {
  BrandBug,
  TopLabel,
  NumberCallout,
  Chip,
  BarsLabel,
  ArrowChips,
  BigBadge,
  RisingLine,
} from './overlays';

// ── Schema del EditMap ───────────────────────────────────────────────────────
const captionPageSchema = z.object({
  startMs: z.number(),
  endMs: z.number(),
  tokens: z.array(z.object({text: z.string(), fromMs: z.number(), toMs: z.number()})),
});

// Un overlay al FRENTE, ubicado por segundos. `type` elige el componente y
// `props` son sus parámetros (validados laxo: cada overlay valida lo suyo).
const overlaySchema = z.object({
  type: z.enum(['topLabel', 'numberCallout', 'chip', 'barsLabel', 'arrowChips', 'bigBadge']),
  fromSec: z.number(),
  durSec: z.number(),
  props: z.record(z.string(), z.any()).default({}),
});

// Una capa "detrás" de la persona: gráfico + recorte segmentado de esa ventana.
const behindSchema = z.object({
  graphic: z.enum(['risingLine']).default('risingLine'),
  fromFrame: z.number(), // frame absoluto de inicio (coincide con los recortes)
  frames: z.number(),
  personDir: z.string(), // carpeta en public/ con f-<abs>.png
  props: z.record(z.string(), z.any()).default({}),
});

export const editedVideoSchema = z.object({
  videoSrc: z.string(),
  durationMs: z.number(),
  fps: z.number().default(30),
  brand: z.string().default('CEREBRO'),
  showBrandBug: z.boolean().default(true),
  captionPreset: z.enum(['marca', 'minimal-top']).default('marca'),
  pages: z.array(captionPageSchema).default([]),
  overlays: z.array(overlaySchema).default([]),
  behind: z.array(behindSchema).default([]),
});
export type EditMap = z.infer<typeof editedVideoSchema>;

export const editedVideoDefaults: EditMap = {
  videoSrc: 'clips/crudos.mp4',
  durationMs: 63716,
  fps: 30,
  brand: 'CEREBRO',
  showBrandBug: true,
  captionPreset: 'marca',
  pages: [],
  overlays: [],
  behind: [],
};

// mapea type -> componente de overlay
const OVERLAYS: Record<string, React.FC<any>> = {
  topLabel: TopLabel,
  numberCallout: NumberCallout,
  chip: Chip,
  barsLabel: BarsLabel,
  arrowChips: ArrowChips,
  bigBadge: BigBadge,
};

// recorte de persona para una ventana "detrás"
const PersonCutout: React.FC<{dir: string; startFrame: number; count: number}> = ({dir, startFrame, count}) => {
  const frame = useCurrentFrame();
  const idx = Math.min(count - 1, Math.max(0, frame));
  const name = `${dir}/f-${String(startFrame + idx).padStart(4, '0')}.png`;
  return <Img src={staticFile(name)} style={{position: 'absolute', inset: 0, width: '100%', height: '100%', objectFit: 'cover'}} />;
};

export const EditedVideo: React.FC<EditMap> = (map) => {
  const sec = (n: number) => Math.round(n * map.fps);
  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      {/* 1 · video de base */}
      <OffthreadVideo src={staticFile(map.videoSrc)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />

      {/* 2 · capas DETRÁS: gráfico + recorte de persona encima */}
      {map.behind.map((b, i) => (
        <Sequence key={`bh${i}`} from={b.fromFrame} durationInFrames={b.frames} name={`detras:${i}`}>
          <RisingLine durationInFrames={b.frames} id={`b${i}`} {...b.props} />
          <PersonCutout dir={b.personDir} startFrame={b.fromFrame} count={b.frames} />
        </Sequence>
      ))}

      {/* 3 · overlays al FRENTE */}
      {map.showBrandBug ? <BrandBug text={map.brand} /> : null}
      {map.overlays.map((o, i) => {
        const Comp = OVERLAYS[o.type];
        if (!Comp) return null;
        return (
          <Sequence key={`ov${i}`} from={sec(o.fromSec)} durationInFrames={sec(o.durSec)} name={`ov:${o.type}`}>
            <Comp {...o.props} />
          </Sequence>
        );
      })}

      {/* 4 · captions arriba de todo */}
      <CaptionsLayer pages={map.pages} preset={map.captionPreset} />
    </AbsoluteFill>
  );
};
