# 🌐Automatiza un Blog de WordPress Make + ChatGPT

> Ruta: Automatizaciones Make › 🌐Automatiza un Blog de WordPress Make + ChatGPT

**🎬 Vídeo (35.6 min):** https://youtu.be/fQmUR-jIzZ0

**📎 Recursos:**
- Make (Sheets + Wordpress + OpenAI)
- Make (RSS + Wordpress + OpenAI)

---

Si sientes que crear contenido para tu blog consume más tiempo del que tienes, este post es para ti. Hoy te voy a mostrar cómo puedes **automatizar completamente tu blog en WordPress**, usando herramientas de automatización e inteligencia artificial que hacen el trabajo pesado por ti. Desde generar contenido hasta publicarlo con imágenes, todo el proceso es **100% automático**.

Vamos al grano: te voy a enseñar dos métodos distintos para lograrlo, y te voy a contar por qué el módulo **Text to Structured Data** es un cambio de juego en este tipo de flujos.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/30f935e6c4884af9a545cefe19f804b36087d02486e547c9ae2e621c52728eeb-md.png)

---

## **¿Por qué deberías automatizar tu blog?**

- **Tiempo libre para lo importante**: Te olvidas de las tareas repetitivas, y puedes enfocarte en lo estratégico (tu oferta, tu newsletter o tu negocio).
- **Tráfico constante**: Publicaciones regulares que traen visitas orgánicas a tu sitio.
- **Fácil de escalar**: Una vez que lo configuras, puedes replicarlo para varios nichos.

---

## **Cómo funciona esta automatización**

Vamos a usar [**Make.com**](http://Make.com), una herramienta que conecta más de 10,000 aplicaciones para crear flujos de trabajo automáticos. Este será el corazón del sistema. Además, combinaremos:

- **Google Sheets**: Para almacenar los títulos o URLs que quieras usar como base (**RSS Feeds**: Método alternativo para trabajar con noticias en tiempo real.)
- **Perplexity AI**: Para generar resúmenes desde URLs.
- **OpenAI (ChatGPT y DALL-E)**: Para personalizar el contenido con tu tono de voz y generar imágenes.
- **WordPress**: Donde todo se publica automáticamente.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/aa5c6015b9bd4815a1c6e9c70e0232d165b21d2c1afc401183e03c225c648ac6-md.png)

---

#### ***Nota: Recuerda que puedes descargar e importar las automatizaciones al final de esta guía.***

## **Paso a paso para automatizar tu blog**

### **1. Configura **[**Make.com**](http://Make.com)

- Crea un escenario en [Make.com](http://Make.com).
- Usa Google Sheets como disparador. Cada vez que agregues un nuevo link en tu hoja, se activará la automatización.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c716bda3a94543118d8f5a25e2d6329c91dddba80fa14944b31f0944f2efb4a1)

### 2. Configura el módulo de Perplexity para que resuma el contenido del enlace.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6afa58f088b7452a9821b4ce8c0262f4253c15a2ccec40df982f8100431fc441-md.png)

---

### **3. Personaliza el contenido con tu tono de voz**

Esto es clave. Usaremos un agente en OpenAI que adapta el contenido al estilo que tú quieras. Así, no parecerá un texto genérico, sino algo que tú mismo escribirías. Aquí tenemos[ una guía para configurar este agente](https://www.skool.com/imperio-digital/classroom/a65de4cd?md=7132612be2564c469e7a0ced8afbb7e4), pero básicamente se entrena con ejemplos de tu propia escritura. Usaremos el módulo de "Message an assistant"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/09bd55ad8f4e448b81a247f0917b92389f5a866bf3564e679abb67ab81eac093-md.png)

Por ejemplo:

- Prefiero usar "tú" en vez de "usted".
- Hacer las oraciones claras y en voz activa.

El resultado es un contenido que se siente auténtico, pero generado automáticamente.

---

### **4. Optimización SEO y formato HTML (message an assistant)**

Con otro agente en OpenAI, transformamos el texto para que siga las mejores prácticas de SEO y lo convertimos en formato HTML. Las instrucciones de este agente / asistente las puedes encontrar aquí, también te dejo el prompt aquí abajito:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/58c1df1c3d224e5793cd0ec58883d48a4319997974d246a39da0bde2edf64c95-md.png)

[Agente de SEO para Blogs - Automatizaciones · Imperio Digital](https://www.skool.com/imperio-digital/classroom/a65de4cd?md=5c87216c72ec45cd9e424b218f968e82)

###   
**5. Text to Structured Data: El módulo estrella**

Este paso es donde realmente pasa la magia. Usamos el módulo **Text to Structured Data** para separar el contenido en:

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/61da9d468e724efa9a70643cd9dd36896f5fa0af75f24f3d9dc492f691fede66)

- **Título**: Lo que aparecerá en la cabecera del post.
- **Cuerpo**: El contenido completo, en HTML.

Esto facilita que WordPress pueda recibir cada elemento y publicarlo exactamente donde debe ir.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d870a50102264b2f8d4abfdb3d303be378ddb5aefc2247e2996bdb258bef4fba-md.png)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/69127f936a684afbb4a771be84ed9254bad270ca97904b5392096281ed30abf0)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f77107d113a649b6b58d9c7ba3efeff3785909a117e14e0ba6a7bd484b417c28)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/74a4b907e6384451aa72d43801f235a8013a63de16ce4d1ab2a8903daa99e4ff)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9c26774a10d447fdac95f868f66764f8a8ab4342fd694f22adf0b05a277dfbf0)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7f7849b6575148348de898b17b116b5d564d699461dc479397f0b637f65287b7)

---

### **6. Genera una imagen personalizada**

Para que tu blog luzca profesional, generamos una imagen relevante con **DALL-E 3**. Puedes usar prompts simples como: "Crea una imagen para un artículo sobre el mercado de criptomonedas". Este paso eleva la calidad visual de tus publicaciones, pero también podrías usar otros generadores de imágenes como Flux si quieres resultados más realistas.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9c44f228ef8b459ba405092894d789833d899561616749299a7e21ed127ec549)

---

### **7. Publica en WordPress automáticamente**

Conecta tu WordPress a [Make.com](http://Make.com) usando el plugin **Make Connector**. Desde ahí, configuras la automatización para que cada post tenga:

- Su título.
- Su cuerpo.
- Su imagen.
- Su estado (puedes publicarlo directamente o dejarlo como borrador).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cb68a7a233ab44d59839a07e9aec235e74b67c46e0604f3e949af2135471e60e)

Aquí le pondremos en texto para que no nos salga escrito el URL y se vea la iamgen, el siguiente código HTML que reemplazaremos el [URL] por la variable URL.

> <img src = "[URL]">

---

## **Método alternativo: Trabajar con RSS Feeds**

¿Quieres publicar contenido fresco y relevante en tiempo real? Usa **RSS Feeds**:

1. Crea un feed personalizado en [**rss.app**](http://rss.app).
2. Configúralo como disparador en [Make.com](http://Make.com).
3. Resúmelo y personalízalo con los mismos pasos que vimos antes.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/543987f8a752459d9b76311e10f414817fa2cb6f785f40829c240fb2ed7addaa)

Usaremos "Watch" si queremos que tome los artículos a futuro que se publicarán en un nicho en específico

Usaremos "Retrieve" si queremos tomar artículos que ya han sido previamente publicados.

Esto es ideal si tu blog se enfoca en noticias de nicho, como criptomonedas, inteligencia artificial o tecnología.  
  
Si quieres más información sobre RSS, tenemos [una automatización aquí ](https://www.skool.com/imperio-digital/classroom/a65de4cd?md=5c87216c72ec45cd9e424b218f968e82)que la cubre más a detalle.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3b94106d4fff40428004588b1ca81ec24488c33b07dd45c98f51d6837622c9d6-md.png)

---

## **¿Por qué este sistema es tan potente?**

La combinación de **Text to Structured Data**, personalización de tono de voz y optimización SEO te da una ventaja brutal:

- Tu blog no solo será automático, sino que también **se verá y se sentirá profesional**.
- Todo el proceso está diseñado para que incluso alguien sin experiencia pueda configurarlo.

---

## **Recuerda que...**

- Puedes descargar esta automatización completa con un clic aquí abajito.
