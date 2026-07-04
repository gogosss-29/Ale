import React from 'react';
import {
  AbsoluteFill,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
  Easing,
} from 'remotion';
import {HOOK_TEXT, HOOK_DURATION_S} from '../config';

// Gancho animado en los primeros segundos para retener al espectador
export const Hook: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const totalFrames = HOOK_DURATION_S * fps;

  if (frame > totalFrames) {
    return null;
  }

  const entrada = spring({
    frame,
    fps,
    config: {damping: 14, mass: 0.7, stiffness: 120},
    durationInFrames: 18,
  });

  const salida = interpolate(
    frame,
    [totalFrames - 12, totalFrames],
    [1, 0],
    {extrapolateLeft: 'clamp', extrapolateRight: 'clamp', easing: Easing.in(Easing.ease)},
  );

  const y = interpolate(entrada, [0, 1], [70, 0]);
  const scale = interpolate(entrada, [0, 1], [0.7, 1]);

  const words = HOOK_TEXT.split(' ');

  return (
    <AbsoluteFill
      style={{
        justifyContent: 'flex-start',
        alignItems: 'center',
        paddingTop: 220,
        opacity: salida,
      }}
    >
      <div
        style={{
          transform: `translateY(${y}px) scale(${scale})`,
          display: 'flex',
          flexWrap: 'wrap',
          justifyContent: 'center',
          gap: '10px 16px',
          maxWidth: 900,
          padding: '0 60px',
        }}
      >
        {words.map((w, i) => {
          const wSpring = spring({
            frame: frame - i * 3,
            fps,
            config: {damping: 12, stiffness: 140},
            durationInFrames: 16,
          });
          return (
            <span
              key={i}
              style={{
                display: 'inline-block',
                transform: `translateY(${interpolate(wSpring, [0, 1], [30, 0])}px)`,
                opacity: wSpring,
                fontFamily: 'Inter, Arial, system-ui, sans-serif',
                fontWeight: 900,
                fontSize: 96,
                lineHeight: 1,
                letterSpacing: -2,
                textTransform: 'uppercase',
                color: '#ffffff',
                textShadow:
                  '0 6px 26px rgba(0,0,0,0.75), 0 2px 6px rgba(0,0,0,0.95)',
                WebkitTextStroke: '3px rgba(0,0,0,0.35)',
              }}
            >
              {w}
            </span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
