import React from 'react';
import {Composition} from 'remotion';
import {VideoEdit} from './VideoEdit';
import {FPS, WIDTH, HEIGHT, DURATION_IN_FRAMES} from './config';

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="VideoEdit"
      component={VideoEdit}
      durationInFrames={DURATION_IN_FRAMES}
      fps={FPS}
      width={WIDTH}
      height={HEIGHT}
      defaultProps={{
        music: true,
        musicVolume: 0.12,
      }}
    />
  );
};
