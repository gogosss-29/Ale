# 🚀 Auth con Supabase y Deploy a Vercel

> Ruta: Vibe-Coding › 🚀 Auth con Supabase y Deploy a Vercel

**🎬 Vídeo (24.1 min):** https://youtu.be/hN6KA80wNW8

---

## Parte VIII. Auth con Supabase y Deploy a Vercel (cierre del curso)

Cerrar el MVP como “producto real”. En esta lección hacemos dos cosas que separan un prototipo de una app usable:

1. **Autenticación con Supabase** (signup, login y verificación por email).
2. **Deploy a Vercel** (build de producción, variables de entorno y verificación final).

## 1. Recap rápido del MVP antes del cierre

Al inicio del video confirmamos que el MVP ya funciona en local:

- Dashboard operativo.
- Diagnósticos y reportes generados.
- Cotizaciones, clientes y envío de correos.
- Flujo híbrido con n8n funcionando.

Luego detectamos el hueco obvio: **no hay sign-up/sign-in**, entonces cualquiera podría entrar. Eso no es aceptable si lo vas a usar con clientes o equipo.

## 2. Decisión clave. Supabase Auth vs BetterAuth

Aquí no nos complicamos por “lo popular”. Elegimos por encaje con el stack:

- Ya usamos Supabase.
- Supabase tiene Auth integrado.
- Soporta verificación por correo sin montar infraestructura extra.

Resultado: **Supabase Auth gana por simplicidad y velocidad para MVP**.

## 3. Qué se implementa en Auth (lo mínimo correcto)

En esta lección se integra:

- Pantalla de **Sign up**
- Pantalla de **Sign in**
- Flujo de **verificación por email** obligatorio antes de poder iniciar sesión
- Redirección correcta después de login
- Protección básica de rutas (si no hay sesión, no entras)

## 4. Configuración clave dentro de Supabase

Paso importante que mucha gente se salta:

En Supabase, dentro del proyecto:

- Authentication . Providers . Email
- Activar “**Confirm email**” (confirmación de correo después de registrarse)

También se menciona:

- Puedes personalizar templates de email después.
- Para el MVP no lo hacemos perfecto. Solo funcional.

## 5. Prueba real del signup y verificación

La prueba correcta es:

1. Registrarte con email + password
2. Ver que te llegue el correo
3. Confirmar el email
4. Volver al sitio y hacer login
5. Confirmar que ya te deja entrar al panel

Esto valida que el flujo no es “fake UI”. Es Auth real.

## 6. Deploy a Vercel. Qué importa de verdad

Aquí lo que importa no es el botón de deploy. Es el checklist mental:

- Código actualizado y empujado a GitHub
- Build correcto en producción
- Variables de entorno configuradas en Vercel
- Redeploy después de setear variables
- Confirmar que Auth funciona en producción, no solo en local

## 7. Truquito práctico. Variables de entorno

En local ya tienes `.env.local`. En producción no existe.

En Vercel:

- Settings . Environment Variables
- Importar variables (si lo haces manual, te equivocas más)
- Guardar y hacer **Redeploy**

Si no haces esto, la app “carga” pero no funciona. Especialmente Auth y Supabase.

## 8. MCP de Vercel. Realidad vs expectativa

Se intenta que Vercel deploy “solo” usando MCP y CLI.  
La realidad práctica del video:

- A veces pide login, tokens o device auth.
- Si te frustra, haces deploy manual conectando GitHub, es igual de válido para MVP.

La lección: **no te cases con el camino fancy**. Termina el deploy.

## 9. Verificación final en producción

Checklist de cierre en el dominio de Vercel:

- Login funciona
- Dashboard carga
- Diagnósticos funcionan
- Envío de correo (n8n + Gmail) funciona
- Todo sin errores visibles

Con eso ya puedes compartir el link, aunque sea con dominio temporal.

Al final debes tener:

- App con Auth real (signup, login, email verification).
- Deploy funcional en Vercel con variables de entorno correctas.
- MVP usable desde una URL pública.
- Flujo de n8n validado desde producción.

### Te dejo el repositorio de Github por si quieres clonarlo y testarlo, solo recuerda que tienes que cambiar tu variables de entorno.

[https://github.com/agenciainsigniaia-oss/Automation-Opportunity-Finder..git](https://github.com/agenciainsigniaia-oss/Automation-Opportunity-Finder..git)
