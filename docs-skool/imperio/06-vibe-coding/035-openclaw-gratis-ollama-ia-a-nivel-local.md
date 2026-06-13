# OpenClaw GRATIS + Ollama (IA a nivel local)

> Ruta: Vibe-Coding › OpenClaw GRATIS + Ollama (IA a nivel local)

**🎬 Vídeo (25.6 min):** https://www.youtube.com/watch?v=k0RmZG87XTU

---

> **PD: Esto también funciona para Claude Code.**   
>   
> Es decir cuando llegas al límite, puedes seguir coding con modelos locales + ollama. tiene una integración super sencilla que muestro al final del video.

Anthropic cortó el acceso a suscripciones para herramientas de terceros como OpenClaw. Si estabas corriendo tu agente con Claude Pro o Max, eso ya no existe.

Así que me puse a probar alternativas usando **Ollama** — una herramienta que te permite correr modelos open source tanto en local como en la nube, y conectarlos directo a OpenClaw o Claude Code. Probé Nemotron, Qwen, Gemma 4, DeepSeek, MiniMax y más.

En el video te muestro qué encontré, cuáles modelos están funcionando mejor hoy para tareas agénticas (usando [Pinch Bench](https://pinchbench.com) como referencia), y el setup híbrido que uso: Nemotron como cerebro principal completamente gratis, con Sonnet como fallback para el 10% de tareas más complejas.

También te dejo el prompt que corro semanalmente para auditar y limpiar mi OpenClaw con Nemotron — sin gastar un peso:

```
Quiero hacerte una auditoría completa de tus archivos. Agenda 10 sesiones aisladas.
Cada sesión audita un archivo diferente de mi workspace:
17:50 → SOUL.md
17:55 → IDENTITY.md
18:00 → USER.md
18:05 → AGENTS.md
18:10 → TOOLS.md
18:15 → HEARTBEAT.md
18:20 → MEMORY.md
18:25 → Notas diarias (memory/*.md)
18:30 → Skills instalados
18:35 → Síntesis completa con nota del sistema, problemas críticos y mejoras prioritarias
Cada sesión debe: leer el archivo, detectar qué está desactualizado/roto/mejorable.
La sesión 10 manda el reporte ejecutivo completo.
Proponme el plan, lo apruebo y lo agendamos.
```

**Links útiles:**

- [Ollama](https://ollama.com) — para correr modelos open source
- [Pinch Bench](https://pinchbench.com) — benchmark agéntico para comparar modelos
