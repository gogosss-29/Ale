# 🌍 Cuentas e identidad para tus agentes

> Ruta: 🦞 Reto Imperial OpenClaw › 🌍 Cuentas e identidad para tus agentes

---

Hasta aquí, tus agentes funcionan **a tu nombre**: usan tu correo, tus tokens, tus cuentas. Eso está bien para empezar, pero a medida que escalas el Gran Consejo vas a querer que cada consejero tenga su **propia identidad**.

## Por qué darles cuentas propias

- **Trazabilidad.** Cuando algo sale mal, sabes exactamente qué consejero lo hizo.
- **Permisos granulares.** No le das al Embajador acceso al GitHub donde vive tu código.
- **Profesionalización.** El día que un consejero manda un correo, debe firmar como ese consejero, no como tú.
- **Seguridad.** Si una cuenta se compromete, no se compromete todo tu sistema.

---

## 3 opciones para el correo

Investiga cuál te queda mejor y elige una para empezar:

### Opción 1 — Cuenta de correo tradicional

Crear una cuenta normal (Gmail, Outlook, etc.) y darle usuario y contraseña al consejero. **Funciona, pero suele dar problemas:** los agentes no se mueven con fluidez por las interfaces de correo y hay riesgos de bloqueo por actividad sospechosa.

### Opción 2 — AgentMail *(recomendada)*

Servicio creado específicamente para uso por agentes IA, con buena integración con OpenClaw.

📖 [docs.agentmail.to/integrations/openclaw](http://docs.agentmail.to/integrations/openclaw)

### Opción 3 — Resend *(recomendada)*

Otra opción diseñada para automatización de email con OpenClaw, muy buena si tu consejero solo necesita **enviar** correos (newsletters, notificaciones, confirmaciones).

📖 [resend.com/blog/email-automation-for-openclaw-using-resend](http://resend.com/blog/email-automation-for-openclaw-using-resend)

> 💡 **Recomendación:** las dos últimas opciones están construidas pensando en uso por agentes IA. Invéstigalas primero antes de pelearte con un Gmail tradicional.

---

## Cuentas adicionales para crear apps

Si quieres que el Gran Consejo desarrolle apps reales (no solo automatice), créale cuentas en:

- **Supabase** → ya la tienes desde la lección del Gran Consejo, asegúrate de que cada consejero tenga sus propias keys.
- **GitHub** → repositorio donde vive el código que los consejeros generen.
- **Vercel** → para deploy y hosting de las apps.

Y dale acceso a sus **CLI o MCPs** para que puedan ejecutar código y publicarlo en producción sin pasar por ti.

## Resultado esperado al cerrar esta lección

- Al menos un consejero con cuenta de correo propia (AgentMail o Resend).
- Repositorio GitHub específico para el sistema (separado del de backups personales).
- Vercel conectado para deploys.
- Cada consejero firma como sí mismo cuando interactúa con el mundo.
