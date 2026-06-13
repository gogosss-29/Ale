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

## 🎙️ Transcripción

Ahora sí vamos a meter no ya el lleno a la gente de ella que en este caso es Roberto que es una gente bastante simple vamos a ver primero si como que es lo que tiene lo que tiene prometiado también así como ponemos todos estos nodos si queremos agarrar poner una gente de ella lo ponemos acá y acá tenemos la gente de ella vamos a mostrar esto un poco como se armó para que quede bien claro nosotros ven que acá tenemos Manto de información tenemos el user message, tenemos todo el sí. message tenemos memoria tenemos un modelo tenemos tools si sobre esto vamos a ir uno por uno viendo, primero lo más importante vamos a dar a rar y esto que ven acá lo pasamos Vamos a definir vídeo. que es que no vaya a tener un chat directamente conectado esto que ven acá de chat trigger node es por si lo queremos probar de esta forma, así que podemos conectarlo acá y correr testeos, mandarlo mensaje. que o la como estás no va a contestar nada bueno tiene modelo ni nada pero bueno esto para eso es lo que está está este parámetro que se ve ahí, entonces hay que sacar esto y poner Define Below y acá como para que conteste tenemos que conectarlo vamos a conectarlo y acá le ponemos todo lo que trabajamos anteriormente que es el chat input, todo lo que vimos hasta recién era para poder armar el chat input, bien y ahí lo tenemos. Ahora, este es el mensaje, nada más. Vamos a ver el System Message, que parece que tenemos que poner Ad option y le ponemos System Message. Haga que tiene interesante esto. que yo le puedo poner expresiones. Entonces, si ven bien lo que es el curso de de noche en el deshacero, van a poder ver qué profesionales. Y que le podemos mostrar algunas cosas y sacar algunas otras cosas según lo que esté disponible. o según la persona puedo decir que por ejemplo si la persona tiene un negocio no sé si la persona es un un asesor que le conteste una forma si es de un cliente que le conteste de otra pero bueno para eso están las expresiones y no me quiero profundizar mucho ahí que no es el así que no, acá tenemos el system message, vamos a ponerle exactamente lo que le pusimos acá, copio todo. y le pedamos así ya tiene lo mismo, y acá como ven que pasa tenemos el sistema el prompt por un lado que es todo esto que vimos acá vamos a repasarlo un poco si en brown, constructor automóneo. de sesiones conía, rol, si como ven nosotros estamos usando almohadillas que es markdown todo este sistema de puntuación. con almodillas, con guiones, con estos asteriscos y demás se llama Markdown que se que va así. part down que permite que la ella pueda entender mucho mejor las cosas ahora vamos a ahorrar esto, primero le ponemos el rol, después vamos a ponerle un divisor que es, sexto y le vamos a dar un poco de contexto general sobre a qué personas está tendiendo o qué conversaciones va a tener estos dos son muy importantes, estos dos primeros espacios, casi siempre funcionan muy bien por lo de esta forma, acá tenemos un saludo inicia el que este saludo inicial lo podríamos poner abajo no hay problema porque también es muy importante si viene el saludo inicial es muy importante algo las cosas más importantes es el objetivo. Entonces, nosotros tenemos las tres cosas más importantes que es roll. Contexto y Objetivo. El saludo lo podemos poner acá o lo podemos poner abajo pero está bien y luego ya empezamos a ver un poco el el estilo, el tono, así que queremos que tenga, que tipo de conversaciones buscamos que tenga. que tipo de consejos que queremos quere en este caso y por otro lado también vamos a ver qué es lo que tiene que seguir, la ir a paso a paso, esta guía de trabajos, lo pueden encontrar como guía de trabajo, lo pueden, encontrar como SOP como flujo de acción, flujo de sí. Lo importante es que la ya pueda ver, y decir, este es la forma en la que yo trabajo, este es la forma en la que yo accióno, este es el proceso. de pensamiento. Como si fuera un flujo de trabajo, de primero a esto, después de hago esto, después de hago esto, bueno, es importantísimo que esté. Claro, para que tenga unas instrucciones de que hace el primero y que hace después. Luego tenemos algunas restricciones de temas permitidos. tenemos lo de las herramientas que lo vamos a ver, tenemos una breve descripción de las herramientas tenemos prohibiciones que esto muchas veces lo que se ve es que nosotros le empezamos a poner cosas porque comente los errores si de por ejemplo no sé si vemos que inventa datos, que invente información lo voy a poner en la sección de prohibido lo voy a poner en uno de estos. tenemos que tener mucho cuidado con todo este prompt y con esta parte también porque no siempre hay que darle Muchísima información, o empezar a cargarlo de un montón de prohibidos, por ejemplo, que es algo que se ve muy normalmente, no va a ser que, si os, y lo siga. Generalmente si el prompt te está andando malo no te está haciendo caso es porque está muy cargado hay que tratar de hacerlo contrario. no se es más, hay que tratar de descargar el prompt, que también en h8n desde cero tenemos una parte donde vemos bien bien bien, todo el prontéo y demás igual vamos a profundizar acá que estamos hablando de agentes y es súper importante entender el prontéo Cuando vemos que no funciona, el promedio que estamos haciendo, busquemos sacar la información. Busquemos darle por ahí otro tipo de tareas o, por ahí meter un subagente, también es algo que pueda servir, entonces nada, esto con esta parte y por último el formato de salida, de ¿Qué querido? Podemos que responda como queremos que estén las respuestas de la gente. Hay veces que queremos que lo dede de una forma estructurada, como para que escribir un shazon. a veces que queremos que lo de esta forma, esto determina muchísimo cómo va a contestar y qué va a hacer en la gente de ella. Bueno, ya tenemos el prompt user message y el system message todo esto con prompting vamos ahora a ver En el próximo vídeo, todo lo que es esto que ven acá, que estools, memorias y modelos.
