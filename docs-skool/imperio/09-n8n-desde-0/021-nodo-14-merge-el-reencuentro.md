# Nodo 14: Merge (El Reencuentro)

> Ruta: n8n Desde 0 › Nodo 14: Merge (El Reencuentro)

**🎬 Vídeo (8.6 min):** https://www.loom.com/share/e12851c060f64a18a97c8148c022686e

**📎 Recursos:**
- 17. Merge - Mail a Vtas o Gerencia

---

El Concepto: "El Embudo".

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9fd07e9cde42476ea2bddf153970b6f46081768518d84dabb7691e2708ea7703-md.png)

Cuando usas un nodo If, divides tu camino en dos (Camino A y Camino B).

Pero a veces, después de hacer cosas distintas en cada camino, quieres que todos vuelvan a la misma fila para terminar el proceso juntos.

El nodo Merge toma esos caminos separados y los vuelve a unir en una sola línea.

### **1. La Situación (Escenario: Gestión de Pedidos)**

- **El Origen:** Tienes un Google Sheet con pedidos nuevos (on row added)  
  
 ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/dd77461d7ec345f7bd4af7bc25b2001d45ba42a58abd45cd9dc42105691107d5-md.png) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e12bd1b7bb0d43b1b569e26bfd4403f0745b9c4f96504106b5b1f58aaa15d866.png) ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/7da04e1b580846f2b4188a46d5800def4d9932ed86a04c2d9cb65abf60e5a30e.png)
- **La Lógica (El If):** - Si el pedido es **Mayor a $1.000.000** (VIP) $\rightarrow$ Le mandas un correo al Gerente.
- Si el pedido es **Menor a $1.000.000** (Normal) $\rightarrow$ Le mandas un correo a Ventas. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/e03db181431e4a818ff98b5a6a1bc1a1b6f4a40dabf54b13959af4dbb27b1dd1-md.png)

Bonus, como puedes ver hay muchos simbolos de . o $, vamos a eliminarlos con el code: 

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/dece0681f0b94a7a9fafb4f2999e491795a5d1b890664875a5364669618eb869.png)

ahi si pasamos de $1.250.000 a 1250000

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/4dd8bbf307bd4d30aa939c221ef98704910cde59555b40ba99094a493c614c36-md.png)

- **El Problema:** Después de mandar esos correos distintos, quieres hacer una acción final para **TODOS**: Marcar el pedido como "Procesado" en el Google Sheet.
- **Sin Merge:** Tendrías que poner un nodo "Actualizar Sheet" en el camino de arriba y *otro igual* en el de abajo (doble trabajo).
- **Con Merge:** Unes los dos caminos y pones **un solo** nodo "Actualizar Sheet" al final.

---

### **2. Paso a Paso: Cómo construirlo**

#### **Paso A: El Divisor (If)**

Imagina que ya tienes tu **Google Sheets** (leyendo pedidos) conectado a un **If** (separando por precio).

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cdfa4634ff5a4d3bbf044155b0d6724e838ded777ba84617a3fa1c1803b25b9a-md.png)

- **Camino True (Arriba):** Conectas un Gmail para el Gerente. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/9688464b013d4ac69c89582acc474ae679d548e4801947d498ace7f1d6b38e5d-md.png)
- **Camino False (Abajo):** Conectas un Gmail para Ventas. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/eb459a72ecac46f7a9cf2aab3ab1aaec91e72866a45645598f59e68613d1846e-md.png)

#### **Paso B: La Unión (Merge)**

Aquí es donde simplificamos.

1. Agrega el nodo **Merge** al final del lienzo.
2. **Conexión (Física):** - Agarra el puntito de salida del **Gmail del Gerente** (Arriba) y conéctalo a la **Input 1** del Merge.
- Agarra el puntito de salida del **Gmail de Ventas** (Abajo) y conéctalo a la **Input 2** del Merge.
- *(Se formará un diamante o rombo visualmente).* ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/cdd98dc939984b5abbde1d406c7566d76721975997104937aba7224e01500337-md.png)
3. **Configuración:** - **Mode:** Selecciona **Append** (Anexar).
- *¿Qué significa?* "No me importa de dónde vengan (de arriba o de abajo), simplemente déjalos pasar y ponlos en una sola fila india". ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/aa768cfe5ffd4582b2f70a26aab4fc777730160207744d3e9a20f500c1d8f296-md.png)

#### **Paso C: La Acción Final (Google Sheets)**

Ahora que todos los pedidos (VIP y Normales) volvieron a estar en una sola línea:

1. Conecta un nodo **Google Sheets** a la salida del Merge.
2. **Action:** Update Row.
3. **Configuración:** En la columna "Estado", escribes "Procesado". ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/be721f9924c84bd4bf7577ea5dcf6527160b992643714b55aa71ae0e22a550b4-md.png)

---

### **3. Resultado Final**

- **Caso VIP:** Entra al If $\rightarrow$ Va por Arriba (Email Gerente) $\rightarrow$ Cae al Merge $\rightarrow$ Se marca como Procesado.
- **Caso Normal:** Entra al If $\rightarrow$ Va por Abajo (Email Ventas) $\rightarrow$ Cae al Merge $\rightarrow$ Se marca como Procesado. ![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/d02914a2fea245f881871cdeba9c14819a7488b6b6874d04bf66223a086ce49e-md.png)

Usaste **un solo nodo** final para actualizar la planilla, en vez de dos. Tu flujo se ve limpio y ordenado.

![image.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8521fd68c64a42fd98da2e5776dd2adef1082a54305f4410865a3206fb7561e0-md.png)

### **4. Criterio (Por qué usarlo)**

- **Orden:** Evitas tener flujos con "cabos sueltos". Todo empieza junto y termina junto.
- **Mantenimiento:** Si mañana quieres cambiar la palabra "Procesado" por "Enviado", solo editas **un nodo** final, no tienes que andar buscando en todas las ramas del If.
