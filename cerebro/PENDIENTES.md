# 📌 Pendientes — Cerebro · Máquina de contenido + Base de conocimiento

Backlog vivo de la sesión. Orden = prioridad sugerida.

---

## ⚙️ Remotion — MEJORAR SU USO (piloto hecho, en pausa)
**Estado:** piloto COMPLETADO ✅ — proyecto en `remotion/`, renderiza en este
entorno (chromium del contenedor + `--chrome-mode=chrome-for-testing`). Los 4
estilos ya portados a código y renderizados: #11 (BR3 v2), #12, #13 y #99.
Videos entregados a Ale para veredicto.
**Pendiente (anotado por Ale): ver cómo MEJORAR el uso de Remotion.** Ideas a
explorar cuando se retome:
- Veredicto de Ale sobre los 4 renders (¿#99 lo representa como firma?).
- **Parametrizar plantillas** (props: textos/datos/colores por reel, sin tocar diseño).
- Calidad visual: tipografía propia (embeber fuente de marca), grain/texturas,
  easings más finos, motion blur real (`@remotion/motion-blur`).
- Audio: sound design programado (ticks/whooshes/bass) con `<Audio>` en la compo.
- Flujo: comando único "render de todos los b-rolls de un reel" + naming por reel.
- Integrarlo al pipeline de la skill (la máquina entrega .mp4, no prompts, cuando
  la pieza es Remotion según el router).
- Marcar Remotion como "operativo" en `motor-produccion.md` tras el veredicto.

---

## 🎨 Estilo propio #99 "Cerebro Signature" — VALIDAR/ITERAR
**Qué es:** estilo insignia de marca (`cerebro-guiones/references/estilo-99-cerebro-signature.md`).
Grafito + oro fundido + line-art que se dibuja solo (caos→orden) + glifo Cerebro.
**Estado:** concepto v1 + 1 prompt de prueba aplicado al cierre del reel-003.
**Pendiente:** generarlo en Flow, ver cómo interpreta el "signature move" y el glifo,
e **iterar** (intensidad del oro, velocidad, glifo) hasta que sea inconfundible.
Decidir uso: #99 para momentos de marca (hook/cierre) + #11 para datos, o todo #99.
Relacionado: cerrar la idea de **"estilo propio por reel"** (mundo visual a medida del tema).

---

## 🎬 Captions del avatar — PENDIENTE DE OPTIMIZAR
**Estado:** motor funcionando con 3 enfoques renderizados sobre clip real:
1. Preset `marca` (karaoke 3 palabras, Archivo, activa en rojo, abajo).
2. Preset `minimal-top` v2 (1 palabra, Fraunces soft-serif, marfil, arriba). No convenció.
3. **`EditorialCaptions`** (frases compuestas sans+serif itálica, posiciones por frase,
   texto DETRÁS de la persona vía segmentación IA/rembg cuadro a cuadro). Es la dirección
   de la referencia 2 de Ale — falta pulirla con su feedback.
**Optimizar cuando se retome:** afinar tipografías/tamaños/posiciones con Ale,
más momentos "detrás" (funciona mejor con planos abiertos), animaciones por letra,
auto-propuesta de diseño de frases desde la transcripción, y velocidad del pipeline
(segmentación 196 frames ≈ minutos). Assets: modelo u2net_human_seg en ~/.u2net.

---

## ⭐ 0. Avatar Omni se DEFORMA por el bloque de identidad (IMPORTANTE)
**Problema:** los prompts del avatar con el bloque de identidad textual (dentadura
"no blanquear/no emparejar…" + físico "no me hagas más chico…") **deforman** la
cara/cuerpo en vez de fijarlos. Demasiadas aclaraciones → el modelo sobre-corrige.
**Hipótesis/soluciones a probar:**
- Confiar en la **imagen de referencia** (Modo B con un frame/foto real) y
  **reducir o quitar** las aclaraciones de texto sobre dientes/cuerpo.
- O simplificar el bloque de identidad a 1–2 frases positivas (no negativas).
- Pedirle a Ale un clip donde Omni le haya salido BIEN, para copiar ese vocabulario.
**Acción:** recalibrar `cerebro-guiones/references/director-avatar-omni.md` con lo
que realmente funcione en Omni. Afecta toda la producción de avatar.

---

## ⭐ 1. Auto-conexión al sistema de guardado de YouTube (IMPORTANTE)
**Objetivo:** que la lectura de **contenido nuevo** de los canales se haga
**automática**, sin que Ale exporte el `analisis_videos.xlsx` a mano cada vez.

**Contexto actual:**
- Proyecto de Antigravity (local en la máquina de Ale) descarga canales de YouTube
  y analiza cada video. Salida: `analisis_videos.xlsx`.
- Columnas: `Título del Video, URL del Video, Conceptos Clave, Información Útil,
  Casos y Experiencias, Citas Destacadas, Fecha de Análisis, Estado`.
- Estados: `Completado` / `Sin Transcripción` / `Error LLM`. Hoy: 67/408 completados.
- Hoy la ingesta es **manual**: Ale exporta el xlsx → se vuelca a
  `cerebro/base-conocimiento/`.

**Opciones para automatizar (decidir al implementar):**
1. **Claude Code local + ingesta incremental:** un script lee el xlsx/DB del
   proyecto Antigravity y agrega SOLO los `Completado` nuevos desde la última
   corrida a `base-conocimiento/`. Requiere correr el motor en la máquina de Ale.
2. **Carpeta/Sheet compartida (Drive):** Antigravity escribe a Google Sheets/Drive
   y se lee por MCP (atención: el conector Drive pidió `requires approval`).
3. **Graphify (lección 036):** correr sobre la carpeta de transcripciones; `graphify
   update` es incremental (solo procesa lo nuevo). Base consultable con menos tokens.
4. **Hermes (Fase 3):** cronjob diario que reingesta y deja ángulos nuevos
   propuestos cada mañana (encaja con la ventana 4-6am de Ale).

**Recomendado:** hacerlo cuando montemos Claude Code local (opción 1 + 3), y luego
automatizar el disparo con Hermes (opción 4).

**Dependencias:** instalar Claude Code local; (para Drive) resolver el permiso del
conector; saber dónde guarda Antigravity la DB/transcripciones.

---

## 2. Correr el orquestador `reel-cerebro` en vivo (próximo paso natural)
Tomar un ángulo (banco Notion o base de conocimiento) → guion en la **voz
calibrada** de Ale → Ale aprueba/corrige → guardar en Notion "Guiones" (primera
entrada del bucle de mejora). Demuestra todo el sistema de punta a punta.

## 3. Fase 2 — MCP a fondo
- **Escritura en Notion:** resolver el posible `requires approval` para guardar
  guiones en "Guiones".
- **Experimento auto-avatar con Higgsfield** (Soul + voz): ver si cierra el loop
  de video sin Flow (calidad a verificar vs método Veo 3.1 validado).

## 4. Fase 3 — Hermes 24/7
Servidor (VPS/Mac Mini) + Telegram/WhatsApp + cronjobs. Primeros casos: reel listo
a las 6am · captación de Cerebro por WhatsApp. Requiere cuentas/claves/Tailscale.

## 5. Completar la base de conocimiento
316 videos `Sin Transcripción` + 25 `Error LLM`. Depende de que el proyecto
Antigravity los procese. Cada lote nuevo → reingesta (ver pendiente #1).

## 6. Más calibración de voz
Ingerir el **Google Doc de marca personal** de Ale (borradores) para afinar
`voz-ale.md` y el few-shot. Bloqueado por `requires approval` del conector Drive
(o Ale pega el texto).

## 7. (Opcional) Regenerar `reel-001` en la voz calibrada
Para tener un ejemplo completo end-to-end ya en la voz de Ale.
