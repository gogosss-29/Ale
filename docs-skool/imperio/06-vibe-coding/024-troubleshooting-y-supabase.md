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
