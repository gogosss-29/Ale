# 🧩 1. Qué vamos a necesitar?

> Ruta: Agentes de WhatsApp › 🧩 1. Qué vamos a necesitar?

**🎬 Vídeo (3.3 min):** https://www.loom.com/share/4c4c3a0d91da48c4b9d95e5a3039c4ad

---

> NOTA: Si NO has instalado n8n, puedes hacerlo siguiendo el tutorial de [aquí](https://www.skool.com/imperio-digital/classroom/8e2ffdbc?md=2606db521b014a3e8034d5a992dbb6b3)[.](https://www.skool.com/imperio-digital/classroom/d32f4fc7?md=6a3fb77e9ac943418699065623a6ba15)

En este módulo revisamos las tres piezas que necesitas para que tu agente de IA funcione en WhatsApp. Todo es simple y modular. Lo único que usamos es:

1. **n8n (el cerebro)**  
Aquí se procesa todo: los mensajes, la lógica y la llamada a la IA. Puedes usarlo en tu propio servidor o en su versión cloud (ambas funcionan igual).
2. **Airtable (la memoria)**  
Es donde vamos a guardar una base de datos muy simple con la información de cada usuario y sus mensajes. Con el plan gratuito basta.
3. **Evolution (el puente hacia WhatsApp)**  
Es lo que conecta tu número de WhatsApp Business con n8n. Puedes instalarlo en tu servidor o usarlo en la versión cloud.

También explicamos, de forma rápida, cómo funciona la plantilla completa:  
Los mensajes que llegan por WhatsApp entran por un webhook, se agrupan unos segundos (para juntar mensajes seguidos), se procesan con un agente de IA (en este caso un consultor llamado Roberto) y luego se envía la respuesta de manera natural al usuario.

La idea de este módulo es que entiendas el paso a paso general antes de enchufar todo a tu propio número. En el siguiente video vemos exactamente cómo hacerlo.

## 🎙️ Transcripción

Bueno, vamos a, vamos a meternos de lleno directamente en qué vamos a necesitar para poder tener esto y para poder enchufarlo y hacerlo funcionar. Vamos a necesitar, inicialmente, tres puntos, tres cosas. Primero N8n, que es esta aplicación que vemos acá, la pueden instalar en su servidor, si hay contenido en la comunidad para que puedan ver cómo instalarlo y también se puede usar la versión cloud que es exacta. Exactamente lo mismo, bien. Esto primero. Después, por otro lado, vamos a necesitar una cuenta de Airtable, donde vamos a poner, una base de datos súper simple por lo pronto, ¿sí? Esto también, necesitamos el plan gratuito y una base de datos que tenga esta estructura. Después, ok, la vamos a investigar, lógicamente. Por otro lado, vamos a necesitar Evolution, que es lo mismo, se puede encontrar, ponen en su servidor o lo pueden usar en la versión de la nube, en la versión cloud. Esto está todo lo que viene ahora está preparado para, evolución si está levantado en su servidor que también es súper simple y hay contenido para que se pueda hacer. Dicho esto, vamos a meternos bien de lleno sobre, primero, una breve explicación sobre qué es lo que hace este agente en particular, qué es lo que nos importa es entender la plantilla y el paso a paso que va a suceder. y después de esto ya les vamos a dar las instrucciones para que puedan hacerlo para que puedan enchufar esto que ya está armado en un número de ustedes, en un sistema suyo y después vamos a ir paso a paso, parte por parte, sobre cómo funciona cada sección. de la gente de IA que como ven tiene varias partes. Vamos a ver acá que directamente, necesitamos un webhook, bien, todos los mensajes de whatsapp llegan por un webhook, acá vamos a guardar un poco la información para luego buscarla y lo primero que hacemos es determinar un ID para referirnos a la persona. número de teléfono, lo que sea. Luego acá tenemos que la persona puede enviar audio, puede enviar textos, puede enviar imágenes. y el agente de ella lo va a recibir de la misma forma. Por otro lado, tenemos que el agente de de IA va a esperar unos segundos, así que acá tenemos seteado en 10 segundos, se puede setear en 30 por ejemplo. Pero esta es la cantidad de segundos que va a esperar el agente de IA para poder recolectar todos los los mensajes y luego procesarlos y luego tenemos efectivamente el agente de guía que en este caso es Roberto, un consultor en inglés. inteligencia artificial que es capaz de dar soluciones y de diagnosticar diferentes problemas que hay en un negocio para poder resolverlos. implementando inteligencia artificial y por último vamos a tener el envío de los mensajes que tenemos un breve detalle acá y luego tenemos que se envían los mensajes de manera natural, vamos a en el próximo vídeo. módulo que ahora voy a poner a grabar vamos a ver qué es lo que tenemos que hacer para enchufar directamente esto en su número en un par de de minutos.
