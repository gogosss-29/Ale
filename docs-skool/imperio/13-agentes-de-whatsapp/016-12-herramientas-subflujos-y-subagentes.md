# 🛠️ 12. Herramientas, subflujos y subagentes

> Ruta: Agentes de WhatsApp › 🛠️ 12. Herramientas, subflujos y subagentes

**🎬 Vídeo (7.9 min):** https://www.loom.com/share/a2d088ff1d3045d386e955fc13c2e0f8

---

En este módulo entramos a la parte más poderosa del agente: las herramientas.  
Aquí es donde deja de ser un bot conversacional y se convierte en un sistema capaz de ejecutar procesos reales, consultar datos, activar automatizaciones o incluso llamar a otros agentes especializados.

Las tools son lo que permiten que el agente *haga*, no solo que *hable*.  
Y en n8n, prácticamente no hay límites.

---

## **1. Qué es una tool dentro de un agente**

Una tool es una acción externa que la IA puede decidir ejecutar cuando la conversación lo requiere. Puede ser:

- Un nodo de Airtable
- Un módulo de código
- Un request HTTP
- Un workflow completo
- O incluso… otro agente IA

La IA no necesita saber cómo está construida. Solo entiende:

- Su nombre
- Los parámetros que debe enviar
- Una descripción que le dice cuándo usarla

Con eso, actúa como si tuviera “brazos adicionales”.

---

## **2. Subflujos: workflows convertidos en herramientas**

Esta es una de las capacidades más potentes: dejar que el agente active un escenario completo de n8n.

Esto permite:

- Procesar datos complejos
- Llamar APIs externas
- Consultar bases personalizadas
- Generar documentos, cálculos y reportes
- Ejecutar automatizaciones bajo demanda

El flujo es simple:

1. Creas un subflujo
2. Definís los parámetros que necesita
3. Le das una descripción clara (“usar esta herramienta cuando…”)
4. La IA envía datos, espera la respuesta y continúa la conversación

Así puedes resolver tareas avanzadas sin saturar el prompt del agente principal.

---

## **3. Subagentes: agentes dentro de agentes**

Un subagente es un agente especializado que el principal puede invocar como una tool.

Ejemplos:

- Un subagente para redactar copies
- Otro para analizar negocios
- Uno para empresas grandes
- Uno para cálculos financieros
- Uno para clasificar o validar inputs

Cada subagente tiene su propio:

- Prompt
- Modelo
- Herramientas
- Objetivo

Desde el agente principal, se usa igual que cualquier tool.  
Por ejemplo, podría tener una herramienta llamada *asesor_de_empresas_grandes* y usarla automáticamente cuando detecta empresas con más de 100 empleados.

Esto modulariza la lógica y evita crear un agente gigante e inestable.

---

## **4. El rol de la descripción**

La descripción de la tool es fundamental.  
Es el texto que le dice a la IA:

- cuándo debe usar la herramienta
- para qué sirve
- qué parámetros debe enviar

La IA **no ve** el contenido interno de la herramienta.  
Solo ve el nombre, la descripción y la lista de parámetros.

Si la descripción es clara, la herramienta se usa bien.  
Si es vaga, la IA la ignorará o la ejecutará en el momento incorrecto.

---

## **Qué logras con este módulo**

- Agentes que ejecutan acciones reales, no solo generan texto
- Subflujos que expanden capacidades sin límites
- Subagentes especializados y fáciles de mantener
- Prompts más livianos y ordenados
- Un sistema modular y escalable
- La base de agentes empresariales robustos, capaces de operar como “departamentos enteros” automatizados

Este módulo abre la puerta a automatizaciones avanzadas donde la IA conversa, decide, ejecuta y regresa con resultados precisos.
