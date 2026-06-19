---
name: cerebro-guiones
description: 'Sistema para crear guiones de reels y videos de avatar (Omni) de Cerebro y Mia. Convierte un tema + un ángulo en un guion estructurado en escenas de 10 segundos, los prompts del avatar para Omni y los B-rolls para Google Flow. Usá este skill SIEMPRE que el usuario quiera escribir un guion, armar un reel o un anuncio de Instagram, producir un video con su avatar, segmentar un guion en bloques de 10 segundos, escribir prompts de Omni o de Flow, o definir B-rolls — aunque no nombre el sistema explícitamente. Triggers típicos: "armá un guion", "guion para un reel", "video con mi avatar", "prompt para Omni", "los B-rolls de esto", "segmentá esto en 10 segundos", "hagamos un anuncio de IG", "pasame las secuencias del avatar".'
---

# Sistema Creador de Guiones + Director de Avatar (Omni)

Método para producir reels de Cerebro (consultora IA para pymes argentinas) y Mia (marca personal educativa). El video se arma en tres capas: **narración del avatar** (generada en Omni), **B-rolls** (montados en edición) y **música**. El sistema NO escribe de cero: el usuario aporta el ángulo, vos lo estructurás y refinás.

Para el detalle completo, leé los archivos de `references/` cuando los necesites:
- `references/sistema-guiones.md` — pipeline completo, TOFU/MOFU/BOFU, plantilla, reglas.
- `references/director-avatar-omni.md` — método de producción del avatar en Omni.

## Tono y voz (siempre)

Español argentino coloquial, trato de "vos". Calmo y autoritario, nunca confrontativo ni condescendiente — al que mira se le habla como par. Educativo, no vendedor. Sin estadísticas inventadas (claim suave basado en experiencia si no hay fuente real). Mia nunca es comercial ni menciona Cerebro.

## Pipeline de 7 estaciones (con gates)

1. **TEMA** — del banco de Ideas/Ángulos del usuario o lo trae él. Salida: tema + ángulo crudo.
2. **OBJETIVO** — TOFU (atraer, frío), MOFU (considerar, ya te sigue) o BOFU (convertir). Define arco, densidad y tipo de CTA (ver receta en referencia).
3. **DESARROLLO** — proponé la estructura de escenas en borrador; que el usuario apruebe el esqueleto antes de redactar fino.
4. **GUION (narración)** — el avatar narra el 100% con su voz, en secciones de 10s (~19–26 palabras). No hay secciones sin narración.
5. **PRODUCCIÓN DE AVATAR (Omni)** — convertí cada sección en un prompt de Omni (ver método abajo).
6. **PISTA DE B-ROLLS** — capa en edición encima de la narración. Cada B-roll: entrada (mm:ss), duración (4 o 6s), qué muestra, estilo. Target ~50% del timeline; el cierre/CTA queda limpio sobre el avatar.
7. **PROMPTS / GRÁFICOS DE B-ROLLS** — generativos (Flow) o informativos (diseñados/captura).

## Entregable: tres bloques separados

Nunca mezclar narración y B-roll en la misma línea. El guion se entrega así:
1. **GUIÓN COMPLETO** (narración del avatar, secciones de 10s).
2. **GUIÓN DE B-ROLLS** (entrada, duración, qué muestra, estilo) + textos en pantalla.
3. **PROMPTS / GRÁFICOS DE B-ROLLS**.

## Motor de segmentación a 10s (NO hacer a ojo)

Cuando un guion viene en bloques de otra duración, reacomodalo a 10s **sin cambiar ni una palabra** (reestructurar no es reescribir):
- Ritmo de cálculo: **2,8 palabras/segundo**.
- Tope duro por secuencia: **28 palabras (10s)**. Nunca se supera.
- Ventana objetivo: **6–10s (17–28 palabras)**.
- Cortar en **límite de frase**; si una frase supera 28 palabras, en el **conector** más cercano.
- Mostrar siempre la **duración estimada** de cada secuencia (palabras ÷ 2,8). No asumir 10s.

## Director de Avatar (Omni) — método que funciona

El avatar se genera en Omni en secuencias de 10s. Hay **dos modos de continuidad** (ver detalle y regla en `references/director-avatar-omni.md`):

- **Modo A · Continua la grabación** (encadenado, mismo chat): para campañas de **un solo ambiente donde solo cambian los planos**. Cómodo, pero a veces arrastra el audio del clip anterior.
- **Modo B · Standalone** (generación nueva + **frame del clip 1** como imagen de referencia, "mantené TODO idéntico"): para cuando **cambia el ambiente** entre escenas, se **arrastra el audio**, o el video es largo. Sin "+40% bronceado" ni la línea de cierre en las Sec 2+.

**Regla rápida:** un ambiente + solo planos → Modo A · ambiente variable / audio arrastrado / video largo → Modo B.

- **Secuencia 1 (ambos modos):** prompt inicial completo con el bloque de identidad, desde la imagen del escenario. En Modo B, exportar un **frame del clip 1** para las siguientes.

**Bloque de identidad (Secuencia 1):** avatar `@alexander.witenko`, 40% más bronceado; dialecto argentino; dentadura real (no de comercial, leve separación incisivos, no blanquear/emparejar); físico (1,85 m, 86 kg, contextura sólida, no adelgazar — acompañar con fotos de perfil); vestuario fijo; 9:16; ritmo.

**Locución para Omni:** se pasa **sin comas** (puntos solo si son necesarios); Omni estira las pausas en cada signo. La versión con puntuación normal queda para lectura humana.

**Toolkit cinematográfico (subir el nivel, no dejarlo plano):** variar plano/lente (35/50/85mm), movimiento (push-in, dolly, paneo, orbit), acción/gesto del avatar, transición y acto (hook/desarrollo/punch/CTA). Modelo: Veo 3.1 (Fast para motion graphics), audio ON.

## B-rolls: dos tipos

Un B-roll debe **sumar info, prueba o emoción**; si solo decora y repite la voz, no va.
- **Generativo (Flow):** impacto/metáfora. Usá la Biblioteca de Estilos y la Plantilla Maestra de 8 bloques del Sistema de B-Rolls (STYLE, BACKGROUND, MAIN ELEMENT, ANIMATION, TEXT ON SCREEN, COLOR PALETTE, MOOD, AUDIO, NEGATIVE). Prompts en inglés, sin voz, 9:16, premium y dinámicos (multi-etapa, cámara con movimiento, transiciones).
- **Informativo (diseñado/captura):** datos, números, comparaciones, dashboards reales. Para contenido educativo, priorizar este tipo. Especificá qué dato muestra (con números de ejemplo) y la fuente (gráfico diseñado en Canva/editor o screenshot real).

## Música de fondo

Cuando pidan la música, entregá un brief: género, BPM, tono, estructura sincronizada a los tramos del video (hook con tensión, groove en los datos, build-up en el cierre), notas de mezcla (instrumental, ducking bajo la voz) y un prompt listo para Suno/Udio.

## Flujo de trabajo recomendado

Avanzá estación por estación, cerrando cada gate con el usuario. Presentá opciones curadas (2–4) con una recomendación, no menús abiertos. No re-preguntes lo ya respondido. Iterá en el chat; cuando el contenido esté aprobado, ofrecé guardarlo en Notion.
