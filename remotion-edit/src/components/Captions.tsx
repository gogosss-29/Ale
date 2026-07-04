import React, {useMemo} from 'react';
import {
  AbsoluteFill,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
} from 'remotion';
import {
  createTikTokStyleCaptions,
  type Caption,
} from '@remotion/captions';
import captionsData from '../data/words.json';

// Agrupa palabras en "páginas" de subtítulo estilo TikTok/Reels
// (~1.1 s por página => frases cortas, muy legibles en vertical)
const COMBINE_MS = 1100;

export const Captions: React.FC = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const nowMs = (frame / fps) * 1000;

  const {pages} = useMemo(() => {
    const captions = captionsData as Caption[];
    return createTikTokStyleCaptions({
      captions,
      combineTokensWithinMilliseconds: COMBINE_MS,
    });
  }, []);

  const page = useMemo(() => {
    return pages.find((p) => {
      const end = p.startMs + Math.max(...p.tokens.map((t) => t.toMs - p.startMs));
      return nowMs >= p.startMs && nowMs <= end + 150;
    });
  }, [pages, nowMs]);

  if (!page) {
    return null;
  }

  const enterFrame = (page.startMs / 1000) * fps;
  const enter = spring({
    frame: frame - enterFrame,
    fps,
    config: {damping: 200, stiffness: 120},
    durationInFrames: 8,
  });
  const scale = interpolate(enter, [0, 1], [0.86, 1]);
  const opacity = interpolate(enter, [0, 1], [0, 1]);

  return (
    <AbsoluteFill
      style={{
        justifyContent: 'flex-end',
        alignItems: 'center',
        paddingBottom: 430,
        paddingLeft: 70,
        paddingRight: 70,
      }}
    >
      <div
        style={{
          transform: `scale(${scale})`,
          opacity,
          textAlign: 'center',
          display: 'flex',
          flexWrap: 'wrap',
          justifyContent: 'center',
          gap: '10px 16px',
          maxWidth: 940,
        }}
      >
        {page.tokens.map((token, i) => {
          const active = nowMs >= token.fromMs && nowMs <= token.toMs;
          const spoken = nowMs > token.toMs;
          return (
            <span
              key={i}
              style={{
                fontFamily:
                  'Inter, "Helvetica Neue", Arial, system-ui, sans-serif',
                fontWeight: 800,
                fontSize: 74,
                lineHeight: 1.05,
                letterSpacing: -1,
                textTransform: 'uppercase',
                color: active ? '#0a0a0a' : '#ffffff',
                backgroundColor: active ? '#7CF86B' : 'transparent',
                padding: active ? '2px 14px' : '2px 0',
                borderRadius: 14,
                WebkitTextStroke: active ? '0px' : '2px rgba(0,0,0,0.55)',
                textShadow: active
                  ? 'none'
                  : '0 4px 18px rgba(0,0,0,0.65), 0 2px 4px rgba(0,0,0,0.9)',
                opacity: spoken ? 0.92 : 1,
                transition: 'none',
              }}
            >
              {token.text.trim()}
            </span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
