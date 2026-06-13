# 🤖 10. Prompting y configuración de Agentes

> Ruta: Agentes de WhatsApp › 🤖 10. Prompting y configuración de Agentes

**🎬 Vídeo (6.7 min):** https://www.loom.com/share/df87a76950cd4e05a5f590c4d038ebe0

---

En este módulo entramos en la parte más importante del agente: su cerebro.  
Aquí definimos cómo piensa, cómo responde, cuáles son sus límites y qué objetivo debe cumplir. Todo esto ocurre dentro del bloque del agente IA, donde configuramos el prompt, las reglas y los parámetros que guiarán cada respuesta.

---

## **Cómo se arma el agente**

Dentro del nodo del agente vemos elementos clave:

- **User message:** lo que envía la persona
- **System message:** instrucciones base del agente
- **Memoria**
- **Modelo**
- **Tools**

El nodo se deja en modo *Define Below*, lo que permite controlar exactamente qué información recibe. Todo lo que construiste en módulos anteriores —input, memoria, datos del usuario— converge aquí.

---

## **El System Message: donde nace la personalidad**

El system message es el corazón del agente. Aquí defines:

- **Rol:** quién es y qué función cumple
- **Contexto:** con quién interactúa y en qué situaciones
- **Objetivo:** qué debe lograr en cada conversación

A esto se suman:

- Tono y estilo
- Instrucciones paso a paso (SOP)
- Límites y restricciones
- Formato de salida

Usar Markdown facilita la claridad y la interpretación del modelo.

---

## **Guía mental (SOP)**

Esta sección define cómo debe pensar el agente. El orden habitual:

1. Analizar el mensaje
2. Identificar intención
3. Revisar memoria
4. Responder o ejecutar una acción

Sin este proceso, la IA responde de forma reactiva. Con él, responde de forma consistente y profesional.

---

## **Límites y restricciones**

Los agentes no fallan por “falta de prohibiciones”, sino por prompts saturados o contradictorios.  
Regla clave: **si tu agente funciona mal, quita antes de agregar**.

Cuando necesites funciones muy específicas, considera crear subagentes en lugar de recargar el principal.

---

## **Formato de salida**

Aquí defines cómo debe responder:

- Conversacional
- Listas
- Pasos
- JSON estructurado

Un formato claro evita trabajo manual y asegura que otros módulos puedan seguir procesando sin errores.

---

## **Qué logras con este módulo**

- Agentes que piensan como tú lo necesitas
- Prompts claros y fáciles de mantener
- Respuestas consistentes en tono, estructura y objetivo
- Menos errores y comportamientos inesperados
- Preparación para integrar memoria, herramientas y modelos avanzados

En resumen: este módulo convierte a tu agente en una entidad coherente, estratégica y alineada con tu negocio.
