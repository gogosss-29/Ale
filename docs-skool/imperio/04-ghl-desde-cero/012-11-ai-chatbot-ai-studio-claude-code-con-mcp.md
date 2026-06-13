# 🧠 11. AI Chatbot, AI Studio & Claude Code con MCP

> Ruta: GHL desde Cero › 🧠 11. AI Chatbot, AI Studio & Claude Code con MCP

**🎬 Vídeo (26.1 min):** https://www.loom.com/share/d75d1855ace84d36859004d1845cbf6b

---

**Curso: Go High Level Desde Cero · Sección 11 de 12**

> *GHL ya es potente. Con AI, es imparable.*

Todo lo que hemos construido hasta ahora es potente pero **manual en su diseño** — tú definiste cada paso, cada mensaje, cada condición. En esta sección le agregamos **inteligencia artificial**. Cubrimos 3 cosas: primero, **clonar páginas** con AI Studio; segundo, un **chatbot** que atiende pacientes en la landing 24/7; y tercero — lo que nos diferencia de cualquier otro curso — cómo conectar **Claude Code directamente a GHL vía MCP** para consultar y operar tu negocio con lenguaje natural.

## **📚 Qué vas a aprender**

- Usar **AI Studio** para clonar una página web completa con un solo prompt
- Los **3 tipos de chatbot** de GHL (form-guided, prompt-based, flow-based) y cuándo usar cada uno
- Construir un chatbot **desde cero** para la clínica con personalidad, objetivo e información
- Integrar el **chat widget** en la landing page
- Configurar **Claude Code + MCP de GHL** para consultar y operar tu negocio con lenguaje natural
- Casos de uso reales: consultar oportunidades, mover leads, mandar WhatsApp, modificar workflows desde la terminal

## **🛠️ Paso a paso**

### **1. Clonar una página web con AI Studio**

En la Sección 6 vimos AI Studio construyendo una landing desde cero. Ahora veamos otra función potente: **clonar** una página existente.

1. Busca una clínica dental en tu ciudad (la que te guste cómo se ve).
2. Copia la URL de la landing.
3. En **AI Studio**, escribe un prompt simple:

> 📋 Prompt — Clonar landing
> 
> "Clona esta página, así como está, tal cual, tráete todos los videos, tráete toda la información. Necesito clonarlo. URL: https://[pagina-a-clonar].com"

AI Studio analiza la página, extrae estructura, textos, imágenes y te genera una versión editable dentro de GHL. Típicamente tarda **3-5 minutos**.

> 💡 **Usa clonación como punto de partida**, no como resultado final. Te ahorra 80% del setup, luego ajustas tono, colores e info de tu negocio.

### **2. Tour por Agent Studio**

Ir a **AI Agents → Agent Studio**. Aquí viven tres tipos de agentes:

TipoQué haceCuándo usarlo**Voice Agents**Reciben y realizan llamadas telefónicasAtención telefónica 24/7, agentes inbound/outbound**Conversational Agents**Responden chat, SMS, WhatsApp, Instagram, FacebookLead conversion, agendado de citas, FAQ**Reputation Manager**Responde reseñas de Google automáticamenteMantener reputación activa sin tiempo manual

### **Plantillas pre-hechas**

GHL tiene agentes pre-configurados que puedes instalar directo:

- **Dental Appointment** (agente conversacional para clínicas dentales)
- Reputation templates
- Lead qualification templates

Puedes instalarlos y después adaptarlos a español (vienen por defecto en inglés).

### **3. Crear un chatbot desde cero (prompt-based)**

Para aprender el flujo, mejor construir uno propio. **Agent Studio → Create Bot**.

#### **Elegir el tipo de bot**

GHL te pregunta entre 3 opciones:

TipoCuándo usarlo**Form-guided**Captura básica de leads / reservas sin lógica compleja**Prompt-based**Tú das instrucciones personalizadas — ideal para FAQ + agendado**Flow-based**Constructor visual tipo n8n — calificación avanzada con condiciones

Vamos con **Prompt-based** (es el que sustituye prácticamente un flujo de n8n en muchos casos).

#### **Configuración avanzada**

- **Nombre del bot:** `Bot de Sonrisa Perfecta`
- **Modo:** Piloto automático **desactivado** (queremos el modo en tiempo real, con posibilidad de que el humano tome el control)
- **Canales permitidos:** solo **Live Chat** (no WhatsApp, no Instagram, no Facebook — evitamos duplicación)
- **Nombre comercial:** `Clínica Sonrisa Perfecta`
- **Delay de respuesta:** 2 segundos
- **Bot inactivo cuando humano responde manualmente:** Sí ✅
- **Reactivar bot después de respuesta humana:** No ❌
- **Estilo de respuesta:** Equilibrado
- **Modelo LLM:** GPT-4.1 o GPT-4.1 mini (mini es más barato y suficiente para agendado)

> ⚠️ **Cuidado con los canales.** Si dejas todos activados (WhatsApp, IG, FB…), el bot intentará responder por todos lados y duplicarás respuestas con tus workflows existentes.

> 💡 **Costo:** aproximadamente **$0.007 USD por mensaje**. Con volumen moderado no supera los $3 USD/mes. GHL ofrece un plan de **$90 USD/mes con IA ilimitada** si tienes muchos chats.

### **4. Entrenar el bot — Personalidad, Objetivo e Información**

En la pestaña **Bot Training** hay 3 campos clave:

- **Personality** (cómo habla)
- **Goal** (qué debe lograr)
- **Additional Information** (qué sabe)

> 💡 **Best practice:** escribe los prompts en **inglés** y dentro del prompt mismo indica "responde siempre en español latinoamericano". Los modelos funcionan mejor así.

### **Usar Claude Code para generar el prompt**

En vez de escribirlo a mano, le pedimos a Claude Code que lo genere:

> 📋 Prompt — Pedirle a Claude Code el system prompt del bot
> 
> "Tengo este sistema de chatbot en GHL que tiene tres secciones: Personality, Goal, Additional Information. Basándote en esta documentación de prompting (pega o referencia la doc oficial de GHL) y en esta info de la clínica dental Sonrisa Perfecta (nombre, servicios, horarios, ubicación, promociones activas), genérame los 3 prompts optimizados."

Claude Code te devuelve 3 bloques listos para pegar.

#### **Pegar en GHL**

Copias y pegas cada bloque en su campo correspondiente. Revisa:

- **Promociones activas** — pueden cambiar, ajusta manualmente
- **Dirección y ciudad** — verifica que sea la correcta
- **Límite de caracteres** — cada campo tiene ~1,490 caracteres. Si te pasas, recorta.

### **Configurar acciones del bot**

En **Actions** activar:

- ✅ Reservar citas
- ✅ Cancelar citas
- ✅ Reprogramar citas
- ✅ Enviar resumen de conversaciones (por email a administradores)

⚠️ **Atención:** si activas "Reservar citas", GHL te pedirá seleccionar un calendario antes de poder guardar. Si no quieres que el bot agende directamente (porque tu calendario requiere pago, como el nuestro), desactiva esa acción y en el prompt pídele que **comparta el link del calendario** en lugar de agendar.

### **5. Crear el Chat Widget e integrarlo en la landing**

Ir a **Sites → Chat Widgets → + Create**.

#### **Configuración del widget**

- **Tipo:** Chat en tiempo real (no SMS, no Email, no Facebook)
- **Nombre:** `Limpieza Dental`
- **Estilo:** Floating (burbuja abajo a la derecha)
- **Mensaje visible:** "Hola, ¿cómo podemos ayudarte?"
- **Avatar:** usar el logo o imagen profesional
- **Posición:** bottom-right
- **Título en producción:** "¿Tienes alguna dudas? Por favor indícanos tu nombre y duda."
- **Habilitar horarios** ✅ (responde dentro del horario de atención)
- **Idioma:** Español

#### **Integrar en la landing**

Volver al funnel → **Settings del funnel → Chat Widget → seleccionar **`Limpieza Dental`.

### **Marcar el agente como principal**

En **Agent Studio → lista de agentes**: si tienes múltiples, dale clic a los tres puntos del que quieres como default y **Set as Primary**.

### **6. Test del chatbot en vivo**

Abrir la landing en **ventana de incógnito** (para no tener sesión activa).

Conversación de prueba:

> **Tú:** "Hola"
> 
> **Bot:** "¡Hola! Soy Sofía de Sonrisa Perfecta. ¿En qué puedo ayudarte?"
> 
> **Tú:** "¿Tienes la promo de limpieza dental? Quiero agendar."
> 
> **Bot:** "¡Sí! Limpieza dental a $499 el mes de abril. Tenemos disponibilidad hoy (23 abril) a las 12. ¿Te queda bien? También tengo el jueves 24 a las 2."

Revisa la conversación desde el lado del admin en **Conversations** y en **AI Studio → Conversation AI**.

### **7. 🔥 Claude Code + MCP — El diferenciador**

Aquí está lo que nos separa de cualquier otro curso de GHL.

**MCP (Model Context Protocol)** es un protocolo que permite que Claude se conecte directamente a herramientas externas. En este caso, le conectamos **Go High Level**. Significa que puedes **hablar con tu CRM** en lenguaje natural desde la terminal.

### **Setup — Datos que necesitas**

- **Location ID** de tu subcuenta
- **Token** de integración privada

#### **Obtener Location ID**

**Settings → Company → Business Profile** → copiar el valor de **Location ID**.

#### **Generar Token de integración privada**

**Settings → Private Integrations → + New Integration**

- **Nombre:** `Claude Code`
- **Scopes:** seleccionar **todos** (hay un warning con los de escritura de usuarios — aceptar)

Copiar el token generado y guardarlo temporalmente.

### **Configurar el MCP en Claude Code**

Abrir Claude Code en tu terminal. Pedirle que genere el archivo de configuración:

> 📋 Prompt — Configurar MCP de GHL en Claude Code
> 
> "Necesito que nos conectemos a Go High Level vía MCP. Aquí está la documentación oficial del MCP de GHL: [pegar doc oficial]. Hay que hacer la configuración que necesites. Trae el archivo `.mcp.json` y yo agrego los valores reales ahí."

⚠️ **Detalle importante:** la doc oficial de GHL muestra una configuración que está **incompleta**. Después de varias pruebas, la configuración correcta es:

> 📋 Plantilla — Configuración MCP de GHL (corregida)
> 
> ```json
> {
>   "mcpServers": {
>     "ghl-mcp": {
>       "type": "HTTP",
>       "url": "https://services.leadconnectorhq.com/mcp/",
>       "headers": {
>         "locationId": "TU_LOCATION_ID_AQUI",
>         "Authorization": "Bearer TU_TOKEN_AQUI"
>       }
>     }
>   }
> }
> ```

Diferencias vs. la doc oficial:

- `type: "HTTP"` — la doc no lo incluye, pero es obligatorio
- **Name: **`ghl-mcp` — sin prefijo del proyecto
- **URL correcta** — verificar que termine en `/mcp/`

> 💡 **Tip de seguridad:** nunca pongas el token directamente en el chat. Pídele a Claude Code que genere el archivo y tú rellenas los valores reales en disco. Así evitas que los secrets queden en el historial.

### **Activar la conexión**

Después de guardar el `.mcp.json`, **cerrar la conversación y abrir una nueva** (cada vez que modificas la config del MCP hay que reiniciar la sesión para que se cargue).

### **8. Casos de uso reales con Claude Code + MCP**

Una vez conectado, puedes hacer cosas como estas en lenguaje natural:

#### **Consultar información**

> **Tú:** "¿Cuál fue el último mensaje de Carlos Domínguez y a través de qué canal?"
> 
> **Claude:** *consulta contacto → conversaciones → responde con el último mensaje enviado, recibido, fecha y canal*

#### **Mover oportunidades**

> **Tú:** "Mueve a María Becerra a oportunidad ganada, hasta el final del pipeline."
> 
> **Claude:** *llama a la API → confirma el cambio*

#### **Disparar workflows manualmente**

> **Tú:** "Agrega a María Becerra de manera manual al workflow de rescate de no-show."
> 
> **Claude:** *añade al workflow → muestra los nodos que disparará*

#### **Enviar WhatsApp real**

> **Tú:** "Manda un WhatsApp real de prueba a Carlos Domínguez con la plantilla de confirmación."
> 
> **Claude:** *envía el mensaje usando la plantilla aprobada*

#### **Consultar métricas**

> **Tú:** "¿Cuánto tengo ahora como ganancia potencial en mi pipeline?"
> 
> **Claude:** *suma el valor de todas las oportunidades abiertas y responde*

### **9. Tip práctico — Guardar datos de la cuenta en CLAUDE.md**

Para no tener que repetir el Location ID y el contexto en cada sesión, guárdalo en el `CLAUDE.md` del proyecto:

```markdown
# GHL — Clínica Sonrisa Perfecta

- Location ID: TU_LOCATION_ID
- Pipeline principal: Nuevos Pacientes
- Calendario activo: Limpieza Dental ($499)
- Workflows activos: 6 (ver lista en memory/)
```

Así Claude Code tiene el contexto automáticamente en cada sesión nueva.

## **📎 Recursos**

### **📋 Plantilla — Personality del bot**

```
You are Sofia, the virtual assistant at Clínica Dental Sonrisa Perfecta (Cancún, MX).

Tone: warm, professional, concise. Always respond in Spanish (Latin American, neutral).

Style:
- Max 2-3 sentences per response.
- Use the patient's first name when known.
- Emojis: moderate use (🦷, 😊, 📅). Never excessive.
- Never make medical diagnoses. If asked, always redirect to an in-person consultation.
```

### **📋 Plantilla — Goal del bot**

```
Primary goal: help patients schedule appointments and answer FAQ.

Priorities (in order):
1. If the patient wants to book: share the calendar link for "Limpieza Dental $499" (since it requires online payment).
2. Answer FAQ using Additional Information.
3. If the patient has an emergency: escalate to human operator immediately.
4. If the patient asks about a specific treatment not listed: redirect to a phone call.

Never:
- Never promise discounts not listed.
- Never make medical diagnoses.
- Never invent prices.
```

### **📋 Plantilla — Additional Information del bot**

```
Clínica Dental Sonrisa Perfecta
Dirección: Av. Kukulkán #123, Cancún, México
Horario: Lun-Vie 9:00-19:00, Sáb 9:00-14:00, Dom cerrado
Teléfono: (998) 123-4567

Servicios y precios:
- Limpieza dental: $499 (promoción abril, regular $999)
- Ortodoncia: consulta gratis, tratamiento desde $15,000
- Blanqueamiento: $3,500
- Revisión general: $500
- Extracción muelas del juicio: desde $2,500

Métodos de pago: Visa, MasterCard, Amex, Mercado Pago.
Promoción activa: CUMPLE10 (10% descuento cumpleaños), VUELVE15 (15% rescate).

Para agendar limpieza: comparte este link (requiere pago online):
https://landing.clinicasonrisaperfecta.site

```

### **📋 Plantilla — **`.mcp.json` completo

```json
{
  "mcpServers": {
    "ghl-mcp": {
      "type": "HTTP",
      "url": "https://services.leadconnectorhq.com/mcp/",
      "headers": {
        "locationId": "TU_LOCATION_ID",
        "Authorization": "Bearer TU_TOKEN_INTEGRATION"
      }
    }
  }
}
```

### **🛠️ 36 herramientas disponibles vía MCP de GHL**

Entre las más útiles:

- `list_contacts`, `search_contacts`, `create_contact`, `update_contact`
- `list_opportunities`, `update_opportunity`
- `list_conversations`, `search_conversations`, `read_messages`, `send_message`
- `list_workflows`, `add_contact_to_workflow`, `remove_contact_from_workflow`
- `list_appointments`, `create_appointment`, `cancel_appointment`
- `list_calendars`, `list_pipelines`

### **💰 Pricing del AI en GHL**

ServicioCostoMensaje individual del bot~$0.007 USDPlan ilimitado$90 USD/mesClaude Code + MCPCosto de Claude (API Anthropic, normal)

## **⚠️ Troubleshooting común**

- **El chat widget no aparece en la landing:** verifica que seleccionaste el widget correcto en Settings del funnel y que le diste **Save + Publish**.
- **El bot intenta agendar pero no tiene calendario asignado:** desactiva la acción "Book Appointment" y en el prompt dile que comparta el link del calendario en su lugar.
- **Claude Code dice "contacto no encontrado" pero sí existe:** el bot quizá guardó el contacto con otro apellido. Pregúntale a Claude: "¿qué contactos hay con ese primer nombre?" y confirma el nombre correcto.
- **MCP no se conecta:** cierra y reabre la sesión de Claude Code. La config del MCP solo se carga al inicio. Verifica que agregaste `"type": "HTTP"` (el error más común).
- **Las plantillas de WhatsApp no aparecen en el bot:** todavía no fueron aprobadas por Meta. Espera 24-72h y reintenta.

## **✅ Checklist antes de avanzar a la Sección 12**

- [ ] Probaste clonar una página web con AI Studio
- [ ] Chatbot conversacional creado (prompt-based) con Personality / Goal / Information
- [ ] Chat widget integrado y probado en la landing en modo incógnito
- [ ] Private Integration de GHL creada con todos los scopes
- [ ] Archivo `.mcp.json` configurado con `type: HTTP` + Location ID + Token
- [ ] Probaste al menos 3 consultas con Claude Code + MCP (consultar, mover, enviar)
- [ ] Location ID y contexto guardado en `CLAUDE.md` del proyecto

## **➡️ Siguiente sección**

**Sección 12 — El Después: Dashboard, Entrega & Replicación.** Última sección del curso. Configuramos el dashboard con las métricas que importan, hacemos el recorrido completo del **antes vs. después**, y cerramos con cómo **replicar todo esto en cualquier nicho** (bienes raíces, gym, abogados, salón de belleza) en una fracción del tiempo usando **Snapshots**.
