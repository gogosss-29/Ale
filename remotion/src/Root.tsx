import React from 'react';
import {Composition} from 'remotion';
import {BR3GanasOFacturas} from './BR3GanasOFacturas';
import {Estilo13Punch} from './Estilo13Punch';
import {Estilo99Signature} from './Estilo99Signature';
import {Estilo12TechReveal} from './Estilo12TechReveal';

// Todos 9:16 · 24fps (firma de los estilos)
export const Root: React.FC = () => {
  return (
    <>
      {/* Estilo #11 · Data Motion */}
      <Composition
        id="BR3-GanasOFacturas"
        component={BR3GanasOFacturas}
        durationInFrames={96}
        fps={24}
        width={1080}
        height={1920}
      />
      {/* Estilo #13 · Kinetic Typography Punch (3s) */}
      <Composition
        id="Estilo13-FacturarNoEsGanar"
        component={Estilo13Punch}
        durationInFrames={72}
        fps={24}
        width={1080}
        height={1920}
      />
      {/* Estilo #99 · Cerebro Signature (4s) */}
      <Composition
        id="Estilo99-DelCaosAlOrden"
        component={Estilo99Signature}
        durationInFrames={96}
        fps={24}
        width={1080}
        height={1920}
      />
      {/* Estilo #12 · Dark Tech Reveal (4s) */}
      <Composition
        id="Estilo12-FuenteDeVerdad"
        component={Estilo12TechReveal}
        durationInFrames={96}
        fps={24}
        width={1080}
        height={1920}
      />
    </>
  );
};
