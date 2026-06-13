# OpenClaw en Mac Mini desde cero (paso a paso)

> Ruta: Vibe-Coding › OpenClaw en Mac Mini desde cero (paso a paso)

**🎬 Vídeo (9.4 min):** https://www.youtube.com/watch?v=i5piRc39NPU&t=327s

---

Si quieres tener tu agente corriendo 24/7 sin depender de un VPS, el Mac Mini M4 es la opción más limpia que existe hoy. Fue diseñado para correr indefinidamente, tiene acceso completo a tus archivos locales, y el costo energético mensual en Chile sale alrededor de $2.000 pesos.

En este video muestro el setup completo desde que saco el Mac Mini de la caja hasta tener OpenClaw respondiendo por Telegram.

**Los pasos en orden:**

1. Configurar el Mac Mini como computador nuevo
2. Instalar Homebrew desde el terminal
3. Instalar Node.js vía Homebrew y verificar la versión
4. Instalar OpenClaw con el one-liner de [openclaw.ai](http://openclaw.ai)
5. Conectar el cerebro — para esto usé el token de Claude en vez del API key directo
6. Instalar Claude Code para que reconozca el comando de setup
7. Crear el bot en Telegram via BotFather y conectarlo
8. Primer mensaje, primera respuesta

El proceso completo toma menos de 10 minutos si tienes todo listo.

Un detalle práctico que no se menciona en otras guías: el puente entre tu computador principal y el Mac Mini se puede hacer con una carpeta compartida de Google Drive. Todo lo que modificas en un lado se refleja en el otro, lo que facilita mucho el manejo de archivos sin tener que estar físicamente frente al servidor.

Antes de terminar el video, dos advertencias importantes: si vas a instalar en VPS en lugar de Mac Mini, mira el video de seguridad con Tailscale primero. Y si es tu primera vez usando OpenClaw, hay un video separado de setup y onboarding que recomiendo ver antes de este.
