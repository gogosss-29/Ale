# 🤓 Conexión MCPs + Supabase

> Ruta: Vibe-Coding › 🤓 Conexión MCPs + Supabase

**🎬 Vídeo (36.0 min):** https://youtu.be/7ppKLr2mfBA

---

## Parte II. Supabase + MCP. Conexiones dinámicas en Antigravity y qué viene en el siguiente video

Antes de seguir construyendo, aquí hacemos una pausa estratégica para entender dos piezas que te van a ahorrar horas:

1. **Qué es Supabase y por qué lo usamos en este proyecto**
2. **Qué es MCP (Model Context Protocol) y por qué conectarlo a Antigravity cambia el juego**

Luego hacemos la parte práctica: conectar **GitHub, Supabase, Vercel y n8n** a Antigravity, cada uno con un método distinto. La idea es que entiendas que no hay una sola forma “correcta”. Hay varias, y tú eliges según el caso.

Al final, te explico qué haremos en el siguiente video.

## 1. Qué es Supabase (en simple y sin humo)

Supabase es una alternativa open-source a Firebase basada en **PostgreSQL**. Piénsalo como un backend completo en una caja:

- **Base de datos relacional (Postgres)**
- **Auth listo** (email, social login, teléfono, etc.)
- **Storage** (archivos, imágenes, PDFs)
- **APIs auto-generadas** (para leer/escribir datos sin montar servidor propio)
- Edge Functions si luego quieres lógica server-side

### Por qué lo usamos aquí

En este proyecto Supabase tiene dos roles claros:

1. **Guardar datos**: clientes, diagnósticos, cotizaciones, correos enviados
2. **Habilitar acciones**: auth y operaciones que requieren backend real

## 2. Cuándo sí y cuándo no usar Supabase

### Sí usarlo cuando:

- Necesitas guardar data de usuarios
- Quieres login real y sesiones
- Tienes relaciones (uno a muchos) como: - Un cliente . muchos diagnósticos
- Un diagnóstico . muchas cotizaciones
- Una cotización . muchos correos enviados
- Quieres lanzar rápido un MVP con backend incluido

### No usarlo cuando:

- Tu app es 100% estática (landing sin datos)
- Todo es almacenamiento local sin usuarios
- Tienes lógica backend ultra compleja y necesitas arquitectura propia

## 3. La parte importante. Relaciones en base de datos

Este proyecto usa relaciones reales, no “listas sueltas”:

- **Clientes** . Diagnósticos (1 a N)
- **Diagnósticos** . Cotizaciones (1 a N)
- **Cotizaciones** . Emails enviados (1 a N)

Esto es lo que hace que luego puedas:

- consultar historial
- filtrar
- auditar
- tener trazabilidad  
Sin volverte loco.

## 4. Qué es MCP y por qué te ahorra tiempo

MCP (Model Context Protocol) es un estándar abierto creado por Anthropic para conectar modelos de IA con herramientas y datos, tipo “USB universal”.

La diferencia práctica:

- Sin MCP: tú escribes integraciones a mano, APIs, headers, body, errores, etc.
- Con MCP: el modelo ya sabe cómo hablar con la herramienta, tú pides en lenguaje humano.

MCP reduce fricción. Punto.

## 5. Qué MCPs vamos a conectar en este curso

Para este proyecto conectamos:

- **GitHub MCP**: leer repos, archivos, buscar código, issues, PRs
- **Supabase MCP**: ver proyectos, manejar DB, tablas, auth, etc.
- **Vercel MCP**: deploy, logs, proyectos, env vars (con CLI y sesión)
- **n8n MCP**: listar workflows, ejecutar, buscar, etc.

La meta es que Antigravity pueda:

- leer tu PRD y código en GitHub
- crear y ajustar DB en Supabase
- ayudarte a deployar en Vercel
- crear o integrar flujos en n8n  
Todo desde el chat.

## 6. Conectando MCPs en Antigravity (lo práctico del video)

### A) GitHub (nativo, pero ojo con Docker)

Antigravity trae GitHub “preconfigurado”, pero a veces lo intenta correr via Docker.

Aquí mostramos la forma pro:

- Instalas GitHub MCP
- Generas un **Personal Access Token (classic)** en GitHub
- Si te lo pone como Docker, editas el JSON y lo conviertes a **npx**
- Guardas y refrescas

Buenas prácticas del token:

- Expira en pocos días si es demo
- Scope solo lo necesario (repo, workflows, hooks, etc.)
- Nada de permisos innecesarios

Luego haces el test obligado:

- “Listame mis repos” para confirmar que sí hay acceso real

### B) Supabase (nativo y directo)

Supabase sí es plug-and-play:

- Generas **Supabase Personal Access Token**
- Lo pegas en Antigravity
- Confirmas que aparece en Tools
- Test rápido: “Confirma que puedes ver mi proyecto”

### C) Vercel (no viene nativo. se conecta manual)

Aquí enseñamos otra ruta:

- Vercel MCP no aparece preconfigurado
- Buscamos documentación oficial del MCP (mcp server + npx)
- Pegamos config manual en el JSON
- Si ya estabas logueado, puede que no te pida token
- Si quieres forzar el onboarding para el tutorial: - `npx vercel login`
- te manda a `vercel.com/devices`
- autorizas y listo

Esto es importante porque mucha gente cree que “si no pidió token. no conectó”. No. Puede usar sesión local.

### D) n8n (no nativo. se configura por repo oficial)

Aquí hacemos algo que te sirve para cualquier herramienta:

- Buscamos el MCP oficial de n8n en GitHub
- Le pedimos al agente que lo clone, lo lea y nos devuelva el config exacto
- Rellenamos: - URL de n8n
- API key de n8n (creada en settings)
- Guardamos, refrescamos y probamos: - “Listame mis workflows”

Si te lista tus flows, ya está.

## 7. Regla de oro del módulo

Cada vez que conectes un MCP:

1. conéctalo
2. refresca
3. haz una prueba real (listar repos, listar workflows, ver proyecto)

Si no pruebas, vas a perder tiempo después y no vas a saber si el bug era tu app o la conexión.

## 8. Qué sigue. Próximo video (win rápida)

En el siguiente video hacemos una “win” rápida de 0 a 100:

- Construimos un clon de **Linktree**
- Mobile-first
- Deploy a Vercel
- Te quedas con una URL pública
- Lo puedes poner en Instagram, TikTok, donde sea
- Sin pagar Linktree

Después de esa win, regresamos al proceso completo para construir una app más grande con el flujo completo y deploy final.
