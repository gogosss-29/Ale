# 🔍 Analiza Ads de Facebook de tu Competencia

> Ruta: Automatizaciones Make › 🔍 Analiza Ads de Facebook de tu Competencia

**🎬 Vídeo (23.6 min):** https://www.youtube.com/watch?v=7dK71uG40Og

**📎 Recursos:**
- A) Correr FB Ads Library
- B) Mirar FB Ads Library

---

# Cómo automatizar el análisis de competencia en Facebook Ads con Make + Apify

En marketing digital, **entender lo que está haciendo tu competencia en Facebook Ads** puede ser la diferencia entre reaccionar tarde o anticiparte con mejores campañas. Por suerte, hoy no necesitas pasar horas revisando manualmente la Facebook Ads Library: puedes automatizar todo el proceso con **Make** y el **Facebook Ads Library Scraper de Apify**.

En este artículo te muestro cómo lo resolvimos con **dos escenarios simples**, que terminan entregándote un informe semanal de tu competencia directo en tu correo o el de tu cliente.

---

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f8b248c612304f10b60123fcec793ea6e3bad907719d41f8a1dd3bb0d1c4360f-md.png)

## Paso 0 – Habilitar el actor en Apify

Antes de construir nada en Make, tienes que habilitar el actor en Apify:

1. Entra al actor: [Facebook Ads Library Scraper – Input JSON](https://console.apify.com/actors/XtaWFhbtfxyzqrFmd/input).
2. Haz clic en **“Create Task”**.
3. Esto creará una tarea asociada a tu cuenta y hará que el actor quede disponible en [Make.com](http://Make.com).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b481eeea2ecb4bcd8f92b394e8fe7844ba7318dfcfe749fe98982d8ad50faeeb)

1. Esto creará una **tarea asociada a tu cuenta** y hará que el actor esté disponible después en [Make.com](http://Make.com).

---

## Escenario 1 – Correr el Scraper en la frecuencia que quieras

El primer escenario es el que lanza el scraper con la periodicidad que definamos.

- El primer escenario es directo: se encarga de **ejecutar el scraper de Apify** con la frecuencia que definas (diaria, semanal, varias veces al día, etc.).
- Este scraper extrae los anuncios publicados en la **Facebook Ads Library**, con toda la información relevante: página, URL, título, descripción, cuerpo del anuncio, fecha de inicio, etc. Rellena con la cantidad de páginas o URL's que quieras. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9aa0e6d0a884489abddeaafdc02d55868c9e38e9a1dd455faf60bd191c70b55b-md.png) Los URL los puedes encontrar aquí: [https://www.facebook.com/ads/library](https://www.facebook.com/ads/library) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2304a64815614ffb9be7279330bbd9d2138452fada5e4652b48ff88a35a9ec3c-md.png) Y puedes buscar por cuenta ("Lego" por ejemplo) o por palabra clave ("inteligencia artificial" por ejemplo).  ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8fdf0202ea204d15bbcbbb0d485dd5223110e15b17cb44e880bad9ef622be957-md.png) Copias la URL y la pegas  ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2a9d50679914401aa4f5b9049ba5fa55bf31cdb9d91f411c861705b98971d0c9) **Reemplaza las variables** que quieres dejar como base en el JSON:
- Haz clic en **JSON** y copia todo el código resultante. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/42fa10e1336d43d5acc35cda7a1e7c6019faeb83fcb843dd95dbb606ecfc5169-md.png) En **Make**, crea un nuevo escenario, y en el módulo **Run Actor**, ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b6d2c1ad9f8449298c99429625f12f0cc7a0023e5a0e46edad47a180a2759bcc) Selecciona el actor y pega ese JSON en **Input**, define la **frecuencia** (diario, semanal, etc.). Listo, ese escenario dispara el scraper con tu configuración y deja los resultados en un dataset para el escenario 2.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2d393160b1ce421f9a55b0bb9c0b9497ed88a14128e34505922c35d6517c9ae8)

- define la **frecuencia** (diario, semanal, etc.). Listo, ese escenario dispara el scraper con tu configuración y deja los resultados en un dataset para el escenario 2.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/051a7c34e37649f4a3a10b2821e70e1287819c155ce8451884b5d127bb3a1380)

---

## Escenario 2 – Procesar, agrupar y enviar informe

#### El segundo escenario es donde ocurre la magia. Se compone de **cinco módulos**, cada uno con una función clara:

- **Mirar Actor** → Se activa cuando el scraper terminó de correr.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/90c86f0b6c384598b4e0d2c4a337029109c09a4aa02f45fca380b2e6ed8c6707)

- **Extraer Ads** → Descarga los datos de la corrida (los anuncios capturados).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b80771c67f9b4368ab1e8df2b8638273d0cbae97c1d04a648468ce7298f5c3b3)

- **Agrupar en Texto** → Convierte los datos en un formato legible: ```
Página: {{2.snapshot.current_page_name}} URL: {{2.url}} Título: {{2.snapshot.title}} Link Description: {{2.snapshot.link_description}} Cuerpo: {{2.snapshot.body.text}} {{2.start_date_formatted}}
``` ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/674625646e804bc1854b7fd32eb5a1a3d6e9938e77564ea1b78fc8db0d11982e)
- **Clasificar + Redactar** → Con ayuda de IA, genera un **análisis de competencia en HTML**, evaluando qué están haciendo tus competidores, cuáles son sus enfoques y qué podrías replicar o diferenciar.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f43e114e69174bbab4900cca4409e1bc747bd351e24d45cfada43b4cf412d287-md.png)

```
Tu rol es crear un informe de los cambios que se han hecho en los ultimos 7 dias como analisis de competencia.
Te dare una seried einformacion, y diras solamente de los ultimos 7 dias, no antes, de los cambios que se han hecho, ya que es un update semanal. Tu output sera en HTML y haras el analisis de competencia. Luego daras y redactaras tood en HTML y actuaras como un media buyer. Diras tipo la competencia está haciendo esto... tu podrías hacer un approach parecido o no... emite juicio. Primero daras solamnente la informacion, cuanto tiempo lleva, que approach tienen, el link de cada uno, etc. 

#Tu output sera HTML.

Contexto del contenido: {{31.text}}

Fin del contexto.
```

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/54cd96434e9c488ba78394bf53b3b583f6e0c2ba1ae14022b12f585d9919e947-md.png)

- **Enviar Correo** → Te manda el informe final por email, con asunto “Actualización Semanal Anuncios”.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f26889e9058f44a18f0612d9d4aff2bec3aa3a21deaf4bf2992c0ced5f040420)

---

## El resultado: cada semana recibes un **resumen curado de lo que está testeando y publicando tu competencia**.

---

## ¿Para qué sirve esto?

- **Investigación de la competencia** → Entiendes su ángulo creativo, ofertas y frecuencia.
- **Monitoreo constante** → Te mantiene al día con cambios semanales en sus campañas.
- **Servicio para clientes** → Puedes empaquetarlo como un **servicio premium**: enviar reportes semanales de la competencia a marcas que quieran estar informadas.
- **Inspiración creativa** → Saber qué funciona (o qué no) en tu industria, para iterar más rápido.
