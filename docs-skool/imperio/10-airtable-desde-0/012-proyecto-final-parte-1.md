# 🏆 Proyecto Final – Parte 1

> Ruta: Airtable Desde 0 › 🏆 Proyecto Final – Parte 1

**🎬 Vídeo (10.3 min):** https://www.loom.com/share/e4277d5104f847d0940a069fcf0c1799?sid=c1f8bbe5-4738-4ec2-bbd0-9f1a0d5d6822

---

Imperiales! Entramos en la recta final del curso con el **Proyecto Final**, donde todo lo aprendido cobra vida en una integración real con **Airtable + Make** 💥

🧠 **¿Qué vamos a construir?**  
Un sistema que te permite **publicar contenido en redes sociales directamente desde Airtable** con un solo clic. Literalmente, apretás un botón y se publica en Instagram o LinkedIn (sí, en serio).

---

🚀 **¿Qué hicimos en esta primera parte?**

✅ Creamos un **botón "Publicar"** en la tabla de posteos de Airtable.  
✅ Ese botón dispara un **webhook en Make** usando una fórmula.  
✅ Le enviamos el `RECORD_ID()` del posteo como parámetro.  
✅ Confirmamos que Make recibe correctamente ese dato para seguir con el flujo.

🔗 Esto marca el inicio del sistema automatizado. Cada vez que toques “Publicar”, Make sabrá qué contenido debe procesar.

---

🧩 **¿Por qué importa esto?**  
Porque con este paso le das “vida” a tu gestor de contenido. Dejás de usar Airtable solo como base de datos para transformarlo en un **centro de operaciones automatizadas**. Nada se publica sin control, y todo queda trazado.

---

👀 **En la próxima fase...**  
Vamos a usar ese `recordId` para **consultar toda la información del posteo** (imagen, copy, plataforma) y preparar la **publicación real en Instagram o LinkedIn**, dependiendo de lo que elijas en Airtable.

Esto recién empieza. 🔥  
Nos vemos en la Parte 2 del Proyecto Final.

## 🎙️ Transcripción

Entramos en la recta final, arrancamos el primer módulo del proyecto final. Así que, bueno, este, vamos de lleno con, con acá, con lo que, con lo que hay que hacer. Este, en principio, lo que yo les mencioné en el video de introducción, vectorio es que vamos a hacer una conexión, o sea tenemos que encontrar la forma de conectar la información que tiene un registro con make, ok? y para eso vamos a usar nuestro amigo del botón. Esta es una propiedad que nos va a, bueno, nos va a permitir, por supuesto, crear un botón que nos va, o sea, va a ser el trigger para empezar a armar la automatización, ok, y la integración. con este botón le vamos a dar a publicar a un récord en específico, a un registro específico y con esa información registro vamos a publicar en redes sociales, ok? Entonces lo primero que vamos a ver en este vídeo es, bueno, ¿cuál como armar la conexión, ok? Eso es lo único que vamos a hacer acá. Entonces, vamos a agregar acá una propiedad, le vamos a poner publicar, en la etiqueta del botón le voy a poner publicar, y le vamos a poner Rosita, ok? Los botones tienen acciones y acá están todas las acciones que se pueden hacer. Yo voy a poner acá la de OpenURL porque vamos a abrir una web. Bueno, acá no me deja guardarlo, por supuesto, porque no le puse nada en la fórmula. Lo voy a guardar acá, así, vacío. Bueno, acá lo que tienen que saber, Lo primero que vamos es agregar un webhook en un escenario de Make. Lo voy a copiar aquí. Lo que voy a hacer es que este botón abra la url. Esta acción tiene acá para rellenar un formato de fórmula. Entonces nosotros vamos a tener que poner la url entre comillas porque es un texto. Y pueden ser otra cosa. Entonces, lo que yo quiero que ustedes vean es que cuando nosotros, Si nosotros abrimos en una pestaña nueva, por ejemplo, uno de estos links de los webhooks, estamos enviando efectivamente un webhook. Entonces, ese es el truquito que vamos a aprovechar acá en este botón. Si ustedes ven que acá yo me posteo uno, Yo ya configuré el botón, pero si le damos a publicar, van a ver que se abre acá. Ah, perdón, no lo puse acá a escuchar al ojo, pero me voy a poner por acá. Voy a guardar acá. Vamos a darle a save. ¿******* botones? Ahí está. Vamos a ver que si yo le doy acá a publicar, acá me dice que lo aceptó y acá ya. ¿Qué pasa? Que no nos llega nada. No nos llega absolutamente nada. ¿Para qué me sirve esto? Yo lo que necesito es que el botón me devuelva información de la del registro que yo le estoy apretando, porque como ven, cada uno de estos botones corresponde a un registro. Bueno, vamos a seguir jugando con el link, ok? Les voy a explicar brevemente cómo funcionan los links. Los links pueden llegar a tener parámetros y esos parámetros son los que vamos a utilizar nosotros para decirle, por ejemplo en este caso, le vamos a enviar al webhook el record ID del botón que estamos apretando, ¿ok? ¿Cómo hacemos eso? Bueno, los links, voy a hacer un ejemplo acá, voy a agregar acá, este sería el webhook que nosotros tenemos. Si nosotros quisiéramos enviar un parámetro a través de la URL, lo único que tenemos que hacer es agregar un signo de pregunta que nos va a permitir agregar parámetros Vamos a poner por ejemplo recordId, este va a ser el nombre de la variable que vamos a enviar, ponemos igual y le introducimos un valor, por ejemplo, ejemplo1. Sí. Vamos acá y lo ponemos a escuchar de vuelta y yo le doy a Enter para ver acá que va a llegar la data bien. Es más, voy a ejecutar acá de vuelta y acá voy a recargar para que vean que ahora no llegó vacío, sino que ahora llegó con, de base tenemos un parámetro y además tenemos un valor para el parámetro y bueno acá como como ven esta es la construcción del parámetro nuevo que estamos enviando. Y esto es lo que vamos a hacer acá. ¿Se acuerdan que yo les dije al principio que pongan entre comillas el link porque esto es un campo de fórmula? Bueno, esto es lo, Esto es increíble. Esto es increíble, ¿por qué? Bueno, porque acá, Le damos, perdón por el corte, como les decía, acá en el link podemos agregar un parámetro y le vamos a poner, por ejemplo, record ID, como les comenté, la estructura. Lo que pasa es que la variable que va a tomar RecordID siempre va va a variar. Y acá es donde entra a jugar nuestra amiga la fórmula ¿no? Que nos da la posibilidad de que sea dinámico ese espacio. Así que, Acá, como les dije, vamos a cerrar lo que es texto y vamos a concatenar con este carácter. El RecordID, la variable de RecordID, ¿se entiende lo que estamos haciendo? Estamos. Voy a dividirlo acá para que sea un poco más visual. Vamos a agarrar. y vamos a hacer que tocamos el botón del registro, ok? Quiero aclarar que cada uno de estos botones corresponde a un registro, bien? La información que vamos que va a fluir, va a tener que ver con el registro que estamos tocando, muy importante. Vamos a hacer que se abra un link, ¿bien? Ese link está compuesto por la URL del webhook, que pusimos en make, ok, importante, y además le estamos agregando un parámetro que le vamos a llamar recordId y que le vamos a dar el valor de, y esto lo dejamos dinámico, porque acá lo que se va a construir es que le vamos a concatenar evidentemente el record ID. El record ID, como saben, como les expliqué en los módulos anteriores, se puede utilizar como variable cuando estamos armando formas. De esta forma nos va a quedar exactamente este todo este link, pero solamente hasta acá y esto va a ser dinámico, le vamos a mandar un record ID. Vamos a hacer la prueba final, vamos a venir acá, vamos a determinar StructureData y vamos a hacer la prueba final. la prueba de oro primero vamos a tocar acá este botón de publicar vamos a ver que se nos abre acá y acá nos va a decir que está aceptado ok pero vamos a correr este este este tiempo escenario. Ahora que está escuchando vamos a tocar de vuelta este botón y ahora, como ven, acá en la url tenemos el record ID y que es lo que recibimos acá exactamente el mismo record ID ok con esto vamos a darle vamos a guardar el escenario lo vamos a guardar como proyecto final la próxima.
