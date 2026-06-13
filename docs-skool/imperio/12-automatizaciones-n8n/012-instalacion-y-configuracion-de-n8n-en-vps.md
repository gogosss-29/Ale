# 🎥 Instalación y configuración de N8N en VPS

> Ruta: Automatizaciones n8n › 🎥 Instalación y configuración de N8N en VPS

**🎬 Vídeo (77.8 min):** https://www.loom.com/share/af37bfb888ad45dd8856f41c2c868e0f

---

Hoy les traigo una instalación de n8n self-hosted que quedó realmente brutal.

Con este setup puedes tener tu propio n8n en un VPS barato, listo para correr automatizaciones en serio, sin depender de la nube oficial.  
Pagas centavos al mes, escalas cuando quieras y puedes montar flujos para tu negocio o incluso para clientes.

Toda la instalación se hizo en vivo. Desde elegir el proveedor hasta dejar n8n corriendo con dominio propio, EasyPanel y credenciales de Google conectadas.

📌 ¿Qué vas a tener al final?

Con este flujo terminas con:

- Un VPS Linux optimizado para n8n
- EasyPanel instalado para gestionar todo por interfaz gráfica
- n8n corriendo con la última versión estable
- Dominio propio tipo `n8n.tudominio.com` y `easypanel.tudominio.com`
- Certificados SSL activos
- Volumen de disco configurado para guardar binarios
- Conexión completa con Google (Gmail, Drive, Sheets, Calendar, etc.)

![CleanShot 2025-11-25 at 10.17.41.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ba2a9674a0eb4dedbe4d1e08ff94a15cf4d725de28f6412d87e6a570a3a4672d-md.png)

🔧 Paso 1. Elegir el VPS correcto sin quemar dinero

En el video revisamos varias opciones típicas para Latinoamérica.

- Hostinger
- HostGator
- Google Cloud
- Ionos

Conclusión directa.

- Para producción muy grande y súper escalable. Google Cloud. Pero es más técnico y complejo.
- Para algo realista, barato y suficiente para agencia o negocio. Ionos VPS Linux gana en relación precio vs recursos.
- Un XS o M sirve para empezar a jugar. Con 4 cores y 8 GB de RAM ya tienes algo serio para producción.

![CleanShot 2025-11-25 at 10.19.05.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b1d4281a551a4268b474ad8e0200f54787b5ca399fa147a383e71c159482c6ea.png)

🖥️ Paso 2. Crear el VPS en Ionos y preparar acceso

Flujo básico que se siguió.

1. Elegir VPS Linux, no Windows. - Linux consume menos recursos y está pensado para servidores.
2. Seleccionar plan (ejemplo. 4 cores y 8 GB de RAM) con pago mensual o anual.
3. Escoger ubicación del servidor en Estados Unidos. Latencia perfecta para México y Latam.
4. Sistema operativo. Ubuntu 22.04 LTS.
5. Finalizar compra, esperar a que el VPS arranque y copiar. - IP del servidor
- Usuario root
- Contraseña inicial

![CleanShot 2025-11-25 at 10.23.44.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/dd9b10543b1340fda08b39a0f0d9073e0efc0b0c256e474ea339fedb2daf05e6.png)

🔐 Paso 3. Conectarte por SSH y montar EasyPanel

Para administrar todo sin sufrir con consola en crudo, usamos EasyPanel.

1. Conectarte por SSH - En Windows. PuTTY
- En Mac o Linux. SSH directo por terminal
2. Usuario. `root`
3. Pegar la contraseña del VPS desde el panel de Ionos
4. Ejecutar el script oficial de instalación de EasyPanel que te da su web - Lo pegas en la consola y lo dejas trabajar
5. Cuando termina, entras a EasyPanel vía navegador usando. - `http://IP_DEL_SERVIDOR:3000`

Ahí creas tu usuario y contraseña para EasyPanel.

⚙️ Paso 4. Instalar n8n con plantilla en EasyPanel

Dentro de EasyPanel.

1. Ir a `Servicios` o `Projects` y crear un nuevo proyecto llamado `n8n`.
2. Abrir la sección de plantillas.
3. Buscar `n8n` y usar la imagen oficial.
4. Ver la versión estable en GitHub Releases y ponerla en el campo de versión. - Ejemplo. `1.108.2` si esa es la última estable.
5. Crear el servicio y luego darle `Implementar` para hacer el deploy.

EasyPanel levanta el contenedor y te da una URL temporal tipo.

- `http://algo.random.easypanel.app`

Con eso ya puedes entrar al setup inicial de n8n y crear tu usuario admin.

![CleanShot 2025-11-25 at 10.24.55.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b0eede292c2c43b6bbc7ff024da19eb1218331bf527d48cfba34ca61ab638007.png)

🌐 Paso 5. Conectar dominio propio y DNS

No tiene sentido quedarse con la URL fea. En el video se conectó un dominio tipo `agenciax.com` usando HostGator como registrador, pero la lógica aplica para cualquier proveedor.

Queríamos dos subdominios.

- `n8n.agenciax.com` para el editor de n8n
- `easypanel.agenciax.com` para el panel de EasyPanel

Pasos.

1. En EasyPanel. - Ir a `Dominios`
- Agregar `n8n.agenciax.com` apuntando al puerto de n8n
- Agregar `easypanel.agenciax.com` apuntando al puerto 3000
2. En el panel DNS del dominio (HostGator en el video). - Crear registro A para `n8n` apuntando a la IP del servidor
- Crear registro A para `easypanel` apuntando a la misma IP
- TTL bajo (600s) para que se propague rápido

Después de unos minutos, ya podíamos entrar a.

- `https://n8n.agenciax.com`
- `https://easypanel.agenciax.com`

🔒 Paso 6. SSL y variables de entorno clave

En EasyPanel se gestionan los certificados automáticamente, pero puede tardar un poco en emitirse el SSL. Una vez activo, desaparecen los avisos de sitio inseguro.

En el proyecto n8n configuramos variables importantes.

1. Activar nodos de la comunidad. - `N8N_PACKAGE_MANAGER_ALLOW_BUILTIN` = `true`
- `N8N_RUNNERS_ENABLED` = `true`
2. Crear un volumen de almacenamiento para binarios. - Nombre. `binary_data`
- Path. `/home/node/binary`  
Esto permite guardar imágenes, PDFs, etc. en disco y reutilizarlos entre escenarios.

📩 Paso 7. Conectar n8n con Google (Gmail, Drive, Sheets, etc.)

Aquí es donde la instalación deja de ser “demo” y pasa a “herramienta real de trabajo”.

Se configuró todo por Google Cloud Console.

1. Crear proyecto en Google Cloud. - Nombre. algo tipo `n8n-agenciax`
2. Activar APIs necesarias. - Gmail API
- Google Drive API
- Google Sheets API
- Google Calendar API
- Cualquier otra que vayas a usar (Search, etc.)
3. Configurar pantalla de consentimiento OAuth interna (si solo la usas tú o tu organización).
4. Crear credenciales OAuth tipo “aplicación web”. - Agregar URIs de redirección. - `https://n8n.tudominio.com/rest/oauth2-credential/callback`
- Versión sin `callback` por si la quieres reutilizar después
5. Copiar `client_id` y `client_secret` en n8n dentro de las credenciales de Google.

En el video se conectaron.

- Gmail. para recibir correos y disparar flujos
- Google Drive. para crear carpetas y subir archivos
- Sheets y Calendar se dejan listos para configurarlos igual

![CleanShot 2025-11-25 at 10.26.56.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/dd1c0bd2ed8047f88d0e701dd86ed7c7d1207b29df974447855afb05bfb002f3-md.png)

🧪 Paso 8. Test rápido dentro de n8n

Para probar que todo estaba bien.

- Se creó un trigger de Gmail para “message received”
- Se conectó con la cuenta de la agencia
- Se probó con `Fetch test event` y se trajo un correo real de bienvenida de Google
- Se añadió un nodo de Google Drive para crear una carpeta de prueba y confirmar que la credencial funciona

Con eso ya quedó demostrado que la instalación está bien conectada, que el dominio funciona y que Google responde.

🚀 ¿Por qué este setup es tan potente?

Porque te da.

- Control total sobre tu infraestructura
- Costos ridículos comparado con SaaS tradicionales
- Escalabilidad real. puedes subir de plan en el VPS en minutos
- Posibilidad de alojar automatizaciones para clientes y cobrarles mensual
- Libertad para montar extra. Telegram, WhatsApp, APIs propias, scrapers y lo que se te ocurra

Este es literalmente el “backend de automatización” que muchas agencias y negocios necesitan pero no tienen.
