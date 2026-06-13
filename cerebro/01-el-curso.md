# 01 — El Curso (paso a paso, replicable de cero)

Este es el recorrido completo para crear el avatar digital desde cero. Cada paso
indica el **qué** y el **porqué**; los **cómo** exactos (comandos, parámetros) están
en `02-playbook.md`.

## Fase 1 — Entrenar el Soul (identidad reutilizable)
1. **Reunir material**: 15–20 imágenes de la persona, variadas en ángulo (frontal,
   perfil, tres cuartos), expresión e iluminación. Más variedad = mejor parecido.
2. **Si solo hay vídeos**: extraer fotogramas nítidos (ver playbook). Priorizar
   **primeros planos** de la cara; descartar fotos de espaldas, borrosas o con ojos
   cerrados. Evitar que todas tengan la misma luz de color (p. ej. LED morado),
   porque el modelo hereda ese tinte en la piel.
3. **Subir las imágenes** a Higgsfield (flujo `media_upload` → PUT → `media_confirm`).
4. **Entrenar** con `show_characters action=train`, tipo `soul_2`, pasando las
   **URLs https** de las imágenes (no los UUID; el validador rechaza UUID en bruto).
5. **Esperar** ~10 min hasta `status: ready`.

> ⚠️ Lección aprendida: el primer Soul (v1) se entrenó con pocas fotos y poco
> variadas y **no se parecía**. El v2, con 15 fotogramas de vídeos reales, sí. La
> calidad y variedad del material de entrada es lo que más impacta el resultado.

## Fase 2 — Subir la voz
1. Conseguir 1–3 min de audio limpio de la persona hablando.
2. Si viene como `.mp4` de WhatsApp, **convertir a `.mp3`** (Higgsfield rechazaba el
   contenedor mp4 de audio). Ver playbook.
3. Subir (`media_upload` → PUT → `media_confirm` type=audio).
4. **Recortar un clip de ~12 s** para usarlo como audio del vídeo.

## Fase 3 — Generar imágenes (validar el parecido)
1. `generate_image` con `model: soul_2` + el `soul_id`.
2. Prompt enfocado en retrato realista, luz neutra, expresión natural.
3. Revisar el parecido. Si no convence, volver a Fase 1 con mejor material.

## Fase 4 — Generar el vídeo hablado
1. `generate_video` con modelo `seedance_2_0` (o `veo3_1` calidad máxima).
2. `start_image` = un retrato generado del Soul; `audio` = el clip de voz de 12 s.
3. Formato 9:16, 12 s, 720p, prompt de lipsync (ver playbook/activos).

> ⚠️ Lección aprendida: `generate_video` se bloquea con `requires approval` en
> entornos automáticos. Ejecutar en sesión interactiva (ver `00`).

## Fase 5 — Persistir el conocimiento (este cerebro)
1. Escribir IDs, proceso y estado en el repo (`cerebro/` + `CLAUDE.md`).
2. Reflejar en Notion para lectura humana.
3. Actualizar `04-estado.md` tras cada avance.

## Resumen del flujo
Material → Soul entrenado → (validar con imágenes) → + Voz → Vídeo hablado →
todo registrado en el cerebro.
