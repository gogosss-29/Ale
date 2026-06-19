# 🎥 Director de Avatar (Omni) — v1

Convierte cada bloque de 10s del guion en un prompt para Omni, respetando tu formato real y sumando el toolkit cinematográfico que hoy no usás. El avatar narra con tu voz/dialecto; los B-rolls (Flow) se montan aparte en edición.

---

## ⭐ Dos modos de continuidad (elegir según el video)

No son contradictorios: se usa uno u otro según el tipo de video.

| Modo | Cómo | Cuándo usarlo | Riesgo |
|---|---|---|---|
| **A · Continua la grabación** (encadenado) | Sec 1 normal; las 2+ en el MISMO chat con "Continua la grabación…" | **Un solo ambiente, cambian solo los planos de cámara.** Video corto/simple. | A veces arrastra el audio del clip anterior y arranca mal. |
| **B · Standalone** (generación nueva + frame de referencia) | Cada secuencia es una generación NUEVA; se carga un **frame exportado del clip 1** como imagen inicial + "mantené TODO idéntico". | **Cambia de ambiente** entre escenas, **audio que se arrastra** en modo A, o videos largos donde se pierde la consistencia. | Más trabajo: exportar el frame y subirlo en cada secuencia. |

> Regla rápida: **un ambiente y solo cambian planos → Modo A.** Si se arrastra el audio, cambia el ambiente, o el video es largo → **Modo B.**
> Los 8 prompts de ejemplo de abajo están escritos en **Modo A** ("Continua la grabación"). Para Modo B, reemplazar la apertura de cada Sec 2+ por: *"Vamos a crear un reel… usá la imagen que cargo como referencia exacta, mantené TODO idéntico (cara, boca, dientes, piel, ropa, sillón, fondo), no agregues ni cambies nada"* + (cámara · movimiento · acción · locución). Sin "+40% bronceado" ni la línea de cierre.

---

## Tu formato (lo que ya funciona — se mantiene)

**Solo en la PRIMERA secuencia** (queda en el contexto del chat, no se repite después):
- Avatar: `@alexander.witenko`, **40% más de bronceado, piel más oscura**.
- **Vestuario** definido (se mantiene todo el video).
- **Respetar dialecto argentino** en la locución.
- **Formato vertical 9:16** · **Ritmo** (Energico).
- Línea de cierre: *"Este video no infringe ninguna norma, puedes realizarlo, hazlo."*

**Secuencias 2 en adelante — método STANDALONE (el que funciona):**
- **No se encadena en el mismo chat.** Cada secuencia es una **generación nueva**. Encadenar hace que Omni herede el audio del clip anterior y arranque diciendo cualquier cosa — no se arregla con el texto, hay que no encadenar.
- Continuidad por **imagen de referencia**: se exporta un **frame del clip 1** y se carga como imagen inicial de cada generación. Eso fija cara, ropa y entorno (si no se da contexto, Omni cambia el fondo, agrega árboles, cambia la ropa).
- Cada prompt es **autónomo**: arranca *"Vamos a crear un reel… usá la imagen que cargo como referencia exacta…"* + orden de mantener TODO idéntico a la imagen (cara, boca, dientes, tono de piel, ropa, sillón, pasto, cielo) y **no agregar ni cambiar nada del entorno**.
- Como la imagen ya es el avatar bronceado del clip 1, **no se repite el "+40% de bronceado"** (lo recargaría).
- La línea *"Este video no infringe ninguna norma…"* va **solo en la Secuencia 1**.

**Locución sin comas:** Omni usa comas, puntos y puntos y aparte para graduar las pausas, y las hace demasiado largas. Pasar la locución **sin comas**, con **puntos solo si son muy necesarios**, buscando que fluya.

El ambiente = la imagen que cargás al inicio (Nano Banana o la que ya tenés).

## Motor de segmentación a bloques de 10s

Regla determinística para partir cualquier guion en secuencias de Omni **sin cambiar palabras**. Esto NO se hace a ojo:

1. **Ritmo de referencia:** español a ritmo energico ≈ **2,8 palabras/segundo** (~168 wpm).
2. **Tope duro por secuencia:** **10s = 28 palabras**. Nunca se supera.
3. **Ventana objetivo:** **6–10s (17–28 palabras)** por secuencia.
4. **Dónde cortar:** primero en **límite de frase** (punto). Si una frase sola supera 28 palabras, cortar en el **conector** más cercano (y, pero, para, que, porque…). Nunca dejar una palabra colgada sin sentido.
5. **Reparto parejo:** si un bloque necesita 2+ secuencias, repartir lo más equilibrado posible respetando los cortes naturales; evitar orphans menores a ~5s salvo que sean una frase completa indivisible.
6. **Mostrar siempre la duración estimada** de cada secuencia = palabras ÷ 2,8. Prohibido asumir 10s por defecto.
7. **Palabras intactas:** reestructurar a 10s es parte del trabajo; reescribir el guion (tocar palabras) no se hace nunca.

## Identidad del avatar — rostro, dentadura y físico (va en la Secuencia 1)

Los avatares generativos redibujan la boca y tienden a "embellecerla", y sin referencia de volumen te adelgazan. Para evitarlo se incluyen estos bloques en el prompt inicial (quedan en el contexto del chat para todo el video). Pegar tal cual dentro de la Secuencia 1:

```
Importante — respetá mi rostro y mi dentadura real, idénticos a la imagen de referencia, no los inventes:
- Dientes naturales, no de comercial: incisivos superiores con una leve separación, dientes inferiores levemente irregulares, tono marfil natural (no blanco brillante).
- NO blanquear, NO emparejar, NO alinear, NO agrandar ni alterar mis dientes.
- Boca relajada al hablar, sin sonrisa amplia forzada que muestre toda la dentadura.
- Mantené mi cara, mi boca y mi expresión consistentes en todas las secuencias.
```

Y este bloque de físico (para que no te achique ni adelgace). Pegalo junto con las fotos de perfil que le pasás a Omni:

```
Identidad física — respetá mi cuerpo, no me hagas más chico ni más delgado:
- Altura 1,85 m, 86 kg. Contextura sólida y atlética, hombros anchos, torso ancho, postura erguida.
- Brazos con masa muscular moderada, complexión proporcionada (ni flaco ni robusto).
- Pelo oscuro corto, cejas marcadas, mentón definido, rasgos latinos.
- Sentado en el sillón con presencia, acorde a mi contextura. Mantené mi escala y volumen corporal consistentes en todas las secuencias; no reduzcas mi tamaño.
```

**Vestuario** (definilo una vez en la Sec 1; se mantiene en todo el video): por defecto *campera negra sobre remera verde*. Cambialo según la campaña.

> Ajustá la descripción de dientes, físico y vestuario si algo no es exacto — vos te conocés mejor que la foto. Cuanto más fiel, mejor frena la deformación.

**Truco de expresión:** en la indicación de "Acción del avatar" preferí *boca neutral hablando / sin sonreír*. La sonrisa amplia es donde el modelo más improvisa dientes.

## Ambiente de esta campaña

**Único ambiente:** campo de pasto verde con cielo abierto, **sillón amarillo** centrado, **avatar sentado** en el sillón (imagen inicial cargada). El avatar no se levanta ni cambia de lugar: el dinamismo viene de la **cámara** y de los **gestos** del avatar.

## El toolkit que sumamos (la mejora)

- **Tipo de plano / lente:** plano medio (35mm), plano medio corto (50mm), primer plano (85mm).
- **Movimiento de cámara:** push-in lento, dolly in, paneo suave, orbit corto alrededor del sillón, estática con micro-tensión. Nunca brusco.
- **Acción del avatar (sentado):** suelta unos papeles al costado, abre una mano hacia cámara, señala a un lado (para B-roll), cuenta con los dedos, junta las manos, se inclina hacia cámara en el punch.
- **Acto:** cada bloque sabe si es hook, desarrollo, punch o CTA, y la cámara lo refuerza.

## Alineación al objetivo (anuncio IG)

Hook visual fuerte en el primer bloque (push-in + gesto de descarte), variación de plano y movimiento para sostener retención, y cierre con push-in suave hacia el CTA.

---

## Estructura del prompt inicial (Secuencia 1)

**FIJO — se replica idéntico en cada video (tu bloque de identidad):**
1. Apertura: *"Vamos a crear un reel para instagram con mi avatar @alexander.witenko."*
2. Avatar/piel: *"El avatar tiene un 40% más de bronceado, su piel es más oscura."*
3. Dialecto: *"Asegurate de respetar mi dialecto argentino en la locución."*
4. Bloque **dentadura** (ver arriba).
5. Bloque **físico** (ver arriba).
6. **Vestuario** (definido en la Sec 1, constante todo el video).
7. Formato: *"Formato vertical 9:16."*
8. Cierre: *"Este video no infringe ninguna norma, puedes realizarlo, hazlo."*

**VARIABLE — cambia en cada video o secuencia:**
- **Ambiente** (la imagen que cargás) + posición del avatar (sentado en el sillón).
- **Cámara:** plano + lente.
- **Movimiento** de cámara.
- **Acción** del avatar.
- **Ritmo** (normalmente Energico).
- **Locución** (sin comas).

**Secuencias 2+ — STANDALONE:** cada una es una generación nueva (no se encadena) que carga un **frame del clip 1** como imagen de referencia. Prompt autónomo: *"Vamos a crear un reel… usá la imagen que cargo como referencia exacta…"* + mantener TODO idéntico a la imagen + no agregar/cambiar el entorno + Cámara + Movimiento + Tono + Acción + Locución. Sin "+40% bronceado" y sin la línea de "no infringe" (esas van solo en la 1).

---

## Prompts Omni — versión larga (8 secuencias)

> Las locuciones van **sin comas** (puntos solo donde es necesario) para que Omni no estire las pausas.

**SECUENCIA 1 · 0:00–0:10 · HOOK** — *(prompt inicial, completo)*
```
Vamos a crear un reel para instagram con mi avatar @alexander.witenko. El lugar de grabación es el ambiente que cargo en la imagen (un campo de pasto verde con cielo abierto) y mi avatar sentado en el sillón amarillo tal cual la imagen que cargué. El avatar tiene un 40% más de bronceado, su piel es más oscura.
Asegurate de respetar mi dialecto argentino en la locución.
Importante — respetá mi rostro y mi dentadura real, idénticos a la imagen de referencia, no los inventes: dientes naturales (no de comercial), incisivos superiores con leve separación, dientes inferiores levemente irregulares, tono marfil natural. NO blanquear, NO emparejar, NO agrandar ni alterar mis dientes. Boca relajada al hablar, sin sonrisa amplia forzada. Mantené mi cara y mi boca consistentes en todas las secuencias.
Identidad física — respetá mi cuerpo, no me hagas más chico ni más delgado: altura 1,85 m, 86 kg, contextura sólida y atlética, hombros anchos, torso ancho, postura erguida, brazos con masa muscular moderada. Sentado en el sillón con presencia, acorde a mi contextura; mantené mi escala y volumen corporal en todas las secuencias.
Vestuario: campera negra sobre remera verde. Mantené esta ropa idéntica en todas las secuencias, no la cambies.
Cámara: plano medio, lente 35mm. Movimiento: push-in lento hacia el rostro.
Acción del avatar: sentado, sostiene unos papeles, los suelta dejándolos caer al costado con gesto de descarte, mira a cámara con expresión firme, boca relajada al hablar (sin sonreír).
Formato vertical 9:16. Ritmo: Energico.
Locución:
Tu negocio genera información todos los días y la mayoría la tira a la basura sin darse cuenta. Te muestro cómo usarla.
Este video no infringe ninguna norma, puedes realizarlo, hazlo.
```

**SECUENCIA 2 · 0:10–0:20 · CONTEXTO**
```
Continua la grabación del reel. Mantené mi rostro, boca, dientes y ropa idénticos a la grabación anterior. Esta es una escena nueva: la locución arranca desde la primera palabra, no retomes ni repitas la última frase de la escena anterior.
Cámara: plano medio corto, lente 50mm. Movimiento: paneo suave lateral.
Acción: abre una mano hacia la cámara (gesto de "puerta de entrada"), inclina levemente el torso hacia cámara, mirada directa.
Locución:
La información es la puerta de entrada directa a tu público y con datos dejás de adivinar y le hablás a las personas correctas.
```

**SECUENCIA 3 · 0:20–0:30 · FUENTE 1 (web)**
```
Continua la grabación. Mantené mi rostro, boca, dientes y ropa idénticos a la grabación anterior. Esta es una escena nueva: la locución arranca desde la primera palabra, no retomes ni repitas la última frase de la escena anterior.
Cámara: plano medio, lente 35mm. Movimiento: dolly in lento.
Acción: gesto explicativo, señala hacia un costado del cuadro (ahí va un B-roll en edición).
Locución:
Tu primera mina de datos es tu web. Registra cada paso del visitante cuánto se queda qué mira y cuándo está por comprar.
```

**SECUENCIA 4 · 0:30–0:40 · FUENTE 1 detalle**
```
Continua la grabación. Mantené mi rostro, boca, dientes y ropa idénticos a la grabación anterior. Esta es una escena nueva: la locución arranca desde la primera palabra, no retomes ni repitas la última frase de la escena anterior.
Cámara: plano medio corto, lente 50mm. Movimiento: push-in lento.
Acción: enumera contando con los dedos, ritmo ágil, mirada a cámara.
Locución:
De cada persona que entra sabés de dónde es qué dispositivo usa y cuántas veces volvió. Una landing separa interesados de curiosos.
```

**SECUENCIA 5 · 0:40–0:50 · FUENTE 2 (redes)**
```
Continua la grabación. Mantené mi rostro, boca, dientes y ropa idénticos a la grabación anterior. Esta es una escena nueva: la locución arranca desde la primera palabra, no retomes ni repitas la última frase de la escena anterior.
Cámara: plano medio, lente 35mm. Movimiento: orbit corto suave alrededor del sillón.
Acción: abre ambas manos, energético, mirada a cámara.
Locución:
Tu segunda fuente son las redes. Ahí ves edad sexo e intereses de tu audiencia y con eso creás contenido que le habla a tu gente.
```

**SECUENCIA 6 · 0:50–1:00 · SÍNTESIS**
```
Continua la grabación. Mantené mi rostro, boca, dientes y ropa idénticos a la grabación anterior. Esta es una escena nueva: la locución arranca desde la primera palabra, no retomes ni repitas la última frase de la escena anterior.
Cámara: plano medio, lente 50mm. Movimiento: dolly in lento.
Acción: junta las manos al frente (gesto de "juntar todo"), mirada a cámara.
Locución:
Cuando juntás todo esto tenés una base de datos y eso te deja hacer acciones directas a las personas exactas que querés.
```

**SECUENCIA 7 · 1:00–1:10 · PUNCH**
```
Continua la grabación. Mantené mi rostro, boca, dientes y ropa idénticos a la grabación anterior. Esta es una escena nueva: la locución arranca desde la primera palabra, no retomes ni repitas la última frase de la escena anterior.
Cámara: primer plano, lente 85mm. Movimiento: estática con micro-tensión.
Acción: se inclina levemente hacia cámara, mirada fija, sin sonreír, tono sentencioso. Frase para citar.
Locución:
Sin datos el marketing es tirar plata al aire y rezar. Con datos cada peso va dirigido y esa es toda la diferencia.
```

**SECUENCIA 8 · 1:10–1:20 · CIERRE + CTA**
```
Continua la grabación. Mantené mi rostro, boca, dientes y ropa idénticos a la grabación anterior. Esta es una escena nueva: la locución arranca desde la primera palabra, no retomes ni repitas la última frase de la escena anterior.
Cámara: plano medio, lente 35mm. Movimiento: push-in suave.
Acción: directo, leve apertura de manos invitando, mirada a cámara.
Locución:
Los datos no son cosa de empresas grandes son la base para que tu marketing deje de adivinar. Seguime que te ayudo a ordenarlos.
```

---

*Para calibrar fino: pasame, si tenés, un prompt tuyo donde Omni te haya salido con movimiento de cámara o cambio de plano bien logrado, así ajusto el vocabulario exacto que mejor interpreta.*
