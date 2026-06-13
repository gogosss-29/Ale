# 🧠 11. Selección de Modelos y Uso de Memoria

> Ruta: Agentes de WhatsApp › 🧠 11. Selección de Modelos y Uso de Memoria

**🎬 Vídeo (8.8 min):** https://www.loom.com/share/7370252a750247d1a351ea9675a35471

---

## **1. Selección de Modelos**

Dentro del nodo del agente puedes elegir cualquier modelo, pero en la práctica solo unos pocos funcionan realmente bien para conversaciones.

### **Modelos recomendados**

**1. GPT-4.1 Mini**  
Ideal para conversación diaria:

- Más humano
- Natural
- Rápido
- Económico

No tiene razonamiento profundo, pero para chats fluidos es perfecto.

**2. GPT-4.1**  
La versión completa, con capacidad de análisis.  
Sirve cuando el agente debe pensar, planificar o resolver algo más complejo.

Puedes ajustar el **Reasoning Effort** para controlar:

- Tiempo de respuesta
- Consumo
- Profundidad del análisis

### **Modelos no recomendados**

**Nano**  
Suele fallar en consistencia. Para agentes conversacionales no es fiable.

---

## **Parámetros clave**

- **Temperature (0.6–0.7):** controla creatividad. Más alto → más riesgo de inventar.
- **Frequency Penalty:** reduce repeticiones.
- **Timeout:** normalmente no requiere cambios.
- **Max Iterations (5):** útil solo si el agente debe ejecutar varias acciones internas.

Estos ajustes te permiten equilibrar calidad, costo y velocidad según el uso del agente.

---

## **2. Memoria del Agente: cómo recuerda**

La memoria define cuánto contexto mantiene el agente entre mensajes.  
Sin una buena configuración, olvida datos, mezcla información o responde incoherente.

### **Opción 1: Memoria simple (nativa de n8n)**

Perfecta para pruebas o agentes pequeños.

Requiere dos cosas:

- **Session key:** en WhatsApp, se usa el *remoteJID* (el número del usuario).
- **Cantidad de mensajes a recordar:** por defecto son 5; para uso real, mejor 20.

### **Opción 2: Memoria con Postgres / Supabase**

Recomendada para producción.

Ventajas:

- Más estable
- Escalable
- Difícil de romper
- Fácil de consultar

En n8n solo creas una credencial de Supabase y el agente ya puede leer/escribir su memoria allí.  
Supabase permite usar Postgres de forma no-code, por eso es tan útil en agentes reales.

---

## **Qué logras con este módulo**

- Elegir el modelo adecuado para tu agente
- Controlar creatividad, razonamiento, velocidad y costos
- Construir memoria estable y escalable
- Evitar pérdidas de contexto y errores comunes
- Preparar un agente listo para producción en WhatsApp, web o cualquier entorno real
