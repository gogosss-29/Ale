# 🎯 6. Funnel: Landing Page + Calendario

> Ruta: GHL desde Cero › 🎯 6. Funnel: Landing Page + Calendario

**🎬 Vídeo (30.4 min):** https://www.loom.com/share/e4dc7d4bb40a4764a73f3d30553d8cdf

---

**Curso: Go High Level Desde Cero · Sección 6 de 12**

> *Cada minuto que un paciente gasta intentando agendar es un paciente que quizás no regresa.*

Tenemos CRM y pipeline — ahora vamos a **llenarlos de pacientes**. Para eso construimos un **funnel**: una página diseñada específicamente para convertir visitantes en citas agendadas, con el calendario integrado. Este video es un poco más largo que los otros porque te voy a enseñar las **4 maneras distintas** de crear landings en GHL, con recomendaciones de cuándo usar cada una.

## **📚 Qué vas a aprender**

- La diferencia entre **website** y **funnel** (y por qué importa)
- Las **4 formas** de crear landing pages en GHL
- Crear un funnel con 3 pasos: Landing → Appointment → Thank You
- Conectar un subdominio específico para el funnel
- Integrar el calendario de citas en la landing
- Probar el flujo completo como si fueras el paciente

## **🛠️ Paso a paso**

### **1. Website vs. Funnel — La diferencia clave**

WebsiteFunnelInformativo ("quiénes somos, qué hacemos")Orientado a **una sola acción** (agendar)Varias páginas navegablesPocas páginas, secuencialesVisitante paseaVisitante se **convierte**

**Ejemplo del "antes" del curso:** esa página HTML de los 2000s que mostramos en la Sección 1 es un website arcaico. No tiene formulario, no agenda, no convierte.

![CleanShot 2026-04-24 at 13.49.21.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2b8f009adaea4075b3d6607545c8aafacf9396fbcd7647a7a50949081e8a16da.png)

### **2. Estructura típica de un funnel (3 páginas)**

```
Landing Page → Appointment (calendario) → Thank You Page

```

- **Landing:** atrae la atención, muestra el valor, invita a agendar
- **Appointment:** calendario integrado para reservar fecha/hora
- **Thank You:** confirmación + promoción extra / upsell

GHL crea esta estructura automáticamente cuando partes de plantilla.

### **3. Las 4 formas de crear una landing**

Ir a **Sites → Funnels → + New Funnel**.

#### **Forma 1: Plantilla predefinida (la más rápida)**

- Darle **Continue** → se abre el buscador de plantillas
- Buscar por industria: `dental`, `dental appointments`, `medical`, etc.
- Elegir la más parecida a lo que necesitas

GHL carga la plantilla con Hero, servicios, testimonios, equipo, mapa, footer. **Todas las plantillas son mobile responsive** — puedes previsualizar en tablet y celular arriba a la derecha.

✅ **Cuándo usarla:** cuando necesitas algo funcional rápido y no quieres partir de cero.

#### **Forma 2: Desde cero (control total)**

- **+ New Funnel → From Scratch**
- Te da un canvas en blanco. Tú creas cada sección, columna, elemento.

Elementos disponibles: menú, botones, formularios, sliders, imágenes, videos, testimonios, código custom (HTML/JS/CSS), mapas, SVGs, reviews, pricing tables, countdowns, etc.

✅ **Cuándo usarla:** cuando tienes un diseño específico en mente y tiempo para construirlo.

#### **Forma 3: AI Funnel (beta)**

- **+ New Funnel → Funnel AI**
- Te pregunta: nombre del negocio, industria, objetivo (leads / appointments), tono
- 5 generaciones gratis, después ~$1.40 USD por generación

Limitación: a veces lo genera en inglés, testimonios son falsos (hay que cambiarlos). Como punto de partida funciona, no para publicar directo.

✅ **Cuándo usarla:** para arrancar rápido y después editar.

#### **Forma 4: AI Studio (beta) — la más potente**

- **Sites → AI Studio**
- Le describes en lenguaje natural qué quieres y él construye todo el funnel, no solo la landing

**Prompt ejemplo usado en el video:**

> 📋 Prompt — AI Studio
> 
> "Crear una página de aterrizaje (landing page) para mi clínica dental que se llama Clínica Sonrisa Perfecta. La idea es que la gente que venga de Facebook e Instagram aterrice aquí, vea la promoción del mes (limpieza dental por $499 pesos) y haya un calendario para agendar en nuestra sucursal. Tono profesional. Agrega una sección de reviews / social proof y al final un espacio para contactar por WhatsApp."

También puedes **adjuntar tu logo** para que lo use y saque la paleta de colores automáticamente.

Después de ~3 minutos genera una landing mucho mejor que Funnel AI, con el logo integrado y los colores correctos.

✅ **Cuándo usarla:** es la forma más rápida y potente para arrancar con algo profesional.

⚠️ **Limitaciones de AI Studio:**

- No lo ves en la lista de tus embudos (tiene su propia sección)
- No puedes editarlo con el editor drag-and-drop tradicional — solo con la IA

### **4. Conectar el subdominio del funnel**

En el editor: **Settings → Domain → Connect Domain**.

⚠️ **Importante:** no uses tu dominio raíz (`clinicasonrisaperfecta.site`) para el funnel — déjalo para el website principal. Usa un subdominio:

```
landing.clinicasonrisaperfecta.site
```

GHL te da el CNAME a agregar en Hostinger:

```
Tipo:   CNAME
Nombre: landing
Valor:  byte.ludicrous.cloud
TTL:    Automático
```

> ⚠️ **Ojo:** el valor cambia según el tipo de recurso. Para **sitios/funnels** es `byte.ludicrous.cloud`, para **email** es otro, para **sub-cuenta** es `brand.ludicrous.cloud`. Revisa bien el que te da GHL en cada caso.

### **5. Entender el editor de GHL**

Estructura jerárquica del editor:

```
Sección (row morado)
 └─ Column Row (azul)
     └─ Column (morado)
         └─ Elementos (headline, image, button...)
```

Herramientas útiles en el menú superior:

- **Cookies consent** — popup de cookies
- **Custom code** — meter HTML/JS/CSS
- **SEO & AI Search Optimization** — metadata, keywords, schema markup (importante para que los LLMs indexen tu página)
- **Pop-up settings** — ventanas emergentes
- **Background** — color o imagen de fondo global
- **Tipografía** — fuentes globales
- **Tracking code** — pixel de Facebook, Google Analytics, etc.

### **6. Crear el calendario**

Ir a **Calendars → + Create Calendar → Personal Booking**.

Configuración:

- **Nombre:** `Limpieza Dental`
- **Duración:** 30 min
- **Disponibilidad:** Lunes a Viernes, 8am-5pm
- **Aviso mínimo:** 4 horas
- **Intervalo a futuro:** 14 días

Guardar y volver al funnel. El AI Studio te preguntará "¿qué calendario conecto?" — seleccionas **Limpieza Dental**.

### **7. Crear el Thank You Page**

Desde el AI Studio, pedirle:

> 📋 Prompt — Thank You Page
> 
> "Crea el thank you page con un mensaje de agradecimiento por agendar y un cupón de 5% de descuento si presentan el código GRACIAS5 al momento de visitar la clínica."

### **8. Publicar**

- **Publish** en la landing → conectar dominio → generar metadata automáticamente (title, description, favicon, social OG image)
- **Publish** en el appointment → ya conecta el calendario
- **Publish** en el thank you

![CleanShot 2026-04-24 at 13.50.37.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/24cd6f09851d4d8c850280b087fa17bc8207510f62b741138625f9808f2fd0ca-md.png)

### **9. Test completo — simular paciente**

Abrir `landing.clinicasonrisaperfecta.site` en pestaña nueva:

1. Ver la landing → clic en "Agendar cita"
2. Se abre el calendario → elegir fecha y hora
3. Formulario pide: nombre, apellido, teléfono, email
4. **Submit** → aparece el Thank You Page con el cupón

Volver a GHL → **Contacts** → aparece el nuevo contacto con el appointment registrado.

## **📎 Recursos**

### **📋 Plantilla — Estructura del funnel**

```
Funnel: Limpieza Dental $499
├── Step 1 (Home/Landing)     → landing.clinicasonrisaperfecta.site
├── Step 2 (Appointment)       → /appointment
└── Step 3 (Thank You)         → /thank-you
```

### **📋 Plantilla — CNAME para funnel**

```
Tipo:   CNAME
Nombre: landing         # o el subdominio que elijas
Valor:  byte.ludicrous.cloud
TTL:    Automático
```

### **📋 Prompt para AI Studio (copy-paste)**

```
Crear una página de aterrizaje (landing page) para mi clínica dental
llamada [NOMBRE DE LA CLÍNICA]. La idea es que la gente que venga de
Facebook e Instagram aterrice aquí, vea la promoción del mes
([SERVICIO] por [PRECIO]) y haya un calendario para agendar en
[UBICACIÓN].

Tono: profesional y amigable.

Incluir:
- Hero con la promoción
- Sección "Por qué elegirnos"
- Social proof / reviews
- Calendario integrado
- Contacto por WhatsApp al final
- Mapa con ubicación
```

### **💡 Tips visuales**

- **Logo:** si queda pequeño, entra a `Image → Width/Height` y ajusta (ej: 275 × 75 px).
- **Sección ancho completo:** activa `Allow rows to take the entire width` en el row.
- **Menú sin borde:** ponle el mismo color de fondo de la sección.

## **⚠️ Troubleshooting común**

- **El dominio no aparece en el dropdown después de agregarlo:** guarda, refresca la página y vuelve a entrar.
- **AI Studio no aparece en tu lista de embudos:** es correcto — AI Studio vive aparte, no se lista con los funnels tradicionales.
- **El calendario no carga en la landing:** verifica que elegiste el calendario correcto y que está **publicado**.

## **✅ Checklist antes de avanzar a la Sección 7**

- [ ] Funnel creado (usa el método que prefieras — AI Studio recomendado)
- [ ] Subdominio del funnel conectado con CNAME verificado
- [ ] Calendario de citas creado y configurado
- [ ] Thank You Page con mensaje + cupón
- [ ] Test real: entraste como paciente, agendaste, apareciste en el CRM

## **➡️ Siguiente sección**

**Sección 7 — Checkout, Pagos & Thank You.** El funnel ya captura y agenda — ahora le agregamos la parte que todo dueño de negocio quiere ver: **cobrar**. Conectamos Stripe (y probamos Mercado Pago, que acaba de salir), creamos productos, configuramos el checkout y hacemos un test de pago completo.
