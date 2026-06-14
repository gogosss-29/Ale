# 📖 Introducción

> Ruta: Vibe-Coding › 📖 Introducción

**🎬 Vídeo (11.3 min):** https://youtu.be/y_tNxHy0aiE

**📎 Recursos:**
- Dominando la IA con Antigravity

---

En este módulo damos la bienvenida al curso de** Antigravity** y te mostramos cómo empezar de la forma más simple y práctica posible.

Este es uno de los cursos más estratégicos y accionables que hemos lanzado en Imperio Digital. No vas a aprender teoría suelta. Vas a construir una **aplicación real** que te ayuda a diagnosticar negocios, detectar oportunidades de automatización con IA y convertir eso en cotizaciones y ventas.

La app que vamos a crear está pensada para adaptarse al **99% de los casos de uso** de freelancers, agencias y profesionales que venden automatizaciones o soluciones con n8n e IA.

![Antigravity Info.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/f1d2c5f4e78e4bd6b6ee976cf1b15d0527a61922a6d6439c816f6093552df2ec-md.png)

### ¿Para quién es este curso?

Este curso es para ti si:

- Eres freelancer o agencia de automatización.
- Usas o quieres usar n8n de forma profesional.
- Quieres vender automatizaciones con más claridad y mejores precios.
- Necesitas una herramienta para diagnosticar clientes y cerrar proyectos más rápido.
- No quieres depender solo de llamadas largas o documentos manuales.

No necesitas ser desarrollador senior.  
Sí necesitas criterio de negocio y ganas de construir algo útil.

### ¿Qué vas a aprender?

Durante el curso aprenderás a:

- Entender y usar Antigravity como framework de desarrollo.
- Diseñar un MVP guiado por agentes de IA.
- Construir un flujo de diagnóstico de automatización orientado a negocio.
- Adaptar recomendaciones y precios según país y poder adquisitivo.
- Guardar diagnósticos, clientes, cotizaciones y seguimientos.
- Desplegar una app funcional con frontend, backend y base de datos.

Al final del curso tendrás una **app operativa**, lista para usar con tus clientes o dentro de tu agencia.

### Pero no me hagas caso solo a mi, checa este video 👇🏼

[https://www.loom.com/share/7a686a219adf48c09bd7157fe6fe81db](https://www.loom.com/share/7a686a219adf48c09bd7157fe6fe81db)

### Tech stack que vamos a usar

Todo el stack es moderno, probado y **100% funcional**.

Usaremos:

- [Antigravity](https://antigravity.google/)
- [Google AI Studio](https://aistudio.google.com/)
- [GitHub](https://github.com/)
- [Supabase](https://supabase.com/)
- [Vercel](https://vercel.com/)

Importante.  
No necesitas pagar nada para seguir el curso.  
Google exige tener billing activo en la cuenta, aunque el consumo sea cero. Si no activas billing, no podrás avanzar, pero **no implica un gasto real**.

### Cuentas que necesitas crear antes de avanzar

Antes de comenzar, asegúrate de tener:

- Una cuenta de Google con billing activo.
- Una cuenta en GitHub.
- Una cuenta en Supabase.
- Una cuenta en Vercel.

Todas pueden crearse gratuitamente.

### Cómo está pensado el curso

El curso está diseñado incluso para personas que **nunca han usado Antigravity**.

Avanzaremos paso a paso:

1. Entendiendo la lógica.
2. Construyendo páginas claras.
3. Definiendo qué sí hace el MVP y qué no.
4. Refinando el resultado con IA.

No vamos a ejecutar automatizaciones reales ni conectar n8n todavía.  
Este curso se enfoca en **diseño, diagnóstico y producto**, que es donde la mayoría falla.

Ahora sí.  
Prepárate un café o un mate.

En los próximos módulos vas a construir una app que no solo se ve bien, sino que **te ayuda a cerrar proyectos reales**.

## 🎙️ Transcripción

Hola imperiales, ¿cómo están? Estoy muy emocionado de este hacer el primer curso. Vamos a hablar acerca de lo que es pipe coding en este en este curso. Les voy a enseñar cómo poder empezar con una idea, desde que ustedes tengan la idea de la aplicación que quieran hacer hasta desarrollar la idea y hacer el display final para tener ya su aplicación funcionando. Nos vamos a enfocar en web apps, aplicaciones web. Y en este curso vamos a ver cómo crear una aplicación desde cero. Ahorita les voy a comentar en qué nos vamos a estar enfocando, pero antes de eso me gustaría decirles o explicarles qué es VIPE coding. Okay, Vipe Coding es eh un término relativamente nuevo. empezó en febrero del 2025, como podemos ver aquí, y básicamente significa eh es la práctica del desarrollo de software, donde la inteligencia artificial le escribe a la mayor parte del código basado en instrucciones y lenguaje natural, o sea, los famosos promps del usuario donde nosotros le decimos, necesito hacer una aplicación que haga esto, esto, esto, que tenga esas funcionalidades con estos menús, etcétera, ¿no? ¿Qué es lo que priorizamos? la velocidad, la experimentación y la vibra o la intuición. Por eso se llama vibe coding, ¿no? No dejamos la perfección de lado. Eh, nos olvidamos de que el código existe, nosotros hablamos con lenguaje natural y me gustará que tenga esto y me gustará que brille y que cuando pases el mouse se ponga de este color. Eso lo que es el B coding, ¿no? Las tendencias actuales, eh, honestamente está desplazando la codificación manual, inclusive la gente que sí sabe de código, los desarrolladores están integrando herramientas de intigenar todo lo que son sus desarrollos. Esto también le está permitiendo a founders o a personas no técnicas poder trabajar con sus MVPs y poder sacar lo que es literal sus eh sus ideas para poder validarlas. Y está siguiendo una filosofía que es crea primero y refina después. Eh, en este caso nosotros vamos a utilizar Antigravity, que Antigravity tiene obviamente al ser de Google tiene integrado lo que es Gemini 3.0 Pro, obviamente el 3.0 Flash. También tiene integrado Cloud que vamos a ocupar un poco el Opus 4.5 que es el último que ha salido. Y eh también tiene modelos locales por si quieres utilizar eh modelos que corren localmente en tu computadora. No los vamos a ocupar en este caso porque son bastante limitados y se trata de que sea un agente orquestador. Básicamente es la colaboración humana entre IA. Tú le vas pidiendo cosas y antigravity orquesta, diferentes agentes que van trabajando por ti, van haciendo todos los request que tú le vayas pidiendo. ¿Okay? Vamos a utilizar también Google AI Studio. Google I Studio es una plataforma que, como podemos ver aquí donde se podemos eh hacer un modo chat, podemos hablar y pedirle que haga unas cosas muy parecido a Gemini, pero también podemos entrar en modo build donde ya le podemos eh pedir que nos cree aplicaciones web con el lenguaje, con el idioma que nosotros queramos, reangular con lenguaje, usando nosotros lenguaje natural, modo stream en el que podemos hablar, interactuar con voz o inclusive con video. Y también vamos a poder generar imágenes con Banana Pro, vamos a poder generar vídeos con BO3.1, BO3.0, vamos a poder exportar el código y también vamos a utilizar Gitbook para control de versiones. Vamos a subir nuestro código a Gitbook, que ahorita vamos a ver cuando les hable acerca del tex tag, qué es lo que podemos hacer y cuáles son las diferentes herramientas que vamos a utilizar. ¿Okay? Entonces, como les comentaba, vamos a estar utilizando Antigravity, ¿okay? Vamos a descargar Antigravity, se lo vamos a ver en el siguiente capítulo del curso. Y pero antes de eso quiero hablarles un poquito específicamente ahora de Antigravity. ¿Qué es Antigravity? Antigravity es un framework, básicamente es un eh una interfaz, digamos, donde tenemos eh todo lo que vamos a estar trabajando. ¿Okay? Eh, podemos construir aquí las los diferentes agentes de inteligencia artificial como núcleo de desarrollo. Quiero aclarar que esto no reemplaza el código, simplemente se encarga de acelerar la estructura y lo vuelve iterativo. No es una herramienta para improvisar, no es para que tú llegues a Antigravity y le digas, "Necesito crear una aplicación o necesito que hagas esto." Antigravity y vamos a llegar ya con todo la estructura hecha ya con todo hecho y y listo. Okay. ¿Cómo funciona Antigravity? Hablando de alto nivel, eh, Antigravity, como les comentaba, es un orquestador. Tú tienes diferentes agentes que les puedes pedir que hagan de todo. puedes decir, eh, ve y analiza este código que ya te pasé o necesito que vayas y que investigues en estos sitios esta información o y al mismo tiempo le pides a otra gente que te genere tu RM file o que te genere un prompt para que tú utilices dentro de un skill o una función que le vayas a pedir a tu agente directamente. también te permite hacer como un deep research, hacer investigaciones más profundas, puedes hacer análisis de mercado, puedes hacer gráficas, puedes pedirle que te genere un documento donde se va a ver cuál es el paso a paso, pues hablar con él directamente y pedirle que lo haga o tienes el modo planificación para hablar y pedirle que te haga algunas cosas. Cuando instalemos Antigravity, ahorita lo vamos a ver. Tú puedes configurarlo de diferentes maneras. Tú puedes decirle, "Sugéreme, pero no hagas ningún cambio, yo voy a hacer todo." O puedes decir, "Sugireme, yo te autorizo qué cambios puedes hacer." O, básicamente te doy acceso libre y tú haz todo lo que tengas que hacer. A mí no me preguntes nada porque yo no sé nada. Simplemente dime cuando ya esté esté listo. Eh, aunque no conozcas mucho de programación de código, no te sugiero que utilices esta última opción. Siempre es mejor que te diga, "Mira, voy a hacer esto." Y tú veas más o menos igual, aunque no tienas el código, pero que veas qué es lo que va a hacer. Tú decirle, "Okay, si hazlo o no hazlo." O si no te queda claro, preguntarle, "A ver, ¿por qué lo vas a hacer?" y ya te aseguraste que si haces esto no vas a afectar otra cosa. Así es como a mí me gusta utilizarlo. Eh, en Antigravity tú puedes utilizar diferentes eh lenguajes, digamos, dentro de ese de ese framework y puedes llamar librerías, utilizar diferentes textor de de Antigravity. Okay. ¿Qué vamos a usar nosotros? Bueno, antes de eso, ¿para qué sí es antigravity? Antigravity es bueno para MVPs y para productos internos, ¿okay? cuando no les recomiendo utilizar antigravity, cuando sean eh software o plataformas para escalar o para llevar a producción a clientes externos, porque cuando les piden que haga cierta funcionalidad o ciertos cambios en un módulo, ahí es donde se van a meter en una situación que en realidad no entiende cómo funciona el código. Entonces, para cuestiones que ustedes tengan una idea en su cabeza, quieren llevarlo a validar, no saben si es algo que la gente va a pagar por eso o ustedes mismos ustedes quieren que era una app para ustedes, utilicen antigravity. De lo contrario, yo les sugeriría que se vayan con un desarrollador y que alguien le salga el el código. Esto solamente es para MVPs, productos internos. Eh, no dudo que inclusive este año salga algo más o inclusive antigravity evolucione al punto de que ya puedas llevarlo a una experiencia completa y hacer un un salir a producción y tener cientos de usuarios utilizando tu herramienta. ¿Okay? Cabo aclarar que antigravity, perdón, no es magia. Okay, requiere que sepas qué es lo que vas a construir, requiere que tengas un criterio técnico mínimo, por lo menos que sepas qué es lo que estás haciendo, ¿no? Nada más darle siguiente siguiente click. Tienes que leer, tienes que tomar tu tiempo para hacer buenos proms, entender la documentación, qué es lo que está pasando, etcétera. Y por lo mismo, una regla clave es si haces un mal promp, vas a tener un muy mal resultado, ¿okay? Tú tienes que desarrollar la idea, tienes que saber qué es lo que quieres hacer para que la la I en realidad te entienda y pueda hacer todo eso por ti. Vamos a hablar acerca del text. Okay. Eh, algo que quiero aclarar para este curso, todas las herramientas que vamos a utilizar tiene su versión gratuita y su versión de pago. Todo lo que te voy a enseñar lo vas a poder hacer con la versión gratuita. No tienes que pagar absolutamente nada. Sin embargo, es importante aclarar que en Google Cloud te va a pedir que actives tu un billing account o que tengas un billing account. No tienes que meterle fondos, no tienes que meterle dinero, pero si tienes que meter una tarjeta de crédito y configurar tu billin account para que puedas usar las AP keys de Gemini en las diferentes etapas que vamos a estar eh utilizando. Entonces, ahora sí hablemos del text. Vamos a usar Antigravity como lo como lo mencioné. Aquí tenemos a Antigravity. Lo vamos a descargar en el siguiente video. Ahorita no. Vamos a utilizar también Google AI Studio donde vamos a empezar con la maquetación de nuestro proyecto. Aquí es donde vamos a empezar a darle las ideas, vamos a empezar a decirle cómo queremos que se vea visualmente. Esto nos va a generar el primer código para de aquí llevarnos a antigo. El código lo vamos a subir a GitHub. Entonces tienen que crear su cuenta de Gitop si no la tienen. Como les comento, no tiene ningún costo, puede iniciar con la cuenta gratuita. Vamos a utilizar Supas para la base de datos y para lo que son el Oout, que básicamente es para poder autenticar usuarios y también para las ed functions, que básicamente son funciones que tú puedes crear para que eh hagas cosas, digamos que si fuera como una picol. Y vamos a utilizar Dribble para lo que es la parte de la interfaz gráfica. Dribble es una plataforma, es una página web que a mí me gusta utilizar mucho. Por ejemplo, si nos vamos para acá donde dice dashboard y nos es como para darte una idea de diseño. ¿Sabes que yo quiero que mi app se vea así? Me gusta este diseño, me gusta más o menos como tiene estos eh cuadrados, está todo pegado, los colores que utiliza. Entonces, yo hago una captura de pantalla, lo doy a Google Studio y le digo, "Quiero que mi aplicación se vea así." Entonces, para eso vamos a utilizar Del para inspirarnos. Y por último, Versel para hacer el deploy, igual gratuito. Desde aquí vamos a poder hacer un deploy. Subimos nuestro código una vez que lo hayamos finalizado con Antigravity. y va a estar listo para que lo utilicemos en la web, lo compartamos y empecemos a generar esas cotizaciones y entender qué podemos automatizar y cómo podemos ayudar a nuestros clientes. Te veo en el próximo
