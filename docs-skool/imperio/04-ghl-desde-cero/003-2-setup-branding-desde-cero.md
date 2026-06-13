# 🧱 2. Setup & Branding desde Cero

> Ruta: GHL desde Cero › 🧱 2. Setup & Branding desde Cero

**🎬 Vídeo (14.3 min):** https://www.loom.com/share/cf5a279af21c43c692c8115580898234

---

**Curso: Go High Level Desde Cero · Sección 2 de 12**

> *La primera impresión cuenta — incluso antes de que te conozcan.*

En esta sección creamos la subcuenta de la clínica desde cero, le conectamos un dominio real y le damos identidad visual: logo, colores y todos los datos del negocio. Cuando terminemos, la clínica va a tener su propia casa dentro de Go High Level, lista para recibir todo lo que construiremos en las siguientes secciones.

## **📚 Qué vas a aprender**

- La diferencia entre **cuenta de agencia** y **subcuenta** (y por qué importa)
- Crear la subcuenta **"Clínica Dental Sonrisa Perfecta"** desde cero
- Comprar un dominio y conectarlo a GHL vía DNS
- Subir el logo y configurar branding (colores, moneda, idioma, zona horaria)

## **🛠️ Paso a paso**

### **1. Entender la estructura: agencia vs. subcuenta**

En GHL existen **dos niveles**:

- **Cuenta de agencia:** tu cuenta maestra, desde donde gestionas a todos tus clientes.
- **Subcuenta:** cada cliente vive aquí, con sus propios datos, llaves y configuración.

> Analogía: la agencia es un edificio, cada subcuenta es un departamento independiente. Un cliente nunca ve los datos de otro.

![CleanShot 2026-04-24 at 09.41.43.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/106802df2ed3436faff692cb595b9c36d14e7a450d424ce9ae123ceb92648635.png)

### **2. Crear la subcuenta**

Desde la agencia, ir a **Sub-Accounts → Create Sub-Account**.

![CleanShot 2026-04-24 at 09.42.59.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7b26c552e9e44da8a2725b065c10d6f33f93d2bd703645ab8da15b2bceef9492-md.png)

> Importante: aunque existe un *snapshot* predefinido para clínicas dentales, la recomendación es **empezar de cero**. Quitar lo que no te sirve toma más tiempo que crear desde limpio.

Llenar los datos básicos del negocio:

- Nombre del negocio: `Clínica Dental Sonrisa Perfecta`
- Ciudad, dirección, código postal
- Nicho: dental
- Correo del responsable
- Zona horaria: la de tu clínica

![CleanShot 2026-04-24 at 09.45.39.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/57848bdff3554d759f2d0dfbbb902b9bdea8d80dd5a64ffd9baa35ddb1efb635.png)

**Desactivar** la opción de "añadir datos de muestra" — queremos el sistema limpio.

### **3. Comprar y conectar el dominio**

Ir a un proveedor (en el video usamos **Hostinger**, pero sirve Namecheap, Cloudflare o el que ya uses).

1. Buscar el dominio — en el caso: `clinicasonrisaperfecta.site` (99 MXN el primer año).
2. Completar la compra.

![CleanShot 2026-04-24 at 09.52.34.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7a56dc0c586e4486b1ee57a2c7b23d5c343b4c41e3da40a5915367d444bb99b2.png)

Ya en GHL, dentro de la subcuenta:

- Ir a **Settings → Domains → Add Domain**
- Pegar el dominio y elegir **subdominio** tipo: `app.clinicasonrisaperfecta.site`
- GHL te muestra los registros DNS que tienes que crear

![CleanShot 2026-04-24 at 09.53.23.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/b4898a996cca4a028192f7010c32df13078f412801464e5ea016f4a41a03db55.png)

### **4. Configurar DNS en tu proveedor**

En Hostinger (o tu proveedor): **Advanced → DNS / Nameservers → Manage DNS Records**.

Agregar este CNAME:

```
Tipo:   CNAME
Nombre: app
Valor:  brand.ludicrous.cloud
TTL:    Automático

```

> ⚠️ El DNS puede tardar hasta 24 horas en propagarse. Normalmente son minutos. Si te marca error al verificar, no entres en pánico — refresca y prueba de nuevo.

![CleanShot 2026-04-24 at 09.53.59.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/00775d854d12485da0924c271e83b15a24726414033f4fabb2ad10832b682ddc.png)

Volver a GHL y darle **Verify Records**. Cuando aparezca en verde, ya tienes el dominio conectado.

### **5. Configuración del negocio y branding**

Dentro de la subcuenta, ir a **Settings → Business Profile**:

- **Nombre legal:** `Clínica Dental Sonrisa Perfecta S.A. de C.V.`
- **Correo del negocio:** `contacto@lc.clinicasonrisaperfecta.site` (lo configuraremos en la Sección 3)
- **Teléfono del negocio**
- **Moneda:** MXN (o la que corresponda)
- **Idioma:** Español
- **Tipo de empresa:** Incorporation / Corporation
- **Sector:** Sanidad

### **6. Crear y subir el logo**

Abrir Canva con dimensiones **350 × 180 px** (las que pide GHL):

1. Nuevo diseño → tamaño personalizado
2. Elemento: buscar "sonrisa" o un ícono dental
3. Texto: "Sonrisa Perfecta"
4. Ajustar tipografía y color
5. Exportar con **fondo transparente** (PNG)

En GHL, subir el logo en **Business Profile → Logo**.

> 💡 No te obsesiones con el logo en esta etapa. El objetivo es tener algo funcional en 10 minutos. Siempre puedes mejorarlo después.

---

## **📎 Recursos**

### **🎨 Paleta sugerida para Sonrisa Perfecta**

```
Primario:   #1E88E5  (azul dental)
Secundario: #FFFFFF  (blanco)
Acento:     #F5F5F5  (gris claro)
```

### **📐 Dimensiones del logo**

- **Ancho:** 350 px
- **Alto:** 180 px
- **Formato:** PNG con fondo transparente

### **🔗 Proveedores de dominio recomendados**

- **Hostinger** (el del video)
- **Namecheap**
- **Cloudflare**
- O el que ya uses para tu VPS/hosting

### **📋 Plantilla — Registro CNAME**

```
Tipo:   CNAME
Nombre: app
Valor:  brand.ludicrous.cloud
TTL:    Automático
```

---

## **✅ Checklist antes de avanzar a la Sección 3**

- [ ] Subcuenta creada con todos los datos del negocio
- [ ] Dominio comprado
- [ ] Subdominio (`app.tudominio.com`) con CNAME apuntando a GHL y verificado
- [ ] Logo de 350×180 subido
- [ ] Moneda, idioma y zona horaria configurados

---

## **➡️ Siguiente sección**

**Sección 3 — Canales de Comunicación:** conectamos email (con SPF/DKIM/DMARC), compramos un número para SMS y configuramos WhatsApp Business. Porque un sistema bonito no sirve si no puede comunicar con los pacientes.
