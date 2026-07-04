# Nodo 8: Switch (El Distribuidor)

> Ruta: n8n Desde 0 › Nodo 8: Switch (El Distribuidor)

**📎 Recursos:**
- 8. Switch - Redirección a área

---

**El Concepto:** "La Recepcionista". El cliente llega al mesón y dice qué necesita. La recepcionista no le dice "Sí" o "No" a diferencia del nodo “if”; le dice: *"Para Ventas piso 1, Soporte piso 2, Reclamos piso 3"*. Este nodo toma un dato y lo envía por **múltiples caminos distintos** dependiendo de qué dice ese dato.

![image.png](../imagenes/ed80415bde9549faa533a4ef39213054530dbd4b0aeb4531845908516d379a3f.png)

**1. La Situación (Escenario Real)**

- **La Entrada:** Tienes el mismo formulario de contacto en n8n anterior, pero ahora agregaste una pregunta clave: *"¿Con qué departamento quieres hablar?"*.
- **Las Opciones (Dropdown):** 1. Ventas
2. Soporte
3. Marketing
- **La Misión:** Quieres que el mensaje llegue al canal de Slack correcto automáticamente, sin que tú tengas que leerlo y reenviarlo.

---

### **2. Paso a Paso: Cómo construirlo**

#### **Paso A: El Formulario (El Menú)**

1. Abre tu nodo **n8n Form Trigger**.
2. Agrega un campo nuevo tipo **Dropdown** (Selección múltiple). - **Label:** Departamento.
- **Options:** Agrega tres opciones: Ventas, Soporte, Marketing. ![image.png](../imagenes/d144456475524bc786dd1bba54b05af42639585a3d234e07ae3db73c90f0904b-md.png)
3. **Testear:** - Dale a "Test Step".
- Abre el link del formulario, selecciona **"Soporte"** y envíalo. ![image.png](../imagenes/25c0fa8c591c473d859b28b7293275379a8d8aba84d5425c9a0a08b0ea30d3c3.png)
- Verifica que n8n recibió el dato.

#### **Paso B: Configurar el Switch (Las Reglas)**

Aquí es donde le enseñas al robot a dirigir el tráfico.

1. Conecta el nodo **Switch** al Formulario. ![image.png](../imagenes/eef95cbdf52346df9a77aa470a78730b43018aae12344e66bc53938f40d21c70.png)
2. **Mode:** Rules.
3. **Data Type:** String (Texto).
4. **Value 1 (¿Qué evaluamos?):** Arrastra el campo Departamento desde el nodo anterior. ![image.png](../imagenes/c49d5029d8c7429d9bd0373df34aff4125f07388e1e041db8c4baac56c7be975-md.png)
5. **Routing Rules (Creando los caminos):** - **Regla 0 (Ventas):** - Operator: Equal (Igual a).
- Value 2: Ventas.
- *(Esto crea la Salida 0)*.
- **Regla 1 (Soporte):** - Dale a "Add Routing Rule".
- Operator: Equal.
- Value 2: Soporte.
- *(Esto crea la Salida 1)*.
- **Regla 2 (Marketing):** - Dale a "Add Routing Rule".
- Operator: Equal.
- Value 2: Marketing.
- *(Esto crea la Salida 2)*.

Dale a **"Test Step"**. *Como seleccionamos "Soporte" en la prueba, verás que el dato sale iluminado por la ****Salida 1**** (la del medio).*

![image.png](../imagenes/f5f55051745b4bf395b9eb64e65af6d157d55ce45f3243d589a168487575ce53.png)

#### **Paso C: Los Destinos**

Ahora verás 4 puntitos a la derecha del nodo (0, 1, 2 y Fallback).

1. **Salida 0 (Ventas):** registralo en sheets
2. **Salida 1 (Soporte):** Conecta un nodo (ej. Gmail) que cree un ticket técnico.
3. **Salida 2 (Marketing):** Conecta un http para mandar un Whatsapp. ![image.png](../imagenes/8282cf0f911f452a9f1da3a69c037d0e984b9cb49d3e483fa919856a5b1b444a.png)
4. **Fallback:** (Opcional) Si alguien logra mandar una opción que no existe, saldrá por aquí. Úsalo para errores. ![image.png](../imagenes/2a07904112ce4ac59dc1ca619daa1e7eb43fca007845464c94ebe3fbe21046cc.png)

---

### **3. Resultado Final**

Tienes un sistema de "Mesa de Ayuda" automatizado.

- El cliente elige su camino en el formulario.
- n8n lee la elección.
- El mensaje aterriza en el escritorio de la persona correcta al instante.

### **4. Criterio (Por qué usarlo)**

- **Orden Visual:** Si usaras el nodo *If* para esto, tendrías que preguntar: *"¿Es ventas? No. -> ¿Entonces es Soporte? No. -> ¿Entonces es..."*. Eso se ve horrible. El Switch te deja ver todas las opciones en una columna vertical limpia.
- **Escalabilidad:** Si mañana abres el departamento de "Finanzas", solo agregas una regla más al Switch y listo. Es modular.
