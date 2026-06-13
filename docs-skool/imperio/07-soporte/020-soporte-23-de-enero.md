# Soporte - 23 de Enero

> Ruta: 🛠️ Soporte › Soporte - 23 de Enero

**🎬 Vídeo (55.5 min):** https://www.youtube.com/watch?v=3Iqn15W6XZo

---

## Problemas que resuelve

Cómo **evitar bloqueos y límites** al enviar correos a gran escala, cómo **recuperar nodos faltantes** al migrar workflows en n8n, y cómo **conectar ManyChat + Make** para responder DMs con IA (mapeo correcto de webhook response), además de criterios para **elegir n8n vs Make** según volumen y costos.

---

## Intervenciones (cronológico)

[01:03] Jorge – Enviar correos masivos desde n8n sin reventar Gmail  
Jorge quiere, cuando entra una oferta laboral, filtrar en su base (+100.000 CVs) y mandar email a todos los perfiles que coincidan (ej: “geólogos”). Se aclara que **Gmail directo puede limitar/bloquear** por volumen y reputación, y conviene usar un **servicio de envío** (tipo newsletter/marketing email) para proteger la cuenta.

[02:36] Franco – Recomendación: usar plataforma de emailing (no Gmail)  
Se sugiere usar un proveedor de campañas (se menciona Mailchimp como referencia), y que en n8n hay nodos nativos para integrarlo. Se enfatiza: el objetivo es **proteger el dominio/cuenta** y evitar problemas por volumen.

[05:07] Daniel – Diferencia entre transactional vs marketing email + alternativa más barata  
Explica que hay **emails transaccionales** (compra, reset password) vs **emails de marketing**, y que para envíos de volumen conviene un proveedor tipo MailerLite/SendGrid (menciona “Srid/Sangrid” como su stack) por costo y entregabilidad. Advierte que con Gmail es fácil meterse en problemas.

---

[07:36] Tomás – Migración de cuenta n8n: desaparecieron nodos (Evolution API)  
Tomás importó un workflow en una nueva cuenta y ya no ve nodos que antes sí (Evolution API). Se identifica que faltan los **community nodes**.

[09:36] Franco – Solución base: instalar Community Nodes  
Se indica que es tema de instalación: hay que **instalar los community nodes** (igual que en la cuenta anterior).

[10:22] Carlos – Importante: reinstalar y reimportar el workflow  
Aclara que si importaste el JSON sin tener el community node instalado, queda “roto”. Recomendación:

1. **Eliminar** el workflow importado
2. **Instalar** community nodes
3. Volver a **importar** el JSON o copiar/pegar desde el workflow que sí tiene los nodos.

[12:10] Tomás – Duda sobre EasyPanel: ¿un solo proyecto o varios?  
Consulta si puede meter todos los servicios en un solo proyecto (por estar en plan free).

[12:50] Carlos – Sí se puede, solo cuida Redis/Postgres  
Se confirma que funciona sin problema. Buenas prácticas: separar, pero no obligatorio. Ojo con:

- **Redis**: no mezclar datos entre escenarios (evitar conflicto).
- **Postgres**: crear tablas separadas por escenario y considerar limpieza si crece el volumen.

---

[14:52] Gabriel – Error en Make + ManyChat + ChatGPT para responder DMs de Instagram  
Gabriel intenta un flujo: ManyChat → Webhook (Make) → ChatGPT → devolver respuesta a ManyChat. Tiene errores y no logra que ManyChat “reciba” el texto generado.

[17:29] Franco – Concepto clave: ManyChat espera respuesta del webhook  
Se explica que ManyChat envía un webhook y **espera respuesta** (ventana de ~10s). Para esto no se usa HTTP module al final, sino **Webhook Response** devolviendo el body correcto.

[20:06] Franco – Ajuste de mapeo: devolver el “Result” correcto  
Se corrige el mapeo de variables: el contenido estaba mal referenciado (choice/message/content). Se ajusta para devolver el output correcto del modelo y que ManyChat lo pueda leer.

[24:03] Franco – Configuración en ManyChat: External Request + Response Mapping  
En ManyChat se prueba la solicitud y se verifica que ya se recibe la respuesta. Luego se configura el **mapeo de respuesta** (syntax/JSON path) para guardarlo en un **campo personalizado**.

[30:16] Franco – Crear campo personalizado “respuesta” y usarlo en el reply  
Se crea un custom field (texto) y se usa esa variable en el mensaje de salida de Instagram para que el DM se responda con el texto generado.

[33:21] Franco – Limitación práctica: si el flujo tarda >10s, este método falla  
Se deja claro que esto sirve si el procesamiento es rápido. Para agentes más complejos (calificación, agenda, lógica larga), hay que hacerlo con arquitectura distinta y ver los recursos de ManyChat en la comunidad.

[36:42] Franco – Recomendación técnica: para alto volumen, mejor n8n que Make  
Por costos (Make cobra por operaciones) y escalabilidad, para muchas conversaciones diarias conviene **n8n**, levantando servidor, y usando la comunidad/plantillas para implementar.

---

[41:17] Miembro – Agradecimiento a Carlos por soporte EasyPanel/n8n  
Comenta que pudo resolver problemas de versión/config con ayuda de Carlos y ya quedó listo para avanzar.

[42:21] Miembro – Scraping de precios en dos regiones (misma tienda, distinto dominio)  
Consulta si se puede comparar precio entre “.com” vs “.[com.mx](http://com.mx)” usando link por WhatsApp. Se responde que sí: probablemente funciona por SKU/ID, pero puede cambiar el HTML y requerir ajustar el scraper por región.

---

[44:22] Miembro – Qué vender con automatizaciones: ya arma chatbots Q&A para ecommerce  
Pregunta por recomendación de producto/servicio vendible. Franco sugiere:

- Elegir una solución base replicable para ecommerce (para referidos y rapidez)
- Iterar y sumar automatizaciones con el tiempo
- El pricing no depende solo del tiempo, sino del valor
- Lo más importante: conseguir cliente, resolver y luego expandir.

[50:46] Juana – En qué plataforma se hacen estos chatbots/agentes  
Se aclara diferencia:

- “Chatbot” viejo (menú 1/2/3) vs **agente IA** (texto o voz).
- Recomendación general: **n8n** por flexibilidad, costo y escalabilidad (aunque Make también puede).

[52:27] José – Duda herramienta para postear redes con n8n (app/post)  
Carlos confirma que la usó (barata y funcional, especialmente para Instagram) mediante community node.

---

[54:02] Franco – Aviso: próxima sesión enfocada en ventas/consultoría  
Se adelanta que Benja anunciará una sesión distinta sobre **cómo vender**, hacer consultoría, preguntas correctas y proceso comercial.

[55:13] Cierre – Recordatorio de formato  
Sesiones martes y viernes con preguntas/respuestas. Se cierra la sesión.
