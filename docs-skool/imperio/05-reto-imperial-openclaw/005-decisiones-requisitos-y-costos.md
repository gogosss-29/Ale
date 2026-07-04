# 🛠️ Decisiones, requisitos y costos

> Ruta: 🦞 Reto Imperial OpenClaw › 🛠️ Decisiones, requisitos y costos

---

Lo primero es instalar OpenClaw. Antes de tocar nada, vas a tomar dos decisiones: **dónde** lo instalas y **qué modelo de IA** lo va a alimentar.

- **Tiempo estimado:** 30-90 minutos
- **Nivel técnico:** Principiante / Intermedio
- **Costo aproximado mensual:** $10-50 USD (según el camino que elijas)

**Vas a necesitar:** una tarjeta para pagar el hosting (o el Mac Mini ya comprado), una clave API de OpenAI (para Codex) o de Anthropic, y paciencia para seguir las instrucciones al pie de la letra.

---

## Decisión 1: ¿Dónde lo instalas?

### Camino A — VPS con Hostinger *(recomendado)*

Es el camino que recomendamos para la mayoría de los Imperiales. Es rápido de levantar, escalable, y si algo se rompe lo puedes reinstalar sin perder hardware.

**Lo importante a tener en cuenta:**

- Plan recomendado: **KVM 2** en Hostinger.
- Sistema operativo: **Ubuntu 24.04 LTS** (siempre LTS).
- **Nunca** instales OpenClaw como `root`. Crea un usuario dedicado (`openclaw`) y trabaja desde ahí.
- Acepta conscientemente las advertencias de seguridad de OpenClaw durante el setup.

### Camino B — Mac Mini local *(solo si ya tienes el hardware)*

Si tienes un Mac Mini M4 (o superior) que puede correr 24/7 en tu casa, este camino te da control total y costos energéticos bajos. **Solo recomendado si ya tienes el hardware** y entiendes lo que implica tener un servidor en tu casa.

> ⚠️ **Ten en cuenta:** si vas por el camino del Mac Mini y lo expones a internet, sigue siendo igual de crítico aplicar las capas de seguridad de la lección **🛡️ Seguridad y Túnel Privado - Tailscale**. La cercanía física no te protege.

---

## Decisión 2: ¿Qué modelo de IA usar?

### Recomendación principal: Codex (suscripción ChatGPT Plus)

Si ya pagas ChatGPT Plus, Codex viene incluido y puedes usarlo con OpenClaw sin que el costo se dispare.

> 🚨 **Importante:** Anthropic ya **no permite usar Claude Code mediante OAuth** con herramientas de terceros como OpenClaw. Si estabas pensando en usar tu suscripción de Claude Pro / Max, ese camino está cerrado. Para Anthropic, hoy la única opción es API Key dedicada (con costo por uso).

### Camino alternativo: Ollama + modelos open source *(gratis)*

Si quieres correr OpenClaw sin pagar API y aprovechar modelos open source en local o en la nube, Ollama es el puente. Incluye comparativa de modelos (Nemotron, Qwen, Gemma, DeepSeek, MiniMax) y un setup híbrido: Nemotron como cerebro principal + Sonnet como fallback solo para tareas complejas.

### Si vas con API directa

- Crea una API Key **dedicada solo a OpenClaw**.
- Pon un presupuesto bajo al inicio ($5-10 USD para pruebas).
- Nunca uses la misma key para otros proyectos.

---

## 💸 Resumen de costos (USD aprox. / mes)

- **VPS Hostinger KVM 2:** ~$15-25 USD
- **Mac Mini M4 (electricidad en LATAM):** ~$2-5 USD
- **Codex (ChatGPT Plus):** $20 USD (ya incluido si lo pagas)
- **API directa (pago por uso):** $10-50 USD
- **Ollama + modelos open source:** $0 USD
- **API de Brave Search:** $0 USD (plan gratuito suele alcanzar)

**Total estimado:** $0-70 USD / mes

## ✅ Resultado esperado al cerrar esta lección

- VPS o Mac Mini funcionando.
- Usuario dedicado `openclaw` creado.
- OpenClaw instalado correctamente.
- Modelo de IA conectado (Codex, API directa u Ollama).
- Listo para conectarlo a Telegram en la siguiente lección.

> 🆘 **¿Te trabaste en algún paso?** Comparte tu duda en el [foro de la comunidad](https://www.skool.com/imperio?c=5940479213c14125b945f06fc7092bdc&s=newest&fl=) o búscala en [Community OS](https://os.imperioagentico.com/) — el RAG de la comunidad ya tiene historial de instalaciones reales de otros Imperiales.
