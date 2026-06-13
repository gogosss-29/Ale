# 🧬 Framework SOUL

> Ruta: 🦞 Reto Imperial OpenClaw › 🧬 Framework SOUL

**🎬 Vídeo (25.7 min):** https://www.youtube.com/watch?v=M8kOnNLL-3E

---

# Framework SOUL: El 1% que saca OpenClaw al máximo

La mayoría instala OpenClaw, lo conecta a Telegram, le pide un par de cosas y dice "listo, funciona." Y sí, funciona. Pero están usando el 1% de lo que realmente puede hacer.

En este video muestro el framework SOUL, que es el sistema que uso para convertir el agente de algo reactivo a algo que trabaja por ti aunque no lo estés mirando.

**S — Setup:** El error más común es no hacer un onboarding real. El agente no sabe quién eres, qué haces, ni cómo trabajas. Antes de pedirle cualquier cosa, hay que llenarlo de contexto. Yo le di acceso a mis correos, a mis conversaciones de Gemini, a mi canal de YouTube, a mis redes. Le dije que investigara hasta conocerme mejor que yo mismo.

**O — Orquestar:** Los features que nadie usa. El agente puede ejecutar comandos en terminal, instalar sus propias herramientas cuando no puede lograr algo, y tomar control del navegador via extensión de Chrome. Además existe CloudHub, que es básicamente un App Store de skills para el agente — Trello, Slack, Whisper, Google, cientos de opciones instalables en segundos.

**U — Unificar:** El mismo agente responde por Telegram, Slack, Discord, WhatsApp o lo que uses. Mismo contexto, mismo agente, distintos canales. Y puede hablar con otros agentes en paralelo — mi hermano y yo tenemos un grupo de Telegram donde nuestros bots trabajan en colaboración.

**L — Libertad:** Acá está la diferencia real. El heartbeat y los CronJobs convierten al agente de reactivo a proactivo. El heartbeat revisa tareas pendientes y las ejecuta solo. Los CronJobs programan acciones específicas: todos los viernes a las 6, el día 1 de cada mes, cada 3 horas. El mío me manda un resumen matutino con trending topics de Twitter y un borrador de newsletter antes de que yo despierte.

**El tema de seguridad:** Si lo instalaste en un VPS sin Tailscale, probablemente estás expuesto. Existe Shodan, un servicio que escanea todo internet, y si buscas Cloudbot aparecen miles de instancias con IP y puerto público. La solución es crear una red privada entre tu VPS y tu computador para que el servidor sea invisible al resto de internet. Las instrucciones están en la descripción del video.
