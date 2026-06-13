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
