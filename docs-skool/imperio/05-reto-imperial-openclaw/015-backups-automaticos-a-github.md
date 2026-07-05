# 💾 Backups automáticos a GitHub

> Ruta: 🦞 Reto Imperial OpenClaw › 💾 Backups automáticos a GitHub

---

Tu agente vive en archivos. `SOUL.md`, `MEMORY.md`, `USER.md`, `AGENTS.md`, configuraciones, skills personalizados, notas en `memory/`... Todo lo que tardaste semanas en armar es texto que vive en el VPS o en tu Mac Mini. Si se cae el servidor, si borras algo por accidente, o si una skill mal configurada sobrescribe un archivo clave, sin un backup pierdes todo.

La VPN privada y el firewall (que ya configuraste) protegen al agente de **accesos indebidos desde afuera**. Los backups protegen al agente de **la pérdida de datos desde adentro**: errores propios, fallos del proveedor, comandos mal ejecutados, corrupciones de disco. Son dos capas distintas y las dos son obligatorias.

## Por qué versionar en GitHub (y no solo copiar archivos)

Podrías hacer un `cp` diario a otra carpeta y listo. Pero versionar con Git te da algo que una copia plana no:

- **Historial completo:** puedes volver a la versión de hace 3 semanas exactamente.
- **Diff entre versiones:** ves qué cambió, cuándo, y por qué la memoria del agente empezó a fallar.
- **Almacenamiento gratuito:** GitHub te da repos privados ilimitados.
- **Recuperación remota:** si pierdes el VPS entero, restauras desde cualquier máquina.

---

## Pasos para configurarlo

1. **Crea un repositorio privado en GitHub** dedicado a tu OpenClaw (ej. `mi-openclaw-backup`). **Privado**, no público — aunque tengas `.gitignore` bien armado, los archivos de configuración suelen tener pistas sobre tu setup que no quieres exponer.
2. **Genera un Personal Access Token** con permisos **solo** para ese repositorio. No uses un token con acceso a toda tu cuenta de GitHub: si se filtra, el daño es enorme. Token granular, scope mínimo.
3. **Pásale al agente el repo y el token**, y dile que configure un CronJob diario que: - Haga `git add` de los archivos clave: `SOUL.md`, `MEMORY.md`, `USER.md`, `AGENTS.md`, `TOOLS.md`, `HEARTBEAT.md`, configuraciones del agente, skills personalizados, y todo lo que viva en `memory/`.
- Excluya credenciales y API Keys vía `.gitignore` (mínimo: `.env`, `*.key`, `secrets/`, cualquier archivo con tokens).
- Haga commit con timestamp en el mensaje (ej. `backup 2026-05-04 03:00`) y push automático.
4. **Verifica al día siguiente** que aparece un commit nuevo en el repo. Si no apareció, el CronJob no corrió — debugea ahí mismo, no esperes a la emergencia.

> 🔒 **Regla de oro:** nunca subas API Keys, tokens ni contraseñas al repositorio. Antes del primer commit, pídele al agente que te muestre exactamente qué archivos va a versionar y revísalos uno por uno. Si ves algo que no debería estar, agrégalo a `.gitignore` antes de seguir.

## Verifica que el backup realmente funciona

Un backup que nunca probaste no es un backup, es una ilusión. Una vez al mes:

- Clona el repo en otra máquina (tu computadora local sirve).
- Confirma que los archivos clave están ahí y son recientes.
- Idealmente, levanta una instancia de prueba con esos archivos para confirmar que el agente arranca con ese contexto.

Si no haces este chequeo periódico, vas a descubrir que tu backup estaba roto justo el día que más lo necesitas.

## Resultado esperado al cerrar esta lección

- Repositorio privado en GitHub creado y dedicado al OpenClaw.
- Personal Access Token con scope mínimo generado.
- CronJob diario activo, con timestamp en cada commit.
- `.gitignore` revisado, sin credenciales filtradas.
- Verificación manual hecha al día siguiente del primer commit.
- Recordatorio mensual programado para validar que el backup sigue funcionando.
