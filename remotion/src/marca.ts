// ─── Marca Cerebro: tipografía y tokens compartidos ─────────────────────────
import {loadFont} from '@remotion/fonts';
import archivoTtf from '../public/fonts/Archivo-Variable.ttf';

// Archivo (variable, OFL) embebida en el bundle como data-URI (ver
// remotion.config.ts) — grotesca moderna con pesos fuertes, la voz
// tipográfica de los b-rolls. Sin dependencia de red ni del dev-server.
loadFont({
  family: 'Archivo',
  url: archivoTtf,
  format: 'truetype',
  weight: '100 900',
}).catch(() => undefined); // si falla, cae al stack del sistema

export const FONT_MARCA = "'Archivo', Arial, 'Liberation Sans', sans-serif";

// Paletas (fuente de verdad: references de la skill)
export const PALETA = {
  // #11 Data Motion
  grid: '#EDEDED',
  ink: '#111111',
  rojo: '#E2352B',
  verde: '#1FB85B',
  blanco: '#FFFFFF',
  // #99 Cerebro Signature
  grafito: '#14161A',
  hueso: '#F2EEE6',
  oro: '#E8B04B',
  // #12 Dark Tech
  voidNavy: '#0B1A2C',
  cian: '#2FD3E3',
  // #13 Kinetic
  negro: '#000000',
  crema: '#F5F1E6',
};
