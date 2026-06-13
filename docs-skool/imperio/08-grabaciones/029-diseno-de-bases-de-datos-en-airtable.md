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
