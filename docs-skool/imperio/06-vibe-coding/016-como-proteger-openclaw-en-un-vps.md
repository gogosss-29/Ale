# 🔒 Cómo Proteger Openclaw en un VPS

> Ruta: Vibe-Coding › 🔒 Cómo Proteger Openclaw en un VPS

---

## **⚠️ El Problema**

Si instalaste Clawdbot o Moltbot en un VPS (servidor virtual), tu control panel está expuesto a todo internet en una URL como:

```
http://TU_IP_PUBLICA:18789/
```

Ver Video instalación aquí: [https://www.skool.com/imperio-digital/classroom/6e17d0fa?md=7aa1c407bd5f40809a9072020ad5e8f7](https://www.skool.com/imperio-digital/classroom/6e17d0fa?md=7aa1c407bd5f40809a9072020ad5e8f7)

### **¿Por qué es grave?**

Existen servicios como **Shodan**, **Censys** y otros que escanean **TODAS** las direcciones IP de internet, las 24 horas del día, los 7 días de la semana. Indexan todo lo que encuentran y lo hacen buscable.

**Esto significa que:**

- Tu panel de control aparece en bases de datos públicas
- Cualquiera puede buscar "Clawdbot" y encontrar tu instancia
- Si alguien obtiene tu token (fuerza bruta, leak, phishing), tiene control total

### **¿Qué pueden hacer con acceso?**

- 📧 Leer todos tus mensajes (Telegram, WhatsApp, Signal, etc.)
- 📁 Acceder a tus archivos y memoria del agente
- 🤖 Ejecutar comandos en tu servidor
- 🔑 Robar API keys y credenciales guardadas
- 💬 Enviar mensajes haciéndose pasar por ti
- 🦠 Instalar skills maliciosos

**No es paranoia — ya está pasando.** Se estima que cientos o miles de instancias han sido comprometidas.

---

## **🛡️ La Solución: Tailscale**

**Tailscale** crea una red privada virtual (VPN) entre tus dispositivos, sin la complejidad de configurar una VPN tradicional.

### **¿Cómo funciona?**

1. Instalas Tailscale en tu VPS y en tu computadora
2. Ambos quedan en una "red privada" con IPs tipo `100.x.x.x`
3. Solo dispositivos con tu cuenta pueden verse entre sí
4. El resto de internet **no puede acceder**

### **Beneficios**

**AspectoSin TailscaleCon Tailscale**VisibilidadCualquiera te encuentraInvisible a scannersProtecciónSolo el tokenRed privada + tokenAccesoIP pública expuestaSolo tus dispositivosTelegram/Signal✅ Funciona✅ Sigue funcionando igual

**Tiempo de implementación:** ~10 minutos  
**Costo:** Gratis (hasta 100 dispositivos)

---

## **🚀 Opción 1: La Forma Fácil (Prompt para tu Agente)**

Si tu Clawdbot/Moltbot tiene acceso a terminal, simplemente envíale este mensaje:

```
Necesito que asegures este servidor con Tailscale para que el control panel no quede expuesto a internet. 

Pasos:
1. Instala Tailscale: curl -fsSL https://tailscale.com/install.sh | sh
2. Ejecuta: sudo tailscale up (dame el link para autenticar)
3. Espera a que yo instale Tailscale en mi computadora y me conecte
4. Cuando te confirme, cierra el puerto 18789 al público con UFW, permitiendo solo acceso desde la red de Tailscale (100.64.0.0/10)
5. Mantén SSH (puerto 22) abierto por si acaso

No cierres el puerto hasta que yo confirme que puedo acceder via la IP de Tailscale.

```

Tu agente debería guiarte por el proceso. Cuando te dé el link de autenticación:

1. Ábrelo y crea cuenta / logueate (puedes usar Google, GitHub, etc.)
2. Instala Tailscale en tu Mac/PC (ver abajo)
3. Confirma que puedes acceder via `http://IP_TAILSCALE:18789/?token=TU_TOKEN`
4. Dile al agente que cierre el puerto público

---

## **🔧 Opción 2: Instalación Manual Paso a Paso**

### **Paso 1: Instalar Tailscale en el VPS**

Conéctate a tu VPS por SSH y ejecuta:

```
curl -fsSL https://tailscale.com/install.sh | sh
```

### **Paso 2: Conectar el VPS a Tailscale**

```
sudo tailscale up
```

Te mostrará un link tipo `https://login.tailscale.com/a/xxxxx`

**Ábrelo en tu browser** y logueate (Google, GitHub, email, etc.)

Verifica que quedó conectado:

```
tailscale status
```

Deberías ver algo como:

```
100.x.x.x    tu-servidor    tu-email@    linux    -

```

**Anota la IP** (la `100.x.x.x`) — la necesitarás después.

### **Paso 3: Instalar Tailscale en tu Computadora**

**Mac (con Homebrew):**

```
brew install tailscale
brew services start tailscale
tailscale up
```

**Mac (sin Homebrew):** Descarga desde [https://tailscale.com/download/mac](https://tailscale.com/download/mac)

**Windows:** Descarga desde [https://tailscale.com/download/windows](https://tailscale.com/download/windows)

**Linux:**

```
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

⚠️ **Importante:** Logueate con la **MISMA CUENTA** que usaste en el VPS.

### **Paso 4: Verificar la Conexión**

Desde tu computadora, ejecuta:

```
tailscale status
```

Deberías ver tu computadora Y tu VPS en la lista.

Prueba el ping:

```
tailscale ping IP_TAILSCALE_DEL_VPS
```

Si responde, están conectados. ✅

### **Paso 5: Probar Acceso al Control Panel**

Abre en tu browser:

```
http://IP_TAILSCALE_DEL_VPS:18789/?token=TU_TOKEN

```

Por ejemplo:

```
http://100.101.208.49:18789/?token=abc123...

```

**¿Carga el control panel?** Perfecto, sigue al siguiente paso.

**¿No carga?** Verifica que:

- Tailscale está corriendo en ambos dispositivos
- Usaste la misma cuenta en ambos
- La IP es la correcta (la de Tailscale, no la pública)

### **Paso 6: Cerrar el Puerto Público**

Ahora que confirmaste que funciona via Tailscale, cierra el acceso público.

En tu VPS, ejecuta:

```
# Configurar políticas por defecto
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Permitir SSH (¡importante para no quedarte afuera!)
sudo ufw allow 22/tcp

# Permitir TODO desde la red de Tailscale
sudo ufw allow from 100.64.0.0/10

# Eliminar regla que expone el puerto 18789 (si existe)
sudo ufw delete allow 18789

# Activar el firewall
sudo ufw --force enable

# Verificar las reglas
sudo ufw status
```

Deberías ver algo como:

```
Status: active

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere
Anywhere                   ALLOW       100.64.0.0/10

```

**Nota:** El puerto 18789 **NO** debería aparecer como ALLOW desde Anywhere.

### **Paso 7: Confirmar que Quedó Cerrado**

La prueba final. Desde tu **celular con datos móviles** (desconecta el WiFi), intenta abrir:

```
http://TU_IP_PUBLICA:18789/

```

**Resultado esperado:** No carga / timeout / error de conexión.

Si no carga, **felicidades** — tu Clawdbot está protegido. 🔒

---

## **✅ Checklist Final**

- Tailscale instalado en el VPS
- Tailscale instalado en tu computadora
- Ambos dispositivos en la misma cuenta de Tailscale
- Puedes acceder al control panel via IP de Tailscale
- Firewall (UFW) activado
- Puerto 18789 NO está abierto al público
- Probado desde celular con datos (no carga la IP pública)

---

## **❓ Preguntas Frecuentes**

### **¿Telegram, WhatsApp, Signal siguen funcionando?**

**Sí, exactamente igual.** Esos servicios funcionan porque Clawdbot se conecta *hacia afuera* a sus servidores. No necesitan conexión entrante.

### **¿Puedo acceder desde cualquier lugar?**

**Sí**, mientras tengas Tailscale instalado y conectado en ese dispositivo. Puedes agregar tu celular también.

### **¿Qué pasa si pierdo acceso?**

SSH (puerto 22) quedó abierto. Puedes entrar por SSH y arreglar cualquier problema.

### **¿Tailscale es gratis?**

**Sí**, para uso personal (hasta 100 dispositivos). Más que suficiente.

### **¿Puedo agregar más dispositivos?**

Sí. Instala Tailscale en cualquier dispositivo, logueate con la misma cuenta, y automáticamente puede acceder a tu VPS.

### **¿Y si quiero que otra persona acceda?**

Tailscale tiene la opción de compartir dispositivos con otras cuentas (Tailscale Sharing). O puedes darle acceso a tu cuenta.

---

## **🆘 Si Algo Sale Mal**

### **Me quedé afuera del VPS**

SSH sigue abierto. Conéctate por SSH y revisa las reglas de UFW:

```
sudo ufw status
sudo ufw allow 18789  # Para abrir temporalmente
```

### **Tailscale no conecta**

Verifica que el servicio esté corriendo:

```
sudo systemctl status tailscaled
sudo systemctl restart tailscaled
```

### **No veo mi otro dispositivo**

Asegúrate de que ambos usen la misma cuenta. Revisa en [https://login.tailscale.com/admin/machines](https://login.tailscale.com/admin/machines)

---

## **📚 Recursos**

- [Tailscale - Sitio oficial](https://tailscale.com/)
- [Tailscale - Documentación](https://tailscale.com/kb/)
- [Video sobre vulnerabilidades de Clawdbot](https://youtu.be/rPAKq2oQVBs)

---

*Más vale 10 minutos de configuración que perder el acceso a tu agente. Protégete.* 🛡️
