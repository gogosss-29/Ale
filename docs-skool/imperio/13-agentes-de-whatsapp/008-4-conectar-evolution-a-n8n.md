# 🔌 4. Conectar Evolution a N8N

> Ruta: Agentes de WhatsApp › 🔌 4. Conectar Evolution a N8N

**🎬 Vídeo (3.7 min):** https://www.loom.com/share/6bb46c79908c40a2bb11765b58b8d9a5

**📎 Recursos:**
- Agente Whatsapp n8n Imperio

---

En este módulo conectamos tu número de WhatsApp Business con n8n usando Evolution. Esta es la parte que permite que cada mensaje que recibas en WhatsApp llegue directamente al agente.

El proceso es simple:

1. Creamos una **nueva instancia en Evolution** (es donde se vincula tu número).
2. Abrimos WhatsApp Business en el celular y escaneamos el **código QR** que aparece en Evolution (esto conecta tu número a la plataforma).
3. Vamos a n8n, creamos un workflow nuevo y **importamos el archivo** que te damos en el curso.
4. Dentro del flujo, copiamos la URL del **webhook** y la pegamos en la sección de eventos de Evolution.
5. Activamos la opción para que todos los mensajes entrantes se envíen a ese webhook.

Con estos pasos, tu WhatsApp queda conectado a n8n y listo para que el agente reciba y procese mensajes de inmediato. Una vez configurado esto, pasamos al siguiente paso para enlazar Airtable.

## 🎙️ Transcripción

Bien, ya tenemos, eh, la parte de Arteigo la armada, nos queda configurar la parte de Evolution. Vamos a verlo. Tienen que tenerlo ya ustedes en su servidor y una vez que lo tengan en su servidor lo que vamos a hacer es crear un nuevo. una nueva instancia de Evolution. ¿Esto para qué es? Es para conectar su número de teléfono. Vamos a poner acá. una distancia, si quieren podemos poner imperio digital, lo dejan así como está, si quieren poner el número de teléfono lo ponen. si no, no hay problema, le dan a guardar, buscan la instancia, acá, y ahí ya tenemos directamente les aparece en instancia para conectar con el QR. Acá qué es lo que tienen que hacer ustedes. Tienen que agarrar el celular con, con la cuenta de Whatsapp Business y van a la sección de Whatsapp Business de vincular un nuevo dispositivo. Cuando van a vincular un nuevo dispositivo les va a aparecer para conectarlo con un QR y ahí es donde van a agarrar el celular con la cámara y escanear este QR que les aparece. Con ese QR ahí lo que hacemos es conectarlo, conectar el número de Whatsapp Business a Evolution y les va a aparecer algo así. Les va a aparecer su nombre, les va a aparecer el número de teléfono, la cantidad de contactos, chats, mensajes, es todo y ahora una vez que tenemos esto vamos a volver a n8n y vamos y ya empezar a conectar todo. Acá en N8n ustedes ya van a tener esto, lo van a tener para importarlo. directamente, lo que van a hacer acá con esto es lo siguiente, vamos a arrancar de cero, ustedes van a tener un archivo, van a la parte de de crear workflow, vamos a venir acá, vamos a crear workflow, arriba a la derecha y cuando van a crear workflow lo que hacen es importar desde archivo y archivo, seleccionan. buscamos acá, es este, abrir y ahí está y ya tienen esto armado, una vez que tengamos esto armado, lo que vamos a tener es un una configuración de webhook acá y lo que vamos a buscar es este valor, lo vamos a editar si les aparece exactamente igual a esto lo van a editar un segundo y si no queda igual copian este valor de parámetros. production url, éste, lo copian y vamos a llevarlo a Evolution a la parte de eventos, esperen que apareció de nuevo, a la parte de eventos, vamos a webhook pegamos esto acá vamos a poner habilitar, esto les va a aparecer de esta forma Ahí van abajo y van a la parte donde dice messages absurd, le dan a que quede de esta forma, guardar. y ahí ya estaría conectado este número a en el
