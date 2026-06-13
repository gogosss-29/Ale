# Nodo 1: Schedule Trigger (El Despertador)

> Ruta: n8n Desde 0 › Nodo 1: Schedule Trigger (El Despertador)

**🎬 Vídeo (4.5 min):** https://www.loom.com/share/99014a9a79ce4ee3b51f7981ea3a1649

**📎 Recursos:**
- 1. Schedule Trigger - Dólar DIario

---

### **1. Schedule Trigger**

**Qué es:** El "reloj despertador" de tu automatización. En Make es cuando le haces clic al relojito debajo del primer módulo para decirle "Run every 15 minutes". En n8n, es un nodo explícito.

**Para qué sirve:** Para iniciar flujos basados en el tiempo, no en eventos externos (como recibir un correo).

**Ejemplo Concreto (Para recrear ahora mismo):** Vamos a simular un **"Monitor de Dólar Diario"** (o de lo que quieras revisar rutinariamente).

**Pasos para recrearlo:**

1. Arrastra el nodo **Schedule Trigger** al lienzo. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d3870cae65724e389395e94f661b4d79f098a3adca39496686f5b293a76c34f9.png)
2. Ábrelo y configura: - **Trigger Interval:** Days
- **Time:** 09:00 (o la hora que quieras).
- **Mode:** Every Day.  
 ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c3e4f12780c44df2aeb0abd8d13b7af8ab4a61866fb84cffbb2c0c3c51a7b0e4.png)
3. Conecta un nodo simple después, un **HTTP Request** que consulte una API pública).

Así se configura el nodo **HTTP Request**:

1. Agrega el nodo **HTTP Request** a tu canvas y conéctalo después del *Schedule Trigger*.
2. Ábrelo y configura solo esto: - **Method:** Déjalo en GET (porque vamos a *pedir* información).
- **URL:** Pega esto: [https://mindicador.cl/api](https://mindicador.cl/api)
- **Authentication:** Déjalo en None (esta API es pública, no pide llaves).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/114dd9c320ed4e778f911db3dbd7013715c72c12020a4c74889d3074bdfb0acf.png)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e844403f125f44e496412d8038e09dbc24324447b5a7402b9019e742c6588504-md.png)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/947bc28da743404390ca1ca9327929918f57d73b69ad46e296d76d5b5087f5b0-md.png)

Agregamos el gmail

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c2564d253e6948ce9cc92fca8fc97bbbac185a0fb89a4b67ada97e13a31ffd87-md.png)

Arrastra la variable desde la izquierda a la derecha que queremos. Para este caso haremos dólar.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/913a5f05ee2843d58783584beee524bb3e62715c49a3469da3bbaf0701f3795a-md.png)

**Resultado:** Todos los días, a las 9 AM en punto, n8n se despierta y ejecuta lo que venga después. Sin que tú muevas un dedo. Es la base para reportes diarios o limpiezas de bases de datos nocturnas.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/a7a43b869207452a87452674ed266d3b247729d966d44813b15b3d7cd5a400b5-md.png)

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/dbe220f963064fa395bd93f182e38d1f7eff3604c4d540a685c405b4d89db49c-md.png)

## 🎙️ Transcripción

A continuación, vamos a ver uno de los quince nuevos que te van a permitir construir tu 8020 en automatizaciones en N8N. Es decir, el 20% de los nuevos que te van a ayudar a construir el 80% de tus automatizaciones. Pregamente, vimos que teníamos lo que son los disparadores. Los disparadores son los que ejecutan un flujo de trabajo dentro de N8N. Tenemos disparadores anteventos, tenemos disparadores ante webcooks y ahora vamos a ver el disparador ante tiempo. Es decir, es como una pequeña alarma que todos los días o con la frecuencia que nosotros queramos va a ejecutar un escenario en específico. Aquí dice que agregamos un nuevo no y uscamos el schedule trigger, nos va a aparecer algo así, es justamente esto que está acá y aquí podemos poner el trigger según cada cuánto tiempo queremos que se ejecute. Por ejemplo, aquí tenemos el trigger que queremos que se ejecute a las 1, 2, 3, etcétera y a la hora en específico, pero también puede hacer que se ejecute cada cierta cantidad de días o cierta cantidad de segundos, ok? Para este caso voy a eliminar este que está acá y te lo voy a mostrar con un escenario bastante sencillo. Este escenario lo que hace es todos los días a una determinada hora, en este caso como puedo ofer acá, a las 9 a.m, todos los días me va a mandar el precio del dólar, ¿por qué? Porque va a ejecutar esta parte que sal acá que es una piabierta de el precio del dólar en Chile, donde me da el precio en UF y el precio dólares y después me va a mandar el correo electrónico y ya tenemos conectado en nuestra cuenta de Google, tenemos conectado instalado en 8 vena, así que debería funcionar bastante bien. Voy a ejecutarlo una vez, podemos ver que llamo a la API, se devolvió al correo y ahora si es que entramos en correo electrónico, metida el precio de la web y no solo eso, sino que la tasa de desempleo, el dólar, etc. Si quisiera volver a crearlo, simplemente pondría acá el que yo trigger aquí vamos a ponerlo que se ejecute no sea las 10 de la mañana por ejemplo y vamos a empezar a armarlo aquí alaito vamos a mandar acá queremos que se ejecute ya con llamados htp ok vamos a conectarnos a mind api.cl esto era donde está en específico lo voy a sacar de acá no más queremos que saque la api de mind api aquí podemos hacer lo que sea podemos poner cualquier módulo, vamos a ejecutar el paso y vamos a ver que me devuelve aquí el precio de el dólar en moneda de chileno, el euro, el IPC, etcétera, después vamos a enviarnos un correo electrónico, acá nos vamos a ir a Gmail, vamos a bajar, vamos a buscar send a message, vamos a dar a enter y vamos a mandarnos el correo a nosotros, ok, me va a mandar a uno de mis correos que están acá, chimey.com, perfecto y le vamos a poner el dólar, está a y vamos a bajar acá, voy a buscar el dólar en específico, donde está el dólar acá, el intercambio y vamos a o el valor mejor dicho y lo vamos a poner justamente acá, ok, el dólar está a x, pesos chilenos, lo va a poner, en el asunto lo va a poner un punto y ahora si es que le voy a guardar, ya el imino esto que aparece justo acá, voy a eliminar el escenario anterior y le doy a guardar y lo voy a publicar, lo voy a publicar, todos los días a la hora en específico que le di acá se va a correr la automatización, bastante importante que sepas en qué horario está a tu N8N para que se adapte a la hora en específico. ¿Por qué? Porque a veces tenemos el N8N en otros horarios y queremos enviarlo a cierta hora y se envía con tres horas de redrazo o cuatro horas de redrazo. Y también lo puedes cambiar en el caso de que sea así. Y así funciona el schedule trigger es un disparador bastante sencillo, bastante sencillo y aquí lo podemos modificar como queramos. Podemos ponerlo en minutos, en horas, en semanas, ¿verdad? o en meses, en semana, sería ciertos días en específico dentro del día. O sea, acá ahí le voy a poner quiero los lunes, martes miércoles, jueves, piernes, no los domingos, y que se mande en específico a lássico de la mañana. Y así sería. En esta plantilla, tomo las a encontrar pública dentro de los nodos de schedule clear.
