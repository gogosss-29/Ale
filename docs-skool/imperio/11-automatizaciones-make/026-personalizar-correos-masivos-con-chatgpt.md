# 📧 Personalizar Correos Masivos con ChatGPT

> Ruta: Automatizaciones Make › 📧 Personalizar Correos Masivos con ChatGPT

**🎬 Vídeo (18.7 min):** https://www.youtube.com/watch?v=dbETsmaJ_QQ&t=16s

**📎 Recursos:**
- Mails Personalizados Assistant v2

---

## Bienvenidos y Bienvenidas Nuevamente

Hoy les voy a mostrar una automatización sencilla para poder contactar a leads o clientes potenciales, enviándoles un mensaje personalizado a cada uno. Vamos a suponer que tenemos una agencia de marketing digital y queremos contactar a gente de un nicho específico. Dentro de este nicho existen subnichos, así que trabajaremos con una lista de personal trainers especializados en distintos subnichos (pérdida de grasa, ganancia de músculo, etc.). La idea es enviarles un mensaje automatizado y escrito con ChatGPT, explicándoles por qué nuestra agencia de marketing digital es la mejor opción para su nicho en particular.

## Vista General

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/66c2bd594b4849a3be1f299c856d8a46c1b97ba41a9a4aeaa5a1b16fa68b17cb)

Antes de mostrarles cómo crear todo paso a paso, les voy a presentar una imagen general de lo que vamos a hacer. Utilizaremos Google Sheets para juntar la lista de leads, redactar un mensaje personalizado a cada uno y luego enviarles un email. Si ya tienes una lista de clientes potenciales o un formulario que las personas van rellenando, puedes usar este método para enviarles un mail personalizado cada vez que lo rellenen.

## Paso a Paso

### 1. Buscar y Crear Tabla de Leads

Buscamos en Google "personal trainers en España" utilizando operadores "OR" para obtener resultados más específicos. Por ejemplo:

#### Búsqueda en Google:

```
"profesión o nicho" "@gmail.com" OR "@outlook.com" OR "@yahoo.com"
```

(Más detalles sobre esto en la publicación anterior "[Guía para Generar Leads y Automatizar Mails con IA](https://www.skool.com/imperio-digital/classroom/a65de4cd?md=fb8c8f5919674366a88747bf287d15b3)")

Copiamos los resultados en ChatGPT para generar una tabla que incluya nombre, usuario de Instagram, email, nicho y una frase descriptiva (One Liner).

#### Prompt para ChatGPT:

```
Necesito que me hagas una tabla donde incluyas las siguientes columnas: nombre de la persona, usuario de Instagram, email de contacto, nicho en el que se encuentran y un One Liner que describa su negocio.
```

Pegamos la tabla generada en Google Sheets.

### 2. Crear un Prompt para un Asistente Especializado en ChatGPT

Le asignamos un rol a ChatGPT para que nos ayude con la redacción de los emails. Aquí mencionamos que hay un asistente que te ayuda a crear asistentes (sí, como escuchaste). Puedes usar este enlace para acceder al creador de asistentes: [Assistant Creator for API](https://platform.openai.com/playground/assistants).

#### Código para Crear el Asistente:

`Necesito que me ayudes a crear un asistente especializado en ventas para [agencia/empresa/] donde nos dedicamos a [contexto y servicios/productos]. Tu tarea principal es redactar mensajes breves y efectivos para atraer leads. La estructura del mensaje debe ser: Situación actual, dónde quieren llegar y qué sienten que les falta para lograrlo. Ejemplo de mensaje: Hola [Nombre], me encanta el enfoque que tienes en [Instagram/negocio], especialmente [detalle]. Soy [Nombre], fundador de [Agencia]. Estoy interesado en tus metas para [objetivo]. ¿Qué pasos consideras que te faltan para lograrlo?`

Esto nos dará el prompt para el asistente que usaremos como instrucción base cuando creemos el assistant.

### 3. Crear el Asistente en OpenAI Playground

Vamos a OpenAI Playground bajo la sección "Assistants" para crear el asistente. Puedes acceder a la plataforma desde aquí: [OpenAI Playground](https://platform.openai.com/playground/assistants).

#### Pasos en OpenAI Playground:

1. Accede a la sección "Assistants".
2. Crea un nuevo asistente y proporciona las instrucciones detalladas o el prompt que creamos anteriormente en ChatGPT.
3. Selecciona la versión de GPT que prefieras (por ejemplo, GPT-4).
4. Puedes probarlo en la parte de la derecha hasta que te comience a dar las opciones y resultados que deseas.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9e7e523267ac4455b82c670471202bac9da509248b9e495aa2d03faf893d8bbb-md.png)

### 4. Conectar el Asistente con Herramientas de Automatización

Usamos Make.com para conectar ChatGPT con Google Sheets y enviar los correos electrónicos personalizados automatizados.

#### Secuencia para Make.com:

1. En Make.com, seleccionamos Google Sheets y configuramos "Watch New Rows" para monitorear la hoja en la que tenemos los leads.
2. Seleccionamos la hoja de datos y especificamos que la tabla contiene encabezados (de tenerlos).
3. Configuramos el límite de ejecución para evitar el envío masivo de correos simultáneamente.
4. Añadimos el módulo de ChatGPT y configuramos el asistente creado previamente para generar los mensajes personalizados.
5. Añadimos el módulo de correo electrónico, configurando los campos necesarios (destinatario, asunto, cuerpo del mensaje) usando los datos de la tabla y el mensaje generado por ChatGPT.

### 5. Pruebas y Ajustes

Realizamos pruebas para asegurarnos de que los mensajes se generan y envían correctamente.

#### Consejo:

Configura el envío de correos electrónicos cada 60 minutos para evitar problemas de spam. Ajusta este intervalo según tus necesidades y observaciones.
