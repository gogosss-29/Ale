# 💳 7. Checkout, Pagos & Thank You Page

> Ruta: GHL desde Cero › 💳 7. Checkout, Pagos & Thank You Page

**🎬 Vídeo (20.4 min):** https://www.loom.com/share/c73f1a5837da4b08b9f0e8a3241ed8e5

---

**Curso: Go High Level Desde Cero · Sección 7 de 12**

> *Dinero en la cuenta antes de que lleguen al consultorio.*

El funnel ya captura y agenda — ahora la parte que todo dueño quiere ver: **cobrar**. Conectamos Stripe, probamos Mercado Pago (que acaba de salir para GHL), creamos nuestro primer producto, configuramos el checkout y hacemos un test completo de pago. Al final tienes un sistema que captura, agenda *y* cobra de forma automática.

## **📚 Qué vas a aprender**

- Conectar **Stripe** (test mode + live mode) a GHL
- Conectar **Mercado Pago** (integración nueva, muy útil para LATAM)
- Crear un **producto** con precio, descuento, imagen y categoría de impuestos
- Configurar la **checkout page** y el **thank you page** con variables dinámicas
- Test de pago completo con tarjetas de prueba

## **🛠️ Paso a paso**

### **1. Disclaimers importantes**

- **Mercado Pago** es una integración muy reciente — puede fallar intermitentemente. En el video intentamos primero con MP y al final usamos Stripe como respaldo. **Recomendación:** prueba ambos y usa el que te funcione más estable.
- **La mejor forma de integrar productos** es a través del funnel tradicional (desde plantilla o desde cero), no con AI Studio. AI Studio aún no conecta bien con el flujo de productos.

### **2. Conectar Stripe**

Ir a **Settings → Integrations → Payments → Stripe → Connect**.

- Inicias sesión con la cuenta de Stripe existente (debes tener una creada).
- Autorizar la conexión → listo.

![CleanShot 2026-04-27 at 09.52.52.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/244d33147afe4b89b6d4080ed69bc3be3186971c72994939862ee7821b1e3096.png)

Opcional:

- **Register Domain** → habilita **Apple Pay** y **Link** (autollenado de datos de pago).

### **3. Conectar Mercado Pago**

Ir a **Settings → Integrations → Payments → Mercado Pago → Connect**.

GHL abre una **documentación paso a paso** con capturas. Los pasos clave:

1. Crear cuenta en Mercado Pago (si no la tienes).
2. Tener una **cuenta de negocio** configurada.
3. Ir a MP → **Tus integraciones → Crear aplicación**.
4. Copiar las **credenciales de Test** y las de **Producción**.
5. Pegarlas en GHL (modo test primero).

### **4. Crear el primer producto**

Ir a **Payments → Products → + Create Product**.

- **Nombre:** `Limpieza Dental`
- **Descripción:** `Promoción del mes de abril — Limpieza dental completa`
- **Etiqueta:** `Promoción` (opcional)
- **Colección:** vacío (o crea una si agrupas productos por sucursal/promo)
- **Categoría de impuestos:** `Dental Hygiene Products` (o la que aplique en tu país)
- **Imagen:** ver siguiente paso

![CleanShot 2026-04-27 at 09.53.17.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8e47903e9be840b5bce893a098cd8c3f6190ed564ae3492080024a0a96e0f231.png)

#### **Generar imagen del producto con IA**

Abrir Gemini (o ChatGPT, Midjourney, etc.) y usar este prompt:

> 📋 Prompt — Imagen de producto
> 
> "Dame una imagen realista para usar en el producto de mi limpieza dental en Go High Level. Tiene que ser una foto clara de una limpieza dental en un consultorio clínico moderno, estilo foto profesional, fondo neutro."

> ⚠️ Gemini incluye su logo watermark — para producción, usa otra herramienta sin marca de agua o remueve el watermark con Photoshop/Canva.

Descargar la imagen y subirla al producto.

#### **Precio con descuento**

- **Precio actual:** `499` (MXN)
- **Compare-at price:** `999` — esto muestra el descuento visualmente (999 tachado, 499 en grande).

Guardar. **Felicidades, tienes tu primer producto creado.** Los productos se sincronizan automáticamente con Stripe y/o Mercado Pago según la conexión activa.

### **5. Agregar el producto al calendario (cobro con la cita)**

Ir al calendario `Limpieza Dental` → **Edit → Advanced Settings → Payments**.

- Activar **Accept Payments** ✅
- **Proveedor por defecto:** Stripe (en el video empezamos con MP pero dio error, cambiamos a Stripe)
- **Tipo:** Sell Products — buscar y agregar `Limpieza Dental $499`
- **Modo:** Test (mientras pruebas) → Live cuando esté todo ok

> 💡 **Truco importante:** los formularios del calendario NO aceptan el producto en el campo "Accept Amount" simple — el producto se agrega al **formulario del calendario**. Ver siguiente paso.

### **6. Crear formulario personalizado con producto**

Ir a **Sites → Forms → Builder → + Create New Form**.

- **Nombre:** `Limpieza Dental $499`
- Campos: nombre, apellido, teléfono (opcional por políticas de GHL), email
- Sección **Products** → Add Product → elegir `Limpieza Dental`

Guardar y volver al **Calendario → Advanced Settings → Forms** → elegir el formulario recién creado.

### **7. Thank You Page dinámico con variables**

Editar la Thank You Page del funnel y usar **variables de GHL**:

Panel de variables → buscar **Appointment**:

```
{{appointment.date}}          — fecha completa
{{appointment.start_time}}    — fecha + hora
{{appointment.start_time_only}} — solo la hora
{{contact.first_name}}
{{contact.email}}
```

> ⚠️ **Pegar sin formato** (`Cmd+Shift+V`) para que no se rompa el estilo.

Ejemplo del texto:

> 📋 Plantilla — Thank You Page
> 
> **Reserva confirmada, {{contact.first_name}} 🎉**
> 
> ✅ Pago exitoso.
> 
> 📅 Fecha: {{appointment.date}} 🕐 Hora: {{appointment.start_time_only}} 📍 Ubicación: [Dirección de la clínica]
> 
> Te esperamos. Si necesitas reagendar, puedes hacerlo aquí: [LINK AL CALENDARIO]
> 
> **Preséntate con el código **`GRACIAS5` para obtener un 5% de descuento adicional.

### **8. Test completo de pago**

Abrir el funnel como si fueras un paciente:

1. Landing → **Agendar**
2. Calendario → elegir fecha/hora
3. Formulario → llenar datos
4. Checkout aparece con el producto ($499) y el campo de tarjeta

#### **Tarjetas de prueba**

**Stripe (test mode):**

```
Tarjeta:      4242 4242 4242 4242
Fecha:        cualquier fecha futura (ej: 12/30)
CVV:          cualquier 3 dígitos
```

**Mercado Pago (test mode):**

```
Tarjeta:      5031 4332 1540 6351  (MasterCard test)
Fecha:        11/25
CVV:          123
Nombre:       APRO
```

Click en **Pay**. Si todo salió bien:

- Te redirige al Thank You Page
- El contacto aparece en el CRM con la cita + pago registrado

### **9. Verificar el pago en el CRM**

Ir a **Contacts → [nuevo contacto] → Payments**.

También en **Payments → Transactions** aparece la transacción.

### **10. Cuándo cobrar online vs. en persona**

Cobra online cuando...Cobra en persona cuando...Quieres **reducir no-shows** (el paciente que paga viene)Es un servicio largo/variable y el precio puede cambiarEl servicio tiene precio fijoTrabajas con seguros o financiamientoPromos con deadline (crea urgencia)Es el primer contacto y no quieres fricción

## **📎 Recursos**

### **📋 Variables de GHL para el Thank You**

```
{{contact.first_name}}
{{contact.last_name}}
{{contact.email}}
{{contact.phone}}
{{appointment.date}}
{{appointment.start_time}}
{{appointment.start_time_only}}
{{appointment.reschedule_link}}
{{company.name}}
{{company.address}}
```

### **💳 Tarjetas de prueba**

**Stripe:**

```
4242 4242 4242 4242 · cualquier fecha futura · cualquier CVV
```

**Mercado Pago:**

```
5031 4332 1540 6351 · 11/25 · 123 · Titular: APRO
```

### **💡 Dos formas de cobrar en GHL**

FormaCuándo usar**Producto en formulario del calendario**Servicios que requieren agendar cita**One-Step Order (producto en landing)**Productos físicos o servicios sin agendar

## **⚠️ Troubleshooting común**

- **Mercado Pago rechaza el pago:** el token de prueba puede expirar. Vuelve a generar las credenciales en MP o cambia a Stripe.
- **El producto no aparece en el checkout:** verifica que asignaste el formulario correcto al calendario (Advanced Settings → Forms).
- **La fecha no se muestra en el Thank You:** estás usando la variable incorrecta. Prueba `{{appointment.start_time}}` en vez de `{{opportunity.date}}`.

## **✅ Checklist antes de avanzar a la Sección 8**

- [ ] Stripe conectado (test mode funcionando)
- [ ] Mercado Pago conectado (opcional, pero útil para LATAM)
- [ ] Al menos 1 producto creado con precio, descuento e imagen
- [ ] Calendario con el producto asignado vía formulario
- [ ] Thank You Page con variables dinámicas
- [ ] Test de pago completo exitoso (apareció en CRM y en Payments → Transactions)

## **➡️ Siguiente sección**

**Sección 8 — Workflows: Confirmaciones & Recordatorios.** El funnel está completo: captura, agenda y cobra. Pero hasta aquí depende del paciente. En la siguiente sección arrancamos con **lo más potente de GHL: las automatizaciones**. Construimos los 2 primeros workflows — confirmación automática de cita y recordatorio 24h/2h antes — para eliminar horas manuales de trabajo por semana.
