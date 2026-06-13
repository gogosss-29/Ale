# Soporte - 8 de Oct

> Ruta: 🛠️ Soporte › Soporte - 8 de Oct

**🎬 Vídeo (64.7 min):** https://www.youtube.com/watch?v=qTT7_qNbXQA

---

## Problemas que resuelve

Conexión de APIs “no soportadas” vía HTTP en Make para TTS y manejo de archivos; recuperación de memoria en agentes de atención por WhatsApp con ManyChat + OpenAI (thread_id, tiempos de espera y mapeos); recolección de assets de clientes y publicación en escala usando Airtable + Google Drive; control de buffers de mensajes (Redis/Chatwoot) evitando null items con filtros y validaciones.

---

## Intervenciones (cronológico)

[01:03] **José – Conectar Wavespeed TTS vía API en Make**  
Problema: POST funcionaba pero no se guardaban/recuperaban los audios.  
Solución:

- En HTTP → POST a la ruta correcta (modelo “HD”), `Content-Type: application/json` y `Authorization: Bearer`.
- Parsear “Response” en el 2º HTTP (GET de prediction/result) para exponer el URL final.
- Insertar `Sleep (10s)` entre POST y GET para esperar el asset.
- `HTTP > Get a file` con la URL de CloudFront y luego `Google Drive > Upload a file` (nombre desde la columna “text” del Sheet). Resultado: MP3 subido con nombre correcto y flujo estable.

[22:00] **Jorge – ManyChat + OpenAI Assistant sin memoria (thread_id)**  
Problema: El asistente reiniciaba la conversación; no persistía el hilo.  
Solución:

- Enviar `thread_id` en el webhook a Make en JSON bien formado.
- Guardar/leer `thread_id` en Airtable y mapearlo en el nodo de OpenAI.
- Mapear el `subscriber.last_input_text` como mensaje del usuario.
- Aumentar `Wait` en ManyChat a ~30s (antes 10s no alcanzaba para la respuesta del modelo).
- Corregir campo `phone` en las búsquedas y activar el escenario. Resultado: continuidad real del chat.

[50:00] **Silvia – Intake de imágenes/vídeos y calendario de contenidos**  
Problema: Google Forms no entregaba bien los archivos ni los enlazaba con el calendario/cliente.  
Solución:

- Usar **Airtable Forms** para recibir email + imágenes/vídeos (obtienes URLs públicas).
- Make: trigger por nuevo registro → crear carpeta en **Google Drive** por cliente → `HTTP Get a file` (desde la URL de Airtable) → subir a carpeta del cliente.
- Recomendación: separar escenarios por cliente/publicación para robustez. Pricing: considerar volumen (35 cuentas) y soporte; cobrar por valor y carga operativa.

[57:45] **Carlos – Buffer Redis/Chatwoot genera item **`null` tras loop  
Problema: En el tercer ciclo del `GET` aparecía un ítem `null` que disparaba error, aunque el flujo seguía.  
Solución:

- Añadir **Filter/Switch** antes o después del `Wait` para descartar `null` y cortar el loop limpio.
- Alternativa: validar `null` con un bloque “Code” y/o considerar **Supabase** como store de buffer.
- Notas: 404/503 vistos fueron transitorios; refrescar y manejar reintentos.

[1:03:19] **Cierre**  
Próxima sesión (viernes): revisión a fondo de **Agent Builder de OpenAI** y cómo integrarlo en flujos.
