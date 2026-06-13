# ⭐️ Extraer y analizar reseñas de Amazon con Apify

> Ruta: Automatizaciones Make › ⭐️ Extraer y analizar reseñas de Amazon con Apify

**🎬 Vídeo (29.2 min):** https://youtu.be/U7yrtOu_omU

**📎 Recursos:**
- A) Correr Amazon Scraper
- B) Mirar Amazon Scraper

---

# Cómo extraer y analizar reseñas & dolores de productos de Amazon con Apify

En este tutorial vamos a construir un sistema automatizado para **extraer reseñas de Amazon**, analizarlas y transformarlas en un reporte que llega directo a tu correo con la frecuencia que quieras. Todo con la ayuda de **Apify** y un flujo de automatización en Make.

---

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0e80d6374a0c4a5f991216f7b28b1cfc9ae84f74e50e47468a43c3784ed02243-md.png)

## Paso 0: Habilitar el actor en Apify

Antes de armar nada en Make, primero debemos **activar el actor en Apify**:

1. Entra al actor Amazon Reviews Scraper.
2. Haz clic en **“Create Task”**.
3. Esto creará una **tarea asociada a tu cuenta** y hará que el actor esté disponible después en [Make.com](http://Make.com).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5bef4538cfbd4f22a688e032fbd727d80ce94a5130584e97b05cfa29580184c4)

1. Esto creará una **tarea asociada a tu cuenta** y hará que el actor esté disponible después en [Make.com](http://Make.com).

---

## Escenario 1: Ejecutar el actor con la frecuencia que quieras

El primer escenario es el que lanza el scraper con la periodicidad que definamos.

- Entra al actor de Apify:[ ](https://console.apify.com/actors/R8WeJwLuzLZ6g4Bkk/input)[**Amazon Reviews Scraper – Input JSON**](https://console.apify.com/actors/R8WeJwLuzLZ6g4Bkk/input)[.](https://console.apify.com/actors/R8WeJwLuzLZ6g4Bkk/input) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c4bfcca2514243c9a9e7d037c40ccb544cb7a230629a47e7ad2a120dbbbfb025-md.png)
- **Reemplaza las variables** que quieres dejar como base en el JSON: - Las **URLs de productos de Amazon** que quieres analizar (`productUrls`).
- El **número de reseñas** que quieres traer por ejecución (`maxReviews`).
- Opcionalmente, los **filtros por rating** (`filterByRatings`, por ejemplo `"twoStar"`, `"threeStar"`, etc.).
- Haz clic en **JSON** y copia todo el código resultante.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7601a013cd894a3c8d45dc3be7c1bbbc947c4a0fd9c74f8abfde89c44653f4be)

- En **Make**, crea un nuevo escenario, y en el módulo **Run Actor**, ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0a1ae954e8de49dbb106f9ce21ad97cfd8c3ef17f6b74352a2c536d95be92fd6) Selecciona el actor y pega ese JSON en **Input**, define la **frecuencia** (diario, semanal, etc.). Listo, ese escenario dispara el scraper con tu configuración y deja los resultados en un dataset para el escenario 2.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/79fb604692fd4177ad701cc579c1d02592f68fa39dbc42e1bc6efd9cbb1f7e56)

- define la **frecuencia** (diario, semanal, etc.). Listo, ese escenario dispara el scraper con tu configuración y deja los resultados en un dataset para el escenario 2.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f9454c006862412183ad3c9f2ad8c81544cd3fededb346188db9c0cb2184acd1)

---

## Escenario 2: Extraer y analizar la data automáticamente

Una vez que el actor termina su trabajo, se activa el segundo escenario: **recoger, analizar y enviar la información**.

### Flujo de trabajo:

- **Webhook de Apify**: se dispara cuando el actor termina (el del escenario 1).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/678a786a1e944774819d499cd05bee150e3328baa9bf4f4e890f5820a94a938c)

- **Get Dataset Items**: traemos los ítems en JSON (título de la reseña, puntuación, autor, fecha, texto, URL).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8db61521fd0f4d049773f28e2e55decac9a1ec672afc4944b287cadfe835a585)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/20989aa27ba948389c78db99fcd5173f3ff7ef0e73d0440daab6e5ab2cfd5f7a)

- **Agregador de texto**: unimos todas las reseñas en un bloque legible.

- ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/eaf731de93294b8285e30688b248b62927772e5d14b14e1981b9c7d41e23c5d9)
- **Análisis con IA**: se detectan los dolores y se agrupan en 3 categorías, asignando a cada uno un **índice de potencial (1–10)** según urgencia y oportunidad.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/31394c701eef4e80891e59eaec931c427a30b5bd5e084438b361d6d057273227)

- ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/218cfedcd30743d1b757e62f3fc0f35d067ac6d866ed45dfabe02515431483cb) > Analiza las siguientes reviews de Amazon y detecta:
> 
> Problemas o dolores: quejas, insatisfacciones o puntos negativos mencionados.
> 
> Oportunidades de mejora: ideas para mejorar el producto, servicio o experiencia.
> 
> Ideas de contenido: temas o enfoques que podrían usarse para generar piezas de contenido basado en estos dolores.
> 
> A cada problema u oportunidad asígnale un potencial (1 a 10) considerando urgencia, impacto y rentabilidad. 
> 
> Además, harás una categorización o agrupación / reduccion a 3 problemas principales y sus cantidades por reseña. Si no clasifican, no las agruparas innecesariamente. Te dejo las reseñas a analizar aquí:
> 
> {{25.text}} ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ab403c99d6114c319f1c262cbe3cd6ca96102e3eddd44d818c5a74210f0f6d21)
- **(Opcional) Extracción de variables**: convertimos el análisis en datos claros (problema 1, problema 2, problema 3, totales y no aplica). Esto permite después enviarlo a Google Sheets o armar un dashboard histórico.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ae766295556a46c7b26dd5996c68c1cf9eb0e1a3121644948377b5e78c99508a)

- ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f0558643309b42209558a81af6f2f0aa9c4f2842184a41d9b4442eba889cc6a5) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/16ac636305d24348801b625aab1ebc2936169c10215f4a30a3d92750803eb0ad) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/495a9b49b44847aabdfcac64e23947433bb52884df5b4918bfc4627b31aea9d9-md.png) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/18f4548300a74dc48f68e19e43df92cd7adba2850b684d778b01b95bc26460ad) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/192e008d768e447790cb40a8b3c2abd23a209d1165a74d8a8fc5aaefc457dcdc) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/99e32759662b45f29deda05f490c0b89e8b6d74d669a4faa80cd90e897698838) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/17c3161349634ca2b019e944197710bd0d3939d2582f40638fd5f678ddec5326) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d38b74f51c0a411cb6acc29af0018b4952ab09a0860f45feb7096711e6ff5072)
- **(Opcional) Registro en Google Sheets**: añadimos los resultados en una hoja para seguir el progreso semana a semana.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/673ebf35cff74de88faa4c67b25733fc6138d16013c54c4b84f9c19ee884b8f5)

- ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/825abedb889e48c88a240f234a02d714986a0e9af4c54be19dd7e394d268686f)
- **Generador de HTML**: redactamos automáticamente un cuerpo de correo con los problemas principales y ejemplos de reseñas **(request anything de Make AI Tools) o tambien podemos usar el "Create a Completion" de OpenAI si queremos un mejor output a un mayor costo.**

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/de0afb58ee4d4964a46536a59067117d4edb61b4487f4094936a74e67f5130e5)

- ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/93e483f7bede4f5d8bf80f3d3ca87fc200a19b9465bf4fcf9ae8aa1b0dca5127) Alternativamente podemos usar el modulo de "Create A Completion" de OpenAI si queremos un mejro informe.
- **Email automático**: enviamos un informe con el resumen, directo a tu bandeja.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/101490e04cab414c9bfbc59a98b49295e7b9d82cc7734b0181bf4fcb882d7aa2)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3b2033c0cf7b4c818785bc20b1f77cb768aeedd72bc943c892bc1c931ec4a4f6)

---

## ¿Qué ganamos con este sistema?

- **Levantar dolores reales de clientes** a partir de reseñas en Amazon.
- **Analizar uno o más productos a la vez**, con total flexibilidad.
- **Detectar oportunidades de mejora o negocio** en base a experiencias reales.
- **Monitoreo constante**, con la frecuencia que tú definas.
- **Automatización total**, sin tener que revisar manualmente cada reseña: los reportes llegan por correo y se registran en Sheets.

---

## URL principal del actor

- Amazon Reviews Scraper: [Amazon Reviews Scraper](https://console.apify.com/actors/R8WeJwLuzLZ6g4Bkk/input)
