# Guía completa de sesiones en Claude Code

> Ruta: Claude Code › Guía completa de sesiones en Claude Code

---

5 métodos para retomar, continuar y compartir tus sesiones entre terminal, desktop y celular.

Te ha pasado que cierras la terminal después de 1 hora de debugging intenso y al abrir Claude Code de nuevo... tienes que volver a explicar TODO desde cero?

A mí me pasaba constantemente. Perdía contexto, perdía decisiones arquitectónicas, perdía el hilo de lo que estaba haciendo.

La buena noticia es que Claude Code tiene **5 métodos nativos** para que nunca más te pase. Y en este post te los voy a explicar todos con casos de uso prácticos y los comandos listos para copiar y pegar.

## 📊 Vista general: Los 5 métodos

Antes de profundizar, acá tienes la tabla comparativa para que veas cuál te conviene según tu situación:

![02-tabla-comparativa.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d27bb18b578e41bc9a7b1ed2231e50bbb63a7750094f4ded8905d687ea78a015.png)

**Pro tip importante:** Siempre usa `/rename mi-proyecto` al inicio de cada sesión. Tu yo del futuro te lo va a agradecer cuando tengas 50+ sesiones guardadas.

## 🌳 ¿Cuál método debo usar? — Árbol de decisión

Si no sabes cuál elegir, sigue este flujo:

![03-arbol-decision.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/191c0fb99ed446ec96b237b161a00cec9eac546bbda244bb9147bd7e9a715fd2.png)

La lógica es simple:

- ¿Necesitas otro dispositivo? → **Remote Control**
- ¿Es la sesión más reciente? → **--continue**
- ¿Es para scripts/automatización? → **--session-id**
- ¿Nada de lo anterior? → **--resume**
- ¿Quieres explorar caminos divergentes? → **Fork (SDK)**

## ⚡ Método 1: `claude --continue` (Cero fricción)

**Cuándo usarlo:** Acabas de cerrar la terminal y quieres seguir exactamente donde estabas.

### Comandos:

```
# Continuar última sesión del directorio actual
claude --continue

# Forma corta
claude -c

# Continuar + enviar prompt directo
claude -c "corre los tests otra vez"

# En modo no-interactivo (para scripts)
claude -c -p "checa errores de TypeScript"
```

### Casos de uso reales:

**🔌 Tu Mac/PC se durmió a media sesión** Estás debuggeando un webhook y tu Mac entra en sleep. Regresas, abres terminal:

```
cd ~/projects/mi-proyecto
claude -c
```

Claude ya tiene todo el contexto — archivos que leyó, comandos que corrió, el stack trace que estaba analizando.

**🍔 Te fuiste a comer y regresaste**

```
claude -c "¿dónde nos quedamos?"
```

**🔄 Workflow iterativo (TDD)** Estás en un loop de: corre tests → Claude analiza → arregla → repite. Si reiniciaste la terminal:

```
claude -c "corre los tests de nuevo y dime si ya pasan"
```

**Dato clave:** `--continue` siempre retoma la sesión más reciente **del directorio actual**. Si cambias de carpeta, toma la última sesión de esa otra carpeta.

---

## 🔍 Método 2: `claude --resume` (Picker interactivo)

**Cuándo usarlo:** Quieres volver a una sesión específica de hace días o semanas.

### Comandos:

```
# Picker interactivo (navega con flechas)
claude --resume

# Forma corta
claude -r

# Resumir por nombre
claude -r "crm-hvac"

# Resumir por ID específico
claude -r abc123-def456

# Resumir + enviar prompt
claude -r "crm-hvac" "revisa el último cambio"
```

### Casos de uso reales:

**📋 Retomar proyecto de cliente después de días** El lunes trabajaste en un CRM y el martes en un scraper de Instagram. Es miércoles y quieres volver al CRM:

```
claude --resume
# Aparece el picker → buscas "crm" → enter
```

**🧠 Recuperar una decisión arquitectónica** Hace una semana discutiste con Claude la estructura de base de datos. Necesitas recordar por qué elegiste cierto schema:

```
claude -r
# Buscas "schema" o "base de datos" en el picker con /
```

**🏷️ Sesiones con nombre (la mejor práctica)** Al inicio de cada sesión importante:

```
claude
> /rename cliente-mario-scraper
# ... trabajas toda la tarde ...

# 3 días después:
claude -r "cliente-mario-scraper"
```

**Tip:** Dentro del picker puedes escribir `/` para buscar por keyword en todas tus sesiones históricas.

## 📱 Método 3: `/remote-control` (Multi-dispositivo)

Esta es la feature más poderosa y la que menos gente conoce. **Te permite continuar tu sesión de Claude Code desde cualquier dispositivo — celular, tablet, otro browser — en tiempo real.**

![05-remote-control.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0201265a7ab845609bc6e46cba99189945cae6c2b86d4b869914cdd50678135c.png)

**Comandos:**

```
# Iniciar Remote Control desde una nueva sesión
claude --remote-control

# Con nombre personalizado (recomendado)
claude --remote-control --name "mi-proyecto"

# Desde DENTRO de una sesión ya activa
/remote-control

# Con nombre desde dentro
/remote-control --name "refactor-v2"
```

### ¿Cómo funciona?

1. Ejecutas el comando en tu terminal
2. Te genera una **URL** + **código QR**
3. Desde tu cel: escaneas el QR con la app de Claude, o abres `claude.ai/code` y buscas la sesión por nombre (aparece con ícono de computadora + punto verde 🟢)
4. **La conversación se sincroniza en tiempo real** entre todos los dispositivos

### Detalle CLAVE:

A diferencia de Claude Code en la web (que corre en la nube), **Remote Control corre en TU máquina**. Las interfaces web y móvil son solo una ventana hacia tu sesión local. Esto significa:

- ✅ Acceso a tu filesystem local
- ✅ Tus archivos, tu código, tu entorno
- ⚠️ Tu Mac necesita estar encendida y conectada
- ⚠️ Requiere Claude Code v2.1.51+ (`claude --version` para verificar)

### Casos de uso reales:

**🛋️ Del escritorio al sofá** Estás en tu MacBook codificando. Son las 10pm, quieres seguir pero desde el cel:

```
/remote-control --name "feature-auth"
# Escaneas QR con iPhone → sigues desde la cama
```

**☕ Code review en movimiento** Tu Mac está en casa corriendo. Desde un café revisas PRs:

```
claude --remote-control --name "pr-review"
# Desde el cel: abres claude.ai/code → sesión "pr-review"
```

Si la Mac se duerme o pierdes conexión, **se reconecta automáticamente** cuando vuelve online.

## 🔧 Método 4: `claude --session-id` (Automatización)

**Cuándo usarlo:** Necesitas IDs predecibles y determinísticos para scripts, CI/CD o flujos multi-agente.

### Comandos:

```
# ID fijo por proyecto
claude --session-id "mi-proyecto-v1"

# ID dinámico basado en la branch de Git
claude --session-id "feat-$(git branch --show-current)"

# ID por ticket (perfecto para integraciones)
claude --session-id "ticket-${TICKET_ID}" -p "analiza el bug reportado"

# ID fijo para agentes específicos
claude --session-id "agente-literal-renderly" "analiza con enfoque conservador"
claude --session-id "agente-creativo-renderly" "propón alternativas radicales"
```

### Casos de uso reales:

**🤖 Agentes multi-rol (estilo La Forja)** Si usas una metodología multi-agente, cada agente tiene su session-id fijo:

```
# Agente Literal
claude --session-id "forja-literal" "revisa este módulo sin cambios radicales"

# Agente Creativo
claude --session-id "forja-creativo" "propón soluciones disruptivas"

# Agente Disruptivo
claude --session-id "forja-disruptivo" "cuestiona toda la arquitectura"
```

## 🧪 Método 5: Fork de sesiones (Avanzado — vía SDK)

**Cuándo usarlo:** Quieres explorar 2+ caminos divergentes partiendo del mismo contexto, sin perder la conversación original. Como un `git branch` pero de conversaciones.

### Ejemplo con el SDK:

```
import { ClaudeCode } from '@anthropic-ai/claude-code';
const claude = new ClaudeCode();

// Sesión original — ya analizamos los requerimientos
const original = await claude.query({
  prompt: "Analiza los requerimientos del proyecto NÚCLEO"
});

// Fork A: Explorar Supabase self-hosted
const forkA = await claude.query({
  prompt: "Diseña la arquitectura con Supabase self-hosted en Coolify",
  fork: { session_id: original.session_id }
});

// Fork B: Explorar Supabase managed
const forkB = await claude.query({
  prompt: "Diseña la arquitectura con Supabase managed cloud",
  fork: { session_id: original.session_id }
});

// Ambos forks tienen TODO el contexto previo pero divergen en la solución
```

### Casos de uso:

- **Comparar arquitecturas** sin repetir todo el contexto
- **Multi-agente automatizado** — forkeas la sesión base en N ramas
- **A/B testing de soluciones** — mismo problema, diferentes approaches
- **Recuperar de un límite** — si se acaban los tokens, resumes con más budget

---

## 📋 Cheat Sheet: Todos los comandos

Guarda esta imagen para referencia rápida:

![04-cheatsheet-comandos.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c73e5396597e4a70aa07ace4e5af3ecdae8dcb022f66450ba2e2ba55ee5f375d.png)

**Comandos complementarios de gestión:**

```
# Renombrar la sesión actual (HAZLO SIEMPRE)
/rename nombre-descriptivo

# Exportar conversación a archivo
/export sesion-backup.md

# Compactar contexto (cuando se llena)
/compact

# Limpiar chat actual (empezar fresco)
/clear

# Ver historial de sesiones personalizado
/history
```

## 🗃️ ¿Dónde se guardan las sesiones?

Todo vive en `~/.claude/projects/` de tu máquina:

```
~/.claude/
├── projects/
│   ├── tu-proyecto/
│   │   ├── session-abc123.jsonl    ← transcript completo
│   │   ├── session-def456.jsonl
│   │   ├── sessions-index.json     ← índice con metadata
│   │   └── memory/
│   │       └── MEMORY.md           ← memoria persistente
│   └── otro-proyecto/
│       └── ...
```

**Datos importantes:**

- ✅ Cada sesión se guarda **automáticamente** — no necesitas hacer nada
- ✅ Las sesiones **no expiran** — puedes resumir una de hace meses
- ✅ El historial completo se restaura: mensajes, resultados de tools, archivos leídos, todo
- ✅ Sesiones del mismo repo Git se agrupan (incluyendo worktrees)
