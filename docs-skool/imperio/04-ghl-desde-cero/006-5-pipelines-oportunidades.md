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

## 🎙️ Transcripción

Muy bien, entonces en la última sesión vimos cómo crear contactos, etiquetas, campos personalizados, smart list o listas inteligentes. Ya tenemos nuestros DRM con pacientes, pero hay una pregunta que todo dueño de negocio necesita responder todos los días. En Queta Pesta cada paciente y cuánto dinero potencial tengo juego. Para eso, existen los pibles. En esa sección vamos a construir el Paiplan de la Clínica y a entender la diferencia entre un contacto y una oportunidad, que es una de las cosas más importantes de Goja y Level y que mucha gente no entienta. Primero, un Paiplan es una representación visual del camino que recorre un paciente, imagina que es un enbudo horizontal, al izquierdo entre los leads nuevos y a la derecha sano en los clientes ya ganados. Vamos aquí a el menú de oportunidades clientes potenciales y si se fijan aquí dice crear una nueva secuencia, un nuevo pipeline, ok, vamos a crear un pipeline entonces desde cero enfocándonos en el nicho de la clínica dental para un risa perfecto, perfecto. Lo primero es definir el nombre del pipeline del humbudo, vamos a llamarle nuevos pacientes ya que tenemos el nombre vamos aquí nos dice ok esta vez que a los colores de visualización de la secuencia esto ya es completamente criterio de cada persona como le gusta verlo puede ser nombre de etapa sin ningún color nombre de etapa con un puntito o nombre de la etapa que la etapa tenga un color como tal de mi no personal me gusta que el nombre de la etapa tenga el color de fondo así que vamos a tomar esta opción luego aquí tenemos secuencia de la etapa como hablamos esto va a la izquierda a derecha así que lo que este primero va a ir a salir a la izquierda y lo que esté el último será hasta la derecha, ustedes lo pueden reorganizar con un drag and drop. ¿Qué tenemos aquí? Podemos cambiar el color de la etapa. Fue a seguir un poco el sistema de semáforos o el sistema de frío caliente, empezando con colores azules, colores fríos, terminando con colores calientes o pueden usar también un sistema de que al final cuando el cliente ya fue ganado, digamos, ya realizó el tratamiento ya pagó, que se en verde y si está en medio de la etapa, que está en amarillo, está en unisio, que está en rojo, que se ya queda criterio de cada quien. Aquí que tenemos también, tenemos esto que es para mostrar en el gráfico y en la distribución que lo vamos a ver en el dashboard más adelante para cuestionar el tablero. Así que empecemos. La primer fase que va a ser lo primero donde van a entrar todos los clientes en nuestro embudo va a ser nuevo lit, que ya lo tenemos ahí. El siguiente va a ser engagement. A mí me gusta dejarlo en inglés porque es un nombre bastante genérico y es más fácil de seguirlo, pero si ustedes aquí pudieran poner con un nuevo prospecto y ya fue contactado, etcétera, en el par caso vamos a manejarlo así, que más tenemos, tenemos también hita agendada, agendada, tenemos asistió asita, le podemos dar en añadir etapa y nos agrego no está bajo, no asistió tratamiento en proceso y cliente ganado, vamos a usar en caso un sistema de que los primeros van a ser tonos rojos y después nos vamos a ir acercando hacia los tonos amarillos en caso de que no asistió lo van a poner en negro, tratamente en proceso y terminamos con un verde de cliente de ganado. Eso es meramente criterio cada quien como lo quiera manejar y en este caso entonces vamos a darle crear. Al momento que ya creamos nuestro hmbudo regresamos a clientes potenciales que vamos a tener aquí los colores. Esto es una vista estilo canban, que tenemos aquí en Nuevo Lid, en Gage, menos chita, defendada, asisto, asita, no asistió para también tu proceso y cliente ganado. Obviamente aquí no tenemos nada porque también no creamos oportunidades, lo que tenemos son clientes. Aquí quiero explicar, un contacto es una persona, en este caso vamos a contactos, tenemos aquí, por ejemplo Roberto Martins. Roberto Martínez es un contacto, el contacto tiene un correo, un número de teléfono, nombre, apellido, tiene las etiquetas que ya configuramos, etcétera, que eso es un contacto. Ahora, una oportunidad que también no hemos creado en ninguna es el valor potencial de ese contacto dentro de Payland, dentro de Embudo. Por ejemplo, Roberto Martínez ahorita la vamos a que era una oportunidad de limpieza dental que hay agendado para el viernes. Entonces vamos a hacer eso primero. Vamos aquí donde dice añadir oportunidad, lo podemos hacer de muchas formas, desde el pipeline, lo podemos hacer desde el contacto o la forma más común que lo vamos a ver más adelante, es desde una automatización. entonces vamos nos devuelta a los contactos, recuerde que para cuestión de paso a paso vamos a tener estos contactos que estamos utilizando, vamos a agarrar Roberto Martínez y aquí van a ver arriba a la derecha que tiene las actividades, que es como un historial todo lo que ha pasado, las tareas notas que uno pueda agregar, aquí pueden dejar como nota de historia del clínico, etcétera, titas que todo lo que hay entrado por medio del calendario lo pueden agregar de manera manual o si lo hacen a través de un calendario se va agregando aquí documentos que ustedes pueden subir o documentos que se ha enviado a través de la misma plataforma pagos si ustedes les enví tienen conectado alguna método de pago como Stripe, Mercado Pago, etcétera que es algo que acabo de liberar justo en lo que estoy grabando el curso perdón Boja Level, liberó la integración con un mercado pago, algo que se usa muchísimo en Latinoamérica y asociaciones. Ok, son directamente los objetos que tiene tal cual cada contacto. Nos vamos aquí en actividad y que más tenemos aquí seguidores, seguidores son personas o miembros de esta clínica que pueden estar siguiendo, que pueden estar viendo actualizaciones y tal cual cuando esto está asignado a alguna persona. Si está asignado a alguna persona tienes alguna automatación que si que todos los mensajes, correos, todo va a salir al nombre de esta persona de Silio, una comunicación, la va a poder ver en el inbox, esta persona, etc. Ahora lo que nosotros queremos hacer es crear oportunidades. Para crear no oportunidades de los contactos, vamos irás a la parte de abajo, podemos colapsar esto más fácil, recuerden que aquí tenemos una nota que también podemos agregar directamente acá y vamos a ver que aquí dice automaciones, aquí te muestras y está corriendo, está activo, correo dentro de una automatización y lo que nosotros estamos buscando clientes potenciales que viene siendo las oportunidades, vamos a darle clic en añadir y a lo que nos va a pedir automáticamente muchos campos se mapen porque lo estamos agregando desde contacto, tenemos el nombre, el correo, el teléfono y ese es el nombre de la oportunidad. Por defecto te va a poner el nombre del contacto, pero aquí tu puedes ponerle, no sé,ión y el texto que tú quieras. Para efectos de esto vamos a ponerle que Roberto Martínez tiene una limpieza dental, así se va a llamar el nombre de la oportunidad, está en la secuencia de nuevos pacientes que lo habíamos creado, ahorita está como vamos a dejarlo en el caso como nuevo lit, valor del cliente potencial, hay que definir un precio en casas en pesos mexicanos, porque yo puse que esta clínica está en México, pero ustedes aún así pueden elegir la moneda por defecto de su negocio, en caso voy a decir que una limpieza de ventanas es en 5.000, propietario es por si lo quieren asignar a alguien, seguidores, lo mismo aquí propietarios, podrás ser por ejemplo el doctor en específico que vaya a ser tratamiento por por decir así no tenemos la fuente aquí en tipo de tratamiento entonces podemos hacer una limpa podemos coger limpieza aquí podemos gestionar campos como si queremos agregar algo ya lo vimos la vez pasada así que vamos a regresar y a que regresamos vamos a esta abajo y vemos que tenemos de tecrete de pacienta activo lo cual decíamos que en el caso cuando lo creamos Roberto y era un pacienta activo entonces por lo tanto no lo vamos a poner como un volir vamos a ponerle como tratamiento en proceso y vamos a darle crear listos y se fijan ya dice aquí creado por creado registro y ya se habilita si tenemos lo de las citas tareas notas, pagos, objetos que es muy parecido a lo que vimos en nivel de contacto. Pones esas flechas podemos navegar vamos a otro contacto en casas microfimenes vamos a crearle también aquí en clens potenciales oportunidad, vamos a decir que en el caso Mario sí es un nuevo lead, vamos a decir que le está interesado en no sé, una revisión general y nosotros podrámos mil pesos por revisión general, no tiene ninguna etiqueta ahorita, vamos a ver tenemos la etiqueta de lead nuevo, ten en cuenta que eso lo está haciendo en forma manual ya en la práctica que vamos a ver más adelante una automatización, te encargaría de crear todo esto y vamos a darle crear, perfecto, voy a poner al video voy a crear más oportunidades para todos estos clientes dummy y continuamos para que vean cómo se vería el pavel. Ya tenemos todas las oportunidades creadas, aquí podemos navegar, vemos que tenemos con un nuevo lit amario, con peres ya está en engagement, que más tenemos aquí. Amaria BCR no asistió a la cita que tenía, aquí en tratamientos en proceso vemos que venja y Roberto ya están en proceso y Carlos dice cliente ya ganado como pueden ver cada uno de estas etapas tiene un total que es la suma del potencial que se podría ganar aquí tal cual ustedes pueden verlo en esta forma con esta vista pues también pueden verlo de esta forma dependiendo como lo quieren ver a mí personalmente me gusta más esto cambian y les permite que se encamba en que eso se vuelve un drag and drop que es cerca de lo mejor ok eso es un nuevo cliente ya no responde algún mensaje o algo y manualmente lo podemos mover en engagement y se va moviendo conforme las diferentes etapas ok algo que quiero dejar en este un contacto puede tener múltiples oportunidades por ejemplo vamos a ver acá en el caso Roberto tiene un está en tratamiento en un proceso y a lo mejor tiene ahorita no sé está en tratamiento de un proceso de blanqueamiento pero el próximo mes ya tiene agenda una limpieza nos puede estar Roberto con tratamiento en en en esta etapa del pipeline y con cita agenda de aquí otra vez Roberto sin ningún problema que ahora un tip práctico un dueño de una clínica debería abrir esto cada mañana tomarse un café y en cinco minutos saber exactamente qué oportunidades en atención hoy. Por ejemplo, vemos que aquí en el caso María no asistió. Entonces, ¿y sabe que es un cliente potencial por 20.000 pesos? Entonces, ¿sabe que tiene que dar seguimiento a María para ver porque no asistió? Y, obviamente, lleguemos al punto de cliente ganado. Entonces, en momento, el CRM y el Pairland están listos. Ahora sabemos, ¿quiénes nuestros pacientes en qué tapa está cada uno, pero el pipeline está vacío si no llenamos ese embudo con pacientes nuevos. En la siguiente sección construimos lo que va a llenar pipeline que es el funnel, va a ser una landing page con calendario integrado que va a capturar estos leads y agendas decitas automáticamente, así que nos vemos en el siguiente video.
