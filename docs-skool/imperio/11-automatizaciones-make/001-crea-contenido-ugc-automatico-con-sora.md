# 📽️ Crea Contenido UGC automático con Sora

> Ruta: Automatizaciones Make › 📽️ Crea Contenido UGC automático con Sora

**🎬 Vídeo (32.3 min):** https://youtu.be/PcXe9oej_z4

**📎 Recursos:**
- Plantilla UGC Automatizacion Make

---

Hoy les traigo una automatización que quedó **realmente brutal**.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cf06738f38c14e27a717112c3d3a4e4e15f459dcf4154e6594b25d88d6d584eb-md.png)

Con esta automatización puedes generar **videos UGC completos** (persona hablando del producto, tono natural, estilo “review honesta”) usando **solo una foto**.  
  
No necesitas actores, micrófonos, cámaras ni edición.

La interfaz está hecha en **Bolt** y la automatización corre completa en **Make** usando **Sora** como motor de video.

El flujo es:  
**subes imagen → Make procesa → Sora genera → recibes video listo para descargar**.  
Todo eso, 100% automático.

---

# 🔧 Cómo funciona:

## 1. Interfaz en Bolt

Creamos una app simple con el** prompt que te dejo al final**, donde ingresas:

- Nombre del producto
- Imagen
- Descripción
- Info adicional (tono, emoción, contexto)

Apenas presionas **“Generar video”**, Bolt envía todo a Make vía webhook.

---

## 2. Webhook en Make

Make recibe los cuatro parámetros y genera un `video_id` para trackear toda la generación.

Todo queda registrado en un Google Sheets.

---

## 3. Procesamiento de imagen

Make hace tres tareas clave:

- **Descargar la foto**
- **Redimensionarla a 720×1280** (formato UGC vertical)
- **Convertirla a PNG** para evitar errores en Sora

Esto deja la imagen lista para usar como input del modelo.

---

## 4. Generación de video con Sora

Make llama al modelo **Sora 2** (o Sora 2 Pro si quieres más fidelidad).

Le pasa:

- El texto del prompt
- La imagen procesada
- Las variables del usuario
- La duración del video

El modelo genera un video UGC corto, ideal para anuncios o pruebas de creativos.

---

## 5. Subida y conversión

Cuando Sora termina:

- Subimos el video al Drive
- Creamos un link compartible
- (Opcional) Convertimos el archivo con CloudConvert a MP4 limpio
- Guardamos todo en Sheets

---

## 6. Retorno a Bolt

Make le devuelve a Bolt:

- `video_id`
- `status: completed`
- `url` del video listo
- `download_url`
- `thumbnail_url`

Bolt refresca la interfaz y muestra el **video final listo para reproducir**.

---

# 🧩 Prompt de Bolt.new (para replicar la interfaz)

```
Crea una aplicación llamada "UGC Imperial" con un tema oscuro elegante (fondo gris casi negro #0F0F11, texto blanco, acentos violeta #7C4DFF).

Esta app permite generar videos UGC publicitarios conectándose al webhook de Make:

https://hook.us1.make.com/b9p5guwrnhlw4u5h9t8bw72sks7lkyxb

Diseño general minimalista, moderno y rápido.

Todos los campos deben tener bordes redondeados y fondo gris oscuro (#1C1C1E).

---

INTERFAZ EN ESPAÑOL - DISEÑO SIMPLIFICADO:

- Sin sidebar ni menús laterales

- Header simple con logo "UGC Imperial"

- Una sola pantalla: "Crear Video UGC"

---

FORMULARIO PRINCIPAL:

Título: "Crear Video UGC"

Subtítulo: "Describe el concepto de tu video y qué quieres crear..."

Campos (todos con placeholders en español):

1. Nombre del Producto → campo de texto

2. Imagen del Producto → campo de texto (URL input)

3. Descripción → campo textarea

4. Información Adicional → campo de texto (opcional)

Botón principal: "Generar Video" (color violeta #7C4DFF)

---

FUNCIONALIDAD DEL WEBHOOK:

Al presionar "Generar Video", enviar datos como JSON al webhook con esta estructura:

{

  "product_name": "...",

  "product_image": "...",

  "description": "...",

  "additional_information": "...",

  "status": "create"

}

IMPORTANTE: Incluir status: "create" en la primera llamada junto con toda la información.

---

PANTALLA DE CARGA:

Después de enviar el formulario:

- Mostrar pantalla de carga elegante con:

  * Spinner grande morado girando

  * Mensaje: "Generando Tu Video"

  * Animación de puntos rebotando

  * Botón rojo "Cancelar Generación" (por si acaso)

Sistema de detección:

1. Suscripción realtime a la base de datos para detectar cambios instantáneos

2. Polling cada 3 segundos como respaldo para verificar si el video está listo

---

WEBHOOK RESPONSE - ENDPOINT:

Crear un Edge Function en:

https://[tu-proyecto].supabase.co/functions/v1/video-webhook

Que reciba esta estructura cuando Make termine de procesar:

{

  "video_id": "uuid-del-video",

  "status": "completed",

  "video_url": "url-para-visualizar",

  "download_url": "url-para-descargar",

  "thumbnail_url": "url-del-thumbnail-opcional"

}

---

PANTALLA DE VIDEO COMPLETADO:

Diseño de dos columnas:

LADO IZQUIERDO:

- Reproductor de video integrado

  * Si es Google Drive: usar iframe con formato /preview

  * Si es link directo: usar <video> tag HTML5 con controles nativos

- Nombre del producto debajo

- Descripción del producto

LADO DERECHO:

- Ícono de confirmación verde grande

- Título: "¡Video Generado!"

- Sección destacada "Link de Descarga" con emoji 🎬

- Link del video en recuadro verde con borde, clickeable y copiable

- Botones de acción:

  * "Abrir Video" (verde - abre video_url en nueva pestaña)

  * "Descargar" (azul - descarga usando download_url)

  * "Generar Otro Video" (violeta - vuelve al formulario)

---

GALERÍA DE VIDEOS GENERADOS:

Debajo del formulario, mostrar cuadrícula de videos previos.

Cada tarjeta incluye:

- Miniatura del video (thumbnail_url)

- Nombre del producto

- Estado: "Completado" o "En Progreso"

- Fecha y hora de creación

- Botones: "Descargar", "Abrir", "Eliminar"

Diseño: tarjetas color #1C1C1E, texto blanco, acentos violetas.

---

BASE DE DATOS (Supabase/Bolt Database):

Tabla: generated_videos

Campos:

- id (uuid, primary key)

- product_name (text)

- product_image (text, url)

- description (text)

- additional_information (text, nullable)

- status (text: 'in_progress' | 'completed')

- video_url (text, nullable) → para visualizar

- download_url (text, nullable) → para descargar

- thumbnail_url (text, nullable)

- created_at (timestamp)

Configurar:

- Row Level Security policies para acceso público

- Realtime subscription habilitada

- Edge Function para recibir webhooks sin autenticación JWT

---

ESTILO VISUAL COMPLETO:

Colores:

- Fondo principal: #0F0F11

- Campos/tarjetas: #1C1C1E

- Bordes: #2E2E33

- Texto: #FFFFFF (blanco)

- Acentos principales: #7C4DFF (violeta)

- Acento secundario: verde para confirmaciones

- Acento terciario: azul para acciones secundarias

- Cancelar/eliminar: rojo

Efectos:

- Bordes redondeados en todos los elementos

- Padding amplio y diseño aireado

- Transiciones suaves (0.3s) en hover

- Sombras sutiles en tarjetas

- Animaciones de loading fluidas

---

FLUJO COMPLETO DE USUARIO:

1. Usuario completa formulario → Click "Generar Video"

2. Se crea registro en BD con status: 'in_progress'

3. Se envía data al webhook de Make con status: "create"

4. Aparece pantalla de carga con spinner y botón cancelar

5. Sistema verifica cada 3 segundos + realtime subscription

6. Cuando Make responde con status: "completed":

   - Se actualiza BD con video_url y download_url

   - Sistema detecta el cambio automáticamente

   - Muestra pantalla de video completado

7. Usuario ve el video, puede descargarlo o abrirlo

8. Click "Generar Otro Video" → vuelve al formulario

9. Videos anteriores aparecen en la galería abajo

---

TECNOLOGÍAS:

- React + TypeScript + Vite

- Supabase/Bolt Database (PostgreSQL + Realtime)

- Supabase Edge Functions (Deno)

- Tailwind CSS para estilos

- Detección automática de tipo de video (Drive vs directo)

---

IMPORTANTE - DETALLES TÉCNICOS:

1. El video_url es para visualización (puede ser iframe de Drive o video directo)

2. El download_url es específicamente para descargar (webContentLink de Google Drive)

3. Convertir automáticamente links de Google Drive:

   - De: https://drive.google.com/uc?id=XXX&export=download

   - A: https://drive.google.com/file/d/XXX/preview

4. Implementar doble sistema de detección:

   - Realtime subscription para cambios instantáneos

   - Polling cada 3 segundos como respaldo

5. Link de descarga debe mostrarse destacado en recuadro verde con emoji 🎬

6. Todos los textos de la interfaz deben estar en español

```

---

# 🎥 Prompt de Sora (UGC)

```
Rol:

Eres un creador de videos UGC especializado en producir anuncios cortos y auténticos que se sientan como reseñas reales de usuarios.

Tarea:

Una persona sentada en una habitación acogedora sostiene el producto (de la imagen).

Nombre del producto: {{2.product_name}}.

Descripción del producto: {{2.description}}

Habla directamente a la cámara con tono natural, como si realmente usara el producto.

Sonríe, muestra el producto cerca de la cámara y comenta lo útil y estiloso que es.

Luz natural, estilo de video grabado con el celular en mano, duración aproximada de 10 segundos, con vibra de anuncio UGC realista.

Idioma: Español (neutral, natural y cotidiano).

Info adicional: {{2.additional_information}}

```

---

# 🚀 ¿Por qué esta automatización es tan poderosa?

Porque te permite:

- Crear UGC sin grabar nada
- Generar decenas o cientos de variaciones en minutos
- Venderlo como servicio a clientes
- Montar una **mini SaaS** con un MVP real
- Ahorrar costos gigantes en producción
- Testear ángulos creativos de manera rápida y barata

Esto es velocidad, volumen y escalabilidad.  
  
Justo lo que piden hoy las campañas.  
  
#Recuerda que puedes descargar la plantilla aquí abajo.
