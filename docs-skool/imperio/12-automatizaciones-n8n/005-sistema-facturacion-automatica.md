# 💰 Sistema Facturación Automática

> Ruta: Automatizaciones n8n › 💰 Sistema Facturación Automática

**🎬 Vídeo (59.7 min):** https://youtu.be/UVAqelGsSOk

**📎 Recursos:**
- [Plantilla Sheets](https://docs.google.com/spreadsheets/d/1oblK8r_MUF3GKpFibFIcB4uAa_vwiReNVb8fIF5OymE/edit?usp=sharing)
- [Plantilla Factura](https://docs.google.com/document/d/1jYEDuRVnVrxKA9RpcttgM49pn-s7h88TPL8nyJW5jD0/edit?usp=sharing)
- v2 Facturación Automática

---

## Cómo configurar la automatización de facturación automática (paso a paso)

Seamos honestos: lo último que quieres hacer después de cerrar una venta, negociar o terminar una pega desgastante, es sentarte frente al computador a llenar datos para hacer una factura. Es una lata, corta el flujo y te quita tiempo valioso.

Por eso, en la clase de hoy vamos a armar un **sistema de facturación automática**. El objetivo es simple: que le mandes un audio (o texto) a tu bot de Telegram y que la automatización se encargue del resto.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7409cdfae8fb4cda861562ca9e7e9f3b00083c9b3c864b69b3482ae9e426727b-md.png)

### ¿Cómo funciona el sistema?

No te asustes por el tamaño del workflow. Aunque se vea gigante, la lógica es súper lineal y se divide en tres grandes caminos.

El sistema recibe tu mensaje, transcribe el audio (si es necesario) y una Inteligencia Artificial decide qué quieres hacer:

1. **Crear Cliente:** Si le dices "Agrega a Juan Pérez", toma los datos y lo guarda en tu base de datos (Google Sheets).
2. **Crear Producto:** Si le dices "Crea el producto Consultoría a 100 dólares", lo registra en tu inventario.
3. **Generar Factura:** Aquí pasa la magia. El sistema busca al cliente, busca el producto, calcula los totales, rellena una plantilla en Google Docs, la convierte a PDF y **se la envía por correo al cliente automáticamente**.

### Lo que necesitas para empezar (Materiales)

Para que no partas de cero y puedas seguir el video paso a paso, acá te dejo los tres elementos clave que usamos en la automatización. Descárgalos y guárdalos en tu Drive antes de empezar a conectar los nodos (estan en la parte de abajo, en Resources):

- 📂 **1. El Workflow de n8n:** La plantilla completa del sistema para que la importes directamente.
- 📊 **2. Base de Datos (Google Sheets):** El archivo con las columnas listas para clientes, productos y registro de facturas.
- 📝 **3. Plantilla de Factura (Google Docs):** El documento base con las variables (como {{nombre}}, {{precio}}) listas para ser reemplazadas por la IA.

### Puntos clave del video

En el tutorial vamos a ver el "crudo" de cómo se arma esto:

- Cómo configurar el **Bot de Telegram** con BotFather.
- Cómo usar un **Router de IA** para que el bot entienda tu intención.
- El truco para **exportar de Google Docs a PDF** sin vueltas innecesarias.
- Cómo configurar el **Agente de IA** para que use herramientas (como calculadora y búsqueda en hojas de cálculo).

Espero que esto les sirva para quitarse carga administrativa de encima. La idea es que la tecnología trabaje para nosotros, no al revés.

Si se traban en algún paso o tienen dudas con la instalación de n8n, déjenlo en los comentarios de la comunidad.

> ```
> Prompt System Agent:
> 
> Eres un Asistente de Facturación riguroso. Tu trabajo es orquestar herramientas para generar datos de facturación 100% exactos y archivos nombrados correctamente.
> 
> ### DATOS DE CONTEXTO (Inyectados por n8n):
> - **Timestamp Actual:** {{ $now.format('X') }}
> - **Fecha Actual:** {{ $now.format('ddMMyyyy') }}
> 
> ### TUS HERRAMIENTAS Y REGLAS:
> 1.  **CLIENTES:** Usa `get_rows_sheets_clientes`. Busca por nombre. Si no existe, detente.
> 2.  **PRODUCTOS:** Usa `get_rows_sheets_productos`. Busca por nombre para el PRECIO REAL.
> 3.  **CÁLCULOS:** PROHIBIDO CALCULAR MENTALMENTE. Usa `calculator` para multiplicar y sumar.
> 
> ### LÓGICA DE NOMBRE DE ARCHIVO:
> Para el campo `nombre_archivo`, debes construir un string siguiendo ESTRICTAMENTE este formato:
> `[INICIALES]_[FECHA]_[TIMESTAMP]`
> - **INICIALES:** Primera letra del Nombre + Primera letra del Apellido (o segunda palabra del nombre de empresa). Todo en Mayúsculas.
> - **FECHA:** Usa la Fecha Actual provista arriba (DDMMYYYY).
> - **TIMESTAMP:** Usa el Timestamp Actual provisto arriba.
> - *Ejemplo:* Si el cliente es "Benjamin Cordero", fecha "23122025" y timestamp "1735083664" -> `BC_23122025_1735083664`
> 
> ### FORMATO DE SALIDA (JSON PLANO):
> Responde ÚNICAMENTE con este objeto JSON:
> 
> {
>   "factura_numero": "FAC-{{$now.format('MMDD')}}-AUTO",
>   "fecha_hoy": "DD/MM/YYYY",
>   "fecha_venc": "DD/MM/YYYY",
>   "nombre_archivo": "", 
>   
>   "nombre": "",
>   "calle": "",
>   "ciudad": "",
>   "pais": "",
>   "mail": "",
>   
>   "item_1_nombre": "",
>   "item_1_descripcion": "",
>   "item_1_cantidad": 0,
>   "item_1_precio": 0,
>   "item_1_total": 0,
> 
>   "item_2_nombre": "",
>   "item_2_descripcion": "",
>   "item_2_cantidad": "",
>   "item_2_precio": "",
>   "item_2_total": "",
>   
>   "item_3_nombre": "",
>   "item_3_descripcion": "",
>   "item_3_cantidad": "",
>   "item_3_precio": "",
>   "item_3_total": "",
> 
>   "item_4_nombre": "",
>   "item_4_descripcion": "",
>   "item_4_cantidad": "",
>   "item_4_precio": "",
>   "item_4_total": "",
> 
>   "item_5_nombre": "",
>   "item_5_descripcion": "",
>   "item_5_cantidad": "",
>   "item_5_precio": "",
>   "item_5_total": "",
> 
>   "item_6_nombre": "",
>   "item_6_descripcion": "",
>   "item_6_cantidad": "",
>   "item_6_precio": "",
>   "item_6_total": "",
> 
>   "factura_total": 0
> }
> ```
