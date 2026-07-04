# ☁️ 3A. Cloud (Evolution API)

> Ruta: Agentes de WhatsApp › ☁️ 3A. Cloud (Evolution API)

**🎬 Vídeo (5.8 min):** https://www.loom.com/share/54bbddf057e94a48914da4a1b794da1e

---

**En este módulo mostramos cómo levantar Evolution API en su versión cloud **(la forma más rápida y directa) para conectar WhatsApp Business con n8n sin usar servidores propios.

Explicamos que existen dos caminos:

1. **Levantar Evolution API en tu propio servidor** (más técnico, pero también posible). Si te interesa esa opción, tienes disponible el otro video donde explicamos el proceso completo.
2. **Usar Evolution API Cloud** (la opción sencilla). Si quieres avanzar rápido y seguir el paso a paso sin complicaciones, este es el video correcto.

En este módulo hacemos lo siguiente:

1. Creamos una cuenta en **Evolution API Cloud** (plan inicial).
2. Configuramos un proyecto y creamos una instancia nueva.
3. Añadimos un cliente y seleccionamos el canal “WhatsApp Web”.
4. Desde el celular abrimos WhatsApp Business, vamos a “dispositivos vinculados” y escaneamos el **código QR** que muestra Evolution.
5. Una vez conectado, vamos a la sección de eventos en Evolution y pegamos el **webhook de n8n** (la Production URL).
6. Activamos la opción correspondiente para que todos los mensajes entrantes se envíen al flujo.

Con esto, tu número de WhatsApp Business queda conectado a Evolution API Cloud y listo para integrarse con n8n y el agente.

Si quieres hacerlo rápido y sin pasos técnicos, usas este método (Cloud).  
Si quieres profundizar más, tienes también el video donde explicamos cómo levantar Evolution API en tu propio servidor.

## 🎙️ Transcripción

Bien, para levantar ahora el Evolution API, que es para poder conectar justamente WhatsApp, vamos a seguir estos pasos. Volviendo un poquito para atrás para repasar, vamos a usar Evolution API para conectar un Whatsapp Business con N8n. ¿Sí? Entonces, para poder hacerlo hay dos opciones, podemos levantar el Evolution API en nuestros servidores, o podemos levantarlo en levantar o podemos usar la versión cloud, que es lo que vamos a mostrar acá, a fines prácticos. Vamos a ver, BlastDisk. Las diferencias más que nada están en que usando el cloud tenemos que pagar 20, 19 dólares al mes y en el servidor un poco más de trabajo porque hay que levantarlo en el servidor, pero que también hay un video de Carlos donde explica bien cómo se hace, pero, Para los que quieran hacerlo lo más rápido posible y seguir el paso a paso desde acá, vamos a hacer todo el proceso creándonos una cuenta y pagando evolución a pie. desde cloud, que es esto. Bien, vamos a ir acá evoapicloud.com, vamos a darle a suscribirse. en el plan inicial, voy a crear una cuenta vamos a llenar todo acá y ahora volvemos, esto, esto, esto no lo tienen que llenar Contraseña, registrar. Yo lo voy a guardar. Entra en Verification Code, nos van a ver, nos va a dar ya un mail, muy bien, ahí yo puse Está todo bien y la contraseña que yo la había guardado Ahí estamos. Bien. Perfecto. Vamos a ir directamente, Entra acá, al plan Starter Lo apagamos con todo esto y aparecemos acá. Tenemos proyectos, límites, usuarios, nos aparece absolutamente todo esto, no necesitamos más que esto realmente, vamos a ir Mira, proyectos, Ahí se ha salido, listo. Vamos a proyectos, creamos nuevo proyecto, vamos a poner Corrigi, Cloud. y entramos acá, una vez que entramos acá vamos a darle a instancias, crear nueva instancia, bueno tenemos que crear un cliente, voy a ponerme yo, Franco Ricci acá le ponemos whatsapp web bailis importante esto evolución y InstancesLimit 1 dejamos todo esto así como está, no hay problema Y ahí estamos. Acá vamos a agregar el customer, le ponemos nombre, banco rich y lo que sea, canal, esto es importante, pongan whatsapp web, veinte minutos. y luego acá si quieren poner el número de teléfono yo lo voy a poner, así queda Bien, guardar. A ver, Bien, tenemos esto, ahora vamos a darle acá, abrimos tenemos todo esto acá podemos darle a ver GetQuery y ahora lo que voy a hacer es conectarlo directamente a con mi celular. Voy a ir a Whatsapp Business y voy a ir a Settings, a la configuración. voy a buscar donde diga dispositivos vinculados, vincular un nuevo dispositivo, y ahora Ahora voy a poner el QR de nuevo y lo escaneo. Ahí me está. login in, que se ve bien tenemos que mantener esto abierto, vamos a poner evolution y ahí ya estaría sincronizándose vamos mientras a recargar, bueno ahí ya está conectado, eso es todo después una vez que tenemos esta instancia seguimos el resto de los pasos. ¿Qué van a hacer? Ir acá a la parte de eventos, vamos a webhook. y acá le vamos a poner directamente el webhook que teníamos ya copiado de n8n. que para que quede también super claro, vamos a ir acá esto puede ser Puede ser que quede repetido en más de un módulo, pero es importantísimo que quede bien. Vamos acá, buscamos Production URL, copiamos. Cambiamos, volvemos acá de nuevo y le pegamos ese webhook. le vamos a dar a habilitar, buscamos acá abajo messages absurd Le damos acá, le damos a OK y ahí ya estaría conectado todo sin ningún problema.
