# Soporte - 9 de Diciembre

> Ruta: 🛠️ Soporte › Soporte - 9 de Diciembre

**🎬 Vídeo (61.8 min):** https://www.youtube.com/watch?v=5xhRec4a0kA

---

### Problemas que resuelve

- Cómo enviar **audios, imágenes y archivos en WhatsApp** usando Evolution, Make y N8N sin errores de formato.
- Cómo **corregir problemas de tokens, webhooks que se desactivan solos y credenciales mal mapeadas**.
- Cómo diseñar **agentes de WhatsApp más humanos** (marcar escribiendo, mensajes leídos, envío multimedia).
- Cómo estructurar flujos estables para **manejar archivos binarios (audio, imagen, video)** y evitar datos nulos.
- Cómo **integrar IA con AirTable** para seleccionar y enviar imágenes de productos automáticamente.  
  
[00:00] Inicio de la sesión y contexto

Franco da la bienvenida y explica la dinámica de la sesión: análisis técnico caso por caso, con foco en resolver problemas reales de automatización en WhatsApp usando Evolution, Make y N8N. Se confirma la fecha y el formato práctico del encuentro.

---

### [01:24] Raimundo – Problemas con audios y estados de WhatsApp

Expone dificultades para:

- Enviar audios desde N8N.
- Marcar mensajes como leídos y “escribiendo”.
- Errores de token y credenciales en Evolution.

**Solución:**  
Franco explica la diferencia entre webhooks de entrada y credenciales de envío, muestra cómo crear correctamente la credencial de Evolution y cómo mapear el `remoteJID` usando expresiones.  
Se habilita la lectura automática de mensajes desde la configuración de Evolution para evitar errores manuales.

---

### [08:25] Ale – Descarga de audios e imágenes desde Evolution

Plantea el problema de archivos descargados en formato `.ENC` y errores al intentar enviarlos a ChatGPT.

**Solución:**  
Se explica que Evolution en Cloud entrega **URLs directas al archivo**, por lo que no es necesario decodificar Base64.  
La clave es:

- Identificar la **media URL correcta** desde el webhook.
- Usar un **HTTP Get File** para tratar el archivo como binario.
- Evitar pasos innecesarios que rompen el flujo.

---

### [14:19] Claudio – Error de credenciales y Record ID en AirTable

Muestra un error al usar una plantilla de WhatsApp con N8N donde los mensajes no se guardaban correctamente.

**Diagnóstico y solución:**

- El problema no era la credencial sino el **Record ID incorrecto**.
- Se explica por qué **reseleccionar la base** es obligatorio aunque tenga el mismo nombre.
- Se corrige el mapeo usando `record ID` en lugar de campos manuales.
- Recomendación clave: copiar y reutilizar el mapeo para evitar errores al cambiar credenciales.

---

### [21:50] Raimundo – Webhooks que se apagan solos

Consulta por un comportamiento extraño donde el webhook de Evolution se desactiva.

**Análisis:**  
Franco explica que puede suceder si:

- El webhook no responde correctamente.
- El flujo falla durante pruebas.

**Soluciones prácticas:**

- Activar `Respond immediately` en el webhook.
- Probar el webhook en producción.
- Limitar los eventos solo a `messages.upsert`.
- Ejecutar el webhook manualmente para fijar la estructura de datos.

---

### [26:33] Monitoreo de errores en N8N

Franco comparte un **workflow interno de monitoreo de errores** usado en la agencia.

**Valor clave:**  
Permite recibir alertas automáticas (WhatsApp, servidor, etc.) cuando un flujo falla, evitando que el cliente detecte el error antes que el equipo.

---

### [28:15] John – Envío de imágenes desde un agente de WhatsApp

Pregunta cómo hacer que un agente:

- Detecte qué producto quiere el usuario.
- Envíe automáticamente la imagen correcta.

**Desarrollo en vivo:**  
Franco construye el flujo completo:

1. Productos con imágenes en AirTable.
2. La IA selecciona el producto correcto.
3. Se obtiene la URL de la imagen.
4. Se descarga la imagen como binario.
5. Se envía por WhatsApp usando `send media` en Evolution.

Se introduce el concepto de **sub-workflows como herramientas**, separando:

- Lógica del agente.
- Envío técnico de la imagen.

---

### [39:02] Diferencia entre enviar una imagen fija vs dinámica

Se aclara que:

- Enviar imágenes fijas es simple.
- Enviar imágenes dinámicas requiere que la IA seleccione el registro correcto, pero **no es complejo si la lógica está bien diseñada**.

---

### [52:30] Ale – Error con media URL y data nula

Se detecta que el error no era de configuración sino de **URL incorrecta**.

**Solución:**

- Abrir la URL del archivo en el navegador.
- Confirmar que devuelve directamente el media.
- Usar ese enlace en un HTTP Get File.  
El flujo queda funcionando correctamente.

---

### [01:01:30] Cierre

Franco cierra la sesión reforzando:

- La importancia de entender cómo trata archivos Evolution.
- No sobrecomplicar flujos cuando ya existe una URL válida.
- Pensar siempre la lógica antes de copiar plantillas.  
Invita a continuar el trabajo en las próximas sesiones.
