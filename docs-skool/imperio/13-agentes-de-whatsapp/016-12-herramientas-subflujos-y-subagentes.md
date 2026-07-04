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

## 🎙️ Transcripción

vamos a entrar ahora allá en la parte más importante que es las herramientas. Vamos a ver acá, tenemos esto que ven acá, que son herramientas o tools, como le quieran decir. Nosotros las podemos agregar, podemos agregar la cantidad que querramos. acá. Ahora, tenemos un montón de herramientas y realmente no hay un límite. lo que se puede hacer. ¿Por qué? ¿Por qué tenemos? Primero si queremos poner un Nacho de debe. Ok. Gracias. Si quiero poner un nodo de air table como lo que tenemos ahí, le puedo dar nodo de air table para vamos con las configuraciones. Y también algo muy importante, puedo ponerle código si quiero que GPL les vuelvo a ayudar a escribir audio y lo que para mí es más importante, lo más potente es esto, que yo lo que puedo una herramienta que sea llamar a un escenario. Esto que significa que yo puedo crear un, un escenario como yo quiera usando todo el potencial de N8N y dárselo como una herramienta. a la gente para que la gente pueda mandar la información vamos con ejemplo vamos a ponerle a ver ¿Qué puede ser? Un buscar propiedades en toco, por ejemplo. Y acá, si yo voy a desenario, tengo algunas cosas importantes todo esto que ven no lo están relevantes lo que lo que hace la herramienta en sí, sino la complejidad que ven que tiene, lo que devuelve, hay unas gente mentida en el medio. pero que acá el trigger es este y acá yo le digo todo lo que necesito obtener el workflow padre, se llama, o del agente de ella en este caso, entonces si yo como acá y tengo todo esto, Acá me va a aparecer la información que puedo pedirle a la gente, de ella que le mande al workflow. ¡Pavono! Yo tengo acá esto. Tengo esto como una herramienta. La herramienta necesita cierta, vamos. Ahora nada, tengo esta herramienta ahí que se ve, esta herramienta que es este workflow. ya me marca que necesita cierta información. Entonces, yo lo que tengo que hacer es desde la gente de ella Es decirle la información que necesita y poder pasarle al workflow para que funcione. Que eso lo determinó acá. Entonces acá yo le puedo poner que le mandé el remote jota id por ejemplo que lo puedo traer directamente desde acá lo puedo seleccionar ahí y por ejemplo si yo quiero usarla a darle un no ser peyer el presupuesto, lo que sea Puedo poner acá para que el modelo de IA escriba lo que le parezca, entonces Acá yo le doy un prompt de poner el presupuesto para invertir que tiene la persona. y acá esto es un valor que se va a generar con la ira, entonces eso está muy bueno poder entenderle flexibilizado. no los vamos a meter en esto acá ahora si quería mostrar eso para que sepan que se puede llamar a otros workflows y cómo se hace y qué cosas hay que tener en cuenta y demás y también algo muy importante que esto va para cualquier herramienta que, que acá tenemos una descripción, que esta descripción la ella lo va a tomar como pero un teo muy directo sobre cuando usar una herramienta y cuando, no vamos a vamos a ir al caso que ya agarramos ahora agresada escripción de negocio yo le pongo la descripción para que la ia pueda saber para que sirve ese herramienta específico. A la ia no le importa lo que haya dentro de la herramienta. La hía lo único que toma es, toma el nombre que tiene la herramienta, toma los parámetros que necesitan, darle a la herramienta, que es esto que veíamos acá abajo, si necesita algo, puedo el generarlo y el y todo el promptio de bueno esta descripción nombre y lo que vimos acá acá por nombre y las cosas que se necesiten ahora la ia no es sin importar la herramienta que sea sin importar si es un workflow, sin importar si es una herramienta simple, sin importar si es un agente de ella, lo que va a hacer es, enviar la información y esperar una respuesta. Eso es todo lo que va a hacer, entonces eso es importante que se entienda. Por último, otra herramienta muy potente acá, es poder poner. un agente de ella. Entonces acá lo que tenemos es una gente de ella que tiene cómo arramienta otro subagente que este subagente se Comunica, le tiene también un sistema prompt, como vimos acá, un sistema message, acá tenemos el mensaje. Podemos dar un modelo, podemos conectar si queremos al mismo modelo, creo, vamos a dar, si me deja, si lo puedo conectar al mismo modelo. lo puedo conectar a la misma memoria, si quiero, si que esto no es recomendable porque da errores, de cara a la memoria, de poder herramientas, de poder otros subagentes y quiero para que usé como herramienta. entonces acá en donde se empieza a poner bastante más lindo todo lo que se puede hacer con una gente de ella ahora ¿Qué pasa? con esto acá. Nosotros, a este agente, lo tenemos que tratar como una herramienta. Si yo le quiero poner, por ejemplo, asesor de m. presas grandes. Y choque alipongo, que le doy bueno. Usa. esta herramienta subagente para cuando la persona que estés con la que estés hablando. empresa masor a sien empleados por ejemplo Entonces, acá como ven es lo mismo. Yo le puedo cargar el prompo, podemos avanzar sobre esto y demás, pero este, Lo único que va a tomar es que esto es una tool, nada más, le podemos dar que es un suagente que sirve acá, yo también tengo que decir un poco. con esta parte de herramientas disponibles, tengo que marcar ahora el por ejemplo acessor de empresas grandes y en la descripción usar cuando la empresa sea mayoras y empleados lo que sea todo esto lo lo van vamos a poner y se puede y va a interpretarlo bien a la gente de ella, pero de nuevo volvimos a lo mismo a éste que es el que le va con testar a la persona. ¿Qué no importa? Solamente lo que le da y lo que le devuelve. Nada más. Pues es que es importante probar ver para acá, En el varían las herramientas, varían los tubos, varían los subagentes, varían todo. Pero es importante que se entienda la teoría y que es lo que es lo que es lo que lo que funcionó bien vamos a borrar todo esto y pegar ya un pequeño repaso a lo que tenemos aquí Gracias.
