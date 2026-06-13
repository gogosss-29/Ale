# Soporte - 5 de Mayo

> Ruta: 🛠️ Soporte › Soporte - 5 de Mayo

**🎬 Vídeo (57.9 min):** https://www.youtube.com/watch?v=9V4L4-GuHXI

---

**Problemas que resuelve:** Cómo centralizar comunicaciones dispersas en múltiples canales para proyectos con varios interlocutores, cómo construir una base de datos relacional funcional en Google Sheets para automatizaciones con N8N, y cómo gestionar el contexto en Claude Code para mantener calidad de respuestas en tareas largas.

---

**Intervenciones**

**[01:13] Daniel – Paper trail de comunicaciones en empresa HVAC** Comparte el caso de una empresa constructora en EE.UU. donde managers y estimadores usan teléfonos personales para comunicarse, perdiendo historial de llamadas, textos y promesas verbales. Propone usar Twilio para asignar números corporativos, capturar voz y SMS, transcribir con IA y vincular cada comunicación al proyecto correspondiente mediante una base de datos de contactos unificada.

**[09:33] Flor – RAG para escuela en casa con PDFs de libros escolares** Explica que tiene cientos de PDFs de libros escolares organizados en local, con acceso parcial vía OpenAI, pero el sistema no recupera bien información con imágenes ni permite escalar a móvil. Solución: usar Notebook LM para consultas por materia con acceso en la nube. Para escalar a web app robusta, implementar OCR página por página, chunking y vectorización en Supabase. GPT Image 2 para generar infografías desde capítulos exportados como texto.

**[30:20] Ángel – Bitácora de obra con N8N, Telegram y Google Sheets** Muestra un flujo donde el director de proyecto envía notas de voz o texto, la IA transcribe y formaliza, y se guarda en Google Docs. El problema: el estado de sesión se pierde entre pestañas porque los datos están duplicados en lugar de relacionados. Solución: construir una base de datos relacional en Google Sheets con tres tablas vinculadas — personas, proyectos y sesiones — eliminando la duplicación de datos y leyendo siempre desde la tabla fuente.

**[31:09] Dorian – Prospección para agencia con herramientas de hace un año** Consulta si el método de Apify + Apollo sigue siendo válido o si hay uno más actual. Ya tiene dominio, correo corporativo calentado y Brevo configurado. Consejo: no cambiar de método cuando ya hay avance. Usar la experiencia en media buying como ventaja. Arrancar rápido con volumen y mejorar en el camino. Mientras más personalizado y cercano al dolor concreto del cliente, mayor conversión.

**[51:41] Glenda – Cuándo y cómo usar el comando compact en Claude Code** Pregunta si conviene compactar mientras se ejecuta una tarea y si hay forma de automatizarlo. Solución: no compactar durante una tarea activa. Para tareas largas, pedir un resumen del estado antes de abrir una nueva sesión con ese contexto. Dividir el proyecto en tareas independientes y asignar un chat por tarea para evitar contaminación de contexto.
