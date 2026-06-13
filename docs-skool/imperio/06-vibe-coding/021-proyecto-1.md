# 🏆  Proyecto 1

> Ruta: Vibe-Coding › 🏆  Proyecto 1

**🎬 Vídeo (? min):** https://youtu.be/d6mXu2tlevk

---

## Parte III. Primera win. Clon de Linktree en tiempo récord (repo listo para clonar)

En este módulo hacemos tu primera win real con Antigravity. La meta es simple. Pasar de idea a app pública en Vercel en menos de 30 minutos. Terminamos cerca de los 35. Sigue siendo una win.

Si quieres clonar la app ya terminada, aquí está el repositorio

```txt
https://github.com/agenciainsigniaia-oss/nova-bio-link.git

```

## Qué vas a construir

Un clon simple tipo Linktree para centralizar tus links y usarlo en tus redes:

- Foto y bio
- Botones a redes (LinkedIn, Instagram, Facebook, TikTok)
- CTA de “Recursos / Toolkit” y “Trabaja conmigo”
- Captura de email para leads (sin Supabase. MVP)
- Deploy público en Vercel

No usamos Supabase en este video porque no lo necesitas para un Linktree. Queremos velocidad.

## Tech stack del video

- Antigravity (orquestador)
- React + Vite + TypeScript
- Tailwind
- GitHub (para repo y versionado)
- Vercel (para deploy)
- n8n (para capturar emails por webhook)

Cuentas necesarias (todas pueden ser gratis):

- GitHub
- Vercel
- n8n (cloud o self-host)
- Antigravity

## Flujo del video (lo importante, sin relleno)

### 1) Prompt. Cero técnico

Le damos a Antigravity un prompt con:

- Estilo (neobrutalista)
- Marca ficticia (Alex Nova. Nova AI)
- Secciones (bio, links, CTA, footer)
- Objetivo (captar correos y centralizar redes)

Antigravity decide framework y estructura. Tú solo defines resultado.

### 2) Ver la app local sin complicarte

Cuando termina, corres:

- `npm run dev`  
y abres el [localhost](http://localhost).

Aquí es donde confirmas si el diseño ya está usable antes de moverle algo.

### 3) Truquito clave. “Ver lo que yo veo”

Le pides al agente que abra el navegador y vea tu app. Antigravity navega, hace scroll, prueba botones, rellena campos, toma screenshots. Esto acelera QA y cambios visuales.

Cambios que pedimos en el video:

- Efecto “flip” en la foto de perfil en escritorio
- En mobile, alternar imagen cada 2 segundos con animación
- Links reales para “descarga” y “trabaja conmigo”
- Actualizar URLs de redes

### 4) Captura de emails sin Supabase. Usando n8n

No hacemos base de datos. MVP.

Idea:

- El formulario manda el email a un **webhook de n8n**
- n8n recibe el payload
- Luego tú conectas lo que quieras. Gmail, Google Sheets, Airtable, CRM, newsletter, etc.

Workflow sugerido en n8n:

- Webhook trigger
- Validación mínima (email no vacío)
- Guardar o enviar a donde quieras
- Responder al front con confirmación

Nombre del escenario en el video:

- “Linktree lista de correos”

### 5) Buenas prácticas. GitHub como debes hacerlo

Cuando ya está funcionando:

- Crear repo
- Commit inicial
- Push
- README claro con: - cómo correr local
- qué hace la app
- dónde configurar el webhook de n8n
- qué variables se usan si aplica

Esto es parte del producto. No es opcional si lo vas a compartir o vender.

### 6) Deploy a Vercel desde Antigravity

Con el MCP de Vercel conectado, le pides:

- Crear proyecto
- Build
- Deploy
- Validación final en producción

Después pruebas:

- link público abre
- botones funcionan
- formulario dispara webhook
- n8n registra ejecución

## Qué aprendiste en esta win

- Cómo usar Antigravity para construir una app completa con un prompt
- Cómo hacer QA visual con navegador controlado por el agente
- Cómo resolver captación de leads sin backend pesado usando n8n
- Cómo cerrar el loop completo: repo + deploy + verificación

## Lo que viene después

En los siguientes videos ya entramos en modo serio:

- Supabase (tablas, relaciones, seguridad básica)
- Auth
- Integraciones con Gemini
- Variables de entorno en Vercel
- MVP listo para vender o usar en producción con mejores prácticas

##
