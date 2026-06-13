# Proyecto Ale — Avatar digital de Alexander (Higgsfield)

> **Para cualquier sesión nueva:** este archivo es el traspaso de contexto. Léelo
> entero antes de actuar. El usuario (Alexander) viene trabajando en crear su
> "digital twin" en Higgsfield: un Soul entrenado con su cara + su voz, para
> generar imágenes y un vídeo hablado. Todos los IDs de abajo viven en su cuenta
> de Higgsfield y siguen válidos entre sesiones.
>
> **🧠 CEREBRO COMPLETO:** la documentación detallada y reproducible está en la
> carpeta [`cerebro/`](cerebro/): `00-vision-y-conexion`, `01-el-curso` (paso a
> paso), `02-playbook` (cómo técnico), `03-activos` (IDs), `04-estado`. Empezar
> leyendo `cerebro/00`, `cerebro/03` y `cerebro/04`.

## Objetivo actual
Generar un **vídeo hablado** (avatar de Alexander moviendo los labios sincronizado
con su propia voz). Las imágenes ya funcionan; el vídeo quedó pendiente por un
problema de aprobación de la herramienta `generate_video` (ver más abajo).

## Activos en Higgsfield (IDs válidos entre sesiones)

| Elemento | ID / valor |
|---|---|
| **Soul "Alexander v2"** (LISTO, usar este) | `9ffc9c16-eeb2-465d-b2b5-03a7b14a227d` |
| Soul "Alexander" v1 (antiguo, NO se parecía) | `332ec8a8-f2cf-4e03-ba77-2d761b5c3754` |
| **Retrato base** v2 (neutro, mirando a cámara) | `43c9b6e8-e08c-47af-b8b7-94b61bae1b2e` |
| Retrato v2 alternativo (sonriendo) | `58c21662-17ef-4a33-8b7b-04bd781e8c78` |
| **Voz — clip 12 s** (para el vídeo) | `41bd653e-a16f-4089-baea-60cbcfba1d18` |
| Voz — completa 3:27 | `efc51158-010b-4a2f-ae28-a9b1d4026f90` |

- Tipo de Soul: `soul_2`. Para generar imágenes con su identidad:
  `generate_image` con `model: "soul_2"` + `soul_id` del Soul v2.
- El Soul v2 se entrenó con 15 fotogramas extraídos de 8 vídeos suyos (IMG_3393–3401).
  Nota: todo el material tenía luz LED morada; si hace falta mejorar, pedir vídeos
  con luz blanca/natural y reentrenar.

## TAREA PRINCIPAL PENDIENTE: el vídeo hablado
Lanzar `generate_video` con estos parámetros exactos:

```
model: seedance_2_0      (alternativa máxima calidad: veo3_1)
medias:
  - { role: start_image, value: 43c9b6e8-e08c-47af-b8b7-94b61bae1b2e }
  - { role: audio,       value: 41bd653e-a16f-4089-baea-60cbcfba1d18 }
aspect_ratio: 9:16
duration: 12
resolution: 720p
prompt: "The man speaks directly to the camera in a natural, relaxed way, lips
perfectly synchronized with the provided voice audio, subtle natural head
movements and blinking, soft neutral indoor lighting, steady camera, realistic"
```

## Problema de aprobación de `generate_video` (historial)
- En la sesión original, `generate_video` devolvía siempre:
  `Streamable HTTP error: Error POSTing to endpoint: MCP tool call requires approval`.
- `generate_image`, subidas, audio y entrenamiento SÍ funcionaban en esa sesión.
- El permiso de Claude YA estaba concedido: `mcp__Higgsfield__generate_video` está
  en `allow` dentro de `.claude/settings.local.json` desde el 12-jun 22:30, y aun
  así fallaba. ⇒ NO era el sistema de permisos de Claude.
- Hipótesis vigente: la generación de **vídeo de persona real + voz** dispara un
  paso de aprobación/consentimiento del lado de Higgsfield/MCP que el entorno
  remoto de la sesión original no podía atender. En una **sesión nueva** el vídeo
  parece sí ejecutarse (el usuario confirmó "ahí lo hizo").
- **Acción para la sesión nueva:** intentar `generate_video` directamente con los
  parámetros de arriba. Si funciona, perfecto. Si vuelve a dar "requires approval",
  la alternativa segura es generarlo en la app/web de Higgsfield (imagen + audio ya
  están subidos en la cuenta del usuario).

## Notas de entorno / herramientas
- Higgsfield es un conector MCP. Flujo de subida de archivos del agente:
  `media_upload` → PUT de los bytes al `upload_url` con curl → `media_confirm`.
  Para entrenar Soul, pasar **URLs https** (CloudFront) de las imágenes, no los
  UUID en bruto (el validador rechazaba los UUID).
- Para archivos locales del usuario: `media_upload_widget` (sube de a uno).
- Google Drive: el conector falla al descargar archivos > ~10 MB ("session
  expired"); para vídeos grandes usar el widget de Higgsfield.
- Idioma del usuario: español. Responder en español.
