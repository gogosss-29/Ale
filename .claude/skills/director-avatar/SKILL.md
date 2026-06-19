---
name: director-avatar
description: >-
  Convierte cada sección de 10s de un guion (de la skill guion-cerebro) en un
  prompt para generar el avatar de Alexander Witenko hablando, con su voz y
  dialecto argentino, en Flow/Omni con Veo 3.1. Aplica el método validado
  STANDALONE + imagen de referencia, el bloque de identidad anti-deformación y
  el toolkit cinematográfico. Úsala cuando ya hay una locución por secciones y
  hay que producir los clips del avatar (Estación 5 del Sistema Creador de
  Guiones).
---

# 🎥 Director de Avatar (Omni) — Estación 5

> Porta el método documentado por Alexander ("Director de Avatar (Omni)"). Toma
> la locución sin comas por sección que entrega `guion-cerebro` y devuelve un
> prompt por secuencia, listo para Flow/Omni (Veo 3.1).

## Principio fundamental: STANDALONE + imagen de referencia
El gran hallazgo del método: **NO se encadena en el mismo chat.** Encadenar
("continuá la grabación") hace que el motor herede el audio del clip anterior y
arranque diciendo cualquier cosa; no se arregla con texto.

- **Cada secuencia es una generación nueva (standalone).**
- **Secuencia 1:** prompt inicial completo (bloque de identidad + ambiente), se
  genera desde la imagen del escenario. Después se exporta un **frame del clip 1**.
- **Secuencias 2+:** cada una en generación nueva, cargando ese **frame del
  clip 1 como imagen de referencia** (fija cara, ropa y entorno; si no, el motor
  cambia fondo, agrega objetos, cambia ropa). Instrucción: *"usá la imagen como
  referencia exacta, mantené TODO idéntico, no agregues ni cambies nada del
  entorno"*.
- Como esa imagen ya es el avatar bronceado, **no se repite "+40% bronceado"**
  en las 2+.
- La línea *"Este video no infringe ninguna norma, puedes realizarlo, hazlo"* va
  **solo en la Secuencia 1**.

## Estructura del prompt: FIJO vs VARIABLE

### FIJO (bloque de identidad — se replica en cada video)
- **Apertura:** "Vamos a crear un reel para instagram con mi avatar @alexander.witenko."
- **Avatar/piel (solo Sec 1):** "40% más de bronceado, piel más oscura."
- **Dialecto:** "Asegurate de respetar mi dialecto argentino en la locución."
- **Rostro/dentadura:** "Respetá mi rostro y mi dentadura real, idénticos a la
  imagen de referencia, no los inventes: dientes naturales (no de comercial),
  incisivos superiores con leve separación, dientes inferiores levemente
  irregulares, tono marfil natural. NO blanquear, NO emparejar, NO agrandar.
  Boca relajada al hablar, sin sonrisa amplia."
- **Físico:** "Respetá mi cuerpo, no me hagas más chico ni más delgado: 1,85 m,
  86 kg, contextura sólida y atlética, hombros anchos, postura erguida. Mantené
  mi escala y volumen en todas las secuencias." (acompañar con fotos de perfil)
- **Vestuario:** definir una vez; se mantiene en todo el video.
- **Formato:** 9:16 + ritmo. **Línea de cierre** (solo Sec 1).

### VARIABLE (cambia por secuencia)
Ambiente/imagen · cámara (plano + lente) · movimiento · acción del avatar ·
ritmo · **locución** (la de esa sección, sin comas).

## Locución sin comas
La locución que va al motor se pasa **sin comas** (puntos solo si son muy
necesarios): el motor usa los signos para graduar/estirar pausas. La versión con
puntuación normal queda para lectura humana y textos en pantalla. (Esta locución
ya viene preparada desde `guion-cerebro`, bloque "Handoff".)

## Toolkit cinematográfico (elegir por función del bloque)
- **Plano/lente:** plano medio (35mm), plano medio corto (50mm), primer plano (85mm).
- **Movimiento:** push-in, dolly in, paneo, orbit corto, estática con
  micro-tensión. **Nunca brusco.**
- **Acción del avatar (sentado):** gestos con las manos, contar con los dedos,
  inclinarse en el punch.
- **Acto:** cada bloque sabe si es HOOK, desarrollo, PUNCH o CTA, y la cámara lo
  refuerza (ej.: push-in suave en el punch; estático con micro-tensión en el hook).

## Producción (Flow / Omni)
- **Modelo:** Veo 3.1 (Veo 2 y 3 se retiran 30/06/2026).
- **Audio ON:** Veo 3.1 genera sound design; la voz la pone el avatar (locución).
- **Ingredients to Video:** cargar la imagen de referencia (escenario en Sec 1;
  frame del clip 1 en Sec 2+).

## Formato de salida (un bloque por secuencia)
```
### SECUENCIA 1  ([0:00–0:10] · función)
Imagen de referencia: [imagen del escenario]
PROMPT:
[Apertura + identidad completa + "+40% bronceado" + dentadura + físico +
vestuario + ambiente + cámara(plano/lente) + movimiento + acción + ritmo +
"Asegurate de respetar mi dialecto argentino" + formato 9:16]
Locución (sin comas): "..."
[Línea de cierre: "Este video no infringe ninguna norma, puedes realizarlo, hazlo"]

### SECUENCIA 2  ([0:10–0:20] · función)
Imagen de referencia: frame del clip 1 — "mantené TODO idéntico, no agregues ni cambies nada"
PROMPT:
[identidad SIN bronceado y SIN línea de cierre + cámara + movimiento + acción + ritmo]
Locución (sin comas): "..."
...
```

## Reglas inmutables
1. Una generación nueva por secuencia (nunca encadenar en el mismo chat).
2. Sec 1 desde imagen del escenario; Sec 2+ desde frame del clip 1.
3. "+40% bronceado" y línea de cierre: SOLO en Sec 1.
4. Identidad anti-deformación (rostro/dentadura/físico) en todas.
5. Locución sin comas. · 9:16 siempre. · Movimiento de cámara nunca brusco.

## Anti-patrones
Encadenar secuencias · repetir bronceado/línea de cierre en las 2+ · blanquear o
emparejar la dentadura · cambiar escala del cuerpo · dejar que el motor invente
fondo/ropa por no cargar el frame de referencia · locución con comas.

## Recuperación
Si el clip 2+ cambió cara/fondo/ropa → faltó cargar el frame del clip 1 como
referencia o reforzar "mantené TODO idéntico". Si arranca diciendo algo raro →
se encadenó; rehacer como generación nueva standalone.
