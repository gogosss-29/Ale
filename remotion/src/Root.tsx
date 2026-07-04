import React from 'react';
import {Composition} from 'remotion';
import {BR3GanasOFacturas, estilo11ChartSchema, estilo11ChartDefaults} from './BR3GanasOFacturas';
import {Estilo13Punch, estilo13Schema, estilo13Defaults} from './Estilo13Punch';
import {Estilo99Signature, estilo99Schema, estilo99Defaults} from './Estilo99Signature';
import {Estilo12TechReveal, estilo12Schema, estilo12Defaults} from './Estilo12TechReveal';
import {CaptionedClip, captionedClipSchema, captionedClipDefaults} from './CaptionedClip';
import {EditorialCaptions, editorialSchema, editorialDefaults} from './EditorialCaptions';

// Todos 9:16 · 24fps (firma de los estilos). Props parametrizables por reel.
export const Root: React.FC = () => {
  return (
    <>
      {/* Estilo #11 · Data Motion (chart barras vs línea plana) */}
      <Composition
        id="Estilo11-Chart"
        component={BR3GanasOFacturas}
        schema={estilo11ChartSchema}
        defaultProps={estilo11ChartDefaults}
        durationInFrames={96}
        fps={24}
        width={1080}
        height={1920}
      />
      {/* Alias histórico del piloto */}
      <Composition
        id="BR3-GanasOFacturas"
        component={BR3GanasOFacturas}
        schema={estilo11ChartSchema}
        defaultProps={estilo11ChartDefaults}
        durationInFrames={96}
        fps={24}
        width={1080}
        height={1920}
      />
      {/* Estilo #13 · Kinetic Typography Punch (3s) */}
      <Composition
        id="Estilo13-Punch"
        component={Estilo13Punch}
        schema={estilo13Schema}
        defaultProps={estilo13Defaults}
        durationInFrames={72}
        fps={24}
        width={1080}
        height={1920}
      />
      {/* Estilo #99 · Cerebro Signature (4s) */}
      <Composition
        id="Estilo99-Signature"
        component={Estilo99Signature}
        schema={estilo99Schema}
        defaultProps={estilo99Defaults}
        durationInFrames={96}
        fps={24}
        width={1080}
        height={1920}
      />
      {/* Estilo #12 · Dark Tech Reveal (4s) */}
      <Composition
        id="Estilo12-TechReveal"
        component={Estilo12TechReveal}
        schema={estilo12Schema}
        defaultProps={estilo12Defaults}
        durationInFrames={96}
        fps={24}
        width={1080}
        height={1920}
      />
      {/* Fase 2 · Captions del avatar (duración = la del clip, 30fps) */}
      <Composition
        id="CaptionedClip"
        component={CaptionedClip}
        schema={captionedClipSchema}
        defaultProps={captionedClipDefaults}
        durationInFrames={196}
        fps={30}
        width={1080}
        height={1920}
        calculateMetadata={({props}) => ({
          durationInFrames: Math.ceil((props.durationMs / 1000) * 30),
        })}
      />
      {/* Captions EDITORIALES (frases compuestas + texto detrás de la persona) */}
      <Composition
        id="EditorialCaptions"
        component={EditorialCaptions}
        schema={editorialSchema}
        defaultProps={editorialDefaults}
        durationInFrames={196}
        fps={30}
        width={1080}
        height={1920}
        calculateMetadata={({props}) => ({
          durationInFrames: Math.ceil((props.durationMs / 1000) * 30),
        })}
      />
    </>
  );
};
