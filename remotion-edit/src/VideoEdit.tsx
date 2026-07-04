import React from 'react';
import {
  AbsoluteFill,
  OffthreadVideo,
  Audio,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  Easing,
} from 'remotion';
import {Captions} from './components/Captions';
import {Hook} from './components/Hook';
import {ProgressBar} from './components/ProgressBar';
import {VIDEO_SRC, MUSIC_SRC, BRAND_HANDLE} from './config';

export type EditProps = {
  music: boolean;
  musicVolume: number;
};

// Zoom sutil y lento sobre el vídeo para dar dinamismo (Ken Burns muy leve)
const useSubtleZoom = () => {
  const frame = useCurrentFrame();
  const {durationInFrames} = useVideoConfig();
  return interpolate(frame, [0, durationInFrames], [1.0, 1.06], {
    extrapolateRight: 'clamp',
    easing: Easing.linear,
  });
};

export const VideoEdit: React.FC<EditProps> = ({music, musicVolume}) => {
  const zoom = useSubtleZoom();

  return (
    <AbsoluteFill style={{backgroundColor: '#000'}}>
      {/* Vídeo base con zoom sutil */}
      <AbsoluteFill style={{transform: `scale(${zoom})`}}>
        <OffthreadVideo
          src={staticFile(VIDEO_SRC)}
          style={{width: '100%', height: '100%', objectFit: 'cover'}}
        />
      </AbsoluteFill>

      {/* Viñeta sutil para enfocar el centro y separar los subtítulos del fondo */}
      <AbsoluteFill
        style={{
          background:
            'radial-gradient(120% 80% at 50% 42%, rgba(0,0,0,0) 55%, rgba(0,0,0,0.38) 100%)',
          pointerEvents: 'none',
        }}
      />
      {/* Degradado inferior para legibilidad de subtítulos */}
      <AbsoluteFill
        style={{
          background:
            'linear-gradient(to top, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0) 34%)',
          pointerEvents: 'none',
        }}
      />

      {/* Música de fondo suave */}
      {music ? (
        <Audio src={staticFile(MUSIC_SRC)} volume={musicVolume} loop />
      ) : null}

      {/* Capas de edición */}
      <ProgressBar />
      <Hook />
      <Captions />

      {/* Handle de marca sutil */}
      <AbsoluteFill
        style={{justifyContent: 'flex-end', alignItems: 'center', paddingBottom: 60}}
      >
        <span
          style={{
            fontFamily: 'Inter, Arial, system-ui, sans-serif',
            fontWeight: 700,
            fontSize: 34,
            color: 'rgba(255,255,255,0.9)',
            letterSpacing: 1,
            textShadow: '0 2px 8px rgba(0,0,0,0.8)',
          }}
        >
          {BRAND_HANDLE}
        </span>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
