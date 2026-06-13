# 🤮Crea Anuncios de Texto en Masa | Canva + Make

> Ruta: Automatizaciones Make › 🤮Crea Anuncios de Texto en Masa | Canva + Make

**🎬 Vídeo (23.3 min):** https://www.youtube.com/watch?v=nsq1k_uzX-E&feature=youtu.be

**📎 Recursos:**
- Ads Horribles v2 (en masa)

---

Si estás corriendo anuncios en Meta (Facebook, Instagram) y sientes que cada vez te cuesta más mantener tus campañas rentables… no estás solo. Lo que antes funcionaba, hoy muere rápido. No es problema de tu producto, ni de tu targeting. El problema es que **el juego cambió**.

👉 Meta ya no premia al que mejor segmenta… sino al que **más rápido lanza nuevos anuncios.**

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/425d83c5f47a4291a3057a081c209b17ea3c63965db348eb983d8c4313a4430b-md.png)

La realidad es brutal: **los anuncios se fatigan más rápido que nunca.** Si no produces nuevos creativos cada semana, tus campañas empiezan a perder rendimiento, tus costos suben y tus ventas bajan. Lo sabes… lo has visto en tus dashboards.

Pero aquí viene el verdadero dolor:  
❌ No tienes un diseñador disponible 24/7.  
❌ No quieres perder horas creando piezas en Canva.  
❌ Y pagar una agencia cada semana es insostenible.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c66950f0e9af45389b04e9a8f2a10c92a1004db3763f44f69b13ae05206b2864-md.png)

Por eso nació esta solución. Un sistema probado que usan agencias top y media buyers de todo el mundo: **“Ugly Ads”**. Creativos ultra simples, fondo blanco, texto grande, CTA claro… que literalmente **rompen el patrón y venden.**

Y la mejor parte: hoy te damos la guía completa y la automatización lista para que puedas crear tus propios Ugly Ads **en masa, en minutos y sin diseñador.**

🚀 Este blog no es teoría. Es un paso a paso que conecta Canva, Google Sheets y Dropbox con [Make.com](http://Make.com), para que tú o tu equipo generen 10, 20 o 50 anuncios por semana… **sin tocar un solo diseño manualmente.**

Prepárate. Porque después de esto, nunca más vas a depender de freelancers, agencias ni de tu propio tiempo para tener anuncios listos, frescos y rentables.

---

**PASO A PASO**  
Primero, crea una copia del siguiente [template ](https://www.canva.com/design/DAGrYHH5JRk/5R2BYsaf7kQd3AFHhN57Jw/view?utm_content=DAGrYHH5JRk&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink&mode=preview)en Canva

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6c0bee5fe95b4db7b7677824cc503c87dfcf562243734adeaf56c474427f41ff)

Entra a ChatGPT o chatbot de preferencia,  y pégale el siguiente prompt:

IMPORTANTE: Las variables de arriba, recomiendo rellenarlas y personalizarlas con tu información. Esto si es que NO tienes un GPT entrenado con al info de tu empresa. Si lo tienes, recomiendo pegarselo directamente ahi y mencionarle que tiene toda la info en su entrenamiento.

> # VARIABLES A RELLENAR  
> 
> (Escribe tu información y **no** borres los corchetes dobles).
> 
> - {{NOMBRE_COMUNIDAD_O_EMPRESA}}  
> 
> - {{DESCRIPCION_BREVE}}    *(¿Qué hace, a quién ayuda?)*  
> 
> - {{MOTIVADORES_CLAVE}}   *(Ej.: ahorrar tiempo • escalar negocios • conseguir leads …)*  
> 
> ---
> 
> ## SYSTEM_PROMPT TEMPLATE  
> 
> ERES EL MEJOR CREADOR DE “UGLY ADS” DEL MUNDO, RECONOCIDO POR META (2024) COMO CASO DE ÉXITO GLOBAL.  
> 
> TU MISIÓN ES GENERAR **10 ANUNCIOS ULTRA SIMPLES** —FONDO BLANCO, TEXTO GRANDE Y MENSAJE CLARO— PARA **{{NOMBRE_COMUNIDAD_O_EMPRESA}}**, {{DESCRIPCION_BREVE}}.
> 
> ### INSTRUCCIONES PRINCIPALES  
> 
> DAME **10 ANUNCIOS**, CADA UNO COMPUESTO POR **5 BLOQUES**:
> 
> 1. 🔺 **BLOQUE SUPERIOR (8 PALABRAS EXACTAS)** Gancho directo.  
> 
> 2. 🔷 **BLOQUE CENTRAL (19 PALABRAS EXACTAS)** Beneficio o promesa (finaliza con **punto**).  
> 
> 3. 🔻 **BLOQUE INFERIOR (2 A 5 PALABRAS)** CTA contundente.  
> 
> 4. ✏ **PRIMARY TEXT (≤ 125 CARACTERES)** Copia para Meta: breve, conversacional, máx. 2 líneas, 1 emoji opcional.  
> 
> 5. 📰 **HEADLINE (≤ 30 CARACTERES)** Beneficio clave + CTA; capitalización tipo Título.
> 
> 2. **ASEGURA** comprensión total en < 5 segundos.  
> 
> 3. **USA** tono humano y orgánico (parece post nativo, no corporativo).  
> 
> 4. **REFLEJA** LOS MOTIVADORES CLAVE DE TU AUDIENCIA: {{MOTIVADORES_CLAVE}}  
> 
> 5. **ENTREGA** LA RESPUESTA COMO **TABLA MARKDOWN** con las columnas:  
> 
>    **N° | Bloque Superior | Bloque Central | Bloque Inferior | Primary Text | Headline**  
> 
>    y **10 filas (un anuncio por fila)**.
> 
> ### CADENA DE PENSAMIENTO OBLIGATORIA  
> 
> 1. **ENTENDER** la misión de {{NOMBRE_COMUNIDAD_O_EMPRESA}} y las necesidades de su público.  
> 
> 2. **DESTILAR** los beneficios principales (tiempo, escala, dinero, etc.).  
> 
> 3. **DIVIDIR** el mensaje en gancho, beneficio, CTA, primary text y headline.  
> 
> 4. **VERIFICAR** que los bloques tengan **exactamente 8 / 19** palabras y el CTA 2-5 palabras.  
> 
> 5. **ENTREGAR** la tabla final.
> 
> ### MEJORES PRÁCTICAS  
> 
> **Primary Text** – Pregunta o promesa, máx. 2 líneas, verbo de acción, cifra concreta, ≤ 125 caracteres.  
> 
> **Headline** – 3-6 palabras impactantes, mayúsculas iniciales, CTA implícito (“Escala Sin Equipo”, “Ahorra 10 H/Semana”).
> 
> ### QUÉ NO HACER  
> 
> - NO usar más o menos de **8 / 19** palabras en los dos primeros bloques.  
> 
> - NO exceder **5** palabras en el CTA ni los límites de caracteres en Primary Text y Headline.  
> 
> - NO añadir diseños complejos ni texto pequeño.  
> 
> - NO prometer resultados irreales.  
> 
> - NO omitir CTA ni usar jerga confusa.
> 
> ---
> 
> ### EJEMPLO (CASO *IMPERIO DIGITAL*)  
> 
> | N° | Bloque Superior (8) | Bloque Central (19) | Bloque Inferior | Primary Text | Headline |
> 
> |----|--------------------|---------------------|-----------------|--------------|----------|
> 
> | 1 | ⚙ Automatiza tu negocio sin código hoy mismo | Guías, plantillas y comunidad generan leads automáticos, escalan ventas globales, liberan horas diarias y multiplican tus ingresos rápidamente sosteniblemente. | Prueba gratis ahora | Escala con Imperio Digital: automatiza tareas, genera leads y libera horas diarias. 🚀 Únete gratis. | Escala Sin Código Ya |

Una vez que lo envíes, te dará un resultado así

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0cb84cd72d7e44de8de0d82ee729d2465448e0f853d142fd9081a055de3dab65-md.png)

Luego, copiaremos eso y lo pegaremos en un Google Sheets, si gustas puedes crear una copia de este [aquí](https://docs.google.com/spreadsheets/d/1bWNfzQlWMvkGyIORgdF7FUhmvhRar-AYfI6DI6H0CIs/edit?usp=sharing)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/bda016a5312d475e84c1b76c4378155627cbf6a72e764accb2c69ac406e32abb-md.png)

Luego volveremos a la [plantilla](https://www.canva.com/design/DAGrYHH5JRk/5R2BYsaf7kQd3AFHhN57Jw/view?utm_content=DAGrYHH5JRk&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink&mode=preview) previamente duplicada, y nos iremos a "bulk create"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/aabc6ab907934764875c8c4ab393a8e30cd90a49f73c4ea6af80bd15455e31ad-md.png)

Iremos a "Enter Data Manually"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4ca6808673ff4a3f9f0af07f64d2d355777a617910164e9b8f640c1681573ad2)

y copiaremos "ctrl + c" y pegaremos "ctrl + v" la tabla que creamos previamente

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/5ee6140bca49453c9524750a14a06d3d407566fb8c7e4b01bdd84ff21c3414e9-md.png)

Le daremos a "Done" y asignaremos cada bloqeu a cada columna. Esto lo haremos haciendo clic derecho en el bloque superior, y dándole a "connect data"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/269900be507f4afa8eb68116568d8766a6e00c6716674a2db1f83875e4552aaf)

aqui cruzaremos la data de "bloque superior" con el primer subtítulo de arriba

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/495e12c6fd6f4f21a845562016aca829d07d4694af74439d8ce1bfee47ca4a22-md.png)

Haremos lo mismo para el bloqeu central (clic derecho en el texto del bloque central + connect data)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/170b027702074af48cf4dcee5894c9d7b63ee18a21e44452a4d9f39b657ff5ac-md.png)

Y finalmente lo mismo en el bloque inferior

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c383ca1921af4ea9b69bc16408ae87abee6b899448db4e1d84ae1666c3e365e3-md.png)

Una vez listo, le daremos a "continue".

Deseleccionaremos el primer número "1" y le damos a "Generate Designs"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2a0f8434a01e4fecbf3f103e2840e5e4f188d00c3e914a8ba7d59771f53a996e-md.png)

Nos dirá esto

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/bc410de9e1b148b69eaf6a619c4d48a24b7c8e8a16934a668dd0d0c7fa7a240a)

Volveremos al inicio y crearemos uan carpeta que se llame "Ugly Ads" o el nombre que quieras

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3da6bf2191c04600a8b7a29ef4372ab822f0dae78637444f8aa5c3dbf0bee3ed-md.png)

y arrastraremos el archivo generado a la carpeta

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ebf7451607024f01889c0feaa36cafaf07fed393f3c843e490036626befdd946)

Ahora entraremos a [Make.com](http://Make.com) e improtaremos la automatizacion que está al final de esta pagina

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/3282dc058a324131a8a88f38dcb09dc70217010846e244e186d42335ce6a82ed-md.png)

Importar, plantilla

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/dcea1a8bc40b43258b3cc6c8f656ca4f3758735de0494aba88c85ee47b3f70eb)

Pero de todos modos, si quieres ver los parametros y lo que hay que poner, te los dejaré aquí. Primero, comenzaremos con un "repeater", y este valor "10" lo reemplazaras por la cantidad de ADS que decidiste crear, es dec ir, la cantidad de filas. El valor irá aumentando + 1 cada vez que se ejecute.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/360029eb09544a83b7b395008f04bcdf24e460657a1a4ddfb20a43a680124ca8)

Luego agregaremos el canva de "Export a Design", donde se exportan los diseños de la automatizacion que ya hicimos.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a7f93d9dcc2c4c529f093a12a1fa919300df9dffc95c43939a348b32634d8a24-md.png)

Personalizaremos los parámetros según lo que necesitemos. Para este caso 1080 x 1080 y en formato PNG está bien. "Export as a single image" pondremos "No" para que no se exporte como una imagen larga, sino varias distintas.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/375b0a0f3a134ac1a00e0de33d371db1cf2f021b0cb647648e27f5cf0d821595-md.png)

Luego lo subiremos a Dropbox, para esto le pondremos que el nombre será i (seleccionado del repeater) .png (o el formato que elegimos).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/eb0ea859250346648f37b238ae12a3d4eb03e8ea89154320a0625e709c5a1346-md.png)

NOTA: Si te está presentando algún error relacionado a los "missing scopes" al conectar nuestra cuenta de dropbox, puedes revisar esta publicación de aquí: [Error Dropbox Missing Scope 401.](https://www.skool.com/imperio-digital/classroom/a65de4cd?md=3d858f2b1048492f8de11236ca3882f8)

Aqui pondremos el URL

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/6247fe9610c849caa9e7e8d9f88ddc29baa57502bfa04585a615b58f985347f5)

Le daremos a "Guardar" y "Run Once"

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/2a9e5db13d27428a882b2d51a158193a3ec3653666ae46d8a2c0ff2c795686bc-md.png)

Haciendo que cada vez que se genere o complete una creación, se actualice el Google Sheets con la informacion respectiva.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/bebe59bbc8314df5966d39cbc333a174c1a0149f11ce427389f42782e5bdd9ca-md.png)

Dándonos algo así

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d524809d58e54d538b0f0e21675070a7d1e63af183494a72b8a893a7b228d38b-md.png)
