# 📤 14. Formateo y envío de mensajes

> Ruta: Agentes de WhatsApp › 📤 14. Formateo y envío de mensajes

**🎬 Vídeo (4.0 min):** https://www.loom.com/share/3d9ba7f021454a5fb15e9bb3c63792af

---

En este módulo cerramos el ciclo completo del agente.  
Aquí convertimos la respuesta generada por la IA en un mensaje limpio y listo para enviarse por WhatsApp mediante Evolution. Ya no procesamos entradas: preparamos la salida final que verá el usuario.

---

## **1. Limpieza de la respuesta de la IA**

Cuando el agente responde, el texto llega a la variable **output**.  
A veces la IA incluye caracteres extraños, saltos de línea innecesarios o símbolos que no se ven bien en WhatsApp.

Para evitarlo, usamos un nodo de formateo que:

- Detecta caracteres no deseados
- Los elimina automáticamente
- Devuelve un mensaje limpio y seguro

Pedirle a la IA "no uses X símbolo" no siempre funciona.  
La solución real es **sanear el mensaje antes de enviarlo**.

---

## **2. Espera controlada (opcional)**

Este paso no siempre es necesario, pero puede ser útil cuando:

- La IA genera respuestas largas
- Queremos evitar choques si llegan nuevos mensajes mientras se procesa
- Es necesario espaciar envíos para evitar bloqueos o parecer spam

Normalmente se dejan unos segundos, pero el nodo es totalmente opcional.

---

## **3. Envío final por WhatsApp**

El último paso es enviar el mensaje al usuario.  
Esto se hace mediante un POST al endpoint de Evolution:

- Se usa la URL del webhook
- Se envía el API key
- Se pasa el número del usuario (remoteJID + sufijo de WhatsApp)
- Se envía el texto limpio generado en el paso anterior

El sistema utiliza automáticamente:

- La instancia correcta
- El webhook inicial del flujo
- La variable **output_limpio** como contenido final

El usuario recibe la respuesta en segundos, como si estuviera conversando con una persona real.

---

## **Qué permite este módulo**

- Convertir la salida de la IA en un mensaje limpio y sin errores
- Enviar respuestas confiables a cualquier número de WhatsApp
- Controlar la cadencia de los mensajes cuando es necesario
- Completar el circuito del agente: mensaje entrante → procesamiento → inteligencia → mensaje saliente

Con esto, tu agente ya piensa, recuerda, decide, ejecuta… y ahora responde correctamente.  
Queda oficialmente listo para producción en WhatsApp utilizando n8n y Evolution.

## 🎙️ Transcripción

Bien, vamos ya finalizando con esto, vamos acá tenemos estos tres puntos Primero, ya tenemos la respuesta de la gente, ya la gente respondió y lo tenemos en ésta variable que ven acá, ésta variable chiquita, el resto es expresión, sí. pero si yo como sé que es esa variable porque si yo agarro esto de roberto consultor conía me pone output es esto y son punto auto repasamos por qué y son porque es el nodio por qué output, por qué es lo que devuelve la idea, nada más. Entonces acá tenemos esto, esto que hace es un formato, es un un formateo que nosotros lo usamos para borrar dos signos que no queremos que estén, que son este. y este. Entonces con esto con lógica muchas veces les habrá pasado ustedes que quieren decirle a la gente. de ella o a un asistente de ella o a que pede no escribas con estos dos signos y lo va a escribir igual no es muy difícil sacar. se lo compromete. Entonces, ayúzamos lógica. ¿Por qué? Porque podemos detectarlo con esta expresión que se lo pueden pasar a GPT. y lo que hace es borrar automáticamente todos estos signos si los encuentran, los de la sacón, un espacio vacío, ¿sí? esto es lo que hace este nodo y ahí ya tenemos que trabajamos con esta variable, ya no trabajamos con esto vamos a esperar acá que esto es realmente por una cuestión de que hay veces que manda mucho mensajes si queremos que espero que tenga que no pero con este siempre hay x cantidad de segundos de que recibe el mensaje, también se puede borrar no hay ningún problema. Pero sirve y acá tenemos la espera respuesta que tenemos esta llamada al webbook que tenemos un RL, que en mi caso es evolución.robo-system.exiceta, tenemos el endpoint que es esto, que es para que manda un mensaje. y luego tenemos la instancia, que es el nombre como tenemos asociado el whatsapp business en de voluja. Esta expresión le va a funcionar ustedes en ningún problema no tienen que cambiar nada porque toma toda la info de acá abajo ¿Cómo sabemos que lo toma de webhook? Porque acá dice webhook, entre paréntesis. Bien, entonces acá tenemos esto. la URL es un post. Tenemos la información, tenemos acá, tienen que poner su apiqui, esto que acá, y acá le, Dejamos dos variables importantes. Aquí les tenemos que contestar y que les tenemos que contestar. Acá lo tenemos que poner como un remote j, Entonces lo vamos a poner con número de teléfono a roba s.batzap.net y esto ya así que lo tiene de uno de los móvulos de acá y luego por otro lado le damos ya esto que lo que vemos es leamos directamente output limpio, que es lo que nos dio el último como módulo que ese. como en acá, si yo lo llamo, obtiene esto, ya yo podría borrar, le doy es, esto acá y va a ser exactamente lo mismo. Y esto que va a ser nos va a contestar. Esto El aparte es la parte por ahí más simple, se pueden agregar más cosas, se puede hacer que mande por ahí varios mensajes en vez de uno solo, se puede hacer que espere más. Lo que sea, se puede complijizar muchísimo, pero para arrancar y para que se entienda esto, señoras y señores. es una gente de ella conectado en whatsapp, levantado en n8n que les va a tomar 10 minutos de Vamos a ir subiendo obvio muchísimo más contenido de esto con funciones, con más trabajo, con más funcionalidades, con, Lo que pidan, hacíamos ya contribuyendo y les vamos dando una mano en lo que es necesario. Un saludo.
