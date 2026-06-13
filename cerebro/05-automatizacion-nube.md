# 05 — Automatización en la nube (botón único)

Objetivo de Alexander: **todo en la nube, apretar un botón**, sin terminal ni código.

## Arquitectura (3 cajas)
```
[ Formulario n8n ]  →  [ n8n (orquestador) ]  →  [ Worker AvatarHype (FastAPI + ffmpeg) ]
   "metés el tema"        guarda las keys           corre el pipeline y devuelve el anuncio
                          en su store cifrado
```

- **Worker:** `avatarhype/service.py` (FastAPI) + `Dockerfile` (trae ffmpeg). Se despliega
  en un host de contenedores (Render / Railway / Fly / Cloud Run / VPS). Expone:
  - `GET /salud` (estado + qué keys hay, sin revelarlas)
  - `POST /producir` (tema → anuncio)
  - `POST /voz` (texto → tu voz)
- **n8n:** Form Trigger (el "botón") → HTTP Request al worker `/producir` → entrega el
  resultado (Drive / email / etc.).

## Dónde van las API keys (NUNCA por chat ni GitHub)
- En el **panel del host del worker** (ej. Render → Environment) como variables:
  `APIMART_API_KEY`, `ANTHROPIC_API_KEY` (o `OPENAI_API_KEY`), `ELEVENLABS_API_KEY`,
  `ELEVENLABS_VOICE_ID`, opcional `GEMINI_API_KEY`.
- En **n8n** solo hace falta la URL del worker (y un token propio si se protege).
- Alexander las pega una sola vez en esos paneles. El worker las lee de su entorno.

## Pasos para montarlo
1. Decidir host del worker (recomendado: Render o Railway — despliegan desde el repo).
2. Desplegar el repo (usa el `Dockerfile`). Cargar las keys en el panel del host.
3. Probar `GET /salud` → confirmar `ffmpeg: true` y keys en `true`.
4. Tener una instancia de n8n (cloud o self-host).
5. Importar el flujo: Form Trigger → HTTP Request `/producir` → entrega.
6. Apretar el botón → sale el anuncio.

## Giro de estrategia (2026-06-13): usar créditos de Flow (Ultra) vía agente de navegador
**Decisión de Alexander:** tiene Google AI **Ultra** (10.000 créditos/mes en **Flow**) y su
clon ya le gusta en Flow. **Verificado:** los créditos de Flow son **solo-web, NO usables
por API** (la API de Veo se factura aparte). ⇒ Para usar esos créditos automáticamente, la
única vía es **automatizar el navegador** (un agente que abre Flow, pega el prompt, genera,
descarga).
- **Camino elegido:** **agente IA de navegador (browser-use)**, corriendo **local** en la
  compu de Alexander, conectado a su Chrome con la sesión de Flow iniciada. Driven por los
  prompts del cerebro. (Playwright determinista se descartó: UI de Flow no inspeccionable
  desde acá.)
- **Contras asumidas:** corre local (no nube), zona gris de ToS de Google (volumen moderado),
  frágil ante cambios de UI. Necesita una key LLM para el agente.
- **APImart (ruta nube por API): TERMINADA y PARKED como backup.** Worker en Render funciona
  (`https://ale-9izu.onrender.com`), genera video con Veo 3.1 Fast pagando por clip. Se deja
  como opción a futuro para volumen sin tocar la compu.
- Se mantiene: cerebro (guiones+prompts 6C argentinos), grade cine, voz ElevenLabs. Solo
  cambia el paso de render (API → navegador en Flow).

## Estado
- ✅ **FUNCIONANDO EN LA NUBE (2026-06-13):** worker desplegado en Render (Docker, Free),
  URL `https://ale-9izu.onrender.com`. ffmpeg OK, key APImart cargada en Render.
  Formulario web `/` genera clips desde el navegador (botón v1, sin n8n).
  Primer vídeo generado OK con **Veo 3.1 Fast** (Omni Flash estaba saturado → se cambió de
  modelo desde el selector). Pago/saldo de APImart resuelto.
- 🔜 Siguiente: meter el avatar real (fotograma en URL pública), armar el anuncio de 3 clips
  + grade cine, sumar voz (ElevenLabs) + key LLM para el cerebro, y el botón n8n.
- Worker (`service.py`) + `Dockerfile` + `requirements-service.txt` listos.
