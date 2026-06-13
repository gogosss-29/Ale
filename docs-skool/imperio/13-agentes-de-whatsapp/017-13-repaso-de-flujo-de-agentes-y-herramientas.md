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

## 🎙️ Transcripción

Muy bien. Vamos a pegar un último repaso a lo que ya tenemos creado, que es esto que les va a quedar a ustedes en la herramienta. Como ven, tenemos todo esto que ya lo vimos, todo el System Prompt. y demás, en settings no tenemos nada raro, está todo perfecto. En el modelo tenemos 4.1 mini con esta temperatura. ya lo llamamos recién, la memoria tenemos seleccionada la memoria simple que tenemos este id seleccionado como la llave así que puede ser esto puede ser un número de teléfono no hay problema y que tenemos acá 20 Ahora tenemos estas dos herramientas. Vamos a repasar un poco cada herramienta. Esta herramienta la tenemos seteada que nosotros le ponemos, por ejemplo, la table tool y nosotros acá seleccionamos qué es lo que hacemos. Si vamos a trabajar sobre un registro o vamos a trabajar sobre una base, si vamos a actualizar, buscar, obtener, borrar, crear entonces acá tenemos seteado de esta forma ¿qué es lo que hace esta herramienta? carga la descripción del vídeo negocio del usuario. Una vez que tenga suficiente información para describir el negocio del usuario, usar esta herramienta para cargar la información. Esto es lo que va a hacer. Ponemos acá, se va a la tabla clientes. ¿Qué es lo que hace esto? Ir acá, va a la tabla clientes. clientes, busca y actualiza sobre uno de estos que lo va a actualizar acá o acá. después acá que tenemos que seleccionar qué es lo que hace esto buscar la columna con la que va a encontrar a la persona, que en este caso es teléfono, va a entrar a buscarla, por el teléfono y a partir de ahí vas a ver a quién se la tiene que actualizar. y luego acá es esto que veíamos recién que escribe con inteligencia artificial la descripción del negocio No le ponemos un valor fijo, no le ponemos un valor de acá, de todo esto que tenemos y demás. No, le damos la libertad a la IA para que lo haga. que lo hacemos con este botón que vimos acá, entonces esto es todo lo que hace esta herramienta Y esta va a ser algo muy similar, pero lo único que lo va a hacer con soluciones, ¿sí? Es la misma herramienta, muy diferente. parecida tiene este diferente cambio y acá que seleccionamos otro campo en el table que es este que ven acá. acá. Sí. Entonces. Este es el funcionamiento del agente de IA. ¿Qué va a suceder? Va a recibir, según todo el prompt que tenemos acá, lo que va a hacer es Comprender el contexto y las necesidades del usuario. Identificar tareas repetitivas. Detectar oportunidades de automatización. Proponer un plan de acción. Guiar el con claridad y hacer las preguntas necesarias. Acá tenemos el objetivo que lo vimos recién y vamos a ver el flujo de trabajo que es lo que va a hacer acá 1, 2, 3, 4, 5, 6, 7 tiene estos pasos va de nuevo identifica la intención y el contexto del mensaje va a revisar si tiene información suficiente, si no tiene información suficiente, va a pedir más información, va a analizar algunos procesos, va a detectar oportunidades de automatización, va a diseñar una propuesta concreta y va a explicarle los beneficios. y bueno, ofrecer un próximo paso claro. Esto es lo que va a buscar hacer el agente de IA teniendo en cuenta esto que vimos recién del objetivo, una clave. cosa va a complementar mucho a la otra, por eso es que tal vez esto lo podríamos poner abajo, no hay ningún problema, pero bueno. Esto es lo que vamos a buscar, entonces con cada una de las herramientas, algo que sí se podría hacer, por ejemplo, acá, de detectar oportunidades. identificar esto, si la información recibida es suficiente. ¿Qué le podemos poner para mejorar el funcionamiento de la tool? Vamos acá y le Le ponemos, si es suficiente, usa. actualizado, descripción, negocio y sigue al siguiente paso. Bien, entonces acá que pasa, le empezamos a meter en el flujo de trabajo directamente las herramientas, que esto es muy importante. después de hacerlo. Y acá, destacar oportunidades de automatización con IA. Y acá, ¿qué le vamos a poner también? cuando detectes cuando detectes posibles soluciones Usa, actualizar, soluciones, negocio y siga el siguiente paso. Entonces acá tenemos de nuevo lo mismo, le estamos poniendo las herramientas. Esto es todo lo lo que va a hacer el agente de IA, va a charlar y va a buscar tener una descripción y va a buscar plantear soluciones. Vamos a ir ya. al último punto que son estos tres.
