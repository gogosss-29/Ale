# [Curso] 🛡️ Seguridad y Túnel Privado - Tailscale

> Ruta: 🦞 Reto Imperial OpenClaw › [Curso] 🛡️ Seguridad y Túnel Privado - Tailscale

**🎬 Vídeo (23.9 min):** https://www.loom.com/share/7f64fa4debe444898693eb3dc886bd8b

---

## 🎯 Objetivo

Cerrar **completamente** el acceso público a OpenClaw y permitir acceso **solo desde tus dispositivos**, usando:

- Tailscale (VPN privada)
- Firewall del servidor
- Validaciones reales de funcionamiento

Si no haces esto, tu OpenClaw **queda expuesto a Internet**.

## 🚨 El problema real (por qué esto es obligatorio)

Si OpenClaw queda accesible por IP pública:

- Bots escanean puertos automáticamente
- Servicios como Shodan indexan tu servidor
- Ataques de fuerza bruta
- Robo de API Keys
- Acceso a memoria del agente
- Ejecución de comandos en tu VPS

Esto **pasa todo el tiempo**, no es teoría.

## ✅ La solución

**Tailscale**:

- VPN privada
- Red cerrada solo a tus dispositivos
- Hasta **100 dispositivos gratis**
- Sin exponer puertos públicos
- Compatible con VPS, laptop, celular

## 📚 Recurso base

Te dejo el enlace (placeholder) a la guía completa usada como referencia:

👉 **ENLACE GITHUB GIST – Guía de seguridad OpenClaw / CloudBot / MoltBot**

```
https://gist.github.com/benjacord/848a8bcc62d0483e41063609e947ec36
```

## 🧭 Paso 1. Estado actual (inseguro)

Hasta ahora:

- Accedemos vía `127.0.0.1` o túnel manual
- El panel **puede quedar expuesto**
- No hay aislamiento real

Vamos a corregir esto.

## 🔐 Paso 2. Instalar Tailscale en el VPS

### Instalación (manual y segura)

Ejecutar **como root** en el VPS:

```
curl -fsSL https://tailscale.com/install.sh | sh

```

## 🔑 Paso 3. Autenticar Tailscale en el servidor

Después de instalar:

```
sudo tailscale up

```

Esto te dará:

- Un link de autenticación
- Login con Google, GitHub u otro proveedor

## 🧠 Paso 4. Iniciar sesión en Tailscale

En el navegador:

- Inicia sesión con tu cuenta
- Autoriza el dispositivo (VPS)

Resultado esperado:

- VPS conectado a la red privada Tailscale

![Google Chrome 2026-02-06 15.46.33.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2a689bae787741de9455a559bfd925d7524e85ddeea54080bdc94a4573702823)

## 💻 Paso 5. Instalar Tailscale en tu computadora

Instala Tailscale en:

- Mac / Windows
- Celular (opcional pero recomendado)

Proceso:

- Descargar app
- Iniciar sesión con la **misma cuenta**
- Autorizar el dispositivo

## 🔎 Paso 6. Verificar conexión privada

En el VPS:

```
tailscale status

```

Debes ver:

- VPS
- Tu computadora
- Otros dispositivos autorizados

## 🌐 Paso 7. Acceder al panel de OpenClaw vía IP privada

Tailscale asigna una IP privada, por ejemplo:

```
100.x.x.x

```

Accede a OpenClaw usando:

```
http://IP_TAILSCALE:PUERTO

```

⚠️ Importante:

- OpenClaw escucha en loopback por defecto
- **No todas las IPs funcionarán**
- Esto es normal y más seguro

## 🧯 Paso 8. Configurar Firewall (UFW)

Ahora vamos a **cerrar todo** excepto:

- SSH (por seguridad)
- Red Tailscale

### Ver estado del firewall

```
sudo ufw status

```

### Configuración recomendada

```
sudo ufw default deny incoming
sudo ufw default allow outgoing

```

### Permitir SSH (emergencia)

```
sudo ufw allow ssh

```

### Permitir tráfico desde Tailscale

```
sudo ufw allow in on tailscale0

```

### Activar firewall

```
sudo ufw enable

```

## ✅ Paso 9. Validaciones obligatorias

### 1. Probar acceso público (DEBE FALLAR)

- Intenta acceder por IP pública
- Resultado esperado: ❌ NO CARGA

### 2. Probar Telegram

Desde Telegram:

```
Hola, ¿sigues online?

```

Resultado esperado:

- ✅ Responde correctamente

### 3. Probar panel web vía Tailscale

- Accede desde IP privada
- Chat funcional

## 🧠 Qué logramos con esto

- OpenClaw **no es visible en Internet**
- No aparece en Shodan
- No responde a escaneos
- Solo tus dispositivos acceden
- Telegram sigue funcionando
- Panel web sigue funcionando

## ⚠️ Notas importantes

- El firewall puede bloquearte si configuras mal
- Mantén siempre acceso SSH
- No instales skills sin revisar código
- No guardes API Keys sensibles sin rotación

## ✅ Resultado final

- VPN privada activa
- Firewall configurado
- Panel protegido
- OpenClaw operativo
- Seguridad de nivel profesional
