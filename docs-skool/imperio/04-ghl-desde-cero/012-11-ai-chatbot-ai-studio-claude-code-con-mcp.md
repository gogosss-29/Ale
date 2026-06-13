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

## 🎙️ Transcripción

Perfecto, ya casi llegamos al final del curso. Todo lo que hemos construido hasta ahora es potente, pero manual en su diseño. Tú definiste cada paso, cada mensaje, cada condición, así que en esa sección agregaremos inteligencia artificial. Vamos a cubrir tres cosas. Primero, las herramientas nativas de AI que trae por defecto. Segundo, un chatbot que atiende a pacientes en la land in page 24 a 7 y tercero, que es lo que nos diferencia de cualquier otro curso, que es como conectar cloud code directamente a ailever para consultar tu negocio con lenguaje natural y pedirle que haga algunas cosas por ti. Vamos primero a ella de estudio, de que estudios se los había enseñado y hicimos la landa en que no acabamos usando, pero les quiero enseñar también otra funcionalidad que tiene, así que vamos a nuestra navegador y vamos a buscar alguna clínica dental en mi ciudad, así es la primera que me arroja, pero que está bastante bien, nos está enfocado a un sector de turismo, así que vamos a agarrar la web, no me importa todo esto, se lo me importa hasta acá, vamos hacia aquí y le voy a decir, clona esta página, así como está tal cual traite todos los vídeos, traite toda la información, necesito clonarlo. Le ponemos la URL y lo mandamos. Como pueden ver, fue un programa muy sencillo, muy básico, solamente el eje clona esta página y ya está. Entonces lo voy a dar pausa para que no se haga tan largo, pero que vamos viendo cómo está analizando, va a construir todo y la verdad que termino regreso, más o menos les digo cuánto tardó. Listo, entonces mientras trabaja, el EIA y Studio vamos a irnos a la parte de agentes de EIA, es algo a lo cual le ha apostado mucho en los últimos meses, yo diría años, y en lo personal le llevo casi dos años con agentes de voz, como hay en medio con agentes de voz tomando llamadas diario, en este caso les quiero enseñar un poco de lo que tenemos en la parte de agentes de audio. Hay diferentes tipos de agentes, están los agentes de voz, que pueden recibir llamadas y pueden realizar llamadas, esa parte del adbound es relativamente nuevo, a llamadas fuera de Estados Unidos, tenemos la parte del chat, también tenemos la parte del chat, pero en caso como para agendar cosas y este es más uno de lead conversion y de ventas, tenemos el reputation manager que básicamente puede contestar automáticamente tus reseñas de Google y como aquí sale los diferentes voice agents, tenemos chat widget, tenemos contenido con AI, nos vamos aquí en agent studio, aquí puedes crear diferentes agentes que van a vivir dentro de la plataforma que ponen varias cosas, aquí tenemos lo que son agentes de voz, agentes conversacionales, bases de conocimiento y hay plantillas de agentes que ya existen y que tú puedes implementar. Esas son agentes de voz, quien de curso no lo vamos a ver porque será algo completamente en mucho más largo, igual podríamos agregar un bonus después y esas son agentes conversacionales que ya vienen preconflurados. Se fijas, aquí tenemos uno de dentro de la appointment con 51 mil mensajos respondidos y vamos a tomar con un talento de reseñas, vamos a ver si hay alguno con reseñas, vamos a buscar el dental, es el único que tenemos, vamos a implementarlo, es lo que te dice para mensajes, Instagram, Facebook, webchat, live chat y WhatsApp y te da todas estas acciones, aquí tú puedes ver dentro esto hay obviamente gratuitos y hay de par vamos a darle instalar vamos a ver qué es lo que nos da habilita instale y vamos a hacer otro nosotros desde cero para que veamos la diferencia a refrescar aquí está dentro de la pomembu quien lo más bueno es que tengamos que adaptar lo a español lo bajar el nombre en inglés para poderlo extinguir y tenemos tres estados del completamente desabilitado, tu gerido que te va dando como indicaciones de la ventana de chat o piloto automático y decir que el bot responde de manera automática todo. Y aquí tú puedes configurar los canales proveedores. Aquí tenéis cuidado con esto. Si tú no más buscas como vamos a hacer curso un chat, una gente perdón que responda a través de un chat widget que tengamos en lo que no está página web entonces necesitamos quitar varias de estas cosas porque si no estaríamos respondiendo por ese mes, Instagram, Facebook, etcétera. Entonces, no queremos que chat de en ese mes, no lo queremos en Instagram, no lo queremos en Facebook, no lo queremos en WhatsApp, no queremos widget chat, queremos chat en tiempo real. Aquí, configuración avanzada, nombre comercial, clínica, un risa perfecta. Estable es que la configuración del modo piloto automático se pone hacia su negocio, un segundo está bien, uno máximo como el mensaje es como puede enviar una conversación, también permite que vos responda a imágenes con otras de voz, vamos a decirle que sí, poner el bot de mode en activo cuando envío un mensaje manualmente a través de su clubo de trabajo, eso que sí que nosotros intervenimos, el bot se vuelve inactivo para esa contacto de esa conversación. Y aquí vos respondo a reactivar el bot, y en este caso yo no lo que una vez que hablo en un humano, yo no quiero reactivarlo. Confiriendo la respuesta, habilitar confiación de estilo de respuesta y aquí como queremos que sea. consisto, equilibrado, detallado y obviamente aquí nos va a cobrar por mensaje y el level ofrece una opción de 90 dólares al mes lo tienes que lo cheque de que es ia ilimitada para este tipo de casos, no sale guardar, vamos a lo que es el entrenamiento del bot y aquí como podemos ver no tenemos una base de datos objetivos del bot, aquí nos podemos escoger nosotros qué modelo va a utilizar algo tectean en cuenta no es como que ustedes vayan a poner sus llaves esto es lo cobra directamente a ustedes en su factura el acuerdo al consumo aquí más o menos te dije mira el coste estimado por mensaje son puntos 007286 dólares por mensaje es un costo muy bajo pero ya en volumen es evidentemente suma yo que tengo uno funcionando no son ni tres dólares más o menos armés. Aquí podemos definir la personalidad, todos los que son los programes, yo siempre lo recomiendo manejarlos en inglés y con únicamente la parte de donde le dices o que vas a hablar en español, etcétera, así hacerlo configuras, no ningún problema. Por ejemplo aquí si yo esta no lo vas a aprender o los quiero enseñar como viene porque nos vamos a confiar una descero. Aquí tienes la personalidad, el objetivo, información adicional, ahí se está en Maldon como pueden ver, aquí tú puedes confiar reacciones. Puedes darle que reserve hitas, actives, flujo de trabajo, que busque información de contacto, de tener voz, transferencia humana, transferida a otro voz, pigmento automático y tú puedes recibir un resumen de las conversaciones. Pues, de hecho, recibieron a por corre electrónico y no sé, todos los administradores. El objetivo del voz aquí como esto nos tenemos que el calendario, pero vamos a eliminarlo, espide que seleccionamos un calendario a la poder guardarlo y si no reservar cita suelen ver el ácido reserva. Posar las respuestas del bot después de la reserva, aquí va el flujo trabajo, todo es la reserva, se ve un empleado de reservar una cita, permitir que el bot anule, permitir que el bot reprogramme, es por si alguien habla por el chat dice hoy, quiero regendar o quiero cáncelo, vamos a darle que sí, vamos a darle guarda y vamos a saber que nos hace falta aquí que no nos desfue continuar y es como que información nacional, digo que no lo vamos a usar ahorita, pues añadir aquí valores personalizados, aquí tienes como directrices para el prompting, vamos a ver, para alguna razón no me desfada el aborto, distrito, por alguna razón no es el que estoy implementando, no me aguardarlo, pero vamos a hacer uno desde cero para que regresamos aquí, lista de acentes, vamos a crear bot, si aquí nos va a preguntar va a ser una configuración guía de formularios y es el perfecto para la captura básica de lids y la reserva de citas que no requieren lógica o cuando sí no es complejo. Vot basado en prompts, que es proporciona sus propias instrucciones personalizadas, prompt para un proceso personalizado de captura de lids, reserva de citas o preguntas y resposas generales y un constructor basado en flujos, constructor visual basada en el flujo para la captura y nutrición avanzada de lids, que involucra lógicas y condiciones complejas. Es un constructor reflujo visual, calificación avanzada de lich, objetivos y mares pasos de reserva de citas, pues por si queremos poder calificar lich. Esto fácilmente te puede sustituir un flujo de nocho N, y en el caso vamos a hacer un muy sencillo que va a ser basado en prompts, porque tampoco queremos el típico de formulario. Ok, preguntas y respuestas generales, Obtitivo va a ser reservar cita, vas a ponerle bot de sonrisa perfecta, piloto automático no lo queremos para esto, unicamente chat en tiempo real, nombre comercial, gríticas sonrisa perfecta, vamos a divajarlo 25, si puede hacer esto y queremos que es pesto, no queremos que se reactive, queremos que esa respuesta sea equilibrada, vamos a darle guardar, internamiento del bot, También otros podemos agregar una base de conocimiento para que pueda el bot ir a consultarla y eso va a depender de qué tanto informacionamos a necesitar y aquí tenemos nuestro objetivo del bot. Aquí tenemos estos modelos que podemos utilizar, yo lo recomiendo con 4-1 o 4-1-minis y es nada más como para agendar en el calendario desde más cliente y entonces tenemos la parte de personalidad, objetivo e información adicional, vamos a darle aquí para verlo y de hecho le había pedido a Cloud Code que me trabajara y que me diera el información. Listing prompt, putso revisantes de grabado, HTML y los otros que se los inventé, no hay ningún problema. Datboard son brisa perfecta, vamos a ver qué nos dio, contiene de chatboard, sección uno, no lechbait, intent flows, escalation rules, Houston prompt, eres ofía, te tata, todo esto como es magnum, lo podemos copiar, antes de copiar esto, vamos a hacer, vamos a pedirle que haga una fruta, vamos a regresar para acá, vamos a pasarle mira, Nisto que realiza es una ajuste, está dividido en tres secciones, de hecho puedes revisar esta documentación como para mejorar tus prompts te voy a dar el ejemplo lo que me viene ahorita por defecto y en base a eso mejoralo y adaptalo para clínicas a una lista de personas de entonces esto es personalidad como pausa voy a llenar todo de regreso listo vamos a ver que nos dio vamos a abrir de esto y nos dice fronte uno en la gente los es lo que se pregunta el cual personalidad un boom boom vamos a está acá, vamos aquí y abrimos esto, pegamos personalidad. Objetivo información ahí se no, el que iba a tener unos cambios, porque pues lo dirección de pedade méxico, pero es cancún, reglamos. Fistica, promoción activas, es bastante, no sé si me acepté tanta información, ahorita vemos, son mapeos, con los caracteres, tengo aquí, creo que no Dejo un límite de carácterés, o que me pasó por 1.490 para el nuevo. Vamos a recortar unas partes. Estamos a quitar varias cosas. Queremos que no organizamos aquí un flujo de trabajo. Aquí hay información de contacto en estamos. Tiene un nombre, en caso sería un nombre ya lo está pidiendo. Después dañe a esas acciones, asegúrese que se pueden incluir las preguntas. Si ya lo estamos preguntando el nombre, postar el COVID-19, de ir a ver, de ser lo podemos tomar nosotros, no necesitamos nada, esto, lo básico ya está. Transferencio humano, transferencio a voz, seguramente solamente reservar citas, la empresa dental, una transferencio inopliado, un tick de botonulo, por resumen de conversaciones, los administradores, listos. Ahora, cómo lo activamos, nos vamos a ir entonces a la parte de sitios, tu guilla de chat, vamos a crear una nueva, aquí va a ser un chat to de nulnok, que combine WhatsApp, chat en vivo, correo electrónico, etcétera, ese es SMS chat por correo electrónico, Facebook chat, chat en tiempo real, Instagram chat, chat de WhatsApp y ahí de voz, en ese caso era un chat en tiempo real, vamos a llamarle y empieza a identar. Ok, en estilos que es un elemento fijo o incertado en línea que va a ir como en medio de nuestra página o el elemento fijo que va a ir aquí flotando abajo, si fijan o si apago el mensaje del chat que lo puedo escoger aquí, osea cerrar esto, será como que la pura burbugita ya ven, y puedo cambiar como quiero que se ve el icono, los colores, que no se queda bien para la página, como trei, hola, como podemos ayudarte, aquí se activarse lo personalizado, no, personalizado de widget, imagen de avatar está bien, donde queremos que esté posicionado abajo la derecha y misión del widget si es automático o si es personalizado, de caso queremos que automático, vamos a ver en ventana el chat, título en producción, tienes alguna duda, por favor indicanos tu nombre y duda, y a alguien se pondará un telfón, un email, el botón diga enviar, asignado a tiempo espero traer su tiempo de inventar el usuario, pa' del excel, pa' del excel, nuestro vamos a hacer en inglés, vamos a habilitar horarios y son una notificación, brind de la ofencia, power by, linica, son risas perfecto, linica, son risas perfecto, vamos a pagarle el idioma español y vamos a darle guardos. Perfecto. Entonces ahora como lo ponemos en nuestra landing page, regresamos a sitios, chambudos, aquí fue lo que implementamos, nos vamos a hacer en configuración de widget, limpieza de ental, guardar, vamos a nuestra página, como venís que ya tenemos a chat aquí, hola, como podemos ayudarte, por favor indica nuestro nombre y duda, y yo supongo contacto contigo. Hola, me llamo Carlos. Quiero saber más de esto. Cuente que aquí no pusimos una promoción específica de la promoción, simplemente como con la idea de enseñarles cómo se puede trabajar. Y ya os parece que ustedes lo configuran. Esto está configurado hay como un delay de en qué tiempo responde y eso lo trabajamos tal cual en el chat widget como en la parte de aca de agents conversacional listas agentes, es una empresa perfecta, un piloto automático chat en tiempo real y tiempo spent de responder dos segundos que me gusten de pueden asignar el chat a diferentes personas. listo, algo que me había faltado es venir acá donde están mis agentes, como acá tengo dos y es darle clic en los tres puntos y era establecer como principal y aquí si fiquen y sale este principal, ahora sí vamos a hacer la prueba, vamos a ver una pesteña de incógnito para que no hay una sesión, ahí está nuestra landing, hola, como podemos ayudarte, duabro, tiene ese pequeño ruido, no sé si lo escuchen y lo voy a decir, hola, ni se dan mucho para asignarte a alguien, la escribiendo, yo la soy sofía, son ni se perfecta, Es que me tienes la promo de Empieza, Dental y quiero Ajundar. Una promo en Empieza, la 499 y el Projilar no tiene 9. Durante Abril los mismos a disponibles son hoy, puedes 23 de abrir las 12, cual te quedan. El más pronto. Perfecto, tercero jueves, que las dos se parecen dar a paz, el nombre completo WhatsApp y 10111 urgencia, el carno es el grado, otro es el otro, no lo vamos a ver, este es un toque y mi tuveo y eso. Ahora, como nosotros tenemos calendario un link de pagos, ya tienen que pagar para poder agendar, la gente no debe poder agendar porque hay un pago de por medio, así que vamos a ver qué es lo que pasa, en ese caso lo mejor será como resolver dudas y compartir el link poner en el prompt que compartan el link del calendario para que la gente vaya directamente y agende porque hay que hacer un pado en línea. Vamos a ver mientras se procesa esto, vamos a irnos acá a la cuenta y vamos a ver si hizo algo en contact. Tenemos como guest visitor que es toda ahorita, de hecho si nos vamos a ir con conversaciones, vamos ver aquí como las pruebas que estuvo haciendo, hay que poner todos, aquí es como que el último mensaje que yo le mandé y si nos vamos de vuelta a AI y inStudio, Conversation AI, contactos únicos, contacto eliminado, hoy a las 752 que puedes y nos vamos a resumen, no resumen, transcripción, eso por nuestras inscripciones, algo pasado con esto, vamos a ver por allá no me respondió, pude ver si algún erroro de que malproteo, si listo que la está haciendo para el empiece intervado, me heuchado un estudo en este link, para confirmar, okay, nos estamos dando el link para confirmar, el link no existe, porque es un link falso que pusimos en el chat de pronto, pero nos estamos dando aquí que básicamente sería esto y ahora les quiero enseñar algo, van a ver que el chat siga aquí, no solo está en el form, porque yo lo ponemos en todo ese embudo, ¿ok? No, es para que se lo tengan en cuenta, vamos a ver cómo va esto, sigue trabajando, entonces mientras vamos a hacer la otra configuración que es el mcp, entonces lleva a ver una nueva conversación que me agente y lo voy a pasar la documentación oficial de goja y leve, esto lo voy a incluir abajo en el Classroom, le voy a poner. Necesito que nos conectemos a High-Level via MSP, hay que estar la documentación oficial a la configuración que necesites. Y algo no más se queda aclarar en la configuración, nos sale que el MSP se conecta de esta forma, pero después de haber hecho ya varias pruebas con otras cuentas, yo sé que el MSP le falta aquí unos parámetros, entonces esto lo voy a incluir también en el post para que lo tengan en cuenta esto no es el dato real, lo real es mcp service está bien, es jchlmcp no lleva el prog, type HTTP, le falta el type aquí, el URL está bien y todo lo más está bien, entonces lo voy a copiar y pegar a mi agente como debe ir en base a mi experiencia que ya he hecho las pruebas y se lo voy a dejar aquí para ahorrarse también esto de esa parte. Listo. Ya se lo mandamos, mientras nos va a pedir que generamos un token, les voy a enseñar que en estamos dos cosas para hacer la configuración. Nistamos el location ID y el token ID. Eso es cómo lo conseguimos, nos vamos a vuelta para acá, nos vamos en configuración, perfil de empresa y aquí tenemos ID de la ubicación y le damos topear. dice perfecto nisto tu talk better y tu location ID como bien saben yo siempre les recomiendo no ponerle el chat simplemente configurarlo directamente así que lo voy a decir trae el archivo punto mcp y yo agrego los valores ahí list ya me generé el archivo vamos a poner dice tu pa ca un ID lo pegamos y el el autorización que es el better they're talking eso nos vamos para acá y nos vamos a ir a la parte de integraciones privadas para dar nueva integración que vamos a ponerle, no sé, cloud code, siguiente seleccionamos todos los scopes y vamos a bajar el que va a ver uno que nos dio un warning, lo pitamos, no necesitamos escribir los usuarios y debamos crear, popiamos el token, nos regresamos y los estuduimos aquí, file, en cuenta algo cada vez que hacemos una configuración de un mcp tenemos que cerrar esta conversación y volverla a abrir para que se actualice listo ya está el token y el id a su una prueba de conexión y me apéame lo que puedes hacer via en mcp y lo que no estoy disponible via mcp quiero que lo hagas via a pico esto y lo mandamos listo dice conexión ok verificé contra tu sub cuenta de locación clínica y edad son dice perfecta con un méxico español de méxico paguen detectado lo que pueda servir mcp 36 herramientas fue listar buscar crear conversaciones buscar conversaciones oportunidades leer mensajes etc. vamos a decirle ok muy bien el cual fue el último mensaje de Carlos julgado, a mi hijo aquí también como va a llamar la pí cuando haga falta, veis dice que no encuentro Carlos julgado, que fue lo que pasó muy probablemente o de aquí, el bot que hicimos no está bien configurado para lo que es guardar el nombre tenemos que ponerlo eso en las acciones, porque de hecho me guardo como Carlos domingues, ok ya di que fue lo que pasó, como ya existe el teléfono que le di y el porró que le di, ya existía mejor Carlos domingues, por eso no encontró nada como Carlos delgado y yo quiero que mi bot confirme con el usuario a y encontre ya un usuario el nombre de carlos domingues, quieres que lo cambia carlos delgado, es un algo que lo tengo que poner las instrucciones de la gente para que pueda hacer eso, entonces vamos a decirle, en la segunda vez tienes 15 contadios, el único carlos que aparece es que es tu mismo carlos domingues como lo que, cual fue el último mensaje, entonces enviado y recibido de carlos domingues y a través de que canal, las son de la conexión, ahí nos contactos cartulmínguez, conversaciones y nada más en paralelo, ok, aquí me dio por último mesas recibido, el último mesaje enviado, etcétera, ok, para cuestiones de la demo y el video que está haciendo estoy en la parte 11 del curso que puedes hacer via MSP o API para que le enseñamos a la gente que esté viendo vídeo, entonces me apiaba esto para que me salga bien el MSP, perfecto, estás en la selección 11, parte 3 cloud code más MSP diferenciador, voy al marte material real con datos en vivo de sonrisa perfecta que puedes demostrar en cámara para ver las herramientas que me faltan y saco a tus reales de 4 o 5 casas de sus factantes. Si ya tengo los datos reales de tu cuenta, también un guión, demos, cierto oportunidades, en el pipeline, demos 2, pacientes en riesgo, di en cámara, me está dando más como un script para que yo lo vaya leyendo, pero quiero que lo hago algo, contacto Workflow pero en la PC, aquí me hice lo que yo le puedo ir pidiendo. Ve, manda un whatsapp real de prueba a Carlos Dominguez, vas a mover también a María Bcerra a oportunidad ganada hasta el final y vas a agregar a María Bcerra de manera manual en el workflow de rescate de no show y obviamente aquí si uno no apestá ya le puede decir hoy es cuánto tengo ahorita como ganancia potencial en mi pipeline y vamos a dejar que vaya que lo consulta, porque workflow es encontrado rescate no show dispara dos acciones restantes en paralelo, admariabecerre tu rescate no show vio restapy, las tres acciones dificultadas, canal de whatsapp, mensaje o la carrera de Confensios de la Empieza, el mensaje de esperamos, fue por teniendo el mes de cerra cliente ganado, via MSP, para ver cerra agregado, el workflow de rescate. Ok, vamos a ver si es cierto, vamos aquí, conversaciones, perdón, contactos, Carlos Dominguez, y vemos aquí un mensaje WhatsApp, vemos que falló evidentemente porque no ha pensado la ventana de 24 horas, perdón, ya pasó la ventana de 24 horas evidentemente por lo se falló, vamos a clientes potenciales y vemos que Mariala Cerrella está aquí como ganado y está al final, muy bien lo hizo y automatización, rescate de no show, gistros de ejecución, ya tienen los Mariala Cerra que fue abregado del cual por cloud code. Y se ha añadido desde integration perfecto. Entonces, completos a tres acciones y si checamos otro, y si para concept me dice el location IDDH el sepacando en los pasos de divinador en la secuenta y tallado en contrarlo aquí como tiene no tenemos un no lo guardamos en el cloud md evidentemente perdió toda esa memoria entonces simplemente lo voy a decir utiliza el msp y ahí está toda la información y por último creo que ese servicio está fallando mía aquí sí que está experimentando problemas de alta latencia pero esto ya lo vimos en la parte de cartón de púneles, se le enseñé todo en ese momento. Así que creo que con esto podemos dar por concluido el video y le pusimos un cerebro a la clínica, el chatbot que atiende 24 o 7, tenemos herramientas de ya que haceran el trabajo, cloud code como orchestador, podemos consultar información de nuestro negocio, podemos pedirle que haga cosas como ya vieron, que manda mensajes, que manda gente a workflow a través del API, que cree contactos, que cree oportunidades, etcétera. Entonces ya en la siguiente y en la última sección vamos a ver resultado completo, el antes ver sus después, las métricas y cómo replicar todo esto en paquiller nicho. Entonces nos vemos ahí para el gran final.
