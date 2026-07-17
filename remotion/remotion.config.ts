import {Config} from '@remotion/cli/config';

// Fuentes embebidas en el bundle como data-URI: la carga de fuentes no pasa por
// el dev-server del render, que se satura con la extracción de OffthreadVideo
// y colgaba los delayRender() de loadFont.
Config.overrideWebpackConfig((config) => ({
  ...config,
  module: {
    ...config.module,
    rules: [...(config.module?.rules ?? []), {test: /\.ttf$/, type: 'asset/inline'}],
  },
}));
