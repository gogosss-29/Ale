# 8️⃣ Integración n8n & Github

> Ruta: Vibe-Coding › 8️⃣ Integración n8n & Github

**🎬 Vídeo (36.3 min):** https://youtu.be/fW9mSRhQLhA

---

## Parte VII. Integración híbrida con n8n, feature nueva de cotizaciones y hábitos pro con GitHub

En esta lección le damos un giro al MVP. Ya no es solo “frontend bonito con Supabase”. Ahora lo convertimos en un **frontend limpio** que puede disparar procesos reales en **n8n**.

La idea es simple:

- Si tu comunidad vive en n8n y quiere mantener lógica en n8n, perfecto.
- Pero igual quieres una interfaz moderna, rápida y presentable para clientes.
- Entonces hacemos un modelo híbrido: **UI en Antigravity. Automatización en n8n**.

## 1. Concepto clave. “Frontend pro” + “backend en n8n”

Aquí defines dos caminos válidos:

- Todo en n8n. Backend, lógica, storage, todo.
- O híbrido. UI y control en el front, automatización pesada en n8n.

Este video se enfoca en el híbrido porque es el más práctico para:

- agencias,
- freelancers,
- y equipos que ya dominan n8n.

## 2. Nueva feature. Página de cotizaciones con “email composer”

En lugar de seguir agregando pantallas random, aquí hacemos una feature de negocio real:

### Qué agregamos:

- Un nuevo menú: **Cotizaciones** (vista lista).
- Al seleccionar una cotización: - Panel izquierdo: composer del correo.
- Panel derecho: historial de correos enviados y estado.

### Lo importante:

- Botón para generar el email con IA (sin escribir desde cero).
- Selección del cliente. Que autopopule su email.
- Inserción dinámica del link único de la cotización.
- Botón para enviar payload a n8n.
- UI de confirmación: fecha de envío + check verde cuando fue exitoso.

Esto convierte el MVP en algo vendible. No es demo. Es herramienta.

## 3. Diseño correcto del flujo n8n

Aquí está el “pattern” que te tienes que aprender:

1. **Webhook Trigger** recibe payload desde la app.
2. Procesas lo necesario (en este video terminamos simplificando).
3. **Gmail node** envía el correo.
4. **Webhook Response** devuelve confirmación al frontend.

### Twist importante del video

Decisión inteligente para simplificar el MVP:

- Ya estamos generando subject y body en el frontend con IA.
- Entonces el payload a n8n se reduce a: - `to_email`
- `subject`
- `body`
- `client_id` o `client_name`
- `quote_id` y `share_link`

n8n solo ejecuta envío y respuesta. Mucho más estable.

## 4. MCP de n8n. Qué sí y qué no debes esperar

Tema clave para expectativas:

- El MCP puede ayudarte a buscar, ejecutar, inspeccionar, y guiarte.
- Pero dependiendo de cómo esté implementado el MCP server, puede que no soporte “crear workflows completos” de forma directa.

Lección práctica:

- No te cases con “IA lo hace todo”.
- Usa IA para estructura, JSON, nodos, mapeos, y checklist.
- Y si no puede crear el workflow, lo montas tú en 3 minutos con la guía.

## 5. API Key correcta de n8n

Aquí está el truquito que te ahorra horas:

Si el MCP no conecta o te da “no autorizado”, normalmente no es “el URL”.  
Es la key.

Ruta correcta:

- n8n . Personal settings . API . Create API key

Luego la pones en tu `.env.local` para que Antigravity pueda usarla.

## 6. Buenas prácticas para payloads entre UI y n8n

Reglas rápidas:

- Payload pequeño. Solo lo que n8n necesita.
- Campos claros y predecibles. Nada “free text” si no es el body.
- Siempre devolver un response JSON al frontend con: - `success: true/false`
- `message`
- `sent_at` (timestamp)
- `email_id` o tracking id si existe

El frontend NO debe marcar “enviado” hasta que llegue `success: true`.

## 7. Feature obligatoria cuando ya envías correos. Gestión de clientes

En el video aparece un punto de producto real:

Si ya vas a enviar correos:

- necesitas ver clientes,
- y editar email.

Entonces agregamos:

- Vista “Clientes”
- Edición del cliente
- Campo de email
- Guardar cambios

Esto no es “nice to have”. Es parte del flujo.

## 8. GitHub. Tu hábito más importante en todo el curso

Aquí no hay debate:

Si no haces commits frecuentes, tarde o temprano te vas a arrepentir.

Buenas prácticas del video:

- Commit después de cada cambio grande.
- Mensaje de commit describiendo qué cambió.
- Update de documentación cuando agregas features importantes.
- Si el agente va a hacer cambios grandes, que te pregunte si quieres commit.

## 9. README actualizado. El MVP debe ser “instalable”

Un MVP real no es solo código. Es “alguien lo puede correr”.

README mínimo obligatorio:

- Qué es la app.
- Qué hace el MVP.
- Tech stack.
- Cómo correr en local.
- Variables de entorno necesarias.
- Cómo conectar n8n (webhook + API key).
- Qué parte hace UI y qué parte hace n8n.

Esto también te ayuda si lo compartes en Skool para que la gente lo clone y lo pruebe.

Al final debes tener:

- Página de cotizaciones con composer e historial.
- Payload listo para enviar a n8n.
- Workflow en n8n con webhook + Gmail + response.
- UI que marca “enviado” solo con respuesta exitosa.
- Vista de clientes para editar email.
- Commits hechos correctamente.
- README actualizado para correr el MVP.
