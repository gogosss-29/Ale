# 🚦 5. Pipelines & Oportunidades

> Ruta: GHL desde Cero › 🚦 5. Pipelines & Oportunidades

**🎬 Vídeo (12.5 min):** https://www.loom.com/share/ce90e0a064154b8288f7dfcb3eefa190

---

**Curso: Go High Level Desde Cero · Sección 5 de 12**

> *Si no sabes en qué etapa está cada paciente, estás volando a ciegas.*

Ya tenemos el CRM con pacientes, pero hay una pregunta que todo dueño de negocio necesita responder cada día: **¿en qué etapa está cada paciente y cuánto dinero potencial tengo en juego?** Para eso existen los **pipelines**. En esta sección construimos el pipeline de la clínica y entendemos la diferencia entre **contacto** y **oportunidad** — uno de los conceptos peor entendidos de GHL.

## **📚 Qué vas a aprender**

- Qué es un **pipeline** y por qué es el corazón del CRM
- La diferencia clave entre **contacto** (persona) y **oportunidad** (valor potencial)
- Construir un pipeline de 7 etapas para la clínica dental
- Agregar valores monetarios a las oportunidades
- Leer el pipeline en 5 minutos cada mañana

## **🛠️ Paso a paso**

### **1. Entender qué es un pipeline**

Un pipeline es la **representación visual del camino** que recorre un paciente, de izquierda a derecha:

```
Lead nuevo → Engagement → Cita agendada → Asistió → Tratamiento → Cliente ganado
                                        → No asistió

```

Piénsalo como un embudo horizontal: a la izquierda entran los leads nuevos, a la derecha salen los clientes ganados.

### **2. Crear el pipeline**

Ir a **Opportunities → Pipelines → Create Pipeline**.

- **Nombre:** `Nuevos Pacientes`
- **Visualización del color:** elegir "nombre con fondo de color" (es más fácil de leer en vista Kanban)

![CleanShot 2026-04-24 at 13.46.41.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/55ac3a4c85694978be7b1fa7dfb4725506d85349a556486e91169e27b9f9372f-md.png)

### **3. Definir las 7 etapas**

Crear las etapas en este orden (izquierda → derecha). **Sistema sugerido:** colores tipo semáforo (frío → caliente, rojo = urgencia, verde = ganado).

> 💡 El orden y los colores son criterio tuyo. Lo importante es que **visualmente** sepas de un vistazo dónde está cada paciente.

### **4. Entender contacto vs. oportunidad**

Esta es la parte que nadie te explica bien:

Contacto La **persona** (Roberto Martínez)

Oportunidad El **valor potencial** en el pipeline

Nombre, email, teléfono, cumpleaños

Tipo de tratamiento, valor MXN, etapa

**Único** por persona

Un contacto puede tener **varias oportunidades**

**Ejemplo real:** Roberto tiene un blanqueamiento en proceso *y* una limpieza agendada para el próximo mes. Son **2 oportunidades** del **mismo contacto**, en etapas distintas del pipeline.

Por eso en la Sección 4 pusimos el campo "Tipo de tratamiento" en la Oportunidad y no en el Contacto.

### **5. Crear la primera oportunidad (desde el contacto)**

Ir a **Contacts → Roberto Martínez**. Abajo encuentras una sección **Opportunities**.

Click en **+ Add Opportunity**:

- **Nombre:** `Roberto Martínez — Limpieza Dental`
- **Pipeline:** Nuevos Pacientes
- **Etapa:** Nuevo Lead (luego lo movemos)
- **Valor:** $5,000 MXN
- **Tipo de tratamiento:** Limpieza (campo personalizado que creamos en la Sección 4)
- **Owner:** (opcional — el doctor o asistente asignado)

Como Roberto ya tiene la tag `paciente-activo` y ya viene antes, moverlo directamente a **Tratamiento en Proceso**.

### **6. Crear oportunidades para los otros contactos**

![CleanShot 2026-04-24 at 13.48.11.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/248ee7e0e5af4f67a938aea30558de80caf128efadb942f7bf8bcec12c540403.png)

### **7. Vista Kanban vs. Vista Lista**

- **Vista Kanban:** drag-and-drop, visualmente satisfactoria, perfecta para tu rutina diaria.
- **Vista Lista:** más denso, útil para exportar o filtrar.

Cada columna muestra un **total en $** — la suma del valor potencial de las oportunidades en esa etapa.

### **8. La rutina del dueño de clínica — 5 minutos al día**

Cada mañana, abrir el pipeline con un café:

- **Columna "No Asistió":** ¿a quién hay que rescatar? (Workflow de la Sección 10 lo hace solo.)
- **Columna "Cita Agendada":** ¿cuántas citas hay hoy?
- **Columna "Tratamiento en Proceso":** ¿quién necesita seguimiento?

> 💡 **Tip práctico:** Si una columna crece demasiado vs. la siguiente, es una señal de fricción. Ej: muchos en "Engagement" pero pocos en "Cita Agendada" = el proceso de agendar tiene un problema.

## **📎 Recursos**

### **📋 Plantilla — Pipeline "Nuevos Pacientes" (7 etapas)**

```
1. Nuevo Lead            [azul]        → Entra todo el que llega por el funnel
2. Engagement            [azul oscuro] → Ya contactamos, aún no agenda
3. Cita Agendada         [amarillo]    → Reservó fecha/hora
4. Asistió               [verde claro] → Vino a la cita
5. No Asistió            [negro]       → Dispara el workflow de rescate
6. Tratamiento en Proceso[amarillo+]   → Múltiples sesiones en curso
7. Cliente Ganado        [verde]       → Tratamiento completado

```

### **🎯 Regla de oro**

**Un contacto = UNA persona. Una oportunidad = UN tratamiento/servicio.**

Un mismo contacto puede tener varias oportunidades activas al mismo tiempo.

## **✅ Checklist antes de avanzar a la Sección 6**

- [ ] Pipeline "Nuevos Pacientes" creado con 7 etapas
- [ ] Colores asignados por etapa
- [ ] Al menos 6 oportunidades creadas (una por cada contacto)
- [ ] Oportunidades distribuidas en diferentes etapas (para probar workflows después)
- [ ] Cada oportunidad con su **valor monetario** y **tipo de tratamiento**

## **➡️ Siguiente sección**

**Sección 6 — Funnel: Landing Page + Calendario.** El CRM y el pipeline están listos, pero el pipeline está vacío si no hay forma de llenarlo. En la siguiente sección construimos el funnel que convierte visitantes en citas agendadas: landing page + calendario integrado, sin llamadas, sin WhatsApp, sin esperar respuesta — auto-servicio total.
