# 👑 [GUIA] Configura tu Agente de LinkedIn

> Ruta: Automatizaciones n8n › 👑 [GUIA] Configura tu Agente de LinkedIn

**🎬 Vídeo (17.0 min):** https://www.loom.com/share/219866bc26964cb689e61f60c64f56a2

**📎 Recursos:**
- Linkedin Agente Auténtico
- [Plantilla Sheets](https://docs.google.com/spreadsheets/d/1VLehRMvAzDgUiU2DipNCeYqVykxMbM6wUSuqFqJxG6U/edit?usp=sharing)

---

## Guía Técnica: Cómo instalar y configurar tu Agente de LinkedIn en n8n (Paso a Paso)

Si llegaste acá, es porque seguramente ya viste cómo funciona este Agente de IA para LinkedIn y los resultados que puede darte. Si aún no ves la "magia" o la lógica detrás de esta automatización, te recomiendo partir por el video principal donde te explico el concepto completo: 👉 [https://www.skool.com/imperio-digital/classroom/8e2ffdbc?md=9e04d92c52a44093a8df35d2cfcccfd4](https://www.skool.com/imperio-digital/classroom/8e2ffdbc?md=9e04d92c52a44093a8df35d2cfcccfd4)

Ahora sí, vamos a lo técnico. En este post vamos a ensuciarnos las manos. Te voy a guiar clic a clic para importar la plantilla, conectar las APIs y dejar a tu agente listo para entrevistarte mañana mismo.

Vamos directo al grano.

---

### Paso 1: Importar la Plantilla y la Base de Datos

Lo primero es tener la estructura lista. Vamos a necesitar dos cosas: el "cerebro" (n8n) y la "memoria" (Google Sheets).

1. **En n8n:** Descarga el archivo JSON de la plantilla (lo tienes en la descripción del video) e impórtalo en un nuevo workflow. Verás que aparecen tres etapas: Contexto, Preguntas Diarias y Generación de Contenido.  [https://docs.google.com/spreadsheets/d/1VLehRMvAzDgUiU2DipNCeYqVykxMbM6wUSuqFqJxG6U/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1VLehRMvAzDgUiU2DipNCeYqVykxMbM6wUSuqFqJxG6U/edit?usp=sharing)
2. **En Google Sheets:** Duplica la plantilla que te compartí. - Dale a "Archivo" > "Hacer una copia".
- Guárdala en tu Drive. Esta hoja es clave porque aquí se guardará tu información.

---

### Paso 2: Crear y Conectar el Bot de Telegram

Telegram será tu interfaz de usuario. Aquí es donde el agente te hablará.

1. Abre Telegram y busca a **@BotFather**.
2. Escribe el comando `/newbot`.
3. Ponle un nombre (ej: `Agente LinkedIn V3`) y un usuario (debe terminar en `bot`, ej: `BenjaLinkedin_bot`).
4. BotFather te dará un **Access Token**. Cópialo.
5. **En n8n:** Ve a las credenciales de Telegram y pega ese token.

**⚠️ Truco para el Chat ID:** Para que el bot sepa que eres tú, necesitas tu Chat ID.

- En el nodo de Telegram (Trigger), dale a "Listen for Event".
- Ve a tu nuevo bot en Telegram y escríbele "Hola".
- En n8n verás que llega la data. Busca el campo `chat.id` (es un número largo) y cópialo.
- Pega ese número en todos los nodos de Telegram donde te pida "Chat ID".

---

### Paso 3: Conectar Google Sheets

Esta parte es vital. Aunque importes la plantilla, n8n no sabe cuál es *tu* hoja de cálculo.

1. Abre cada nodo de Google Sheets en el workflow (son varios: guardar contexto, leer tópicos, guardar post).
2. Conecta tu cuenta de Google.
3. **Importante:** En el campo "Document", selecciona tu copia de la hoja que creamos en el Paso 1.
4. Asegúrate de mapear la hoja correcta (`Context`, `Questions` o `Content`) en cada nodo según corresponda.

> **Ojo:** Haz esto con calma en cada nodo. Si te saltas uno, la automatización fallará porque no encontrará dónde escribir.

---

### Paso 4: Conectar la Inteligencia (OpenRouter y Replicate)

Ahora démosle cerebro y ojos a esto.

**Para el Texto (OpenRouter):**

1. En los nodos de "AI Agent", conecta tu credencial de OpenRouter.
2. Elige el modelo que prefieras. Yo uso **GPT-5.2** (o GPT-4o) para la redacción final porque escribe mejor, y modelos más ligeros (como Flash o GPT-4 mini) para tareas simples como generar preguntas.

**Para las Imágenes (Replicate - Opcional):** Si quieres que genere fotos tuyas:

1. Ve a , crea tu cuenta y busca tu API Token.
2. Pégalo en el nodo `HTTP Request` de n8n (Authentication: Header Auth).
3. **El Prompt Visual:** En el cuerpo de la solicitud (Body), verás un enlace a una imagen. **Cámbialo por una foto tuya real** que tengas alojada en internet (puedes subirla a imgbb o similar y copiar el link directo). Esto sirve para que el modelo "Nano Banana" sepa cómo es tu cara y tu ropa.

---

### Paso 5: Prueba de Fuego

Ya está todo conectado. Hora de probarlo.

**1. Generar Contexto:** Ejecuta la primera parte del workflow manualmente. El bot te pedirá en Telegram: "¿Quién eres?".

- **IMPORTANTE:** En Telegram, mantén presionado el mensaje de la pregunta y selecciona **RESPONDER**. Si no respondes sobre el mensaje, el bot no sabrá a qué te refieres.
- Mándale un audio de 1 o 2 minutos contando tu vida, tu negocio y tus gustos.
- Revisa el Google Sheet: Si ves que la pestaña "Context" se llenó con tus datos, ¡funciona!

**2. Pregunta Diaria:** Simula el trigger de "Preguntas Diarias". Te debería llegar una pregunta aleatoria basada en tus temas (ej: "¿Cuál fue tu mayor error al vender?").

- Responde con un audio (usando la función "Responder").
- Espera unos segundos... y deberías ver en tu Sheet el post redactado y (si lo activaste) la imagen generada.

---

### ¿Listo para automatizar?

Parece técnico al principio, pero una vez que haces estas conexiones, no tienes que volver a tocarlas. Tu único trabajo será responder un audio mientras te tomas el café.

Recuerda que si quieres entender la estrategia de contenido detrás de esto y por qué lo estructuramos así, tienes el video completo aquí:
