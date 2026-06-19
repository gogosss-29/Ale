# 🎬 Runbook de producción — reel-002 (Ruta A: Flow / Veo 3.1)

> Guía paso a paso para producir el reel-002 a mano en Flow + CapCut.
> Los **prompts verbatim** están en `reel-002-dependencia-persona.md` (secciones 3 y 4).
> Modelo: **Veo 3.1** (o Omni Flash si está disponible). Formato 9:16.

## Paso 0 — Prerrequisito: imagen de referencia del avatar
Necesitás **una imagen tuya (avatar) sentado en el escenario** (la del sillón que venís usando).
- Si ya la tenés → usala como *start image*.
- Si no → generala antes con GPT Image 2 / Nano Banana (avatar + escenario), o avisame y la armamos.

## Paso 1 — AVATAR · Secuencia 1 (hook)
1. En Flow: modo **Ingredients-to-Video**, cargá la **imagen de referencia** (escenario).
2. Pegá el **prompt SECUENCIA 1** (archivo reel-002, sección 3).
3. **Audio ON** (Veo genera la voz del avatar con la locución).
4. Generá. Elegí la mejor toma.
5. **Exportá un frame** del clip 1 (lo vas a usar como referencia en las siguientes).

## Paso 2 — AVATAR · Secuencias 2 a 8
Para cada una (S2…S8):
1. **Generación nueva** (NO encadenar en el mismo chat).
2. Cargá el **frame del clip 1** como imagen de referencia + "mantené TODO idéntico, no agregues ni cambies nada".
3. Pegá el prompt de esa secuencia (archivo reel-002, sección 3): cámara + acción + locución.
4. Generá y elegí toma.
> Recordá: NO repetir "+40% bronceado" ni la línea de cierre en S2-S8.

## Paso 3 — B-ROLLS (BR1 a BR5)
Para cada B-roll:
1. En Flow, pegá el prompt (archivo reel-002, sección 4). No necesita imagen de referencia.
2. Duración: BR1/BR2/BR3/BR5 = 6s · BR4 = 4s.
3. Motion graphics → modo **Fast** (Quality solo si querés render más fino).
4. Verificá que NO meta voz (el bloque AUDIO/NEGATIVE ya lo prohíbe).

## Paso 4 — EDICIÓN en CapCut
1. Importá los 8 clips de avatar + los 5 b-rolls.
2. Armá la narración del avatar en la línea de tiempo (S1→S8).
3. Montá los b-rolls **encima**, en sus tiempos (BR1 0:02, BR2 0:22, BR3 0:34, BR4 0:50, BR5 1:02). Target ~50% del timeline.
4. **Textos en pantalla** (archivo reel-002, sección 2) sincronizados con la locución.
5. **Capa de realismo** (ajuste personalizado, valores del curso):
   `Temp -3 · Tinte +2 · Sat -6 · Exp -3 · Contraste +12 · Highlights -35 · Sombras -18 · Fade +6`
6. Música (Epidemic Sound / biblioteca) + subtítulos.
7. Exportá 9:16, 1080×1920.

## Checklist final antes de publicar
- [ ] Hook claro en los primeros 3s · [ ] Avatar consistente entre clips (cara/ropa/fondo)
- [ ] Sin voz en los b-rolls · [ ] Textos sincronizados · [ ] Capa de realismo aplicada
- [ ] CTA visible · [ ] Audio nivelado

> Si algún clip sale mal (avatar deformado, fondo cambiado, locución rara), avisame
> con qué pasó y ajusto el prompt de esa secuencia.
