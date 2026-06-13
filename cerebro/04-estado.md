# 04 — Estado & Pendientes

_Última actualización: 2026-06-13 por Claude (Claude Code)._

## Decisión de ruta (2026-06-13)
**Se desarrolla primero la RUTA DEL CURSO (AvatarHype), no Higgsfield.** Alexander
quiere crear su avatar **con el método del curso** y ver qué tal funciona, respetando
el curso. La ruta Higgsfield (Soul v2) queda en reserva como apoyo de identidad.
- Adaptación hecha en `avatarhype/`: el avatar es ÉL pasando su foto como referencia
  (`avatar_referencia_path` / `--avatar-referencia`); el paso de imágenes genera una
  imagen-ancla suya (GPT Image 2) que se usa como primer frame de los clips. Sustituye
  la captura de Pinterest del curso por su cara; el resto del método es idéntico.
- **Para probarlo falta:** (a) API key de APImart (`APIMART_API_KEY`), (b) una foto
  limpia de su cara (idealmente luz blanca/natural, frontal). Entry point barato:
  `python -m avatarhype.cli avatar --avatar-referencia foto.jpg` (~0,012 €).

## Hecho ✅
- Soul **Alexander v2** entrenado y listo (`9ffc9c16-...`).
- Voz subida: clip 12 s + completa 3:27.
- Retratos generados con el Soul v2 (neutro y sonriendo) — buen parecido.
- Cerebro creado en el repo (`cerebro/` + `CLAUDE.md`).

## Pendiente 🔜
1. **Vídeo hablado** (tarea principal). Todo listo para lanzar; bloqueado por
   `requires approval` en este entorno. **Acción**: ejecutar `generate_video` en una
   sesión interactiva nueva con los parámetros de `03-activos.md` + `02-playbook.md §F`.
2. **Volcar el cerebro a Notion** (proyecto "🧠 Cerebro — Sistema Avatar IA" bajo
   "Recursos - Varios", id `36d5f724-2166-804f-8e4a-f2721b4f84ad`). Bloqueado por el
   mismo `requires approval` al crear páginas. **Acción**: crear las páginas desde una
   sesión con escritura aprobada, copiando el contenido de estos `.md`.

## Ideas / próximos pasos sugeridos
- Generar tanda de retratos en distintos looks (profesional, casual, exterior).
- Versiones de vídeo en 9:16 (reels) y 16:9.
- Si el parecido aún no es perfecto: regrabar 1–2 vídeos de primeros planos con
  **luz blanca/natural** (no LED morado) y reentrenar el Soul.
- Explorar `virality_predictor` para evaluar los vídeos antes de publicar.

## Bitácora
- 2026-06-12 ~21:10: una sesión previa accedió al curso AvatarHype (vía Whop) y
  documentó TODO en `docs/` + creó el pipeline `avatarhype/`.
- 2026-06-12: subidas iniciales, Soul v1 (no se parecía), voz cargada.
- 2026-06-12/13: extracción de fotogramas de 8 vídeos, Soul v2 entrenado, retratos OK.
- 2026-06-13: confirmado que `generate_video` y escritura en Notion fallan por
  aprobación en entorno automático; cerebro persistido en el repo.
- 2026-06-13: **corregido un error**: el `cerebro/` se había construido ignorando el
  curso real de `docs/`. Reescrito `01-el-curso.md` y `00` para apuntar a `docs/` y
  `avatarhype/`. La metodología y prompts viven en `docs/`, no se duplican aquí.

## Nota de seguridad pendiente
- El 2026-06-13 se pegó en chat una cookie de sesión de Whop con tokens vivos.
  **Acción del usuario:** cerrar sesión en Whop y reentrar para invalidarla.
