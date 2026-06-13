# 📞  3. Canales de Comunicación

> Ruta: GHL desde Cero › 📞  3. Canales de Comunicación

**🎬 Vídeo (15.2 min):** https://www.loom.com/share/d53cb4ab7a444c89906d680d44ddb4dc

---

**Curso: Go High Level Desde Cero · Sección 3 de 12**

> *Si no puedes hablar con tus clientes, no puedes venderles.*

Tenemos un sistema bonito, pero un sistema bonito no sirve de nada si no puede comunicar. En esta sección conectamos los tres canales que vamos a usar durante el resto del curso: **email**, **SMS** y **WhatsApp**. Es como poner el cableado eléctrico antes de instalar los focos — sin estos canales, las automatizaciones que construiremos después no pueden enviar nada.

## **📚 Qué vas a aprender**

- Configurar un **dominio dedicado de email** con SPF, DKIM y DMARC para que tus correos no caigan en spam
- Comprar un **número de teléfono** en GHL para llamadas y SMS
- Configurar **WhatsApp Business** con el portafolio comercial de Meta
- Hacer una prueba real de cada canal al final

## **🛠️ Paso a paso**

### **1. Configurar email con subdominio dedicado**

Ir a **Settings → Email Services**. GHL recomienda usar un subdominio dedicado para mejorar la reputación del correo y evitar spam.

La convención es usar `lc.` (de Lead Connector) como prefijo:

```
Subdominio: lc.clinicasonrisaperfecta.site
```

![CleanShot 2026-04-24 at 10.00.37.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ab948dc9fb474754b6512842c59be36a785e38b5d2e94773a2341b6ba51adf78.png)

GHL te va a pedir agregar varios registros DNS en tu proveedor. Te muestra uno por uno:

- **TXT** (verificación de dominio)
- **TXT** (SPF)
- **CNAME** (DKIM)
- **TXT** (DMARC — opcional pero **muy recomendado**)

### **2. Agregar los registros DNS en Hostinger**

Ir a **Hostinger → DNS / Nameservers → Manage DNS Records** y agregar los registros uno por uno tal como aparecen en GHL.

![CleanShot 2026-04-24 at 10.01.57.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/aa4f5242ef5c4121902b1f44f2795c8ed0d7a007fee1444b8b089fd1ceb09305.png)

### **📋 Plantilla — Registros DNS de Email (ejemplo)**

```
Tipo    | Nombre              | Valor                              | Prioridad
--------|---------------------|------------------------------------|----------
TXT     | lc                  | [valor que te da GHL]              | —
TXT     | lc                  | v=spf1 include:mailgun.org ~all    | —
CNAME   | mail._domainkey.lc  | [valor que te da GHL]              | —
MX      | lc                  | [valor MX que te da GHL]           | 10
MX      | lc                  | [valor MX que te da GHL]           | 20
TXT     | _dmarc.lc           | v=DMARC1; p=none; rua=mailto:...   | —

```

Volver a GHL y darle **Verify Records**. Después de unos minutos todos deben salir ✅.

### **3. Configurar el encabezado del email**

En los 3 puntos junto al dominio verificado: **Email Header Settings**.

- **Nombre del remitente:** `Clínica Dental Sonrisa Perfecta`
- **Email del remitente:** `contacto@lc.clinicasonrisaperfecta.site`

> 💡 **Reputación del dominio:** GHL va "calentando" tu dominio conforme envías correos. Cada mil envíos subes de nivel. Esto se ve como una barra de progreso, no pases correos a volumen grande hasta que esté caliente.

### **4. Comprar número de teléfono**

Ir a **Settings → Phone Numbers → Add Phone Number**.

> ⚠️ **Importante:** GHL NO permite conectar un número que ya tengas (a menos que tengas una cuenta Twilio previa). Hay que comprar uno dentro de GHL. Eso es bueno porque además sirve para agentes de voz AI más adelante.

Al comprar, fíjate en los **íconos de capacidades** del número:

- 📞 Solo llamadas
- 💬 SMS
- 📱 MMS

Buscar por **código de área local** de tu clínica. En el caso (Cancún) empezamos con `998`. Tienes mejores probabilidades de que contesten con un número local.

> ⚠️ En México, desde hace poco los números con SMS ya no salen por defecto por cambios en la legislación. Si tu país tampoco los muestra, compra un número de Estados Unidos (≈$1.15 USD/mes) — funciona para SMS sin problemas, pero para llamadas de voz sí conviene uno local.

### **5. Configurar WhatsApp Business**

Ir a **Settings → WhatsApp**. Por defecto cuesta ~$29.99/mes, pero si eres agencia puedes ajustarlo:

- Ir a tu cuenta de agencia → **Rebilling → WhatsApp**
- Cambiar el precio de reventa (ej: 10 USD)

![CleanShot 2026-04-24 at 10.03.45.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/440183e0b10949f1aaf57a2640c1209f5379153c9096419894947d1d45287b68.png)

De vuelta a la subcuenta: **Settings → WhatsApp → Subscribe**.

**Embedded Signup de Meta** — pasos:

1. Conectar con **Facebook Business** (usar tu portafolio comercial existente).
2. Crear o elegir un **Business Portfolio**.
3. Agregar un **número nuevo** (México, categoría: salud/dental).
4. Verificar por SMS/llamada.
5. GHL asigna un número temporal para probar (el número real requiere compra aparte y verificación de negocio).

> ⚠️ **WhatsApp inicia conversaciones solo con plantillas aprobadas por Meta.** Puedes responder a mensajes entrantes sin plantilla durante las 24 horas siguientes (ventana de sesión), pero para iniciar necesitas plantilla aprobada. La aprobación tarda entre minutos y 24-72 horas.

### **6. Prueba de los 3 canales**

Crear un contacto de prueba (puedes ser tú mismo con tu correo/teléfono):

**Email** — desde el contacto, click en email, escribir y enviar. Debe llegar a tu bandeja.

**SMS** — desde el contacto, click en SMS, escribir y enviar. Debe llegar a tu celular.

**WhatsApp** — dado que las plantillas tardan en aprobar, el truco es enviar **tú** primero un mensaje al número del negocio desde tu WhatsApp personal. Eso abre la ventana de 24h y GHL te deja responder libremente.

## **📎 Recursos**

### **📋 Plantilla — Convención de email dedicado**

```
Subdominio:     lc.tudominio.com
From email:     contacto@lc.tudominio.com
Nombre remite:  [Nombre del negocio]
```

## **⚠️ Troubleshooting común**

- **DNS no verifica:** puede tardar hasta 24h. Verifica que copiaste el valor exacto y sin espacios.
- **SMS no disponibles en tu país:** compra un número US de backup para SMS y usa tu número local solo para llamadas.
- **WhatsApp no deja enviar:** estás intentando iniciar conversación sin plantilla aprobada. O envía tú primero desde personal, o espera la aprobación.

## **✅ Checklist antes de avanzar a la Sección 4**

- [ ] Email dedicado con DNS verificado (TXT, CNAME, MX, DMARC)
- [ ] Encabezado de email configurado (from name + from email)
- [ ] Número de teléfono comprado con capacidad de SMS
- [ ] WhatsApp Business conectado vía Embedded Signup
- [ ] Prueba real de los 3 canales (email + SMS + WhatsApp)

## **➡️ Siguiente sección**

**Sección 4 — CRM: Contactos, Campos Personalizados & Smart Lists.** Vamos a crear los 6 pacientes que nos acompañarán durante todo el curso, agregar campos específicos de clínica dental (tipo de tratamiento, fecha de última visita, notas clínicas) y construir listas inteligentes que se actualizan solas.

## 🎙️ Transcripción

Muy bien, entonces en el último vídeo terminamos con la secuencia que ya la tenemos lista con el branding que nosotros creamos, pero no sirve tener un sistema bonito, si no puede comunicar, obviamente con los eh, clientes potenciales o con los pacientes. no se ocupa tanto y sobre todo el whatsapp es lo que más se ocupa para comunicar. Entonces vamos a hacer una prueba al final de cada canal para que veamos cómo funciona ni que todo esté bien y en ese punto yo sé que quiere decir directa construir el emburdo a las automatizaciones pero si no tienen los canales configurados cuando llegues a las automatizaciones no vas a poder enviar nada como cable a la electricidad antes de poner los focus entonces vamos a empezar primero por el correo. Para el correo tienes dos formas de confiar. Cada persona puede tener su correo o pues tener aparte un correo para toda la cuenta que todos utilicen. Entonces vamos a ir aquí a configuración y nos vamos a ir a email service. Sando aquí lo que va a ser GCL es que nos va a decir que nos recomiendo utilizar un subdomínio y obviamente que hagamos todos estos registros para poder mejorar, digamos, que nuestros correos no lleguen a spam, pasarle a crear domine dedicado y vamos a mandarles muy común utilizar lc en coge el euro y os recomiendo que se queden con eso, si el lc punto dice el dominio que compramos, en este caso es clínica son risa, clínica son risa perfecta porque no se sería línica, y vamos a confirmar que esté bien, y ni ya no son risos, vamos a copiarlo para que no terminamos detalles, listo, vamos a dar la añadir y verificar, nos va a pedir como la vez pasada que agregaremos todo esto manualmente, así que primero esté, quiste, lc con tebalor, lo regresamos a jostinger, vamos a la parte de añadir record, que quiste es LSE, porque es el sub-bomín y los dos poquimos, por valor, vamos a darle add-recors, y después nos dice que estexte con valor y es el sub-serbido. Nos vamos para acá, otra vez estexte con valor y con pasar la añadir record. Nos regresamos, ahora va a ser un cmail, in-name y que vamos a añadir. Después de un mx con lc, mx con lc, aquí vamos a hacer una speed de alguna prioridad, no nos pide, entonces vamos a hacerla que nos dé por defecto. Otro mx con esto y confundimos que se igualen lc y añade. Y agregamos todo lo que nos pide, vamos a darle verificar registros. Recuerda que esto puede tardar unos minutos. Se fijan aquí, ya no sale verificado, verificado, verificado, verificado. Y de nuevo, verificado porque es opcional, no lo sabía dado, pero yo os recomiendo que si hagan el DMARC, así que vamos a copiar esto, vamos a copiar esto, nos regresamos y vemos que es un TXT y le ponemos devalos, vamos a que nos vengan los espacios, te añadimos record, regresamos y vamos a darle en verificar el baño de nuevo y vemos que dice ese el emitido y pre-compartido activo calentemente en curso, esto que hace como para cada vez que envíes mil correos pasas al siguiente nivel, es como una forma de ver que vais calentando, no es como que ya estaba en desbloqueando en realidad, muy bien, lo siguiente sería darle aquí en los tres puntos, vamos a darle en configuración de encabezados, aquí vamos a poner el nombre que tenemos que salga, la sera clínica, un risa perfecta y el des de correo electrónico vamos a decir que sea contacto a roba lc que es nuestro subdominio en punto y es el clínica son risa perfecta a punto site, yo tengo el copiado, vamos a darle guardar, la forma en la que van a salir los correos y si nos vamos en configuración de dominio y aquí es como para conectar el calendario, los pagos porque si es 100 por ciento puedes tener varios dominio y conversación 1 o 1 por el trónico masivo para las campañas los flujos de trabajo son las automatizaciones y eso sería como para acá y regresamos aquí hacia atrás y dice el listo se está conectado y vamos a ver nada más de ti confirmar esto, pero si no respuestas a rendear, si no rende o no ni estamos, se respuesta muy bien. Lo siguiente va a ser el número de teléfono para llamadas y mensajes. Una de las cosas que tenemos que considerar es que lamentablemente GHD no permite integrar un número de teléfono que tú ya tengas actualmente. A que compro un número de teléfono con ellos, a menos de que tengas un teléfono con tuilio, entonces si lo puedes traer, pero no me lo he recomendado, por que en caso quieras usar sus ascentes de voz, el cero número de ayes. Entonces en caso vamos a comprar un número, vamos a la añadir número, todo esto va a depender 100% de el país en el que encuentres, hasta el añadir número de teléfono, y en caso tú puedes comprar de varios países, aunque no estés ahí, y obviamente siempre lo mejor es comprar directamente en tu tu país y no probablemente la gente no te vaya con estar verdad perfecto algo que tengas que tiene que tomar en cuenta es que aquí te hice las capacidades de tu teléfono todos estos que estoy viendo es el precio mensual 6 dólares con 25 centavos todo es esto que dice aquí capacidades solo está icono del teléfono quiere decir que el teléfono solo está disponible para hacer llamas no puedes mandarme esas texturas también si hacen filtrar, tú puedes buscar por números de teléfono, por ejemplo la helada de caso cancunes 98, así que si yo pongo que quiero que salga esto en la primera parte del número, me va a buscar teléfonos que empiecen con 998, si es que están disponibles, si acaso no hay, entonces pues puse 998, cuatro, vamos a dar otra vez 998, y a ver si por ejemplo ven cancun quitan la roca, cancun quitan en la roca y en la roca. Por si aquí es donde estáis tu clínica o donde va a estar tu empresa, tienes mejores posibilidades de que te contesten si tienes un número local, verdad? Tienes embargo, todos esos números son las mentes son para llamadas de vos. Caba aclarar que para configurar un WhatsApp que vamos a ver más adelante, tampoco supuso a este número ni estarías conectar tu WhatsApp de manera regular o comprar un número de WhatsApp. En caso el nuevo hecho no está disponible mensajes, así que vamos a restarles a los filtros y vamos a ver todos me están dando por los toll free los a 30 dólares y ninguno me dio por mensaje que vamos a darla actualizar porque va a depender mucho el país pero yo he visto que en México están disponibles mensajes de texto no sé por qué esta vez no me están saliendo, todo va a depender de lo que el país en el que estés, por ejemplo si usamos Chile aquí si no sale por defecto los mensajes de text, hace poco en mi país en México una legislación y cambiaron los, como se manejan los números de teléfono así que no soy esa por eso, vamos a ver si usamos argentina y uno está un poco más caros y solamente a vos, así que regresamos a México y en caso no vamos a poder configurar lo que es los mensajes de texto, pero no pasa nada, vas a coger 9.8, en la primera parte aplicamos y compramos el cancún, vamos a darles por ser la compra, es lo que les dije que había cambiado, nos pide una dirección, vamos a ver la idea de dirección, en Estados Unidos y Canadá no es necesaria crear, tu negocio, dirección a tu nombre de teléfono para verificación local, te voy a enviar el certificado obligatorio para cumplir con las reglas de nombres de teléfonos de conformidad, a ver que me pide aquí, nos vamos a poner aquí una dirección real y mejor si no lo acepta, muy bien, regresamos para acá, en la idea de dirección, tenemos la dirección añadida, validada, así que muy probablemente ni hacemos refrescar esto, para que nos aparezcan, o sea, también que repetimos el proceso de Nierenu, cogemos México y entrábamos 9.8 al principio, un alcancum, procedamos con el pago, y nos sale esto, vamos a recluse el pago, ese es una identificación de negocios y todo eso, y evidentemente nos lo vamos a hacer, así que vamos a comprar un número de Estados Unidos, que es mucho más barato, y a mente para que se le preva y con usted lo vayan a comprar para su negocio y para un cliente se suba su documentación para la proceder a la compra y me pide qué verificar la identidad voy a decirlo en el caso estoy en México de confirmar y vamos a subir mi pasaporte y lo va a dar continuando otro dispositivo y ahorita regresamos. Ok, ya estamos verificados, ya podemos proceder con la compra y al ser nombre de Estados Unidos que podemos usar en mensajes de texto en las cascaciones que tenemos en lados peobligatorio, que sí que nos tenemos que registrar a dos pay y tienes que mandar igual de un número de negocios y eso, por eso la verdad es un poquito de un gorroso y lo he hecho hora de vez para cuentas de Canadá y no es sencillo pero lleva su tiempo, ya tenemos el correo, ya tenemos esto y por último vamos a darle whatsapp, aquí me está cobrando 29 y 99 porque es lo que viene por defecto para la cuenta, así que vamos a cambiar esto y ahorita regreso. Esto mejor se les enseguen, si usted lo aquí hayan cambiado, te van aquí a su agencia, si usted tiene la cuenta de agencia, te van donde dice reventa y van a buscar aquí whatsapp y aquí le van a poner el valor en el caso de 10 dólares, así que en ningún beneficio, en ningún precio reventa, ya vimos guardar, así que ya nos pongo a regresar a la cuenta de clínica mental, nos podemos ir a configuración whatsapp, y ya nos sale a 10. Vamos a darle pagar y suscribirse y lo voy a decir que se cobra la agencia, en caso ustedes tienen una cuenta de un cliente con su y por lo que esa es su cuenta, digamos de cliente, obviamente que los clientes paguen directamente, aquí lo voy a decir que sí, porque ya tengo la está agregada aquí, no tiene que procesar, sino asegúrense que ustedes desayun con esa parte o desde la cuenta de la agencia configurando que se les obre a ellos directamente. Vamos para que se processe el listo. Ok, ahora dice cuarenta suplicación de WhatsApp Business con coexistencia. Es algo muy muy de DHL que tiene coexistencia, que era una nueva cuenta empresa de WhatsApp o migradas de un BSP Business oration Provide Existencia. ¿Qué es esto? Foy Cloud en otra cuenta DHL como Menichad, etc. En caso, voy a crear yo un número nuevo, voy a comprar un número acá. Y si es pleno, esa es un número de teléfono personal para el lápido WhatsApp Business, pero no debe venir a un número WhatsApp personal, no lo necesito, política más aggerida, historial de chats, vamos a conectarse con Facebook. Tío sí, debido a que utiliza cuenta de Facebook, utiliza lo que es un portafero comercial. Entonces, en caso voy a usar uno y lo que yo tengo para no tener que crear ahorita uno. en el supuesto ustedes dan a que escoger el portafelo comercial suyo o de su cliente y aquí vamos, ya tengo un número asignado que no voy a ocupar, entonces pues sí que crear uno nuevo, la oar siguiente y aquí vamos a ponerle dínica, un risa perfecta, mi categoría, a ver si tenemos listas, país México, esa perciosa sí que tengan una página Network y la siguiente. Al añadir un nuevo número, en ese caso que sea de México, y vamos a hacerlo sin número de teléfono ahorita para no tener que comprar todo. Vamos a ver aquí, siguiente. Y quisieran ustedes entonces tendrían que hacer el proceso de comprar un número de teléfono real para conectarlo, cosa que no voy a hacer ahorita por lo mismo que le decía de todo el proceso de comprar un número de teléfono, pero déjame ver esta antes. Y aquí se nos van a pedir verificar, o sea, darle un número de teléfono real para poder hacer una compra. Vamos a darme por acá y esta forma desde fue ya conectada, que nos podamos mandarme. Sí, me dice que confirme, esto puede tomar unos minutos, así que voy a poner pausa de regreso. Ok, me dice que ya quedo listo, vamos a darle continuación, es un número que me asignaron de manera interine, a mandar a mi guava, el número que se asignó, me dice que es el código QR, la cuenta whatsapp business, etcétera, vamos a dejarla aquí y de esta parte y regresamos a Goja Level, terminamos esta, regresamos, puedo en esta, ok whatsapp, es el número de teléfono, con qué dice país, Estados Unidos, sonetados, un beso perfecta, el número de teléfono, para confirmar algo, en 15 números, o crear anuncio, y el número no está verificado en negocio evidentemente aquí pueden dar dos desplantillas para crearlo bien recuerden cuando tengan que iniciar la conversación es viajplantillas. Entonces vamos a regresar, vamos a añadir un contacto de prueba, obviamente para hacer las pruebas, vamos a agregar contacto, me voy a agregar a mí por el electrónico, tengo un lit, un horario, que te compone y guarda perfecto. Entonces ya que estoy aquí con el contacto desde aquí le puedo mandar un mensaje texto y hola por la probando. Le puedo dar un correo el trónico, por rudo prueba, por la probando. Por rudo de DJ, sí. Tal enviar. Y si me voy a WhatsApp, no va a dejar porque no inicia de yo el mensaje, tendré a través de una plantilla, lo cual no teníamos lo que no nos ha dado data. Así que lo que yo voy a hacer es que voy a enviar primero un mensaje de WhatsApp para que me aparezca acá y yo puedo dar un segundo en lo que me doy de alta como bien contacto. Listo, me mandé un mensaje, hola, me da sin formes y como pueden ver aquí, ya me dejes escribir porque ya inicié yo, o inicié en esa suelcidente, la conversación, entonces tenemos entre 4 en que tenemos 24 horas para comunicarnos ahí decía viado con las tardadas dos palomitas y a mi buena notificación de que ya me llegó el mensaje. Entonces es muy bien en este caso tenemos los canales conectados la clínica de puedo hablar con sus pacientes por email, por teléfono, por whatsapp y mensaje de texto y ya podemos hacer las automationes que ese sistema. Entonces en la siguiente selección vamos a crear otros contactos de prueba, vamos a ver los campos personalizados y las listas inteligentes. Nos vamos en la siguiente inflexión.
