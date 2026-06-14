# ⭐ BONUS: Progressive Web App

> Ruta: Vibe-Coding › ⭐ BONUS: Progressive Web App

**🎬 Vídeo (8.9 min):** https://youtu.be/58zCxbrZxLU

---

## (Bonus). Convertir el MVP en una PWA (Progressive Web App)

Este módulo es **bonus**. No es obligatorio para el MVP, pero sí muy útil para:

- Experiencia mobile-first
- Uso tipo “app real”
- Demostrar madurez técnica del proyecto

## 1. Qué es una PWA y por qué importa

Una **Progressive Web App** es una aplicación web que:

- Se instala en el teléfono como una app
- Oculta la barra del navegador
- Se abre en pantalla completa
- Funciona con ícono propio
- Comparte UX muy similar a una app nativa

No reemplaza una app nativa, pero para MVPs, dashboards internos y herramientas B2B es **más que suficiente**.

![PWA.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0a567f72d6994d6aaf274dbb87be71fd195d58140c5240799520ed853870d174.png)

## 2. Análisis del stack actual

Antes de implementar nada, se hace una revisión completa del stack:

- React 19
- React Router
- TypeScript
- Vite
- Tailwind
- Google Fonts
- Supabase
- n8n

Conclusión del análisis:  
El stack **es compatible con PWA** sin cambios estructurales grandes.

## 3. Qué faltaba para ser PWA

El reporte identifica claramente lo que no estaba:

- Web App Manifest
- Íconos PWA (varios tamaños)
- Configuración mobile-first
- HTTPS (ya resuelto por Vercel)
- Ajustes de experiencia offline (limitada)

Importante:  
Algunas funciones **no funcionan offline** por definición:

- Gemini
- n8n
- Envío de correos
- Integraciones externas

Eso es normal y aceptable.

## 4. Implementación de la PWA

Se le pide a Antigravity que:

- Agregue manifest.json
- Configure íconos
- Ajuste meta tags
- Optimice el layout para mobile-first
- Prepare la app para instalación como PWA

Resultado:  
La app ya cumple criterios técnicos de PWA.

## 5. Buenas prácticas antes de publicar el repo

Antes de hacer público el repositorio:

- Eliminar credenciales y API keys
- Documentar variables de entorno necesarias
- Explicar claramente cómo correr el proyecto
- Indicar pasos para probar la PWA

Esto se refleja directamente en el **README**.

## 6. Commit final del bonus

Se realiza un commit específico con:

- Conversión a PWA
- Ajustes mobile-first
- Actualización del README
- Instrucciones claras para clonar y configurar

Esto deja el repositorio listo para:

- Clonación pública
- Uso educativo
- Extensión por terceros

## 7. Redeploy a Vercel

Después del commit:

- Vercel detecta cambios automáticamente
- Se ejecuta un nuevo build
- La versión PWA queda disponible en producción

No hay pasos adicionales si Vercel ya estaba conectado al repo.

## 8. Instalación en móvil (prueba real)

Ejemplo en iPhone:

1. Abrir la URL en **Safari**
2. Menú . “Agregar a inicio”
3. Confirmar
4. Abrir la app desde el ícono

Resultado:

- App en pantalla completa
- Sin barra del navegador
- Navegación fluida
- Dashboard usable en mobile

## Resultado final del bonus

Al terminar este módulo tienes:

- Un MVP convertido en PWA
- App instalable en móvil
- UX tipo app nativa
- Repo público bien documentado
- Deploy actualizado en Vercel

Este bonus no es para “lucirse”. Es para entender hasta dónde puede llegar un MVP bien construido sin complicarse con apps nativas.

## 🎙️ Transcripción

que ya había acabado de grabar, pero decidí grabar este último módulo como bonus, como lo dice el nombre, eh, porque se me ocurrió que sería bueno enseñarles un poquito acerca de PA. Eh, ¿qué es PWA? Como dice aquí su nombre, espero lo alcanzan a leer, es un Progressive Web App. Básicamente es como si fuera una aplicación móvil que puedes instalar en tu iPhone, en tu Android y lo cual te oculta, digamos, la barra de navegación. y te permite hacer eh tener una experiencia, digamos, un poco más limpia. Entonces, les enseño un poco qué fue lo que hice. Le dije tal cual a la IA, next que investigues cómo podemos convertir este MVP en tener una versión uno que sea mobile first para que puedas hacer una versión PWA. Revisa todas las librerías, tecnologías que estamos utilizando y tenemos reporte que se pueda de reporte de qué se puede, qué no se puede y qué tenemos que actualizar. Okay, hizo la investigación y me generó este reporte. Entonces, este es el estado actual. Nuestro stack tecnológico es React 19.2.3, el React Router DOM, TypeScript, Bill Tool con Vite, eh Styling con Tailwind, Google Fonts, Backend Services con Supabase, N8N, Components y aquí me me dice todo, ¿no? Entonces, ¿qué tenemos actualmente? ¿Qué nos hace falta? El manifiesto, nos va a hacer falta el icono, nos va a hacer falta eh https y obviamente nos dice, ¿qué es lo que tienes que tomar en cuenta? Si lo instalamos como PWA y el equipo donde lo instalemos pues no tiene internet, pues hay muchas cosas que no vamos a poder utilizar evidentemente no como la conexión a N8N o generar el correo con la con Gemini que estamos haciendo, mandar los correos, todo ese pues no va a funcionar, pero obviamente todo eso lo es es obvio. Entonces aquí está toda la investigación. lo que dijo. Recuerden que les voy a pasar este repositorio para que lo puedan clonear si quieren, puedan leer, puedan ver todo. Entonces, ya aquí me dice todo lo que tenemos que hacer y dice que está listo para empezar. Entonces, voy a agarrar este chat y le voy a decir, "Okay, me parece muy bien toda la investigación que hiciste. Estamos listos. ni quiero que eh implementes todo lo necesario para tener esta aplicación PWA y utilizan nanovanana Pro para generar la imagen que necesitamos. Okay, vamos a darle enviar. Okay, al parecer va a empezar con la imagen. Igual voy a intentar mantener lo más cortito posible, así que le pondré pausa y regreso. Okay, se tardó más o menos que unos 5 minutos y me dice, "Listo, he implementado todo. Configuración de PA, identidad visual con los iconos, optimización mobile first, experiencia offline. Siguiente. Entonces, me dice, "¿Te gustaría que probemos bien localmente o prefieres que rimemos alguna parte en específica del diseño mobile?" Entonces, antes de de probar, le voy a pedir eh lo siguiente. Okay, perfecto. Donisto que hagas un commit dejando las notas que lo convertiste a PWA y eh también asegúrate, por favor, que en el Ritmi esté las instrucciones para que cualquier persona que quiera clonar este repositorio pueda configurar todo. Ten en cuenta que volveré este repositorio público en GitHCOP para que la gente lo pueda clonar, por lo cual evidentemente borraremos las credenciales, las APIs de las variables de entorno y cada uno va a tener que poner sus propias credenciales. Así que quiero que dejes eso claro en el RMI para que sepan a dónde ir y qué credenciales son las que necesitan. Actualiza eso y hace el commit para que yo pueda probar el PWA en mi dispositivo móvil. Le damos enviar y ahorita me debería cambiar este ritmi. Vamos a ver que sí. Entonces va a analizar mi local, que son las variables de entorno que les comentaba, y va a actualizar mi RM y al final tendría que hacer el commit githup. Okay, como pueden ver, ya está haciendo cambios en el RMI. Está diciendo clonar, configurar, archivo local, tienes que cambiar las carenciales. Perfecto. Ahorita vamos a abrir GitHop para ver los cambios. Y aquí me está pidiendo autorización para hacer el comit. Le voy a ver que sí. Y ya está checando, me está confirmando que hice todos los cambios, el ritmo, el ritm, perdón, todo. Entonces, vámonos a Ah, sí, bueno, dice que hay algo más que quiere hacer. Sí, es importante. Necesito que hagas el redeploy en Versel para poder ver los cambios actualizados. Vamos a hacer redeploy en Versel. Recuerden que ya conectamos el MCP de Versel y ahorita nos vamos a ir al Gitcop, nos vamos a ir a Verel para que veamos últimas actualizaciones que hicimos todo 100% desde Antigravity. Vámonos para allá. Okay, entonces ya estamos aquí en nuestro Githup. Aquí podemos ver que el último commit va a ser 5 minutos, que es la de conversión total APwa y mobile first. Y si nos vamos a nuestro código y bajamos al Ritmi, aquí podemos ver las las instrucciones que ustedes van a seguir si quieren clonarlo y lo van a tener que poner sus variables de entorno. Ejecutar, probar PWA. Nos vamos a Ver y vemos que fue hace 2 minutos y con este source, este es el último comit que hicimos. Así que por último, déjenme ver si les puedo enseñar en mi computadora cómo se en el celular. para hacer la prueba. Entonces vamos a abrir la app, copiamos y les stream. Déjenme preparar todo en el celular. Okay, entonces ya estamos en el celular. Ponemos aquí el domain. Es es Safari. Es importante que estás en iPhone, lo hagas desde Safari. Le vamos a dar aquí y vamos a buscar el opción, la opción que agregar a inicio. Vamos a darle a agregar y listo. Vámonos a nuestro inicio. Aquí tenemos con el logotipo que nosotros escogimos. Y si abrimos la appun se fijan, es como si fuera una app. No tiene tal cual el navegador ni nada. Y vamos a iniciar sesión nada más para comprobar. Vamos iniciar sesión. ver si tengo algo mal escrito. Okay. Al una razón no me dejaba iniciar sesión. Ahí está el error como de la configuración a usarlo el mirror de mi celular en la computadora. Está ya está la aplicación con menú completamente usable en mobile. Perfecto. Entonces aquí vamos a dejar el video bonus y espero que les haya servido de cómo convertirlo a PA. M.
