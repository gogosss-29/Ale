# 📷 Conseguir Leads de IG Manychat + Mailerlite

> Ruta: Automatizaciones Make › 📷 Conseguir Leads de IG Manychat + Mailerlite

**🎬 Vídeo (22.7 min):** https://youtu.be/aJ8ey_WJ0f8

**📎 Recursos:**
- Leads desde IG Manychat Mailerlite

---

### Guía Paso a Paso: Cómo Conseguir Leads desde Instagram usando ManyChat y MailerLite

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/41ecfda86de1402db3480f7d60049922eaa82022c25d42b68924c5cb56f609fe)

Si quieres aumentar tus leads desde Instagram de forma automática, esta guía es para ti. Aquí aprenderás cómo configurar un agente de ventas automatizado que recopilará los correos electrónicos de tus seguidores cuando comenten en tus publicaciones. Esta información se enviará directamente a tu CRM (MailerLite en este caso), y el sistema enviará tu lead magnet a los interesados de manera automática. Sigue estos pasos y tendrás una máquina de generación de leads en piloto automático!

#### Herramientas Necesarias

1. **Make (antes Integromat)**: Esta herramienta conecta diferentes apps y automatiza procesos.
2. **ManyChat**: Plataforma de automatización de mensajes en redes sociales, que permite crear flujos de conversación.
3. **MailerLite**: CRM para gestionar y enviar correos electrónicos.

**Costo estimado**:

- **Make**: Ofrece planes gratuitos con un límite en las automatizaciones.
- **ManyChat**: Plan gratuito disponible, pero el plan Pro (necesario para la integración con Make) cuesta $15 USD al mes.
- **MailerLite**: Planes gratuitos y pagos según el número de suscriptores.

### Paso 1: Configuración de ManyChat para Instagram

1. **Crear Cuenta en ManyChat**: - Ve a [ManyChat](https://manychat.com) y regístrate.
- Elige la opción de **Instagram** cuando te pregunte por la plataforma de integración.
- Conéctate con tu cuenta de **Facebook** (Instagram y Facebook deben estar vinculados).

### Paso 2: Crear el Flujo de Conversación en ManyChat

1. **Elegir un Template Pre-Diseñado**: - Dentro de ManyChat, busca el template llamado **Ampliar lista de correos electrónicos** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/858bf86379504428b847d0992a8def038ba09b7bf42b4bae8b5b3d43ef2fab37) - Ahora, podremos configurar el template para que, cuando alguien comente una palabra clave en tu publicación, comience la automatización.
2. **Configurar el Trigger**: - Define en qué publicaciones se activará el chatbot (puede ser en una o en todas). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/072e41fb1fcc45e09e7ed3ac1bedc0310942ef98141b41b183548b11a5738f89) - **Ejemplo**: Si estás promocionando una guía, define que cuando alguien comente la palabra "guía", se inicie la conversación.
- Define cual será la palabra que comentarán para desencadenar la automatizacion, por ejempo "guía" ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/bf1048cc48014249bff2371a5d7cf10d7007142917d942eb9d1f344978115401) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3e8afa9e29bb45b68a110dd474516acbddff4e6e8dae4fd4848ae7bd5b87a53f)
3. **Crear el Flujo de Mensajes**: 1. Mensaje de bienvenida: "¡Me alegro mucho que quieras mi guía gratuita "Cómo Crecer y Convertir a Tus Seguidores"! 🥳 Toca abajo para obtener el freebie👇"
2. Pregunta por el correo: "Genial, ¿cuál es tu mejor correo electrónico? Prometo no hacer spam. 😉" ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e2b5c26ed06e413fb0da4a2fa6683d28398156d15b7743b78192bf2bfeb7268b) **Luego incluiremos el link de la guía que le mandaremos** ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/dccbce7496bd40f2992699e605fad9d540e7992b2ef84e7ab2d2eeb10d2088fe-md.png)

La dejaremos corriendo apretando "Publicar en Vivo"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a0b9f86b784d4cf393bd98ac74c76796249751b3cc5a4dbf81d0b6ae29ced5c3)

### Paso 3: Conectar ManyChat con Make y MailerLite

1. **Configurar Make**: - Accede a [Make](https://www.make.com) y crearemos un nuevo escenario.
- Importaremos la automatización de abajo (archivo importable al final de esta guía) o la crearemos directamente  
 ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1f36692c4d0145779851a5cd1a537cec400b9b0dbdb54f6ea8bd9d97d84a31a7)
- Agregaremos 2 módulos, uno de Manychat y otro de Mailerlite. El de Manychat buscaremos el módulo "Watch Incoming Data" ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/87e3970e17f54dff818366b3d857f6fbafefe5fdcd684458a45438cc483a77ba)
- Le daremos a "crear un nuevo webhook", y "agregar conexión". ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4f1dace4f65d4556ab6c3eeec9a4d1a6a664e6a0898c4ddaa121b1878a0b73cb) En Manychat, nos iremos a configuracion y "API". ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6f2e7b4666cd470c818ecc7742c8a40855a1d5995108478585efc28140615fdb) Copiaremos el API de Manychat ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b847b59c669247d8be7c7c9569f5bf31426352163c7446e2899330b93ea01b4d) Pegaremos en Make. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d1657da8c9d140239a2a3f37f30a9c32234b1cf7b24a4ebb985b1b647eb94412)
- Este webhook recibirá la información que ManyChat recoja (nombre y correo del usuario). En el mensaje donde le pedimos el input "el correo electronico" agregaremos una nueva acción, para que cuando nos den su correo, podamos pasarlo a Manychat. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1ec110a451db4c298f2ad5b3a970e92d031ebf7faa2c4843ab83b1d89f12dd3b) Apretaremos en "acciones" y le daremos a "crear nueva acción" ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c0e863d85ce94b249cbae33e4d63e4b9779f8a0d4bee453a89ebab678193d2dd) Nos iremos a la opcion que sale "Make" y le daremos a "activar make" ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/76b60ce97f1342e2b6abeb6b1bfa814b5a445588a2a74cfa8b63be655249c4ff) Luego seleccionaremos el Webhook que creamos previamente en Make ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/00199564312349dc82f71c55ff9e3cfd1917194a47914720991ee9dc5af9f234)
2. **Conectar a MailerLite**: - En Make, añade un nuevo módulo y selecciona **Create Subscriber** en MailerLite.
- Conecta tu cuenta de MailerLite con Make. Para eso crearemos el nuevo modulo "create new subscriber" de Mailerlite ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3a5459af37fd48129d00974b04fd0a482dfd094471b640b9a0015b6d6ff87d22) Nos pedira un API de Maielrlite, y esto lo sacaremos de la página de Mailerlite ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e9860b7c1b9e446dbec98b1b8f4adb9b8c038900b8ea4623aa48faf6e4df2185) Para encontrar el API nos iremos a nuestra cuenta, Integraciones y API ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/05b5346bcdac4ea986b95fca77ae7f1dfd202f10f1f641f5a3e5ba2950f4383f-md.png) Generaremos un nuevo API y los conectaremos  ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9d4e52fc166e4759be0bd53d0015da6aa278ffc570164fc0b21e19d2abf01cc5) - Configura el módulo para que los datos de nombre y correo se envíen automáticamente a tu lista de suscriptores en MailerLite. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e98f6f16dd644ff4b1570212c7c48b75efaee4fd90a04274aaeb34d10e49b4e1) (NOTA: En el email address debes incluir "Last Input Text" o "email". Cualquiera de los dos servirá.) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b82cdb35a39e4921b71cdffa6d290d8b9cc3ced2feb74d8fac775617c8bafb36)

### Paso 4: Probar la Automatización

1. **Prueba en Instagram**: - Publica en Instagram algo como: "Si quieres recibir mi guía gratuita, comenta "guia".
- Comenta la palabra clave y verifica que ManyChat inicie la conversación.
- Asegúrate de recibir el recurso - Ve a tu lista de suscriptores en MailerLite y verifica que el nuevo contacto se haya agregado correctamente.

### Paso 5: Optimiza y Escala

- **Optimiza**: A medida que obtienes resultados, puedes ajustar tus flujos de mensajes en ManyChat para mejorar la tasa de conversión.
- **Escala**: Usa esta estrategia en múltiples publicaciones y experimenta con diferentes lead magnets.

### Conclusión

Con estas simples configuraciones, tendrás un sistema automatizado para capturar correos electrónicos desde Instagram, enviarlos a tu CRM y entregar tus recursos automáticamente. Así es como muchos influencers y negocios están monetizando sus audiencias. ¡Ahora es tu turno de implementarlo!
