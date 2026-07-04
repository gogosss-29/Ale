# 📊 Troubleshooting y Supabase

> Ruta: Vibe-Coding › 📊 Troubleshooting y Supabase

**🎬 Vídeo (20.6 min):** https://youtu.be/ZBVih2BdQzU

---

## **Parte VI. Conectar Supabase de verdad, crear tablas vía SQL y arreglar guardado, share y UI**

En esta lección dejamos Supabase correctamente conectado y pasamos de “UI bonita” a “datos guardándose de verdad”.

Aquí vas a:

- Entender por qué el MCP de Supabase a veces no puede ejecutar SQL desde Antigravity.
- Configurar el **Access Token correcto** de Supabase para el MCP.
- Crear las tablas del MVP en Supabase usando el **SQL Editor**.
- Validar que el flujo de la app ya guarda diagnósticos, clientes y cotizaciones.
- Corregir bugs reales de producto. “No hay diagnóstico para compartir”, modo oscuro ilegible y botón de editar roto.

## 1. Contexto. Por qué falló Supabase desde Antigravity

Arrancamos intentando lo lógico:  
“Ya tengo el MCP de Supabase. Que el agente cree tablas desde aquí”.

Pero aparece el error de “no autorizado”.

La razón principal:

- Tener el MCP configurado NO significa que ya tenga permisos para hacer operaciones sensibles en tu proyecto.
- Para eso necesitas un **Access Token** específico, con permisos correctos.
- Y además, Supabase distingue entre tipos de llaves. No todas sirven para lo mismo.

Conclusión práctica:  
Para el MVP, la vía rápida es crear tablas manualmente con SQL desde el panel de Supabase.

## 2. Crear el Access Token correcto en Supabase

En el video hacemos esto:

- Vamos al perfil de Supabase.
- Entramos a **Account Preferences**.
- Buscamos **Access Tokens**.
- Generamos un token nuevo.
- Lo nombramos algo tipo “Antigravity MCP”.
- Le ponemos expiración corta si solo es para pruebas.

Luego lo pegamos en el entorno local, en el archivo `.env.local`, en la variable correspondiente para Supabase MCP.

Resultado esperado:

- MCP reconoce el token.
- Ya no falla por “token inexistente”.

## 3. Aclaración importante sobre keys. Legacy anon key

En medio del troubleshooting aparece un punto delicado:

Supabase tiene llaves distintas:

- Publishable keys.
- Service keys.
- Legacy keys.

En el video se menciona la **legacy anon key** como parte de la solución.

Regla clara para el curso:

- No expongas keys sensibles públicamente.
- No subas `.env.local` a GitHub.
- Todo lo que usamos aquí es para desarrollo y demo.

## 4. Crear tablas del MVP en Supabase vía SQL Editor

Aunque el agente puede ayudarte a generar el SQL, la ejecución la hacemos así:

- Copiamos el script SQL.
- Vamos a Supabase.
- Abrimos **SQL Editor**.
- Pegamos el código.
- Ejecutamos.

Luego validamos en **Table Editor** que ya existen las tablas del MVP.

En el video se crean tablas como:

- clients
- diagnostics
- quotes
- y otras tablas relacionadas al historial del diagnóstico.

Resultado esperado:

- Las tablas ya existen en Supabase.
- El proyecto ya tiene estructura real para guardar datos.

## 5. Confirmación. “Listo, ya corrí el SQL”

Después volvemos a Antigravity y le pedimos al agente:

- Confirmar que las tablas existen.
- Validar que están creadas con lo correcto.
- Hacer un “quick scan” de infraestructura.

Aquí el agente incluso intenta verificar con herramientas locales, y te confirma qué tablas ya existen y cuáles están listas.

## 6. Prueba en la app. Crear diagnóstico y generar reporte

Volvemos al flujo normal:

- Creamos un diagnóstico.
- Agregamos industria, herramientas, pain points.
- Grabamos audio.
- Generamos reporte.

Aquí se ve si realmente ya está guardando o si solo era UI.

## 7. Bug 1. “No hay un diagnóstico guardado para compartir”

Sale el error:  
“No hay un diagnóstico creado para compartir”.

En el video lo arreglamos así:

- El agente identifica que el sistema intentaba asociar el share link a un cliente buscándolo por email.
- Pero el formulario ni siquiera te pide email, entonces esa lógica estaba mal.

Fix aplicado:

- Si no hay email, usar nombre o empresa como fallback.
- Asegurar que el diagnóstico se guarde antes de permitir compartir.

Resultado esperado:

- Generas link.
- Copias link.
- Ya no falla.

## 8. Bug 2. Modo oscuro. Textos ilegibles

Aunque ya teníamos dark mode funcional, todavía pasaba esto:

- Títulos y textos en colores muy oscuros.
- No se distinguen en fondo oscuro.

Fix aplicado:

- Reemplazar clases con colores fijos por variables o clases consistentes con el tema.
- El agente prueba en navegador, toma screenshots, y valida visibilidad.

Resultado esperado:

- Dark mode legible en todas las pantallas principales.
- Especialmente en el wizard del diagnóstico.

## 9. Bug 3. Botón “Editar” no funciona

Este es un bug típico de MVP maquetado:

- El botón existe.
- Pero no está conectado a ruta o acción.

Fix aplicado:

- Conectar el botón a la vista de edición del reporte o del diagnóstico.
- Confirmar navegación correcta.

Resultado esperado:

- Editar abre la pantalla esperada.
- No se queda en “nada pasa”.

## 10. Validación final. Volver a probar todo

Al final hacemos pruebas rápidas:

- Crear diagnóstico.
- Generar reporte.
- Editar.
- Generar link.
- Dark mode.

Y confirmamos que ya no se rompe el flujo principal.

Al finalizar esta lección debes tener:

- Supabase operativo.
- Tablas creadas en Supabase.
- La app guardando diagnósticos y clientes en backend.
- Share link funcionando.
- Botón editar funcionando.
- Dark mode legible en el wizard y pantallas principales.

Si tienes esto, ya estamos listos para la siguiente fase del MVP.

## 🎙️ Transcripción

Perfecto. Entonces, continuamos donde nos quedamos. Lo último que hicimos fue mejorar eh bueno, no mejorar, sino corregir los errores que teníamos en el la parte de settings. Teníamos light mode, entonces le preguntamos que continuemos con el PRD, que si puede analizar que future sigue pendiente y nos dijo que el sigue regeneración de propuesta publicable, el Epic 3, edición de recomendaciones y la base de datos. Y aquí me dijo mi recomendación. Empezamos por la Epic 4. Eh, agregar el esquema SQL y lógica de compartir. ¿Te parece un te paso? Okay, le voy a decir, "Sí, me parece bien tu plan. Vamos a seguir adelante. ¿Y qué es qué seguiría ahorita? Sigo en modo F. Sigo usando Yemina 3 Flash. Dice configurar suabase lo que voy a hacer ahora mismo, este código yo voy a implementar la vista pública. Voy a empezar creando componente para la vista pública ruta. Para que podamos Okay, yo sé cómo ejecutar esto, pero vamos a hacer una prueba. Oye, pero tú tienes acceso al MCP de Supase. No puedes ejecutar tú y crear las tablas desde aquí. Vamos a ver qué me dice. Accediendo al en local que hace que está buscando cuál es la URL, está viendo la versión CPA base, por algo le rechazó la conexión. Eh, dice que no tenemos Cli de Supase. A lo mejor no va a pedir que instalemos ahorita con el npm. dice, "Tienes razón, normalmente yo debería poder hacerlo. Sin embargo, he intentado conectarme a tu proyecto supervía y me devuelto un error no autorizado. Eso porque aunque tenga losciales de duplicación para que yo pueda crear tablas o modificar la base de datos desde aquí necesito una personal token de su configurado en el servidor. ¿Cómo puedes poseer la vía rápida manual? copia el código SQL. Si algo siempre, tendrás que generar un access token en su Pab settings Access tokens y confiarlo en la extensión por servidores MCP. Mientras tanto, eso es lo que mi plan. Okay, esto ya lo teníamos y si me interesa que pueda hacerlo eh las cosas a futuro. Entonces, vamos a a hacer esto. Pero déjame preguntarle algo antes. Oye, pero revisando mi local, si tienes ahí la personal access token que te di para todo mi proyecto. Puedes confirmar que si la tienes la puedes ver y cuál es el código de Rock y te regresa. Será cuestiones de permisos o de scopes que no te deja acceder a todo el proyecto completo. Vamos a ver qué me dice. Y mientras hace esta investigación, me voy para acá, me voy a mi supase y vamos a ver esta que es de antigravity. Solo me permite eliminarla. No puedo ver nada. Y no me acuerdo si aquí creo que la de scope SH GitHub no supace. Entonces eso no es el problema. Vamos a ver qué nos dicen antigravity. Okay, entiendo perfectamente tu duda como secretos directo para la internet sobre solo puedo ver los tools herramientas. El hecho de que se rojará el error indica que o bien el token está configurado en el entorno donde correp o ha expirado. El error exacto. El código el código de error que recibí fue una valenc server llaves appys service son las que pusimos en el local. Se sirve para que la web guarren las tablas y access token. Es es el caso que tu usuari es el que necesita el servidor posible problema. Si un token antes probable que se deopar el botón. Okay, vamos a ver entonces proyectos y me quiero ir a a la organización organization settings o apps y que no Tengo no es aquí. Vamos para acá. Okay. Entonces, nos vamos aquí en nuestro perfil. Account preferences, access tokens, generate new token. Vamos a ponerle antigravity mcp que expire en un día nada más lo necesito para esto. Generamos el token y aquí está mi token, así que lo voy a copiar. Aquí copy. Vámonos de vuelta a antigravity. Me pide que lo cambien el local, así que voy a [carraspeo] buscar de este lado del lo abro y me dice que lo ponga para base access token. Que agreg esta línea, así que vamos a agregar esto portón. Y aquí iría mi token. Listo. Vamos a darle file save. Cerramos. Listo. Ya agregué el access token. Puedes probar, por favor, y correr el SQL para las creación de tablas. [carraspeo] Okay, está intentando hacer la conexión. Dice que otra vez no pudo network. Vamos a ver qué nos dice esta vez. dice que no pudo, pero que va a crear todo asound que abre una tabla y ahorita me va a pedir que haga la tabla lo más seguro. Déjame ver el otro token que hicimos a nivel proyecto. No me acuerdo cuánto tiempo lo pusimos que expiraba. Gravity creo que no S. A ver si puede ser esta legacía. Vamos a ver qué me dice. Estoy trabajando. Creo que aquí arriba mencionado algo de Legacy para que no tome mucho tiempo y regrese aquellas ociones. Okay. So, después de estar haciendo las pruebas, eh, [carraspeo] el mismo Antigravity me dijo que cambiara este anon key. Este lo sacamos de los proyectos, pero en lugar de publishable and secret keys, en Legacy Anon, este, este es como que te da acceso a todo. Entonces, tengan tengan cuidado, no lo vayan a exponer nunca. Eh, yo cuando suban este video, pues todo esto las cuentas voy a borrar y todo, pero bueno, lo sacamos aquí y nos está pidiendo que, okay, dice, "Ya, okay, ya tengo acceso, está corregido tu token, puedo ver todo, pero no puedo crear eso, hazlo tú, por favor." ¿Qué tenemos que hacer? Simplemente le damos copiar aquí, nos vamos a Supase, nos vamos aquí donde dice SQL Editor, ¿okay? Y aquí le vamos a dar pegar. y le vamos a dar run. Success no Return. Y vamos a ver. Dice create an extension if not existable if not exist clients. Si nos vamos a table editor, vemos que ya tenemos clients diagn diagnos. Entonces, nos vamos de regreso y le voy a decir, "Listo, ya corrí este código SQL. ¿Puedes por favor confirmar que tienes acceso a todo y que no hay ningún detalle? Vamos a ver qué nos dice. Está pidiendo autorización para correr desde su propia terminal y dice, confirma al 100%, revisó la verificación conexión hacia su base de datos. La respuesta exitosa, un arreglo vacío, lo que significa que la tabla de clientes ya existe. Okay. Estado de infraestructura, tabla clientes, cuotas están caros correctos carencial, prueba maestra. Ahora ve tu app local, haz un scan rápido con datos ficticios. Al terminar el portas generar link, este link es una propuesta real. Okay, vamos de vuelta a la A. Hm. Aquí vamos a darle refrescar. Nuevo diagnóstico. Imperio dos seleccionar la industria, e-commerce. Vamos a decirle que vamos a utilizar en HN y sheets. Voy a darle reportes manuales y retrasos de facturación. No va a ser para trás del audio. Okay. Este cliente tiene problemas con sus reportes manuales, ya que tiene que procesar todo e ingresar línea por línea, descarga las facturas y eso tiene que corroborar manualmente contra cada uno de los pagos que se realiza. Audio guardado. Generar reporte. Vamos a ver aquí. Y todavía no me gusta cómo se ve esto, así que le voy a pedir que lo que revise bien. Okay, me dice tener link. No hay un diagnóstico guardado para compartir. Vamos a tomar captura y se lo pasamos a la gente. Te dejo una captura pantalla de el error que me sale. me dice que no hay un diagnóstico creado para compartir, puedes verificarlo y una vez que estás ahí, necesito que también revises el dark mode que platicamos. [resoplido] Algunos textos, sobre todo los títulos, siguen estando obscuros y no se pueden leer bien o no son legibles en modo obscuro. Revisa estas dos cosas ya que vas para allá. Y me di cuenta que el botón de editar tampoco funcionó. Verifica si puedes hacer estas tres cosas en un solo paso o si no ponlo en tus tareas, itera y regresa hasta que esté listo. Okay, vamos a ver. Voy a poner pausa y regreso. Okay, ya terminó. Vamos a ver. Dice, "Entendido he corregido estos pasos. Error. No hay diagnóstico para compartir. Identifico que el error ocurría porque el sistema intentaba buscar un cliente por correo electrónico. No siempre se captura en el Wiz. He robostecido la lógica para que si no hay un email use el nombre de la empresa como identificador. Okay, tenemos que ver porque no me acuerdo que ninguna parte me haya pedido el correo. Segundo, modo oscuro elegible. Repasado todas las clases de colores fijos por nuestras variables semánticas. Botón de editar. Funcional. Ya funciona. Ahora le hac click entre el reporte los títulos. Refresca la aplicación, haz un scan rápido, modo oscuro, editar, generar link. Okay, vamos a hacer todas estas pruebas. Vámonos de vuelta para acá. Vamos a refrescar. Okay. Panelos recientes. Voy aquí. Okay. Diagnóstico. Nombre de la empresa. Imperio 3. Industria. Okay. Nuo diagnóstico. No sigue sin gustarme esto. Continuar. Vamos a poner aquí cualquier cosa para que me salga. Igual esto le voy a decir tal cual. Okay. Editar ya nos deja. Generar link. Link copiado. ¿Qué pasa si pegamos el link? Okay, perfecto. Bastante decente. Okay, vamos a ver decirle. Muy bien, veo que editar ya funciona, generar link ya funciona. Ahora necesito algo más que vuelvas a revisar, lo de dark mode. B, genera tú un diagnóstico para que te des cuenta que en la primer ventana de captura de empresa, los títulos siguieron saliendo muy oscuros. en la segunda ventana donde tú escoges las herramientas sigue saliendo muy oscuro. Así que necesito que vayas y que revises ese proceso. Tú hagas un generes tú un diagnóstico. Okay. Mientras hace eso, vámonos a Supase. Vamos a refrescar. Vemos que en diagnósticos ya no sale. Él lo va a hacer todo, ¿no? Vamos a ver si lo hace. Okay, ya lo hizo. Está viendo esto. Okay. Selecciono ahí. Vamos a ver qué pone con empresa. Okay. Dice que el no está mi input. Tengo que confirmar esto. Vámonos de vuelta. Voy a instalar mi input. Básicamente me está preguntando si puedo hacer todo esto. ¿Qué tiene que seleccionar una industria? Debe ser suficientemente inteligente para seleccionar la industria. Está preguntando de nuevo e-commerce. Okay, va a poner e-commerce. Company. Vamos. Seleccionar la industria. Tú puedes otra vez. Está mi input. Ya te dije que sí. Okay. Hola. Preguntadas. Terminó. Ya está terminando, pero quise ponerle play al video para que vean como aquí se toma los screenshots y aquí se puede ver tal cual el screenshot que tomó para ver el texto, el color y si está bien todo. Y aquí está trabajando sobre eso, esas cosas [carraspeo] que que encontró y ya nada más ahorita le voy a pedir que nos va va a hacer otra prueba más. Y al final ya no más le voy a pedir que me confirme dónde se captura el correo, dónde se capturan los los clientes, porque no me quedó eso muy muy claro y con eso terminaremos el video. Así que vamos a poner igual pausa y regreso. Okay, ya terminó. Dice lo que mejor en el wizard, títulos barra progreso, inputs. Si se fijen tardó bastante porque iba, venía tomar capturad regresaba. He verificado esto. Ya puedes probarlo. ¿Algún otro detalle visual? No creo que visualmente por ahora estamos bien. Te eh dejaré saber si hay algo más en lo que tengas que trabajar, pero algo que no me quedó claro, en qué momento una capturo los clientes o pongo su correo electrónico. Vamos a mandar y voy a parar aquí el vídeo para hacer este dejarlo combo trouble shooting y conectar correctamente suabase y crear las tablas vía SQL. Y en el siguiente video continuamos con esta parte. M.
