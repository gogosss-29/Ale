# 🔍 Encontrar Leads y Envía Mails con IA (Básico)

> Ruta: Automatizaciones Make › 🔍 Encontrar Leads y Envía Mails con IA (Básico)

**🎬 Vídeo (9.6 min):** https://www.youtube.com/watch?v=U_78UFwrX7c

**📎 Recursos:**
- Auto Prospección Leads con ChatGPT

---

En este post, te mostraré cómo utilizar la inteligencia artificial para generar miles de leads y automatizar el contacto con ellos. Este método es ideal para agencias de IA o de marketing, pero puedes adaptarlo a cualquier nicho o profesión. Sigue estos pasos prácticos para poner en marcha tu sistema automatizado.

#### Paso 1: Buscar Leads en Google

1. **Definir tu búsqueda**: - Abre Google y prepara tu búsqueda usando la siguiente plantilla: ```
"profesión o nicho" "@gmail.com" OR "@outlook.com" OR "@yahoo.com"
```
- Utiliza `OR` para incluir diferentes dominios populares en tu sector. Esto aumenta las posibilidades de encontrar más emails relevantes
- *Cada palabra entre "comillas" es un filtro de búsqueda. Si le agregamos el OR entre  dos filtros que están con comillas, es encuentra alguno de los que estén al costado. Si no le agregamos el OR, es filtra por cada uno de los resultados que estén entre comillas. *.
- Ejemplo para restaurantes: ```
"Restaurant Chile" "@gmail.com" OR "@outlook.com" OR "@yahoo.com"
``` Bonus
- Si le agregamos antes el "site:[instagram.com](http://instagram.com)", solamente nos mostrará perfiles de instagram. Esta página puede ser reemplazado por cualquier página que estimes conveniente. Por ejemplo: ```
site:instagram.com "Restaurant Chile" "@gmail.com" OR "@outlook.com" OR "@yahoo.com"
```

#### Paso 2: Copiar Resultados de Búsqueda

1. **Seleccionar y copiar resultados**: - Una vez que Google muestre los resultados, selecciona toda la página utilizando `Ctrl + A` y copia con `Ctrl + C`.
- Abre ChatGPT y pega los resultados copiados.
2. **Repetir para más páginas**: - Ve a la segunda página de resultados de Google.
- Repite el proceso de seleccionar (`Ctrl + A`), copiar (`Ctrl + C`) y pegar en ChatGPT.
- Haz esto para al menos 4 o 5 páginas de resultados.

#### Paso 3: Crear una Tabla en ChatGPT

1. **Pedir a ChatGPT que organice los datos**:

- Utiliza el siguiente prompt en ChatGPT para organizar la información: `Crea una tabla con los datos anteriores en estas columnas: Nombre, Nombre de la empresa, URL de la web, Correo electrónico, Número de teléfono, Instagram.`
- *Aquí incluirás solo las variables que encuentres relevante.*

1. **Revisar la tabla generada**: - ChatGPT devolverá una tabla organizada con todos los leads extraídos.

#### Paso 4: Transferir los Datos a Google Sheets

1. **Copiar la tabla**: - Selecciona la tabla generada por ChatGPT y cópiala.
2. **Pegar en Google Sheets**: - Abre Google Sheets y pega los datos copiados en una nueva hoja de cálculo.

#### Paso 5: Automatizar el Envío de Correos con Make

1. **Configurar Google Sheets en Make**: - En Make, añade un módulo de Google Sheets.
- Selecciona "Watch New Rows" y elige el documento y la hoja donde pegaste los datos.
- Configura el límite de filas a 1 para enviar un correo a la vez y evitar ser marcado como spam.
2. **Configurar el módulo de Email en Make**: - Añade un nuevo módulo de "Send an Email".
- Conecta tu cuenta de correo electrónico.
3. **Personalizar el Asunto y el Contenido del Email**:

- En el campo del asunto, utiliza el nombre del destinatario:
- `Por ejemplo, propuesta para {{Nombre completo}}`
- En el contenido del correo, personaliza el mensaje.

1. **Configurar el Envío**: - Configura Make para enviar un correo cada x minutos para evitar ser marcado como spam. (En este caso, es recomendable elegir una mayor cantidad de tiempo para que no te detecten como Spam).

![15.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/22816f1d3edc4ba0bfc52a7073665536b9aaa4d1f47242848d24684a1a1c13f1-md.png)

Siguiendo estos pasos, puedes crear un sistema automatizado y eficiente para generar y contactar leads de cualquier industria o nicho. Este método no solo ahorra tiempo, sino que también incrementa la eficacia de tus campañas de marketing.
