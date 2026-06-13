# Supabase Self-Hosted en tu VPS — Guía Completa

> Ruta: Vibe-Coding › Supabase Self-Hosted en tu VPS — Guía Completa

**🎬 Vídeo (34.3 min):** https://youtu.be/FrO9eRAhOaw

**📎 Recursos:**
- GUIA Coolify y Supabase

---

**Esta guía documenta el proceso real de instalación**, incluyendo los errores que encontré y cómo los resolví. No es el camino feliz, es lo que realmente pasa.

## ¿Por qué self-hostear Supabase?

Supabase Cloud cobra **$25/mes por proyecto**. Si tienes 3-4 proyectos corriendo, ya estás pagando $75-100 al mes. Self-hosted en tu VPS existente cuesta $0 adicional.

**¿Cuándo SÍ tiene sentido?**

- Tienes 2 o más proyectos que usan Supabase
- Tienes un VPS con mínimo 4 GB RAM disponibles
- Quieres control total sobre tus datos
- Necesitas pgvector para proyectos de IA sin costo extra

**¿Cuándo NO tiene sentido?**

- Eres principiante total en servidores
- Solo tienes un proyecto — $25/mes vale la pena por la comodidad
- No quieres responsabilidad de backups y actualizaciones

## Lo que vas a tener al final

El mismo dashboard visual de Supabase que conoces — Table Editor, SQL Editor, Authentication, Storage, Edge Functions — corriendo en tu servidor, accesible en tu propio dominio con HTTPS.

## Specs del entorno de esta guía

- **Servidor:** Hostinger KVM2 — 2 vCPU / 8 GB RAM / 100 GB NVMe
- **Panel:** Coolify con Traefik como reverse proxy
- **OS:** Ubuntu 22.04 LTS
- **Contenedores:** ~12 servicios Docker simultáneos
- **RAM en reposo:** ~1.5 GB por instancia de Supabase

## Antes de empezar, ten listo

- VPS con Coolify instalado y corriendo
- Un dominio o subdominio disponible (ej: `supabase.tudominio.com`)
- Acceso SSH al servidor
- Cuenta de email para SMTP (usaremos Resend o Gmail)

## PASO 1 — Preparar el servidor

Conéctate por SSH:

bash

```bash
ssh root@TU_IP_VPS
```

Actualiza el sistema:

bash

```bash
apt update && apt upgrade -y
```

Verifica que Docker está corriendo:

bash

```bash
docker --version
docker ps
```

### Crear Swap de 2 GB ⚠️ No te saltes este paso

Supabase inicia 12 contenedores simultáneos. Sin swap, el servidor puede crashear durante el arranque inicial por falta de memoria — aunque tengas 8 GB de RAM.

bash

```bash
fallocate -l 2G /swapfile
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
echo '/swapfile none swap sw 0 0' | tee -a /etc/fstab
free -h
```

El último comando debe mostrar una línea de Swap con 2 GB.

## PASO 2 — Configurar DNS

En tu proveedor de dominio crea un registro A:

```
Tipo:   A
Nombre: supabase
Valor:  TU_IP_VPS
TTL:    300
```

Verifica que propagó:

bash

```bash
nslookup supabase.tudominio.com
```

Debe responder con la IP de tu VPS. Si no, espera 5-10 minutos y vuelve a intentarlo. **No continúes hasta que esto funcione** — si el DNS no resuelve cuando haces el deploy, el certificado SSL falla y tienes que redesployar.

## PASO 3 — Verificar Coolify

Abre Coolify en el navegador:

```
http://TU_IP_VPS:8000
```

Ve a **Servers → localhost → Proxy** y verifica que Traefik esté en verde (Running).

Si no está activo, click en **Start Proxy**.

## PASO 4 — Desplegar Supabase

### Crear el proyecto

1. Click en **"+ New Project"**
2. Nombre: `supabase-production`
3. Click "Continue" → environment: **production**
4. Click "Create"

### Agregar el servicio

1. Click en **"+ Add New Resource"**
2. Buscar "Supabase" en el buscador
3. Seleccionar **Supabase** de los one-click services
4. Servidor: **localhost**

### Configurar el dominio

En el campo de dominio escribe tu subdominio

```
supabase.tudominio.com
```

Click en **Deploy** y espera 5-15 minutos. Coolify descarga las imágenes de los 12 contenedores del stack.

### El contenedor "Minio Create Bucket" en rojo — es normal

Ese contenedor aparece en rojo con estado "Exited" y genera confusión. **No es un error.** Es un job de inicialización que corre una sola vez para crear los buckets de storage y luego termina. "Exited" es su estado correcto.

## PASO 5 — Fix del 404 (lo que me pasó en la instalación real)

Al entrar a `supabase.tudominio.com` me salió un **404**. Lo que lo resolvió:

**Problema:** El template de Coolify a veces guarda la URL sin el protocolo `https://` y Traefik no puede enrutar la petición correctamente.

**Solución en dos partes:**

1. Ir a Coolify → servicio Supabase → configuración del dominio → verificar que el URL tiene `https://` explícito. Si no lo tiene, agréguenlo manualmente.
2. Ir a **Environment Variables** y agregar:

```
SERVICE_FQDN_SUPABASESTUDIO=studio.tudominio.com
```

1. Click en **Redeploy**.

📸 **[SCREENSHOT: campo de Environment Variables con SERVICE_FQDN_SUPABASESTUDIO configurado]**

Después del redeploy, entra directamente a:

```
https://supabase.tudominio.com
```

## PASO 6 — Acceder al dashboard

El dashboard de Supabase Studio está en:

```
https://supabase.tudominio.com
```

Las credenciales están en Coolify → Environment Variables:

```
DASHBOARD_USERNAME
DASHBOARD_PASSWORD
```

**Cambia estas credenciales inmediatamente** después del primer login.

## PASO 7 — Obtener las claves API

En Coolify → Environment Variables busca estas dos claves:

```
SERVICE_SUPABASEANON_KEY     → clave pública (va en el frontend)
SERVICE_SUPABASESERVICE_KEY  → clave privada (NUNCA en el frontend)
```

Guárdalas en tu password manager ahora.

⚠️ **La Service Role Key tiene acceso total a tu base de datos ignorando todas las reglas de seguridad. Nunca la pongas en código del lado del cliente ni en repositorios públicos.**

## PASO 8 — Cambiar el Tenant ID del pooler

El ID por defecto `dev_tenant` es predecible y representa un riesgo de seguridad. **Hazlo antes del primer uso real.**

Genera un ID aleatorio seguro:

bash

```bash
openssl rand -hex 16
```

En Coolify → **Edit Compose File**, busca `supabase-supavisor` y agrega:

yaml

```yaml
supabase-supavisor:
  environment:
    - POOLER_TENANT_ID=pega-aqui-el-valor-generado
```

Guarda y haz **Redeploy**.

## PASO 9 — Configurar SMTP

Sin SMTP configurado, Supabase no puede enviar magic links, confirmaciones de email ni recuperación de contraseña.

### Opción A — Resend (recomendado)

3,000 emails gratis al mes. Crea cuenta en resend.com, verifica tu dominio, genera un API Key.

En Coolify → Environment Variables agrega:

```
SMTP_HOST=smtp.resend.com
SMTP_PORT=587
SMTP_USER=resend
SMTP_PASS=tu-api-key-de-resend
SMTP_SENDER_NAME=Mi App
SMTP_ADMIN_EMAIL=correo@tudominio.com
```

### Opción B — Gmail App Password

Activa verificación en dos pasos en tu cuenta Google → Seguridad → Contraseñas de aplicaciones → crea una para "Supabase".

```
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=tucorreo@gmail.com
SMTP_PASS=xxxx-xxxx-xxxx-xxxx
SMTP_SENDER_NAME=Mi App
SMTP_ADMIN_EMAIL=tucorreo@gmail.com
```

Después de guardar, haz **Redeploy**.

**Nota importante sobre multi-proyecto:** El SMTP se configura a nivel de instancia, no por proyecto. Si necesitas cuentas de email separadas para proyectos diferentes, necesitas instancias de Supabase separadas en Coolify.

## PASO 10 — Configurar Firewall

bash

```bash
# CRÍTICO: permite SSH PRIMERO, antes de activar UFW
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw allow 8000/tcp
ufw enable
ufw status verbose
```

⚠️ **Si activas UFW sin el **`allow 22` primero, pierdes acceso SSH al servidor.

El puerto 5432 (PostgreSQL) **nunca** debe estar abierto públicamente. Para conectarte a la DB desde tu máquina local usa un SSH tunnel:

bash

```bash
ssh -N -L 5432:localhost:5432 root@TU_IP_VPS
```

## PASO 11 — Habilitar pgvector

En el dashboard → **SQL Editor**:

sql

```sql
-- Habilitar extensión
CREATE EXTENSION IF NOT EXISTS vector;

-- Verificar
SELECT extversion FROM pg_extension WHERE extname = 'vector';
```

Para crear una tabla con soporte de embeddings:

sql

```sql
CREATE TABLE items (
  id         UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  content    TEXT NOT NULL,
  embedding  vector(1536),
  metadata   JSONB,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX ON items USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);
```

## PASO 12 — Backups automáticos

Supabase self-hosted no hace backups automáticos. Este paso no es opcional.

Crea el script (reemplaza el nombre del contenedor con el tuyo):

bash

```bash
nano /home/backup-supabase.sh
```

Pega esto:

bash

```bash
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/root/backups/supabase"

mkdir -p $BACKUP_DIR

docker exec supabase-db-XXXXXXXXXXXXXXXX pg_dump \
  -U postgres -F c -b postgres \
  > $BACKUP_DIR/backup_$DATE.dump

find $BACKUP_DIR -name "backup_*.dump" -mtime +7 -delete

echo "[$DATE] Backup completado: backup_$DATE.dump"
```

Para encontrar el nombre exacto de tu contenedor de DB:

bash

```bash
docker ps --filter name=supabase-db --format "{{.Names}}"
```

Guarda con `Ctrl+X → Y → Enter`, luego:

bash

```bash
chmod +x /home/backup-supabase.sh

# Prueba que funciona
/home/backup-supabase.sh

# Verifica que se creó el archivo
ls -lh /root/backups/supabase/
```

Automatiza con cron:

bash

```bash
crontab -e
```

Agrega al final:

```
0 2 * * * /home/backup-supabase.sh >> /var/log/supabase-backup.log 2>&1
```

Verifica que quedó:

bash

```bash
crontab -l
```

## PASO 13 — Conectar tu app

Variables de entorno para Next.js:

env

```env
NEXT_PUBLIC_SUPABASE_URL=https://supabase.tudominio.com
NEXT_PUBLIC_SUPABASE_ANON_KEY=tu-anon-key
SUPABASE_SERVICE_ROLE_KEY=tu-service-role-key
```

## Checklist final

- Swap de 2 GB creado y en /etc/fstab
- DNS propagado y verificado con nslookup
- Traefik activo en Coolify
- Todos los contenedores en verde (excepto Minio Create Bucket)
- Dashboard accesible via HTTPS
- Credenciales del dashboard cambiadas
- Claves API guardadas en password manager
- Tenant ID del pooler personalizado
- SMTP configurado y testeado
- Firewall UFW activo
- Puerto 5432 cerrado al público
- pgvector habilitado
- Script de backup creado y cron configurado
- App conectada y funcionando

## Recursos adicionales

- Documentación oficial de Supabase self-hosting: supabase.com/docs/guides/self-hosting
- Documentación de Coolify: coolify.io/docs
- Resend para emails transaccionales: resend.com
- El PDF descargable de esta guía está disponible en los archivos de la comunidad
