# Domina GitHub como un experto

> Ruta: Vibe-Coding › Domina GitHub como un experto

**📎 Recursos:**
- Presentacion

---

**Problemas que resuelve la sesión del 21 de Mayo: **Cómo trabajar con Git y GitHub desde cero para versionar proyectos sin perder código, cómo coordinar equipos distribuidos usando ramas, issues y pull requests, y cómo aprovechar GitHub Actions para automatizar pruebas y reducir errores en producción.

### Intervenciones

[00:00] Joaco – Apertura y contexto de Anti Gravity 2.0 Da inicio a la sesión y, junto a Patricio, comenta la actualización de Anti Gravity 2.0. Explica que la nueva versión se parece más a Claude Desktop que al IDE original y que el proceso de actualización rompe configuraciones previas. Joaco confirma que volvió a VS Code después de probarla.

[04:00] Carlos – Aclaración sobre Anti Gravity 1 y 2 Explica que Anti Gravity 2.0 NO reemplaza al Anti Gravity original. Ambos coexisten y se pueden descargar desde la página oficial. Eventualmente Google va a discontinuar uno, pero por ahora siguen activos los dos. Recomienda quedarse con el IDE clásico si ya tienes configuraciones armadas.

[06:00] Silvia – Almacenamiento de archivos MP3 y QR para canciones personalizadas Consulta cómo guardar canciones generadas con Suno (vía API de Zuno) y vincularlas a un código QR perdurable. Solución: no usar Airtable porque requiere login y los archivos no son públicos. Contratar un servicio de bucket storage (tipo AWS S3) para hospedar los MP3 públicamente y que el QR apunte directamente a esa URL.

[09:30] Carlos – Qué es Git y para qué sirve Define Git como un sistema de control de versiones creado por Linus Torvalds. Funciona offline, de manera local, y crea una línea de tiempo del proyecto. Es como un "Control Z infinito" que permite regresar a cualquier versión anterior. Aclara que Git y GitHub son cosas distintas: GitHub es la plataforma online que hospeda repositorios Git.

[15:00] Carlos – Diferencias entre Git, GitHub y otros competidores Explica que GitHub es propiedad de Microsoft desde 2018 y que es el estándar de la industria, aunque existen alternativas como GitLab, Bitbucket y CodeBird. Aclara qué es un commit (una marca/etiqueta en el historial) y por qué conviene hacer commits atómicos: cada cambio mínimo merece su propio commit para tener control total al volver atrás.

[20:00] Arturo – Seguridad de skills publicadas en GitHub Pregunta si los skills publicados en repositorios son seguros o pueden estar hackeados. Solución: siempre revisar el repositorio con un LLM antes de clonarlo, verificar estrellas, autor y contribuciones. Aun así, los hackers son cada vez más sofisticados (recientemente hackearon GitBook, NPM y Node.js), así que la revisión nunca es 100% garantía.

[26:00] Luciano y Natalia – Capacidad de almacenamiento en GitHub Consultan sobre límites de Storage en GitHub. Solución: GitHub está pensado para código (texto plano que pesa bytes). Para imágenes o videos, lo ideal es no hospedarlos en GitHub sino en un servicio externo y referenciarlos por enlace en los archivos del repositorio.

[28:30] Natalia – GitHub Desktop como alternativa Pregunta si GitHub Desktop reemplaza la instalación por terminal. Solución: Carlos aclara que GitHub Desktop ocupa más espacio que la instalación directa de GitHub CLI, así que no es la mejor opción si el problema era falta de espacio en disco.

[29:00] Daniel – Aclaración clave: Git ≠ GitHub Refuerza que Git y GitHub son dos cosas distintas. Git es el sistema de control de versiones que viene instalado por defecto en Mac. GitHub es una plataforma externa que actúa como "fachada". Existen otras interfaces como GitKraken, Bitbucket, etc. Todas usan Git por debajo.

[32:00] Marcia y Carlos – El problema histórico de las versiones "final_final_v2" Comparte cómo antes, sin Git, los desarrolladores creaban carpetas como "versión 1", "versión 2", "final_final" y se generaba un caos total. Marcia perdió un desarrollo por un robo de equipo sin respaldo. Git resuelve esto creando puntos versionados (commits) sin duplicar carpetas.

[36:00] Carlos – Demo práctica: crear tu primer repositorio Demuestra en vivo los comandos git init, git add, git commit -m, git status y git diff. Explica que en la práctica con Claude Code, el usuario ya no escribe estos comandos manualmente: Claude los ejecuta automáticamente si está bien configurado en el [CLAUDE.md](http://CLAUDE.md) o en los hooks.

[44:00] Iván y Marcia – Respaldos: Git, GitHub y Drive Consultan si conviene tener proyectos en Drive además de GitHub. Solución: Daniel y Carlos coinciden en NO mezclar Google Drive con repositorios Git locales, porque Drive monitorea cambios constantemente y puede generar conflictos de sincronización con GitHub. El backup correcto es: trabajar local → commit → push a GitHub remoto.

[46:00] Carlos – El archivo .gitignore y los secretos Explica que .gitignore le dice a Git qué archivos ignorar al sincronizar. Crítico: el archivo .env con credenciales y API keys NO se sube a GitHub. Si te roban el equipo y solo tenías las credenciales en local, las perdés. Conviene rotarlas o tener respaldo separado.

[50:00] Carlos – Caso real: proyecto Heyesha (ATS de alto volumen) Muestra un proyecto real donde 5 personas en 4 países colaboran en un sistema ATS. 156 commits, 13 pull requests, 82 issues, sin pisarse los pies. Es el ejemplo vivo de cómo GitHub habilita el trabajo distribuido en equipo.

[53:00] Carlos – GitHub Actions y smoke tests automatizados Muestra cómo configuró una acción que se dispara con la etiqueta E2E: ejecuta Claude Code en un sandbox de GitHub para correr 91 pruebas automatizadas de candidatos (combinaciones de edad, país, experiencia) sin intervención humana. Aclara que GitHub Actions tiene límites gratuitos según si el repo es público o privado.

[57:00] Carlos – Issues: el cerebro externo del proyecto Explica el sistema de Issues como bug tracker, ideas y tareas pendientes. Usa etiquetas (bug, enhancement, documentation, prioridades crítica/alta/media/baja). Los Issues se cierran automáticamente cuando un Pull Request los resuelve. Muestra cómo en el repositorio de OpenCode hay miles de issues abiertos por la comunidad.

[01:08:00] Carlos – Epics y Children: organización jerárquica Explica que un Epic es un issue grande que se divide en varios "children" (sub-issues accionables). Al cerrar todos los children, se cierra el Epic. Sobre el Epic está el repositorio. Para metodología XSC, la jerarquía es: Fase → Epic → Feature → Task.

[01:11:00] Carlos – Pull Requests, merges y revisión de código Muestra cómo se reciben los Pull Requests del equipo, cómo se hace code review pidiendo ajustes, y la diferencia entre merge (fusionar) y cerrar sin merge (tomar el código como referencia y reescribirlo manualmente).

[01:15:00] Daniel y Carlos – Colores de las ramas en VS Code Aclaran que cada rama nueva recibe un color distinto para diferenciarla visualmente. No está asociado al usuario sino al orden en que se abrieron las ramas. Los colores son independientes en cada IDE (VS Code, GitKraken, terminal).

[01:19:00] Joaco – Costo de los E2E tests automatizados Pregunta quién paga el consumo de tokens cuando GitHub Actions corre Playwright con Claude Code. Solución: Playwright corre en modo headless usando la conexión que tú haces entre Claude Code y GitHub. Es tu sesión y tus tokens de Claude Code, NO los paga GitHub. GitHub solo aporta la infraestructura (Actions).

[01:23:00] Carlos – Documento maestro y trazabilidad Muestra cómo mantienen toda la documentación viva dentro del repositorio (arquitectura, auditorías de performance, documentación específica de WhatsApp). El resultado: una app emulando WhatsApp Cloud completa con calculadora de costos, templates aprobados por Meta y previews en tiempo real.

[01:26:00] Daniel – Git Flow como estrategia de trabajo Explica Git Flow: una metodología donde Main/Master nunca se toca directamente. Todo se trabaja desde una rama Develop, y solo cuando hay un Release validado por QA, se hace merge a Master. Esto evita romper producción los viernes en la noche.

[01:34:00] Carlos – Ultra Review de Claude Code Comparte un dato clave: Claude Code lanzó Ultra Review, una funcionalidad que verifica ramas largas antes de hacer merge. Plan Pro: 3 reviews gratis. Plan Max: 6 gratis. Después se paga por uso. Muy poderoso para features completos.

[01:36:00] Carlos – Trabajar con ramas: la regla de oro "Jamás programes directamente en main." Explica convenciones de nomenclatura: fix/ para correcciones, feat/ para funcionalidades. Las ramas permiten probar ideas sin romper lo que funciona y trabajar en paralelo entre múltiples developers.

[01:38:00] Carlos – El hackeo reciente de GitHub Aclara que no hackearon GitHub directamente: un usuario instaló una extensión maliciosa de VS Code que dio acceso a sus repos. Recomendaciones: usar variables de entorno (.env), agregarlas al .gitignore, y en Vercel marcar las variables como "sensible" (después del hackeo de Vercel del mes pasado) para que queden codificadas y nadie pueda leerlas.

[01:41:00] Cierre Joaco cierra agradeciendo el contenido técnico y a Daniel por sus aportes desde la experiencia. Invita a la sesión del día siguiente con Fran y al próximo miércoles de VibeCoding.
