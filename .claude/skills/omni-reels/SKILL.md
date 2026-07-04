---
name: omni-reels
description: >-
  Editar reels/videos de avatar con Google Omni (Gemini Omni) haciendo compositing
  de motion graphics SOBRE un video real, sin que Omni cambie la voz ni el personaje.
  Cubre el flujo completo: cortar el video en secuencias de ≤10s en silencios (con la
  herramienta reel_cutter), pensar el video como una pieza única, y escribir los prompts
  de Omni clavados a la locución. Usar SIEMPRE que se quiera: editar un reel con Omni,
  "armar los prompts de Omni", cortar un video en clips de 10 segundos para Omni,
  animar/agregar títulos y gráficos sobre un talking-head, o cuando Omni "me cambió la voz".
---

# Editar reels de avatar con Google Omni (compositing sobre footage real)

Google Omni (Gemini Omni) genera clips de máx. **10 s, 1080p, con audio**. No edita un video largo de una: se **trocea en secuencias ≤10 s** y a cada una se le pasa un prompt de motion graphics. El riesgo es que, al ser generativo, **regenere la voz o el personaje**. Esta skill evita eso.

## Flujo de trabajo (en orden, no saltear)

1. **Insumos:** el video crudo (talking-head) + el guion/subtítulos.
2. **Cortar con `scripts/reel_cutter.py`** → clips ≤10 s cortados en silencios (nunca a mitad de palabra) + `mapeo_clips.md` (texto exacto por clip) + `segments.json` (timestamp de cada palabra, relativo al inicio del clip). Ver `scripts/README.md`.
3. **Pensar el video COMPLETO primero:** plan maestro con un sistema visual único y un mapa de beats donde **cada clip tiene UN solo foco** (si se piensa clip por clip, se sobrecarga).
4. **Escribir un prompt por clip**, clavado a la locución usando los tiempos de `segments.json`.
5. **Generar en Omni**, verificar voz (paso de verificación abajo), reconcatenar en el orden, **upscalar** (Omni saca 720p/24fps) y recién ahí sumar la música.

## Regla de oro: que Omni NO toque la voz ni el personaje

Es lo más importante y lo más frágil. Dos cosas, juntas:

1. **Preámbulo benigno** (encabeza cada prompt). Decir que es tu propio video y que solo agregue overlays. **NO** usar lenguaje forense ("clone", "dub", "lip-sync", "bit-for-bit", "do not re-render the human", "deepfake") → **dispara el filtro de políticas** y no deja generar.
   > *"This is my own video of myself that I want to enhance with motion-graphic overlays. Keep my original footage and its audio exactly as they are — do not modify the video of me, the background or the lighting, and do not change the sound of my voice or my speech in any way. Only add new graphics, titles and sound effects composited on top, like overlay layers in a video editor. Keep me visible the whole time."*
2. **Disparar TODO por tiempo, nunca "when I say [palabra]".** Los cues de habla hacen que Omni "escuche" y regenere la voz. Usar los segundos de `segments.json`: *"At ~4.3s slide in…"*. Cero "when I say".

## Estructura del prompt (5 bloques)

1. **Preámbulo de voz** (el de arriba).
2. **Goal** — qué es el clip, formato 9:16 1080p, idioma, "do not add subtitles" (si los subtítulos los pone el usuario).
3. **Style & timing** — cada elemento con su segundo exacto y su animación.
4. **Sound effects** — "added softly as separate quiet layers under my original voice, no music, without changing my voice". (Si el usuario pone la música, decir **no music**.)
5. **Constraints** — repetir 9:16/1080p, voz y personaje intactos, y una **lista blanca** de qué texto puede aparecer en pantalla.

## Sistema visual (cohesión entre clips)

- **Composición fija:** gráficos arriba-izquierda; el sujeto abajo-derecha, despejado; nada sobre la cara.
- **Roles de color por nombre** (ver anti-glitch): p. ej. amarillo = títulos/pills de sección, verde = plata/mecánica, gris = lo que NO conviene.
- **Física de animación** consistente: entradas *ease-out-back* (overshoot), salidas *ease-in*, motion blur, glow suave, glassmorphism leve.
- **Tokens recurrentes:** una pill de sección, UN título por clip, un tag de marca que reaparece chico, bug de marca desde el primer beat de identidad.
- **Safe zones:** nada importante en el 10% superior ni el 15% inferior.

## Anti-glitches de Omni (aprendidos a los golpes)

- **NUNCA códigos hex en el prompt** → Omni los escribe en pantalla (p. ej. apareció "#F4C430"). Usar **nombres de color** ("gold", "bright green", "vivid yellow").
- **Bloquear números no dichos:** *"do not add any numbers other than X"* → evita contadores/porcentajes alucinados (p. ej. "1986%"). Solo permitir los números que la persona realmente dice.
- **Salida de Omni:** 720p / 24fps / 10s máx → **upscalar** al final (a 1080p/4K con otra herramienta) y reconcatenar.
- Si un gráfico cae 0.3–0.5s corrido, ajustar el segundo (los tiempos vienen de `segments.json`).

## Verificación de voz (recomendado)

Tras generar, confirmar que la locución no cambió: extraer el audio del resultado y del original, filtrar a banda de voz (300–3400 Hz) y correlacionar. Correlación alta (~0.8+) = misma grabación con SFX encima (OK). Baja = Omni regeneró la voz → reintentar el prompt (revisar que sea time-based y benigno).

## Notas de negocio / ejemplo

Ejemplo real: marca *Invertí sin vueltas* (finanzas, español argentino, formato 9:16). Estilo que funcionó: íconos de línea limpios arriba-izquierda, títulos condensados en amarillo, verde para la plata, diagramas que se dibujan solos. Ver `reference/ejemplo_prompt.md` para un prompt modelo completo.
