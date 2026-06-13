# ¿Qué es un Arnés de Agentes IA?

> Ruta: Vibe-Coding › ¿Qué es un Arnés de Agentes IA?

**🎬 Vídeo (22.1 min):** https://www.youtube.com/watch?v=z3KF8OaLCG4

---

## ¿Qué es un Arnés de Agentes IA?

Sam Altman dijo que el 2026 era el año de los agentes. Anthropic publicó dos artículos dejando claro que el contexto importa más que el modelo. Y Jensen Huang, CEO de Nvidia, dijo en el GTC que el futuro de la IA no son los modelos, sino los sistemas operativos que los rodean.

Lo que él llama "sistema operativo" tiene otro nombre técnico: el **arnés**. Y el 98% de la gente que usa Claude Code, Codex o Cursor no lo conoce.

Si te ha pasado que estos agentes un día están haciendo cosas increíbles y al otro día están fallando en lo más tonto, este post es para ti.

### ¿Qué es un arnés?

El nombre viene de la analogía más literal que existe: el arnés es la silla y las riendas que le pones a un caballo para poder montarlo y controlarlo.

Tu modelo de IA es el caballo. Es potente, rápido, pero solo es un caballo alocado. Genera miles de líneas de código, toma decisiones impredecibles y termina en caminos que no son los que querías.

El arnés es todo lo que se construye alrededor para que vaya en la dirección correcta. Técnicamente está compuesto por 4 piezas:

1. **Contexto** que le das al modelo
2. **Herramientas** a las que puede acceder
3. **Memoria** que le permite recordar entre sesiones
4. **Verificación** que comprueba si lo que hizo está bien

### Por qué importa más que el modelo

Los modelos cambian cada 3 meses. Hoy sale Opus algo.algo, en 3 meses sale Gemini X, después GPT-8. Si construyes tu sistema encima de un modelo, cada vez que sale uno nuevo tu sistema queda obsoleto.

Pero si construyes alrededor de un arnés bien orquestado, ese arnés es 100% tuyo. Los archivos son tuyos, las reglas son tuyas, los procesos los definiste tú. Y dentro de ese arnés, el modelo es intercambiable.

**Los modelos cambian cada 3 meses. Tu arnés no.**

### El caso de Vercel que lo demuestra todo

Vercel construyó un agente llamado D0 (de "data") para hacer queries. En la primera versión le dieron 16 herramientas hiperespecializadas. La lógica era: si le damos las herramientas perfectas, no se equivoca.

Pasó lo contrario. Cuando le quitaron el 80% de las herramientas y le dejaron solo acceso a Bash y un sistema de archivos básico, el agente fue **3x más rápido**, gastó **47% menos en tokens** y subió el éxito de **80% a 100%**.

La lección: un arnés cargado funciona peor. Un arnés mínimo gana siempre.

### Los 3 pilares del Harness Engineering

#### Pilar 1: El arnés vive en tu código

No es magia externa, son archivos en una carpeta. El más importante es `AGENTS.md` (o `CLAUDE.md` si estás en Claude Code). Es el punto de entrada que se carga antes de cada sesión.

Mantenlo corto (menos de 200 líneas). Si lo inflas, ya partes degradado.

Importante: usa `AGENTS.md` porque es estándar abierto. Así no te casas con una herramienta y puedes saltar entre arneses.

#### Pilar 2: No uses un agente para todo

En vez de un solo agente que hace todo, separa en roles:

- Un **agente líder** que orquesta
- Un **agente implementador** que escribe código
- Un **agente revisor** que verifica

Cada uno con contexto limpio, cada uno reportando al `progress/` para que el siguiente pueda retomar desde ahí. Al final es como una empresa: un jefe que delega y subagentes que ejecutan.

#### Pilar 3: Verificación

La IA te puede mentir, no con mala intención, pero te puede decir "terminé este feature, todo bien" y estar roto. El arnés mismo tiene que verificar:

- Tests automatizados
- Linter y type check
- Playwright para autodiagnóstico de interfaces
- Un agente revisor que aprueba o rechaza

El agente no termina porque dice que terminó. Termina cuando el arnés valida que terminó.

### Claude Code, Codex, Cursor, OpenClaw... ¿cuál uso?

Acá viene lo que la mayoría no entiende: **cada uno es un arnés**. Son implementaciones distintas de los mismos 3 pilares.

- **Claude Code**: arnés de Anthropic, usa `CLAUDE.md`
- **Codex**: arnés de OpenAI, mismos pilares, distinta implementación
- **Cursor**: arnés enfocado en el editor
- **OpenClaw / OpenCode**: arnés abierto, autoinstalable, modelos intercambiables

Si entiendes los 3 pilares, saltar entre plataformas es trivial. Si no, vas a estar reaprendiendo cada nueva plataforma constantemente.

### Cómo empezar hoy

**1. Escribe tu **`AGENTS.md`

Crea el archivo en la raíz de tu proyecto. Abre Claude Code o Codex y dile: "Hazme preguntas tipo entrevista para construir nuestro `AGENTS.md`". Que no pase las 200 líneas.

**2. Agrega un script de verificación (**`init.sh`)

Que corra tests, verifique estructura, valide que el proyecto esté en buen estado antes de empezar. Y agrégalo a tu `AGENTS.md`: "ejecuta `init.sh` antes de cualquier cambio. Si falla, para."

**3. Separa tu agente en roles**

Al menos 3: líder, implementador, revisor. Asigna modelos distintos según el rol (el revisor puede usar uno más caro, el implementador uno más barato). Y que cada subagente escriba su resultado en `progress/`, no en el chat.

### Cierre

Los modelos van a cambiar 1000 veces. Tu arnés se queda.

La gente está obsesionada con "cuál es el mejor modelo". La pregunta correcta es: **¿está mi arnés bien construido?**

El arnés es 100% tuyo. El caballo lo estás alquilando.

---

Si te perdiste el video de [**Agentes IA en 18 minutos**](https://www.youtube.com/watch?v=7HlfFHLoYK8&t=342s), mírelo después de este. Ahí cubrí toda la base teórica (agent loop, contexto, memoria, herramientas) que acá asumí. Este video es la arquitectura. Ese es la base.

Nos vemos en la próxima 🤘
