# [Curso] Instalación en VPS con Hostinger

> Ruta: Vibe-Coding › [Curso] Instalación en VPS con Hostinger

**🎬 Vídeo (17.8 min):** https://www.loom.com/share/426a6b039fec4b8a8331885dd4ec0a7f

---

## 🎯 Objetivo

Instalar OpenClaw **correctamente**, desde consola, en un VPS limpio, siguiendo **buenas prácticas de seguridad**.  
Nada de instalaciones preconfiguradas. Nada de correr agentes como root.

## 🧠 Contexto rápido (importante)

OpenClaw ha tenido varias etapas:

- ClawdBot
- MoltBot
- OpenClaw (versión actual)

En este curso **usaremos OpenClaw**, instalado manualmente en un VPS con **Hostinger**, usando **Ubuntu LTS**.

## 🧩 Qué vamos a cubrir

- Contratación del VPS correcto en Hostinger
- Elección del sistema operativo
- Acceso por SSH
- Buenas prácticas iniciales de seguridad
- Creación de usuario dedicado para OpenClaw
- Instalación oficial de OpenClaw

## 🖥️ Paso 1. Contratar un VPS en Hostinger

### Recomendación de plan

- **Plan recomendado**: KVM2
- Más que suficiente para OpenClaw
- Escalable más adelante

📌 Ubicación recomendada:

- Elige el país **más cercano a ti**

![CleanShot 2026-02-06 at 15.30.05.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/58bc79a0b75342008c7909a3df1e49f81a4d28a231d848a78869bbf31c5c145e-md.png)

### Sistema operativo

- Elegir **Ubuntu**
- Versión recomendada: **Ubuntu 24.04 LTS**

> Siempre usa LTS. Son versiones estables, probadas y menos problemáticas.

## 🔐 Paso 2. Crear contraseña root y finalizar setup

- Hostinger te pedirá crear un **password root**
- Usa un **password manager**
- Guarda este password. Lo vas a necesitar

Opciones adicionales:

- SSH Key: **NO por ahora**
- Malware scanner: opcional
- Docker Manager: **NO necesario para este tutorial**

Finaliza el setup y espera a que el VPS se configure (2–3 minutos).

### 🌐 Paso 3. Acceder al VPS por SSH

Desde el panel de Hostinger:

- Copia el comando SSH que te proporcionan

Ejemplo genérico:

```
ssh root@TU_IP_DEL_SERVIDOR

```

### Primer acceso

Al conectarte:

- Te preguntará si confías en el servidor
- Escribe `yes` y presiona Enter
- Luego pega la **contraseña root** (no se verá al escribir)

> Es normal. Las contraseñas no se muestran en terminal.

---

## 🚨 PARÉNTESIS DE SEGURIDAD (MUY IMPORTANTE)

❌ **NO instales OpenClaw como root**  
❌ **NO ejecutes agentes como root**

¿Por qué?

- Root tiene control total del servidor
- Si algo sale mal, comprometes TODO el VPS
- Es una pésima práctica de seguridad

✔️ Solución correcta:

- Crear un **usuario dedicado solo para OpenClaw**

## 👤 Paso 4. Crear usuario dedicado para OpenClaw

Ejecuta este comando **estando como root**:

```
adduser openclaw

```

### 🔑 Configuración del nuevo usuario

- Crea una contraseña **diferente** a la de root
- Usa un password fuerte
- El resto de los campos son opcionales

## 🛂 Paso 5. Dar permisos sudo al nuevo usuario

Ejecuta:

```
usermod -aG sudo openclaw

```

Esto permite que el usuario:

- Use `sudo`
- Instale software
- Administre servicios  
Sin ser root directamente.

## 🔄 Paso 6. Cambiar al usuario OpenClaw

Ahora cambia de usuario:

```
su - openclaw (o como lo hayan llamado)

```

Si todo salió bien, verás algo como:

```
openclaw@tu-servidor:~$

```

✔️ Ahora sí estamos en un entorno seguro.

![CleanShot 2026-02-06 at 15.33.39.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/efac04f8d6544b8f83da1a725bc6fdb8f2ad35e1498b4b7faedcdecc14a71537.png)

## 📦 Paso 7. Instalar OpenClaw (forma correcta)

1. Ve **SIEMPRE** a la página oficial de OpenClaw
2. Copia el comando de instalación oficial

```
curl -fsSL https://clawd.bot/install.sh | bash

```

Ejecuta el comando **como el usuario openclaw**, NO como root.

### Durante la instalación

- Te pedirá la contraseña del usuario `openclaw`
- Descargará dependencias
- Instalará OpenClaw
- Lanzará el setup inicial

## ⚠️ Advertencia de seguridad de OpenClaw

Durante el setup verás advertencias como:

- Proyecto open source
- Software en beta
- Riesgos de seguridad
- Recomendación de auditorías frecuentes

Acepta conscientemente y continúa.

### Tipo de instalación

Cuando te pregunte:

- **Quick Start** ✅
- Manual ❌ (lo veremos más adelante)

## ✅ Resultado esperado al final de esta página

- VPS activo en Hostinger
- Usuario dedicado `openclaw`
- OpenClaw instalado correctamente
- Sin correr nada como root
- Base sólida y segura
