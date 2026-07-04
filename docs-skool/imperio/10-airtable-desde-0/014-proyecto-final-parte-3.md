# 🏆 Proyecto Final – Parte 3

> Ruta: Airtable Desde 0 › 🏆 Proyecto Final – Parte 3

**🎬 Vídeo (3.8 min):** https://www.loom.com/share/4feb8e8d7e994ac3bf1f1b4c7c7c2644?sid=2762adcd-e47f-44a8-b1b4-df53eed6eb9a

---

Imperiales, avanzamos firme con nuestro sistema automatizado de publicaciones.  
En esta tercera parte dejamos completamente funcional el **flujo para publicar en LinkedIn** 💼⚙️

---

📌 **¿Qué hicimos en esta fase?**

✅ **Descargamos la imagen** que viene de Airtable con un módulo HTTP.  
✅ Configuramos el módulo de **“Create an Organization Post”** de LinkedIn.  
✅ Mapeamos automáticamente el título del post, el copy y la imagen.  
✅ Hicimos una **prueba real**: tocamos “Publicar” en Airtable y el post se subió a LinkedIn sin tocar más nada. ¡Épico!

---

🛡️ **Y además...**  
Agregamos una condición clave: **solo se publica si el posteo está en estado “Aprobado”**.  
Esto previene errores y mantiene tu proceso profesional y controlado.

---

🔜 **¿Qué se viene en la Parte 4?**  
Vamos a **refinar el formulario para nuevos posteos**, dejarlo listo para que cualquier miembro del equipo pueda **crear una nueva idea y cargar todo lo necesario** (imagen, copy, estado inicial, etc.).

Tu sistema ya publica en múltiples redes… ahora vas a facilitar la entrada de contenido.  
Seguimos 💪✨

## 🎙️ Transcripción

Vamos por el módulo 3 de este proyecto final. Perdón por el corte brusco en el anterior video. Este, ahora vamos a ver, eh, la parte de Linkedin, ¿ok? Yo les dije que íbamos a poner dos ejemplos, Linkedin y Instagram. Así que vamos a configurar esta ruta, si es Linkedin primero tenemos que ver. Así que para Linkedin, primero vamos a tener que descargar. descargar la imagen, ok, así que vamos a agregar un módulo HTTP donde vamos a descargar una file y lo único que necesitamos poner acá es el url, epa, esta url no, es la de media, ahí estamos. esta url de media. Ahí descargamos y vamos acá, ahora sí, a postear. Create an organization and post. Bien. Perdón por mi pronunciation. Acá yo estoy seleccionando esto como muy de memoria, pero lo explico por las dudas. Bueno, acá yo puse la única pronunciation que tengo. ejemplo que es ésta y acá mapee ya por defecto 1 cuando agrega este módulo ya si ya pusiste el http antes siempre te va a aparecer esto ya mapeado ok la file que vamos a vas a subir es esta, la que quedas a obtener. Como título vamos a poner el título del posteo. Como contenido vamos a poner copy. Ok. Visibility, todo esto lo vamos a Vamos a dejar como está y voy a guardar el escenario, perdón, voy a guardar el escenario no, voy a guardar el módulo. Ahí estamos y ahora sí voy a guardar el escenario. Vamos a alinear todo esto y cositas a tener en cuenta antes de ejecutar. No tenemos copy. por lo que tengo entendido, no le puse copy, pero acá le voy a poner copy De ejemplo, para el posteo 1. Ahí estamos. Bueno, con el copy, la media, todo. y la página acá, vamos a a tener la prueba a fuego, ok? así que le vamos a dar al botón de publicar y vamos a ver qué pasa con esto. Voy a salir de acá, ah no, guardé. Bueno, vamos a, Ya que estamos acá con el posteo 1, vamos a cambiar acá de plataforma, porque si no, no nos va a andar en el escenario. Y vamos a poner acá LinkedIn, ok. Así que, vamos a, ahora sí, pues vamos publicar. Y vamos a ver qué pasa. No me dejó ni cambiar de pestaña. Ahora vamos a ir acá y vamos a ver si se publicó. Ahí estamos, efectivamente se posteó, copy de ejemplo para el posteo 1, ok, así que bueno, nada, salió todo bien. y ya tenemos acá integrados ambos caminos. Ya la parte de make estaría cubierta por ahora para postear. Así que bueno ahora vamos a seguir con tema de formularios e interfaz. Nos vemos para adelante.
