# 🧩 8. Formateo de mensajes (text, audio, image)

> Ruta: Agentes de WhatsApp › 🧩 8. Formateo de mensajes (text, audio, image)

**🎬 Vídeo (4.4 min):** https://www.loom.com/share/3adafa2d2b7e4981a249de10e0e05829

---

En este módulo tomamos cualquier mensaje que envíe el usuario —texto, audio o imagen— y lo convertimos en información limpia y lista para que la IA la procese. Esta etapa es clave: evita errores y asegura que el agente entienda exactamente lo que recibió.

Primero identificamos al usuario y verificamos si corresponde responderle. Luego, según el tipo de mensaje que llega desde Evolution, el flujo sigue una de tres rutas:

**1. Texto**  
El caso más simple. Tomamos el mensaje y lo pasamos directo como *input*, sin transformaciones adicionales.

**2. Audio**  
Aquí el proceso es automático: se descarga el archivo, se convierte, se envía a GPT para transcripción y se guarda el texto final como *input*. Todo ocurre en segundos.

**3. Imagen**  
Descargamos la foto, la analizamos con GPT mediante un prompt diseñado para obtener descripciones útiles y, si el usuario escribió un caption, también se integra al *input*.

---

## **Un solo destino: input**

Aunque existan rutas distintas, todas terminan en la misma variable. Esto:

- evita condicionales repetidas,
- mantiene el sistema más simple,
- y permite que cualquier módulo downstream use siempre `$.json.input` sin preocuparse por el origen del mensaje.

Gracias a esto, el agente puede responder igual de bien a un texto, una nota de voz o una imagen.

---

## **Qué aporta este módulo**

- Aceptas cualquier tipo de mensaje sin romper el flujo.
- Conviertes audio e imágenes en texto útil.
- Mantienes una estructura estándar y fácil de escalar.
- Entregas datos limpios a la siguiente etapa, donde la IA interpreta y responde.

En resumen: este módulo prepara todo para que tu agente entienda al usuario sin importar el formato y mantenga una conversación fluida desde el primer mensaje.

## 🎙️ Transcripción

Siguiendo con esto, una vez que ya determinamos, que con esto determinamos quién es la persona y si le tenemos que contestar, vamos a empezar a hacer, a procesar el mensaje directamente. Primero tenemos esto. Esto, lo que hace, es determinar, según tres filtros, tres rutas, qué tipo de mensaje nos llegó. Evolution, cuando resulta. un mensaje en texto nos manda conversation entonces este es el campo que usamos que es es el message type que lo tenemos acá, está por acá, luego se va a ver a la brevedad. Te quiero encontrar, a ver, Message to, que es esto que vemos acá, entonces esto como lo hacemos, o sea, como lo llamo Vamos, básicamente agarramos directamente esto, lo ponemos, ya lo reciben ustedes armado pero así es como se mueven las cosas en n8n tenemos esto acá y nos evalúa, nos dice una una de estas tres. Puede ser conversación, puede ser audio o puede ser imagen. Entonces, según cada una de estas Según lo que dé verdadero, así que esto es un poquito lógico de que nos pone, nosotros le ponemos unas reglas para que nos diga si si es uno o el otro y a partir de acá ya vamos para una ruta u otra ruta. Si es texto no tenemos que hacer nada, le ponemos input el mensaje y se terminó, ahora Si nosotros, si tenemos audio tenemos que correr acá, esto que lo que hace es obtener la, obtener el el audio, el archivo de audio que recibimos, luego esto se convierte a la Esto es formateo directamente, se convierte en un archivo, se lo mandamos a gpt para que lo transcriba, y luego lo que nos transcribe lo publicamos. convertimos acá, entonces se convierte a texto y listo y lo mismo sucede con la imagen, es un proceso similar. muy similar que no tienen que hacer nada ustedes sino que esto ya está armado pero esto no creo que lo toquen sinceramente pero Esto lo recibimos de esta forma, se convierte igual, en vez de transcribir el audio se analiza la imagen con todo este prompt. Y a partir de acá tenemos esto, acá tenemos el usuario de Junto una imagen y el contenido. contenido de la imagen y otra cosa ¿qué es esto? esto específicamente es ¿cuándo mandamos una imagen en whatsapp y le escribimos un mensaje abajo? Queremos que aparezca, queremos que le llegue ese mensaje a la IA, entonces nosotros ponemos esta variable, que esta variable lo que hace es, si existe lo que hace es analizar si existe el caption, que es como se le dice a este subtítulo de la imagen, se lo va pone y si no lo deja vacío. Bien, ahora qué sucede acá y esto va a servir para la gente que que esté queriendo entender n8n. Nosotros tenemos acá le ponemos input acá le ponemos input y acá acá le ponemos input de nombre a la variable. ¿Por qué? porque nosotros lo que necesitamos hacer es en este punto tener, poder buscar tranquilamente a cualquiera de estos tres. Entonces acá, no importa cual sea. de los tres vaya a andar, nosotros como tenemos exactamente el mismo nombre de la variable del mensaje que es input lo podemos llamar con esto. Esto que ven acá de json, signo pesos, json lo que hace es que referirse al nodo inmediato anterior si quieren profundizar un poco sobre esto está todo lo de N8n desde cero en la comunidad donde pueden profundizar y por ahí les pueda servir bastante para entender qué es lo que está pasando acá. Y esto lo que hace es llamar a él, al mensaje que venga, tanto sea que venga. en el de acá, de acá o de acá. Todo esto para poder nada más que recibir el mensaje, formatearlo y tener bien el mensaje que vamos a procesar, así que ahora vamos a ir con la segunda parte. Perdón, con la tercera parte.
