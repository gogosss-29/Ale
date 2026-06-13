# 🖥️ 3B. (Servidor) EvolutionAPI

> Ruta: Agentes de WhatsApp › 🖥️ 3B. (Servidor) EvolutionAPI

**🎬 Vídeo (3.5 min):** https://www.loom.com/share/e145a6efab3d40a997eed0405415fd00

---

En este módulo mostramos cómo instalar Evolution API directamente en tu propio VPS. Esta opción es un poco más técnica, pero perfecta si quieres tener todo bajo control o si ya trabajas con servidores.

Los pasos que explicamos aplican tanto para EasyPanel como para cualquier VPS basado en Docker (el proceso es prácticamente el mismo).

En este módulo hacemos lo siguiente:

1. Abrimos **EasyPanel** y buscamos la plantilla de Evolution API.
2. Revisamos la página de *releases* para elegir la [versión más reciente](https://github.com/EvolutionAPI/evolution-api) (en el ejemplo usamos la **2.3.6**, que incluye mejoras y correcciones relacionadas con WhatsApp y el protocolo **Baileys**, que es el que Evolution API utiliza para conectarse a WhatsApp Web).
3. Ajustamos la versión en EasyPanel y creamos el contenedor.
4. Esperamos a que el servicio se inicie y revisamos la URL o dominio generado por el VPS.
5. Accedemos al panel de Evolution añadiendo “/manager” al final de la URL.
6. En EasyPanel, buscamos en las variables de entorno el campo **authentication_ip**, copiamos ese valor y lo pegamos en la pantalla de login de Evolution para acceder.
7. Dentro del panel, creamos una nueva instancia y elegimos el protocolo correspondiente (generalmente **Baileys** para WhatsApp Web).
8. Nombramos la instancia sin espacios y confirmamos la versión configurada.

Con estos pasos, Evolution API queda instalado en tu servidor con una instancia lista para conectar tu número de WhatsApp.

Esta opción es ideal si prefieres evitar el plan mensual de Evolution Cloud, si ya tienes un VPS o si necesitas una instalación más personalizable.

Y si quieres más detalles técnicos sobre la instalación, Carlos grabó un[ módulo específico explicando todo el proceso paso a paso](https://www.skool.com/imperio-digital/instalacion-de-evolutionapi-paso-a-paso-seguimiento-del-video-de-n8n-vps?p=0ea7142d). Puedes ir a ese video si deseas profundizar aún más.

## 🎙️ Transcripción

Listo, ahora vamos a instalar la revolución API en nuestro VPS. En ese caso lo vamos a hacer en IZ-PANEL. Si ustedes tienen algún otro VPS, los procesos son prácticamente los mismos, si es un panel, ehm, si es un servicio basado en Docker. template y vamos a buscar evolución app, la seleccionamos y que nos va a pedir que versión, a mí siempre me gusta irme evolución appy y el de gif hoop en evolución appy de este lado donde hicieron releases y vamos a ver cuál es la última versión, en este caso nos vemos que el dado. 1.3.6, que salió el 21 de octubre, vemos que hay unas implementaciones para avelis, chatwood y WhatsApp caché, se ha arreglaro en errores con veilis, veilis es el protocolo, digamos la forma en la que se conecta a volisionapy con WhatsApp, con meta, y ya existe veilis, Existir. también a través de la ápio oficial de whatsapp, pero bien no le veo mucho caso para eso vamos a cambiar el piocesal, entonces vamos a usar la debilis y en este caso vamos a usar vamos a usar la 2.3.6, vamos regresamos a Easy Panel, simplemente aquí cambiamos el 0 por el 6 y le vamos a crear, nos dice que vayamos al proyecto. y tenemos que esperar a que termines de carga que vamos a ver cómo está iniciando todos los servicios si dice que está listo si nos vamos a ver aquí el domain o el domino que nos creo y aquí podemos acceder si os le damos aquí un dice open nos va a mandar siempre te va a mandar aquí lo único que tiene que hacer es ponerle Diagonal Manager y se van a ir a esta página de configuración. Este su serve yo a él es básicamente la misma URL o el domino no tenga su servidor y no está peendo aquí un número walkie. Como lo obtenemos regresamos a la parte de Isipane. aquí abajo donde dice environment o variables de torno, si lo tiene en español, lo seleccionamos, nos vamos ir hasta abajo y donde dice authentication IP aquí, van a copiar ese número, lo regresan a Evolution y lo van a pegar y le dan login, listo y hasta nadentro y una vez que estén aquí ya desde aquí van a voy a darle el más, crear la instancia con el nombre que ustedes quieran y aquí son los tres protocolos de Evolution, WhatsApp Cloud, API y VALYS, no me tenio por centros los casos de los VALYS, no tienen que poner ahorita el número más adelante cuando lo cofibure y aquí ustedes pueden poner el nombre, mi recomendación es no pongan espacios, entonces quiero saber por ejemplo En período digital, alguna vez es de error los espacios, la verdad no se hable por qué, aquí vemos que tenemos la versión 2.3.6 y aquí está su instancia y ya pueden conectar su número de aquí.
