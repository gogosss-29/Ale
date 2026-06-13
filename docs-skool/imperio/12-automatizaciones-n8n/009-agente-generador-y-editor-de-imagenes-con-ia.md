# 🤖 Agente Generador y Editor de Imágenes con IA

> Ruta: Automatizaciones n8n › 🤖 Agente Generador y Editor de Imágenes con IA

**🎬 Vídeo (38.9 min):** https://www.loom.com/share/4c72649db64e4f73988d67800e2b8968

**📎 Recursos:**
- Workflow Principal
- Sub-workflow generar imagenes
- Sub-workflow editar imagenes

---

### NanoBanana Pro + n8n + Telegram (End-to-End)

En este video te enseño cómo **montar un bot de Telegram** para generar y editar imágenes usando **NanoBanana Pro**, con **todo el flujo corriendo en n8n**.

Este setup es ideal para **probar agentes rápidamente** antes de llevarlos a WhatsApp, que no es más difícil, pero sí tiene **más pasos y fricción inicial** por el tema del número y la verificación.

La idea es simple:  
👉 Telegram para pruebas rápidas  
👉 n8n como orquestador  
👉 NanoBanana Pro como motor de generación y edición de imágenes  
👉 Un solo agente que **recuerda**, **interpreta** y **edita sobre la imagen anterior**

---

## 🎯 Qué vas a aprender en este módulo

- Cómo levantar un **bot de Telegram** en minutos
- Cómo crear un **agente generador y editor de imágenes**
- Cómo usar **memoria simple** para mantener consistencia visual
- Cómo separar el flujo en **orquestador + sub-workflows**
- Cómo usar **callback URLs** en lugar de waits fijos
- Cómo generar y editar imágenes **sin volver a subirlas**
- Cómo aprovechar **NanoBanana Pro vía **[**Kie.ai**](http://Kie.ai) para reducir costos

---

## 📸 Resultado final (antes de ver los flujos)

Primero te muestro el resultado.  
Luego entramos al detalle técnico.

Ejemplo del flujo real:

1. Le pido al bot: > “Genera una imagen de un perro surfeando una ola gigante de noche con galaxias en el cielo”
2. El bot genera la imagen.  
 ![photo_2025-12-23 12.15.01.jpeg](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/1c281b5aa09d4260b52ef7e7f67deacb021b38c1f45d480180473983b4d8754e.jpg)
3. Luego le digo: > “Usa la misma imagen, no cambies nada excepto el cielo. Quiero que ahora sea un día muy soleado”
4. El agente: - Recuerda la imagen anterior
- Mantiene **el mismo perro, la misma ola y la misma tabla**
- Cambia únicamente la iluminación y el cielo

![photo_2025-12-23 12.15.05.jpeg](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7fee478ab5b642be835aacb925690940a3501a221d2a4442b20d43a61ee3aa30.jpg)

📌 Esto solo es posible porque **guardamos el ID de la imagen en memoria** y lo reutilizamos en la edición.

## 🧠 Arquitectura general del sistema

El sistema está dividido en **tres flujos principales**:

1. **Workflow principal (orquestador)**  
 ![CleanShot 2025-12-23 at 12.15.58.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a6bdebc073a64c34ad28c5c456450d21a58f6f3035894f1e8f72244e15890397-md.png)
2. **Sub-workflow: Generar imagen**  
 ![CleanShot 2025-12-23 at 12.16.27.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/604f8f7d71544e9893b1770c26ec1b6ae1379993ad494e6bbb296950e35eca15-md.png)
3. **Sub-workflow: Editar / combinar imágenes**  
 ![CleanShot 2025-12-23 at 12.17.00.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/671c1b590c584e03bfb59bd858df65fe02d87051f9ed446b82ca08546fbfe7ac-md.png)

## 🧩 Workflow principal. Orquestador

Este es el corazón del sistema.

### Qué hace:

- Recibe mensajes desde Telegram
- Identifica el tipo de input: - Texto
- Voz
- Imagen
- Normaliza la información
- Llama al **agente de IA**
- Envía el resultado final a Telegram

### Componentes clave del orquestador

- **Telegram Trigger**
- **Switch clásico** para detectar: - Texto
- Audio
- Imagen
- **Transcripción de audio** (si llega voz)
- **Agente de IA**
- **Memoria simple** (uso interno)
- **Llamada a sub-workflows**

📌 Estamos usando **n8n v2.1.2**, que ya corrige problemas de compatibilidad entre agentes principales y sub-agentes.

> ⚠️ Si vienes de una versión anterior y tus sub-agentes no funcionan, no te va a funcionar por arte de magia.  
> Tienes que **crear el sub-agente nuevo y copiar las instrucciones**.

## 🧠 El Agente de IA

Este agente es el que decide:

- Si debe **generar** una imagen nueva
- Si debe **editar** una imagen existente
- Qué **aspect ratio** usar
- Qué **prompt refinado** enviar a NanoBanana

### Detalles importantes:

- Modelo: **OpenAI o4-mini con reasoning alto**
- Uso de **memoria simple**
- El agente **recibe feedback** del sub-workflow (algo que antes de n8n 2.0 no era posible)

```
## ROL

Eres el Agente Editor. Vas a recibir una instrucción del usuario, así como imágenes que deberás editar.

Interactúas por medio de Telegram, y cada imagen la recibes como un ID de imagen.

## HERRAMIENTAS

Dispones de 3 herramientas para cumplir tus labores de edición:

- 'generarImagen': Usa esta herramienta únicamente cuando debas generar imágenes nuevas a partir de un prompt. No la uses para editar imágenes proporcionadas por el usuario.
- 'editarImagenes': Usa esta herramienta cuando necesites editar o combinar imágenes existentes. Puede aceptar hasta 8 IDs de imágenes separados por coma.
- 'mejoradorPrompts': Usa esta herramienta SIEMPRE como PASO INTERMEDIO. Nunca es una acción final. Su output jamás debe devolverse directamente al usuario.

## DEFINICIÓN DE LA HERRAMIENTA `mejoradorPrompts`

Cuando utilices la herramienta DEBES aplicar las siguientes reglas sin excepción:

### Responsabilidad Principal 
Transformar una idea básica del usuario en un prompt completamente refinado, listo para producción y seguro para enviarse directamente en un HTTP POST. 

### Regla Absoluta de Preservación de Identidad 
Si el usuario proporciona una imagen de referencia, debes preservar al sujeto original EXACTAMENTE como aparece. Esto incluye, sin excepción: 
- Estructura y proporciones faciales 
- Ojos, nariz, boca y mandíbula 
- Tono y textura de piel 
- Tipo de cuerpo y postura 
- Apariencia de edad 
- Línea del cabello, peinado y color 
- Rasgos físicos distintivos

Está estrictamente prohibido modificar, embellecer, estilizar, exagerar, rejuvenecer, envejecer o alterar el rostro o características físicas del sujeto, a menos que el usuario lo autorice explícitamente. 

Si no existe autorización explícita, asume siempre: “Mantener al sujeto original exactamente tal como es”. 

### Restricciones Creativas 
- No introduzcas conceptos, elementos, personajes u objetos que no estén implícitos en la instrucción del usuario. 
- No reinterpretes ni reimagines al sujeto. 
- No cambies género, etnia, expresión facial ni identidad física. 
- No apliques estilos artísticos que distorsionen el realismo, salvo que el usuario lo solicite explícitamente. 

### Construcción del Prompt Refinado El prompt refinado debe: 
- Estar escrito en inglés profesional, claro y natural. 
- Usar oraciones completas, no listas de keywords. 
- Definir claramente: 
- Sujeto 
- Entorno 
- Composición y encuadre 
- Perspectiva de cámara 
- Iluminación 
- Estado de ánimo y atmósfera 
- Materiales y texturas 
- Estilo visual 
- Uso previsto (editorial, publicidad, social, UI, etc.) 

Si hay texto visible en la imagen, inclúyelo exactamente como debe aparecer, entre parentesis, nunca uses comillas. 

Si la estructura, simetría o layout es relevante, descríbelo con precisión. 

### Reglas de Output del Mejorador 
- No incluyas explicaciones, markdown ni comentarios. 
- No uses emojis. 
- No uses prompts tipo lista o etiquetas. 
- No menciones reglas internas ni políticas. 
- Actúa como Director Creativo, no como redactor técnico. 
- Escapa correctamente las comillas. - Nunca rompas el JSON.

### Formato Estricto de Salida del Mejorador
La herramienta `mejoradorPrompts` debe devolver ÚNICAMENTE:

{
  "refined_prompt": "..."
}


## FUNCIÓN GENERAL DEL AGENTE

Tu función es interpretar la intención del usuario respecto a generación o edición de imágenes usando el modelo Nano Banana 2 y ejecutar las herramientas necesarias hasta completar la acción solicitada.

## REGLAS OPERATIVAS (HARD RULES)

1. `mejoradorPrompts` NUNCA es una acción final.
   - Siempre debe ser seguido por `generarImagen` o `editarImagenes` cuando existan los datos mínimos.

2. Si el usuario quiere generar una imagen:
   - Llama a `mejoradorPrompts`.
   - INMEDIATAMENTE después llama a `generarImagen`.
   - Nunca respondas al usuario con texto.

3. Si el usuario quiere editar una o varias imágenes:
   - Solicita las imágenes una por una. 
   - Guarda los IDs de imagen. 
   - Una vez tengas todos los IDs: 
   - Pasa el prompt por mejoradorPrompts. 
   - Envía a editarImagenes: 
   - El prompt refinado. 
   - Los IDs de imagen separados por coma. 
   - El aspect ratio correcto (1:1, 16:9, 9:16). Si no es obvio, infiérelo o pregunta.

4. Si el usuario quiere editar una imagen generada previamente: 
   - Usa el último file ID generado. No se lo pidas al usuario, usa tu memoria para consultarlo. 
   - Pasa el nuevo prompt por mejoradorPrompts. 
   - Vuelve a llamar a editarImagenes.

4. Está estrictamente prohibido devolver al usuario:
   - El prompt refinado
   - El JSON de `mejoradorPrompts`
   - Cualquier texto descriptivo del proceso

5. La única salida válida del agente, cuando la intención es clara, es una llamada a herramienta.

6. Solo puedes responder con texto si:
   - Faltan IDs de imagen
   - Falta el prompt
   - La intención no es clara

7. Si respondes con texto, debe ser breve y SOLO para solicitar la información faltante.

8. Guarda siempre el ID de la última imagen editada o generada para futuras ediciones.
```

## ✍️ Mejorador de prompts

Antes de llamar a NanoBanana, siempre pasamos por un **mejorador de prompts**.

Este agente:

- Recibe el prompt básico del usuario
- Lo mejora siguiendo **lineamientos oficiales de Google** para NanoBanana
- Devuelve un JSON con un solo campo: ```
{
  "refined_prompt": "..."
} ```

📌 El agente **no devuelve texto al usuario**.  
📌 Su único trabajo es **mejorar el prompt**.

## 🎨 Sub-workflow: Generar imagen

Este flujo es sencillo y limpio.

### Inputs que recibe:

- Prompt refinado
- Chat ID
- Aspect ratio
- Caption (opcional)

### Pasos:

1. HTTP Request a **NanoBanana Pro** vía [**Kie.ai**](http://Kie.ai)
2. Enviamos: - Modelo
- Prompt
- Resolución
- Callback URL
3. Entramos en un **Wait**
4. NanoBanana llama de vuelta cuando termina
5. Descargamos la imagen
6. La enviamos por Telegram
7. Devolvemos el **ID de la imagen** al agente

⏳ Callback en lugar de waits fijos

Este punto es clave.

Antes:

- Esperabas 15, 30 o 60 segundos sin saber si ya terminó.

Ahora:

- Mandas tu **execution resume URL**
- NanoBanana procesa la imagen
- Cuando está lista, **te llama**
- El flujo continúa automáticamente

📌 Esto hace el sistema:

- Más rápido
- Más limpio
- Más profesional
- Más escalable

## 🧩 Sub-workflow: Editar / combinar imágenes

Este flujo permite:

- Editar una imagen existente
- Combinar hasta **8 imágenes**
- Mantener consistencia visual

### Qué hace:

1. Recibe IDs de imágenes separados por coma
2. Descarga cada imagen desde Telegram
3. Genera URLs públicas temporales
4. Las agrega en un array
5. Llama a NanoBanana con `image_input`
6. Espera callback
7. Envía la imagen final
8. Devuelve el nuevo ID al agente

## 🔗 Cómo obtener URLs públicas de imágenes de Telegram

Usamos este formato:

```
https://api.telegram.org/file/bot<TU_BOT_TOKEN>/<file_path>

```

📌 Son URLs temporales  
📌 Sirven perfecto como input para NanoBanana

---

## 💰 Costos reales con [Kie.ai](http://Kie.ai)

Esto es lo que más me gusta.

- 18 créditos por imagen 1K (~$0.09 USD)
- 24 créditos por imagen 4K
- 1000 créditos = $5 USD
- ~55 imágenes con $5

📌 Es **25–50% más barato** que usar la API oficial directamente.

![CleanShot 2025-12-23 at 12.19.08.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/00b0d7c7e954424085f1623d5d174dc36a9435f971bf4fef83e359b63a772e45-md.png)

## 🧪 Pruebas en vivo con Telegram

En el video también vemos:

- Cómo crear el bot con **BotFather**
- Cómo pegar el token en n8n
- Cómo publicar versiones del workflow
- Cómo ver ejecuciones en tiempo real
- Cómo detectar errores rápidamente

📌 n8n aquí le gana por goleada a Make en debugging.
