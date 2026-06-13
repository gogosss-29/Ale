# Escala WhatsApp, domina OpenClaw, salva tu VPS

> Ruta: 🔴 Grabaciones › Escala WhatsApp, domina OpenClaw, salva tu VPS

**🎬 Vídeo (64.5 min):** https://www.youtube.com/watch?v=ZsUlz0J3uIQ

---

---

**Problemas que resuelve:** Cómo escalar outreach automatizado por WhatsApp a múltiples números y países sin incurrir en costos elevados, cómo evaluar cuándo adoptar herramientas experimentales como OpenClaw de forma segura, y cómo evitar que el VPS se llene por acumulación de archivos binarios en N8N.

---

**Intervenciones**

**[****00:00****] Tomás – Outreach automatizado con Evolution y el problema de escalar a varios números** Comparte que lanzó su sistema de outreach por WhatsApp usando Evolution, enviando mensajes de forma secuencial y creciente.   
Logró su primer interés de cierre con una odontóloga. Su problema: quiere probar el sistema en múltiples nichos y países de forma simultánea, pero no sabe cómo manejar varios números de WhatsApp al mismo tiempo.

Solución: instalar Chatwoot en el mismo VPS donde corre Evolution. Permite gestionar múltiples números desde una sola interfaz, ver todas las conversaciones centralizadas y responder sin necesidad de tener los celulares físicos a mano.

**[****04:44****] Franco y Carlos – Alternativas para conseguir y gestionar múltiples números** Franco sugiere usar eSIMs con apps como Airalo para obtener números de distintos países a bajo costo. Carlos propone una alternativa más técnica: levantar emuladores Android con Bluestacks, instalar WhatsApp Business y usar números virtuales con verificación por voz. Se discuten las limitaciones de Evolution (desconexiones frecuentes) y cuándo conviene migrar a la API oficial de WhatsApp (Whitecloud/Cloud API) para ganar estabilidad y escalabilidad.

**[****14:44****] Franco – Diferencia entre Evolution, coexistencia y API oficial** Explica cómo funciona Whitecloud: permite usar WhatsApp Business en el celular y la API al mismo tiempo (coexistencia), o levantar directamente la API sin necesidad de tener el número instalado en ningún dispositivo. Muestra la plataforma en vivo con ejemplos de ambos tipos de conexión.

**[****25:05****] Flor – ¿Conviene instalar OpenClaw ahora?** Plantea su dilema: quiere instalarlo para automatizar su blog de viajes, pero los propios creadores advierten que hay que tener cuidado. No sabe si sus conocimientos actuales son suficientes para manejarlo.

**[****27:07****] Daniel – Advertencia desde la experiencia: no subirse a la ola antes de tiempo** Con más de 20 años en programación, comparte casos reales donde adoptar tecnología nueva antes de que madure generó caídas graves en producción. Recomienda dejar que la herramienta avance, que otros encuentren los problemas, y adoptarla cuando esté más estable. Para tareas muy específicas, puede tener sentido; para darle control amplio, todavía no.

**[****33:56****] Franco – Perspectiva equilibrada sobre OpenClaw** Coincide con Daniel en la cautela, pero señala que el salto de OpenClaw respecto a otras herramientas ya justifica explorarlo. Comparte cómo en Robu lo están probando en un entorno completamente aislado: N8N propio en un servidor separado, sin acceso al servidor principal, sin compartir credenciales ni bases de datos. El objetivo es que pueda desarrollar flujos en un entorno de laboratorio sin riesgo.

**[****35:16****] Juaco – Cómo está usando OpenClaw de forma segura a nivel personal** Lo instaló en un VPS propio, bajo un subusuario (no root), con acceso parcial solo a una base de datos específica de Notion. Nunca le pasa tokens por el chat. Los archivos de configuración sensibles los edita directamente por SSH. Para compartir documentos generados, usa una carpeta de Drive compartida. Recomienda verlo como algo experimental, en entorno aislado, jamás en el computador personal ni con acceso al correo o datos sensibles.

**[****47:40****] Flor – ¿OpenClaw usa el Chrome del usuario para navegar?** Pregunta si al darle acceso a internet, el agente usaría su sesión de Chrome y sus contraseñas guardadas.

Solución: no. OpenClaw usa un Serverless Browser, no el navegador del usuario. No toca sesiones, no da clics, no accede a credenciales guardadas. Opera a través de llamadas internas sin relación con el entorno local del usuario.

**[****52:22****] Óscar – Shopify bloquea datos de clientes en la API sin plan de $400/mes** Necesita nombre completo y correo de compradores para sus automatizaciones de email marketing y WhatsApp, pero la API de Shopify no los entrega sin el plan plus.

Solución: en lugar de conectarse a la API, aprovechar las notificaciones automáticas que Shopify envía por correo. Configurar N8N para hacer polling de ese mail, extraer los datos necesarios y continuar el flujo desde ahí. Si eso no alcanza, existen métodos más avanzados con nodos HTTP para acceder a la interfaz de administración directamente.

**[****55:19****] Óscar – VPS de Hostinger lleno por acumulación de binarios en N8N** Al procesar videos pesados en sus automatizaciones, el VPS se llenó sin aviso y N8N se cayó. Los archivos quedaban guardados como parte de las ejecuciones.

Solución (Daniel): configurar las variables de entorno de N8N para activar `N8N_BINARY_DATA_MODE=filesystem`, establecer un TTL para los binarios (por ejemplo, 60 minutos), y configurar el pruning de ejecuciones para que no se acumulen indefinidamente. Todo esto se puede hacer con ayuda de Claude o GPT pasándole el directorio de variables de entorno del Docker y la documentación oficial de N8N.

**[****01:04:09****] Cierre** Franco resume la sesión destacando la importancia de explorar herramientas nuevas con criterio, siempre en entornos aislados. Invita a continuar el trabajo el martes.
