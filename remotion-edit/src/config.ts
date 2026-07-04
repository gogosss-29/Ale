// Parámetros del vídeo fuente (probados con ffprobe)
export const FPS = 30;
export const WIDTH = 1080;
export const HEIGHT = 1920;

// Duración real del clip: 63.715 s -> ceil para no cortar audio
export const SOURCE_DURATION_S = 63.715;
export const DURATION_IN_FRAMES = Math.ceil(SOURCE_DURATION_S * FPS); // 1912

export const VIDEO_SRC = 'source.mp4';
export const MUSIC_SRC = 'music.mp3';

// Texto del hook / título inicial (ajustado a la apertura real del vídeo)
export const HOOK_TEXT = 'JUNTÓ 45 MILLONES';
export const HOOK_DURATION_S = 3.0;

// Marca / handle mostrado sutilmente
export const BRAND_HANDLE = '@alexander';
