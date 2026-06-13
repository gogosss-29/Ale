# 👑 [GUIA] Configura tus Anuncios Cinemáticos

> Ruta: Automatizaciones n8n › 👑 [GUIA] Configura tus Anuncios Cinemáticos

**🎬 Vídeo (18.0 min):** https://www.loom.com/share/2ca9f684ac1c40d49bc9a893355bda7a

**📎 Recursos:**
- Plantilla Concept Board
- Plantilla n8n Ads Cabrones
- [Plantilla Airtable](https://airtable.com/invite/l?inviteId=invBaulIxzkCuW8E3&inviteToken=67eed0831f09e9e696400d074cdc39730f72d8fdced82389823c9466e59e8633&utm_medium=email&utm_source=product_team&utm_content=transactional-alerts)
- [Gema Personalizada Director](https://gemini.google.com/gem/18dwvNrz2zkkZFbce5zeD19VQLaXqb6TY?usp=sharing)

---

Aquí les dejo el paso a paso técnico para dejar funcionando la automatización de los "Anuncios Cabrones". Sigan este orden para no perderse con las credenciales.

### 1. Descarga los Archivos Base

Lo primero es tener los materiales a mano. Al final de esta guía, van a encontrar cuatro archivos clave

- El **Concept Board** (imagen de referencia)
- La **Plantilla de n8n** (el archivo .json)
- La **Plantilla de Airtable** (la base de datos)
- *Opcional:* Acceso a la gema personalizada si la requieren.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/151f1abd71bc452fac0eb380bac29386a6325ae402f54e6185643ca0ff479331.png)

### **2. Configuración de Airtable**

- Abran el link de la plantilla de Airtable y hagan una copia en su propia cuenta para poder editarla
- Vayan a **Developer Hub** en Airtable para crear un nuevo Token
- **Ojo aquí:** Al crear el token, asegúrense de agregarle **todos los scopes** (permisos) disponibles (lectura, escritura, esquemas, etc.) para que la automatización no falle después
- Agreguen la base que acaban de copiar a los permisos del token y guárdenlo en un lugar seguro

### **3. Importación y Ajustes en n8n**

- En n8n, creen un nuevo workflow e importen el archivo "Ads Cabrones" que descargaron
- **Importante:** La plantilla viene con nodos configurados con un nombre específico (ej: "Ads Cabrones IA"). Es muy probable que tengan que actualizar las credenciales en cada nodo de Airtable dentro del flujo, seleccionando su propia cuenta conectada

### 4. Conexión de las APIs (El motor de la IA)

Necesitamos conectar tres servicios clave. Para Wavespeed y las APIs genéricas, usaremos el tipo de autenticación "Generic Bearer Auth"

- **Airtable:** Usen el token que crearon en el paso 2
- **OpenRouter (Modelos de Texto):** Creen su cuenta, saquen la API Key y conéctenla en los nodos correspondientes
- **Wavespeed / API Key (Imágenes y Video):** Vayan a su perfil en Wavespeed, generen una API Key, cópienla y créenla en n8n como una credencial "Generic Bearer Token"
- **ElevenLabs (Voz):** Busquen la voz que les guste (filtren por español para mejores resultados), copien el "Voice ID" y péguenlo en el nodo de voz antes de generar.

### 5. Ejecución del Flujo (Cómo operar la máquina)

La automatización funciona por etapas para que tengan control creativo:

1. **Dirección Creativa:** Llenen los datos en Airtable (producto, referencias) y ejecuten para generar los prompts y escenas
2. **Revisión:** Si les gustan las escenas propuestas en Airtable, denle el visto bueno.
3. **Generación de Medios:** Ejecuten nuevamente para crear imágenes, luego videos, música y voz.
4. **Lógica de "Done":** El sistema revisa los checkbox de "Image Done" o "Video Done". Si una escena ya está lista (tiene el check), la automatización se la salta para no gastar créditos extra. Si quieren regenerar algo, simplemente desmarquen esa casilla.

---

Dudas?

Dejen sus preguntas en los comentarios de este mismo hilo para ir resolviéndolas en orden y que todos aprendamos.
