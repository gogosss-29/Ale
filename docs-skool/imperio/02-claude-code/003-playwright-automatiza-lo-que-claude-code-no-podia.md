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
