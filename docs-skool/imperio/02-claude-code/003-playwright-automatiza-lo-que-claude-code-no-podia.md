# Playwright: Automatiza lo que Claude Code no podía

> Ruta: Claude Code › Playwright: Automatiza lo que Claude Code no podía

**🎬 Vídeo (33.0 min):** https://www.youtube.com/watch?v=dghyElh4EFw

---

Claude Code siempre fue brutal en una cosa: crear. Crear código, automatizaciones, deploys de agentes, sistemas completos. Lo que le pidieras lo construía.

Pero tenía un punto débil del que muy pocos hablaban: era pésimo diagnosticando problemas en interfaces y navegando la web.

Si querías sacar métricas de tu comunidad de Skool, no podías. Si querías debuguear errores en un dashboard interno, no podías. Si querías operar una aplicación como lo haría un humano, simplemente no podías.

Eso cambió.

Apareció Playwright integrado con Claude Code, y esto cambia completamente el juego de las automatizaciones, el debugging y de cómo operamos día a día con esta herramienta.

Hoy ya no necesitamos que un servicio tenga una API. No necesitamos que tenga un MCP. No necesitamos crear scrapers a medida. Simplemente le das un navegador a Claude Code y lo usa como lo estarías usando tú.

Y antes de que pienses que esto es Computer Use mejorado, déjame aclararte algo: es una categoría completamente distinta. Y mucho mejor.

---

## El problema que nadie estaba resolviendo bien

Antes, cuando usábamos Claude Code, teníamos dos formas de conectarlo a servicios externos.

La primera era a través de APIs. Una aplicación expone un endpoint, te conectas con un token, y le dices a Claude Code que ejecute herramientas específicas dentro de ese servicio.

La segunda era a través del MCP, el Model Context Protocol. Un traductor universal entre el agente y la herramienta, optimizado para LLMs.

El problema es que muchísimas aplicaciones no tienen ni API ni MCP.

Skool, por ejemplo. Si quiero sacar data de mi comunidad Imperio Digital, tengo que hacerlo manualmente. No hay API. No hay MCP. La única alternativa era armar un scraper desde cero, adaptarlo cada vez que el frontend cambiara, y rezar para que no me bloquearan la cuenta.

Google Trends es otro caso. Lo uso constantemente para detectar qué keywords están subiendo. Pero su API pública no existe. Solamente hay una versión privada que aceptan a poca gente.

Y aquí es donde alguien diría: usa Computer Use. Pero Computer Use no funciona bien. Gasta una cantidad obscena de tokens porque literalmente saca un pantallazo, lo manda al modelo de visión, mueve el mouse, saca otro pantallazo, lo interpreta otra vez. Y así. Para una acción de 20 pasos se demora 20 conversaciones. Es lento, es caro, y si el frontend cambia un poco, ya no funciona.

Esto es exactamente lo que vino a resolver Playwright.

---

## Playwright: por qué es otra cosa

Playwright es un proyecto open source de Microsoft. Originalmente diseñado para testing de aplicaciones web, ahora también funciona como infraestructura para agentes de IA.

La diferencia clave con Computer Use es que Playwright no mira píxeles, mira el accessibility tree.

El accessibility tree es una representación textual de la estructura de cualquier página web. Lo usan los lectores de pantalla para personas con discapacidad visual. Pero lo importante es que rescata cada elemento con su nombre: botones, links, formularios, inputs, todo.

Entonces, en vez de decirle al agente "haz click en la coordenada 845-641 después de analizar esta imagen", le decimos directamente "haz click en el botón Submit". Es texto. Es determinístico. No se confunde.

Y esto cambia tres cosas fundamentales:

1. Es más rápido. No tiene que sacar pantallazos ni interpretar imágenes. Lee texto y ejecuta.
2. Es más barato. Mucho menos consumo de tokens por acción.
3. Es más confiable. No se confunde con cambios visuales menores ni con animaciones.

Para el 99% de los casos en los que quieres automatizar, scrapear datos, llenar formularios, navegar interfaces o hacer debugging, Playwright le pasa por encima a Computer Use. Solo tendría sentido seguir usando Computer Use para aplicaciones nativas con interfaces muy visuales, tipo Photoshop o Illustrator.

Para todo lo que viva en un navegador, Playwright es objetivamente superior.

---

## Cómo conectarlo a Claude Code

La conexión es ridículamente simple. Ni siquiera tienes que crear cuenta ni sacar API key, porque Playwright es open source.

Abres Claude Code y le dices algo así como:

> "Investiga la documentación oficial de Playwright MCP en el repositorio de Microsoft ([https://github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)). Una vez que la entiendas completamente, conecta el MCP a esta sesión y dime qué herramientas quedaron disponibles."

Listo. Después de reiniciar Claude Code, ya tienes acceso a más de 20 herramientas para controlar navegadores. Funciona con Chrome, Edge, Firefox y Safari. Y puedes correrlo en modo headed (ves la ventana del navegador en tiempo real) o headless (corre en background sin que veas nada).

Para tareas largas o automatizaciones programadas, headless es lo ideal. Para iterar y entender cómo está navegando, headed es lo mejor.

---

## Tres casos reales de cómo lo estoy usando

Para no quedarnos en lo teórico, te muestro tres casos concretos que estoy ejecutando ahora mismo.

### Caso 1: Scrapear Google Trends para planear contenido

Una de las cosas más útiles para creadores de contenido es saber qué keywords están subiendo. El problema es que Google Trends no tiene API pública.

Antes, esto era un trabajo manual de entrar, buscar término por término, capturar pantalla, comparar. Una hora por sesión, fácil.

Con Playwright, le doy a Claude Code un prompt con la lista de términos que me interesan (Claude Code, Claude Design, OpenClaude, Antigravity, Cursor, etc.), le pido que los compare en grupos, y que me devuelva un archivo Markdown con el ranking absoluto y recomendaciones de contenido para grabar.

En 5 minutos termina el análisis completo. Con snapshots de cada búsqueda, JSON estructurado de la data, y una recomendación concreta del próximo video que debería grabar.

Lo mejor es que mientras está corriendo, puedo seguir trabajando. El navegador se abre en su propia ventana, no toma control de la mía. Y si veo que está haciendo algo mal a la mitad, puedo intervenir y reorientarlo en vivo.

### Caso 2: Debugging de mi dashboard interno

Tengo un dashboard que se llama Imperio Agéntico. Es un buscador interno para los miembros de la comunidad, porque el buscador nativo de Skool funciona terrible.

El problema es que cada vez que iteraba en la UI con Claude Design, no podía verificar si los cambios se veían bien en distintos viewports. Tenía que entrar manualmente, probar en mobile, en tablet, en desktop, anotar bugs, volver a Claude Code, pasarle el feedback. Muy lento.

Ahora le paso el link del dashboard a Claude Code, le digo que entre con Playwright, ajuste su resolución a mobile, navegue todas las secciones y me devuelva un diagnóstico con las cinco mejoras prioritarias.

En minutos descubrí que mi navegación mobile estaba rota. Solo se veían tres botones de seis. Mi sección de "perfil" cargaba vacía. Tenía llamadas N+1 en el backend. Cosas que llevaban días invisibles porque nunca probé el flujo desde un device real.

Y si tienes el plan Max, puedes conectarlo directamente al proyecto en otra ventana de Claude Code y dejarlo que se autoalimente. Detecta bugs, los soluciona, vuelve a probar. Loop completo sin tu intervención.

### Caso 3: Extraer métricas de Skool día por día

Skool no permite exportar el detalle del conversion rate diario. Solo te muestra un gráfico que tienes que interpretar pasando el mouse por cada punto.

Con Playwright le pido a Claude Code:

1. Entra a mi cuenta de Skool
2. Ve a settings, métricas
3. Encuentra el gráfico de conversion rate
4. Haz hover sobre cada uno de los 31 puntos del mes
5. Anota cada valor con su fecha
6. Devuélveme un JSON con toda la data

Y aquí está la magia: no son 31 acciones separadas con 31 pantallazos. Es un script único que ejecuta los 31 hovers en una sola pasada y devuelve toda la información de golpe. Comparado con Computer Use, esto es la diferencia entre 5 minutos y una hora.

---

## El combo que lo hace imparable: Routines

Si te gustó lo que viste, esto te va a gustar más.

Claude Code Routines es la función de automatización programada de Anthropic. Te permite definir tareas que se ejecutan en horarios específicos, en infraestructura de Anthropic, sin que tengas que dejar tu computador prendido.

Cuando combinas Playwright con Routines, puedes armar cosas que antes eran imposibles sin un servidor 24/7, scripts custom y monitoreo constante:

- Scraping diario de tus métricas a las 2 PM, con resumen automático en tu inbox
- Monitor de precios de competidores en Amazon
- Bot que entra a comunidades Skool y rescata las publicaciones que están funcionando
- Búsqueda automática de oportunidades en marketplaces
- Scraping de portales inmobiliarios con alertas de propiedades nuevas

Todo esto antes requería un developer, infraestructura propia, y un costo recurrente importante. Hoy son dos prompts: uno para Playwright y otro para la Routine.

---

## Limitaciones honestas

No te quiero vender humo, así que también hablemos de los puntos débiles.

Primero: usa tokens. No tantos como Computer Use, pero igual gasta. Cada acción mete el accessibility tree del modelo en contexto, y una sesión completa puede gastar 100K tokens fácil. Si lo vas a usar en tareas largas, considera el CLI de Playwright directo (sin pasar por MCP), que puede gastar hasta 4 veces menos según pruebas que vi.

Segundo: hay sitios con anti-bot agresivo. Bancos, ciertos retailers, plataformas con Cloudflare en modo paranoico. Playwright tiene formas de mitigar la detección y en la mayoría de los casos funciona, pero si tu objetivo es scrapear sitios muy protegidos, prepárate para iterar mucho.

Tercero: requiere iteración. Casi nunca el primer prompt te va a dar el resultado perfecto. Vas a tener que conversar, ajustar, refinar. La gracia es que cuando llegas al flow correcto, le pides a Claude Code que te genere un skill replicable, y a partir de ahí queda estandarizado para siempre.

---

## Por qué esto cambia las reglas del juego

Hasta hace poco, automatizar interfaces web en serio requería conocimiento técnico real. Selenium, Puppeteer, scripts custom, infraestructura, servidores, mantenimiento.

Hoy es una conversación con Claude Code.

Esto no es un upgrade incremental. Es la diferencia entre poder vender automatizaciones que antes no podías ofrecer y quedarte limitado a los servicios que tienen API.

Si vendes servicios de IA, automatizaciones o quieres empezar a empaquetar este tipo de soluciones para clientes, este es el momento de aprender a operarlo bien. El mercado de "automatizar lo que no se podía automatizar" está completamente abierto.

Y para que lo apliques de inmediato, dejé adentro de Imperio Digital el **Playwright Starter Pack** completo. Trae los prompts exactos del video más cinco casos de uso adicionales, sección de troubleshooting, y guía paso a paso para convertir cualquier flow en un skill replicable + Routine programada.

Lo encuentras en la sección de Recursos de la comunidad.

[Únete a Imperio Digital](https://www.skool.com/imperio-digital)

— Benja

---

---

# 🎬 Playwright Starter Pack para Claude Code

**Recurso exclusivo para miembros de Imperio Digital**

Esta es tu colección de prompts listos para copiar, pegar y adaptar. Todos probados con Claude Code + Playwright MCP.

La idea es simple: te damos los prompts base de los casos de uso más comunes, tú los adaptas a tu contexto y los corres. Cuando llegues al flow perfecto, le pides a Claude Code que te genere un skill replicable y queda estandarizado para siempre.

---

## 📑 Índice

1. Setup inicial
2. Configuración avanzada
3. Casos de uso del video - Scraping de Google Trends
- Debugging de UI
- Métricas de Skool
4. Casos de uso adicionales - Monitoreo de competencia
- Llenado de formularios
- Scraping de marketplaces
- Auditoría SEO
- Verificación de checkout
5. Crear un skill replicable
6. Combinarlo con Routines
7. Tips y mejores prácticas
8. Troubleshooting

---

## Setup inicial

### Prompt 1: Conectar Playwright MCP a Claude Code

```
Necesito que investigues la documentación oficial de Playwright MCP en el repositorio de Microsoft (https://github.com/microsoft/playwright-mcp). Una vez que la entiendas completamente, haz lo siguiente:

1. Instala y conecta el MCP a esta sesión de Claude Code
2. Verifica que la conexión esté activa
3. Lístame todas las herramientas (tools) que quedaron disponibles
4. Lístame las capabilities opcionales que existen y cuáles recomiendas activar
5. Dame un resumen ejecutivo de cómo está configurado

Después de eso te voy a pedir el primer caso de uso real.
```

### Prompt 2: Verificar que está funcionando

```
Haz una prueba rápida con Playwright. Abre en modo headed la página https://example.com, saca un snapshot del accessibility tree, y descríbeme qué elementos detectas. Quiero confirmar que la conexión está estable antes de seguir.
```

---

## Configuración avanzada

### Modo headed vs headless

- **Headed:** Ves la ventana del navegador en tiempo real. Ideal para iterar, debuguear y entender qué está haciendo Claude.
- **Headless:** Corre en background sin interfaz visual. Ideal para tareas largas, automatizaciones programadas, y cuando ya tienes el flow validado.

### Prompt 3: Cambiar entre modos

```
Cambia el modo de ejecución de Playwright a [headed/headless] para esta tarea. Cuando termines la ejecución, puedes volver al modo por defecto.
```

### Persistent profiles (sesiones autenticadas)

La primera vez que te logueas en una cuenta a través de Playwright, las cookies quedan guardadas. Las siguientes veces no necesitas iniciar sesión de nuevo.

### Prompt 4: Setup de sesión autenticada

```
Vamos a configurar un persistent profile para [nombre de la plataforma]. Abre Playwright en modo headed, ve a [URL de login], y déjame iniciar sesión manualmente. Una vez que esté dentro, guarda el profile para que las próximas sesiones ya entren autenticadas. Confírmame cuando esté listo.
```

---

## Casos de uso del video

### Caso 1: Scraping de Google Trends

#### Prompt completo

```
Usando Playwright en modo headed, necesito que entres a Google Trends y hagas un análisis de las cosas que están en tendencia en los últimos 30 días.

Términos a comparar (agrúpalos en búsquedas paralelas para tener marco de referencia):

GRUPO 1 (Coding agents): Claude Code, Cursor AI, GitHub Copilot, Windsurf, Continue Dev
GRUPO 2 (UI/Design): Claude Design, Lovable, V0, Bolt
GRUPO 3 (Open source): OpenClaude, OpenCode, Ollama, DeepSeek
GRUPO 4 (Anthropic ecosystem): Antigravity, Claude Skills, Claude Opus, Anthropic API

Para cada grupo:
1. Haz la búsqueda en Google Trends
2. Captura un snapshot
3. Identifica el peak de búsqueda en el período
4. Identifica la tendencia (subiendo, bajando, estable, breakout)
5. Anota cualquier evento relevante (lanzamiento, viral, etc.)

Al final:
- Genérame un archivo trends-daily-[fecha].md con todos los hallazgos
- Genérame un trends-data.json con la data estructurada
- Guárdame los snapshots en una carpeta /snapshots
- Dame un ranking absoluto de los términos por interés actual
- Recomiéndame el video que debería grabar hoy basado en breakouts y tendencias al alza
```

#### Prompt de seguimiento (interrumpir y reorientar)

```
Para un momento. Veo que estás haciendo las búsquedas por separado. Cambia el enfoque: agrupa los términos dentro de la misma búsqueda de Google Trends para tener comparación visual directa, y guarda esos snapshots en lugar de los individuales.
```

---

### Caso 2: Debugging de UI

#### Prompt completo

```
Esta es una aplicación que tenemos en producción: [URL del dashboard]

Es un software para [descripción del producto y target user]. He estado iterando con Claude Design pero hay bastantes bugs y problemas de UX que necesito identificar.

Necesito que con Playwright:

1. Inicia sesión con esta cuenta: [credenciales o "te voy a loguear yo manualmente"]
2. Una vez dentro, navega todas las secciones principales del dashboard
3. Prueba la app en tres viewports:
   - Desktop (1920x1080)
   - Tablet (768x1024)
   - Mobile (375x667)
4. En cada viewport, captura snapshots de cada sección
5. Documenta todos los problemas que encuentres:
   - Bugs visuales (elementos cortados, superpuestos, fuera de pantalla)
   - Problemas de navegación (botones que no funcionan, links rotos)
   - Issues de performance (cargas lentas, errores en consola)
   - Problemas de UX (flows confusos, CTAs poco claros)

Devuélveme un reporte con:
- Las 5 mejoras más urgentes
- Las 5 mejoras de mediano plazo
- Capturas que evidencien cada problema
- Recomendaciones concretas de cómo solucionarlas
```

#### Prompt para iterar en vivo (Plan Max)

```
Ya identificaste los bugs. Ahora vamos a un loop de auto-corrección. Tengo el proyecto del dashboard corriendo en otra ventana de Claude Code en /Users/yo/proyectos/dashboard.

El loop sería:
1. Identificas un bug con Playwright
2. Pasas el feedback al proyecto local
3. Esperas a que el cambio se deploye (auto-reload está activo)
4. Vuelves a probar con Playwright
5. Si está solucionado, pasas al siguiente bug. Si no, iteras.

Ejecuta este loop hasta que las 5 mejoras urgentes estén implementadas. Documenta cada cambio que hagas en un changelog.md.
```

---

### Caso 3: Scraping de métricas de Skool

#### Prompt completo

```
Necesito empezar a trackear mis métricas de Skool día por día. Específicamente el conversion rate (la tasa de visitantes que se convierten en miembros).

Skool no me da opción de exportar la data, hay que rescatarla del gráfico haciendo hover sobre cada punto.

Con Playwright en modo headed:

1. Entra a https://www.skool.com/[mi-comunidad]
2. Ve a settings, ajustes, métricas
3. Busca la sección de conversion rate
4. Haz hover sobre cada uno de los 31 puntos del gráfico del último mes
5. Registra el valor de cada día con su fecha
6. Genérame un archivo skool-metrics-[fecha].json con la data
7. Genérame un resumen en markdown con:
   - Promedio mensual
   - Mejor día
   - Peor día
   - Tendencia (subiendo, bajando, estable)
   - Días con anomalías (>2 desviaciones estándar)

Importante: ejecuta los 31 hovers en una sola corrida, no como 31 acciones separadas. Aprovecha que Playwright puede scriptear esto sin pantallazos intermedios.
```

---

## Casos de uso adicionales

### Caso 4: Monitoreo de competencia (precios)

```
Quiero armar un monitor de precios de competencia para [tu nicho/producto].

Con Playwright en modo headless, necesito que:

1. Entres a estos sitios:
   - [URL competidor 1]
   - [URL competidor 2]
   - [URL competidor 3]

2. Para cada uno, extraigas:
   - Nombre del producto
   - Precio actual
   - Precio anterior (si está visible)
   - Stock disponible
   - Reviews y rating
   - Ofertas activas

3. Compara con la data de la última corrida (si existe en /data/competitors-[fecha-anterior].json)

4. Genérame:
   - Un JSON con la data de hoy
   - Un reporte markdown con cambios significativos (>5% de variación de precio)
   - Una recomendación de acción (subir precio, bajar precio, mantener, urgencia)
```

---

### Caso 5: Llenado masivo de formularios

```
Tengo una lista de [N] contactos en /data/contactos.csv que necesito ingresar en [plataforma/CRM] vía formulario web (porque no tiene API ni MCP).

Con Playwright:

1. Lee el CSV
2. Para cada fila:
   - Ve a [URL del formulario]
   - Llena cada campo con la data correspondiente del CSV
   - Haz submit
   - Captura el ID o confirmación de creación
   - Espera entre submits para no parecer bot (3-5 segundos random)
3. Si algún submit falla:
   - Captura screenshot del error
   - Anota el ID del registro que falló
   - Continúa con el siguiente
4. Al final, genérame:
   - reporte-cargas-[fecha].md con éxitos y fallos
   - errores-screenshots/ con las capturas de los fallos
   - retry-list.csv con los registros que necesitan reintento
```

---

### Caso 6: Scraping de marketplaces (búsqueda de oportunidades)

```
Quiero que busques oportunidades en [Mercado Libre / Amazon / Facebook Marketplace] en el rubro [tu rubro].

Con Playwright en modo headless:

1. Entra al marketplace
2. Aplica estos filtros:
   - Categoría: [categoría]
   - Rango de precio: [min] - [max]
   - Ubicación: [ciudad/zona]
   - Antigüedad de publicación: últimos 7 días
3. Recorre las primeras [N] páginas de resultados
4. Para cada listing, extrae:
   - Título
   - Precio
   - Ubicación
   - Vendedor (si está visible)
   - URL del listing
   - Foto principal (URL)
   - Fecha de publicación

5. Aplica esta lógica para identificar oportunidades:
   - Precio significativamente por debajo del promedio del rubro
   - Listings con buena foto y descripción detallada
   - Vendedores con alta reputación
   - Publicaciones de menos de 48 horas

6. Devuélveme un reporte con las 10 mejores oportunidades, ordenadas por score.
```

---

### Caso 7: Auditoría SEO de un sitio

```
Necesito hacer una auditoría SEO completa de [URL del sitio] usando Playwright.

Para cada página principal del sitio (homepage, sobre nosotros, productos/servicios, blog, contacto):

1. Ve a la página
2. Extrae:
   - Title tag
   - Meta description
   - H1, H2, H3 (estructura jerárquica)
   - Imágenes sin atributo alt
   - Links internos (rotos vs funcionales)
   - Links externos (rotos vs funcionales)
   - Schema markup (si existe)
   - Open Graph tags
   - Tiempo de carga aproximado
   - Cantidad de palabras del contenido principal

3. Verifica:
   - Si el title está entre 50-60 caracteres
   - Si la meta description está entre 150-160 caracteres
   - Si hay un H1 único por página
   - Si las imágenes pesan menos de 200KB cada una

4. Devuélveme:
   - audit-seo-[dominio]-[fecha].md con todos los hallazgos
   - issues-prioritarios.md con los top 10 problemas a resolver
   - recomendaciones.md con acciones concretas y priorizadas
```

---

### Caso 8: Verificación de checkout (e-commerce)

```
Tengo una tienda en Shopify/WooCommerce/[plataforma] y quiero asegurarme de que el flujo de checkout funcione correctamente desde la perspectiva del cliente.

Con Playwright en modo headed:

1. Entra a [URL del producto]
2. Agrega el producto al carrito
3. Ve al carrito
4. Aplica el código de descuento [código] (si existe)
5. Procede al checkout
6. Llena el formulario con datos de prueba:
   - Email: test@ejemplo.com
   - Nombre: Juan Test
   - Dirección: [dirección de prueba]
7. Llega hasta antes del paso de pago (NO completes la compra)
8. En cada paso, captura:
   - Screenshot del estado
   - Tiempo que tomó cargar
   - Errores en consola del navegador
   - Comportamiento de los campos (validaciones, formato)

Devuélveme:
- Un reporte del flujo completo
- Los puntos donde un cliente real podría abandonar
- Recomendaciones de optimización del checkout
```

---

## Crear un skill replicable

Una vez que tengas un flow funcionando bien, no quieres repetir el prompt cada vez. Crea un skill.

### Prompt para generar el skill

```
Lo que acabamos de hacer funcionó muy bien. Conviértelo en un skill replicable para que pueda llamarlo en futuras sesiones.

El skill debe:
1. Tener un nombre descriptivo: [nombre del skill, ej: scraping-google-trends]
2. Documentar el objetivo del skill
3. Listar los inputs requeridos (qué tengo que pasarle cada vez)
4. Documentar paso a paso lo que ejecuta
5. Definir el formato del output esperado
6. Incluir manejo de errores comunes
7. Tener ejemplos de uso

Guárdalo en /skills/[nombre-skill]/SKILL.md siguiendo el formato estándar de skills.

Después de crearlo, muéstrame cómo se invoca en futuras sesiones.
```

---

## Combinarlo con Routines

Claude Code Routines te permite ejecutar tareas en horarios específicos sin que estés presente. Combinado con Playwright, puedes automatizar literalmente cualquier proceso web.

### Prompt para crear una Routine

```
Quiero crear una Routine que ejecute el skill [nombre-skill] todos los días a las [hora] en modo headless.

Configúrala con:
- Nombre: [nombre descriptivo de la routine]
- Frecuencia: diaria a las [hora]
- Repositorio: [tu repo si aplica]
- Acción: ejecutar el skill [nombre-skill] con los inputs [inputs específicos]
- Notificación: envíame el resultado a [Slack/email/Notion] cuando termine
- En caso de error: reintentar 2 veces con 5 minutos de espera, después notificarme

Una vez configurada, ejecuta una corrida de prueba inmediata para validar que funciona.
```

### Ideas de Routines útiles

- **Daily content research:** scraping de Google Trends a las 7 AM con resumen en tu inbox
- **Weekly competitor watch:** monitoreo de precios y novedades de competencia los lunes
- **Hourly metrics check:** verificación cada hora de métricas críticas con alertas
- **Daily lead magnet update:** actualización automática de un PDF basado en data scrapeada
- **Bi-daily Skool engagement:** revisión de posts nuevos en comunidades target

---

## Tips y mejores prácticas

**1. Empieza siempre en modo headed.** Hasta que el flow funcione perfecto, mantén el navegador visible. Te ahorra horas de debugging.

**2. Usa persistent profiles para sitios con login.** Una vez logueado, deja la sesión guardada. Evitas meter credenciales en cada prompt.

**3. Pide output estructurado.** Siempre pídele JSON o markdown estructurado. Evita outputs en texto libre que después no puedes procesar.

**4. Documenta los selectores que funcionan.** Si Playwright encuentra un selector que funciona perfecto, anótalo. Los frontends cambian y vas a querer volver a esos selectores específicos.

**5. Implementa esperas inteligentes.** No uses sleeps fijos. Usa esperas basadas en eventos del DOM (waitForSelector, waitForNavigation). Más confiable y más rápido.

**6. Respeta los rate limits.** Si estás scrapeando, mete delays random entre acciones (2-5 segundos). Evita bloqueos.

**7. Maneja errores graceful.** Que la tarea continúe aunque algunas iteraciones fallen. Después revisas los errores y reintentas solo esos.

**8. Considera el CLI directo para tareas largas.** El MCP gasta más tokens. Si tu Routine va a correr todos los días por horas, el CLI directo de Playwright puede gastar hasta 4x menos.

---

## Troubleshooting

### "Playwright no responde / se cuelga"

Prueba:

1. Reiniciar la sesión de Claude Code
2. Verificar que el navegador subyacente esté instalado: `npx playwright install`
3. Cambiar de modo headless a headed temporalmente para ver qué está pasando

### "El sitio detecta que soy un bot"

Prueba:

1. Activa el modo stealth de Playwright (si está disponible en tu versión)
2. Aumenta los delays entre acciones
3. Usa un user agent realista
4. Si es un sitio con Cloudflare agresivo, puede ser que necesites alternativas

### "Mi sesión autenticada se perdió"

Las cookies tienen tiempo de expiración. Si pasaron muchos días, vas a necesitar volver a loguear. Considera:

1. Renovar la sesión cada [N] días automáticamente
2. Usar tokens de API si el servicio los ofrece como alternativa

### "Está usando muchos tokens"

Si el accessibility tree es muy grande:

1. Limita el scope del scraping a secciones específicas
2. Usa selectores precisos en vez de explorar toda la página
3. Considera el CLI de Playwright en lugar del MCP

### "El selector que funcionaba dejó de funcionar"

El frontend cambió. Pídele a Claude Code:

```
El selector [selector] dejó de funcionar. Ve a [URL], inspecciona el accessibility tree actual, identifica el nuevo selector correcto y actualiza el skill correspondiente.
```

---

## Recursos

- **Playwright MCP (oficial):** [https://github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)
- **Documentación Playwright:** [https://playwright.dev](https://playwright.dev)

## 🎙️ Transcripción

Cloud Code siempre fue brutal en una cosa, [música] crear. Crear código, crear automatizaciones, hacer deploy de agentes y básicamente lo que le pidieras lo construías. Pero había algo en lo que era terrible y ese algo era diagnosticar problemas en la interfaz o simplemente navegar en las interfaces. Todo lo que incluía meterse un navegador, es decir, debugar errores en aplicaciones web o automatizar las acciones en la web que no tienen appis o conexiones directas o mcps o alguna manera oficial de conectarse, Cloud Code no servía. Si querías entrar a tu school a sacar métricas, no podías. Si querías navegar el dashboard de algún cliente, no podías. O si querías operar algún tipo de aplicación como lo haría un humano, simplemente no podías hasta ahora, porque ahora tenemos una aplicación que se llama Playwright. Y esta aplicación es brutal y vino a cambiar el juego completamente de las automatizaciones y el debugooging y de cómo usamos Cloud Code hasta el día de hoy. Este es literalmente el último eslabón que faltaba para poder realmente automatizar todo, porque hoy día ya no necesitamos que un servicio tenga una API de conexión, no necesitamos que tenga un MCP, no necesitamos estar creando scrapers a medida, simplemente le das un navegador a Cloud Code y lo usa como lo estarías usando tú. Pero esto es superdinto al computer use clásico que ya conocemos. No es ese sistema lento que se demora media hora en ejecutar una acción, toma un pantallazo, vuelve para ejecutar otra acción, toma un pantallazo, vuelve, se confunde con cada actualización y después vuelve con un error. No, esto es otra cosa. Y ya te voy a mostrar por qué. En este video te voy a mostrar qué es Playwright realmente y por qué es mucho mejor que Computer Use en el 99% de los casos. Segundo, ¿cómo lo conectamos a Cloud Code en menos de un minuto? Tercero, tres casos de uso reales que estoy usando yo para scrapear métricas de mi school, un servicio que era casi imposible antes porque no tiene una API pública para debuguear errores en mi dashboard interno y en el sistema operativo que tengo corriendo. También cómo lo conecto a Google Trends para planear mi contenido, siendo este un ejemplo perfecto de una aplicación que no tiene API ni MSP y la única manera de poder sacar data de ahí era haciéndolo manual, es decir, puros casos de verdad, no un juguete. Y cuarto, te voy a mostrar un bonus de cómo conectarlo a Cloud Code Routines para realmente poder automatizar tareas en piloto automático sin que estés ahí abriéndote la posibilidad a cosas que antes simplemente no se podían. Así que si te quedas hasta el final, vas a salir aprendiendo a usar una herramienta que te permite crear automatizaciones que antes ni siquiera te podrías haber imaginado. Vamos de lleno. Pero antes te agradecería un montón si me dejas un like en este video. Le metimos bastante bastante esfuerzo y de esta manera le dices también a YouTube que este tipo de videos te interesan y te empieza a recomendar más videos que realmente aportan valor y además también me ayudas a mí, así que vendría siendo un win win. Ahora sí vamos de lleno con Playwright Má Cloud Code. Antes de mostrarte cómo tengo que explicarte un poco el problema. Antes cuando usábamos Cloud Code teníamos dos maneras de conectarnos a distintos servicios. La primera, a través de las APIs, ahí una aplicación o un servicio expone un endpoint, se conecta a través de un token y le dices a Cloud Code, "Okay, comunícate con esta aplicación y ejecuta alguna de estas herramientas o tools." Y el segundo es a través de el MCP, que es una versión que está lista y optimizada para los LLMs. El model protocol se conecta directamente a servicios como cloud y cumple el rol de traductor universal entre el agente y la herramienta. un poco más a detalle de esto en el video de Agente Gia en 18 minutos. Pero acá está el problema. Hay muchas aplicaciones web o muchas aplicaciones que directamente no tienen una API de integración o un MCP. En Imperio, por ejemplo, mi comunidad school, si es que quiero sacar data, tengo que estar sacándola manualmente porque no tengo ninguna API o MSP para conectarlo. Tendría que literalmente armar un scraper desde cero, adaptarlo cada vez que haya una actualización o un nuevo frontend y rezar para que no me bloqueen la cuenta de School. o Google Trends, por ejemplo, lo uso para ver qué tanto están buscando un keyword en específico en todo el mundo en Google, pero sabes qué es lo que pasa, no tienen API pública, solamente a través de una aplicación de las cuales aceptan a pocas personas. Y aquí es donde la gente diría, bueno, usa Computer use, pero no funciona bien, realmente gasta un millón de tokens porque estás literalmente sacando un pantallazo y después mandándolo y navegando y pantallazo y mandándolo. Toma el screenshot, lo interpreta con visión, mueve el mouse, después toma screenshot, lo interpreta con visión. Después hace clic, toma screenshot y al final para ejecutar una acción de 20 pasos se demora 20 conversaciones, se demora mucho, es caro y es lento. Y esto es lo que vino exactamente a resolver Playright, un navegador real integrado con Cloud Code en este caso que actúa a través del accessibility tree en vez de a través de píxeles, lo que es realmente un gran cambio. Y Playwgright es un proyecto open source que como podemos ver acá es de Microsoft y mira lo que sale acá. Reliable web Automation for testing, scripting and AI agents. Si te fijas, tienes acá tres opciones. Tienes el Playwright test, que es para hacer E2I, que no nos sirve en este momento. Tenemos el Playwright CLI, que sí nos interesa, y el Playwright MSP, que nos permite tener acceso a, creo que más de 20 tools para ejecutar acciones dentro de el navegador en este caso. Y lo interesante acá también es que, como podemos ver, puede usar distintos navegadores. Puede usar Chrome, puede usar Edge, puede usar Firefox, puede usar Safari y los puedes correr acá de dos maneras. Tenemos los headless y tenemos los headed. Esto es básicamente si es que quieres que se vea lo que está ejecutando a nivel de interfaz o si es que no quieres que se vea a nivel de interfaz. Y una de las diferencias más importantes de este video antes de pasar a instalarlo y mostrarte los casos de uso reales, es que tenemos que entender que esto no es computer use. Computer use, que lo vimos en el video de Cloud Cowork, funciona así. Toma un pantallazo, lo manda a un modelo de visión. Ese modelo de visión dice cuál es el script de lo que tiene que hacer. Mover el mouse acá. Okay. Después se devuelve un pantallazo y dice, "Okay, ¿qué tenemos que hacer ahora?" Tenemos que apretar. Okay. Y devuelve otro pantallazo o ejecuta la acción y después devuelve otro pantallazo y así continuamente. Pero al final el problema que tiene es que es bastante lento, es bastante caro también porque usa muchos recursos y si la página es dinámica y cambió aunque sea un poco, ya no va a funcionar. Mientras que Playgright es completamente distinto, porque Playright no está mirando píxeles, sino que mira el accessibility Tree o el árbol de accesibilidad. Y esto es una representación visual de la estructura, es decir, todas las páginas lo tienen, de cómo está estructurada una página web. Y, de hecho, también se aplica y se usa para la gente que tiene discapacidad visual, pero lo importante es que rescata cada uno de los elementos como los botones, los links de navegación, dónde hace clic, todo lo que son los inputs, lo que son los forms, todo eso tiene un nombre. Así que en vez de decirle al computer use, haz click en la coordenada 845 raya 641. Después de haber analizado una imagen con visión, le dice, haz clic en el botón submit o haz clic en el botón enviar o haz clic en el botón regresar, ya que lo entiende de una manera mucho más rápido que analizar una imagen. Lo mejor es que no se confunde porque es algo determinístico, ¿ya? O sea, como que no es una imagen que puede pasar como un proceso de visión y confusión, ¿verdad?, en la interpretación de la imagen, sino que es determinístico, ya que es texto. Y esto es algo que la gente no está entendiendo bien, porque playwght no es computer use mejorado, sino que es una categoría completamente distinta porque no está entendiendo, no es el mismo sistema, otro sistema completamente distinto y para el 99% de los casos que vas a querer automatizar, scrapear datos, automatizar, rellenar formularios, navegación, testeo de buging, es objetivamente superior, ¿ya? O sea, Computer use podría seguir teniendo su trono, digamos, en aplicaciones como con interfaces más ligadas a, no sé, Photoshop quizás o Illustrator, no sé, en específico, bien cómo sería, pero para algo que esté en un navegador, ¿no? En una aplicación local como Photoshop, por ejemplo, debería ser superior, debería ser superior en el 99% de los casos. Okay, esto que estamos viendo acá es la página oficial y si es que entramos al MCP, podemos ver que se instala con un simple comando que vendría siendo este de acá. Entonces puedes correr ese comando, pero yo prefiero decirle lo que vamos a hacer. Así que voy a entrar a Cloud Code. Ya sea estás en VS Code o estás usándolo en Antigravity o a nivel de terminal o en la misma aplicación de Cloud Code, que creo que está funcionando bastante bien, vas a entrar y le vas a decir, "Necesito que me investigues." Una vez que lo investigues y entiendas toda su documentación, vamos a integrar el MCP. Entonces, léelo, entiéndelo y después vamos a empezar con la conexión. Y esto es lo interesante porque funciona muy bien. No tienes que poner tu cuenta, no tienes que hacer nada, no tienes que ni siquiera sacar una API porque Playright es un proyecto open source y funciona excelente. Me voy a preguntar si es que quiere que haga el fetch. Para este caso le voy a poner omitir permiso, ya que no no me interesa que me esté preguntando todo el rato y quiero que tome decisiones autónomas. Y aquí me va a decir que Playwght ya está conectado porque lo conecté previamente, pero en el caso de que no lo hayas conectado, simplemente te va a decir que ya se conectó. Aquí te dice resumen ejecutivo, framework, que es playrght, que es playgrid mp, los tools que tenemos disponibles, las capabilities que no están activadas en este momento y las tres formas de controlar el browser que vendría siendo cómo está funcionando. Entonces, si es que no lo has activado y lo quieres activar, probablemente vas a tener que reiniciar cloud y abrir una nueva sesión, ¿verdad? Esto lo puedes hacer cerrando la aplicación y volviéndola a abrir. De hecho, cuando yo lo instalé por acá, podemos ver que fue literalmente búscame Playwrght, Sus Dogs MSP e impléntalo. Y literalmente lo hizo. Y si te fijas acá ya está listo para llegar y usar. Tenemos los tools que están disponibles por acá, tenemos capabilities opcionales que podemos meter y esto es lo importante. Tenemos distintas formas de controlar los browsers. Tenemos el Playbright msp, clouding Chrome y el computer use en este caso. Entonces también tenemos integrado el computer use. Acá el que nos interesa acá es el Playwgright MSP. Hagamos una prueba en una nueva sesión y vamos a irnos acá y voy a decirle usando Playwrite necesito que entres a Google Trend y veas las cosas que están en tendencia en los últimos 30 días. vayas anotándolo todos los días y después me digas como cuáles son los que están en aumento. Invéntale una clasificación, alguna especie de criterio para la creación de contenido. Es importante que veas cosas como Cloud Code, que veas cosas como Cloud Design, OpenCla, Antigravity y todas las herramientas al final principales necesarias que tenemos que estar cubriendo y que estamos viendo para ver cuándo tenemos un aumento en la parte de creación de contenido. Luego me las vas a ir etiquetando, me las vas a ir guardando y esto lo vas a hacer todo este scraping vía playbright. Entonces ahora lo que hicimos es estamos empezando con el proceso de automatización de scrapeo de data en Google Trends, que es el primer ejemplo que vamos a ver. Aquí me escribo mal cloud, es la única diferencia, Cloud Code y aquí también cloud design, ahora sí. Y open [música] antigravity y todas las herramientas al final principales necesarias que tenemos que estar cubriendo. Okay, lo vamos a hacer todo vía playground. Al final générame un archivo Trends Daily con la fecha de hoy y dame una recomendación para el video de hoy. Okay. Si ves acá al final le dice que sea modo headed. ¿Por qué modo headed? porque queremos ver qué es lo que está haciendo por fines de este video. Podría hacerlo de headedless, es decir, como que lo haga en atrás y no estéis viendo lo que estoy haciendo, pero como estoy grabando el video, quiero ver cómo lo hace para que tú también puedas ver cómo es el proceso de navegación. Entonces voy a cargar Playrght y empezar a scrappear Google Trends en Moonhead para detectar las tendencias relevantes para tu contenido. Si te fijas, ahora lo que hicimos es creamos un prompt, pero después lo que podemos hacer si es que llegamos a la fórmula perfecta de scrapeo o de lo que sea, podemos crear un skill. Entonces, si es que nos damos cuenta de que hizo todo esto bien, aquí voy a ponerle omitir permisos. De que lo hizo bien, después podemos pedirle, "Okay, ahora necesito que me crees un skill para que hagas siempre esto de la misma manera." o seas determinístico en el proceso de creación de esta parte. Entonces, así lo que hacemos es creamos una especie de SOP y de guidelines que podemos tener en cuenta ahí como referencia para poder al final sistematizar y poder hacer de esto un sistema que funciona y que es replicable. Entonces, mira, aquí entró, ya buscó cloud, entonces nos puso acá dentro de el mundo en los primeros 30 días y ahora podemos ver que debería empezar a agregar nuevas vistas para ir comparando. Una cosa interesante también de Playwright es que si es que ves que está haciendo algo mal, tú le puedes ir diciendo aquí mismo, sobre todo cuando lo conectas con Cloud Code. Entonces, suponte que acá podemos ver datos de Cloud Code capturado. Tenemos un Pck en abril o en 33. Había evento breakout por cloud source leaked, ¿verdad? Guardo snapshot y sigo con el siguiente query. Y aquí podemos ver que ya empezado a buscar cloud design, pero supongamos que ahora quiero que no sé que salga y no los busque como por separado, sino que empiece a buscarlos en paralelo. Lo voy a decir, empieza agrupar distintos términos dentro de la misma búsqueda para tener marco y referencia de comparación. Luego vas guardando esos también. ¿Ya? Entonces, si te fijas, tenemos una tarea que era tienes que hacer esto hasta esto, pero entre medio lo interrumpimos con un prompt. Y fíjate, aquí lo que está haciendo es va a empezar a tomar este mensaje antes de que complete y lo va a tomar como referencia. Entonces, mira, Cloud Design tuvo lanzamiento. Acá tuvimos un P de 100, ahora va bajando y ahora está empezando a incorporar esta distinta instrucción que nos entrometimos a la mitad de Entonces, fíjate, ahora sí nos dice, buen punto, agrupo términos dentro de cada búsqueda. Reganizo el plan en cuatro grupos comparativos en vez de 12 búsquedas sueltas. Entonces ahí está como haciendo la reorganización de el cloud Code en este caso o de el Google Trends. Vamos a mantenerlo acá. Vamos a ver cómo lo hace. Y también, obviamente, como esto está corriendo en background y abre su propio navegador, ya, o sea, no no no toma control de tu navegador actual, sino que abre su propio navegador, podemos ir haciendo distintas tareas, ¿verdad? Podemos ir abriendo acá, entrando, creando otra sesión y mientras sigue trabajando lo podemos dejar trabajando. Y fíjate acá ya tenemos como va agrupando los primeros, o sea, ha avanzado un poco más y está comparando Cloud Code con Cloud Design, con Cloud Skills, con Cloud Opus, con Antropic Appi y está haciendo como distintas separaciones o está haciendo las comparaciones que fue en los grupos que le pedimos directamente. por aquí va a seguir haciendo todo esto y fíjate aquí tomó también cursor AI, Winsurf, client continue dev GithitHub Copilot en este caso y está viendo también como las las diferencias en las cosas que están más trending. Entonces, yo ahora sé que no tengo idea. Kitubilot está con una buena proyección, está, digamos, subiendo el interés, está más gente buscándolo. Y fíjate lo rápido que es esto, o sea, ahora buscó literalmente los otros constructores como Antigravity, buscó acá Lovable, las diferencias, B New, B New está s super mal, se quedó como bastante atrás. Lo está bastante bien, pero como que lo Apple también puede ser un search term como como aparte, entonces no sé, pero ve cer. Fíjate qué interesante, Antigravity está arrasando en ese sentido. Después podría ser como compárame los de mayores búsquedas al final cuando termines con todos. Entonces, mira, empezó a hacerlo de hecho, justo como naturalmente empezó a buscar Cloud Code con Antigravity para poder compararlos. Y fíjate que en Cloud Code está comparándolo mucho más, hay mucho más buscada en Cloud Code actualmente que en Antigravity. Mira, lo volvió a separar. Busco también Open Cloud, Open Code y Cloud Skills. Mira, fíjate, Open Cloud, busco dos. Eh, Open Code lo están buscando bastante más que cloud skills. Y bueno, quizás tendría que refinar un poco como tener los mismos criterios de búsqueda. Si estamos comparando agentes IA que me busque, no sé, pues, Hermes con open cl con, no tengo idea, open code, ¿verdad? Y después como en CL buscar antigravity versus, no tengo idea, vs code, ¿verdad? Para ver qué es esto. Después, no sé, comparar Codex con cloud code, pero en fin. El punto y lo interesante que quiero que veas es cómo tenemos acceso a algo que no teníamos API previamente y eso creo que es como lo importante. Aquí me buscó Cloud Code, concursor con copilot, open code y antigravity. Y actualmente Copilot está lo están buscando bastante, pero también puede ser nuevamente como algo nuevo, puede ser como no es es una palabra más genérica, entonces no tenemos un indicio tanto como realmente esto, pero en fin, creo que se entiende un poco la idea de cómo armamos esta automatización, pero nuevamente no funciona solamente para scrapear datos. paréntesis. Todo esto me los va guardando todo en un en un archivo Markdown al final. Y mira lo interesante, o sea, como que al final nos terminó agrupando los que tenían más índices de búsqueda y nos los agrupó, cachá. Ahora podéis ver que no sé, pues copáis lo desta con mucho, pero nuevamente habría que eliminarlo en este caso porque no es referencia porque es una palabra que se puede usar para otras cosas. y nos está creando el Jason, que vendría siendo como toda la información que recopiló relevante. Y fíjate que después de unos minutos ya literalmente volvió con todo esto, con el final ranking, con el ranking absoluto, nos dice como los hallazgos principales. Por ejemplo, aquí me recomendaría un video. Andre Carpati publicó sus cloud skills y hay un skill cavem que está polándose más. Combina dos breakouts simultáneos de contenido en español. Super interesante. Si es que abrimos acá, podemos abrir el PNG que nos acaba de generar, que lo voy a abrir justamente acá. Y tenemos el archivo Markdown, si es que se lo queremos alimentar algo, o tenemos los snapshots. Y aquí sí podemos ir viendo cómo cómo nos agrupó todos los snapshots de la información en el caso de que quisiéramos verlo. En fin, creo que está bastante bastante interesante, pero nuevamente no nos sirve solamente para scrapear, sino también nos sirve para debuguear y probar cosas. Por ejemplo, dentro de la comunidad school tenemos algo que se llama el de Imperio y aquí es al final un buscador porque el buscador de school funciona s super mal. De hecho, si es que tú buscas algo, acá tienes un keyword based search. ¿Ya? Entonces, si es que no sé, busco open cloud y lo busco acá después y busco open class separado, nos aparecen menos resultados. En cambio, si es que yo busco acá tutorial de OpenC, va a hacer un rack based system, es decir, como un buscador mejor, ¿verdad? Para poder buscar las cosas y encontró los siete post y todo. Y bueno, eso fue al final como todo el sistema de cómo entramos acá y esto me manda, ¿verdad? por ejemplo, acá, no sé, al ceteo y a la sección completa de Open Cloud Imperio, pero al final toda esta interfaz la creé directamente con Cloud Design, entonces tenía que estar probando, tuve que estar cambiando muchas cosas, viendo si funcionaban, viendo si no y ahora voy a pedirle a Cloud Code que llegue con Playwrght y me haga un debuging completo. Entonces, voy a copiar acá el link y voy a entrar acá a Cloud Code. Entonces, voy a entrar una nueva pestaña y el dolor que tenía al final era que Cloud Code nunca podía ver como la UI. es decir, la navegación. Entonces, siempre habían distintos books. Ahora le puedo decir algo por el estilo de esta es una aplicación que tenemos que es Imperio Agéntico, que es una comunidad o un software para los miembros de la comunidad. El problema es que hay bastantes bugs, de repente hay cosas que no están bien y necesito hacer un diagnóstico de UI y que me vuelvas con las cinco mejoras directas que puedo empezar a implementar. Desde ya te voy a dejar el link a continuación. Entra, te voy a dar acceso a mi cuenta y vas a entrar y vas a empezar a ejecutar las cosas. ¿Okay? Esto también es importante y relevante porque acá, por ejemplo, estamos entrando en una cuenta ya y por default Playwright lo que hace es abre un nuevo navegador que no tiene acceso a tu cuenta. Entonces fíjate, voy a entrar al sitio, acaba de abrir esto y nos pidió una cuenta. Notoriamente nos va a decir acá, "Okay, tengo que empezar a usar una cuenta." Vamos a darle la opción de sacar un snapshot y se va a dar cuenta de que en este caso necesita una cuenta para poder usarla. Entonces aquí voy a llegar yo y voy a iniciar sesión directamente. Entonces aquí ya está dentro como enjamín y ahora sí empieza a hacer este especie de computer use. ¿Ya? Entonces para este caso sí tiene que ver la interfaz, tiene que entender la navegación y puede usarlo y también está incluido dentro de Playwright. Entonces lo está haciendo. Entonces aquí hay layout de tres columnas. Voy a revisar que me perdí otras secciones y si es que estuviese corriendo el proyecto de Imperio Argéntico, que es este dashboard, junto a Playwright puede ir haciendo los cambios en vivo. Entonces, podemos darle autonomía en ese sentido, lo que es realmente una maravilla. Esperemos unos segundos y vamos a ver qué nos trae. Que se note paréntesis que todo esto lo está haciendo solo. O sea, entró, preguntó cuál es el club anual, empezó a preguntar directamente y yo no estoy haciendo absolutamente nada desde acá. Ahora solito ajustó su resolución y está probando en móvil. O sea, fíjate como la pantalla que está acá esta, yo no tengo control y ajustó completamente su resolución. Yo creo que está en mobile. Y mira, faltan dos botones de navegación clave, ¿verdad? Que son el leaderboard y mi perfil. Faltan las sesiones, concurso, perfil y todas esas cosas se pierden en móvil. Yo, la verdad, no tenía idea que se veía tan mal en móvil. Voy a tener que hacer un par de cambios aparentemente, pero en fin, creo que se entiende un poco hacia dónde va esto. Y después de unos minutos, aquí tenemos el diagnóstico. Mira, mobile está roto a nivel navegación, solo se ven tres botones. Mi perfil se ve el dueño vacío. No sé por qué no cargo esta vez. Llamadas N+1. Okay, aquí me dio todas las cosas que yo podría llegar y podría pasárselos a mi otro proyecto de Cloud Code y podría hacer el debuging que antes no estaba haciendo. No lo tengo acá porque lo tengo corriendo en el Macmenia ese y está scrapeando constantemente la data de school. Está superinesante, pero en fin, si estuviese conectado podría ir implementando estas mejoras y autoalimentándose constantemente. Entonces, si tienes el plan Max, puedes dejarlo así, auto o retroalimentándose constantemente y nada, va optimizando todo el tiempo. Lo que me lleva al tercer caso y es que no solamente se conecta con aplicaciones que no tienen APIs o MCPs o que te mejoran las interfaces, sino que también le podemos sacar valor real del día a día. Voy a mostrar algo que no tiendo a mostrar mucho, que es un poco las métricas de la comunidad de Imperio, pero al final creo que es un caso superútil que mucha gente va a poder ver como un caso real y es como yo estoy usando Playwright y sacándole mucho valor día a día. Entonces, voy a entrar acá y le voy a decir algo por el estilo de necesito empezar a scrapear mis métricas de school, específicamente el conversion rate, es decir, cada cuántas personas que entran hay una tasa de conversión y se vuelven miembros de Imperio Digital. Necesito sacar día a día, ya que no me aparece la opción de descargar esto. Entonces, necesito sacar día a día, entrar vía playbright. Te vas a settings, ajustes y ahí te van a aparecer las métricas. centro de las métricas aparece el conversion rate y ahí tienes que hacer un hover por encima de cada día en un puntito y ahí te va a aparecer, vas a registrar cada uno de los días y después me vas a volver con cada una de las métricas de los días del conversion rate. Okay, ahora sí vamos a ver si es que nos tomó todas las palabras bien. Debería porque llevo un tiempo ya usando mi app de voz a texto, entonces debería ir ajustándose y entrenándose con las palabras que voy usando. Eh, de interior digital play. Okay, school me lo tomó bien. Playgright conversion rate. Perfecto. Buenísimo. Okay, ahora sí vamos a hacerlo. Va a entrar, va a probar aquí nuevamente. Si es que no lo está haciendo visible, podemos entrar y pedirle explícitamente que lo haga headed. Así que ahora sí voy a abrir school y navegar. Primero arranco el navegador. Vamos a ver ahora cómo se abre. Si es que no se llega a abrir es porque lo tenemos que hacer headed. Entonces, para este caso no estoy viendo que se abrió. Ya, entonces no lo tenemos acá. y voy a reformular el prompt porque no le dije que lo haga headed, entonces voy a volver a hacerlo y voy a pedirle acá hazlo headed, es decir visible. Entonces, estando acá, vamos a ver cómo lo toma y cómo lo hace. Ahora sí podemos ver cómo entró y ya está dentro de la comunidad de Imperio Digital. Debería irse a la derecha. Ahora yo no estoy haciendo nada. Vamos a achicar un poquito esto. Vamos a achicar esto también un poco al costado y vamos a ver cómo está navegando en tiempo real. Yo estoy sin absolutamente nada. O sea, tiene que entrar a settings, tiene que entrar a el hover de cada una de las cosas. Entonces, aquí nuevamente entra School, empieza a verlo, me dice que encuentra el botón de settings ahí al costado. Llegó a las métricas, fíjate, hizo clic aquí en el conversion rate, scrolleó hacia abajo para poder verlo completo, eh, hizo un hover de prueba. Y esto, esto me encantó porque no es que tenga que ejecutar 31 acciones para cada uno de los días, a diferencia del computer, use, que es saca pantallazo, muévelo, pasa, saca pantallazo, muévelo, pasa, sino que está probando esto acá. El funcionó ahora los 31 días en una sola corrida. Fíjate lo que está haciendo en ese momento. Tac, tac, tac, tac, tac, tac, tac. Registró cada uno de esos. ¿Ya? Y esto es una diferencia clave con el computer use. El computer use hubiese tomado 31 pantallazos, esto no, sino que es un script que hizo como tac, tac, tac, tac, tac, tac, tac, y pasó por cada uno de los días porque entendía que tenía que hacer un hover para registrarlo. Entonces, recién mandó el input de hacer la acción de 30 hovers encima de cada uno y después devolver la información y ahora está guardando el Jason localmente para armarme el reporte. Y okay, aquí tienes los datos de los conversion rates individuales por cada uno de los días. Después ya podemos hacer lo que queremos, podemos literalmente, no sé, tomarlos, cruzarlos con otros datos, etcétera. Y en todo esto nos demoramos 5 minutos sin escribir código, sin tener que estar manualmente haciendo hover sobre las cosas. Y aquí hay un dato clave que aplica también a este caso y al caso de Google Trends y a los otros casos, ¿verdad? del dashboard también y es de los persistent profiles. La primera vez que armas un flow y te logueas en una cuenta en específico, los cookies quedan por un determinado tiempo. De ahí en adelante ya Cloud entra directamente a través de Playwrite y ya no te empieza a pedir la clave constantemente porque quedaste abierta en esa sesión. Supongamos que me gustó esto y queremos hacerlo ya algo un poco más estandarizado y no tener que hacerlo. Vamos a decirle, creemos un SOP en formato skill para que sea replicable. Entonces, ¿qué está haciendo ahora? Literalmente eso está creando un SOP en formato skill para que sea replicable, para que no tengamos que darle el prompt constantemente y que sea como, "Okay, ejecuta el skill análisis de school." Entonces ahí lo ejecuta, lo guarda y se replica, que es lo que es como lo importante. Y aquí está el combo que realmente hace a Playwright imparable, imparable. Si es que lo combinamos con los cloud code routines, es decir, esa función de cloud que aparece aquí arriba en un costado que lo lanzaron para automatizar cosas dentro de esa infraestructura y usando los servicios de cloud, Playwright se vuelve realmente imparable. ¿Por qué? porque puede empezar a ejecutar acciones dentro de routin sin que esté directamente tú. Entonces acá, por ejemplo, Daily School Scrape. Revisar el contenido de conversion rate de school usando Playwright. Entra school, scrapea las métricas del día, perfil settings, conversion rate, saquemos el promedio solo mensual. Todos los días lo vamos a hacer a las 2 pm. Entonces, supongamos que queremos ejecutarlo en este momento para hacer la prueba. Le voy a dar acá a ejecutar ahora. Y podemos ver que ya está en ejecución. Mandó un mensaje aquí a nuestra conversación. Ahora lo estoy haciendo a nivel local, pero también puede ser a nivel de nube si es que quieres ejecutarlo siempre. Y aquí tenemos, mira, está usando el browser navigate. Aquí tenemos que, bueno, dejarlo siempre en omitir permiso en este sentido. Está usando el browser navigate, está entrando, sacando los browser tabs, etcétera. Si es que quisiéramos hacerlo exactamente lo mismo, pero a nivel de nube, la lógica es exactamente la misma, o sea, es literalmente lo mismo. Hacemos acá school daily updates, no tengo idea. Acá entra a schools, scrapea vía playwrite mp ejecuta xxx. Okay. Selecciona un repositorio. Vamos a elegir el repositorio. Supongamos que es este. Vamos a conectarlo a las cosas que queremos. Vamos a crearlo y debería estar también haciendo lo mismo, entrando vía Playwrite, haciendo un server headedad probablemente porque no interesa que lo estés viendo en ese momento, y ejecutando el playrht para hacer el scraping o la tarea que le solicites hacer. Y con esto podemos hacer un millón de cosas que antes no podíamos hacer. Antes era imposible. Necesitábamos un servidor que estuviera 247 corriendo abierto, ¿verdad? Teníamos que crear un script que ejecutara las acciones, un sistema de monitoreo o quizás algún Chromejob. Teníamos que asegurarnos que el frontend no cambiara y hoy día ya esto es distinto. Son literalmente dos promps, uno para playrght y otro para la routine. Podemos armar monitores de competencias automáticos. Por ejemplo, en vez de estar usando Apify, puede entrar a Amazon y scrapear precios. Podemos armar un bot de school que entre y que esté viendo las publicaciones para poder después extraer data de qué está funcionando. No tengo idea. En otras comunidades podemos hacer que entre a marketplace y que esté buscando constantemente oportunidades. O si estás en el mundo de real estate y de bienes inmuebles o no sé, venta o barriendo de propiedades, puedes estar haciendo exactamente lo mismo, entrando y buscando oportunidades si es que tienes tu routine o tienes algún Mac Mini por ahí lo dejas prendido. Entonces, Playwright al final te da estos ojos que Cloud Code antes no tenía directamente o que tenía que usar computer use y no gastaba mucho. Y antes de cerrar, porque siendo honestos y en este canal siempre intento de serlo, también tiene algunas limitaciones que tenemos que tener en cuenta. Primero, el MCP Playwright usa tokens, o sea, al final estamos ejecutando muchas acciones y es caro, no es tan caro como computer use, pero igual te va a usar tokens. Cada acción está metiendo el accessibility tree de cada modelo y una sesión completa podría gastarte 100,000 tokens fácil. Entonces, si vas a usar esto en tareas largas, también puedes considerar el CLI de Playwright directamente. Este es de la gente que usa el CLI, no como MCP directamente y puede gastar hasta cuatro veces menos token según lo que he investigado. Segundo, hay ciertos sitios que tienen eh seguros antibot, sobre todo las plataformas como bancos, como ciertos retailers o las plataformas que tienen, no sé, algún cloudfare muy agresivo. No sé si, por ejemplo, la compra de pasajes en ciertas aerolíneas y en la mayoría de las ocasiones Playwright tiene la manera de mitigar eso ya, es decir, funciona, pero en ciertas ocasiones también los podría detectar si es que es algo muy avanzado, pero la mayoría de los casos funciona superb, pero es importante conocer que también existen ciertas limitancias en ese sentido. Y tercero, también requiere iteración, o sea, casi nunca vas a sacar un flujo excelente al primer intento. Muchas veces vas a tener que conversar, seguir iterando, seguir probando y al final de eso se trata. La gracia es que cada intento va a ir siendo mejor y cuando sientas que llegaste ya a la perfección o a lo más decente, vas a pedirle que te cree un script o un skill que en table y crea una especie de SOP o standard operating procedure de cómo se productiza este sistema, por así decirlo, o estandariza, mejor dicho, este sistema. Dicho eso, para el 95% de los casos que te interesan a ti, scrapear data, probar errores, encontrar bugs y hacer debuging de plataforma, ejecutar acciones, hacer investigaciones que antes no podrías, automatizar tareas repetitivas, ¿verdad?, en la web y todas las acciones y conexiones a aplicaciones que antes no podías usar porque no tenían API o MSP, te va a servir bastante bien. Esto era lo que le faltaba a Cloud Code para ser ya realmente imparable. Así que sé que puede haber sido mucha información, pero para recapitular, Cloud Code es increíble creando, pero es muy malo diagnosticando problemas en interfaces y Playwright vino a literalmente cerrar esa brecha, no con computer use, sino con accessibility tre, que es más rápido, más barato y más confiable. lo conectas directamente entrando a Cloud Code y diciendo, "Conéctame con Playwrght MSP o dándole ejecutando ese comando para hacerlo." Luego, si es que llegas y combinas esto con routins, puedes dejar ciertas cosas automatizadas sin la necesidad de tu estar ahí. Y como te dije a la mitad del video, los promps que usé de acá también los tengo publicados en el Playwright Starter Pack dentro de Imperio, además de una guía paso a paso de todo lo que hicimos y cómo lo puedes setear por completo para ti y casos de uso. Así que si te interesa mantenerte al tanto de lo que está pasando en el mundo de la IA y las automatizaciones, recomiendo que te des una vuelta por Imperio, donde tenemos alrededor de cinco sesiones semanales, cursos de cloud code, cloud design, antigravity y open cloud. y puedes llegar a construir softwares como Einar, que logró construir aplicaciones para una industria de millones de dólares, Tomás, que está muy agradecido de estar en Imperio, o David, que reemplazó una agencia completa usando Open. Y si todavía no has visto el video de routines de cómo automatizar cosas en cloud, te lo voy a dejar acá. Y si quieres ver el curso más completo de Cloud Code en español completamente gratis, también te lo voy a dejar acá. Te agradecería mucho tu like en este video y nos vemos en la próxima.
