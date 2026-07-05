# Diseño de bases de datos en Airtable

> Ruta: 🔴 Grabaciones › Diseño de bases de datos en Airtable

**🎬 Vídeo (57.7 min):** https://www.youtube.com/watch?v=b8FK3CPjO8w

---

## Problemas que resuelve

Cómo estructurar correctamente datos en Airtable sin romper información, cómo separar carga, lógica y visualización para evitar errores humanos y cómo construir sistemas simples pero escalables usando tablas relacionadas, formularios e interfaces sin exponer la base de datos al cliente.

---

## 🧠 Intervenciones

---

### [00:01] Franco – Introducción y objetivo de la sesión

Presenta la sesión de viernes enfocada en Airtable como herramienta base para sistemas reales. Explica que el objetivo no es algo avanzado, sino entender bien los fundamentos que suelen generar errores más adelante.

---

### [02:06] Franco – Qué es Airtable y por qué usarlo como base de datos

Explica Airtable como una base de datos relacional, no como una planilla.

**Problema**  
Usar Google Sheets como base genera:

- Errores humanos
- Datos sensibles expuestos
- Automatizaciones frágiles

**Solución**  
Usar Airtable como:

- Base de datos central
- Fuente de información para agentes de IA
- Sistema estructurado y escalable  
Define Airtable como “Sheets con esteroides”.

---

### [06:02] Franco – Estructura de datos y relaciones entre tablas

Muestra ejemplos reales de bases con múltiples tablas relacionadas (clientes, feedback, movimientos).

**Problema**  
Datos aislados que no se pueden cruzar ni medir correctamente.

**Solución**  
Crear tablas relacionadas:

- Un registro conecta con otro
- Datos coherentes
- Escalabilidad real  
Permite medir información entre tablas sin duplicar datos.

---

### [09:31] Franco – Separar dato, carga y visualización

Introduce el concepto central de Airtable.

**Problema**  
En Google Sheets:

- Todos editan el mismo lugar
- Se rompen fórmulas
- Se borran datos críticos

**Solución**  
Dividir el sistema en tres capas:

- **Dato** (backend, no accesible)
- **Formularios** (carga controlada)
- **Interfaces** (visualización para el cliente)  
Evita errores y pérdida de información.

---

### [11:27] Juana – Caso práctico: peluquería y carga de clientes

Consulta cómo usar Airtable para que una peluquería cargue nuevos clientes y se conecte a un asistente automatizado.

**Problema**  
El cliente necesita cargar datos sin acceso a la base completa.

**Solución**  
Usar formularios conectados a la base:

- Carga simple
- Sin acceso a tablas internas
- Datos listos para automatización o IA

---

### [13:20] Franco – Creación de sistema desde cero (clientes, citas y pagos)

Construye una base en vivo para una peluquería.

**Problema**  
Poner todo en una sola tabla impide:

- Medir ingresos
- Saber deudas
- Escalar el sistema

**Solución**  
Separar en tablas:

- Clientes
- Citas
- Pagos  
Vincularlas mediante record IDs para mantener coherencia.

---

### [17:40] Franco – Uso de IDs y relaciones automáticas

Explica el uso de auto-number como identificador único.

**Problema**  
IDs manuales generan errores y duplicados.

**Solución**  
Usar IDs automáticos:

- Cada registro es único
- Relaciones estables
- Menos errores humanos

---

### [20:22] Franco – Cálculos y lógica sin IA

Implementa fórmulas para:

- Total pagado
- Total adeudado
- Valor de vida del cliente

**Problema**  
Intentar resolver cálculos simples con IA genera errores innecesarios.

**Solución**  
Usar lógica y fórmulas:

- Más rápido
- Más preciso
- Más barato  
Se corrige un error generado por IA en vivo.

---

### [27:09] Franco – Medición real del negocio con datos conectados

Muestra cómo ver:

- Cuánto pagó cada cliente
- Cuánto debe
- Cuántas citas tuvo

**Problema**  
Datos sueltos no permiten decisiones claras.

**Solución**  
Tablas conectadas + fórmulas → métricas reales en minutos.

---

### [33:24] Franco – Construcción de interfaces para clientes

Crea una interfaz visual para la peluquería.

**Problema**  
El cliente no puede interactuar con tablas internas sin riesgo.

**Solución**  
Interfaces personalizadas:

- Visualización clara
- Edición controlada
- Uso tipo app  
El cliente ve solo lo necesario.

---

### [37:06] Franco – Optimización de vistas y campos visibles

Ajusta qué información se muestra y cuál no.

**Problema**  
Mostrar demasiados campos confunde y no aporta valor.

**Solución**  
Diseñar vistas:

- Solo campos útiles
- Orden lógico
- Mejor experiencia de uso

---

### [42:08] Franco – Formularios para agregar citas y pagos

Agrega botones y formularios dentro de la interfaz.

**Problema**  
El cliente necesita cargar información sin romper relaciones.

**Solución**  
Formularios guiados:

- Citas
- Pagos
- Validaciones automáticas  
Evita pagos duplicados y errores.

---

### [45:54] Franco – Restricciones lógicas para evitar errores

Filtra citas que ya tienen pago.

**Problema**  
Un cliente puede cargar pagos duplicados.

**Solución**  
Filtros lógicos:

- Solo permitir acciones válidas
- Evitar inconsistencias en datos

---

### [48:12] Franco – Creación de formulario para nuevos clientes

Muestra cómo crear y compartir un formulario externo.

**Problema**  
No se pueden crear nuevos clientes desde la interfaz directamente.

**Solución**  
Formulario externo:

- Link público
- Integrado al sistema
- Accesible desde la interfaz

---

### [51:23] Franco – Sistema mínimo viable en menos de una hora

Resume el sistema construido.

**Problema**  
Creer que estos sistemas requieren semanas.

**Solución**  
Con buen diseño:

- Sistema funcional en 40 minutos
- Escalable
- Listo para automatizar o integrar IA

---

### [54:52] Rosa – Duda sobre Make e imágenes

Consulta por un problema técnico con imágenes que no se muestran.

**Solución**  
Se aclara que no es un problema de plan ni de soporte, sino de implementación técnica. Se propone resolverlo en detalle el martes.

---

### [57:36] Cierre

Franco confirma que las grabaciones quedan disponibles en la plataforma y cierra la sesión deseando buenas fiestas e invitando a continuar el trabajo en la próxima clase.

## 🎙️ Transcripción

Impecable. Bueno, buenísimo. Para la gente que lo está viendo grabado, estamos a 19 de diciembre, ya terminando el año y una sesión de viernes que vamos a ver un tema específico. Bien, vamos a hacer algo por ahí bastante, no sé si básico, pero sí algo que que es muy muy importante de poder ver y poder aprender bien, que es Ata Table. Bien que muchas veces lo están viendo, unos no igual que acá dentro de todos somos pocos estamos Juana y tengo acá a Sens que no me acuerdo tu nombre está muteada pero pero bueno ahí de última podríamos hacer algo un poquito cómo soy Rosa. Rosa, ahí está. Me acordaba que eras de España, pero no acordaba tu nombre. Gracias, Juana. Rosa de todas formas, igual al ser pocos podemos aprovechar es a ver algo como si estuviéramos haciendo los partes. Bien, a ver, acá se van uniendo más, pero vamos a ver, vamos a tratar de llevarlo lo más dinámico posible. Bien, vamos a voy a compartir acá un segundo. Sí, una pregunta. Sí, cómo no. Este, en al final al finalizar te puedo hacer una pregunta sobre una automatización. Sí, seguramente haya seguro que haya tiempo para eso. Seguro que sí, porque somos somos pocos. Vamos a aprovechar, vamos a repasar un poquito de table y después a partir de ahí vemos de de aprovechar el tiempo como cómo vaya surgiendo la idea de los viernes, así queda bien todo el contenido y demás, es que se hable de un tema específico. Sí. Eh, pero a partir de ahí, siendo que que nada, esto estamos a fin de año, eh, podemos aprovechar un poco el tiempo y avanzar por ese lado. Bien, vamos a vamos a mostrar un poco esto. Denme un segundo que ahí voy a abrir el miro. Ya varios saben que nosotros usamos mucho table para un montón de de funcionalidades y realmente repasamos muchísimo table, eh, pero es importante poder verlo bien. Acá tenemos eh a ver, a ver, a ver, a ver, a ver, quiero encontrar el flujo que lo tenía y se me perdió, me parece. Vamos a ver. Okay, acá sí. Bien, voy a compartir pantalla. Me A ver, coméntenme si se ve bien ahí. ¿Se está viendo bien la pantalla? Ahí es. Bueno, vamos a ver un poco esto de table. Primero que nada, para la gente que no conozca table, vamos a repasar un poco la plataforma. Solo tenemos acá table, tenemos diferentes clientes y demás diferentes bases. Vamos a abrir alguna que esté dentro de todo decente. Vamos a ir acá. Este es de un cliente nuestro. Sí. Y como ven acá ustedes van a abrir el table y tenemos cuatro puntos acá: data, automatización, automatizaciones, interfaces y formularios. Básicamente table es una base, es una base de datos, una tabla, como ven acá, que tenemos diferentes hojas, bien, con diferentes cosas que vamos metiendo, que vamos usando y demás. Esto en particular es algo que usamos para apoyar a un bot, para apoyar a un agente de IA que tenemos conectado, que tenemos usándolo. Y acá lo que vamos a tener es diferentes formas de relacionar la información. Tenemos clientes acá, tenemos otras cosas, tenemos una biblioteca de información que ayuda a la gente de IA, tenemos un buffer de mensajes, que esto es algo muy específico. Y luego tenemos un poco más de información por otros lados, ¿no? Como esto, movimientos de los clientes. Esta es una de las bases. Si vamos, por ejemplo, a otra base de otro cliente, tenemos algo un poco más completo. Sí. Un poco más complejo también. Porque estamos ya viendo por ahí el flujo de trabajo de una agencia de marketing. Que vemos que acá tenemos los clientes de la agencia de marketing, tenemos los encargados, tenemos los media buyers, que son la gente que corre ads, diferentes consultas, clientes, un montón de información, pero como ven, nada, es algo que está bastante completo. Todo esto es la parte de atrás de Air Table. Air table es una base de datos que sirve para poder depositar y usar un montón de información. es muy similar a Google Sheets en un montón de situaciones, en un montón de cosas. Sí, es un formato de tabla, pero funciona bastante diferente en otros en otros puntos. Ahora vamos a meternos un poquito acá con el con esto, ¿no? Esta explicación de Air Table. Nosotros, ¿qué es lo que tenemos con Air Table? tenemos en un principio la manera más fácil de de de verlo, de escribirlo es sheets con esteroides, ¿sí? Google Excel con superpoderes, básicamente. Entonces, acá nosotros tenemos varias cosas que, como vimos recién, el punto central de Air Table es el dato, bien, que es esto que vimos acá, todo lo que vemos de esta parte, de esta parte de tablas son datos que tenemos diferentes filas con características que son las columnas y demás. Ahora, ¿qué pasa con el dato? Nosotros podemos hacer, por ejemplo, una estructura que los datos estén conectados uno con el otro, que esto que ven acá, ¿no? Por ejemplo. Entonces, tenemos por decir algo, que si vamos acá a tengo unos formularios de clientes cerrados. Estos son líneas de clientes cerrados y estos clientes cerrados están relacionados, son los clientes que cierran los clientes de la agencia de marketing en este caso. Entonces vemos que está relacionado, que acá abrimos y es un registro que, como ven, está conectado a un registro de clientes. Después vamos a, por ejemplo, feedback semanal. Y acá tenemos diferente feedback que dan los clientes que está conectado de nuevo a la tabla de clientes. Entonces, tenemos un registro por un lado que está relacionado y se puede medir con otro. Esto, ¿qué nos genera? Nos genera una estructura de datos donde hay un montón de cosas interconectadas que permiten que esto pueda escalar, que sea sostenible y que pueda tener una base de datos sólida y que realmente funcione de forma eficiente. ¿Sí? Esto con el tema de los datos. Ya muchos de ustedes conocen cómo funciona la estructura de datos. No nos vamos a meter mucho por acá, pero sí es importante que se pueda repasar un poco porque esta es la base de Ata table. Bien, todo esto es la parte que le da nafta, que le da información a Air Table que tenemos acá. Ahora, por otro lado, nosotros acá vemos que tenemos el dato, pero nuestros clientes no ven todos estos datos. Los clientes acceden ahí de otra forma que si quieren ingresar un dato, lo ingresan con un formulario, no es que se tienen que venir acá y ya les habrá pasado muchas veces que usan, por ejemplo, un Google Sheets entre muchas personas y alguien termina rompiendo ese goll Sheets porque no lo sabe cómo usar o porque se confunde de cierta forma y termina rompiendo y quitando progreso tal vez o perdiendo datos en un Google Sheets. Por eso es que nosotros no les damos acceso a esta parte, que como ven es sensible. Si yo agarro y borro acá, me permite borrar o puedo hacer un montón de cosas y no queremos que eso suceda. Entonces Air Table lo que hace para evitar esto, las herramientas que te da son estas dos cosas que vemos que son interfaces, que es donde acceden los clientes, que si ven es como una aplicación que se hace con diferentes datos, con métricas, con accesos para editar o no editar de un lado o del otro. Si lo vemos acá, también sucede lo mismo en la otra aplicación, que como ven, le mostramos los datos que tiene, pero solamente pueden verlos y si quieren ingresar un dato se hace con un formulario. Vamos a repasarlo acá un poco esto que es super importante. Vamos. Acá nosotros tenemos siempre esto, ¿no?, de que tenemos el dato, que era lo que hablábamos recién. El dato atrás es lo que es la nafta o la la el combustible del sistema que hace que funcione, que de una forma o de otra, pero no queremos que accedan a la parte de atrás que vimos recién. Entonces, para cargar datos, Air Table lo que hace es darte formularios. Mediante un formulario se carga un dato y entra a toda esta estructura. Pero eso permite que no tengamos que darle acceso a nadie a esta estructura de datos. De nuevo lo mismo. Ahora, para verlo nosotros tenemos la interfaz, que lo que hace la interfaz es permitir una visualización del dato. Sí, de nuevo, sin tener que meterse acá y empezar a ver todo. Porque, ¿qué pasa? ¿Qué pasa en Google Sheets? En Google Sheets vos tenés el dato vivo, tenés la tabla, tenés la información que vos en el mismo espacio estás cargando datos, en el mismo espacio estás viendo los datos y en el mismo espacio es lo que está dando la información o jugando con información sensible que hace cosas que se mueve o que sirve para tomar una decisión contable, para poder sacar una fórmula, para desatar automatizaciones y demás. Entonces, en Google Sheets tenemos todo en el mismo lugar. Acá en Table tenemos la posibilidad de dividirlo en tres, que es esto que vimos, la carga, el dato en sí y la visualización del dato. Sí, esto es algo que como ven por ahí uno lo tiene un poco naturalizado o o ya trabajando hace tiempo lo ves y nada, es s simple, pero es importante que esto quede claro, ¿sí? que realmente a la gente que por ahí está arrancando o que tiene alguna duda que puedan verlo bien y aclararse las dudas. Así que nada, vamos a ir un espacio acá. Igual primero, ¿hay alguien acá que nunca haya usado ver table? Todo el mundo buenísimo. Sir algo, yo estoy queriendo usarlo para una amiga que tiene una peluquería y que ella me ingresa datos. A eso le llama datos de nuevos clientes. Mm. Y para que este se puede conectar a table con una plataforma para un asistente que cada dato de nuevo cliente que entra a table, este cliente se le oferta o se le vuelva a contactar o qué sé yo. Okay, bien. No entendí mal. Sí, no es así. Es así. Okay. Table, justamente lo que hacemos es eso, es usarlo como nafta muchas veces para los agentes de IA, que permite tener la información de, bueno, este cliente entró hace un hace un mes, hace dos meses, este cliente debe x cantidad de plata o este cliente tiene esta información, lo que sea, pero funciona justamente para poder nada que que quede esa información guardada de una forma o de otra. Entonces, eso sirve muchísimo. Ahora vamos a ver algunas bases de table de agentes de IA, de cómo se ven y demás. Eh, ahora justamente sucede esto. Por ejemplo, Juana quiere, vamos a suponer que quiere hacerle un sistema a esta Juana va a ser la persona que esté atrás del sistema, la persona que esté armando el table, que esté armando las interfaces, los formularios y demás, pero no va a querer que su amiga vea absolutamente todo porque puede romper o porque puede ver más información de la que quiere o porque puede confundirse en el sistema. Entonces ahí lo que se hace es separar de nuevo la el dato de la visualización y por eso es que creamos una interfaz, ¿sí? que es lo que estábamos viendo recién. Vamos acá, vamos a volver a a esto. Y de nuevo para dar un último repaso es esto, ¿no? Lo que veíamos recién, que el dato es donde va a tener la información de los clientes, de bueno, de cuánto debe cada cliente, de si un cliente tiene una cita, por ejemplo, bien, lo que sea. Ahora, con este dato, nosotros no queremos que aparezca y que vea una tabla, sino que vamos a buscar la forma de armarle una interfaz para visualizarlo. Vamos acá, vamos a ir a, vamos a hacer una una de cero directamente. Así lo hacemos y se muestra bien todo. Creamos. Voy a crear acá base testeo Juana. Vamos a poner o base peluquería Juana. tenemos esto. Entonces, acá esto lo cerramos y vamos a tener una tabla primero, ¿no? Tabla clientes, donde vamos a tener el nombre del cliente. Después vamos a tener, por ejemplo, el número de teléfono del cliente y luego vamos a tener, por ejemplo, estado, que puede ser estado un estado de cliente activo o cliente inactivo y luego cliente activo. Y vamos a ver, por ejemplo, si queremos ponerle un detalle, ¿no? Eh, ya seleccionamos el tipo que tenemos. Bueno, tenemos eso también, ¿no? Ahora vamos a ver un poco los tipos de datos. Tenemos eh detalle. Si creamos un nuevo campo, que es lo que estuvimos haciendo acá, nosotros vamos a seleccionar qué tipo de dato va a tener el campo, si es todo esto. Tenemos un montón de opciones y tenemos que saber seleccionarlo. Bien, entonces acá, por ejemplo, vamos a poner nombre del cliente, franco, teléfono, pues estado activo, detalle. Franco se viene a cortar el pelo todas la todos los lunes, por ejemplo. Sí. Y así le proponemos Juana interactivo y así Juana va martes de por medio. Bien, lo que sea. Acá es más que nada para que vean el funcionamiento de la tabla, ¿no? La base, los datos atrás. Ahora vamos a suponer que nosotros queremos crear otra tabla que sea citas, ¿no? Y acá vamos a poner, por ejemplo, una un vamos a hacer una tabla relacionada. Vamos a relacionar las citas con los clientes porque ya justamente tenemos los clientes en otra tabla. Cada cita corresponde a un cliente. Entonces, tenemos que combinarlas, tenemos que vincularlas de una forma u otra. Entonces, en los tipos de dato para vincular, yo voy acá donde dice link to another record o vincular a otro registro. Y acá voy a tablas existentes, link a clientes. Acá pongo cliente nada más. Traigo el nombre por decir algo, nada más. Y acá tenemos fecha. Y vamos a ponerle fecha de la cita. Y tenemos, vamos a ponerlo de esta forma. Se formatea bien. Entonces, acá, ¿qué vamos a poner? Este es el campo primario, ¿sí? Que siempre tiene que ser único. Entonces, acá vamos a poner un auto number directamente. Que cada cita tenga un ID o ID cita. Esto sea un número nada más que se hace automáticamente. Ahora, ¿qué pasa si Juana tiene una cita, yo acá directamente le vinculo el cliente, busco entre los clientes que están acá, que son estos dos que hicimos, agarro que está Juana, esto se trae automáticamente y le digo, bueno, Juana va a tener el 22 de diciembre a las 13m. Bien, y acá ya tenemos dos registros, dos tablas que son la tabla de citas y la tabla de clientes que están vinculadas. Ahora, por otro lado, ¿qué pasa? Cada cita y así vamos vamos a ir un un rato, ¿no? Pero cada cita tiene un pago y por ahí esto es un sistema que pueda funcionar para eh para tener para registrar pagos, por ejemplo. Entonces, como pago es diferente a cita y a clientes, pero está vinculado a una cita, vamos a crear una nueva tabla acá que sea tabla de paus. Y acá, ¿qué vamos a hacer de nuevo? Vamos a poner en el en el en el campo primario le ponemos un número, un ID de pago. Luego le vamos a dejar, vamos a vincularlo directamente a en la a la cita. Entonces, si yo voy para acá de nuevo, vamos a lo mismo. Voy a vincular otro registro, selecciono la tabla de citas y vamos a ver. Y le pongo cita nada más. Es acá no traigo nada, no es necesario. Y de pago cita vamos a ponerle estado. Vamos a poner pagado o acá pagado en o sin o no pagado. Vamos a poner acá. Sí, apagado. Y por último, por ahí nosotros querramos guardar en este punto el comprobante del pago. Entonces, le ponemos un tipo de dato de attachment de de archivo y dejamos acá para que puedan cargar un comprobante y cargar una imagen. Bien. Y acá podemos vincular tranquilamente. Vemos que tenemos una cita de Juana que por ahí no está apagada y demás. Entonces acá vamos a ver que tenemos en la tabla de citas tenemos un vínculo a un cliente y vínculos a pagos. Entonces, ¿qué sucede con esto? Para hacer una pausa por ahí. Y lo que sucede con esto es que empezamos a tener datos coherentes. Empezamos a tener que cada cliente interactúa con una cita, con un pago. Si cada cita tiene un estado de estar pagado, cada pago tiene un estado de pagado, no pagado, ¿sí? Una cita también. Entonces, acá tenemos un montón de cosas que después podemos medir porque ahora yo muy el acá me falta el monto importante. Vamos a ponerlo eh acá monto o valor. Acá lo que podemos hacer, si está todo vinculado, yo puedo después ir a clientes y saber exactamente cuánta plata me rindió cada cliente, cuánta plata me debe Juana, cuánta plata me pagó Franco en el último año, pues está todo conectado y está todo hecho con registros. Entonces, esto es muy diferente y mucho más potente que el uso normal de Google Sheets, que por ahí permite hacer un montón de cosas, pero termina siendo un poco más complejo. Acá estamos profundizando un poco sobre la tabla y demás, y ahora vamos a ver, vamos a cargarla un poco más a la tabla y meternos en interfaces. Pero antes de eso, quiero primero confirmar que no fui muy rápido porque por ahí fui un poquito rápido y después ver esto, ¿no? De si se está entendiendo cómo funciona la relación entre tablas, cómo funciona table por atrás y demás. ¿Alguien un comentario de esto? Yo sí entendí. Muy bien. Bueno, me parece muy poderoso poder conectar y hacer listas coherentes porque así se uno habita evita trabajo, ¿verdad? Totalmente, totalmente. Vamos a creo que mis clientes van a hacer peluquerías. Muy bien. De 10. Bueno, buenísimo. Vamos a a llenar un poquito más esta tabla, así podemos medir y y sacarle bastante provecho a todo esto. Vamos a poner acá Pablo por el teléfono que sea. Acá le ponemos cliente activo, detalle, no importa. Vamos a crear varias citas. Sí, vamos a crear que, por ejemplo, Juana fue también va fue el 10, eh, que de nuevo que Juana fue el uno. Bien, vamos a ponerle a Franco, que Franco fue ahora hace poco, Pablo lo mismo. Y acá tenemos bien todo esto. Ahora, ¿qué pasa? nos quedan los pagos todavía, pues ya tenemos los clientes bien armados y tenemos las citas bien armadas, nos quedan los datos de pago. Entonces, para los datos de pago, vamos a crear acá un pago. Una vez que lo creamos desde acá, desde esta interfaz, ya nos ya lo vincula. Y acá vamos a ver y vamos a suponer que está por decirte algo, unos, no sé, 500 bien 500 lo que sea, ¿eh? O 100, así que un poco más más prolijo. Y tenemos acá que está apagado. Bien, acá vamos a hacer uno nuevo. Vamos a vamos a ir conectando todo esto, ¿no? 100. Esta puede salir 150 y está 100, lo que sea. Bien. sobre que esto está apagado y esto lo pagado. Vamos a hacer las vinculaciones a las citas acá que tenemos. Vamos a vincular acá y acá. Entonces, ven que todo se va enchufando, todo va conectando. Nos queda un pago acá para Pablo que tenemos, vamos a suponer que Pablo fue a hacerse la barba también y tiene 200 pesos en vez de 100 pesos nada más, pero todavía no lo pagó porque es para el 29 y estamos a 19. Entonces, reinando, tenemos los clientes que tienen sus citas, sus citas que tienen sus pagos, ¿sí? Y los pagos que tienen los montos. Entonces, ¿cómo hago yo para saber, por ejemplo, cuánto me rindió cada cliente? Primero tenemos que hacer ciertas sumas, ¿no? Primero sabemos que si está pagado ya podemos contar esta plata, ¿no? Entonces vamos a ir a la cita y vamos a traerle información de una tabla para mostrarla en otra. Vamos acá y tenemos los pagos. Y así como vemos que esto nos muestra el nombre del cliente, nos muestra algo de otra tabla, vamos a hacer lo mismo con los pagos. Vamos a entrar acá. Vamos a ir a lookup fields o campos de búsqueda y vamos a traer el valor y vamos a traer el estado. De esa forma nosotros ahora podemos hacer algo bastante interesante que es poner un campo de fórmula para decir, bueno, si está pagado, que me muestre en ese campo esta plata de nuevo. Sí. Entonces, y si no está pagado, que me muestre cero. Pero acá nosotros lo vamos a hacer solamente para poder vincular esto a clientes, porque acuérdense que estamos haciendo una vinculación de clientes a citas, de citas a pagos. Entonces vamos a ir acá, vamos a hacer una fórmula y acá tenemos un espacio para crear la fórmula con i que es s simple y le ponemos es eh contar o sumar el valor contar eh sumar el valor de pagos si el estado es pagado. de otra forma dejar vacío. Y acá ponemos crear fórmula y ahí nos tiene que tirar una fórmula más o menos bien, tal vez perfecta. Vamos a ver si quiere, si tiene ganas. Me parece que está un poquito mal igual. A ver. Sí, está mal. Eh, estado valor from pagos. Sí, esto no me estarían dando. No me está seleccionando esto. Array join valor from pagos. Esto me sobra. Muy bien. Por eso es importante más allá de usar estas estas herramientas para hacerlo, es ver bien y entender qué está pasando. Que como vieron acá había un error que la IA tuvo un error y lo pudimos corregir en un minuto. Vamos a ponerlo acá. Y de todas formas no me estaría agarrando. Vamos a vamos a hacerla vamos a hacerlo manual. Vamos a hacerlo manual porque esto no va a arrancar muy bien. Vamos a poner esto. Es como Excel, ¿sí? para la gente que lo tenga un poquito bacalado, un poquito eh acostumbrado. Vamos a poner si seleccionamos el campo estado igual a pagado. Y acá le vamos a poner el valor uno, que es mostrar justamente el valor from pagos. de otra forma dejar vacío. Como bien, esto era algo s simple que la IA se dio 50 vueltas para poder hacer y nosotros lo podemos hacer en un minuto. Le pusimos una fórmula de Excel. Si el estado, que es esto que vemos acá, es pagado, va a mostrar, debería mostrar el valor este de otra forma lo deja vacío. Por eso son las comas para separar términos. Lo dejamos acá y como ven, ahora sí funciona bien. Vamos a formatearlo acá para que nos dé h Bueno, no está bien. Ahora, ¿qué sucede con esto? Ya tenemos cuáles son los campos pagados, ¿no? Y cuál es tod cuál está, cuál es ya podemos vincular directamente un cliente a un pago. Ahora, ¿qué quiero hacer yo? Yo lo que quiero hacer es traerme acá a esta tabla el total de plata que me pagó un cliente a lo largo de toda su vida. Entonces, yo voy a hacer lo mismo que hice antes, traer información de un campo. Voy a ir acá y voy a traer total pagado, que es lo que hicimos recién, la fórmula. Y acá nos va a dar 100,1. Y acá vamos así usar otra fórmula para que nos dé el total porque ya tenemos los campos, pero vamos acá y le vamos a poner, creo que era zoom y le ponemos total pagado. Seleccionamos todo esto y acá ya terminó. Ya tenemos el se llama valor de vida. del cliente. Vamos a ver si lo podemos formatear. Lo voy a formatear a pesos. Está perfecto. Entonces, vamos a hacer un pequeño repaso. Tenemos tres tablas. La tabla de clientes, la tabla de citas y la tabla de pagos. ¿Por qué hacemos tres tablas si no ponemos todo en uno? para que sea todo coherente y para poder medir una cosa con otra y que podamos tener una buena interfaz que ahora lo vamos a mostrar en los próximos minutos, pero tenemos, ¿no?, tres clientes en este caso con un total de cinco citas de las cuales dos solamente fueron pagas y tenemos acá un pago por cada cita, pero no tenemos todo acá. Entonces, tenemos citas, pagos, clientes, todo vinculado una cosa con otra. Ahora, como está vinculado y empezamos a traer y traer información, podemos ver en una sola tabla el valor total de vida del cliente y ver bien ah todo lo que todo lo que pagó. Ahora, por otro lado, también podemos hacer lo mismo para ver todo lo que debe. Entonces, vamos a volver acá a donde estábamos recién y vamos a toter, vamos a duplicar esto. Total pagado, total tenemos casi todo, es casi la misma información. Lo único que acá le vamos a poner total adeudado. Y acá donde dice que busque los que dicen pagado, vamos a poner busque los que dicen no pagado. Y ahora va a aparecer de este lado. Vamos a volver a hacer lo mismo que hicimos recién. Vamos a clientes, vamos a traer la información y como ven, ya todo empieza a tener muchísimo más sentido porque empieza a funcionar de otra forma. Entonces acá de nuevo lo mismo. Vamos a duplicarlo otra vez este campo y vamos a poner total o deuda del cliente. Y acá en vez de seleccionar el campo que dice total pagado, vamos a poner total adeudado. Eh, ahí estamos. Entonces, de esa forma nos es muy fácil ver que lo que nos debe cada cliente en unos 15 minutos de estar construyendo esto, tenemos un sistema básico de para ver cuánto nos debe cada cliente, cuánto nos pagó cada cliente, cuántas citas tiene cada cliente, etcétera. ¿Sí? Entonces, esto es un poco lo que uno logra con tablas relacionadas o lo que uno logra con table de esta forma. De nuevo, vamos a hacer una pausa acá. Esto que ya fue un poquito más rápido, más complejo también, más dinámico, pero que medio tiene un punto. ¿Se entendió? ¿Esto está siendo claro? Bueno, seguimos un segundo. Ya tenemos un manejo dentro de todo bastante bueno de el back. sería de la tabla de todo esto. Bien, ahora esto es solamente una de las partes de table. Vamos a ver ahora qué le damos nosotros en este caso al cliente para que pueda cargar una o para que pueda, vamos a ver primero para que pueda ver esta información. Vamos a ir interfaces, que es esto que vemos acá. Y acá vamos a construir una nueva interfaz desde cero. Vamos a ponerle peluguería o datos peluguería. Y acá vamos a empezar a jugar ya un poco con las diferentes interfaces que nos permite hacer table. te permite hacer muchas interfaces ya prearmadas, como ven acá, lista, galerías, esto de Canvan, pilares, calendarios, formularios, que ahora vamos a verlos, un dashboard, esta que me encanta, que es un review, un un revisión del registro. Sí. Y también lo podemos hacer en blank. Nosotros no usamos blank porque no se puede abrir de celular, es bastante tedioso. Usamos mucho de estos otros, ¿no? Y como ven, se puede abrir también desde el celular algunas. Vamos a usar esta para poder ver el perfil de cada de cada uno de los clientes, ¿no? Tenemos el record review siguiente. Seleccionamos acá clientes y vamos a dejarlo a vacío. Acá vamos, podríamos filtrar, podríamos hacer varias cosas, pero vamos a dejarlo así. Vamos a next. Vamos a traer bastante de esta de esta información. Vamos a traer todo y ahora lo vamos a ir agarrando, ¿no? Vamos a poner clientes, le ponemos el nombre nada más. Finalizar. Y acá, como ven, ya estamos tocando y jugando con una interfaz donde donde vemos acá los tres clientes que tenemos en este caso y vemos los datos que queremos que aparezcan. Le puedo dar al cliente si quiero al a la piruquería, si quiero que lo pueda editar o no. Puedo cambiar el tamaño acá. Puedo cambiarle alguna etiqueta, puedo cambiarle algo para que se pueda ver de forma diferente. Sí, puedo cambiarle esta etiqueta acá para que no diga nombre y diga cliente o teléfono, nada de todo podemos hacer acá, pero vamos a repasar bien todo esto. Vamos a ver algo, ¿no? Vamos a poder, vamos a crear algo como como si alguien lo fuera a usar. Vamos a crear un nuevo grupo acá, que esto es estético. Le ponemos datos generales. Acá ya vemos que tenemos nombre dos veces. No me interesa tener el nombre dos veces. Sí, puedo tener el teléfono. Vamos a suponer que queremos crear un campo de mail, ¿no? Entonces vamos a crear acá campo. Le pongo email, correo y acá tenemos el campo de correo que lo vamos a completar en este caso para que quede pablo@gmail.com. Listo. Después tenemos el estado, tenemos detalle si queremos verlo. Y acá ya tenemos la información general. Para que quede un poquito más lindo, le vamos a poner color de fondo. Y acá tenemos Pablo y los datos generales. Ahora, por otro lado, vamos a ver acá y le vamos a poner, esto es otro grupo, como ven acá son dos grupos diferentes de datos que es estético nada más, pero acá le vamos a poner información o histórico del cliente o cuenta del cliente. Y acá vamos a empezar a verlo de una forma. Vamos a poner a mostrar el título. Ponemos esto. Y acá vemos que tenemos las citas, ¿no? Que la podemos ver de esta forma o puedo ponerla para que se vean de esta otra forma, por ejemplo. Y tenemos acá una tabla directamente de citas. No es tan práctico en este caso, así que vamos a dejarlo como estaba antes. Vamos a ponerlo acá. Citas y a ver si acá puedo hacer algo. Bueno, ven todo esto que ven acá, todo esto que que estamos viendo acá a la derecha, son todas las configuraciones que tiene, ¿sí? Todo lo estético. Dependiendo de yo dónde cliqueé, me van a aparecer unas cosas u otras. Puedo cliquear acá y ven que me muestra más del campo. Puedo cliquear acá y me muestra de toda la página en general. Puedo cliquear acá y me muestra de este seleccionador. Sí, que ven todo esto por acá. Ahora vamos a repasar eso. Pero como ven, nosotros tenemos esto, creamos, tenemos un listado de citas que ahora tenemos una sola y acá tenemos ya el eh los tenemos los casos, ¿no? Tenemos la la información. ¿Qué nos importa? El último dato que sacamos nos importa acá. Necesitamos tener el valor de vida del cliente, que lo pedimos recién, y la deuda del cliente. ¿Sí? Ahora, ¿qué nos pasa con esto? Nos sirve tener más información de las citas de Pablo. Nosotros tenemos ahora que me aparece el ID de la cita, el nombre del cliente dos veces. O sea, no me sirve para nada porque yo ya lo sé a golpe de ojos. Yo ya sé que estoy en Pablo, en el cliente de Pablo y el ID de la cita al cliente no no nos importa. Sí. Entonces vamos a ajustar esto acá. Y acá vemos que cuando yo aprieto, voy acá y me dice campos fields y veo los campos que están visibles. Lo que me interesa principalmente es el valor de la cita. Valor, perdón. sacamos cliente, ponemos valor y ponemos estado. Sí, esta es una forma de poder hacerlo. Entonces, acá tenemos citas, el ID de la cita que siempre va a aparecer porque necesitamos un identificador, el valor y el estado. ¿Sí? Ahora, necesitamos algo más acá. Sí, la fecha. fecha de la cita, valor estado. Y por otro lado, bueno, podríamos total pagado, total dudado, ¿no? Bueno, acá tenemos esto, ¿no? De la cita número cinco con esta fecha que vamos a ponerla, vamos a cambiarlo de orden acá, que me aparezca fecha la cita, valor y estado. Y a partir de acá ya tenemos que ahora tenemos una sola cita, pero vamos a ver qué pasa si hay más citas ahora en un segundo. Y ya tenemos algo que si lo probamos lo vamos a publicar acá y acá se ve dentro de todo bastante estético que si yo cambio de cliente, pongo Pablo, pongo Franco, pongo Juana, van a aparecer todos. Sí, acá por ejemplo en Juana que tiene tres citas, se puede ver un poco más gráfico de cómo quedaría en un caso real donde tenemos un montón de información, esto un montón de información de las citas. Entonces vemos que si nosotros tuviéramos cinco, seis, siete citas, sería muy poco práctico ver la cuenta del cliente. Entonces vamos a hacer una modificación con esto. Vamos a ir acá y le vamos a poner para que sea una view directamente. Y ven que ya cambia todo. Y acá tenemos lo mismo, los campos visibles. Voy a esconder el ID. Voy a poner esto acá para que sea un poquito mejor. Y tenemos el estado. Quiero achicarlo un poco a esto. Vamos a poner short citas y le ponemos un resumen, ¿no? De resumen de las citas del cliente. Acá de nuevo le vamos a poner un Vamos a tratar de ponerlo más chiquito. Bien, más chico que esto no se puede. Ahora, primero vamos a ver las citas y abajo la cuenta del cliente. Acá tenemos esto. Y ahora es donde empieza ya lo interesante. ¿Por qué? Porque yo acá le estoy le estoy dando una interfaz a la a la peluquería para que pueda ver toda la información que como ven ahora queda un poquito diferente, ¿no? Que tenemos datos generales, citas y la cuenta del cliente. Sí. Pero el cliente me va a decir, "Bueno, ¿y cómo hago yo más allá de para ver esto? ¿Cómo puedo saber yo para poder sumar una cita o para poder cargar un cliente?" Y acá es donde ya empieza algo un poco más interesante, que es poder darle esa opción. Si nosotros seleccionamos acá, en este caso, vamos para abajo, vamos a poder ver una opción de agregar registros a través de un formulario. Le damos a clicar acá. Y acá tenemos el formulario que le va a estar saliendo a la persona, que vamos a editarlo de va a ser agregar cita, usa este formulario para agregar una cita. Acá va a seleccionar el cliente, que las opciones que va a tener van a ser los clientes que están cargados. Por eso es lo que que es importante que esté todo coherente, ¿no? Vamos a tener el cliente la fecha de la cita y va a poder agregar un pago si quiere, pero realmente el pago va a tener que agregarlo por otro lado porque acá no nos va a dejar crear un nuevo pago. Sí. Ahora vamos a ir acá. Cliente cita. Acá le vamos a poner un mensaje de cita cargada correctamente y cargar. Entonces, acá, ¿qué es lo que tenemos ahora? Ya un poquito más cargado, ¿no? Acá si yo creo, voy, añado registro, cliente, me aparece Juana porque estoy en el cliente Juana. Sí, esto es importante, que no es que tengo que seleccionarlo siempre, sino que automáticamente me pone y lo voy a poner que va a venir en Navidad a las 10 de la mañana. Cargar. Acá, como ven, ya aparece. ¿Qué sucede? No tenemos esto, no tenemos el valor y el estado porque tenemos porque cargamos una cita, no cargamos un pago. Entonces, vamos a volver a editar acá. Vamos a ir acá a agregar otro botón. Primero le vamos a poner acá en el en la etiqueta le ponemos agregar cita y acá le vamos a poner agregar pago o sí agregar pago. Y acá le vamos a poner, vamos a seleccionar nuevamente. Tenemos open recordation formes, client, no. Vamos a poner acá que tiene que ser un pago. Esto es lo que estamos creando. Y record form acá. Editar. Acá vamos a tener que seleccionar la cita. Sí. Y acá nos aparecen un montón de citas y esto ya sí que es un poco incómodo. Entonces cuando veamos esto, vamos a ver que primero quiero que me aparezca, quiero que me aparezca el cliente de la cita, quiero que me aparezca la fecha de la cita. Entonces yo si voy acá ahora me van a aparecer cliente Juana, fecha de la cita. Ya lo puedo ver. Y otra cosa muy importante es que yo no quiero que mi cliente, o sea, que la peluquería pueda cargar un pago a una cita que ya tiene un pago cargado. ¿Sí? Entonces vamos a poner en selección, que es esto, la cantidad de los registros que se pueden seleccionar. Vamos a poner registros específicos y en el filtro vamos a poner dónde pago este vacío. Entonces acá solamente me debería dejar seleccionar las citas que no tengan un pago. Bien, así vamos jugando un poquito más. Vamos a cargar que, por ejemplo, tenemos 200 pesos a la cita que creamos que todavía no lo pagó y no tengo un comprobante lógicamente y ahí ya se cargaría. Vamos a poner recargar y el mensaje le ponemos pago cargado. Pago cargado correctamente. Bien, vamos a publicar y ahora de nuevo tenemos ya un segundo botón. Vamos a cargarle un pago. Acá tenemos 200 a la cita que es esta de Juana. Estado no pagado. Y vemos que primero que la deuda de Juana ya subió, ya está vinculado esto. Sí. Y después que aparece acá. ¿Qué pasa si ahora ponerle el registro otra cita a Juana para el 23 que ya la pagó? Ya la tengo acá registrada. Le agrego un pago y le voy a poner que una cita cara de 3300 me aparece acá para seleccionarla y el estado es pagado. Lo cargo y ahora me subió el valor de vida del cliente. Entonces, como ven, esto lo que genera es que esté todo extremadamente relacionado y que en media hora, 40 minutos que estuvimos acá haciendo y explicándolo, podemos tener un sistema que esto es un mínimo, un producto mínimo viable para una plugería o para un para un negocio de que vende algo. Bien, tiene sus cosas y demás, pero dentro de todo está simple, ya está prearmado y no nos tomó mucho tiempo hacerlo. Sí, esto es lo que tiene potente Air Table si lo usas bien, si lo usas con todo este con este embrollo, ¿no? Con con este eh con estas capacidades. Ahora, ¿qué nos queda hacer acá? Por último, ¿no? Ya tenemos para agregar cita, para cargar pago, pero nos queda, ¿qué pasa si yo quiero crear un nuevo cliente? No, vamos a ver acá. Voy a este a esta pantalla, voy a botones y puedo agregar un botón que sea, voy a la configuración, sea agregar cliente o cargar cliente. Y acá directamente lo que hago es eh vamos a Me dejará, mira bien. No me deja poner un formulario para crear un cliente en este momento. Sin embargo, si puedo ir a un URL externo que ahora lo vamos a configurar. ¿Por qué? Porque yo sí puedo tener un formulario acá para crear un nuevo cliente. Entonces, acá ya entramos en la tercer parte. Ya vimos la estructura de datos, que esto fue lo que más estuvimos revisando. Vimos un poco la interfaz para ver métricas, para jugar un poco, qué es esto que estamos que está que estuvimos viendo acá. Todo esto se llama interfaz. Y ahora lo que nos queda es ver este otro punto que es el punto de los formularios para cargar las ventas o para para cargar los datos. ¿Sí? Entonces vamos acá. Formularios, pongo en construir, selecciono clientes, nuevo cliente, crear formulario. Acá tenemos ya todos los datos, no nos vamos a meter mucho en esto. Lo publicamos. Y ahora dejamos que cualquiera pueda acceder. Copiamos el link. Ya tenemos el formulario. O sea, que yo cada vez que con esto creo un cliente se me crea un dato. Vamos a suponer que vamos Tito el teléfono que sea estado activo. Detalle. Tito viene muy poco a la peluquería. Correo@gmail.com. Lo cargo, voy a ver dato, voy a voy directamente a donde lo vería el cliente, que es acá. Y acá vemos que ya aparece Tito en 2 minutos solamente cargándolo con un formulario. Entonces, ahora, ¿qué nos faltaba? ¿Qué estamos haciendo antes? Yo quiero que el cliente pueda acceder al formulario desde acá. Entonces, yo copié el link, le pego el link acá. Vamos a publicarlo. Y acá si yo aprieto ahí me lleva directamente al formulario de nuevo cliente. Sí. Entonces yo acá tengo a Tito, ¿no? Nuevo cliente que apareció hace poco. Voy a cargarle que Tito vino el 21 o va vino el 15. Lo cargo, le agrego un pago. Tito pagó 500 por la cita del 15. Ven que ya todo es muy intuitivo, todo es muy fácil una vez que lo tenés acá y ya está. Y listo. Ah, bueno, le puse 5200. Bueno, pagó bastante, Tito. Entonces, acá ya está todo calculado, está todo armado. Es algo super intuitivo, superfácil, ¿sí? porque estamos usando Table, que es una plataforma hecha un poco para esto. Bien, así que creo que por hoy igual medio que estamos de revisión de table, que estuvimos revisando un poco formulario, interfaz, datos de los formularios, podríamos repasar un poquito más, pero nada, quería darles ahí a ustedes un poco de tiempo a ver si tienen alguna duda, algo específico, algo que quisieran armar en Air Table y no saben si se puede armar o no. Ten un poquito de de espacio así. Aprovecho para descansar la garganta también. Una pregunta. Ajá. Ah, donde tú has puesto ese registro interfaz, ¿se la damos así toda lista al cliente o es que el cliente tiene que hacer lo últimamente has hecho en la plataforma? Bien, nosotros lo que hacemos es armárselo todo directamente y darle un acceso al cliente. Una vez que tenemos esa interfaz, nosotros podemos que tenemos esto, vamos a acá, yo puedo ir a compartir interfaz e invitar un colaborador. Sí, con esto ya estaría bien. Y y cómo lo así como está lo ve el el la dueña del del peluquería, digamos, ¿no? Sí, exactamente, exactamente. Okay. O sea, ella a través de un formulario puede agregar un nuevo cliente. Sí, a través de un formulario puede agregar un nuevo cliente, agregar pagos, citas, no hay problema con eso. Puede hacerlo todo. Okay, entendí. Y estos videos que tú estás grabando se quedan en la plataforma para poder volverlo a saber y ponerlos en práctica, porque en teoría lo entiendo, pero en práctica es donde ahí me doy la pelea. Muy bien. Sí, sí, sí, sí. Todo teoría es fácil, pero cuando pones a practicar te sale uno por defecto y el otro Claro. Y te pierdes, ¿no? Sí, sí, sí, sí, sí. Ahí, eh, sí, se graban y se suben a la plataforma. Este, dime, ¿te puedo hacer una pregunta? Sí, quiero avanzar. He hecho una automatización para hacer videos en real. Okay, bien. Vamos a voy a primero tengo que confirmar que se entendió todo con el resto y si estamos con un poquito de tiempo ahí vamos a a ver eso. Bien. por eh eh Rosa, bueno, Raúl, ¿alguien tiene algún comentario o duda de lo que vimos hasta recién en TB? Bueno, estamos entonces eh vamos cierre acá con esto. Juana, sí, ahora sí eh comentamos un poco en qué era lo que estabas haciendo. Pantalla, ¿cómo no? Sí. Y si tú quieres puedes este, mira, yo estaba haciendo este el escenario uno, lo he estado haciendo pero excelente, según yo, y acá tengo el problema. Yo creo que aquí en la data me sale, por ejemplo, este, la imagen supuestamente aquí está. Espera, a ver, para ver dónde está el comentario. Mm. quitar de mucho tiempo y como tú ves aquí no me sale la imagen tres y no sé a qué se debe. Bien, eso es algo que va a requerir bastante tiempo por verlo y resolverlo con con atención. Yo te diría que el martes puedas venir y y lo vemos bien bien en detalle, así te lo llevas resuelto porque hoy te puedo dar por ahí algún alguna indicación o algo, pero resolverlo como me gustaría resolverlo, lo vamos a poder hacer el martes si podéis dedicar unos 15 o 20 minutos. Sí. Okay. Y sobre esto, porque yo tuve un plan para yo tener permiso y poner la URL de la imagen de Frit. He tenido que cambiar mi plan porque yo le pregunté al soporte y me dijo, "Tengo que pagar al premio plan que es 36 y en aquí en euros me sale algo de 40. Lo he cambiado, pero ni aún así me sale este URL. Aquí debería de salirme la imagen tres. ¿Crees que tengo que pedir ayuda al soporte o no? No, no, no creo. Creo que es algo más interno de de make. Está llamando con un http con un módulo. ¿Cómo está llamando la API? Con Ah, ahí. Okay. Generar imagen. Bien. Sí, es es cuestión de verlo bien en profundidad, pero no tiene nada que ver con soporte. Estoy seguro que es algo que podemos resolver. Okay. Si no vaya a ser que pierda tiempo escribiendo soporte. Tranqui, tranqui. Es el problema. Pero bueno, okay, Franco. Bueno, esperaré el martes. Dale, el martes lo vemos en profundidad, pero bueno, bien. Y muchas gracias, ¿no? Por favor. Bueno, espero que les haya servido, que haya aportado algo bien. Ya estamos a a fin de año, así que también tal vez a muchos no los vea para las fiestas. Tengan excelentes fiestas, eh, y bueno, a muchos Espera, espera, espera, que que discúlpame. Eh, ¿los están en la plataforma o no? los videos de de esta este, por ejemplo, que tú estás haciendo, lo cuelgan en la plataforma para volverla a ver hoy. Sí, sí, sí, sí, sí. En la sección de clase de la comunidad. Okay. Así que nada, con eso vamos cerrando. Espero que tengan un excelente fin de semana y bueno, nos vemos el martes. Muchas gracias. Chao. Gracias. Sí.
