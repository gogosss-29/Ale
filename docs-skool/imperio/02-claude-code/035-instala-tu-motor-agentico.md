# Instala tu Motor Agéntico

> Ruta: Claude Code › Instala tu Motor Agéntico

**📎 Recursos:**
- MAC_motor_agentico_v0.1.0.zip
- WINDOWS_motor_agentico_v0.1.0.zip

---

Pagas suscripciones de IA todos los meses. ¿Sabes cuánto valor estás sacando de ellas? **Probablemente no**, nadie lo sabe, porque ese dato no existe en ninguna pantalla.

![CleanShot 2026-06-11 at 13.39.05.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/03e3152e115e469683c69cac7705e9eb3e69722a83414cfdb7445275d387521e.png)

**Motor Agéntico** es el panel de control de tu operación con IA: un dashboard que corre 100% en tu computadora, lee tu actividad real de Claude Code y tus herramientas de IA, y te muestra lo que hoy es invisible: cuánto gastas vs. cuánto trabajo extraes (*tu ROI real*), cuánto tiempo te ahorran tus skills, qué recuerda tu memoria y qué están haciendo tus asistentes.

**Tres cosas antes de empezar:**

- **Es local.** Tus datos nunca salen de tu máquina. Cero telemetría, cero cuentas, cero nube.
- **Es de solo lectura.** El Motor observa tu actividad; no toca nada.
- **No tienes que programar nada.** Tu agente de IA hace la instalación por ti. Tú solo escribes una palabra.

## Lo que necesitas

- Un PC o Mac.
- Un agente de código instalado: **Claude Code** (recomendado), Codex, Cursor o el que uses.
- 5 minutos.

## Paso 1 — Descarga el ZIP

Descarga **motor-agentico-v0.x.x.zip** desde el enlace de abajo (o desde el área de miembros). Haz doble clic para descomprimirlo. Te queda una carpeta con el Motor adentro.

## Paso 2 — Pásaselo a tu agente

Abre Claude Code (o tu agente preferido) y haz esto:

1. Arrastra el archivo **INSTALAR.md** (está dentro de la carpeta que descomprimiste) a la ventana del chat.
2. Escribe una palabra: `instalalo`
3. Enter.

Eso es todo lo que haces tú. *INSTALAR.md no es un manual para humanos, es un manual para agentes:* contiene las instrucciones exactas para que tu IA instale el Motor de punta a punta y te avise si algo necesita tu atención.

## Paso 3 — Mira cómo se instala solo (~3 minutos)

Mientras esperas, esto es lo que tu agente está haciendo, en orden (no tù):

1. **Verifica Bun** (el runtime que mueve el Motor) y lo instala si no está.
2. **Instala las dependencias** del proyecto (baja ~300 MB de paquetes — es el paso más largo).
3. **Corre el escaneo inicial:** lee tu actividad local de Claude Code y tus herramientas de IA, y construye tu primera foto de datos. Todo se queda en un archivo local dentro de la carpeta del Motor.
4. **Activa el Sueño:** un análisis automático que corre cada mañana a las 7:00 y te deja recomendaciones accionables en el dashboard.
5. **Abre tu dashboard** en `http://localhost:8081`

Cuando el navegador se abra, la instalación terminó.

## Paso 4 — El onboarding

Lo que ves al abrir depende de tu historial:

- **Si ya venías usando Claude Code:** entras directo a tu dashboard, ya poblado con tus números reales. Arriba aparece un aviso dorado — *"Personalízalo en 90 segundos"* — que abre el asistente de configuración cuando tú quieras. Tu dashboard funciona desde el segundo cero.
- **Si estás empezando de cero:** te recibe un asistente de 7 pasos (~90 segundos) que detecta tus herramientas, conecta tus fuentes y personaliza el Motor con tu nombre y tu tarifa por hora — el dato que usa para traducir tiempo ahorrado en dinero.

## Qué vas a ver

- **Tu ROI:** cuánto pagas al mes en suscripciones de IA vs. cuánto trabajo equivalente extrajiste (calculado de tu uso real de los últimos 28 días, a tarifas API publicadas).
- **Gasto y tokens:** qué modelos usas, cuánto costaría eso a precio de API.
- **Skills:** qué comandos usas, cuántas veces, y cuánto tiempo te ahorran.
- **Memoria:** el mapa 3D de lo que tu IA sabe de tus proyectos.
- **Asistentes:** el estado en vivo de tus agentes conectados.
- **El Sueño:** cada mañana, las oportunidades de mejora que el análisis nocturno encontró en tu actividad.

Todo sale de tu data real. *Si algo todavía no tiene datos, el Motor te lo dice honestamente — no inventa números.*

## Actualizar y desinstalar

- **Actualizar:** descarga el ZIP nuevo, reemplaza la carpeta y listo. Tu progreso (racha, nombre, configuración) vive en tu navegador, atado a `localhost:8081` — no se pierde al actualizar. Solo no cambies el puerto ni borres los datos del sitio.
- **Desinstalar:** dile a tu agente *"desinstala el Motor"* con el mismo INSTALAR.md — trae la sección de desinstalación completa.

## Si algo falla

Vuelve a arrastrar **INSTALAR.md** a tu agente y escribe: *"la instalación falló en el paso X, arréglalo"*. El manual incluye el troubleshooting — tu agente sabe qué hacer.

El Motor siempre corre en `http://localhost:8081`; si la pestaña se cerró, ábrela de nuevo.
