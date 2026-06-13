# 🚵 Extrae Publicaciones de Grupos de Facebook

> Ruta: Automatizaciones Make › 🚵 Extrae Publicaciones de Grupos de Facebook

**🎬 Vídeo (36.0 min):** https://youtu.be/zSPvxqSc3kc

**📎 Recursos:**
- A) Correr FB Group Scraper
- B) Mirar FB Group Scraper

---

# Cómo extraer y analizar publicaciones & dolores de grupos de Facebook con Apify

En este tutorial vamos a construir un sistema automatizado para **extraer publicaciones de uno o varios grupos de Facebook**, analizarlas y transformarlas en un reporte que llega directo a tu correo con la frecuencia que quieras. Todo con la ayuda de **Apify** y un flujo de automatización en Make.

---

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c9e32472d12544159e2d177406c765567859cbeffd3d419eaa4d4c8798a19bf5-md.png)

## Paso 0: Habilitar el actor en Apify

Antes de armar nada en Make, primero debemos **activar el actor en Apify**:

1. Entra al actor Facebook Groups Scraper.
2. Haz clic en **“Create Task”**.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8d97b6c1114a49ae97f18c2685b846c13fd4340705fc4d7f97cefebfee044faf)

1. Esto creará una **tarea asociada a tu cuenta** y hará que el actor esté disponible después en [Make.com](http://Make.com).

---

## Escenario 1: Ejecutar el actor con la frecuencia que quieras

El primer escenario es el que lanza el scraper con la periodicidad que definamos.

- Entra al actor de Apify: [Facebook Groups Scraper – Input JSON](https://console.apify.com/actors/2chN8UQcH1CfxLRNE/input).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ff8167e565894d7783d011343ba257a35e415a63788d4d368957a7dbafd7513d)

- **Reemplaza** las variables que quieres dejar como base: - Las **URLs de los grupos** que quieres analizar (`startUrls`).
- El **número de publicaciones** que quieres traer por ejecución (`resultsLimit`).
- **Haz clic en JSON y copia todo el código JSON** resultante.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e5a892ed10be4b3f97f0b8b50b11029cb562fdca1d094017a394454458772d12)

- En **Make**, crea un nuevo escenario, y en el módulo **Run Actor**, ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1a99d51bfe534b5281494f11841eecd607d4b1cdbc9347578dd6fa29befafec8) selecciona el actor y pega ese JSON en **Input**, define la **frecuencia** (diario, semanal, etc.). Listo, ese escenario dispara el scraper con tu configuración y deja los resultados en un dataset para el escenario 2.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/716e22a4b7db43dfbcdd39f783f6740eac4ac172f4ad4235994d7793222b66f7)

- define la **frecuencia** (diario, semanal, etc.). Listo, ese escenario dispara el scraper con tu configuración y deja los resultados en un dataset para el escenario 2.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b57bef83a7ca49e994c9558991d8aab79d48b66e6f0045188772a6cb8a80d912)

---

## Escenario 2: Extraer y analizar la data automáticamente

Una vez que el actor termina su trabajo, se activa el segundo escenario: **recoger, analizar y enviar la información**.

### Flujo de trabajo:

- **Webhook de Apify**: se dispara cuando el actor termina (el del escenario 1).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/513f68756c414146b2b9e404930aac2293db74dd42fb4f3e869ce4aaae6e91cd)

- **Get Dataset Items:** traemos los ítems en JSON (publicaciones, usuario, fecha, texto, URL).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1f788b45ccd5454a86e3d48642a49d95560ba871e5a0419ab6bbf4ac6cad6f8e)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/154ff1812792468db0ba24b38de9dbbfacb070a330c34d3b83afa9d4bf55bea5)

- **Agregador de texto**: unimos todas las publicaciones en un bloque legible.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a7b78f3206814dcab00e22e56e48225a72bb8df3a6014732a6b8967c9f01abd4)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/80d26d4ee1d5457a9516d851c9ba2a8b04836c78dd084d8690751b8bf2d0b01f)

- **Análisis con IA**: se detectan los dolores y se agrupan en 3 categorías, asignando a cada uno un **índice de potencial (1–10)** según urgencia y oportunidad.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/12b876d4b43e435b8e6a0ae5c95e1b4940b1193e1168492e9220da1ee037b0b8)

- ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b66fdc0bd43e49b4bad61105727ce19399cb411585834a579f171dac3950aaaa) > Cuales son dolores o problemas comunes que se enfrenta toda esta gente? Estas son publicaciones de un grupo
> 
> Este es el JSON con informacion, clasificame todo. 
> 
> Tomaremos toda la informacion y las clasificaremos en 3 variables o clasificaciones. Si alguna publicacion no clasifica en estas variables, NO la trates de forzar a meterla en una, simplemente "no aplica". Agruparás las que hacen sentido.
> 
> A cada problema o dolor, le asignaremos un indice de "potencial", que es una combinacion entre urgencia, oportunidad y potencial de capitalizacion entre 1 y 10. El valor 1 es MUY bajo potencial y el 10 ALTISIMO potencial.
> 
> El contenido de las publicaciones es:
> 
> {{26.text}} ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a57cfb253f6648c284692d6b2d519e20aca3093354da42778b6b4bf8144fc4da)
- **(PASO OPCIONAL) Extracción de variables**: convertimos el análisis en datos claros (problema 1, problema 2, problema 3, totales y no aplica). Esto es util solo si quieres despues pasar los datos a uin google sheets, o armar una especie de dashboard historico, y o agrupar los dolroes en variables mas generales.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cdf2e59867044505af8c3443911e3d0839090491215b46c1bc52201a8a31f8d6)

- ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/11b65d92cb1f4b9c84e872f368f94eff1899ea324dbd4b36838334ca872899a3-md.png) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3e67f88ffde2499cb6568cd941e292949ca0136b548946b4869e42a7b434e273) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cfda17581c1c4b05a4065d2df7db9b900cd95866cd8a40a4b2fc3260bea30937) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8c99c2064e03495eb50d2010985fb9e6710987aca31c4d6085ac93e0480a533e) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/68faaae91e9f4e1cad27cd32b4cab0ea21cce43e433f4fdd8a7d8c369220898d) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/42cda60f33cc4052a98290c9f15fd388519eadd7edab4c299514d0a8abce5366)
- **(Opcional) Registro en Google Sheets**: añadimos los resultados en una hoja para seguir el progreso semana a semana.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a474b1a18f3c478cab6caa45a458d06708bb91794db74f278712a07a765da842)

- ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/63071fdeb829440895ebcb6de1dc01613e0ceee101374caeb8971537e4bdeff2)
- **Generador de HTML**: redactamos automáticamente un cuerpo de correo con los problemas principales y ejemplos de publicaciones. Aqui peudes usar el "Request Anything" de Make, o usar el "Create a Completion" de OpenAI. Mi recomendacion, si quieres un output mas estetico, usa el create a completion. Si quieres uno mas economico, usa el request anything.,

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/71da6e7a68dd49a7b5602df23e1400f54329dab4d2204e65b0c5542f994bb950)

> Convierteme este texto en un informe especifico para Benja, semanal indicando los insights y los reportes que logramos sacar especifico de los dolores de las personas.
> 
> ##Tu output será en HTML. Solo el cuerpo del correo electrónico. 
> 
> ##Tu output será estéticamente MUY atractivo, con uso de colores y lenguaje super cercano y natural
> 
> Usa varios espacios para que se vea ordenado y esjemplifica con links y casos específicos de los dolores de las personas.
> 
> Estos son los dolores (contexto):
> 
> {{8.problema_1}}: {{8.cantidad_problema_1}}
> 
> {{8.problema_2}}:{{8.cantidad_problema_2}}
> 
> {{8.problema_3}}:{{8.cantidad_problema_3}}
> 
> Aqui hay mas contexto mas especifico
> 
> {{5.result}}

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6776ecc8a2df436db90e730eb27bd620913c7709a75d48a4a92feb87b3f4e4f0-md.png)

- **Email automático**: enviamos un informe con el resumen, directo a tu bandeja.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8a10adf694a64669bac0f7062c058689b136887d29b447119b5eb43dc9609aab)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/89f38ae68bec40ce93e0fa17acbaed20c5604102be334272b1c383b07dcef9ca)

---

Output:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/60b8e8842357413992f2108c3540ba66c252144bf628461b8c4102a28b6aac9e-md.png)

## ¿Qué ganamos con este sistema?

- **Levantar dolores reales** de comunidades en Facebook.
- **Analizar uno o más grupos a la vez**, con total flexibilidad.
- **Detectar oportunidades de negocio** a partir de lo que la gente pide, reclama o necesita.
- **Monitoreo constante**, con la frecuencia que tú definas.
- **Automatización total**, sin tener que entrar manualmente a los grupos: los reportes llegan por correo y se registran en Sheets.

---

## URL principal del actor

- Facebook Groups Scraper: [Facebook Groups Scraper](https://console.apify.com/actors/2chN8UQcH1CfxLRNE/input)
