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
