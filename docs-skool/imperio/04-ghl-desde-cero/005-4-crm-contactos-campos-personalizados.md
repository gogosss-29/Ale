# 👥 4. CRM: Contactos & Campos Personalizados

> Ruta: GHL desde Cero › 👥 4. CRM: Contactos & Campos Personalizados

**🎬 Vídeo (11.4 min):** https://www.loom.com/share/65750331426541d1a9cecf5a3a007819

---

**Curso: Go High Level Desde Cero · Sección 4 de 12**

> *Conoce a tus pacientes mejor que ellos mismos.*

Hasta ahora hemos construido la infraestructura. Ahora vamos con **lo más importante de cualquier negocio: los clientes**. En esta sección creamos los pacientes que usaremos durante todo el curso, agregamos campos específicos para una clínica dental y construimos listas que se actualizan solas.

## **📚 Qué vas a aprender**

- Crear contactos manualmente con datos ficticios (pacientes que nos acompañarán todo el curso)
- Entender **DND** (Do Not Disturb) por canal
- Crear **campos personalizados** específicos para clínica dental
- Diferencia clave entre **campos personalizados** y **etiquetas (tags)**
- Construir **Smart Lists** que se filtran y actualizan automáticamente

## **🛠️ Paso a paso**

### **1. Crear el primer contacto**

Ir a **Contacts → Add Contact**.

Para Roberto Martínez:

- **Nombre:** Roberto
- **Apellido:** Martínez
- **Email:** (usa un correo real tuyo o variaciones — útil para pruebas)
- **Teléfono:** el tuyo (para pruebas de SMS/WhatsApp)
- **Ciudad:** Ciudad de México
- **Fecha de nacimiento:** 13/02/2005 (se usa después para el workflow de cumpleaños)
- **Fuente:** Google

![CleanShot 2026-04-24 at 10.06.27.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/06b896ca4c264b87821f0d1e63dd93d1d0a6d57aa42345d7ad5720e38b443d4e.png)

### **💡 DND — Do Not Disturb**

Junto al formulario aparece una sección **DND** con íconos por canal (email, SMS, llamadas, WhatsApp).

- Sirve para marcar que un contacto **no quiere ser contactado** por un canal específico.
- Respeta consentimiento — GHL no le enviará nada por ese canal aunque corras workflows.
- Úsalo cuando el paciente explícitamente pida no recibir X tipo de comunicación.

### **2. Crear los otros 5 contactos**

Repetir el proceso para los otros 5 pacientes (pueden ser ficticios, pero con correos y teléfonos reales/tuyos para poder probar los flujos más adelante).

> 💡 **Estos 6 pacientes nos van a acompañar durante TODO el curso.** Cada uno representa un escenario distinto: lead nuevo, paciente activo, no-show, cliente ganado, etc. Invierte los 5 minutos en crearlos bien ahora.

### **3. Crear campos personalizados específicos para dental**

Ir a **Settings → Custom Fields → Add Field**.

GHL ofrece muchos tipos de campo:

- Texto (línea única / múltiple)
- Número, teléfono, monetario
- Dropdown (único / múltiple)
- Radio, checkbox
- Fecha
- Archivo (útil para estudios clínicos)

**Campo 1 — Tipo de tratamiento (Dropdown múltiple)**

- **Tipo:** Single Options (dropdown único)
- **Nombre:** `Tipo de tratamiento`
- **Objeto:** Oportunidad (no Contacto — ahora explicamos por qué)
- **Opciones:** Limpieza, Blanqueamiento, Ortodoncia, Cirugía, Revisión

> 💡 **¿Por qué va en Oportunidad y no en Contacto?** Un paciente puede tener *múltiples* tratamientos a lo largo del tiempo. Si el campo vive en el contacto, sobrescribes el dato cada vez. Si vive en la oportunidad, cada tratamiento es una oportunidad distinta con su propio tipo. Lo verás claro en la Sección 5.

**Campo 2 — Fecha de última visita (Fecha)**

- **Tipo:** Date Picker
- **Nombre:** `Fecha de última visita`
- **Objeto:** Contacto
- **Grupo:** Additional Info

Este campo dispara el workflow de limpieza semestral (Sección 9).

**Campo 3 — Notas clínicas (Texto multilínea)**

- **Tipo:** Multi Line
- **Nombre:** `Notas clínicas`
- **Objeto:** Contacto
- **Grupo:** Additional Info

Útil para anotar historial, alergias, sensibilidades.

### **4. Llenar los campos en Roberto**

Volver al contacto Roberto Martínez → **Additional Info**:

- **Fecha de última visita:** ayer
- **Notas clínicas:** "Roberto se realizó un blanqueamiento. Pagó por tres servicios, tiene dos pendientes."

### **5. Campos personalizados vs. Etiquetas (tags)**

Campo personalizadoEtiqueta (tag)**Qué es**Un dato/valor único por contactoMarcador que se repite y se filtra**Ejemplos**Fecha cumpleaños, notas clínicas, tipo sangrePaciente activo, No-show, Lead nuevo**Uso**Guardar información específicaSegmentar y filtrar grupos

### **6. Crear las etiquetas del curso**

Ir a **Settings → Tags → Add Tag** y crear estas:

- `paciente-activo`
- `no-show`
- `servicio-completo`
- `lead`

![CleanShot 2026-04-24 at 10.07.17.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/98ccf5bfb3f0408d8887138b0b87c29d97a59312207c4bb294d15ae955af6488-md.png)

Asignar `paciente-activo` a Roberto.

> 💡 **Convención:** usa guión medio `-` para las tags, todo en minúsculas. Consistencia = fácil de filtrar después.

### **7. Crear Smart Lists (Listas Inteligentes)**

Las Smart Lists son **filtros guardados que se actualizan solos**. Un contacto aparece automáticamente cuando cumple la condición y desaparece cuando deja de cumplirla.

**Crear Smart List "Pacientes activos":**

1. Contacts → **Advanced Filter**
2. Filtrar por: **Tag = paciente-activo**
3. **Apply → Create**
4. Nombre: `Pacientes activos`

> 💡 Cuando agregas la tag a un nuevo contacto, aparece instantáneamente en la Smart List. Cuando quitas la tag, desaparece. No tienes que mantenerla manualmente.

### **8. Crear el resto de Smart Lists**

Repetir el proceso para:

- `Leads nuevos` → filtro: tag `lead`
- `No-shows` → filtro: tag `no-show`
- `Clientes ganados` → filtro: tag `servicio-completo`

## **📎 Recursos**

### **📋 Plantilla — Tags iniciales**

```
paciente-activo
no-show
servicio-completo
lead
```

### **💡 Regla de oro**

- **Para crear un contacto NO es obligatorio tener nombre y apellido**, pero **SÍ es obligatorio** tener al menos email o teléfono.
- Sin esos dos, GHL no puede identificarlo como único.

## **✅ Checklist antes de avanzar a la Sección 5**

- [ ] 6 contactos ficticios creados (con datos reales tuyos para pruebas)
- [ ] 3 campos personalizados creados (tipo de tratamiento, fecha última visita, notas clínicas)
- [ ] 4 tags creadas
- [ ] 4 Smart Lists filtrando por cada tag
- [ ] Roberto Martínez con campos personalizados llenos y tag `paciente-activo`

## **➡️ Siguiente sección**

**Sección 5 — Pipelines & Oportunidades.** Ya tenemos el CRM, ahora vamos a visualizar el recorrido que hace cada paciente desde que es lead hasta que se vuelve cliente ganado. Y lo más importante: vas a entender la diferencia entre **contacto** y **oportunidad**, que es una de las cosas que la mayoría de gente no entiende en GHL.
