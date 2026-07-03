# 🗺️ Roadmap Remotion — decisiones tras la investigación (2026-06)

> Veredicto de la investigación de Ale sobre el ecosistema Remotion, cruzada con
> nuestro sistema (proyecto `remotion/` ya renderizando en el entorno remoto,
> estilos #11/#12/#13/#99 portados). Regla: adoptar lo que sirve al pipeline
> real, descartar el ruido.

## ✅ Licencia (resuelto)
Ale = individuo → **Free License**: uso comercial, renders ilimitados, $0.
Revisar solo si el equipo (sumando partes que USEN el código) llega a 4+ personas.
Enviar el MP4 terminado al cliente NO cuenta.

## Fase 1 — Quick wins (parametrización + marca)
- [ ] **Props con `@remotion/zod-types`**: schema por estilo (textos, datos, colores,
      duración) → un b-roll nuevo = props nuevas, no código nuevo. + `calculateMetadata`
      para duración dinámica.
- [ ] **Tipografía de marca con `@remotion/google-fonts`** (reemplazar Arial del sistema).
- [ ] **Comando batch**: "render de todos los b-rolls del reel X" (un script, N mp4
      con naming `reelNNN-brK.mp4`).
- [ ] `@remotion/transitions` + `@remotion/motion-blur` en los estilos.
- [ ] Sound design programado (`<Audio>` con ticks/whooshes/bass en la compo).

## Fase 2 — Captions del avatar (el hallazgo grande)
Patrón del `template-tiktok` oficial:
- [ ] Transcribir el clip del avatar (whisper local — ya disponible en el entorno)
      con timestamps por palabra (modelo multilingüe para español).
- [ ] `@remotion/captions` + `createTikTokStyleCaptions()` → subtítulos animados
      palabra-por-palabra con la tipografía/paleta de marca.
- [ ] Composición `CaptionsOverlay`: Ale sube el clip de Omni → se devuelve el clip
      con captions quemados (o overlay transparente para CapCut).
- [ ] Piloto con un clip real del reel-003.

## Fase 3 — Ensamblado del reel en Remotion
- [ ] Composición `ReelAssembly`: clips de avatar (subidos por Ale) + b-rolls
      renderizados + textos en pantalla + música con **ducking programado**
      (`@remotion/media-utils`) → reel casi final; CapCut queda para retoque.
- [ ] Nuestros clips son de 4-10s → esquivamos los issues de `<OffthreadVideo>`
      con fuentes largas (#3070/#3088). Usar `<Video>` de `@remotion/media`.

## Fase 4 — Cuando Ale monte el motor local (Claude Code en su máquina)
- [ ] Evaluar plugin **`DojoCodingLabs/remotion-superpowers`** (slash commands
      /create-short, /add-captions…) — acá no hace falta, allá sí puede sumar.
- [ ] **Guía de performance para su i7-7700HQ/GTX1050/Windows**: render por Docker/WSL2,
      `CONCURRENCY=2-4` (benchmark con `npx remotion benchmark`), `--x264-preset faster`,
      `VIDEO_CACHE_SIZE_IN_BYTES=~2GB` si hay OOM, evitar box-shadow/blur pesados.
      HW-encode (NVENC) NO disponible en Windows (solo macOS/VideoToolbox); la GPU
      solo acelera whisper.
- [ ] MCP de docs oficial de Remotion / `@remotion/skills` para el agente local.

## Cantera (copiar piezas sueltas, NO depender)
- `reactvideoeditor/remotion-templates` (81 componentes MIT) y `av/remotion-bits`:
  fuente de charts/transiciones/reveals para acelerar estilos nuevos. Poco
  mantenidos → copiar y adaptar el código, no instalarlos como dependencia.
- 17 estilos de captions de `ahgsql/remotion-subtitles` como galería de referencia.

## ❌ Descartado (para nuestro caso)
- **ShortGPT / AI-Youtube-Shorts-Generator**: no usan Remotion; para cortar YouTube
  ya está el **Personal Clipper de Higgsfield**.
- **short-video-maker**: pipeline faceless con TTS en inglés — nosotros tenemos
  avatar con la voz real de Ale (Omni). Solo referencia de flags de memoria.
- **react-video-editor**: starter de SaaS con timeline; sobredimensionado.
- **remotion-media-mcp**: exige API paga de KIE; la generativa ya la cubre
  Higgsfield/Flow.
- **Lambda/CloudRun**: innecesario al volumen actual (render local/remoto gratis);
  reconsiderar solo si el volumen escala a cientos/mes.
