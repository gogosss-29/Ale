# Instala Claude Code (automatiza en n8n)

> Ruta: Automatizaciones n8n › Instala Claude Code (automatiza en n8n)

**🎬 Vídeo (18.4 min):** https://www.youtube.com/watch?v=Ivn4rX2wfxk

---

**¿40 minutos armando un workflow? Eso era antes.**

Pasé 2 años dominando n8n, nodo por nodo, workflow por workflow. Hasta que llegó Claude Code y cambió todo el juego.

En este video te muestro cómo crear workflows complejos de n8n en minutos, usando un agente de IA que entiende lo que quieres hacer y lo implementa directamente en tu instancia de n8n.

---

## 🎯 Lo que vas a aprender

✅ **Setup completo desde cero** - VS Code + Claude Code + MCP servers  
✅ **Crear tu agente personalizado "Claudio"** - Tu asistente de n8n 24/7  
✅ **Conectar Claude Code a tu instancia de n8n** - API keys y configuración  
✅ **Demo en vivo** - Workflow de newsletter con IA que se ejecuta solo  
✅ **Modificar workflows con lenguaje natural** - Sin tocar un solo nodo

---

## ⏱️ Timestamps del video

- **0:00** - Intro: 40 minutos vs 5 minutos
- **2:35** - ¿Qué son los MCP y cómo funcionan?
- **4:12** - Setup completo: VS Code + Claude Code + n8n
- **10:46** - Conectar tu instancia de n8n
- **12:48** - Demo en vivo: crear workflow con IA

---

## 🔧 Recursos necesarios

### Herramientas principales:

- [Claude Code](https://claude.com/claude-code) - Necesitas plan Pro o Max
- [n8n](https://n8n.io) - Tu plataforma de automatización
- [Visual Studio Code](https://code.visualstudio.com) - Editor gratuito

### Repositorios de superpoderes:

- [n8n MCP](https://github.com/lvisb/n8n-mcp) - Conexión a n8n
- [n8n Skills](https://github.com/lvisb/n8n-skills) - Buenas prácticas y patrones

---

## ✅ Checklist: Tu primer agente de n8n

Sigue estos pasos después de ver el video:

### 1. Preparación (5 min)

- Descargar e instalar Visual Studio Code
- Verificar que tienes plan Pro o Max de Claude
- Tener tu instancia de n8n lista

### 2. Instalación (10 min)

- Instalar extensión de Claude Code en VS Code
- Crear carpeta para tu agente (ej: "n8n-workflow-builder")
- Configurar permisos en Settings (allow dangerously skip permissions)

### 3. Crear tu agente "Claudio" (15 min)

- Abrir Claude Code en VS Code
- Darle instrucciones de quién es y qué hace
- Instalar repositorio n8n MCP desde GitHub
- Instalar repositorio n8n Skills desde GitHub
- Verificar que creó el archivo [claude.md](http://claude.md)

### 4. Conectar a n8n (5 min)

- Ir a tu instancia de n8n → Settings → API
- Crear nueva API Key (copia y guarda)
- Copiar tu n8n URL desde "Connection Details"
- Pegar ambas credenciales en Claude Code
- Confirmar conexión exitosa

### 5. Primera prueba (10 min)

- Pedirle a Claude que liste tus workflows existentes
- Crear un workflow simple de prueba
- Modificar algo con lenguaje natural
- Verificar que los cambios aparecen en n8n

**Total: ~45 minutos para tener tu agente funcionando para siempre** ⚡

---

## 💡 Ideas de workflows para probar

Una vez que tengas tu agente configurado, prueba con estos:

1. **Newsletter automatizado** (como en el video) - Investiga noticias semanalmente
- Genera resumen con IA
- Envía por email
2. **Monitor de competencia** - Scrapea sitios web
- Detecta cambios de precio
- Notifica por Slack/Telegram
3. **Content pipeline** - Genera ideas de contenido
- Crea drafts con IA
- Publica en múltiples plataformas
4. **CRM automation** - Captura leads desde formularios
- Enriquece datos con Apollo/Hunter
- Crea páginas en Notion automáticamente

---

## 🚀 Próximos pasos

**Si lograste configurarlo:**

- Comparte tu primer workflow en los comentarios 👇
- ¿Qué automatización creaste?
- ¿Cuánto tiempo te ahorró vs hacerlo manual?

**Si te trabaste en algún paso:**

- Publica tu pregunta aquí en la comunidad
- Incluye screenshots del error
- La comunidad te ayuda (y yo también)

**Próximo video de la serie:** Cómo combinar n8n visual con Claude Code para crear workflows híbridos aún más potentes. Si quieres que lo haga, déjamelo saber en los comentarios del video.

---

## ❓ FAQ rápido

**P: ¿Necesito saber programar?** R: No. Claude Code programa por ti. Solo necesitas describir lo que quieres.

**P: ¿Funciona con n8n cloud o solo self-hosted?** R: Funciona con ambos, solo necesitas la API key.

**P: ¿Cuánto cuesta Claude Code?** R: Viene incluido en los planes Pro ($20/mes) y Max ($200/mes) de Claude.

**P: ¿Puedo usar esto con Make o Zapier?** R: Por ahora solo hay MCP para n8n. Make y Zapier no tienen soporte oficial.

**P: ¿Es seguro darle acceso a mi n8n?** R: Sí, tú controlas los permisos de la API key y puedes revocarla cuando quieras.
