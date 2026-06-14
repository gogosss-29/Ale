# 🎥 [PASO 1] Cómo instalar n8n en tu VPS

> Ruta: Automatizaciones n8n › 🎥 [PASO 1] Cómo instalar n8n en tu VPS

**🎬 Vídeo (11.4 min):** https://youtu.be/EFcGuhY8XWk?si=XnH6vah1JCLMTBG6

---

Imperiales, hoy les traigo el paso a paso definitivo para montar su propia instalación de n8n en un servidor VPS **en 5 minutos.**

Seamos sinceros: la versión Cloud de n8n es genial para probar, pero $24 USD al mes por solo 2,500 ejecuciones es un límite que se queda corto muy rápido. La forma real, escalable y "cool" de hacerlo es teniendo **tu propio servidor**.

No solo es hasta un 70% más económico, sino que te da control total para lo que se viene (como conectar Evolution API para nuestros Agentes de WhatsApp).

**📌 ¿Qué vas a tener al final de este tutorial?**

- Un **VPS KVM 2** en Hostinger optimizado.
- **n8n instalado** automáticamente (sin pelear con código desde cero).
- **100 Workflows** pre-cargados listos para usar.
- Tu propio **dominio profesional** (tipo `n8n.tudominio.com`).
- La infraestructura lista para el **Curso de **[**Agentes de WhatsApp**](https://www.skool.com/imperio-digital/classroom/b8e3a86b?md=f7ffc3a3b7c34798844e3285a0cb4548).

---

### **🔧 Paso 1. Elegir el VPS correcto**

Para correr automatizaciones y agentes que se vean increíbles, necesitamos un buen motor. En el video usamos Hostinger por la facilidad de su plantilla pre-instalada (y ya que tienen un plan de afiliados, aunque igual los usaba de antes).

1. Entra a [**hostinger.com/benjamin10**](https://www.google.com/search?q=https://hostinger.com/benjamin10&authuser=1).
2. Elige el plan **KVM 2**. - *Pro tip:* El KVM 1 se queda corto de RAM y el 4 es demasiado para empezar. El 2 es el punto dulce.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9e5ad7e8849f44d99fce1a205adb22e3ac8b651c201e413cbb9e7e3a8fe344cb-md.png)

1. Selecciona el periodo (recomendado 24 meses para olvidarte del tema).
2. Si te fuiste por los 24 meses, y nos quieres ayudar, usa el cupón `BENJAMIN10` para un 10% extra de descuento.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4b17c9b1814343b1957988ab05fd3e8d355d2024089b41c087524d848e4c4113.png)

**⚠️ MUY IMPORTANTE:** Al configurar el servidor, en la sección de Sistema Operativo, elige la opción **"Application"** y busca **"Ubuntu with n8n" o "n8n + 100 workflows"**. Esto te ahorrará horas de instalación manual de Docker.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/96e6a61f45764b08ba74781d01eaf7f336128df10efe4edb9ec293b9b11ff335.png)

---

### **🖥️ Paso 2. Configuración inicial y Licencia**

Una vez que el VPS se termine de instalar:

1. Desde el panel de Hostinger, dale a **"Administrar aplicación"**.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/316be6a6680542fc9ad3ff91c8c3973d947e4da2c8eb4e07b542335accfcf448-md.png)

1. Crea tu cuenta de administrador (correo y contraseña).
2. **Activa la licencia:** Aunque es self-hosted, n8n pide un registro gratuito para desbloquear ciertas funciones. Te llegará un correo, copias la *License Key* y la pegas en *Settings > Usage and Plan*.

Listo! Ya tienes n8n corriendo con 100 plantillas preinstaladas.

---

### **🌐 Paso 3 (OPCIONAL). Conectar tu Dominio Propio (Adiós IP fea)**

No queremos entrar a `http://https://n8n.srv1169942.hstgr.cloud/home/workflows`. Queremos algo profesional como `n8n.tuagencia.com`.

Para esto, hay que hacer dos cosas: apuntar el dominio al VPS y configurar n8n para que reconozca ese dominio.

**1. Apuntar el dominio al VPS:** Debes configurar los registros DNS (tipo A) para que tu dominio redirija a la IP de tu nuevo servidor. 

👉 **Guía oficial:** [Cómo apuntar un dominio a tu VPS en Hostinger](https://www.hostinger.com/support/1583227-how-to-point-a-domain-to-your-vps-at-hostinger/)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d8af22f98cb6485486bf639f18fcb57c845b2417a52d4f14b27d1004ab8db5c7-md.png)

**2. Cambiar la configuración interna de n8n:** Una vez apuntado el dominio, debemos decirle a n8n (a través de la terminal del navegador) que use ese nuevo nombre. 

👉 **Guía oficial:** [Cómo cambiar el dominio de n8n en tu VPS](https://www.hostinger.com/support/11927159-changing-the-domain-for-n8n-on-vps-at-hostinger/)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8ff43d9f428a428bae5da9ce5735bfa8907bd71da5414738aa5c812fc4fda9ce-md.png)

*Nota: La certificación SSL (el candadito seguro HTTPS) se generará automáticamente, pero puede tardar unos minutos u horas en propagarse. Paciencia.*

---

### **🔄 Paso 4. Mantenimiento: Cómo actualizar n8n**

A diferencia del Cloud, aquí tú eres el dueño del servidor, por lo que n8n no se actualiza solo. Pero no te preocupes, Hostinger lo hace muy fácil usando la "Browser Terminal".

Cuando salga una nueva versión con features que quieras probar, sigue estos pasos: 👉 **Guía oficial:** [Cómo actualizar n8n en Hostinger](https://www.hostinger.com/support/11767754-how-to-update-n8n-at-hostinger/)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3aae6c1a12884fb08eb4aa5c67bcab284a040526fb064250b08e5869a62f6929-md.png)

### **🚀 ¿Por qué hicimos todo esto?**

Porque para jugar en las grandes ligas de la IA, necesitas infraestructura propia.

Este servidor es la base fundamental para lo que estamos viendo en el** Curso de Agentes de WhatsApp**, donde conectamos n8n con Evolution API para crear asistentes de IA reales y potentes para negocios.

Si ya tienes tu servidor listo, el siguiente paso es ir directo al curso y empezar a montar tu agente:

👉 **Ir al Curso de Agentes de WhatsApp + Plantilla Oficial**

¡A construir Imperiales!

## 🎙️ Transcripción

Existen varias formas de instalar N8N para correr tus automatizaciones, pero hay solamente una que es realmente cool. Y ese es exactamente el método que te voy a mostrar ahora. Porque para correr automatizaciones o agentes que se vean así de cool y así de increíbles y así de completos, necesitamos hacer un paso antes que es instalar N8N. Y aquí tenemos dos principales grandes opciones. La primera es pagar el cloud de N8N, que realmente nadie lo hace porque es extremadamente caro. Como podemos ver acá son $24 al mes y tenemos 2,500 ejecuciones y lo que todos hacen es correr o levantar N8N en su propio servidor, que es hasta un 70% más económico y es mucho más cool porque podemos decir, "Bueno, yo tengo mis propios servidores, que también es bastante interesante. Además, en los mismos servidores podemos levantar un BPS para correr no solo N8N, sino otros entornos como Evolution Appi, para conectar WhatsApp, etcétera. Y ahora te voy a mostrar cómo hacerlo paso a paso. Así que si sigues esto para el final de este video, vas a tener tu propio servidor corriendo. Lo que vamos a hacer para correr N8N va a ser entrar a hostinger.com/benjamín 10. Y siendo completamente transparente, sí, este código va a hacer que me llegue dinero extra, pero al mismo tiempo te va a dar a ti un 10% de descuento. Entonces, vamos a entrar a Hostinger y aquí es donde vamos a correr nuestro N8N para que te quede algo así de lindo como n8 imperiodigital.cloud. Una vez que estemos aquí adentro vamos a bajar y vamos a elegir qué KBM queremos usar. Aquí puedes usar literalmente el que quieras. Yo en lo personal recomiendo el KBM2 porque cualquier cosa sobre eso ya va a ser un poco mucho. Y el KBM puedes llegar a quedar corto. No creo que ocurra, pero el KBM2 a mí en lo personal me funciona bastante bien. Le vas a dar a elegir plan. Y si eres algo como yo y te gusta pagar una vez y después olvidarte para siempre, vas a elegir el plan de 24 meses, que también es el mejor con el más convenio. En cupones vamos a poner el código Benjamín 10. Vamos a aplicarlo. Te va a hacer un 10% de descuento adicional si es que entraste con el link. Vamos a elegir la ubicación del servidor. Y esta parte es importante porque aquí vamos a instalar N8N con 100 workflows de prueba. Vamos a apretarlo, vamos a darle confirmar y le vamos a dar a continuar. Vamos a ingresar con nuestra cuenta y una vez que hiciste el pago, le das a siguiente. Vamos a crear una contraseña. Le damos siguiente. Escaner de malware. Okay. Y se va a comenzar a configurar nuestro VPS. Y mientras carga, quizás te estás preguntando, bueno, ¿qué es un VPS? Un VPS es un Virtual Private Server, es decir, es un computador que está siendo instalado en los servidores, en este caso específicos. Dentro de estos VPS generalmente se corren o se ejecutan ciertos software o OS como Docker, como Easy Panel, etcétera. Lo que vamos a hacer ahora es vamos a hacer la instalación guiada de N8N con Ubunt y lo más cool es que va a venir con los 100 workflows ya preinstalados para que entres a jugar de una y después de un par de minutos nos va a aparecer algo así. Lo que vamos a hacer ahora es vamos a irnos a administrar aplicación y aquí vamos a empezar a crear nuestra cuenta N8N. Vamos a elegir cualquier correo, llenamos nuestros datos y le damos a siguiente. Luego nos va a dar la opción de que nos manden una licencia a nuestro correo para desbloquear ciertas cosas en específico. Creo que es una muy buena estrategia para hacer también un whel list a la lista de correos en específico. Y vamos a entrar a Gmail, vamos a abrir nuestro correo, vamos a copiar la licencia, volvemos a usage and plan, que lo puedes encontrar bajo settings usage and plan. Enter activation key, copias y activas. Después vuelves atrás y listo, ya tienes N8N funcionando con este link en específico que aparece arriba. Podemos ya empezar a crear nuestras propias automatizaciones, nuestros propios agentes, haciendo las conexiones, etcétera. Y ahora, si es que entramos a este link en específico que aparece aquí arriba, vamos a ver que tenemos ya los 100 templates o las 100 plantillas instaladas. Realmente interesante. Después, si es que volvemos a Hostinger, podemos entrar acá y nos encontramos con nuestro panel. Si es que te vas a BPS, vas a poder administrar las cosas en específico acá de tu BPS. Ahora recordemos que esto está instalado en un computador, en un servidor en específico y estamos corriendo un programa, por lo que no se va a actualizar siempre de manera sola. Lo que debes hacer para actualizarlo es justamente y lo que te saldrá aquí arriba es cómo actualizar N8N. Y esto es realmente así de sencillo. Si es que quieres hacerlo, abres esto y te vas acá, browser terminal, mandas este comando, luego este y luego este. Es decir, abro el terminal, copio lo que me sale acá, pego lo que me sale acá y le doy enter. Luego voy acá, Docker Compose down, enter y Docker Compose upd y le das nuevamente a enter. Y listo. Es así de simple, no hay nada más que hacer. Ahora quizás te estás preguntando, y este es un pequeño bonus, Benja, ¿cómo hiciste para que se vea así de cool? Arriba tu página de N8N cuando entras a n.impimeriodigital.cloud. ¿Por qué yo tengo que estar con estos server flash, flash, flash, flash? Y te voy a mostrar rápidamente también cómo hacemos eso. Si es que volvemos a nuestra página de hostinger, vamos a dar una opción que sale acá, cambiar dominio para N8N. Basta solamente conseguir esas instrucciones. Nuevamente te vas a ir al terminal y vuelves acá. pides el environment que es nano. Y lo que tienes que hacer aquí arriba es justamente cambiarle esto que sale domain name, si mal no recuerdo, ¿verdad? Que ahora es hostinger.cloudsrb, no sé qué, no sé qué, no sé qué. Y tienes que ponerle tu propio dominio. Mi recomendación es compra el mismo dominio dentro de Hostinger, porque hace que sea muy muy simple el hacerlo. Entonces, nos vamos acá, nos vamos a los dominios, obtener un nuevo dominio, te vas aquí y pones Benja es el mejor punto cloud. Le vas a añadir al carrito, continúas en el carrito, compras Benjas elmejor.Cloud y lo pagas. Luego tienes que verificar tu mail. Tu email ha sido verificado. Te vas a los DNS, name servers. Y aquí podemos verificar que el dominio ya está activo y en nuestra posesión. Lo que tenemos que hacer ahora es reapuntarlo a nuestro BPS. Para eso iremos a VPS, copiamos el IP, abrimos dominios, abrimos el nombre del dominio, vamos a DNS o Name servers y nos van a aparecer todas estas cosas que están acá. Y simplemente tenemos que borrar todos los que sean A, C name y a a. Entonces, todos los que son A. Le vamos a borrar C name que tiene wwior y listo. Ahora recuerdan que antes copiamos lo que nos salía acá, que era nuestro IP del BPS. Vamos a irnos a dominios nuevamente, donde estábamos recién, los DNS donde mismo estábamos y vamos a apuntarlos a este dominio en específico. ¿Okay? Esto nuevamente lo pueden encontrar justamente acá y nos están pidiendo que mandemos un a record específico con A. Entonces a record con acá agregar registro y el segundo es a record, es decir, con este y lo vamos a mandar a el mismo de antes. Agregar registro. Añadir registro adicional. Ya existe, le vamos a confirmar. Ahora sí, vamos a volver al terminal anterior donde nos habíamos quedado, es decir, acá openminal. Y vamos a poner el dominio que acabamos de comprar, que vendría siendo Benja es el mejor punto cloud. Solo para verificar si es que este era nuestro dominio. Voy a irme a dominios. Portafolio de dominios. Benja es el mejor. Cloud. Y eso es exactamente lo que vamos a poner aquí. Después le vamos a dar a control X y le vamos a dar a Y enter. Después vamos a reiniciar. Docker compost down, Docker Compose up. Y después de haber esperado unos minutos, ya pudemos entrar al dominio. Nota que le agregué uno más, un type [música] A que es n.7216 que vendría siendo este acá N8N. Y después le pegué en mi bps en específico. Y ahora si es que llego y entro acá, voy a entrar a nn. Benja es el mejor cloud. Voy a dar a enter y debería entrar directamente a mi servidor de VPS de N8N. Después vamos a entrar con el correo que nos registramos, la clave que pusimos y listo. Ahora tenemos ya el dominio listo. Entonces, en vez de que nos aparecía ese feo antes que era el BPS srb, ahora nos aparece un hermoso, hermoso N8N. Benja es el mejor. Cloud. Ahora quizás te estás preguntando, bueno, ¿por qué no ha aparecido esto en específico? Bueno, porque la certificación SSL se demora un poco y no quería esperarla en este video, pero si es que entras, por ejemplo, acá a N8N Imperio Digital Cloud, que es el original, vas a ver que sí cuenta con esta certificación. Así que si, simplemente esperamos unos minutos más, a veces puede ser unas horas y la certificación de SSL se va a hacer de manera automática, como se me hizo aquí en la de Imperio. Okay, entonces ahora estoy en Benjas elmejorcloud. Vamos a irnos a crear un workflow, por ejemplo, aquí podemos ver que ya desaparece esta parte y podemos empezar a crear nuestras automatizaciones en N8N para fines prácticos. Por ejemplo, voy a entrar al school de Imperio Digital, voy a irme al nuevo curso que lanzábamos de agentes de WhatsApp, voy a bajar y me voy a descargar la plantilla del agente de WhatsApp. Y si quisiera implementarla, simplemente apretaría los tres puntitos, importar desde archivo, importar plantilla agente de WhatsApp y después simplemente empiezas a cambiar las credenciales en específico, conectas la credencial en los módulos que lo requieren y listo, ya tienes tu propio servidor de N8N corriendo y listo para empezar a crear automatizaciones, porque sí, podríamos irnos por la versión sencilla en la que pagamos un ojo de la cara en específico por correrlo en el cloud y que estamos limitados. en la cantidad de ejecuciones que podemos hacer o podemos hacerlo de la manera cool y [música] tener nuestro propio servidor. De más está decir que si me quieren apoyar de alguna manera, pueden entrar con hostinger.com/benjamin10. El link va a estar abajo también de este video. Y en el checkout, si es que quieren que se les aplique ese 10% de descuento, van a poner Benjamín 10. Este código solamente lo pueden poner si es que entran con el link de arriba. En el fondo tampoco es tanto, pero un 10% sobre el plan de 2 años vendría siendo algo así como $16 que te puedes ahorrar solamente por poner un código y además así también me llega algo a mí, así que realmente todos ganamos. Y otra de las razones por las que me gusta este host en específico es porque, por ejemplo, aquí en el curso de WhatsApp vas a ver que si queremos levantar un buen agente, porque a ver, seamos sinceros, hay agentes y agentes, si queremos levantar un buen agente de WhatsApp vamos a tener que usar alguna herramienta como Evolution App. Evolution API nos permite conectar directamente WhatsApp Business AN8N. Y aquí tenemos un tutorial del gran Carlos que nos ayudó a conectar este servidor y levantar nuestros propios servidores también en Hostinger. Entonces, mi recomendación es trabajemos con un servidor que unifique todo porque así no te tienes que acordar de 1000 contraseñas y seamos sinceros, es mucho más cool si es que decimos, "Mira, no, yo levanté mis propios servidores" cuando le dices a los clientes. Ahora sí, sin más que decir, espero que este video de acá te haya servido. Y Pich obligatorio, si quieres aprender de automatizaciones e inteligencia artificial, recomiendo que entres a Imperio Digital, porque tenemos un montón de plantillas listas para importar y aprender en conjunto, además de tener cuatro sesiones en vivo donde puedes resolver tus problemas, ir aprendiendo y, en fin, link Imperio Digital también está en la descripción. Y ahora sí, sin más que decir, te deseo mucho éxito y ojalá esto te haya servido.
