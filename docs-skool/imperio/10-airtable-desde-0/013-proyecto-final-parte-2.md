# 🏆 Proyecto Final – Parte 2

> Ruta: Airtable Desde 0 › 🏆 Proyecto Final – Parte 2

**🎬 Vídeo (8.9 min):** https://www.loom.com/share/bcb878c368784d76bbfc622a010e68b6?sid=3f1dfff9-4634-4a5d-8715-35dc28be9b7a

---

Imperiales, seguimos avanzando en este **sistema de publicación automatizada**, y en esta segunda fase hicimos que Make no solo reciba el webhook, sino que **entienda qué tiene que hacer con él** 🧠⚙️

---

🚀 **¿Qué logramos en esta fase?**

✅ Usamos el `recordId` recibido para **buscar el posteo exacto en Airtable**.  
✅ Recuperamos toda su info: título, plataforma, imagen, copy, etc.  
✅ Armamos un **Router** en Make que separa el flujo según la red social:  
 📸 Si es **Instagram**, se publica la imagen con el título.  
 💼 Si es **LinkedIn**, descargamos la imagen con HTTP y publicamos con el copy.

Todo esto completamente **automático**. Solo tocás “Publicar” en Airtable y Make se encarga del resto.

---

🧩 **¿Qué aprendiste acá?**  
Que **no basta con integrar**, hay que **entender cómo estructurar la data** para que tu sistema funcione con lógica y precisión. Las relaciones entre tablas, los valores que se traen... todo cuenta. Y lo hiciste.

---

🔜 **¿Qué sigue?**  
En la Parte 3 vamos a **afinar el flujo de publicación en LinkedIn**, cerrar condiciones y asegurar que **solo se publique cuando todo esté aprobado**.

Nos vemos en la siguiente fase 💪✨

## 🎙️ Transcripción

Asi imperiales, como a, todavía, bueno, vamos acá en la segunda parte del proyecto final. Este, vamos a seguir con esto. Vamos a construir el escenario, eh, ok, para, para terminar de tomar el flujo de que es lo que va a pasar. Recordemos que, eh, ya en el video anterior, eh, hicimos ver, perdón, vimos. How to make this record to make. Okay, so the next thing we're going to do is, well, what we want, right? What we want to do, um, according to the record ID, the one I read, the one where we publish, we publish, of course, with the information of that record. So, first we have to have the information, Del Recordo, ok. Necesitamos tener variables que nos permiten acceder a la información que se recorda ahí. Así que vamos a agregar un modo de arte igual, hmm, la pregunta está acá ¿No? ¿Cuál de estos dos uso? Bueno, el de arriba se usa cuando, está buscando un récord en específico, hmm, pero a partir de un filtro. Por ejemplo, Estás buscando un record dentro de la tabla de posteos que el nombre sea, pues yo, publicación uno, ok? Y el segundo es directamente buscar un record a través de su ID, que es lo que tenemos nosotros y es el método más directo, o sea si ustedes tienen el record ID, usen el segundo, ok? Eh, nos robamos el segundo, así que vamos acá a poner la base, Vamos a poner acá que la, la, la, la tabela de esposteos y el recorredidizlo, tenemos de información de tierra el huevo, ok? Eh, es por acá un poquito, voy a guardar, voy a guardar acá, pues, vamos a hacer una prueba de el poste 1, ok? Voy acá a publicar, se corre el huevo, juc, y acá tenemos la respuesta, I got the record ID, ok, this one is here, good. And here we see that we already have all the information of the record, good, to use in variables, what we are to need to publish. So, well, we are going to publish it on Instagram and LinkedIn, so we are going to add a router, we are going to add here on Instagram mode. Eh, voy a usar una cuenta que tengo que ya, por supuesto, cree, ahí se la conexión, todo. Ok. Tenemos foto URL. Bueno, de base, vamos a tener que crear acá unos, unos, unos, unos campos. Ven acá aquí, en plataforma, tenemos, si desglosamos, tenemos un, un récord adiví también, ¿no? ¿Qué es lo que pasa? Que cuando Creamos la tabla. Yo les mencioné que acá hicimos la conexión con la, con la otra tabla de plataforma. No, acá. ¿Qué pasa con esto? Que acá visualmente estamos viendo que poste uno está conectado con Instagram, pero realmente esto es una conexión entre Uh, idea de registros entre Records ID. Entonces, acá a los que nos permite arrastrar hoy siempre es añadir campos de búsqueda. Y vamos a agregar este plataforma. Y vamos a ver que dice lo mismo. Se va a decir Instagram también en el primer campo. Bueno, ahora cuando cuando carguen, ¿no? Si estamos, ahí está dando un poquito. Ahí está. ¿Cuál es la diferencia acá? In terms of values, reals, this contains the record ID and this contains the text and Instagram, because we are bringing the name and the platform, that is, we are bringing this column here. Okay, this column here is this we just created and this is simply a connection between records and distribution, it is very important to have a account. Um, vamos a, vamos a confirmar esto. Y además, antes de reunir de vuelta en escenario, vamos a agregar urgente un campo de archivos de juntos. Le voy a ponerme a ella, eh, que no, no, parecido no tenemos. Y le voy a subir acá un marchivo. Está, vamos a subir este archivo. El poste o uno, ok, eh, le subir a fotito de congertelations. Bien, eh, esta la que vamos a usar para testiar. No, así que, eh, con esto le voy a dar el botón de, voy a reunir acá esto y le voy a dar el botón de publicar esto para que Uh, uh, we can see the variables in action very well, okay? Uh, I came here that, um, the output is red to the platform, right? And it returns what was before. And, um, here, it returns. Effectively, the name of the platform, Instagram. So that we already have it differentiated, and here we have the middle field. Okay, as we understand all the information, okay? So I'm going to connect this back and we're going to put back the, um, we're going to add a filter here so that the platform, there it is, uh, contains case insensitive, we're going to Instagram. Bien, eh, si es Instagram, esto es por supuesto, ¿no? Para determinar los caminos, eh, vamos a ir acá, vamos a romismo, eh, un plataforma, no, no estoy pudiendo aquí, ¿quién hago? Equal tú, vamos a poner, Contains case insensitive, you can suponar link ed, eh si es link ed, eh. Bien, acá separamos los caminos, vamos a probar primero con el Instagram, vamos a configurar el módulo, vamos a suponar la URL acá de la media URL, bien, y en Caption le voy a poner acá el título del posteo, ok? este, me voy a traer acá. Ahí estamos, vea la save. Vamos a guardar el escenario. Y ya tenemos configurado el módulo para publicar. Tenemos la ruta. Así que vamos a hacer el testeo, ¿no? Lo voy a correr. Ya tengo guardado. Y vamos a sacar el posteo 1. Que tenemos, que la red social a la cual se va a publicar es Instagram y, eh, tenemos la, la fotito acá, ok, de prueba. Acabrí un, un, un, un, acá estoy haciendo pruebas antes. Tengo una caudada en ejemplo, a el cual se va a subir esto. Así que le vamos a dar a publicar. No sé por qué no me veo yo, pero bueno, le vamos a dar a publicar. lo corrimos, acá vamos a ver cómo se está postiando esto, ahí estamos, se postió y acá vamos a ver si pasó?
