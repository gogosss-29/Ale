# 💬 Instalación de Chatwoot en tu VPS con EasyPanel

> Ruta: Automatizaciones n8n › 💬 Instalación de Chatwoot en tu VPS con EasyPanel

**🎬 Vídeo (17.1 min):** https://www.loom.com/share/f571b6bfdb8e409b842a47d4caebef0d

---

En este video te enseño cómo instalar **Chatwoot** en tu propio VPS usando **EasyPanel**, y además cómo **activar todas las funciones de la versión Enterprise sin pagar la suscripción cloud**. Incluye troubleshooting real de conflictos con contenedores y base de datos.

Esto te deja listo para.

- Tener tu propio sistema tipo Intercom / Zendesk
- Conectar WhatsApp, WebChat, Instagram, Facebook
- Integrarlo con n8n, OpenAI y tus bots
- Sin límites por licencias cloud

## 🧱 Prerrequisitos

Antes de empezar debes tener listo.

- VPS con Ubuntu 22.04 o superior
- Docker instalado
- EasyPanel funcionando
- Acceso SSH al servidor (root)

Si no tienes esto, revisa primero el video de instalación de VPS + EasyPanel.

## 🧩 Paso 1. Crear proyecto para Chatwoot en EasyPanel

1. Entra a EasyPanel
2. Ve a **Projects → Create Project**
3. Nombre del proyecto.

```
chatwoot

```

1. Guardas el proyecto

![CleanShot 2025-12-03 at 13.20.11.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7dcf335e301e4b4bbea6441137124b344c739b62506e494eb0d158e80885666d.png)

## 🧱 Paso 2. Instalar Chatwoot desde Templates

1. Dentro del proyecto **chatwoot**
2. Ve a **Add Service → Templates**
3. Busca **chatwoot**
4. Configura. - Language. `es`
- Name. `chatwoot`
- Version. Verificamos primero en GitHub

Abre en otra pestaña.

```
https://github.com/chatwoot/chatwoot/releases

```

En el video la versión estable es.

```
4.8.0

```

1. Regresa a EasyPanel y cambia la versión
2. Presiona **Create**

![CleanShot 2025-12-03 at 13.21.08.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8b7a3efc08b94de2b7d8cac3aa37e4900246ca3f345d4c40b1910461b2e0d697.png)

## ⏳ Paso 3. Despliegue e ingreso inicial

EasyPanel hace el deploy automático.  
Cuando diga **Listening** o **Running**.

1. Ve a **Domains → Open**
2. Se abre el instalador web de Chatwoot
3. Crea la cuenta inicial (solo demo).
4. Inicia sesión

## 🧠 Paso 4. Verificando que estás en Community Edition

Dentro de Chatwoot.

1. Ve a **Profile → Super Admin**
2. Entra con el mismo correo
3. Ve a **Settings → Plans**

Aquí verás.

```
Current Plan: Community Edition

```

Todo marcado como **bloqueado**.  
Bots, SSO, Custom Branding, Audit Logs, Captain, etc.

## 🧨 Paso 5. Habilitar Enterprise sin pagar usando variables de entorno

Aquí está el truco real.

### 5.1 Copiar URL base de Chatwoot

En tu navegador copia la URL base hasta `/app`

Ejemplo.

```
https://TU_URL/app

```

### 5.2 Inyectar variable en EasyPanel

En EasyPanel.

1. Abre el servicio **chatwoot**
2. Ve a **Environment Variables**
3. Agrega una nueva línea.

```
CHATWOOT_WEBHOOK_URL=http://TU_DOMINIO_O_IP/#

```

1. Guarda
2. Deploy del servicio

Repite EXACTAMENTE lo mismo también en.

- Servicio de **chatwoot-sidekiq**

Todos deben llevar la misma variable.

## 🔐 Paso 6. Conexión por SSH al VPS

Ahora vamos a modificar archivos internos del contenedor.

Conéctate por SSH.

```
ssh root@<TU IP>

```

Ingresa la contraseña del VPS.

![CleanShot 2025-12-03 at 13.26.42.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9bd5bf3f798340c6b00f8e7c876d4d76e28bad649ea0460491bd595e57cbb2c6.png)

## 🗄️ Paso 7. Verifica tu base de datos de Chatwoot

En EasyPanel revisa.

- Usuario. `postgres`
- Base de datos. `chatwoot`
- Host. nombre del servicio postgres

Esto lo usaremos para el SQL.

## 🧬 Paso 8. Inyectar Enterprise en la base de datos

Ejecuta este bloque completo en tu VPS.  
OJO. el nombre del contenedor puede variar. Ajusta `chatwoot-db`.

```
docker exec -i "$(docker ps -q --filter 'name=chatwoot-db')" psql -U postgres -d chatwoot -c "
UPDATE public.installation_configs 
SET serialized_value = '\"--- !ruby/hash:ActiveSupport::HashWithIndifferentAccess\nvalue: enterprise\n\"' 
WHERE name = 'INSTALLATION_PRICING_PLAN';

UPDATE public.installation_configs 
SET serialized_value = '\"--- !ruby/hash:ActiveSupport::HashWithIndifferentAccess\nvalue: 10000\n\"' 
WHERE name = 'INSTALLATION_PRICING_PLAN_QUANTITY';

UPDATE public.installation_configs 
SET serialized_value = '\"--- !ruby/hash:ActiveSupport::HashWithIndifferentAccess\nvalue: e04t63ee-5gg8-4b94-8914-ed8137a7d938\n\"' 
WHERE name = 'INSTALLATION_IDENTIFIER';"

```

## ⚠️ Paso 9. Troubleshooting de conflictos de contenedor

En el video ocurrió un error porque ya existía otro contenedor llamado igual.

Solución real aplicada.

1. Renombrar servicio
2. Renombrar base de datos
3. Hacer redeploy limpio
4. Volver a ejecutar los comandos SQL

Esto pasa cuando.

- Tienes más de una instalación de Chatwoot
- Dos servicios apuntan a la misma DB

Si te pasa, debes.

- Cambiar el nombre de la DB
- Editar variables de entorno
- Volver a desplegar

## ✅ Paso 10. Verificación de que ya eres Enterprise

Regresa a Chatwoot.

1. Profile → Super Admin
2. Settings → Plans

Debe decir ahora.

```
Current Plan: Enterprise

```

Y verás todo habilitado.

- Captain
- Custom Branding
- Audit Logs
- SSO
- Bots completos

![CleanShot 2025-12-03 at 13.31.11.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f892fc8c4666437a9327fb20629b7e882d87a6f17cd740a185428fd8a4faebd7.png)

## ✅ Resultado final

Ahora tienes.

- Chatwoot Enterprise
- En tu propio VPS
- Sin mensualidad cloud
- Con control total
- Con posibilidad de automatizar todo
- Con integración directa con n8n y agentes IA

## ❗ Advertencias legales y técnicas

- Esto es para **uso interno, educativo o de agencia**
- Estás habilitando funciones enterprise vía backend
- No es vía plan oficial cloud
- Cada quien es responsable de su uso

##
