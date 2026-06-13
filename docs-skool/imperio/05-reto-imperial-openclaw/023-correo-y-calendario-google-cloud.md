# 📧 Correo y calendario (Google Cloud)

> Ruta: 🦞 Reto Imperial OpenClaw › 📧 Correo y calendario (Google Cloud)

---

Tus consejeros ya tienen identidad. Ahora vamos a **abrirles las ventanas al mundo**: empezamos por correo y calendario, con cuidado, capa por capa.

Para que un consejero (típicamente el Canciller) pueda mirar tu correo y tu agenda y decirte "tienes 4 cosas urgentes hoy", necesita acceso autorizado.

## Cómo hacerlo

Crea un proyecto en **Google Cloud** y otorga al consejero los permisos justos sobre tu cuenta de correo y calendario:

### ✅ Permisos recomendados al inicio

- Leer mensajes de correo.
- Ver eventos del calendario.

### ❌ Permisos que *no* deberías dar al inicio

- Escribir nuevos correos.
- Modificar o crear eventos.
- Borrar correos o eventos.

> 🤖 Si no sabes cómo configurar el proyecto de Google Cloud, **pregúntale a tu propio OpenClaw**: hoy ya conoce el procedimiento y te guía paso a paso. Esto es exactamente para lo que tener un agente con contexto sirve.

## Cuando ya viste cómo se comporta

Después de unas semanas con permisos de solo lectura, puedes evaluar si vale la pena darle escritura limitada (responder borradores que tú revisas, crear eventos en un calendario secundario, etc.). **Nunca le des escritura sobre tu calendario principal sin doble confirmación.**

## Resultado esperado al cerrar esta lección

- Proyecto de Google Cloud configurado con permisos mínimos.
- Canciller con acceso de lectura a correo y calendario.
- Al menos un caso real probado: pedirle al Canciller un resumen de pendientes del día y validar que lo entrega bien.
