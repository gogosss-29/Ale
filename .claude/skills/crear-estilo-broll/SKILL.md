---
name: crear-estilo-broll
description: >-
  Crea estilos nuevos de B-roll para Cerebro a partir de una referencia visual
  (link de Pinterest, TikTok/Reels, imagen o video). Analiza la estética y la
  traduce a una plantilla de estilo de 8 bloques EN LA DINÁMICA NUEVA (premium
  motion graphics, texto que aporta, ritmo punchy). Úsala cuando Ale pase una
  referencia y diga "creá un estilo nuevo", "agregá este estilo", "analizá esta
  referencia para un b-roll", o quiera sumar un universo visual a la biblioteca.
---

# 🎨 Crear Estilo de B-roll (analista visual + ingeniero de prompts)

> Adaptado del agente de Ale a nuestro sistema. Cada estilo nuevo nace ya en la
> **dinámica nueva**: nivel premium + **texto/dato que aporta** + **ritmo punchy**
> (no "inserts serenos lentos", esa filosofía vieja queda descartada).

## Workflow (cada vez que llega una referencia)

### 1. Ingesta (tooling nuestro · CERO suposiciones)
NO inventar el estilo por el título de la URL. Descargar y VER primero.
- **Pinterest:** `curl -sL -A "<UA>"` al pin → buscar la URL real:
  - video → `v1.pinimg.com/videos/.../_720w.mp4` o `mc/720p/...mp4`.
  - imagen → og:image / `i.pinimg.com/originals/...`.
- **Frames:** `imageio-ffmpeg` (`-ss N -frames:v 1`) repartidos por la duración → **Read** los frames (visión).
- (yt-dlp sirve si está instalado; si no, este método funciona.)

### 2. Análisis visual (documentar)
- **Fondo:** claro/oscuro, papel, grid, sólido, sombras gobo.
- **Elementos:** glass UI, 3D, recortes B&N, esculturas, objetos reales, charts.
- **Iluminación/efectos:** glow, sombras duras, parallax, profundidad.
- **Tipografía/texto:** cómo se integra (sans bold, marcador, recorte). **Qué dato comunica.**
- **Paleta:** códigos HEX principales + acento.
- **Animación/ritmo:** cámara (move/estática), multi-etapa, velocidad.

### 3. Mapeo a la plantilla de 8 bloques — EN LA DINÁMICA NUEVA
Bloques: `[STYLE] [BACKGROUND] [MAIN ELEMENT] [ANIMATION] [TEXT ON SCREEN] [COLOR PALETTE] [MOOD] [AUDIO] [NEGATIVE]`. Siempre:
- **[STYLE]:** nivel premium — `premium After Effects mixed-media motion graphics, broadcast quality, camera movement, parallax, shallow depth of field, subtle film grain`.
- **[ANIMATION]:** **punchy y front-loaded** — visual clave + texto en los primeros ~1,5-2s, cámara con movimiento, motion blur, **cut-ready** (se recorta/acelera al ritmo de la locución). Nunca build lento ni estático.
- **[TEXT ON SCREEN]:** **SÍ, integrado al mundo del estilo y que APORTA** (dato/keyword). Palabras exactas y cortas, en español. NO meter códigos hex en el texto (Veo los "imprime"); el color va solo en `[COLOR PALETTE]`.
- **[AUDIO]:** sin voz/narración; sound design del estilo (synth/UI o analógico según el universo).
- **[NEGATIVE]:** lo que rompe el estilo + `distorted misspelled text, static single-pose animation, slow boring motion, low-res, voiceover, narration, human speech`.

### 4. Entregables (2 archivos, rutas nuestras)
1. **Archivo del estilo:** `.claude/skills/cerebro-guiones/references/estilo-NN-nombre.md`
   con: descripción, cuándo usarlo (psicología del estilo), diferencias, firma fija,
   paleta hex, **master template** (8 bloques) y **1 prompt de ejemplo validado**.
2. **Registrar** la fila `#NN` en `references/brolls-biblioteca.md` (tabla).
3. (Opcional) crear sub-página en la **Biblioteca de Estilos** de Notion.
- El **ejemplo** se aplica a un concepto real de Cerebro (ej. "costo de adquisición",
  "caos operacional", "enfoque vs multitasking") para validar.

### 5. Numeración
Asignar el **siguiente ID disponible** (hoy: **#12**; #11 = Data Motion). No reasignar IDs viejos (#03/#04 descartados se respetan).

## Reglas críticas
1. **Cero suposiciones:** ver la referencia antes de definir nada.
2. **Texto integrado + que aporta:** el texto vive dentro del estilo y comunica un dato; nunca flota porque sí, nunca es solo decorativo.
3. **Ritmo punchy / front-loaded / cut-ready** (NO inserts serenos lentos).
4. **Nivel premium broadcast** en todos los estilos.
5. **Duración:** por defecto 4s (punchy); ver buckets en `director-avatar-omni.md`.
6. Consistencia de numeración y rutas.
7. Si la referencia tiene un look que choca con la marca (ej. neón puro), proponer
   la **adaptación a la paleta de Cerebro** y avisar (como con el cyan del plan viejo).
