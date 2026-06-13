# [Curso] 🚀 Instalación en VPS con Hostinger

> Ruta: 🦞 Reto Imperial OpenClaw › [Curso] 🚀 Instalación en VPS con Hostinger

**🎬 Vídeo (17.8 min):** https://www.loom.com/share/426a6b039fec4b8a8331885dd4ec0a7f

---

## 🎯 Objetivo

Instalar OpenClaw **correctamente**, desde consola, en un VPS limpio, siguiendo **buenas prácticas de seguridad**.  
Nada de instalaciones preconfiguradas. Nada de correr agentes como root.

## 🧠 Contexto rápido (importante)

OpenClaw ha tenido varias etapas:

- ClawdBot
- MoltBot
- OpenClaw (versión actual)

En este curso **usaremos OpenClaw**, instalado manualmente en un VPS con **Hostinger**, usando **Ubuntu LTS**.

## 🧩 Qué vamos a cubrir

- Contratación del VPS correcto en Hostinger
- Elección del sistema operativo
- Acceso por SSH
- Buenas prácticas iniciales de seguridad
- Creación de usuario dedicado para OpenClaw
- Instalación oficial de OpenClaw

## 🖥️ Paso 1. Contratar un VPS en Hostinger

### Recomendación de plan

- **Plan recomendado**: KVM2
- Más que suficiente para OpenClaw
- Escalable más adelante

📌 Ubicación recomendada:

- Elige el país **más cercano a ti**

![CleanShot 2026-02-06 at 15.30.05.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/eb6183e423da42c5a0c0f7cbc116c71f8f81755b20284d1996c5e41068c95942-md.png)

### Sistema operativo

- Elegir **Ubuntu**
- Versión recomendada: **Ubuntu 24.04 LTS**

> Siempre usa LTS. Son versiones estables, probadas y menos problemáticas.

## 🔐 Paso 2. Crear contraseña root y finalizar setup

- Hostinger te pedirá crear un **password root**
- Usa un **password manager**
- Guarda este password. Lo vas a necesitar

Opciones adicionales:

- SSH Key: **NO por ahora**
- Malware scanner: opcional
- Docker Manager: **NO necesario para este tutorial**

Finaliza el setup y espera a que el VPS se configure (2–3 minutos).

### 🌐 Paso 3. Acceder al VPS por SSH

Desde el panel de Hostinger:

- Copia el comando SSH que te proporcionan

Ejemplo genérico:

```
ssh root@TU_IP_DEL_SERVIDOR

```

### Primer acceso

Al conectarte:

- Te preguntará si confías en el servidor
- Escribe `yes` y presiona Enter
- Luego pega la **contraseña root** (no se verá al escribir)

> Es normal. Las contraseñas no se muestran en terminal.

---

## 🚨 PARÉNTESIS DE SEGURIDAD (MUY IMPORTANTE)

❌ **NO instales OpenClaw como root**  
❌ **NO ejecutes agentes como root**

¿Por qué?

- Root tiene control total del servidor
- Si algo sale mal, comprometes TODO el VPS
- Es una pésima práctica de seguridad

✔️ Solución correcta:

- Crear un **usuario dedicado solo para OpenClaw**

## 👤 Paso 4. Crear usuario dedicado para OpenClaw

Ejecuta este comando **estando como root**:

```
adduser openclaw

```

### 🔑 Configuración del nuevo usuario

- Crea una contraseña **diferente** a la de root
- Usa un password fuerte
- El resto de los campos son opcionales

## 🛂 Paso 5. Dar permisos sudo al nuevo usuario

Ejecuta:

```
usermod -aG sudo openclaw

```

Esto permite que el usuario:

- Use `sudo`
- Instale software
- Administre servicios  
Sin ser root directamente.

## 🔄 Paso 6. Cambiar al usuario OpenClaw

Ahora cambia de usuario:

```
su - openclaw (o como lo hayan llamado)

```

Si todo salió bien, verás algo como:

```
openclaw@tu-servidor:~$

```

✔️ Ahora sí estamos en un entorno seguro.

![CleanShot 2026-02-06 at 15.33.39.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/383459cac5fc430ba657b7ab81493eb7a2b57df983144264a471583fcf018ed1)

## 📦 Paso 7. Instalar OpenClaw (forma correcta)

1. Ve **SIEMPRE** a la página oficial de OpenClaw
2. Copia el comando de instalación oficial

```
curl -fsSL https://clawd.bot/install.sh | bash

```

Ejecuta el comando **como el usuario openclaw**, NO como root.

### Durante la instalación

- Te pedirá la contraseña del usuario `openclaw`
- Descargará dependencias
- Instalará OpenClaw
- Lanzará el setup inicial

## ⚠️ Advertencia de seguridad de OpenClaw

Durante el setup verás advertencias como:

- Proyecto open source
- Software en beta
- Riesgos de seguridad
- Recomendación de auditorías frecuentes

Acepta conscientemente y continúa.

### Tipo de instalación

Cuando te pregunte:

- **Quick Start** ✅
- Manual ❌ (lo veremos más adelante)

## ✅ Resultado esperado al final de esta página

- VPS activo en Hostinger
- Usuario dedicado `openclaw`
- OpenClaw instalado correctamente
- Sin correr nada como root
- Base sólida y segura

## 🎙️ Transcripción

Muy bien, seguro que muchos de ustedes están esperando este, este video. Hoy vamos a ver cómo instalar OpenCloth en tu VPS usando Hostinger. Eh, seguramente habieron videos de venja donde les comentar que es OpenCloth, que en su momento cuando ves empezado se llamaba eh Cloudbot, luego cambió Moltbot por, creo que 10 segundos duro y luego finalmente a su última metamorfosis como el creador lo llama que es OpenClaw. Entonces hoy vamos a ver cómo instalar OpenClaw en un VPS con Hostinger, que es de las cosas que se recomienda. Vamos a ver también las mejores prácticas, vamos a ver también cuestiones de seguridad, cosas muy importante, primeras configuraciones, vamos a conectarlo con Telegram y vamos a platicar un poquito de cuál es mejor modelo para usar. Muchos dicen que antropic directamente utilizar opus 4.5 también últimamente se puso mucho de moda kimi 2.5 que lo tenemos aquí es de munchot y tiene su justamente algo que se llama kimi code que viene siendo con cifora cloud code pero pues esto obviamente representan otro gasto de $15 al mes. Si lo quieren probar la gente que la aprobado dice que es mucho mejor que cloud code obviamente este es un modelo chino pero bueno se lo dejo a ustedes a su criterio. Para este video nosotros vamos a ocupar directamente opus 4.5 de antropic y al final es bueno enseñar unos pequeños trucos para poder se arraras al 95% en su cuota de sus tokens y también como ser más eficientes, también me vamos a hablar muy por encima porque esto da para muchos vídeos, a ver si hacemos una serie, vamos a hablar muy por encima de lo que es el Harbit y quiere decir cuando tu clobot que tu generes, en este caso open oponclo tu bot como osea que tú que tú le vais a llamar, tenga un Harvey, tenga sus latidos que vas a, básicamente quiere decir sepa cuando va a trabajar, también tenemos los cronjobs que quiere decir que tú configuras con método cron que es como un código de cada cuanto tiempo quieres que se despierte, pues tenerlo dormido o tener los dormidos que puede haber múltiples agentes corriendo y puede ser que se desperta acá 15 minutos para que chiquese algo y se vuelva a dormir. Tú también puedes decir, no sé, en cada tarea que tú definas con un cronjob, puedes decir lo que esa tarea vas a revisar mi correo, a los huevos para revisar el correo en unistas ofus, evidentemente, no? Entonces puedes hacer lo que corre cojico. Entonces despierta, revisio tu correo, corre cojico, te mando un mensaje de telegram y se vuelva a dormir. Y si tú le pidas que vaya y que investigue o que realiza algo, pues entonces ya es cuando utilice opus o si tiene que hacer alguna trimisicación no tan extensiva o no que lleve mucho procedimiento pues puede utilizar zonet, etcétera. Entonces vamos a estar viendo eso y igual más adelante en otro video veremos cómo puedes tener diferentes agentes que es la potencia también de OpenClaw que puedas tener una gente de mejor lugar de agentes vamos a llamar la empleados, digamos que tú tienes tu emprendimiento o lo que sea que está haciendo y quieres tener un dentro de los dos empleados puedes tener como tres niveles el ejecutivo senior digamos el asistente y el director entonces tú puedes tener tu open-clote tu bot como se que le llames director que se va a encargar de administrar todo y digamos que vas a tener como que tu capa gerencial tu capa en medio, tus signos y puedes tener un gerente de desarrollo, pues tener un gerente de diseño, un gerente de finanzas y pues tener asistentes, asistentes de captura, asistentes de investigación, asistente de marketing. Entonces tú tienes tu bot principal que a tu director que le manda ordines a los gerentes y los gerentes de manda ordines a los asistentes y entre ellos se comunica. Entonces, es como que la mejor forma de usar OpenClock en este vídeo no lo vamos a hacer porque es mucho más avanzado, nos vamos a enfocar en la instalación, configuración, mejores prácticas de seguridad, conectarlo con Telegram y echarlo andar y dos bunos al final de cómo mejorar sus prompts y cómo ser más eficientes o en los tokens hasta 95%. Entonces vamos al vídeo. Ya que estamos aquí en la página no tenemos que hacer absolutamente nada aquí. Aquí te dice cómo lo puedes instalar, esto es muy fácil, no ahorita lo vamos a ver. Pero vamos a mejor directo a Hostinger. Aquí estoy en Google, voy a irme a Hostinger y vamos a contratar un VPS. Ahora, si ustedes se van aquí a Hostingers y se van a ser revicios y se van a BPS, se van a salir aquí cuáles son los VPSes, digamos que queremos el KBM2, que es el recomendado es más que suficiente para lo que tenemos que hacer en este momento, y o veinti, yo no tengo cuenta de Hostingers ahorita aquí, voy a crear una junto con ustedes, pero no me que les quieren enseñar bastante rápido es que aquí obviamente es para si quieren pagar 24 meses el periodo y te da 20 un descuento mucho, mucho mayor o 12 meses también hay un descuento acá pagando el 83 dólares o si lo quieren pagar 6, perdón, mes con mes, acá va saliendo en 10 dólares prácticamente. Y donde puedes agarrar aquí más cosas, pero bueno, vamos a enfocarnos en el principal. En este caso, yo voy a poner Estados Unidos y estoy en México es lo que me queda más cerca. Y lo que les quiero enseñar es que lo que sean aplicaciones, como muchos ya pueden haber visto en la comunidad, puede instalar en el 8N, con Warflow, etcétera, muchos lo han hecho. Pero aquí no hay dice nada de que está ya la actualizaron, dice OpenClub, que quiere decir que ya te permite ir a tener tu VPS directamente con OpenCloth preconfigurado. Yo a la persona en la mina me gusta contratar ningún VPS con una aplicación ya preconfigurada, siento que te limita mucho, yo prefiero hacerlo desde cero y lo que les voy a decir en este tutorial como hacerlo desde cero. Si ustedes quieren hacerlo directamente con OpenCloth porque no quieren meterse con sola adelante, pero me recomendar siempre es invérselo un poquito más de tiempo, investiga y sigue, básicamente, sigue este tutorial y lo vas a pasar a hacer desde consola. Entonces, vamos a elegir Plano Es, vamos a elegir Ubuntu, que es, si ya han visto mis videos de cómo confiar en 8N, Evolution App, etcétera, todo lo montamos sobre Ubuntu, con Easy Panel en este caso de Ubuntu, y te va a rojo el Prodefecto de la última versión, a mí siempre me gusta irme a las LTS, que son como que las versiones estables, digamos, que son las que ya tienen tiempo probando y corriendo, y en este caso vamos a elegir la 24.04 LTS, ok, vamos a darle confirmar. Vamos a ver, continuo, 9.99, está muy bien, y en este caso me va a pedir que me cree mi cuenta, la voy a poner pausa simplemente lo que creo la cuenta y regresa. Listo, ya creamos la cuenta, yo pade con PayPal, le me siempre me gusta pagar todo lo que hago en internet y en ese plataformas con PayPal está disponible, porque PayPal da mucha protección lo usual y fácilmente puedes meter reclamos de cualquier cargo que te hayan hecho. Aquí estamos crear un password root, a mí lo particular, cuando son password roots me gusta que me los ginei directamente de esas plataformas, obviamente lo va a generar el password y esto lo voy a gluriar para que no les apresca a ustedes, este password necesito yo copiarlo porque es importante que lo guarden en algún lugar seguro, si tienen algún administrador de contraseñas, usenlo porque la vamos a estar utilizando ese password a lo largo del proceso de instalación, muy bien, ya que lo guardaron, vamos a darle siguiente, ahorita no vamos a poner ninguna SSH key, vamos a dejar así como está, vamos a darle siguiente que si queremos el malware es free, vamos a darle en DockerManager, elaborando lo nistamos ahorita para para esto, así que vamos a darle finish setup y esto va a tardar unos minutitos, seguís aproximadamente de tres minutos en lo que configura todo el vpc, obviamente voy a poner cosa y nos vemos en la derecha que termine. Listo, ya terminó, ahora nos dice que tenemos de 2, podemos solamente conectar a un dominio para poder entrar a nuestro VPS, si ustedes tienen su hosting en algún lado, o inclusive con el mismo hosting, que hay mucho más fácil, si tiene algún dominio, en este caso vamos a copiar el root access o vamos a copiar el comando para entrar a olvidar root más bien, ese es nuestro IP del servidor y vamos a darle Manage PPS. Ya que estamos aquí, simplemente es una ecuación de marketing de Hostinger, lleno de luftes como lo necesiten, y listo, en este caso, No, no va a fecar, la verdad tengo que poner. Ok, la quiza nuestro detalle de nuestro VPS, así que, bueno, también, antes de que uno da en spraya, uso en la guía, la guía de Hosting elaboras bastante buena, si te sán tratados con algo, les puede despueda ayudar. Entonces ya que tenemos esto, vamos en este caso a nuestro terminal, yo estoy en Mac, si ambisos mis otros videos, yo utilizo Ghosty, me gusta mucho para la terminal, así que voy a darle simplemente pegar el comando que copie del panel de Hosting, vamos a darle Nos pide siempre por seguridad que este está detectando esta conexión, puede ser establecida la autenticidad de este servidor, si queremos continuar, si la damos que sí nos va a guardar esa en nuestra máquina, para y cada vez que oéramos entrar a este servidor, desde tu terminal tu máquina si no hemos limpiado nuestras creciales, lo va a detectar que ya confiamos, entonces voy a escribir jazz y lo doy otra vez antes, que me va a pedir la contraseña, tengan en cuenta que todas las contraseñas de un en este caso estamos en Ubuntu, no son visibles y tú ustedes se ponen escribir o pegan, no van a ver la contraseña, entonces sepan que es normal, no caran que algo está fallendo, simplemente por seguridad las contraseñas no aparecen en la terminal, entonces tengan eso en cuenta si ustedes se ponen aquí y le dan pegar a ese contraseñ en no van a beber absolutamente nada, no van a haber ninguna indicación de que están haciendo algo pero está funcionando, así que le denle control B para pegar y den un enter, en este caso ya me acepto la contraseñ y estoy adentro, ok, quiero hacer un paréntese aquí muy importante, normalmente todos los videos que tuve en internet los tutoriales te dicen, ok ya que estás aquí, vete a la página de directamente de OpenClose, copia este comando y vete a tu BPS y pegarlo. Por favor no hagan eso, repito no hagan eso, ¿por qué? Porque están instalando OpenClose en el servidor, en el usuario Ruth, perdón. ¿Qué quiere decir que van a tener la acceso al Ruth de su BPS? Pueden ver si sí está en el BPS, está en la nube, no pasa nada no es mi computadora de todas formas no es lo mejor por cuestión de de prácticas nunca dejen que una ya o un vota géntico trabaje en su usuario root, creer un nuevo usuario en específico para él, inclusive entre las buenas prácticas que vamos a hacer más adelante, la recomendación es crear un correo para él, crear un password manager como no sé, un password.com para él un tem acceso a sus passwords, si no le van a dar acceso a apiquís, generan apiquís que tengas solamente él y pongan en una expirión, así si por alguna razón alguien se inyecta algún malware o algún código malicioso y acceden a su servidor, las apiquís que tengan solos son para aquí, van a tener una expirión, no van a poder utilizarla o darle mal uso. Entonces, lo que vamos a hacer, vamos a crear un nuevo usuario en nuestro servidor Recuerden que estamos en Ubuntu. Como creamos un nuevo usuario, simplemente tenemos que disputar un comando muy cortito, que se va a llamar Add User, Spasio y el nombre aquí queramos. En este caso no va a afectar absolutamente para nada, simplemente el nombre que ustedes quieren, y o tal cual voy a poner OpenClow, quiero que así sea mi usuario y ya está, lo voy a dar entre. Muy bien, me va a pedir una contraseña para el usuario que acabamos de crear, entonces no otra cosa, por favor no vayan a poner la contraseña que utilizaron para su route del BPS, pongan una contraseña que ustedes quieran, utilicen algún generador de contraseñas que exista online o alguna contraseñan segura que no utilicen el otro sistema que hace una contraseña exclusiva para este usuario. Lo mismo no la van a ver, pues ya que la pegaron del unenter, te pide que la confirmes, la vuelven a pegar el anunenter y listo, creo completamente. Ok, ahora pide que pongan un nombre completo para el usuario que acaban de crear, volvamos a lo mismo, el nombre que ustedes pongan es 100% opcional, yo voy a simplemente usar lo mismo, Open Cloud, BPS, le voy a poner, le doy enter, un nombre o no listo nada, así que le puedo dar enter, word for, nada, enter, todo esto es opcional, y la información está correcta, sí, enter, perfecto. Entonces ya creamos un nuevo usuario en ese caso es OpenClow. ¿Qué es lo que tenemos que hacer? Vamos a darle permiso a usuario. Por favor no ejecuten, me gusta reitar eso porque son las dos temas de seguridad, no ejecuten el comando de instalarlo porque se fijan si vemos aquí, seguimos como root, ahorita únicamente creamos el usuario root, perdón el usuario OpenClow, pero no hemos hecho ese switch seguimos como root antes de hacer el switch que tenemos que hacer dale permisos a no usuario que acabamos de creer. Entonces vamos a darle User Mode, Deon RG, sudo y como lo llamamos OpenClue, le vas a darle Enter, listo. Todos estos comandos nos va a desarrollar obviamente en el post para que vayan viendo aquí debajo del video y ya aquí hicimos esto, ahora si vamos a hacer el cambio de usuario, su espacio de guiones pase OpenClose y si se fijan, aquí ya dice OpenClose a roba, entonces ya estamos en nuestro usuario OpenClose, entonces ya que estamos aquí, ahora si ya es seguro instalar como tal OpenClose, regresamos a la página oficial, recuerden que siempre el oficial, vamos a darle aquí donde dice copiar, nos regresamos, le damos pegar y le damos entre, perfecto, nos está pidiendo el password para OpenClote, que es el password que acabamos de crear, así que por favor no va a ir a poder de nuevo el password root, simplemente utilicen el password que claro, déjenme copiarlo aquí y lo tengo en otra pantalla, vamos a pegarlo y le damos en perfecto, estoy instalando todo, está descargando primero todo para después instalarlo, obviamente no tienen que entender nada de esto, simplemente esperen a que trabaje, cuando termine van a entrar automáticamente como un loan bordin en el que les van a pedir, les va a pedir o pinclo que configure ni que confirmen ciertas para metros o ciertas cosas. Vamos para que termine y ahorita regresa. Muy bien, nos estamos de vuelta, ya terminó, ya nos sale aquí que tenemos OpenClore, nos sale aquí una advertencia, como estamos tan alto el vídeo, esto está todavía en beta, esto es de código abierto, por lo cual muchas personas que están haciendo, animizando el código haciendo poco de ingeniería reversiva y viendo cómo funciona por puinyectar malware o por inyectar código maldicioso. Entonces de hecho aquí nos dice que es hagamos auditoría de seguridad constantemente y nos dice entiendo que es una herramienta muy poderosa y por lo mismo llevo un riesgo. Vamos a darle que sí que aceptamos y nos pide que si queremos ser un quick start o manual. Lo recomiendo quick start no nos metamos ahora en tantos detalles técnicos para ser manual así que van a serles o bien
