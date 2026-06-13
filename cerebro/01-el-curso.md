# 01 — El Curso (AvatarHype) + nuestra ejecución

> ⚠️ Corrección (2026-06-13): este archivo antes era un resumen flojo del proceso e
> **ignoraba el curso real ya extraído en `docs/`**. Corregido para apuntar al
> material verdadero.

## A) El Curso real: AvatarHype™ Academy
El curso que sustenta este proyecto está **completamente extraído y documentado** en
el repo (lo hizo una sesión previa accediendo a Whop). NO está aquí abajo: está en
`docs/`, que es la fuente. Aquí solo el mapa.

- **Documento maestro:** [`docs/SISTEMA-AVATARHYPE.md`](../docs/SISTEMA-AVATARHYPE.md)
  — el sistema completo (4 volúmenes), tesis, stack de herramientas, flujo de 6 pasos,
  Método 6C, plantilla de prompt de vídeo (14 bloques), capa de realismo de CapCut.
- **Índice:** [`docs/INDICE-CURSO.md`](../docs/INDICE-CURSO.md).
- **Transcripciones completas (ES):** `docs/transcripciones/` (4 lecciones, ~113 min).
- **Bibliotecas de prompts reales** (¡aquí están los prompts!): `docs/recursos-prompts/`
  - `plantilla_prompts_veo_3_1.md` — plantilla maestra de vídeo, 14 bloques, copiable.
  - `prompts_referencia_visual.md` — cambiar avatar, reemplazar fondo, plano cercano, podcast (flip).
  - `ads_imagen.md` — image-ads (testimonial, before/after, etc.).
  - `trends_virales_ads.md` — recrear un trend viral.
  - `mini_biblioteca_prompts_sora.md` — Sora (Vol.1, obsoleto, valor histórico).
- **Notas con links del curso:** `docs/notas-lecciones/` (Kie.ai, APImart, agentes GPT, recursos del alumno).
- **Pipeline en código (automatización):** carpeta `avatarhype/` (paquete Python).

### Resumen en una línea
AvatarHype enseña a producir **anuncios de e-commerce con avatares IA hiperrealistas**
(UGC, podcast, voz en off, dualcast, imagen) por la ruta más barata (revendiendo modelos
punteros vía Kie.ai / APImart). La clave no es la herramienta sino **el ángulo + el guion**.
Modelo más actual: **Omni Flash** (Vol. 4); formato nuevo: **Dualcast**.

## B) Nuestra ejecución práctica con Higgsfield (track complementario)
En paralelo al curso, en este proyecto se hizo la parte de **clon de identidad** con
Higgsfield (que el curso no cubre con tanta profundidad de "digital twin"):
1. Entrenar un **Soul** (identidad reutilizable) con fotogramas de vídeos reales.
2. Subir la **voz** y recortar un clip.
3. Generar **imágenes** del Soul (validar parecido).
4. Generar el **vídeo hablado** con lipsync.

El paso a paso técnico de esto está en [`02-playbook.md`](02-playbook.md) y los IDs en
[`03-activos.md`](03-activos.md). Encaja como el "paso 3–4" (imágenes/vídeo) del flujo
de 6 pasos del curso, pero usando Higgsfield en vez de APImart.

> Cómo se relacionan: **el curso = la metodología y los prompts**; **Higgsfield = una de
> las rutas de ejecución** para generar el avatar y el vídeo. El sistema grande (ver
> `docs/SISTEMA-AVATARHYPE.md §5`) automatiza todo el pipeline con n8n + APIs.
