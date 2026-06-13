# WhatsApp con IA sin que Meta te banee

> Ruta: 🔴 Grabaciones › WhatsApp con IA sin que Meta te banee

**🎬 Vídeo (64.7 min):** https://www.youtube.com/watch?v=XUfcqK1v_s8

---

**Problemas que resuelve la sesion 22 de Mayo:** Cómo configurar WhatsApp para agentes de IA evitando bloqueos de Meta, cómo decidir entre coexistencia y API oficial, cómo manejar el traspaso bot-humano en agentes de WhatsApp, y cómo estructurar proyectos en Claude Code sin depender de subagentes.

**Intervenciones**

**[00:16] Apertura — Franco** Bienvenida a la sesión del viernes 22 de mayo de 2026. Dinámica abierta: levantar la mano para consultas, soporte similar al de los martes.

**[01:49] Iván — App de finanzas en pareja con agente WhatsApp** Construyó una webapp de finanzas en pareja con Supabase. Quiere agregar un agente de IA por WhatsApp para reducir fricción al cargar gastos. Pregunta el roadmap correcto: ¿N8N, WAHA, Cloud, código puro?

**Solución (Franco):** WAHA por sobre Evolution. El agente se arma en N8N o código puro, no en WAHA. Para conectar con la webapp, no hace falta desarrollar una API propia: usar directamente la API de Supabase para que la IA inserte, edite o borre filas. Sobre escalabilidad: buscar primero validación de mercado, los problemas de volumen se resuelven después.

**[09:33] Carlos — Advertencia sobre políticas de Meta** Meta está bloqueando asistentes personales de IA en WhatsApp y empezando a ofrecer sus propios agentes. Recomienda no basar todo el modelo de negocio en WhatsApp. Sugiere implementar un chat dentro de la propia app como diferenciador, dejando WhatsApp como feature complementario, no core.

**[16:15] Daniel — Riesgo de centralizar en redes sociales** Refuerza el punto: clientes que basaron todo su negocio en social media perdieron todo al ser bloqueados. Recomienda modelo híbrido manteniendo el control en infraestructura propia.

**[19:37] Flor — Actualización del template Forge** No entiende cómo actualizar Forge tras el último mail sobre soporte multi-CLI (Codex, Open Code, Gemini, etc.).

**Solución (Carlos):** Dos pasos. Primero, ir a la carpeta del template clonado y hacer `git pull` para traer la última versión. Después, en cada repositorio donde se use Forge, ejecutar `/update forge` dentro del CLI correspondiente. Si solo usás Claude Code, no cambia nada. Si te quedás sin tokens en Claude Code, podés abrir el mismo proyecto en Codex y ejecutar `/avivar` para retomar el contexto sin perder memoria.

**[25:24] Aporte — Usar Cowork como copiloto del template** Sugerencia de tener un agente Cowork leyendo el repositorio base de Forge para consultar qué comandos aplicar en cada fase sin editar el template original.

**[27:27] Lester — Registrar número WhatsApp desde Estados Unidos sin LLC** Pregunta si puede levantar un número oficial sin tener LLC constituida en California.

**Solución (Franco):** Lo importante no es la LLC, sino tener un business portfolio (no necesariamente verificado) y conectarse por la vía oficial de Meta. Explica las dos opciones: **Coexistence** (necesita una cuenta de WhatsApp Business existente con uso previo, permite usar el celular en paralelo a la API) y **Cloud API** (requiere un número que NO tenga WhatsApp Business activo). WAHA permite conectarse por cualquiera de las dos vías.

**[35:53] Iván — Limitaciones de la coexistencia** Pregunta si la coexistencia tiene limitaciones funcionales (a raíz de Kommo anunciando catálogo solo para Cloud API).

**Solución (Franco + Carlos):** La coexistencia puede desincronizarse cuando hay muchas sesiones abiertas compitiendo por recibir el mensaje primero. Tiene limitaciones reales: mensajes temporales, visualizaciones únicas, menor límite de mensajes por segundo, problemas con flujos y catálogo. Para usuario promedio, la coexistencia alcanza. Cloud API pura es más estable y necesaria para volúmenes altos.

**[42:09] Steven — Pausar la IA cuando interviene un humano** Pregunta en cuál de las tres plataformas (N8N, Evolution, Chatwoot) se configura el traspaso bot-humano.

**Solución (Franco):** Mostró su implementación en N8N: detectar señales entrantes vs salientes desde WAHA, guardar en base de datos un flag `IA in / IA out` por usuario, y filtrar al inicio del flujo. Si está en `IA out`, el flujo termina y la IA no responde.

**[46:25] Aporte (Carlos) — Misma lógica con Chatwoot** Alternativa nativa: usar etiquetas en Chatwoot (humano/bot) con automatizaciones que disparan al agregar etiqueta. En N8N se lee la etiqueta del webhook como filtro inicial. Franco complementa con un enfoque mixto: macro en Chatwoot que dispara un webhook a N8N para marcar `IA out` en la base de datos, así funciona igual desde WhatsApp o desde Chatwoot.

**[49:50] Mateo — Asistente multi-rol con Claude Code** Quiere armar un asistente con múltiples roles (desarrollo, agendamiento, secretario) usando subagentes y skills en Claude Code dentro de VS Code.

**Solución (Franco):** No necesita subagentes, necesita **proyectos separados**. Los subagentes generan más humo del que rinden. Recomendación: correr sesiones de Claude Code en paralelo en carpetas distintas, cada una con sus skills, memoria y patrones específicos. Cada carpeta = un contexto especializado. Para usar desde el celular: comando `/remote-control`. Para contexto compartido entre proyectos: Obsidian como capa de memoria común.

**[58:13] Aporte (Carlos) — Agent SDK como alternativa a remote** El Agent SDK permite conectarse a un Claude Code corriendo en una Mac Mini o VPS y levantar sesiones desde cualquier lugar cargando todo el contexto (skills, MCPs, memoria) sin necesidad de tener remote activado. Permite múltiples sesiones simultáneas. Útil para integrar un chat en una web que actúe como tu Claude Code local.

**[59:40] Daniel — Automatizar gestión de issues en GitHub** Quiere usar Hermes integrado a su VPS para que revise tickets de GitHub, cambie estados, ejecute el código y abra PRs durante la madrugada.

**Solución (Carlos):** Hermes con protocolo ACP conectado a Claude Code o Codex. Carlos comparte su flujo: corre un proceso de mañana y uno de noche en su Mac Mini, que detecta issues, trabaja durante la madrugada y entrega un reporte categorizando (bloqueados, listos para validar, en progreso con dudas).

**[1:04:25] Cierre — Franco** Anticipa que la sesión de la semana que viene tendrá un formato distinto. Saluda y cierra.
