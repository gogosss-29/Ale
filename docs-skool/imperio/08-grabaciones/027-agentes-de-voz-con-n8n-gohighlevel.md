# Agentes de Voz con n8n + GoHighLevel

> Ruta: 🔴 Grabaciones › Agentes de Voz con n8n + GoHighLevel

**🎬 Vídeo (62.1 min):** https://www.youtube.com/watch?v=wXV_8nH2TIw

---

## Problemas que resuelve

Cómo **decidir cuándo usar IA y cuándo lógica**, cómo **estructurar sistemas en n8n que escalen sin romperse**, cómo **conectar agentes de voz con GoHighLevel** para agendar citas reales, y cómo **pensar productos automatizados modulares** (administrativos y operativos) que las pymes sí pagan.

---

## Intervenciones (cronológico)

[00:00] Franco – Apertura y contexto  
Sesión del **30 de diciembre**, fin de año, formato reducido. Se aclara que los martes se usarán para **preguntas y resolución de casos específicos**.

[01:14] Franco – Dinámica de participación  
Se explica el uso del botón **“levantar la mano”** para ordenar preguntas y casos durante la sesión.

---

[02:23] Antonio – Bienvenida y primeros pasos  
Antonio se presenta como miembro nuevo (menos de una semana). Comenta que estuvo evaluando **Make vs n8n**, decidió ir con **n8n**, y está montando su servidor en **Hostinger**, donde tuvo problemas de acceso al VPS.

[03:29] Franco – Acompañamiento técnico  
Se valida el camino de Antonio con n8n y se ofrece apoyo tanto en **VPS/hosting** como en agentes IA cuando lo necesite.

---

[04:49] Juan Felipe – Sistema mensual con lógica + IA  
Juan explica su sistema:

- Procesa **12 planillas mensuales**
- Usa **nodos de código** para lógica (sumas, conteos, validaciones)
- La **IA solo redacta el informe final**, no analiza ni calcula  
Resultado: sistema robusto, claro y sin alucinaciones.

[06:55] Juan Felipe – Aprendizaje clave  
Destaca que entendió el concepto central repetido en sesiones anteriores:  
👉 **Primero lógica, después IA**.  
La IA solo comunica resultados, no decide.

[07:19] Juan Felipe – Próximo paso: producto  
Planea convertir el sistema en una **mini SaaS** para consultorios y negocios similares en 2026.

---

[08:02] Juan Felipe – Duda: un sistema o varios en n8n  
Pregunta si debe crear **flujos separados** o mantener todo en un solo escenario.

[08:21] Juan Felipe – Demo del workflow  
Muestra el flujo completo:

- Cron mensual
- Lógica por planilla
- Merge y consolidación
- Creación de tabla HTML
- Generación de informe
- Guardado histórico por año

[09:47] Juan Felipe – Nuevo requerimiento: WhatsApp  
Quiere enviar un **resumen mensual por WhatsApp**, además del email, usando la tabla consolidada.

---

[10:48] Franco – Solución arquitectónica  
Recomendación:

- Mantener el flujo principal
- Crear una **rama paralela** desde el consolidado
- Usar un **nodo Code** para transformar el JSON en un mensaje de WhatsApp (texto plano)

[12:22] Franco – Manejo de múltiples ítems (Merge issue)  
Se detecta ejecución duplicada por configuración del **Merge node**.  
Solución: ajustar settings y validar inputs para consolidar correctamente los 12 ítems.

[17:24] Franco – Prompting correcto para código  
Explica cómo usar GPT solo para **generar el código JavaScript**, no como parte directa del flujo productivo.  
El código final se pega en el **Code node**.

---

[19:15] Juan Felipe – Error en el script  
Se detecta que GPT devolvió **datos hardcodeados** (strings fijos) en vez de variables dinámicas.

[22:12] Daniel – Debugging con console.log  
Daniel explica cómo usar **console.log + DevTools (F12)** para depurar el código dentro del nodo y verificar qué datos están llegando realmente.

[24:48] Daniel – Insight clave  
El problema no era la lógica, sino que el input estaba **forzado como constante** y no tomaba los datos reales del workflow.

[28:35] Franco – Cierre del caso  
Juan ya tiene la base correcta para generar el resumen y luego conectar WhatsApp (Evolution API o HTTP).

---

[30:31] Carlos – Demo: agente de voz para retail  
Carlos muestra un **agente de voz en inglés** conectado a **GoHighLevel**, capaz de:

- Atender llamadas
- Calificar leads
- Agendar citas
- Confirmar datos paso a paso

[31:27] Carlos – Costos y latencia  
Explica métricas reales:

- ~USD 0.14 por minuto
- Latencia influida por GPT-4.1 + ElevenLabs
- Uso de waits artificiales para que suene más humano

[36:05] Debate – Voz IA vs call centers  
Se discute percepción del usuario final:

- Mejor hablar con IA que con call centers tradicionales
- Importancia del tono, pausas y velocidad

---

[41:08] Carlos – Modelo de precios  
Estrategia comercial en EE.UU./Canadá:

- Setup alto + mensualidad
- Desde USD 497/mes
- Agente avanzado hasta USD 3500 setup  
Se vende como **“empleado 24/7”**, no como “IA”.

[44:35] Carlos – Caso simple que vende más  
Muchos clientes pagan solo por:  
👉 **Mensaje automático cuando hay llamada perdida**, que luego califica y deriva.

---

[46:28] Daniel – Sistema administrativo para contratistas  
Daniel muestra un sistema completo (Next.js + .NET):

- Estimaciones
- Inventarios
- PDFs complejos
- OCR + parsing robusto
- Transcripción y traducción de notas de voz (español → inglés)

[52:59] Daniel – Filosofía Lego  
Construye sistemas **modulares**, vendiendo bloques:

- Agenda
- Estimaciones
- Inventario
- Voz  
Cada bloque agrega valor sin romper lo anterior.

[57:25] Daniel – IA para acelerar, no para reemplazar criterio  
Como developer, usa IA para avanzar rápido, pero **controla estructura y dependencias** para evitar spaghetti code.

---

[01:01:39] Franco – Cierre  
Conclusión general:

- Lo administrativo vende mejor y genera menos fricción
- Sistemas simples, claros y robustos escalan más
- Gran valor en combinar **lógica + automatización + IA con criterio**

Se despiden y se desea buen inicio de año a la comunidad.
