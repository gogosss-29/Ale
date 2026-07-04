import React from 'react';
import {AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate} from 'remotion';

// Barra de progreso fina en la parte superior
export const ProgressBar: React.FC = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  const progress = interpolate(frame, [0, durationInFrames - 1], [0, 1], {
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill style={{justifyContent: 'flex-start'}}>
      <div
        style={{
          position: 'absolute',
          top: 26,
          left: 32,
          right: 32,
          height: 8,
          borderRadius: 8,
          background: 'rgba(255,255,255,0.22)',
          overflow: 'hidden',
        }}
      >
        <div
          style={{
            width: `${progress * 100}%`,
            height: '100%',
            borderRadius: 8,
            background:
              'linear-gradient(90deg, #7CF86B 0%, #b6ff8f 100%)',
            boxShadow: '0 0 12px rgba(124,248,107,0.7)',
          }}
        />
      </div>
    </AbsoluteFill>
  );
};
