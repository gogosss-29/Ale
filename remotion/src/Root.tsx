import React from 'react';
import {Composition} from 'remotion';
import {BR3GanasOFacturas} from './BR3GanasOFacturas';

// Estilo #11 · Data Motion — 9:16, 24fps (firma del estilo), 4s = 96 frames
export const Root: React.FC = () => {
  return (
    <>
      <Composition
        id="BR3-GanasOFacturas"
        component={BR3GanasOFacturas}
        durationInFrames={96}
        fps={24}
        width={1080}
        height={1920}
      />
    </>
  );
};
