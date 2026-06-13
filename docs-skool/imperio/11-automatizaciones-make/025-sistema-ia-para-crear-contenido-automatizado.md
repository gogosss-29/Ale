# 🔥 Sistema IA para Crear Contenido Automatizado

> Ruta: Automatizaciones Make › 🔥 Sistema IA para Crear Contenido Automatizado

**🎬 Vídeo (22.6 min):** https://www.youtube.com/watch?v=f3R7PxB2mfE

**📎 Recursos:**
- v2 (Actualizado) Sistema RRSS

---

## Guía Práctica para Automatizar Publicaciones en Redes Sociales Usando Make.com

En este tutorial, te mostraré cómo crear una automatización para publicar contenido en redes sociales de manera eficiente utilizando inteligencia artificial. Este método es ideal para quienes desean mantener una presencia constante en redes sociales sin dedicarle tiempo diariamente. Sigue estos pasos prácticos para configurar tu sistema automatizado.

### Paso 1: Crear un Google Sheet

1. **Crear un nuevo Google Sheet**: - Abre Google Sheets y crea una nueva hoja de cálculo.
- Nombra la hoja como "Contenido Redes Sociales" o cualquier título relevante.
- Añade una columna llamada "URL de Artículo".
2. **Agregar contenido inicial**:

- Introduce algunas URL de artículos recientes sobre tu industria o nicho en la columna "URL de Artículo" o "Link Noticia". ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/75d766b0f3ae42feacb2e9f4cef15d0568fa643279ea4ec188646a53fb9e482a)

### Paso 2: Vicular Google Sheets a Make

1. **Crear un nuevo escenario en Make**: - Ve a [Make.com](http://bencorde.com/make) y crea una nueva cuenta si no tienes una.
- Haz clic en "Crear nuevo escenario". ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f4e8d65bf7b04ee2925d4124d27ad45f64ba6e348f0e4f4fb884566a91308c64)
2. **Configurar el "trigger" o disparador de Google Sheets**: - Añade un módulo de Google Sheets.
- Selecciona "Watch New Rows" para que el escenario se active cada vez que se añada una nueva fila. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e6e5c8731aed411d9db640fcbad7c2a0522bcf6c3cf343f4b9b7f95788fb6144) - Conecta tu cuenta de Google y selecciona la hoja de cálculo creada anteriormente.
- Establece el límite en 1 para procesar un artículo a la vez.
- Configura el intervalo de ejecución a diario, por ejemplo, a las 10:00 AM.

### Paso 3: Configurar Perplexity e Incluir el API

1. **Crear una cuenta en Perplexity**: - [Regístrate en Perplexity](http://perplexity.a) y accede a tu cuenta.
2. **Obtener la clave API**: - Ve a la configuración de tu cuenta en Perplexity.
- Copia la clave API desde la sección correspondiente.
3. **Agregar el módulo de Perplexity en Make**: - En Make, añade un módulo de Perplexity, este será el que detecta el URL de la noticia.
- Selecciona "Create a Chat Completion". ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7a0f189a270a4972a9c79f694026281e8f03e60b2d0a49c0a92b6fd57c036925)
- Introduce la clave API y selecciona el modelo "Llama 3".
- En el contenido, pon: ```
"Resume este artículo:" [seguido de la referencia a la columna de URL del Google Sheet].
```

### Paso 4: Crear un Router

1. **Configurar el Router en Make**: - Añade un módulo de Router en Make. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9bc669b9c50145ed9d21b975664f395657d28d4332d0433b94dcc1dad64aaf5f)
- Este módulo permitirá dirigir los resultados hacia diferentes acciones (publicaciones en redes sociales).

### **Paso 5: Crear Asistentes Especializados para Cada Plataforma**

#### Ahora crearemos 4 modulos, cada uno cumplira una funcion para cada plataforma:

- Selecciona "OpenAI" y luego "Create a Completion". ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ffc1c80ab8b447eda0182c5fcc84e9bc3ce181bdc0104d48bef202878d66c876)
- Configura el modelo (GPT-4o) y el siguiente prompt:
- Crearemos el primer módulo para **Instagram**:

```
Actúa como un gerente de redes sociales y genera una publicación de INSTAGRAM. La publicación debe involucrar a la audiencia con una introducción atractiva, proporcionar detalles esenciales y fomentar la interacción a través de 'me gusta', comentarios y compartidos. Termina con un llamado a la acción claro y al final de todo pon la fuente. Incluye hashtags opcionales: [#Hashtag1, #Hashtag2]. NO INCLUYAS ** NI LOS HAGAS EN NEGRITA Aquí hay un resumen del artículo que quiero que readaptes: [INTRODUCE ARTICULO AQUI]Fuente: [INTRODUCE FUENTE AQUI]
```

- Repite el proceso anterior, cambiando el prompt para **Twitter**:

```
Actúa como un gerente de redes sociales y genera una publicación de TWITTER. La publicación debe involucrar a la audiencia con una introducción atractiva, proporcionar detalles esenciales y fomentar la interacción a través de 'me gusta', comentarios y compartidos. Termina con un llamado a la acción claro y al final de todo pon la fuente. Incluye hashtags opcionales: [#Hashtag1, #Hashtag2]. NO INCLUYAS ** NI LOS HAGAS EN NEGRITA Aquí hay un resumen del artículo que quiero que readaptes: [INTRODUCE ARTICULO AQUI]Fuente: [INTRODUCE FUENTE AQUI]
```

- Ahora para **LinkedIN:**

```
Actúa como un gerente de redes sociales y genera una publicación de LINKEDIN. La publicación debe involucrar a la audiencia con una introducción atractiva, proporcionar detalles esenciales y fomentar la interacción a través de 'me gusta', comentarios y compartidos. Termina con un llamado a la acción claro y al final de todo pon la fuente. Incluye hashtags opcionales: [#Hashtag1, #Hashtag2]. NO INCLUYAS ** NI LOS HAGAS EN NEGRITA Aquí hay un resumen del artículo que quiero que readaptes: [INTRODUCE ARTICULO AQUI]Fuente: [INTRODUCE FUENTE AQUI]
```

- Ahora para **Facebook:**

```
Actúa como un gerente de redes sociales y genera una publicación de FACEBOOK. La publicación debe involucrar a la audiencia con una introducción atractiva, proporcionar detalles esenciales y fomentar la interacción a través de 'me gusta', comentarios y compartidos. Termina con un llamado a la acción claro y al final de todo pon la fuente. Incluye hashtags opcionales: [#Hashtag1, #Hashtag2]. NO INCLUYAS ** NI LOS HAGAS EN NEGRITA. Aquí hay un resumen del artículo que quiero que readaptes: [INTRODUCE ARTICULO AQUI]Fuente: [INTRODUCE FUENTE AQUI]
```

### Paso 6: Generar Imágenes para Instagram

1. **Crear módulo de DALL-E en Make**: - Añade un módulo de OpenAI y selecciona "Generate an Image".
- Configura el prompt para generar una imagen relevante al artículo.

#### Paso 7: Conectar las Cuentas de Redes Sociales

1. **Configurar módulos de redes sociales**: - Conecta Make con tus cuentas de Facebook, Instagram, Twitter (X) y LinkedIn.
- Configura cada módulo para publicar el contenido generado.
2. **Establecer la programación**: - Configura cada módulo para publicar a la hora y frecuencia deseada.

Siguiendo estos pasos, puedes crear una automatización para mantener tus redes sociales activas con contenido actualizado y relevante, sin necesidad de intervención diaria. Este método no solo ahorra tiempo, sino que también garantiza una presencia constante y profesional en todas tus plataformas.

Para cualquier duda o para descargar las plantillas y recursos, no temas en preguntar.
