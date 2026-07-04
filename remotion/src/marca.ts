// ─── Marca Cerebro: tipografía y tokens compartidos ─────────────────────────
import {continueRender, delayRender, staticFile} from 'remotion';

// Archivo (variable, OFL) self-hosteada en public/fonts — grotesca moderna con
// pesos fuertes, la voz tipográfica de los b-rolls. Sin dependencia de red.
// Carga NO bloqueante: inyectamos @font-face y NO usamos delayRender (Remotion
// controla el reloj en el render, así que un timer de seguridad no dispararía y
// un fallo/lentitud de la fuente colgaría el render). El navegador precarga la
// fuente al montar la página; si no llega a tiempo cae al stack del sistema.
export const injectFont = (
  family: string,
  file: string,
  weight = '100 900',
  style: 'normal' | 'italic' = 'normal',
) => {
  if (typeof document === 'undefined') return;
  const id = `font-${family}`;
  if (document.getElementById(id)) return;
  const el = document.createElement('style');
  el.id = id;
  el.textContent = `@font-face{font-family:'${family}';src:url('${staticFile(
    file,
  )}') format('truetype');font-weight:${weight};font-style:${style};font-display:swap;}`;
  document.head.appendChild(el);
};

injectFont('Archivo', 'fonts/Archivo-Variable.ttf', '100 900');

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
