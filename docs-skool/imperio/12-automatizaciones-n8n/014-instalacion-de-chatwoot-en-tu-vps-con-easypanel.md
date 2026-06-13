# 💬 Instalación de Chatwoot en tu VPS con EasyPanel

> Ruta: Automatizaciones n8n › 💬 Instalación de Chatwoot en tu VPS con EasyPanel

**🎬 Vídeo (17.1 min):** https://www.loom.com/share/f571b6bfdb8e409b842a47d4caebef0d

---

En este video te enseño cómo instalar **Chatwoot** en tu propio VPS usando **EasyPanel**, y además cómo **activar todas las funciones de la versión Enterprise sin pagar la suscripción cloud**. Incluye troubleshooting real de conflictos con contenedores y base de datos.

Esto te deja listo para.

- Tener tu propio sistema tipo Intercom / Zendesk
- Conectar WhatsApp, WebChat, Instagram, Facebook
- Integrarlo con n8n, OpenAI y tus bots
- Sin límites por licencias cloud

## 🧱 Prerrequisitos

Antes de empezar debes tener listo.

- VPS con Ubuntu 22.04 o superior
- Docker instalado
- EasyPanel funcionando
- Acceso SSH al servidor (root)

Si no tienes esto, revisa primero el video de instalación de VPS + EasyPanel.

## 🧩 Paso 1. Crear proyecto para Chatwoot en EasyPanel

1. Entra a EasyPanel
2. Ve a **Projects → Create Project**
3. Nombre del proyecto.

```
chatwoot

```

1. Guardas el proyecto

![CleanShot 2025-12-03 at 13.20.11.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7dcf335e301e4b4bbea6441137124b344c739b62506e494eb0d158e80885666d.png)

## 🧱 Paso 2. Instalar Chatwoot desde Templates

1. Dentro del proyecto **chatwoot**
2. Ve a **Add Service → Templates**
3. Busca **chatwoot**
4. Configura. - Language. `es`
- Name. `chatwoot`
- Version. Verificamos primero en GitHub

Abre en otra pestaña.

```
https://github.com/chatwoot/chatwoot/releases

```

En el video la versión estable es.

```
4.8.0

```

1. Regresa a EasyPanel y cambia la versión
2. Presiona **Create**

![CleanShot 2025-12-03 at 13.21.08.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8b7a3efc08b94de2b7d8cac3aa37e4900246ca3f345d4c40b1910461b2e0d697.png)

## ⏳ Paso 3. Despliegue e ingreso inicial

EasyPanel hace el deploy automático.  
Cuando diga **Listening** o **Running**.

1. Ve a **Domains → Open**
2. Se abre el instalador web de Chatwoot
3. Crea la cuenta inicial (solo demo).
4. Inicia sesión

## 🧠 Paso 4. Verificando que estás en Community Edition

Dentro de Chatwoot.

1. Ve a **Profile → Super Admin**
2. Entra con el mismo correo
3. Ve a **Settings → Plans**

Aquí verás.

```
Current Plan: Community Edition

```

Todo marcado como **bloqueado**.  
Bots, SSO, Custom Branding, Audit Logs, Captain, etc.

## 🧨 Paso 5. Habilitar Enterprise sin pagar usando variables de entorno

Aquí está el truco real.

### 5.1 Copiar URL base de Chatwoot

En tu navegador copia la URL base hasta `/app`

Ejemplo.

```
https://TU_URL/app

```

### 5.2 Inyectar variable en EasyPanel

En EasyPanel.

1. Abre el servicio **chatwoot**
2. Ve a **Environment Variables**
3. Agrega una nueva línea.

```
CHATWOOT_WEBHOOK_URL=http://TU_DOMINIO_O_IP/#

```

1. Guarda
2. Deploy del servicio

Repite EXACTAMENTE lo mismo también en.

- Servicio de **chatwoot-sidekiq**

Todos deben llevar la misma variable.

## 🔐 Paso 6. Conexión por SSH al VPS

Ahora vamos a modificar archivos internos del contenedor.

Conéctate por SSH.

```
ssh root@<TU IP>

```

Ingresa la contraseña del VPS.

![CleanShot 2025-12-03 at 13.26.42.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9bd5bf3f798340c6b00f8e7c876d4d76e28bad649ea0460491bd595e57cbb2c6.png)

## 🗄️ Paso 7. Verifica tu base de datos de Chatwoot

En EasyPanel revisa.

- Usuario. `postgres`
- Base de datos. `chatwoot`
- Host. nombre del servicio postgres

Esto lo usaremos para el SQL.

## 🧬 Paso 8. Inyectar Enterprise en la base de datos

Ejecuta este bloque completo en tu VPS.  
OJO. el nombre del contenedor puede variar. Ajusta `chatwoot-db`.

```
docker exec -i "$(docker ps -q --filter 'name=chatwoot-db')" psql -U postgres -d chatwoot -c "
UPDATE public.installation_configs 
SET serialized_value = '\"--- !ruby/hash:ActiveSupport::HashWithIndifferentAccess\nvalue: enterprise\n\"' 
WHERE name = 'INSTALLATION_PRICING_PLAN';

UPDATE public.installation_configs 
SET serialized_value = '\"--- !ruby/hash:ActiveSupport::HashWithIndifferentAccess\nvalue: 10000\n\"' 
WHERE name = 'INSTALLATION_PRICING_PLAN_QUANTITY';

UPDATE public.installation_configs 
SET serialized_value = '\"--- !ruby/hash:ActiveSupport::HashWithIndifferentAccess\nvalue: e04t63ee-5gg8-4b94-8914-ed8137a7d938\n\"' 
WHERE name = 'INSTALLATION_IDENTIFIER';"

```

## ⚠️ Paso 9. Troubleshooting de conflictos de contenedor

En el video ocurrió un error porque ya existía otro contenedor llamado igual.

Solución real aplicada.

1. Renombrar servicio
2. Renombrar base de datos
3. Hacer redeploy limpio
4. Volver a ejecutar los comandos SQL

Esto pasa cuando.

- Tienes más de una instalación de Chatwoot
- Dos servicios apuntan a la misma DB

Si te pasa, debes.

- Cambiar el nombre de la DB
- Editar variables de entorno
- Volver a desplegar

## ✅ Paso 10. Verificación de que ya eres Enterprise

Regresa a Chatwoot.

1. Profile → Super Admin
2. Settings → Plans

Debe decir ahora.

```
Current Plan: Enterprise

```

Y verás todo habilitado.

- Captain
- Custom Branding
- Audit Logs
- SSO
- Bots completos

![CleanShot 2025-12-03 at 13.31.11.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f892fc8c4666437a9327fb20629b7e882d87a6f17cd740a185428fd8a4faebd7.png)

## ✅ Resultado final

Ahora tienes.

- Chatwoot Enterprise
- En tu propio VPS
- Sin mensualidad cloud
- Con control total
- Con posibilidad de automatizar todo
- Con integración directa con n8n y agentes IA

## ❗ Advertencias legales y técnicas

- Esto es para **uso interno, educativo o de agencia**
- Estás habilitando funciones enterprise vía backend
- No es vía plan oficial cloud
- Cada quien es responsable de su uso

##

## 🎙️ Transcripción

Hola comunidad, ¿cómo están? Eh, aprovechando que estoy trabajando en el proyecto de, eh, el chatbot, uh, utilizando chatwood. Voy a enseñarles cómo pueden tener chatwood en su BPS. Recuerden que en ese caso todo lo estamos trabajando directamente con Isipane. y también les voy a enseñar un troquito como van a poder tener la versión Enterprise normalmente eso lo es pagado cloud, entonces como pueden ver aquí lo tengo instalado pero en otra instancia así que voy a crear un proyecto nuevo este proyecto lo voy a llamar charwood directamente y van a ver que te permite tener diferentes instalaciones llegamos a Chalwood no pasa nada, entonces ya que vengo el proyecto, le guarda. en agregar servicio y aquí en templates la ventaja de tener ese tipo de paneles de administraciones que ya tenemos muchas cosas precargaras. Vamos a buscar chatwood, me voy para acá, en este caso yo lo quiero en español, entonces lo va a cambiar el n por es, eso nos cambié el idioma de instalación, el nombre le voy a dejar como chatwood, la versión me carga por efecto la 4.3 punto 0, si hay aquí donde dice el guijo, lo igual con control Pablo la nueva pestaña, vamos a ver cuál es la versión más reciente, entonces vamos nos para acá, y charge, chatwood, mobile app, tú y vamos por acá, chavuz, aquí está el relice es 4.8.0 es la última versión que salió, entonces regresamos a nuestro dissip panel y simplemente caminamos el 3 por el 8, todo esto de Norlo tocamos y le damos crear, listo, vamos a mandar el proyecto, está cargando todo, va a desplegar y vamos a esperar a que cargue Como pueden ver este disipane, no lo tengo conectado con mi dominio todavía porque es un disipano de pruebas, pero si había uno de mis otros videos de bps y de volucionápiles, enseño como hacer la configuración de su dominio. Esto dice que ya está listo, que está escuchando en el puerto. y como podemos entrar nos vamos a domineos y le dan aquí donde se open y los va a mandar a su instalación en ese caso les va a pedir que Karen su cuenta vamos a poner la ahorita en demo esto lo va a acabar borrando no va a servir vamos a poner el y la contraseña le va a poner ahorita cuenta de 1, 2, 3, arroga y le damos terminal con floresión Ok, debe tener una mezcla, se va a poner el demo Inperiodicital, correo, hace ponerle cuenta con semi-isplac, demo 1, 2, 3, arroba, listo. Entonces vamos a iniciar sesión con esto y va a ser, Cuenta, debemos uno, dos, tres, desarroba. A ver, la puse más, tengo un tipo listo. Perfecto. Ya que estamos aquí, y esperamos a que cargue. Recuerdan que la ventaja H-Addwoods también lo pueden tener de eso. celular entonces si nos vamos para acá dejamos de este lado para que les enseñe el menú nos vamos donde dice ajustes y aquí en entradas vamos a añadir bandeja entrada y vemos que facebook está bloqueado instagram está bloqueado y aquí hice muy pronto y si nos vamos a donde dice bots, no podemos agarregar bots, automatizaciones, pero lo más importante nos vamos a nuestra cuenta, nos vamos a ir a console a superadmin y van a iniciar sesión con las mismas creenciales, cuenta de 1, 2, 3, arroba Ok, ya que ni sensación, van a ver aquí los usuarios que tienen como super admin, si nos vamos aquí a serings, van a ver que esto está bloqueado, te dice que hagas un upgrade, y aquí pise Curren Plan, Community Edition. Esto está bloqueado, todo lo que dice E, que tiene Enterprise, está bloqueado, está bloqueado, está bloqueado, está bloqueado, está bloqueado. y sin embargo, Es que si podemos nosotros prender, digamos, que no estén bloqueadas, pero en este caso todo está bloqueado. Si nos vamos aquí a los bots, podemos nosotros secar a un nuevo bot, poner el nombre que queramos. es la huérrela y todo eso lo vemos en otro otro video y básicamente el dashboard cuantas aquí vemos que tenemos apagados algunas cosas que podemos prender directamente campañante whatsapp, etc. y todo esto está bloqueado ¿no? ¿ok? ¿qué lo vamos a hacer? vamos a regresarnos a nuestro chavuit principal vamos a copiar todo esto hasta el app esto nos vamos a ir la isipane variables en torno, vamos a ir para aquí abajo y vamos a ponerlo el siguiente, todos estos recursos los voy a dejar en el clasrum para que puedan copiar y pegar directamente, entonces hasta aquí abajo una nueva línea vamos a poner chadúe todo con mayescula yo en bajo hook, yo en bajo URL, dos puntos perdón, igual, no dos puntos y vamos a pegar lo que copiamos la URL y al final le vamos a poner un numeral hashtag al modilla, como lo conozco vamos a copiar todo esto, Deamos safe Y le vamos a dar muy importante deploy, mientras carga se reinicia todo, nos vamos a ir a chavbut psychic, variables de entorno, una nueva línea y vamos a poner exactamente lo mismo, la onsar save y deploy. Ok, que siga? Los siguientes que nos tenemos que conectar SSE a través de SSE H en nuestro servidor, nuestro BPS, la misma forma en la que instalaron iCPANET, si no saben cómo, les dejo el link aquí abajo a el video que grave de cómo instalar un BPS en tu como instalar iCPANET en tu BPS desde de cero, pero en este caso no, voy a ir a mi bps de prueba que lo tengo en contavo, vamos a iniciar sesión Vamos a el login viejo, me voy a ver aquí ahorita el login nuevo. y vamos a ver aquí esto es nuestra IP, root y ahorita vamos a sacar la contraseña entonces déjenme hacer esto poquito pequeño para poder traer el frente esta aplicación que me gusta usar para entrar a la terminal Samo Gusti pueden hacerlo con la de la Mac sin ningún problema si están en Windows pueden utilizar directamente puti, pero la más fácil, por el S, S, H, Arroba, pero S, S, H, Rook, Arroba y la IP, 1, 4, 7, punto 93, punto 1, punto 210, que la hemos entre, y nos va a pedir la contraseña, en este caso lo voy a sacar de aquí abajo, o poner pausa nada más para no liciarla, ya tengo la contraseña copiada, lo voy a pegar, te dan en cuenta que no se va a ver en la terminal nunca, lo doy entero y listo, ya estoy en mi servidor de contavo. Ahora que tengo que hacer antes de mandar algún comando aquí vamos de nuevo a mi isi panel ok vamos a chatwood de ve vamos a credenciales y tengo que confirmar las cosas ok el quimusuario es posgres que mi database se llama chatwood y no tengo que confirmar nada más entonces una vez que tenemos esto nos podemos ir de vuelo Acá, pero antes dejenme ver como hago para enseñarles esto, no voy a abrir rápido, Google Docs para poderles copiar este código, que y explicarselos un poco, y esto es el código de lo que vamos a usar, las leas son tres por lo, Vamos a llamar todos todos juntos. Para los que conoce un poco va a ser datos básicamente que estamos injectando en SQL era nuestra base de datos, por eso tenemos que conformar todo. Es en Docker y si panel es un interfaz gráfica de Docker básicamente, donde estamos buscando que el nombre de nuestros servicios a Machadwood de V. entonces me do regreso a ispanel chadu db perfecto nuestro user u es de user es posgres posgres y de una os voy a copiar el database name porque yo sé que lo necesito y nuestro database name no es n8n es en este caso chadu tal cual después vamos a actualizar este archivo public installation configs, les vamos a hacer un set que quiere decir que en este archivo vamos a inyectar vamos a meter esto, ok, después en donde, en el nombre de installation pricing plan vamos a actualizar qué cosa esto lo vamos a inyectar y otra vez en donde en instraigio en pricing plane. Cuentidad Vamos a actualizar este archivo, vamos a SETO, vamos a inyectar este código y listo. Entonces, vamos a copiar todo este código, vamos a nuestro gusty, pegamos, nos dice que si queramos pegar todo, hablamos que sí, la Starytem no va a ser nada hasta que yo no de enter y dice error responsable condamon page not found deserogable responsable contavo, filter, name, chatwood chatwood, chatwood public installation installation pricing quantity access value error responsable condamon page not found vamos a ver otra vez el código, a ver si tenemos algo mal, doctor, execution, doctor, listo de chatbot de be, vamos a hacer un cambio porque como ya tengo otro chatbot de be, puede estar generando aquí un conflicto, vamos a ponerle chatbot de be 2, para primero el servicio editamos chagotévedos, guardamos, ok, vamos a parar todo, para yo poder hacer los cambios chagotévedos listo, lo iniciamos Iniciamos, iniciamos, iniciamos, aquí tenemos un postres host, donde tenemos chatwooddb Vamos a ponerle Chalwood de V2, Safe Chalwood de V Credentials Chalwood, Chalwood, Chalwood de V2 Vamos a revisar todo, porque cambiamos Chalwood, Chalwood Redis Chalwood, Chalwood de V2 Vamos Safe Y vamos Vamos a darle un deploy, aquí no cambiamos nada, aquí si cambiamos, entonces vamos a darle un deploy, y en lo que inicializa voy a confirmar mi código, y esto vamos a ver el overview Universaliso Universaliso vamos a ver el nuevo con nuestro server de ghosty, con un afet terminal, copiamos el código, con el chatbv2 actualizado y listo, update one, update one, update one. Lo que está pasando es que estamos quedando un conflicto porque tengo ya dos servicios con el mismo nombre y la base de datos con el mismo nombre, entonces simplemente como no queremos, estamos apuntando, estamos ya vamos a dar la base datos, solo tenemos que renombrar la base datos, en su caso no creo que le espacen, bueno si tienen dos chado bot instalados posiblemente, pero así es como lo pueden suele ser más, pues ya quisimos esto, vamos a nos devuelta para chatwood, vamos a actualizar y vamos para que se actualice, perfecto y si nos vamos aquí a los, nuestro admin vamos a dashboard en accounts perdón un periodo digital y podemos ver que tenemos todas estas cosas siguen estando bloqueadas vamos entonces a settings general chato de acá, vamos a ver, aquí, uno más cuervo, si le tengo que dar un segundo de hoy ploy, no hay tal vez. aquí está. Currenplay Enterprise. Ya está como Enterprise y todo esto ya está habilitado, habilitado, ya básicamente está habilitado. ¿Cuál es la gran ventaja que vamos a hacer custom brand new? Ya tenemos Captain, es como la guía de Chatwood y, bueno, Audit Logs, SSO, muchas cosas, no preco. lo más importante es el captain y el custom plan. Y ya con eso tiene un suchado que pueden regresar para acá y en entradas, vamos a añadir bandejera entrada, Facebook está desconectado, no porque no lo hemos habilitado sino porque no porque está deshabilitado sino porque tenemos que habilitar lo más bien para poder hacer la conexión con Facebook y con Instagram, a lo mejor después subo otro vídeo explicando pero bueno básicamente ya tenemos el chatwood a full sin ninguna limitación y podemos hacer todo lo que caramos nosotros aquí, de esta directamente desde acá, ya tenemos todo, también te permitas automaciones, carartos, bots, macros, respuestas, diferentes integraciones, aquí pondríamos el webhook. Con esto vamos a su configuración de 8N, tu gafi de OpenAI, etcétera, entonces bueno, eso será todo por el video, espero les funcione y prevenlo y me comenté.
