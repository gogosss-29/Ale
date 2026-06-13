# 🧩Sistema IA para Crear Contenido Autom. en RRSS

> Ruta: Automatizaciones Make › 🧩Sistema IA para Crear Contenido Autom. en RRSS

**🎬 Vídeo (23.3 min):** https://youtu.be/K3Jg1J6uGXY

**📎 Recursos:**
- A) Correr Google News Scraper
- B) Correr Google News Scraper

---

## Cómo extraer, formatear y publicar noticias automáticamente con Apify + Make (IG, Facebook y LinkedIn)

La idea es simple: buscamos noticias sobre un tema específico, armamos un post listo para redes y lo publicamos en Instagram, Facebook y LinkedIn con su imagen oficial y fuente. Todo corre solo, a la frecuencia que quieras.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ec8bbd87fb0e4ab591d788b61bbc3c1b1b869f0f3ec0484ca3cfb770cd0a52c4-md.png)

# Paso 0 – Habilitar el actor en Apify

Antes de construir nada en Make, tienes que habilitar el actor en Apify:

1. Entra al actor: [Google News Scraper – Input JSON https://console.apify.com/actors/eWUEW5YpCaCBAa0Zs/input](https://console.apify.com/actors/eWUEW5YpCaCBAa0Zs/input)
2. Haz clic en **“Create Task”**.
3. Esto creará una tarea asociada a tu cuenta y hará que el actor quede disponible en [Make.com](http://Make.com).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f877eff3c277486c9cbbb318cbcdf9f9225c58c45ed14aaa9c6025c6d2cd5528)

1. Esto creará una **tarea asociada a tu cuenta** y hará que el actor esté disponible después en [Make.com](http://Make.com).

---

## Escenario 1 — Ejecutar el scraper

1. En la configuración del actor verás un campo llamado **searchQuery**. - Ahí escribes el tema o palabra clave que quieras buscar (ejemplo: “inteligencia artificial”, “marketing digital”, “ChatGPT”).
- Si quieres algo más amplio, pon un término genérico o un "tópico".

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/64823a44b0d24fee9985863235058c907e30ecb412594e79b380b8c1f56208a0-md.png)

1. Haz clic en **JSON** y copia todo el código que aparece.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/dc62559fa7e24dc58ee954fa61026f80d7f57ae6d41f4cd694a22cd022a228fe-md.png)

1. En **Make**, crea un escenario con el módulo **Run Actor**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/445415616c95416ea47d8e276561d1a99a970c6d81414bcc926f121ed2bddf45) - Pega ese JSON en **Input**. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a2f0b548e2a54d90846c3b22f035aa3746258dd7377142089455d25aff75f18d) - Define cada cuánto quieres que se ejecute (todos los días, una vez por semana, etc.).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c75287686e3545529ac4550c5436a592dd2e500c3ab0483fad917b99d0cad0ba)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d3b14313b93940129eaa4a6dcc8f8f3bc20122cc2dc4416c95925a9bf2d0b08f)

## Escenario 2 — Mirar resultados y publicar

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7074633e46974bc99b41e7830a1fbdd240dadfdc8d0d4d2ebbb62fc9886c52df)

Cuando el scraper termina, este escenario recoge los datos y los convierte en publicaciones:

- **Webhook**: se activa cuando el actor acaba de correr.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a1e63c869b9d4f8eb45fd51aeb5139bad240b42e2a19400191fa29a07f3ec787)

- **Get Dataset Items**: trae las noticias con título, fuente, link y la imagen oficial.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/08f059accbbf426d98066935c67bd8540b23e3a63f0f421e80b8a404994705ed)

- **Generador de texto (IA)**: arma el texto del post con la noticia y cita la fuente.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f80bed823a5c434282a2288e1c9e04c522a6159bcdae48fb8792e920e2ba5a8e)

> Creame una publicacion híbrida (que funcione para Instagram y Linkedin) en español de caption de la siguiente noticia: "{{2.title}}" . Menciona la fuente al final que es :{{2.sourceUrl}} ({{2.source}}) y la noticia completa la encuentras en {{2.loadedUrl}}

- **Descargar imagen**: baja la foto oficial de la noticia (get a file)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/16afad4c8de041b4b9e0a77342a445e6172bef795b8f4698a4577ba0ad2f510b)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a6e7fc9a78bd42cb984d9d7004e70b771fc9e82487d8483395ce96fe42ddefea)

- **Publicar en redes**: el sistema sube el post a Instagram, Facebook y LinkedIn en paralelo.
- **Router** → Divide el flujo en tres caminos: ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/99f7fdf73152495ab0ee4e0d3d3db8f1ad7326421965432c930ec8fbcbc0ff30) Los caminos: ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0263b8a2597948ebba67dd8b9a1f8c963c0ae3dd2ff54d38af7ca71a9bd79555) - **Instagram for Business** → Publica la noticia como foto con texto. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/200fe213491042dd8f12191bbf9bdd5e53829f4666b14091a6476cc8593b7284) - **Facebook Pages** → Crea un post con la imagen y el texto generado (ahá, aqui si usamos el get a file). ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/11489c44933c4bb79441eb1d0fe128ff6c2e46b0ac744e78853ba19eb513899d)
- **LinkedIn** → Antes de publicar, pasa por un módulo **Traductor Título (IA) que es un modulo de ChatGPT Create a completion** para adaptar o traducir el título,

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/78c555424bae41ffbf0bb52619aa37277fe93ee8852644c5a9eec328129cdb55)

 y luego crea el post en LinkedIn

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5e49adbb992646668dd47ef904b9c2ccd794b90c994544d282d4442216b174a3-md.png)

---

## Qué consigues

- Publicaciones listas y automáticas en **3 redes sociales**.
- Siempre con la **imagen oficial de la noticia**.
- Flexibilidad: eliges el tema y la frecuencia.
- Ahorro de tiempo: todo se publica sin que tengas que entrar a cada red manualmente.

---

Más simple imposible: pones tu palabra clave, copias el JSON, lo pegas en Make y ya tienes noticias transformadas en contenido que se publica solito.
