# Cómo Evitar Alucinaciones

> Ruta: 🔴 Grabaciones › Cómo Evitar Alucinaciones

**🎬 Vídeo (57.2 min):** https://www.youtube.com/watch?v=XymJAV4zJvo

---

## Problemas que resuelve

Cómo **evitar alucinaciones al generar reportes mensuales**, cómo **separar lógica, reporte y análisis con IA**, cómo **procesar CVs en PDF/imagen/Word en n8n**, cómo **enviar imágenes correctamente por HTTP**, y cómo **automatizar envíos de archivos agrupados por proveedor** sin duplicar correos.

---

## Intervenciones (cronológico)

[00:00] Franco – Apertura y contexto  
Sesión del **23 de diciembre**, martes de Q&A previo a Navidad. Se recuerda el formato: traer dudas concretas y usar “levantar la mano”.

---

[01:17] Juan Felipe – Reporte mensual desde Airtable  
Juan muestra un flujo donde recopila múltiples formularios en **Airtable**, filtrados por mes, consolidados en un JSON para generar un **informe administrativo mensual** para clínicas.

[04:21] Juan Felipe – Problema: la IA alucina  
Aunque el JSON consolidado está correcto, al pasarlo directo a la IA para generar el informe:

- Inventa meses
- Cambia años
- Desordena información  
El problema no está en los datos, sino en el uso de la IA.

[06:38] Franco – Diagnóstico clave  
Error conceptual:  
👉 **Datos + reporte + análisis están mezclados en un solo paso**.  
La IA está intentando estructurar y analizar al mismo tiempo.

[08:06] Franco – Modelo correcto de trabajo  
Se explica el flujo ideal:  
**Datos → Reporte (lógica, sin IA) → Análisis (IA)**

La IA no debe recibir JSON crudo, sino un **reporte ya ordenado**.

[10:30] Franco – Solución práctica  
Opciones recomendadas:

- Crear **plantillas de reporte por tabla** (sin IA)
- Luego pedir a la IA que analice **cada tabla por separado**
- Finalmente unir los análisis en un análisis macro

Resultado:  
✔ Menos alucinaciones  
✔ Más control  
✔ Reportes consistentes

[12:50] Juan Felipe – Próximo paso  
Acepta el enfoque y confirma que va a rehacer el flujo invirtiendo el orden.

---

[13:14] Jorge – Automatizar carga de CVs  
Jorge tiene una plataforma de reclutamiento. Quiere que los usuarios suban solo el **CV (PDF, Word o imagen)** y que el sistema:

- Extraiga los datos
- Genere un JSON
- Lo envíe al servidor  
Sin que el usuario complete formularios manuales.

[16:13] Franco – Arquitectura general del flujo  
Se separan dos problemas:

1. **Procesar el archivo** (PDF / imagen / Word → texto)
2. **Responder al servidor con un JSON estructurado**

Se explica la importancia de configurar bien el **Webhook + Respond to Webhook** para evitar procesos colgados.

[19:37] Franco – Recomendación técnica

- Primero lograr un **quick win con imágenes**
- Luego extender a PDFs y otros formatos
- Detectar extensión antes de procesar (si viene en el webhook)
- Si no, descargar el archivo y detectar luego

[22:53] Franco – PDFs no se envían directo a OpenAI  
Aclaración importante:

- OpenAI API no procesa PDFs directamente
- Se recomienda convertir a texto usando servicios intermedios (OCR / [pdf.co](http://pdf.co) / similares)
- Luego recién pasar el texto a IA

---

[24:01] Juan – Error enviando imágenes por HTTP  
Juan intenta enviar imágenes desde URLs guardadas en Supabase, pero recibe errores.

[26:10] Franco – Error detectado  
El problema:  
👉 Estaba enviando una **URL**, no un **archivo binario**.  
Las APIs de mensajería requieren el archivo, no el link.

[30:09] Franco – Solución correcta (3 pasos)

1. **HTTP GET** → descargar archivo
2. Convertir a **binario/Base64**
3. Enviar el binario por HTTP

Se recomienda usar un **sub-workflow** reutilizable para este proceso.

[35:14] Franco – Recomendación arquitectónica  
Separar:

- Workflow principal
- Sub-workflow de descarga y envío de archivos  
Mejor mantenimiento y reutilización.

---

[36:53] Sofía – Caso 1: enviar prefacturas por proveedor  
Sofía tiene múltiples Excel mensuales y necesita:

- Agrupar archivos por proveedor
- Enviar **un solo email por proveedor**
- Usar el nombre del archivo para hacer match con emails

[39:01] Franco – Estrategia correcta  
El flujo debe iniciar desde:  
👉 **Listado de proveedores (Sheets/Excel)**  
No desde los archivos.

[40:39] Franco – Lógica recomendada

1. Buscar proveedores
2. Por cada proveedor: buscar archivos cuyo nombre lo contenga
3. Agrupar archivos (aggregator o router)
4. Enviar **un solo correo** con todos los adjuntos

[46:08] Franco – Clave del diseño  
El disparador es el **listado**, no los archivos.  
Esto evita duplicaciones y simplifica el control.

---

[47:14] Sofía – Caso 2: leer PDFs e imágenes mezcladas  
Tiene archivos heterogéneos (PDFs con imágenes incrustadas) y necesita extraer campos como SKU, orden, container, etc.

[49:33] Franco – Solución conceptual  
Unificar el problema:  
👉 **Convertir todo a imagen (PNG)**  
Luego procesar siempre con el mismo flujo OCR.

[50:49] Franco – Implementación

- Router + filtros por extensión
- Conversión a PNG
- Un solo prompt bien diseñado  
Más simple y más robusto que leer múltiples formatos.

---

[51:25] Juana – Duda sobre webhook y JSON  
Juana pregunta de dónde sale el JSON y cómo conectar dos escenarios descargados de la comunidad.

[53:24] Franco – Recomendación clave  
Evitar copiar y pegar sin entender.  
Seguir **paso a paso el video original**, porque el webhook espera información desde un punto específico del flujo.

---

[56:50] Franco – Cierre  
No se alcanzan todas las preguntas por tiempo.  
Recordatorio de la sesión del viernes post-Navidad.  
Cierre con agradecimientos a la comunidad.
