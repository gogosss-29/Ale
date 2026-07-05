# 💡 Conceptos clave

> Ruta: 🦞 Reto Imperial OpenClaw › 💡 Conceptos clave

---

Ya tienes OpenClaw instalado. Ahora hay que entender cómo funciona por dentro **antes de pedirle nada serio**, porque si no entiendes la base, vas a ir dando palos al aire.

## 💡 Conceptos clave que tienes que dominar

Antes de poner a tu agente a trabajar, asegúrate de entender estos tres conceptos. Si te quedan dudas, díselo al propio agente y pídele que te explique con tus palabras.

### Modelo (el cerebro)

Es el LLM que razona detrás del agente: Anthropic (Opus / Sonnet), Gemini, OpenAI, OpenRouter, MiniMax, Moonshot, o modelos locales vía Ollama. OpenClaw no piensa por sí solo: hereda la inteligencia, la calidad y los costos del modelo que le conectes. Cambiar de cerebro = cambiar las capacidades reales del agente.

### Memoria persistente

Es lo que diferencia a OpenClaw de un chatbot común. El agente guarda tu contexto en el tiempo: quién eres, cómo trabajas, decisiones pasadas, conversaciones previas, archivos relevantes. Sin alimentar bien la memoria, todo lo demás rinde al 10%. Por eso la *S* del Framework SOUL (Setup) es la más importante.

### Skills

Son las **habilidades** que le instalas al agente. Cada skill es un módulo que le agrega una capacidad concreta: leer correos, transcribir audio, controlar un navegador, hablar con una API.

Tres cosas que tienes que tener claras de los skills:

1. **Dónde** los consigues (CloudHub, repositorios públicos).
2. **Qué** hacen exactamente (lee la documentación antes de instalar).
3. **Cómo** se asignan a tu asistente.

<aside> ⚠️

Regla de oro: **no instales todo**. Cada skill puede ejecutar código y acceder a servicios externos. Instala solo lo que necesitas y revisa qué hace antes de activarlo.

</aside>

### CloudHub

Es el "App Store" de OpenClaw: el catálogo central donde encuentras skills listos para instalar (Trello, Slack, Whisper, Google, Notion, cientos más) sin tener que escribir código. La mayoría de las capacidades que vas a querer ya están ahí; aprende a navegarlo antes de salir a buscar skills sueltos por GitHub.

### Canales

Telegram, Slack, Discord, WhatsApp, panel web. El mismo agente con la misma memoria responde por el canal que prefieras: no son agentes distintos en cada lado, es **uno solo con varias puertas de entrada**. La *U* del Framework SOUL (Unificar) trata exactamente de esto.

### HeartBeats

Son el "latido" del agente: revisiones periódicas que hace de sí mismo. En cada heartbeat actualiza su estado, revisa notificaciones pendientes, consulta tareas y ejecuta lo que toque. Sin heartbeat, el agente solo trabaja cuando le hablas; con heartbeat, trabaja por su cuenta.

### CronJobs

Son tareas programadas para ejecutarse en momentos específicos: todos los lunes a las 9, el día 1 de cada mes, cada 6 horas. Son la forma de darle al agente una rutina fija (resumen matutino, auditoría semanal de archivos, reporte mensual, etc.).

### Gateway

Es el túnel por el que accedes al panel web de OpenClaw cuando vive en un VPS. Si lo dejas abierto a Internet, cualquiera puede entrar (Shodan indexa instancias expuestas todo el tiempo). La regla: exponerlo solo dentro de tu red privada — lo aseguramos más adelante con Tailscale + firewall.

📖 Documentación oficial de OpenClaw para profundizar: [docs.openclaw.ai](http://docs.openclaw.ai)
