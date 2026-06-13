# 🎥 [PASO 1] Cómo instalar n8n en tu VPS

> Ruta: Automatizaciones n8n › 🎥 [PASO 1] Cómo instalar n8n en tu VPS

**🎬 Vídeo (11.4 min):** https://youtu.be/EFcGuhY8XWk?si=XnH6vah1JCLMTBG6

---

Imperiales, hoy les traigo el paso a paso definitivo para montar su propia instalación de n8n en un servidor VPS **en 5 minutos.**

Seamos sinceros: la versión Cloud de n8n es genial para probar, pero $24 USD al mes por solo 2,500 ejecuciones es un límite que se queda corto muy rápido. La forma real, escalable y "cool" de hacerlo es teniendo **tu propio servidor**.

No solo es hasta un 70% más económico, sino que te da control total para lo que se viene (como conectar Evolution API para nuestros Agentes de WhatsApp).

**📌 ¿Qué vas a tener al final de este tutorial?**

- Un **VPS KVM 2** en Hostinger optimizado.
- **n8n instalado** automáticamente (sin pelear con código desde cero).
- **100 Workflows** pre-cargados listos para usar.
- Tu propio **dominio profesional** (tipo `n8n.tudominio.com`).
- La infraestructura lista para el **Curso de **[**Agentes de WhatsApp**](https://www.skool.com/imperio-digital/classroom/b8e3a86b?md=f7ffc3a3b7c34798844e3285a0cb4548).

---

### **🔧 Paso 1. Elegir el VPS correcto**

Para correr automatizaciones y agentes que se vean increíbles, necesitamos un buen motor. En el video usamos Hostinger por la facilidad de su plantilla pre-instalada (y ya que tienen un plan de afiliados, aunque igual los usaba de antes).

1. Entra a [**hostinger.com/benjamin10**](https://www.google.com/search?q=https://hostinger.com/benjamin10&authuser=1).
2. Elige el plan **KVM 2**. - *Pro tip:* El KVM 1 se queda corto de RAM y el 4 es demasiado para empezar. El 2 es el punto dulce.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9e5ad7e8849f44d99fce1a205adb22e3ac8b651c201e413cbb9e7e3a8fe344cb-md.png)

1. Selecciona el periodo (recomendado 24 meses para olvidarte del tema).
2. Si te fuiste por los 24 meses, y nos quieres ayudar, usa el cupón `BENJAMIN10` para un 10% extra de descuento.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4b17c9b1814343b1957988ab05fd3e8d355d2024089b41c087524d848e4c4113.png)

**⚠️ MUY IMPORTANTE:** Al configurar el servidor, en la sección de Sistema Operativo, elige la opción **"Application"** y busca **"Ubuntu with n8n" o "n8n + 100 workflows"**. Esto te ahorrará horas de instalación manual de Docker.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/96e6a61f45764b08ba74781d01eaf7f336128df10efe4edb9ec293b9b11ff335.png)

---

### **🖥️ Paso 2. Configuración inicial y Licencia**

Una vez que el VPS se termine de instalar:

1. Desde el panel de Hostinger, dale a **"Administrar aplicación"**.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/316be6a6680542fc9ad3ff91c8c3973d947e4da2c8eb4e07b542335accfcf448-md.png)

1. Crea tu cuenta de administrador (correo y contraseña).
2. **Activa la licencia:** Aunque es self-hosted, n8n pide un registro gratuito para desbloquear ciertas funciones. Te llegará un correo, copias la *License Key* y la pegas en *Settings > Usage and Plan*.

Listo! Ya tienes n8n corriendo con 100 plantillas preinstaladas.

---

### **🌐 Paso 3 (OPCIONAL). Conectar tu Dominio Propio (Adiós IP fea)**

No queremos entrar a `http://https://n8n.srv1169942.hstgr.cloud/home/workflows`. Queremos algo profesional como `n8n.tuagencia.com`.

Para esto, hay que hacer dos cosas: apuntar el dominio al VPS y configurar n8n para que reconozca ese dominio.

**1. Apuntar el dominio al VPS:** Debes configurar los registros DNS (tipo A) para que tu dominio redirija a la IP de tu nuevo servidor. 

👉 **Guía oficial:** [Cómo apuntar un dominio a tu VPS en Hostinger](https://www.hostinger.com/support/1583227-how-to-point-a-domain-to-your-vps-at-hostinger/)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d8af22f98cb6485486bf639f18fcb57c845b2417a52d4f14b27d1004ab8db5c7-md.png)

**2. Cambiar la configuración interna de n8n:** Una vez apuntado el dominio, debemos decirle a n8n (a través de la terminal del navegador) que use ese nuevo nombre. 

👉 **Guía oficial:** [Cómo cambiar el dominio de n8n en tu VPS](https://www.hostinger.com/support/11927159-changing-the-domain-for-n8n-on-vps-at-hostinger/)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8ff43d9f428a428bae5da9ce5735bfa8907bd71da5414738aa5c812fc4fda9ce-md.png)

*Nota: La certificación SSL (el candadito seguro HTTPS) se generará automáticamente, pero puede tardar unos minutos u horas en propagarse. Paciencia.*

---

### **🔄 Paso 4. Mantenimiento: Cómo actualizar n8n**

A diferencia del Cloud, aquí tú eres el dueño del servidor, por lo que n8n no se actualiza solo. Pero no te preocupes, Hostinger lo hace muy fácil usando la "Browser Terminal".

Cuando salga una nueva versión con features que quieras probar, sigue estos pasos: 👉 **Guía oficial:** [Cómo actualizar n8n en Hostinger](https://www.hostinger.com/support/11767754-how-to-update-n8n-at-hostinger/)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3aae6c1a12884fb08eb4aa5c67bcab284a040526fb064250b08e5869a62f6929-md.png)

### **🚀 ¿Por qué hicimos todo esto?**

Porque para jugar en las grandes ligas de la IA, necesitas infraestructura propia.

Este servidor es la base fundamental para lo que estamos viendo en el** Curso de Agentes de WhatsApp**, donde conectamos n8n con Evolution API para crear asistentes de IA reales y potentes para negocios.

Si ya tienes tu servidor listo, el siguiente paso es ir directo al curso y empezar a montar tu agente:

👉 **Ir al Curso de Agentes de WhatsApp + Plantilla Oficial**

¡A construir Imperiales!
