# 🚀 Auth con Supabase y Deploy a Vercel

> Ruta: Vibe-Coding › 🚀 Auth con Supabase y Deploy a Vercel

**🎬 Vídeo (24.1 min):** https://youtu.be/hN6KA80wNW8

---

## Parte VIII. Auth con Supabase y Deploy a Vercel (cierre del curso)

Cerrar el MVP como “producto real”. En esta lección hacemos dos cosas que separan un prototipo de una app usable:

1. **Autenticación con Supabase** (signup, login y verificación por email).
2. **Deploy a Vercel** (build de producción, variables de entorno y verificación final).

## 1. Recap rápido del MVP antes del cierre

Al inicio del video confirmamos que el MVP ya funciona en local:

- Dashboard operativo.
- Diagnósticos y reportes generados.
- Cotizaciones, clientes y envío de correos.
- Flujo híbrido con n8n funcionando.

Luego detectamos el hueco obvio: **no hay sign-up/sign-in**, entonces cualquiera podría entrar. Eso no es aceptable si lo vas a usar con clientes o equipo.

## 2. Decisión clave. Supabase Auth vs BetterAuth

Aquí no nos complicamos por “lo popular”. Elegimos por encaje con el stack:

- Ya usamos Supabase.
- Supabase tiene Auth integrado.
- Soporta verificación por correo sin montar infraestructura extra.

Resultado: **Supabase Auth gana por simplicidad y velocidad para MVP**.

## 3. Qué se implementa en Auth (lo mínimo correcto)

En esta lección se integra:

- Pantalla de **Sign up**
- Pantalla de **Sign in**
- Flujo de **verificación por email** obligatorio antes de poder iniciar sesión
- Redirección correcta después de login
- Protección básica de rutas (si no hay sesión, no entras)

## 4. Configuración clave dentro de Supabase

Paso importante que mucha gente se salta:

En Supabase, dentro del proyecto:

- Authentication . Providers . Email
- Activar “**Confirm email**” (confirmación de correo después de registrarse)

También se menciona:

- Puedes personalizar templates de email después.
- Para el MVP no lo hacemos perfecto. Solo funcional.

## 5. Prueba real del signup y verificación

La prueba correcta es:

1. Registrarte con email + password
2. Ver que te llegue el correo
3. Confirmar el email
4. Volver al sitio y hacer login
5. Confirmar que ya te deja entrar al panel

Esto valida que el flujo no es “fake UI”. Es Auth real.

## 6. Deploy a Vercel. Qué importa de verdad

Aquí lo que importa no es el botón de deploy. Es el checklist mental:

- Código actualizado y empujado a GitHub
- Build correcto en producción
- Variables de entorno configuradas en Vercel
- Redeploy después de setear variables
- Confirmar que Auth funciona en producción, no solo en local

## 7. Truquito práctico. Variables de entorno

En local ya tienes `.env.local`. En producción no existe.

En Vercel:

- Settings . Environment Variables
- Importar variables (si lo haces manual, te equivocas más)
- Guardar y hacer **Redeploy**

Si no haces esto, la app “carga” pero no funciona. Especialmente Auth y Supabase.

## 8. MCP de Vercel. Realidad vs expectativa

Se intenta que Vercel deploy “solo” usando MCP y CLI.  
La realidad práctica del video:

- A veces pide login, tokens o device auth.
- Si te frustra, haces deploy manual conectando GitHub, es igual de válido para MVP.

La lección: **no te cases con el camino fancy**. Termina el deploy.

## 9. Verificación final en producción

Checklist de cierre en el dominio de Vercel:

- Login funciona
- Dashboard carga
- Diagnósticos funcionan
- Envío de correo (n8n + Gmail) funciona
- Todo sin errores visibles

Con eso ya puedes compartir el link, aunque sea con dominio temporal.

Al final debes tener:

- App con Auth real (signup, login, email verification).
- Deploy funcional en Vercel con variables de entorno correctas.
- MVP usable desde una URL pública.
- Flujo de n8n validado desde producción.

### Te dejo el repositorio de Github por si quieres clonarlo y testarlo, solo recuerda que tienes que cambiar tu variables de entorno.

[https://github.com/agenciainsigniaia-oss/Automation-Opportunity-Finder..git](https://github.com/agenciainsigniaia-oss/Automation-Opportunity-Finder..git)

## 🎙️ Transcripción

Okay, vamos a recapitular dónde vamos. Tenemos ya el deploy local, ¿okay? Tenemos nuestro panel, podemos generar nuevos diagnósticos, podemos ver aquí los reportes generados, aquí tenemos las cotizaciones enviadas y tenemos nuestros clientes. Ahorita que lo estaba analizando, me di cuenta que no tenemos un una opción de crear una cuenta y iniciarse así. Entonces creo que no está definido el MVP, pero me parece que es importante incluirlo en esta serie de videos. Así que vámonos a Antigravity para acá. Vamos a ver cuál fue el último chat que estuvimos. [resoplido] com profesional. Perfecto. Okay, vamos a que sí que sea un planning corruping Perfecto. Ya hice todas las pruebas, me parece que todo está funcionando como debería, pero me acabo de dar cuenta que no tenemos un sign up sign in con autentificación. Sé que no está en el MVP, pero lo quiero integrar. Verifica cuál es la mejor forma, si es utilizando directamente Supace o Better Out. Y también quiero que cuando se cree la cuenta tenga que ser verificada eh vía correo antes de poder iniciar sesión. Supas contra Better Out. Better Outificación open source medio popular en el mundo del VING. Entonces, vamos a ver qué es lo que nos recomienda directamente. Eh, yo decí antigravity, pero lo correcto sería decir eh clock. Entonces, le voy a poner pausa mientras hace todo el proceso porque igual cuando utilice planning y modo thinking va a tardar un poquito más. Entonces, le pongo pausa y regreso. Muy bien, ya terminó y vamos a leer la documentación que me generó. Okay. Autentificación. Ah, plan de implementación. Agregaricación de usuarios con verificación por correo electrónico utilizando supace out. ¿Por qué? ¿Por qué suabase? Dice que ya usamos primer verification bu in complejidad baja, mantenimiento gestionado, complejidad media alta, mantenimiento self foster y verificación está disponible pero no está ya built in y requiere back por integración activa con nuestra base. Okay. Abrir confirmar email, personalizar email templates, configurar URL de redirección y dominio de producción. Componentes, eh, okay. Login, sign up, verify, provider. Okay, va a ser un test para ver que esté funcionando. Los va su nombre en el sidewar después de loguearse o solo el email. Nota el email verificar las cantidades por efectos para después personalizarlas después en el das. Okay, vamos a darle proceder y que implemente el plan y ahorita lo responda duda. Va a entrar en modo ejecución y va a empezar a implementar todo. Entonces, voy a poner pausa igual para no hacer el video largo y ahorita regreso. Okay, no se tardó tanto, será unos 5 minutos. Eh, va a ser ahorita las pruebas. Okay, bienvenido de nuevo. Iniciar sesión. Okay, dice que está mi input. Confirmar. Vuelta. Okay, voy a entrar la cuenta. Vamos a ver qué nos dice. Campos estados de pantalla available. Okay, sigue analizándolo, está creando el walkt, preparando el commit y vamos a ver qué nos dice. Lo más probable es que nos pida que creemos un usuario ahorita y que robemos. Vamos a verlo. Aceptar. Y ahorita vamos a ver qué acabo haciendo con esto. Está haciendo un push. Vámonos a mientras termina aquí. Vámonos a Gincop. Vamos a ver qué hizo. Sí, sí tenemos el commit correcto. Justo ahora. Muy bien. Perfecto. Okay. Entonces, a ver qué nos dicen. Okay. Una acción requerida das autenticación providers email y asegúrate que email está habilitado. Okay. Les enseño cómo. Ya lo he hecho antes. Vamos para acá. Supase. Vamos aquí en la parte de proyecto. Okay. Y aquí tenemos una parte de autentication y donde dice, vamos a ver email us to confirm email after signing up. Y eso es eso. lo que nos dijo, ¿se acuerdan que decía que es usar el template que venía por defector y que si queríamos lo podemos cambiar después? Aquí es donde lo podemos cambiar. Entonces, vámonos por acá. Al us sign up. Sí, man, no. Confir email. Sí. Y aquí está email. Si quisamos podamos poner teléfono, Apple, todas esas opciones para iniciar sesión. Secure email, email provider, mínimo de caracteres. Okay, todo parece estar bien. Nos dio vuelta y dice que que lo probemos. Vámonos para acá. Actualicemos. Vamos a darle registrar. Aquí vamos a poner el correo. Vamos a ver si lo aceptan. Va a pedir que confirmen usar este otro correo. Salos. Poner contraseña. Crear cuenta. Okay, dice que tengo que revisar mi correo. Nos vamos para acá. Okay, confirme. Lo de confirmo. Como se como está bastante feo el correo, pero es el templo de su pavase, eso lo podemos editar. Es le pueden decir, es más, dame un temple para su pais que se vea así, así, así. y lo más lo cambian ahí donde les enseñé. Vamos a darle confirmar. Se supone que ya podemos iniciar con mi congresina. Okay, ya nos dejó iniciar sesión. Aquí tenemos clientes, todo perfecto. Entonces ya hicimos la autenticación que nos tardamos 6 minutos a lo mucho ya todo esto funcionando y vamos a ver lo último que sería hacer el deploy. Entonces vamos a decirle, "Okay, perfecto, muchas gracias por implementar esto tan rápido. Creo que ya estamos listos. Eh, nada más ayúdame a darle una última checada. Confirmar que todo está listo antes de hacer el deploy a Verel. A ver si hay no a Verel. No necesito esto. Con que hagamos un flash. Listo. Vamos a ver qué encuentras. No es de que estamos listos para hacer el deploy a Verel. Okay. Va a ser un build. building for production some chunks are larger 50k consider using dynamic import for split ok command resumen de la revisión V producción ejecuté localmente sin errores, la autenticación las rutas públicas los reportes compartidos variables de entorno. Diseño paso para el deploy a ver para desplegar ejecutar recortos importantes por despliegue. Tengo que cambiar las variables de entorno. Es algo que les voy a enseñar. Te gustaría que ayude con el comando de despliegue manualmente. Se supone que conectamos eh el MCP de Versel, entonces él podría hacer todo el despliegue por nosotros. Vamos a confirmar. Okay. Si ya está todo listo, hagamos el deploy. Sin embargo, eh verifica porque tienes el MCP de Versel conectado y entonces tú podrías hacer el deploy por mí. se protecta como [resoplido] está checando las variables. Okay. siguientes paquetes. O si no quisieran conectar directamente a Verel, como ya tienen el código en GitHub. Se pone ver hacer el deploy manual. Vamos a ver si puede hacer el deploy por nosotros. Este, si no hacemos el deploy eh nosotros manualmente ya tener todo sincronizado con Gitcub. Una vez la cuenta creada, literal es siguiente, siguiente la recomendación siguiente y lo último es cambiar las, bueno, no cambiar, poner las kiss en el ah las variables en torno de Versel, porque ahorita las tenemos en las variables en torno locales. Tenemos que subirlas así, esas sí las tenemos que hacer manualmente, ponerlas en las variables entorno de Versel y ya con eso estaremos listos para hacer el deploy. No vamos a utilizar un dominio público ahorita porque esa es una aplicación únicamente de prueba, pero es muy sencillo conectarla con sus dominios públicos. Siempre se tiene que ir a su webhost donde estén y van a agregar el DNS de el registro que les dé Versel y listo. Con eso hacemos el deploy. Digo, no el deploy, el que apuntemos a un dominio que ustedes tienen, un dominio que ya sea ustedes o un dominio que quieran comprar. Depende con el productor que lo hayan comprado. Muchas veces eh tienen conexiones, por ejemplo, con Lob. Si tú tienes tu dominio directamente con con Go Daddy y con Cloudf, me parece, se conecta, tiene integración con ellos, se conecta y te permite eh simplemente iniciando sesión, Lobab se encarga de hacer todo lo que es la parte de la creación. eh del dominio, los registros del DNS y todo. La verdad quiero más seguro es que me vaya a pedir que inicie sesión yo. Vamos a ver si puede sacar. Continuemos esto. No lo había visto. También pueden configurar el navegador por que va a abrir. En este caso me abrió un navegador de Chum que yo no uso. Y recuerden que estoy haciendo todo en incógnito por cuestión de diferenciales para que no se mezcle. Pero si ustedes tienen cuál es una nave por defecto, inclusive en antigravity configuran cuál es el navegador que va a abrir, este, ya pueden tener iniciado y va a ser todo mucho más rápido. Vamos a ver qué nos dice. Está analizando. Okay, listo. Estado final. Código todo está comité pusado build ejecutar pro la aplicación compañero creo crear el archivo bas automáticamente succiones para el SP final como ya tengo todo preparado solo necesitas ejecutar este comando en tu terminal local en NP. Okay, vamos a copiarlo. Proceso hará unas preguntas responde. Okay, okay, okay, creo que es importante las variables entorno. Okay, entonces vamos a hacerle caso. Vamos a nuestra terminal, pegamos el comando y le damos enter. Okay, me dice que sí que hacer ploy. Aquí me está diciendo que le responda que sí. No es un yes nada más es un y le doy enter. Okay. User error de specify token is not use vers login to generate token. Okay. Entonces voy a copiar este error y le voy a decir al correr el comando me dio este error. Vamos a ver qué me dice. Y si no, para no complicarnos mucho, hago el deploy manual y ya está. Cerrar sesión iniciar de nuevo tu navegador para que confesa de GitHube. Okay, entonces vamos a darle. Okay, ni siquiera está iniciado sesión, entonces probablemente por ahí estaba el detalle. Vamos a iniciar sesión. que entre a Versel y ponga este código. Entonces vamos a este navegador donde lo tenemos. Me pide que vaya a versel.com/onaldevice. Pongamos el código. Regresamos antigravity. permitir deploy commit conn equip. Okay, entonces podemos volver a correr esto. Pro, veamos. Sí. Contain your project. Vamos a ir aquí con arriba, que lo que nos decía. Ah, bueno, ya está aquí. Perfecto. Link to existem project. No. Pero no. link to demoortunity con project yes property a ver que construyendo No. y dice que ya hice el deploy y este es el link. Sin embargo, vamos a confirmar directamente en Versel. Vámonos para acá. Vamos a cerrar esto. Vamos aquí. Actualizemos la página. Okay. Com. No, vamos a root. Okay. Y dice que este es mi dominio. Vamos a darle. Okay. No me carga obviamente porque bueno, pueden ser por diferentes razones, pero hay algo que tenemos que hacer. ¿Se acuerdan lo que nos decía de las variables de entorno? Entonces vamos a ir a settings, environment variables, add environment variables. Podemos darle import. Vamos a buscar en mi carpeta donde tengo esto. Ah, car es este. Si no le sale el import. porque es un archivo oculto, digamos, de en Windows es en en creo que opciones de visualización de carpeta, mostrar archivos ocultos y aquí en Mac me parece que es comando shift punto y ya me debería de salir el local. Aquí está. Okay, okay, okay, okay, okay, okay. Vamos a darle save. Y vamos a darle redeploy para que me de todo. Vamos a matar. Vamos a ver deployment conjunción. Es gratis ahorita para hacer el deploy y no necesitan pagar nada. Supongo comentaba, eh, si quieren hacer deploys más rápidos o si le quieren dar mejor eh recursos, digamos, a donde esté su proyecto, entonces ya ahí donde empiezan a pagar. Okay, dice que ya hizo el deploy de nuevo. Vamos a ver. Ahora si nos carga. Estamos aquí. Vamos a iniciar sesión para asegurarnos de que esté funcionando este correo. Okay, inició sesión, está funcionando. Configuración, agencia. Puedo cerrar sesión. Perfecto. Entonces está funcionando. Hicimos ya el deploy. Tenemos la app con esto que podemos pasar esta dirección a cualquiera. Obviamente a nivel producción no haríamos esto. Le pondríamos un dominio, verificaremos otras cosas. Tendríamos que tener en cuenta también suabase, ¿eh? ¿Por qué? Porque tenemos la cuenta gratuita. Okay. ¿Qué quiere decir la cuenta gratuita? Tenemos eh ciertas limitantes al número de request que podemos hacer. o el número de de request simultáneas que me parece que en cuenta gratuita son 25 o 20 si no me equivoco. Y tendrán que hacer el cambio a propí son 200 y obviamente hay muchísimas más cosas para llevar a a producción final, pero eso es un curso básico. Y creo que ya es todo. No hubo que hacer nuestro overhovel una vez que se fue desplegado Versel. Ya pusimos las variables de entorno y ya está listo para funcionar. Bueno, nada más para verificar vamos a ver que efectivamente está funcionando la parte de NHN y de Gemini generando el correo. Así que voy a iniciar sesión de nuevo. Vamos a hacer las pruebas. Eli un cliente que lo escriba la Okay, eso está funcionando. Le enviar el correo. Okay, está funcionando todo perfecto. Espero que lo hayan disfrutado, que les haya gustado, sobre todo que hayan aprendido y eh los leo para ver qué qué cosas están creando ustedes. Yes.
