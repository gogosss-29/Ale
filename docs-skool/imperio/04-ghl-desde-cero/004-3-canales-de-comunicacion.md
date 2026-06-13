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
