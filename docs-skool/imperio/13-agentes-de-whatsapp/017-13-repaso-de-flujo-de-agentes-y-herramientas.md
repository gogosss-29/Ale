# 🔁 13. Repaso de flujo de agentes y herramientas

> Ruta: Agentes de WhatsApp › 🔁 13. Repaso de flujo de agentes y herramientas

**🎬 Vídeo (5.0 min):** https://www.loom.com/share/88fc3fde7e3e4ddb8deafe00a3dad572

---

En este módulo cerramos la primera etapa del agente revisando cómo queda armado el flujo completo. Esta mirada desde arriba es clave para entender cómo trabajan juntos el prompt, el modelo, la memoria y las herramientas, y para poder mejorar o escalar el agente sin romper nada.

---

## **1. Configuración base del agente**

El agente se construye sobre tres piezas principales:

- **System Prompt** con rol, contexto, objetivo, tono y un flujo mental definido.
- **Modelo:** GPT-4.1 Mini con temperatura moderada.
- **Memoria:** memoria simple de n8n usando el *remoteJID* como llave y recordando hasta 20 interacciones.

Con esto, el agente conversa de forma coherente, mantiene contexto y responde con una personalidad estable.

---

## **2. Herramientas conectadas**

El agente tiene dos herramientas integradas directamente con Airtable:

**1) Actualizar Descripción del Negocio**  
La IA genera una descripción cuando tiene suficiente información y la herramienta:

- Busca al usuario por número
- Actualiza el campo en Airtable
- Usa la respuesta de la IA como input

**2) Actualizar Soluciones del Negocio**  
Hace lo mismo, pero con las propuestas o ideas de automatización.

Las dos se activan automáticamente cuando el agente considera que los datos ya están listos, manteniendo la base de datos al día sin trabajo manual.

---

## **3. Cómo piensa y actúa el agente**

El agente sigue un proceso claro, guiado por su prompt:

1. Identifica intención y contexto
2. Evalúa si tiene suficiente información
3. Si falta algo, pregunta
4. Analiza procesos, problemas y oportunidades
5. Detecta posibles automatizaciones
6. Diseña una propuesta clara
7. Explica beneficios y propone el siguiente paso

Esta estructura evita respuestas improvisadas y mantiene conversaciones útiles, siempre orientadas a resultados.

---

## **4. Cómo se integran herramientas y flujo**

Las herramientas no funcionan “aparte”, sino dentro del flujo del agente. Por ejemplo:

- Si detecta que ya tiene información suficiente → actualiza la descripción del negocio
- Si descubre una oportunidad de automatización → actualiza el campo de soluciones

Esto hace que el agente no solo hable: **toma acción y produce datos reales.**

---

## **Qué te permite este módulo**

- Ver cómo encajan todas las piezas del agente
- Entender la función del prompt, el modelo, la memoria y las tools
- Ajustar o expandir el agente sin romper su lógica
- Replicar este blueprint para crear agentes especializados
- Tener un agente que responde, pero también actualiza, registra y ejecuta

Con este repaso ya tienes la visión completa del agente. Desde aquí puedes escalar: agregar tools más avanzadas, integrar subagentes, conectar APIs o llevarlo a producción con memorias robustas.
