# 🔐 Integración Google x n8n

> Ruta: n8n Desde 0 › 🔐 Integración Google x n8n

**🎬 Vídeo (7.3 min):** https://www.loom.com/share/639654e781e445009619988bcc97ccfb

---

👉 En este video te mostramos paso a paso cómo conectar cualquier herramienta de Google (Drive, Sheets, Gmail, Docs) con n8n.

Sabemos que la consola de Google intimida un poco, pero no te preocupes. Es exactamente el mismo proceso para todas las apps. Si lo aprendes para Drive, ya lo sabes para todo.

⚠️ **Diferencia Clave con Make:** A diferencia de Make donde copias una URL genérica, en n8n la URL de redirección es **única de tu servidor**. Aquí te enseñamos dónde encontrarla.

### 📌 Vas a aprender:

- Cómo crear un proyecto en Google Cloud desde cero.
- Cómo habilitar la "Biblioteca" de APIs (Drive, Gmail, Sheets).
- Cómo configurar la pantalla de consentimiento.
- **Lo más importante:** Cómo obtener tu `Client ID` y `Client Secret` para pegarlos en n8n.

---

### **🧠 Recursos Necesarios**

**1. Consola de Google:** 🔗 [console.cloud.google.com](http://console.cloud.google.com)

**2. Tu Redirect URI (URL de Redirección):** Esta **NO** es una lista fija. La tienes que copiar directamente desde n8n cuando creas la credencial. Se ve algo así: `https://[TU-DOMINIO]/rest/oauth2-credential/callback`.

---

### **🚀 Paso a Paso: El Tutorial**

#### **Paso 1: Preparar n8n**

1. Ve a tu n8n, abre el nodo de Google (ej: Gmail) y selecciona "Create New Credential".

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/19ac13a96dd64cb8b8de4a729920042c478b302f23244d4ca74690c49b224744-md.png)

1. Busca Gmail OAuth2 API

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f639f16e271a4379a22841a93ee2867005ff1b7f18894590abcba8d56963503b.png)

1. Fíjate que ahí te pide **Client ID** y **Client Secret**.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/61a74c8e1d6743fbab80ee882998bd101eede487682e40aebd0e318b7ec347cc-md.png)

1. Copia la **"OAuth Redirect URL"** que aparece ahí mismo. La usaremos en el paso 4.

#### **Paso 2: Crear el Proyecto en Google**

1. Entra a la [Google Cloud Console](https://console.cloud.google.com/). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/aa4c1fbd9c58484fa160debe7d764b22cad98d2ee6604b9c94f25f5930e08725-md.png)
2. Arriba a la izquierda, selecciona **"Proyecto Nuevo"**.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/09f5ba58f3a94149ab28dca7077484dd0793b4f0fff1463c89d8d9efdb2bcd64-md.png)

1. Ponle un nombre fácil, por ejemplo: `n8n imperio`.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/fd16de18b5284256b8ee782bfa49df9b1507a0270cf2454bb60d6d13a6dd4665.png)

1. Dale a crear y asegúrate de **seleccionar el proyecto** que acabas de crear.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c31e68b7376a4116b88c8bfc0b1ab142b848219a97ca425b9d270085efbb58c9.png)

Selecciona el proyecto

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b77813f28a914a509f126b19e40e46540229dded6506463caf26cb80c241367e-md.png)

#### **Paso 3: Habilitar las APIs (La Biblioteca)**

1. En el menú lateral, ve a **"APIs y servicios" > "Bibliotecas"** (o APIs habilitadas).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/402f4f10b04146548d2fbca04d9416310275adb7a3124803a09a89f4afd7c629.png)

1. 2. Usa el buscador para encontrar la herramienta que quieres conectar. - Si es Drive: Busca `Google Drive API`. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/625fe18013b34e44ab20bf77ecda6dfd01a3b987114a4b3f9070a96a2763d6a9.png) - Si es Sheets: Busca `Google Sheets API`. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ff5a7b91496d41929d2a4f34f78a2705a67b820d72dc411eaf869dbaeba3fedf.png) - Si es Gmail: Busca `Gmail API`.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/708e314f32f544369a67377003716d705264a3b05bf240fdb0139540d00a43f6-md.png)

1. Dale al botón **"Habilitar"**. - *Nota:* Si quieres conectar varias cosas, repite este paso y habilítalas todas ahora.

#### **Paso 4: Pantalla de Consentimiento (OAuth Consent Screen)**

1. Ve a **"Pantalla de consentimiento de OAuth"** en el menú lateral.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/536ddcfbe2334a8bae2db98b24127e02dc1512e35d0c4b6aab1611e5909d6ad6.png)

1. Dale a "Comenzar".

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cf08aaa70e894db8834397335e506565c55822d5466d4213957fdb3c2b313af3.png)

1. Rellena lo básico: - **Nombre de la App:** `n8n imperio` (o n8n).
- **Correo de asistencia:** Tu email.
- **Información de contacto:** Tu email nuevamente.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/29d2ea1e91bd4b9b8b9ed99f4adc4e998fe8d9de7edf4c9d921b674de4728da4.png)

Luego dale a externo

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4e54bb6f7a064db5b3c8cea4804c63c00badcf57963f42e8b1c4779224494886.png)

Dale a "Guardar y Continuar".

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3345eedbbdf649509a3d75251695cb970b553cac895248bda21afa78d22981cf.png)

#### **Paso 5: Crear las Credenciales (Client ID & Secret)**

1. En el menú lateral, ve a **"Credenciales"** y dale a **"Crear credenciales"**

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2a2e73ca325a44e09a461a74b26b94ab0351d5480982447bb45c98c79bb49322.png)

Luego ** > "ID de cliente de OAuth"**.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/bb0d9906d8224a9dabf24ca68774c6bb48876c2fb7914f2cb295dbd6772bb928-md.png)

**Tipo de aplicación:** Aplicación Web.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2c9b8325bca1423c91a0571bd58a59b985dd4b60f9cc459f8c0f06b690aa49ad.png)

1. **Nombre:** `n8n imperio`.
2. **URIs de redireccionamiento autorizados (CRUCIAL):** - Aquí debes pegar la URL que copiaste desde n8n en el Paso 1.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/69305e1f0a0f4c32929f9cf5e28d7d068293cef119ec4becb59efa6165326b45-md.png)

Y ahora

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b32ffb71bc5a432f9c0ca1b98be6681e1259d0c41b504902989994b4e261f148.png)

1. Dale a "Crear".

#### **Paso 6: Conectar en n8n y Permisos**

1. Google te mostrará tu **ID de Cliente** y **Secreto de Cliente** (TIP DESCARGA ESTO, ya que solo lo podrás ver una vez)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ea98918e9a47470d8dd60fbb1546b5b5c8b9d9dc7b0f44b89ab8c47566485d06.png)

1. Copia el ID y pégalo en n8n.
2. Copia el Secreto y pégalo en n8n.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3dd6998d26884fae9203c947048c1caeeb02b4e67f5d40738e13971d8ef847a5.png)

1. **Ojo! ANTES de conectar:** - Vuelve a Google, ve a **"Acceso a los datos"** (o Scopes) y asegúrate de asociar/habilitar las APIs que activaste. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/699a2967490d4bb88b72e6cd178d33afdf7cddd1ea5f415780dbaf70a4447dec-md.png) Luego baja al máximo y dale "Mostrar 100" ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8565fb3b0de5434b8eabf513c4a659feb2b8b68f1a7e4712ac7beacd0422cfbb.png) Dale a seleccionar todas las filas ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/487c4259b39d48869b099574c0b191e34a2a2eca3ea24f5686c196ca5379cd13-md.png) Luego dale a guardar y actualizar ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6f1cca072dc146a18d4aeb9cdf0551fee624ea0ed54848d9bacaad27b581f939.png) - Ve a **"Usuarios de prueba"** (Test Users) y agrega TU propio correo Gmail. Si no haces esto, no te dejará entrar.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ecf80397c5904d41bd24d4bba4e535b7af79ac1ccac042798fa92916f53f945f-md.png)

Dale a guardar

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8b2a1f451ba74f8e872e1eccfee0cdbf15b7095d8b48445d88f4477f701121cb-md.png)

Luego dale a publicar

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9fe623ff52d2433c962efdf7760a2636ed288df37c364413b5e677ae89ea714d-md.png)

1. Ahora sí, en n8n dale al botón **"Sign in with Google"**.
2. Si te sale "Google no ha verificado esta app", apreta lo que sale abajo a la izquierda mostrar avanzado, y dale a **ir a... **(es seguro, es tu propia app).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8d7d5d3cce12489f99288a4cb793eb244069dac3020c4b48a0f5b1caa08e13cb.png)

1. Marca todas las casillas de permisos y dale a Continuar.

✅ **Account Connected:** Ya tienes Google integrado en tu servidor.

Repite el proceso de agregar credencial, sheets y drive.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/43aa061223f3467780784562be10af8b12d1d9414d64465b9fb1d017aa24c0a0.png)

Elige

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b5d62b00bda64099906389ced16caf8e43c99004008d4214abc212b6015d154e.png)

Llena tus datos

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6e360dc3848f48eba90024ea8c539748ab01306f88164adbb427bb669871eefd.png)

Y repite el proceso para sheets...  
  
Ahora puedes enviar correos, extraer data de sheets y guardar cosas en drive.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/77e99765dd05400b9d6494d59f9cea226863fd6398a7444e99c94972b87ea16d.png)

## 🎙️ Transcripción

Sabemos que conectar las credenciales de Google a N8N a veces puede ser un poco complicado. Por eso que en este video vas a ver cómo lo hacemos en menos de 5 minutos. Lo que vamos a necesitar es entrar directamente a N8N. Nos vamos a ir a la parte que sale credenciales y le vamos a dar a crear nueva credencial. Supongamos que la que queremos conectar primero es Gmail. Vamos a buscar Gmail acá y vamos a poner Gmail o AUS 2 API. aquí nos va a dar un OAuth Redirect URL, este lo vamos a copiar, después vamos a entrar al Google Cloud Console, cuyo link es este que aparece aquí, arriba, importante no apreten esta parte que sale Start Free o empieza a dar arriba, lo que quieres apretar es justamente acá, seleccionar un proyecto y crear un nuevo proyecto, Vamos a ponerle cualquier nombre como N8N Imperio y le vamos a dar a Crear. Una vez que lo creemos, necesitamos asegurarnos de que lo vamos a seleccionar aquí arriba. Vamos a apretarlo y vamos a elegir N8N Imperio. El paso siguiente es habilitar las APIs para eso nos vamos a ir aquí al costado y nos vamos a ir donde sale APIs and Services. Una vez que estemos aquí vamos a irnos a la parte que sale librería o biblioteca, si es que lo tienes en español y vamos a comenzar a habilitar todos los servicios de Google que queramos, el primero que vamos a hacer es Gmail, voy a buscar Gmail, le voy a dar Enter, Gmail API, a habilitar y muy importante, vamos a esperar a que termine de cargar esto, no vayas a salirte antes de que termine, vamos a ver que ya está habilitado, vamos a darle atrás y vamos a aprovechar de habilitar todo de una. Voy ahora a buscar Drive, Google Drive API, habilitar, luego voy a buscar Sheets, Google Sheets API, habilitar, ahora voy a buscar Google y voy a ver si hay algo más de aquí que me gustaría habilitar en específico como el Google Calendar y el Google Slides. Voy a cambiar ahora el idioma y lo voy a poner en español netamente por fines de este video. Y nos vamos a ir a la pantalla de consentimiento. Vamos a darle a empezar. Y vamos a crear nuestra aplicación. Lo voy a poner en el 8N Imperio. Voy a poner mi correo electrónico, próximo aplicación, audiencia externa, siguiente y la información de contacto voy a poner el mismo correo que está acá, siguiente, acepto, continuar y crear. Bueno, parece que voy a deshabilitar la traducción porque la reducción es horrible que es esto de despedir, simplemente lo voy a poner dismiss para que dejé aparecer. Y ahora si vamos a volver atrás donde sale Google Out Platform, vamos a irnos a la barra lateral y vamos a irnos a los APIs and Services y Crenciales. Vamos a poner crear Crenciales y o Out Client ID. En tipo de aplicación le vamos a poner aplicación web y le voy a poner algo de nuevo como N8N. Imperio. Vamos a bajar y en la parte de los URIs vamos a poner al URI y vamos a pegar la Crencial o el URI en específico que apareció antes, vamos a volver acá, lo vamos a pegar y le vamos a dar a crear. Esto nos va a nuestro cliente.de y nuestro cliente secret, que es exactamente lo que nos pién acá. Voy a copiar cliente.de y lo voy a pegar acá y voy a copiar cliente secret y lo voy a pegar acá. Pero antes de darle iniciar, vamos a tener que hacer un paso antes. Vamos a descargar el JSON, porque no vamos a volver a tener acceso a esto. Voy a OK. Vamos a abrir nuestra aplicación en específico dentro de las credenciales, vamos a ir no a data access o acceso de datos y vamos a agregar los scopes, vamos a bajar al máximo, vamos a ver, vamos a poner 100 y vamos a seleccionar todos, vamos a bajar, le vamos a dar a actualizar y no solviden en esta parte de bajar y darle a guardar muy importante. Luego nos vamos a ir a la audiencia, si lo tienes en español te van a hacer los usuarios de prueba y vas a poner a agregar usuarios. Vamos a poner el mismo correo que hemos estado usando y le vamos a dar a guardar. Ahora le vamos a dar a publicar, confirmar y ahora sí vamos a volver a N8N. Ahora sí le vamos a dar a iniciar con Google, Imperio Digital, entrar con tu cuenta y aquí te va a dar una advertencia. Simplemente le vamos a ignorar y le vamos a poner ir, pese a que no es seguro. No te preocupes es seguro porque es tu propia aplicación y la acaba de crear. Vamos a seleccionar todo, le vamos a para continuar y listo conexión éxitos así es que ahora creo un workflow en específico. Me voy a workflow. Creo un workflow. Pongo enviar un mail. Enviar un mail y me lo mando diciendo, deja es el mejor Copio Pego, con muchos signos de exclamación y ejecuto, este paso en específico, voy a abrir mi correo y voy a ver qué recibo el correo es decir, ya está funcionando. Ahora tenemos que habilitar el resto, pero no te preocupes porque no tenemos que hacer todo de nuevo. Simplemente volvemos donde estábamos, creenciales, crear creencial y conectamos el resto de las aplicaciones que pusimos antes cómo, el Drive, continue, ponemos el Client ID, que si lo perdiste está en este JSON en específico que acabamos de descargar, que si quieres buscarlo el Client ID te va a aparecer acá, lo puedes copiar, lo puedes pegar y la secreta, la llave secreta también va a aparecer, está aquí donde sale Client Secret entre las comillas, porque es un JSON, la vamos a copiar, la vamos a pegar, y vamos a iniciar nuevamente con Google, elegir el correo, avanzado, continuar, seleccionar y continuar. Y listo, vamos a repetir este proceso para cada una de las aplicaciones que queramos conectar, vamos a buscar Google Calendar, vamos a conectarla. mismo proceso, continuar, client ID, client secret, guardar, lo mismo para el sheets y ahí está listo, recuerda que acá también tienes una guía específico donde cubrimos, literalmente todo el pasabazo que te acabo de mostrar.
