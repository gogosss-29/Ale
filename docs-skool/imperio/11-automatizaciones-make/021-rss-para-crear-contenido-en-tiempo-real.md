# 📰 RSS Para Crear Contenido en Tiempo Real

> Ruta: Automatizaciones Make › 📰 RSS Para Crear Contenido en Tiempo Real

**🎬 Vídeo (28.8 min):** https://www.youtube.com/watch?v=lxJR5kFomMg

**📎 Recursos:**
- (RETRIEVE) RSS a Redes Existentes
- (WATCHNEW) RSS a Redes Nuevos Post

---

Esta automatización te permite publicar contenido automáticamente en tus redes sociales como Instagram, Facebook, LinkedIn y X (Twitter). Utilizando feeds [RSS](https://bencorde.com/rss), extrae contenido relevante en tiempo real de páginas, genera descripciones o resúmenes con inteligencia artificial, crea imágenes personalizadas con DALL-E para Instagram y programa publicaciones en cada plataforma. 

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/fc630df7a3b3450bb4adb2b9d2838838783422f4463d4fe1a2eefa975b160f6a)

Todo funciona de manera automática, asegurando que tus cuentas estén siempre actualizadas sin intervención manual.

## **Paso 1: Configurar la Fuente RSS**

**¿Qué es **[**RSS**](https://bencorde.com/rss)**?**  
RSS (Really Simple Syndication) es una tecnología que permite a los sitios web enviar actualizaciones automáticas de su contenido. Cuando un sitio publica un artículo nuevo, este se agrega a un "feed" que puedes suscribirte para recibir automáticamente las actualizaciones. En esta guía, usaremos [RSS ](https://bencorde.com/rss)para extraer artículos y publicaciones relevantes para tus redes sociales.

**Configuración inicial**:

1. **Crea una cuenta en **[**RSS.app**](https://bencorde.com/rss): Es gratis y fácil de usar.
2. **Crear un nuevo feed**: - Haz clic en "Crear nuevo feed". ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3522ad582c614b05b6a9c9589167ebc990be787964504e8abc16c305736c1075)
- Selecciona los temas o palabras clave que te interesen, como "artificial intelligence", "marketing", o cualquier otro nicho relevante para ti (no te preocupes, las traduciremos más adelante) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0958253b1d8c4179be6c4c9bb61c09b7bdbd81832d0b4e0cb10c2737c185b09f)
- Trabajaremos con la versión gratuita, pero si tienes la versión premium puedes configurar listas blancas y negras de palabras clave para afinar aún más el contenido, por ejemplo filtrat "inteligencia artificial" con "agricultura" y sólo te aparecerán noticias de IA que involucren agricultura.
- Dale a guardar o "Save Feed"
- Copia el archivo XML  ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a3bc52fa93934759ad0f0257d96f172e051f14a96df14db5a9c99438810763b6)

---

## ***Paso (opcional) Importar la Automatización en ***[***Make.com***](http://Make.com)

***(Si no quieres construir la automatización, puedes importarla directamente, siguiendo estos pasos)***

1. ***Importar el JSON del escenario****:* - *Descarga el archivo JSON al final de esta página.*
- *Sube el archivo en *[*Make.com*](http://Make.com)* apretando los 3 puntitos y seleccionando "Import Blueprint" para cargar todos los módulos y conexiones automáticamente.*

## **Paso 2: Construir la Automatización en **[**Make.com**](http://Make.com)

Entraremos a Make y crearemos la automatización (también peudes importarla directamente si prefieres). Cuando construyas la automatización, tienes dos opciones para manejar el feed [RSS](https://bencorde.com/rss):

1. **"Watch new RSS feed items"**: Este módulo observará las nuevas publicaciones que salgan a partir de ahora. Es ideal si quieres que las publicaciones se publiquen automáticamente conforme se vayan generando.
2. **"Retrieve RSS feed items"**: Este módulo recupera las publicaciones ya existentes. Es útil para hacer pruebas y no tener que esperar a que salga una nueva publicación. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2183d6caf6594c108a1c0a420ef0596ec63d96a66a874363a33d27efa438619d)

**¿Cuál usar?**

- **Usaremos "Retrieve RSS feed items"** por ahora para comprobar que la automatización funciona, ya que permite extraer contenido de inmediato (es decir contenido que ya fue publicado)
- **Cuando quieras que funcione en automático**, cambia a **"Watch new RSS feed items"**, que publicará las nuevas actualizaciones conforme se generen (es decir contenido que se publicará en el futuro)

1. **Añadir el módulo de recuperación de RSS**: - Usa el módulo "Retrieve RSS feed items" para pruebas e ingresa la URL XML copiada de tu feed RSS. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/789e0b3723c648e09275c7eef4d908d08d15a24ce6f644eb9f5c985874e53b0d)
- Especifica cuántos artículos deseas obtener (ej.: 2 para empezar). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2d9ab385776e406b9cb9d127bb980f9761d7e38e53e44ea6a8e767b9a3e3a526)
- **Testea** este módulo para verificar que se están extrayendo los artículos correctamente y poder vincular los pasos siguientes. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/adab8315c791495c80c5f19103556999d476bf440394435f8c9b46e0c02d0ca2)

> **Recuerda**: Cambia el módulo a "Watch new RSS feed items" cuando quieras que la automatización siga funcionando en tiempo real.

---

## **Paso 3: Extraer y Formatear el Contenido**

1. **Añade el módulo “HTTP > Get a File”**: ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d23f920cd8d4463da15faf497158bf82f32082669ef44e1fa55c3149d87fcb71) - Descarga el contenido del artículo utilizando la URL obtenida del feed RSS (nota, es el "URL" que aparece arriba ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/608a61256f264c4cac046d2127306fb00deab6fb8bcb4f85b4194c2c848cbf1e) Le daremos a "Run this module" o correr el modulo individualmente para que podamos seguir extrayendo la data en siguientes modulos
2. **Convertir HTML a Texto**: - Usa el módulo “Text Parser > HTML to Text” para convertir el HTML del artículo en texto plano. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/51f22f85c219453190703d6aab0a693593d8dd8857e74d06b363391c9fb4f632) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1dfbf4b278c64bb494d0ed5eaca1840220d0526cc984499d8b1b3f7bb53906b7)
- Verifica que el módulo funcione extrayendo el texto correctamente.

---

## **Paso 4: Añadir un Router para Diversificar la Automatización**

1. **Agregar un Router en **[**Make.com**](http://Make.com): - El router te permite dividir el flujo en diferentes caminos para distintas redes sociales. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c4ce5cc60a2044b29a285e9eb5af7f0c8b4b8072105e4a9d8179b92ae863f72c)
- Crearemos rutas personalizadas para Instagram, Facebook, LinkedIn y X (Twitter), asegurando que cada una reciba el formato correcto de contenido.

---

## **Paso 5: Configurar Asistentes de OpenAI**

1. **Usa los asistentes preconfigurados**:  
Ya tienes asistentes pre-entrenados disponibles para cada red social en la comunidad **Imperio Digital**: - **Facebook**: [Asistente de Facebook](https://www.skool.com/imperio-digital/classroom/a65de4cd?md=fc86ac00adbc4cc7a2d0e3e5ced904fc)
- **Instagram**: [Asistente de Instagram](https://www.skool.com/imperio-digital/classroom/a65de4cd?md=5b071e54617c49008ede9441eaf68275)
- **X**: [Asistente de X](https://www.skool.com/imperio-digital/classroom/a65de4cd?md=a9b77d8ba8e24753991aa2947c7f756c)
- **LinkedIn**: [Asistente de LinkedIn](https://www.skool.com/imperio-digital/classroom/a65de4cd?md=14089265afd84492879a3b8ea3f0bd6a) - Si no has creado los asistentes, puedes ver como crearlos en el [siguiente link](https://www.skool.com/imperio-digital/classroom/a65de4cd?md=b03e9a24881b42f5a8ff85831305db4d)
2. **Vincular los asistentes**: - Usa el módulo “Message an Assistant” en [Make.com](http://Make.com) y vincula cada ruta del router con el asistente correspondiente para esa red social (Instagram, Facebook, LinkedIn o X). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/174ff439856c48eeb9bed241afd239b819eeb82102b44768963aa6279cd80b5c)

Luego selecciona los respectivos asistentes

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a24a065849b04531a3ae8b50c4f87697e487a7881b264fc6a447d4ce4fe5726d)

Y el mensaje que le mandaremos a cada asistente es "Text" del Parser

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/80750419c596420b8e6c3feab2d278766c93a41aeecd4c91bad35f79f3729161)

La razon por la que solo le mandaremos eso, es porque el asistente ya está entrenado con toda la informacion e instruccion y contexto de lo que debe hacer. Si quieres mas informacion sobre eso, peudes encontrarla [aquí](https://www.skool.com/imperio-digital/classroom/a65de4cd?md=b03e9a24881b42f5a8ff85831305db4d)

Actualizarás y vincularas cada modulo a cada asistente que creamos previamente, y le pondrás el mensaje a linea del router, es decir, uno independiente por cada red social.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d6e9a425535346af825d4be1f8edfabdabd4e8185e7e4af7b100ebaa62b10a47)

La automatización debería verse algo así.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/684b944f3020473396193c4e6f29527ccd779975992e4879a3fe5f3ead31ac7b)

---

## **Paso 6: Generar Imágenes con DALL-E para Instagram (opcional)**

1. **Añadir el módulo "OpenAI > Generate an Image"** para **Instagram**: ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e385c71bf2754416b9db424a77b9683285154a8d106b40d986b43ef652af785b) - Usa DALL-E para generar imágenes con dimensiones de 1080x1080 píxeles (tamaño adecuado para Instagram). Puedes encontrar una [guía con estilos específicos aquí.](https://www.skool.com/imperio-digital/classroom/7efa4739?md=4540be929b0543e5a561ef7203cd3fdb)
2. **Configurar el estilo de la imagen**: - Basado en el contenido extraído, genera imágenes en el estilo que prefieras. Por ejemplo, “minimalista”.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a7740507f6f442dda2e3147f984ebcd6adfe5e16d3b24536a1b6c2be4576e124)

---

## **Paso 7: Publicar en Redes Sociales**

1. **Configura las conexiones a las redes sociales**: - **Instagram**: Usa el módulo "Instagram for Business > Create a Photo Post". ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8392fe375f2748e19b2e119d814ce63540a1f0892bca42218cc776cf3f89abed) Bajo "Photo URL",  agrega el URL que está bajo "Data", y para el Caption, agrega el "Result" que nos dio previamente. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c00ff841bb5045fb9a4579a9a84b86bd6cab7cea3df2440e82eb340f253d6d75) - **Facebook**: Configura el módulo para crear publicaciones. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4f379f8076b347dbb33d9a141953c713928fcfc0712a4fb5ae74dad4be62eaa1-md.png) Selecciona el "Result" o resultado en "mensaje" ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1930aa05a3494cf5a6074d6f59a942df57eda7dc173041e4b7a5c76817bb848a) - **X**: Usa "Twitter > Create a Post". ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/adb6b75c2dd24dee83bc7277cdba766e0ee58962c19945bda38a98162a990f50-md.png) Nota: Necesitas el Client ID y el Client Secret, asi que debes registrarte y solicitar acceso en "X for Developers". - **LinkedIn**: Usa "LinkedIn > Create a User Text Post". ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4dadcbcbd0b0478cac4a0fdb288f9619d6facb36b7e94f9aaa4bf19fa1894f22) Selecciona el "Result" o resultado en "content". Nota: Deja preseleccionado el "Is Reshare Disabled" en "No", para que la gente pueda compartir tu publicación. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a7c8195924384e8993f5e7514f7d2796f3eb10bfed334ddd969edae6fc0ec70c)
2. **Input de contenido**: - Configura el subtítulo y la imagen (para Instagram) o solo el texto (para las otras redes) generados por los asistentes de OpenAI.

---

## **Paso 8: Prueba la Automatización**

1. **Corre la automatización una vez**: - Haz clic en "Run once" para comprobar que todos los módulos y conexiones funcionan correctamente. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0530818c9cde4e1cb41642393ea25c3233b6b35e460f4c7bb07f5e289b28c0c2)
- Verifica que el contenido se publique en las redes sociales que configuraste.

---

## **Paso 9: Activar la Automatización y Configurar la Frecuencia**

1. **Configura la frecuencia**: - Elige la frecuencia con la que quieres que se publiquen las publicaciones (ej.: cada día, cada semana, etc.). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e0aac7d3d08141e0840abe19cd582344aa5d1b91639d41a4aba2014de8a7e7b5)
2. **Activar el escenario**: - Una vez verificado que todo funciona, activa la automatización para que se ejecute automáticamente. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2eab1cd4303a40ea9f8c7a0ae585759c9a7fcc87fc6243dd8b3a5d286921e7f9)

---

**importante: verifica que este funcionando la automatizacion, y luego cambiarás el "Retrieve RSS Feed Items", es decir el primer modulo que creamos, a "Watch New RSS Feed Items", y volverás a seleccionar las variables. Esto lo hacemos porque primero queremos verificar que funciona con publicaciones anteriores, y luego para que empiece a sacarlas en un futuro.**

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c8ccd985b3db4eae91f5186d6f24db4c8ec923228eae4b35a779b518af09781f)

### **Conclusión**

Has creado un sistema automatizado para publicar contenido relevante en múltiples redes sociales, con subtítulos generados por IA y, para Instagram, imágenes personalizadas creadas por DALL-E. Recuerda cambiar el módulo de **"Retrieve RSS feed items"** a **"Watch new RSS feed items"** cuando quieras que el sistema se ejecute automáticamente en tiempo real.

**Descarga el escenario** aquí para empezar.

> **Nota: **Hay dos archivos, el que debemos importar para la automatizacion dependerá de la funcion que quieres que tenga. Si quieres que saque publicaciones antiguas, usa el "Retrieve". Si quieres que saque las publicaciones que se publicarán de hoy en adelante, usa el "WatchNew"
