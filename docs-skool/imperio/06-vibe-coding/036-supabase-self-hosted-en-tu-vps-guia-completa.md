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

## 🎙️ Transcripción

¿Cuánto te está costando Supas? Si tienes más de dos o tres proyectos corriendo en Supis Cloud, probablemente ya estés pagando 50 o más. Esto al mes, evidentemente. Hoy te voy a mostrar cómo correr suabase en tu propio servidor por prácticamente ser op adicionales. Evidentemente hay un gasto que es lo que ya estés pagando en tu servidor, en este caso BPS probablemente y más segue mis otros videos puede ser que ahí mismo tengas tu OpenClow, tu instancia de N8N o otros microservicios. Y honestamente no es nada complicado. Muchas veces cuando las personas escuchan que voy a hostear, vamos a hostear su pais, creen que es muy complicado, pero la verdad es que no lo es. Ahorita te voy a enseñar en el video que vamos a dar. Antes de entrar al tutorial, necesito explicarte algo muy importante. ¿Cuándo tiene sentido hacer esto? Y cuando la verdad no tiene sentido, porque no siempre la respuesta correcta es vamos a hostear todo. Eso es lo que no te dice en la mayoría de los videos. Para los que no conocen Supase, es básicamente un Firebase open source, pero construido sobre Postgress SQL, que es la base de datos relacional prácticamente más popular. En una sola plataforma te da base de datos postres SQL con APIs automática, tienes onticanción con email, o outices también bockets que son almacenamiento de archivos, funciones serverless y real time que te permite sincronizar en vivo entre tus diferentes usuarios. Y sobre todo tiene algo que Firebase no tiene, PG Vector. ¿Qué es esto? Significa que puede ser búsqueda semántica con inteligencia artificial directamente en tu base de datos. Muy útil para aplicaciones con RAG, chatbots o simplemente una búsqueda inteligente. Suabis Cloud es increíblemente cómodo, no me malentiendas. Lo abres, creas un proyecto, 30 segundos y ya tienes todo funcionando, todo corriendo. Únicamente necesitas tu URL del proyecto o tu ref project token, se lo pasas a tu agente o a tu proyecto y ya está funcionando. No tienes que hacer, pero el modelo de pricing no es tan escalable si estás haciendo muchas pruebas para producción. Ya a nivel una aplicación en producción es escala bastante bien, pero si eres alguien como yo que tiene muchas ideas, de repente crea un proyecto, crea otro, quiere probar una app, ya no es redituable. ¿Por qué? Porque tienes que ya después de dos proyectos tienes que brincar mínimo $25 al mes, más te cobran más o menos $10 por proyecto, más menos computing dependiendo qué tanto tráfico que tanto vayas haciendo. Así que si tienes un solo proyecto, Superbit Cloud, te queda muy bien. Si quieres empezar a escalar y tener varios proyectos y tener varias pruebas, ahí es donde se empieza a complicar un poco. La alternativa que vamos a hacer hoy es correr suabase en nuestro propio servidor. Open source, es el mismo producto, cero costo adicional. Si ya tienes el BPS, obviamente hay un tradeof, ¿cuál es el pero? Que tú eres responsable de los updates, de los backups y si algo se cae, pues al final tú eres el único responsable. También hay opciones intermedias. Existe Neon, que es un post de serverless muy barato, escala a cero, pero no te incluye out ni storage nativos y tienes que complementarlo con algunas otras soluciones. Pocket Base también es perfecto para proyectos pequeños, pero no tiene PG vector. Comvex, que es muy popular en estos días, es interesante, pero tiene un vendor locking. Básicamente no usa SQL estándar y va a ser muy difícil que después quieras migrar o llevártelo a alguna otra base de datos. Entonces vamos a ver cuando sí tiene sentido hacer self hosting. Cuando tienes dos o más proyectos que usan paves, cuando tienes un BPS ya comprado ya funcionando con recursos disponibles, en tiendas en mínimo 4 GB disponibles que no estás ocupando. Y también, ¿por qué no? cuando te sientes cómodo utilizando docker y conceptos un poco básicos de del servidor, cuando quieres tener control total sobre tus datos y cuando necesitas PG vector para proyectos de IA y no quieres estar pagando extra. Ahora, como todo, ¿cuándo no? Cuando eres principiante total en servidores, cuando tu proyecto es crítico y no puedes permitirte downtime por errores de configuración. Cuando solo tienes un proyecto no hace tampoco mucho sentido y sobre todo cuando el Roy no justifica el tiempo de setup, aunque es relativamente corto y ni estás a lanzar algún producto rápido y es tu único proyecto en esa cuenta, vete directamente a Supis Cloud. Honestamente, para hacer self hosting debase hay varias opciones. ¿Cuáles son las más populares? sobre todo en estos días toker directo, utilizar easy panel o utilizar culify. Voy a hacer directo. Coolify es la mejor para el caso. Muy fácil de usar, muy amigable, es lo que vamos a ver tutorial. Yo se los recomiendo. Docker directo te da control total, pero tienes que configurar todo manualmente, es decir, el reverse proxy, los certificados SSL, los updates. Hay demasiada fricción si tienes múltiples proyectos y si no tienes tanta experiencia en servidores. Y si panel es más simple, tiene una interfaz muy intuitiva, pero también tiene limitaciones importantes para stacks complejos de Pocket Base o N8N funcionan bien ahí. Suabis tiene más problemas reportados. Sin embargo, Culify es open source, gestiona múltiples servidores desde un solo panel. El SSL es automático vía traffic y el template de Supase es el más completo y mantenido de los tres que mencionamos, por eso es el que yo uso. Así que antes de arrancar checa aquí tengas lo siguiente. Un BPS con mínimo 4 GB de RAM. Yo estoy usando el KBM2 de Hostinger, que te da eh dos núcleos de CPU, 8 GB de RAM y, si no me equivoco 100 GB de almacenamiento y es más que suficiente para este proyecto y a la par tener N8 instalado en ese mismo BPS. Obviamente necesitas tener Culify ya instalado en ese BPS. Si no lo tienes, te dejo un link aquí abajo con la guía oficial. Es bastante tener un dominio, un subdominio que puedas apuntar al BPS. En este caso yo voy a utilizar midominio.com. Vamos a ver si en ese caso era su país.carlosdomínguez.com.mx. De esa manera vamos a apuntar hacia el panel de administración de Supas, que va a ser tal cual el que vieras si ahorita te fueras a Supis Cloud y compraras ahí o crearas una cuenta. Necesitamos obviamente también acceso SSH al servidor. Es muy importante para hacer un par de configuraciones tweaks y una cuenta de email donde vamos a enviar los correos. Puedes utilizar tu cuenta de Gmail personal o inclusive una plataforma gratuita que escala también bastante bien, que es recent, que es de las más populares. ¿Listo? Así que lo primero que vamos a hacer es entrar al servidor por SSH y asegurarnos de que esté listo. Así que vamos a abrir la terminal. Ya aquí tengo mi terminal corriendo en la parte de atrás. Como ven, está vacía. Todavía no he ejecutado nada, así que vamos a entrar a nuestro servidor SSH espacio tu usuario, que este caso yo dejé el usuario root@ y la IP de tu servidor. La IP de tu servidor lo puedes ver fácilmente en tu panel de administración donde hayas comprado el servidor. En mi caso, yo lo compré en Hostinger, así que vamos a Hostinger para que les enseñe dónde pueden ver eso. Abrimos una nueva pestaña, nos vamos a Hostinger, vámonos a nuestra cuenta y aquí en el caso yo ya estoy en mi cuenta, aquí están mis VPS y aquí tengo dos corriendo. Eh, en uno tengo OpenCl completamente aislado y en otro es donde tengo Cullify con otro servi esta IP que sé que es la donde tengo Cliify. Nos vamos a nuestro terminal, pego la IP y le doy enter. me va a pedir que ponga la contraseña. Así que en este caso voy a ir a copiar la contraseña. Tengan en cuenta que cuando entran por SSH y ponen la contraseña terminal, no van a ver la contraseña como tal. No se espanten. No es como que no está funcionando, no está escribiendo. Es porción de seguridad. Péguenla, le dan enter y si la contraseña está bien, evidentemente va a hacer la conex. Así que pegamos nuestra contraseña y le damos enter. Perfecto. Sabemos que estamos adentro porque nos está mostrando toda la información del servidor. Estamos usando Wuntu 24.04 y aquí vemos que cambió a root@ y nuestro servidor. Okay, ya que estamos aquí, ¿qué es lo que vamos a hacer? Primero vamos a actualizar el sistema. Es algo que yo siempre hago antes de instalar cualquier cosa, así evita conflictos de dependencias y vamos a ver que Pullifire obviamente ya instala Docker automáticamente, así que solamente verificamos que todo esté corriendo y todo esté bien. Así que lo primero sería actualizar nuestras dependencias. Para actualizar nuestras dependencias vamos a ejecutar esos dos siguientes comandos anidados. Vas a poner apt update person apt upgrade tengan en cuenta que estamos en un servidor con Ubuntu, como les enseñé, Ubuntu 24.04, así que esos son comandos de Linux y vamos a darle enter. Igual se los voy a dejar aquí abajo para que puedan copiar y pegar. ¿Qué es lo que estamos haciendo? Estamos actualizando nuestro servidor Ubuntu a las últimas versiones de todas las dependencias que sean necesarias. Vamos a darle unos minutos. un minuto a lo mejor a que termine y continuamos. Muy bien, ya terminó. Tomó aproximadamente 2 minutos. Sabemos que ya terminó porque ya puedo ya puedo escribir, ya me regresa esta parte, me dice que todo listo, no es necesario reiniciar. Así que como les comentaba, Cool ya instala Docker automáticamente. Simplemente vamos a comando para verificar que esté corriendo y que todo esté bien. Así que ponemos Docker GU versión y vemos que estamos en la 29.3.1 un con build y vamos a hacer un docker ps y aquí vemos todas nuestras instancias corriendo. Tenemos culify Sentinel, tenemos nuestros TAS runner, tenemos postgracias IQL DN8N, tal cual. Culify, quify, quify ready, quify real time. Muy bien. Ahora, ¿qué vamos a hacer? Esto es paso muy importante porque Supase inicia 12 contenedores al mismo tiempo y durante ese arranque inicial puede necesitar más RAM de la que esté disponible. Así que eh lo que vamos a hacer es un swap, que es como una memoria de emergencia en el disco. Es más lenta que que la RAM, pero salva el proceso. ¿Por qué? Porque cuando arranca base no queremos que nos consuma toda la RAM porque nos va a tirar los otros servicios o nos va a tirar peor, nos puede tirar el servidor. Es muy importante que no te paso aunque tengas 8 GB de RAM o más, ya que cuando arranca Supase es bastante intensivo en memoria y el swap justamente te evita estos crashes inesperados. ¿Qué es lo que vamos a hacer para crear swap? Vamos a ejecutar los siguientes comandos. Regresamos aquí, digamos en la terminal y vamos a escribir palate. Igual todos estos comandos se los voy a dejar aquí abajo. - L 2G diagonal 2G. ¿Por qué? Porque le estamos dando 2 GB. Filocate crea un archivo de 2 GB. Okay. Entonces es importante que hagamos esto y swap file es como le estamos llamando o así se va a llamar. Así que vamos a darle enter. No hay ninguna confirmación, pero no hay ningún error. Ya lo creo. Ahora recuerden que estamos en Ubuntu ch mod. Le vamos a dar permisos a ese archivo, permiso 600, al archivo que se llama swap file y le damos enter. Siguiente comando, vamos a hacer swap on, swap file y le damos enter. Dice reach trap header fail, si no tengo algún typo. Okay, ya vi que me salté un comando. Entonces, antes de eso vamos a hacer un MK swap. Importante que no se les vaya ninguna letra. En este caso, app, file, enter y con las flechas hacia arriba navegamos y repetimos el comando anterior. Listo. Y por último el comando lo voy a copiar porque es un poquito más largo y lo vamos a escribir. Es un eco comilla simple. Sap file non swap swerramos comillas simples y a fs t. No crean que yo me hice todos estos comandos de memoria y nada, simplemente eh le dije a Cloud Code, "Ey, quiero instalar eh mi servidor, tengo Clify, ¿cómo le hago?" Le dio la guía paso a paso. Les voy a dejar la guía también en la documentación, más aparte todos los comandos que voy ejecutando. ¿Listo? Entonces vamos a darle enter. Muy bien. Ahora, ya que tenemos esto, antes de tocar Cliify, el dominio que utilicemos, este caso supabase.carlosinguez.com.mx MX tiene que apuntar al servidor. Evidentemente Pulify utiliza les encrip de traffic para generar certificado SSL automáticamente, pero para eso necesita resolver el dominio. Okay. Si el dominio no apunta al servidor cuando haces el deploy, entonces el el SSL, perdón, el certificado falla, tienes que volver a deployar. Entonces, nos vamos a ir a nuestro panel de DNS. Vamos a crear un registro de tipo A con el nombre del subdominio que queramos y la IP pública de nuestro VPS, que es la que copiamos de Hostinger para crear eh para entrar a nuestro servidor vía SSH y con un TTL en 300 o automático. En mi caso, yo no tengo mi dominio en Hostinger, lo tengo en Hostgator. Así que vámonos a abrir el panel de Hostgator. Vamos a entrar a nuestro panel de administración. Listo. Vámonos a dominios. Vamos a buscar el dominio que queremos. Le damos administrar. Obviamente esto va a variar dependiendo el proveedor de dominios que tengas, pero una vez que ya estemos en la consola de administración del DNS prácticamente el mismo paso. Vamos a darle en añadir registro estilo A. Dijimos que va a ser su TTL. Dijimos que 300 y la IPv B4 es la IP de nuestro servidor que vamos a usar esta 187.1.80.218 y vamos a darle añadir. Listo, ya está añadido. Okay. ¿Cómo vamos a verificar que el DNS ya propagó? Podemos ejecutar un NS lookup a nuestro dominio y ya responde con la IP del BPS, ya propagó. Si no podemos esperar unos minutitos. Va a depender mucho de dóe tengas tu dominio, por lo general es bastante rápido. Muy bien. ¿Cómo hacemos el en ese lookup? Nos regresamos a nuestra terminal. Puede ser desde la terminal que estamos acá o puede ser desde tu terminal de la del estando directamente en la Mac, no importa. Vamos a darle ns lookup espacio y el dominio completo con el subdominio supaves.carlosdominguez.com.mx. Le damos enter y vemos que ya no está regresando nuestra IP, así que sabemos que ya hizo la propagación. Mi recomendación, si no te sale esto, espérate un poquito, no pasa al siguiente paso hasta que ya te muestre tu IP correcta. Toma el que les digo entre 1 a 30 minutos, dependiendo más o menos de con quién tengan este servicio de su dominio, pero es importante para que no les vaya a fallar, ¿verdad? Entonces, vámonos a nuestro Cullify. Ahora sí que abrimos Collify en nuestro navegador y lo primero que quiero verificar es que el proxy de traffic esté activo. Como les comentaba, traffic es el reverse proxy que Culify utiliza para manejar el tráfico y generar el certificado SSL automáticamente. Cuando alguien entra a nuestro dominio, trafic recibe la petición y la redirige al contenedor correcto. ¿Cómo lo verificamos? Y del lado izquierdo voy a ir a la parte X servers, local host y aquí donde dice proxy, ven que dice proxy running y está en verde, quiere decir que está activo. Si no, le tenemos que dar en start proxy. Muy bien, ahora sí que ya verificamos eso, nos regresamos a nuestro dashboard. Vamos a crear un nuevo proyecto. En este caso le vamos a llamar sub production. No quiero una descripción. Le doy continuar. Voy a seleccionar aquí uno nuevo en producción y vamos a buscar Supase. En el buscador ponemos superabase y seleccionamos esta opción. Ya que nos puso en la parte de configuración del service tag, vamos a configurarlo. Okay, vamos a configurar el dominio. Entonces aquí lo que tenemos que hacer, como ven, tenemos todos sus servicios. Con Studio Analytics Vector rest out real time def supervis mini minion create pocket sup storage todos estos servicios todos están en rojo porque no tenemos que hacer deploy. Antes de hacer deploy es importante que configuremos el dominio que por el que fuimos a configurar a hostgator. Tenemos que cambiarlo aquí. Vamos a darle en settings. Vamos a darle aquí donde dice domains. Vamos a borrar todo esto y vamos a poner puncarlos dominguez.com.mx mx y vamos a asegurarnos de que esté bien escrito. Muy bien. No tienes que poner https diagonal diagonal dos puntos, nada de eso. Quify se encarga de agregarlo. Ya que pusimos esto, podemos un human readable name. Vamos a vamos a dejarlo así y vamos a darle say. Nos va a dar una advertencia. Estamos estamos seguro porque estamos quitando el puerto. Vamos a decirle que sí, que lo quite de todas maneras. Ya que le dimos save save, perdón. Vamos a darle deploy. Okay. Y ya que le dimos deploy, va a empezar a cargar, va a empezar a levantar todos los servicios. Esto, honestamente puede durar entre 5, 15, 20 minutos. ¿Por qué? Porque que está haciendo es que está descargando todas las imágenes por primera vez, que obviamente está preconfigurado dentro de Coolify, pero las imágenes están en su servidor, no está en nuestro servidor, sabe lo que tiene que hacer, sabe todos los servicios que necesitamos, pero recuerda que son 12 contenedores distintos como hablábamos, por eso es importante el swap que configuramos anteriormente. Así que el punto, por eso tarda 5, 15, 20 minutos dependiendo, porque tiene que traerse todo del servidor y instalar las imágenes, descargar las imágenes de los 12 contenedores. Así que mientras esperamos les explico qué es cada uno de los servicios principales, un poquito como para que entiendan. Entonces, Supavi Conk Gateway, básicamente es el portero que recibe todas las peticiones y las dirige al servicio correcto. Go through es el servicio de autenticación, el storage API maneja los archivos y el servicio más importante es el de Suabase DB, que es realmente es la base de datos, que es el Postgress SQL eh real. Y aquí algo muy importante que quiero aclarar porque mucha gente asume que self hostes significa solo terminal, no es así. Cuando entras a tu dominio de supace, como les comentaba, supase.carlosomínguez.com.mx, mx. En mi caso tienes exactamente o vamos a ver exactamente el mismo dashboard visual que en supace.com, Supabase Cloud como les mencionaba y Supace Studio es uno de esos 12 contenedores que se desplegaron, que es justamente ese dashboard visual. Así que no perdemos absolutamente nada a nivel interfaz o funcionalidades. Si nos fuamos directamente a sup.com y contrataramos el servicio. Tenemos el table editor para ver y poder también editar datos visualmente, el SQL editor para poder correr queries, queries SQL directamente. Tenemos el autentication para configurar proveedores. Si yo quiero que mis usuarios o si yo soy el único usuario, pero yo quiero iniciar sesión con email, iniciar sesión con Google, con GitHook, Apple, usar Magic Links, también tenemos los templates de de correo para confirmar cuentas, cambiar contraseña, todo eso. Tenemos el storage con todos los buckets y las políticas. Tenemos las edge function, que también son muy importantes para poder crear y hacer deploy de funciones serverless. Y también tenemos logs en tiempo real de todos los servicios. Prácticamente todo lo que tenemos en suavis.com lo vamos a tener en el self hosted. El tradeof como les mencioné es que tú eres los responsable de actualizarlo, todo lo responsable de mantenerlo y todo lo responsable si se cae de averiguar qué pasó y volver a levantar el servicio. Así que es literalmente la misma interfaz corriendo en tu servidor para un uso cotidiano, todo lo que tengas que hacer en el día a día, en tus proyectos donde requieras tu pavés. La única diferencia real, como les comentaba, es que a nivel de infraestructura tú te haces cargo de todo. Muy bien, vemos que ya terminó porque ya no está cargando y todos dicen started, started, started. Así que vamos a cerrar esto y vamos a verificar. Vámonos de vuelta aquí a back y vamos a verificar. Vemos que todos los contenedores están en verde. Healthy, healthy, healthy, healthy rest. Okay. Minion create bucket. Vemos que eso está en rojo. Falló por alguna razón. Verde, verde, verde, verde, verde. Okay. Solo hay uno que no está levantado, pero vamos a ver que aquí dice running onhealthy. Y ya dice running healthy. Okay. Mientras aquí nos diga running healthy, estamos bien. Entonces, ¿qué es lo que necesitamos aquí? nos tenemos que ir a environment variables o variables de entorno y vamos a sacar dos claves que van a ser muy importantes. La primera va a ser la es la clave pública y es la que va en el front end de nuestro sistema. Y la segunda que es la service rle key es la clave privada y nunca nunca va en el frontend. La service roll tiene acceso completo a tu base de datos, ignorando todas las reglas de seguridad. Por lo mismo, por favor, nunca la expongas en el código de lado del cliente o repositorios públicos. Siempre utiliza archivos para tener tus variables a nivel local. Ahora, el paso es el que la mayoría de los tutoriales omite y es un riesgo de seguridad. El connection puller de Supabase tiene por defecto un tenant ID llamado def tenant guion. Es completamente predecible porque como es lo que tiene por defecto, si alguien quiere maliciosamente hacerle algo a tu base de datos, por defecto es lo que va intentar, ¿verdad? Así que vamos a cambiar. Pero lo primero que vamos a hacer, vámonos a nuestro Environment Viables y vamos a buscar esas dos llaves que les comenté, la anon key rad key. Aquí vemos que dice service Superbase anon key. Vamos a copiarla. Evidentemente voy a pausar el video para que no se vea, pero para poder ver su llave únicamente le van a dar clic aquí como en el ojito, la copian, guarden en un lugar seguro, la pegan y vamos a repetir el mismo servicio con el servicio. Así que voy a copiar eso y ahorita regreso. Listo, tenemos las llaves copiadas y ya las tengo guardadas en un lugar seguro. Entonces vamos a ir al darle edit al compost file y voy a buscar el servicio de supace supervisor y voy a agregar la variable de entorno con un valor aleatorio. Para generar ese valor uso open SSL rent que ahorita les enseño. Vamos para allá. Muy bien, regresamos a general. Vamos a darle aquí donde dice edit file. Le damos click y aquí tenemos todo esto. Como pueden ver, no se liquea, no se ven aquí las claves porque es simplemente es es como que la variable que está llamando de donde yo les les enseñé. Así que vamos a hacer lo que les comentaba. Vamos a agregar una variable de entorno. Aquí dice environment. Vamos a agregar lo siguiente. Nos vamos a hasta abajo. Aquí veo que terminamos. Le damos enter, espacio comilla simple y esto va con mayúsculaser gu bajo tenant y gu bajo id. Vamos a decirle que esto es igual a y vamos a dejarlo así. Vámonos de regreso a nuestra terminal aquí o en la directamente estando en la Mac. Vamos a darle open. Open SSL ran tex de 16. Le voy a dar enter nada más para que vean que me genere un valor aleatorio. No va a ser con el que me voy a quedar. Lo voy a repetir para generar uno nuevo. Le pongo pausa y ahorita regreso. Listo, ya lo agregué, le di guardar y es todo lo que necesitamos. Tengan en cuenta que el proceso lo hacemos por seguridad y también es importante que deba hacerse antes del primer uso real, que que si ya tienes datos y lo cambias después, necesitarás hacer migraciones de base de datos. Así que hazlo ahora antes de que empieces a configurar y antes de que empiece a tocar nada más. Así que el dashboard de Superabase en teoría ya está configurado, ya debe estar levantado, debe estar listo. Las credenciales de acceso están en quulify, así que tenemos que cambiarlas inmediatamente después del primer login. Te preguntarás dónde veo mis credenciales de acceso o dónde está eso? Vamos a regresar a Supas. Vamos a darle, perdón, variables de entorno de estado para que cargue. Y aquí tengo el que dice dashboard password. Y por aquí debo tener otro dashboard username. Dash dashboard username. Aquí está dashboard y username. Okay, lo mismo. Voy a ponerle pausa, voy a copiarlas y regreso. Listo, ya que las copié, vamos a abrir una nueva pestaña. Vámonos a sup.carlosomínguez.com.mx y le damos enter. Yup. 404 not pound. Vamos a ver qué es lo que pasó y a lo mejor el scionamiento no está correcto. Muy bien, como pueden ver ya estamos en supace.carlos domigues.com.mx break default y ya tenemos aquí la interfaz de su Quiero aclarar algo para el para el video, para los que lo estén viendo, que normalmente en los videos todo sale perfecto y no te cuentan los errores. Como pudieron ver, a mí me salió error 404 y luego no server available. era por una parte que había faltado. Yo les comenté en un principio en el video que Supase te, perdón, Coolify te agregaba el https por efecto. Algunas veces funciona, algunas veces no. Entonces, ¿qué tuve que hacer? Regresar en mi domains, agregar https dos puntos doble diagonal y lo que hice fue redeploy y ya funcionó y ya me cargó el proyecto. Okay, entonces vamos a continuar. Algo eh importante, tenemos que configurar o tenemos que ver que tenemos en SMTP, ¿okay? Es el protocolo para envío de correos y sin eso no puede enviar emails, no puede hacer confirmaciones de registro, magic links, recuperación de contraseñas, nada. Este caso, nosotros vamos a usar recent, que tiene 3,000 emails gratis al mes y es el más confiable para eso. Si prefieres usar Gmail, activa verificación de dos pasos en tu cuenta de Google, creas una contraseña de aplicación y utilizas smtp.gmail.com con el puerto 587 con la contraseña que hayas creado de aplicación. ¿Okay? Entonces, en nuestro caso, como vamos a utilizar Resent, deja les enseño cómo se ve. Regresamos a Colify, estamos dentro de nuestro servicio de SUP. Nos vamos de nuevo a variables de entorno y vamos a buscar todo lo que sea lo relacionado al SMTP. Puedo hacer un control F para poder buscar. Y aquí, perfecto, aquí veo SMTP, admin email vacío, host vacío, port 587, user vacío, pass vacío, sender name vacío. Así que vamos a configurar mtp host. Vamos a poner SMTP. Lo voy a poner aquí para que lo puedan ver. SMTP. recent.com, que es la plataforma que vamos a utilizar. El puerto 587 está bien. El user vamos a usar recent tal cual así. El SMTP sender name. Vamos a ponerle por ahora Carlos Domínguez y esto lo podemos configurar después más adelante. Okay. Y vamos a la contraseña. Necesitamos nuestro API Key de recent. Entonces, vámonos a crear una cuenta de recent, si es que no la tienen. Yo tengo ya eh cuentas de recent que he estado utilizando, pero es gratuito. Y aquí donde dice API Keys ustedes van a generar su API key. Le voy a poner pausa para copiarla y regreso. Muy bien. Entonces, ya saqué mi API Key, ya la pegué y le di restart y se levantaron todos los servicios. Vamos a regresar acá a nuestro proyecto. Vamos a actualizar y vemos que está corriendo. Okay. Ahora, algo muy importante, vamos a configurar el firewall. El firewall protege al servidor de accesos no autorizados y la regla más importante, el puerto 5432 de Postgress SQL nunca debe estar abierto públicamente. Así que antes que nada vamos a cerrar todos los puertos. Vámonos a nuestra consola. Okay, vamos a hacer aquí un clear para que se vea más y vamos a ejecutar lo siguiente. UFW espacio allow 22/ TCP. Okay, ¿qué estamos haciendo aquí? Esto es el puerto 22. Es el puerto de SSH. Entonces, UFW allow espacio 80 TCP. Y vamos a hacer el siguiente 443. es HTTP HTTPS y el del dashboard de Colify que es el 8000. Luego UFW FW. Vamos a darle que yes. Okay, está todo listo. Es importante que primero ejecutes el alado 22, que es el de SSH, perdón, antes de ejecutar el de UF enable, porque si no te quedas sin acceso al servidor si no has configurado bien ese puerto, ¿verdad? Y por último, para terminar vamos a regresar acá a nuestro Supase. Como pueden ver es prácticamente la misma interface y utilizaron Supasloud supase.com. Vámonos de ese lado donde dice SQL Editor es proyecto y vamos a escribir lo siguiente. Darle create espacio extension espacio if not exista enter select. Esto es un query exversion from pg- extension where name con comillas simples vector un poco complejo, pero esto qué es lo que hace. Básicamente estamos habilitando PG vector. Okay, vamos a darle run y vamos a ver qué nos dice. Okay, exersion.08 08 y listo, ya tienes su pavis corriendo en tu propio servidor con https, con PG vector para IA y con Collify gestionando todo. Para resumir qué es lo que logramos, configuramos el servidor con un swap para evitar crashes. Apuntamos al DNS, desplegamos el stack completo, configuramos el SMTP también para poder mandar email de autenticación. Protegimos el servidor de Firewall, activamos el PG vector para búsqueda semántica con IA y todo que nos habremos tardado 45 minutos, 40 minutos, todo con el mismo dashboard visual que ya conoces en Supas Cloud y sin pagar los $25 por ese proyecto adicional. Así que espero que te haya sido útil la guía. Recuerda que aquí abajo te dejo el documento con el paso a paso y todos los comandos que fuimos ejecutando a lo largo de la guía.
