# Anuncio — "Estado de resultados" (avatar de Alexander, argentino)

Generado por el cerebro AvatarHype (Fase 1). Ángulo de dolor para emprendedores.
Acento Rioplatense forzado. 3 clips de ~8 s (≈24 s). Plano medio.

## Estrategia
- **Público:** dueños de negocio / emprendedores que facturan pero no saben si ganan.
- **Dolor:** miran la plata en la cuenta, no la ganancia real → confunden movimiento con rentabilidad.
- **Ángulo:** "tu cuenta bancaria te miente; tu estado de resultados te dice la verdad".

## Guion
1. (hook) ¿Tenés un negocio y mirás solo la plata que hay en la cuenta? Ese es el error más común.
2. (valor) El estado de resultados te muestra si de verdad ganás: ventas menos costos, tu ganancia real.
3. (cierre) Sin eso, laburás un montón y no sabés si te queda algo. Mirá tus números, no tu cuenta.

## Producción
- Plano **medio** (cabeza-hombros). Evitar plano abierto (la cara se nota más artificial de lejos).
- Frame inicial: un fotograma del avatar de Alexander (imagen→vídeo).
- Tras renderizar: unir los 3 clips y aplicar el **grade cine**
  (`python -m avatarhype.cli realismo --clip X --estilo cine`).
- Voz: si se quiere su voz real exacta, doblar con ElevenLabs por encima (lip-sync).

---

## Prompt 6C — Clip 1 (hook)
```
A hyper-realistic 9:16 handheld iPhone front-camera selfie video.
[CHARACTER] the exact same person from the provided reference images. Identity, face, skin texture, hair and outfit must match perfectly at all times.
[GOAL] Maximum realism. Must feel like a real casual UGC selfie, not AI-generated.
[ENVIRONMENT] sitting on a chair outdoors in a green field, soft natural daylight, cloudy sky
[ACTION] The subject is speaking to the camera, medium shot, head and shoulders.
[HUMAN MOTION] Movement must feel completely natural and human: slight vertical bounce, subtle side-to-side sway, natural shoulder movement, inconsistent micro-movements, and breathing that subtly affects motion and speech.
[LANGUAGE] Speak in authentic Argentinian Rioplatense Spanish (Buenos Aires). Use voseo ('tenés', 'mirás', 'sabés'), sheísmo (ll/y as soft 'sh'), porteño melodic intonation, fillers like 'che', 'viste', 'o sea'. Not Spain Spanish, not Mexican, not neutral Latin American.
[TONE] calm, confident, casual, not selling, not performing.
[SCRIPT] "¿Tenés un negocio y mirás solo la plata que hay en la cuenta? Ese es el error más común."
[BEHAVIOUR] Starts speaking slightly mid-thought, blinks naturally, briefly glances away, subtle pauses between phrases.
[CAMERA] slow gentle zoom in toward the face.
[LIGHTING] natural daylight only, slight exposure changes, soft uneven shadows.
[AUDIO] raw iPhone microphone, light ambient noise, audible breathing, no music.
[NEGATIVE PROMPT] studio lighting, beauty filter, perfect skin, ad-like polish, exaggerated gestures, robotic delivery, over-sharpening, artificial background, unnatural motion, flicker.
```

## Prompt 6C — Clip 2 (valor)
Igual que el Clip 1, cambiando:
```
[SCRIPT] "El estado de resultados te muestra si de verdad ganás: ventas menos costos, tu ganancia real."
[CAMERA] handheld iPhone selfie, slightly off-center framing, natural micro-shake, minor autofocus adjustments, rolling shutter effect, no stabilization.
```

## Prompt 6C — Clip 3 (cierre)
Igual que el Clip 1, cambiando:
```
[SCRIPT] "Sin eso, laburás un montón y no sabés si te queda algo. Mirá tus números, no tu cuenta."
[CAMERA] handheld iPhone selfie, slightly off-center framing, natural micro-shake, minor autofocus adjustments, rolling shutter effect, no stabilization.
```
