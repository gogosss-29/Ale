# El error que arruina tus agentes de WhatsApp

> Ruta: 🔴 Grabaciones › El error que arruina tus agentes de WhatsApp

**🎬 Vídeo (63.2 min):** https://www.youtube.com/watch?v=7ecvW_F2aoA

---

**Problemas que resuelve:** Cómo instalar agentes de WhatsApp de forma segura y qué prácticas seguir antes de salir a producción, cómo configurar un VPS para OpenCloud y Evolution sin comprometer la estabilidad, y cómo automatizar la gestión de pacientes en clínicas con sistemas cerrados sin API.

---

**Intervenciones**

**[01:29] Luis – Amazon FBA y primeros pasos con IA** Nuevo miembro que usa solo ChatGPT de forma básica. Quiere explorar automatizaciones para contactar proveedores y analizar competidores en Amazon. Solución: se lo orienta a ver la grabación de Claude Code de la semana y a unirse a la sesión del lunes con Juaco para recibir guía personalizada según su negocio.

**[08:42] Tomás – Sistema de reactivación de pacientes desde historial de WhatsApp** Quiere construir una base de datos a partir de conversaciones antiguas de WhatsApp Business de un odontólogo: nombre, resumen del chat, tratamiento, última fecha de contacto y clasificación frío/tibio/caliente. Solución: exportar chats desde WhatsApp Business o sincronizar con Evolution API al conectar el número, descargar en CSV y cargar a Airtable. Se advierte que los audios e imágenes pueden presentar problemas al exportar.

**[13:36] Tomás – Agente WhatsApp con tres funciones: conversación, agenda y reactivación** Consulta si el cliente puede seguir usando WhatsApp Web mientras corre el agente, y qué buenas prácticas seguir al lanzar. Solución: WhatsApp Web puede generar conflictos ocasionales con la API (mensajes que no aparecen en web pero sí se enviaron), especialmente con pauta publicitaria. La recomendación es ofrecer acceso desde WCloud. Como buena práctica, apagar el nodo de envío los primeros días y recibir notificaciones de las respuestas generadas para revisarlas antes de habilitarlas en vivo.

**[24:45] Juan – Chatbot en página HTML de agencia aduanera** Cliente con página en HTML puro, sin plugins, quiere un chatbot integrado. Solución: armar el flujo del agente en N8N y pedirle a Claude Code un widget embebible en HTML que haga llamadas API al backend. Se menciona también el chat widget de Chatwoot como alternativa.

**[26:54] Guille – Landing pages más profesionales con Claude Code** Las landings generadas son demasiado genéricas. Quiere agregar efectos 3D, imágenes y mejor diseño. Solución: usar el skill humanizador web de Benja con componentes de 21st.dev, crear un archivo `design.md` con tipografía, colores y estilos de referencia, y conectar el MCP de shadcn/ui para acceder a una biblioteca de componentes de alta calidad. Google Stitch también se menciona, pero requiere más intervención manual.

**[44:18] Bostala – Configuración de VPS para OpenCloud y agentes de WhatsApp** Duda sobre qué proveedor y cuánta RAM elegir para no tener que migrar después. Solución: Hostinger con 8 GB de RAM es suficiente para empezar. Se recomienda no mezclar OpenCloud y agentes de WhatsApp en el mismo VPS sin contenerización Docker. Usar EasyPanel para gestionar N8N y Evolution por separado. Si se combinan, mínimo 8 GB; si se separan, 4 GB por servicio. Hacer upgrade es simple y no genera pérdida de datos.

**[48:45] Juan Felipe – Automatización en clínica dental con sistema clínico cerrado** Clínica con problemas de urgencias no atendidas por WhatsApp, cancelaciones sin reemplazo, órdenes de radiografía sin seguimiento y falta de empatía proactiva. El software clínico no tiene API por restricciones legales en Colombia. Solución en dos frentes: (1) Monitor de WhatsApp con N8N y WCloud que guarde mensajes en Airtable o Supabase y los analice con IA para detectar urgencias y prioridades. (2) Para extraer datos del sistema clínico: descargar reportes diarios en Excel y cargarlos a Drive o Airtable como puente. Si no, explorar acceso no convencional con Claude Code inspeccionando la interfaz del software. Como alternativa de largo plazo: migrar a un sistema propio en Airtable si la clínica es pequeña.

**[1:00:02] Daniel – Aporte sobre escalabilidad en clínicas** Señala que muchas soluciones simples funcionan bien para pocos usuarios pero colapsan al escalar. Propone hacer más research antes de implementar y se ofrece a colaborar dado que conoce el contexto de clínicas en Colombia.
