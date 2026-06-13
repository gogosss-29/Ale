# Meta Ads Manager + Claude Code = Media Buyer

> Ruta: Claude Code › Meta Ads Manager + Claude Code = Media Buyer

**🎬 Vídeo (12.6 min):** https://www.youtube.com/watch?v=mfk82SbXgGo&t=93s

**📎 Recursos:**
- [Politica de Privacidad (enlace)](https://raw.githubusercontent.com/benjacord/meta-app-policies/main/privacy-policy.md)
- [Eliminación de datos (Enlace)](https://raw.githubusercontent.com/benjacord/meta-app-policies/main/data-deletion.md)

---

Le pagaba $600 al mes a Cristóbal para manejar mis Meta Ads. Era bueno en lo suyo, pero la realidad es que yo igual tenía que decirle qué hacer, qué cambiar, qué probar. En algún punto me di cuenta de que el trabajo real lo estaba haciendo yo, él solo lo ejecutaba.

Entonces armé esto.

Un agente en Claude Code que se conecta directamente a la API de Meta, sin dashboards de terceros, sin SaaS, sin intermediarios. Código real que corre en tu terminal y que puedes controlar con lenguaje natural.

En el video de arriba muestro exactamente cómo lo armé y cómo funciona en vivo. Acá te dejo el resumen y los recursos para que lo repliques.

---

**Qué puede hacer**

Todo lo que harías tú dentro del Ads Manager, pero desde la terminal con un mensaje:

- Ver en qué campañas estás gastando y cuánto
- Identificar los ads con mejor CPA
- Pausar o activar campañas y adsets
- Cambiar presupuestos
- Crear campañas nuevas completas, con copies personalizados por país
- Analizar tus top performers por período

Lo que me voló la cabeza fue cuando le pedí que creara una campaña de retargeting para mis 5 mejores países con copy personalizado para cada uno. A España le metió "No curres solo", a Chile "No batalles solo". Nadie le dijo cómo hacerlo, él lo infirió del contexto.

---

**Por qué funciona mejor que contratar a alguien**

No porque sea más inteligente que una persona. Sino porque nadie conoce tu negocio mejor que tú.

Cuando tienes un media buyer, igual tienes que explicarle el contexto, los ángulos, qué quieres probar. Aquí ese paso se elimina. Tú le hablas directo, el contexto ya está en el [CLAUDE.md](http://CLAUDE.md), y los cambios son instantáneos.

---

**El setup en 3 pasos**

**1. Crea tu app en Meta for Developers**

Entra a [developers.facebook.com](http://developers.facebook.com) → My Apps → Create App. Dale todos los permisos posibles (Marketing API, páginas, catálogos). Publica la app y genera un access token desde Graph API Explorer con todos los scopes que necesitas.

**2. Inicializa el proyecto con Claude Code**

Copia el prompt de abajo, pégalo en Claude Code con tu token al final y deja que lo arme todo solo. En menos de 2 minutos tienes el proyecto completo funcionando.

**3. Verifica la conexión**

```
node src/cli.js accounts
```

Si ves tus cuentas de Ads, estás listo.

---

**One Prompt Setup**

```
Tu rol es ser Matías, mi Ad Manager personal de Meta Ads. Tu trabajo es 
gestionar, analizar, modificar y crear campañas directamente desde la 
terminal usando la API de Meta — sin que yo tenga que abrir el Ads Manager.

Cuando te pida algo, lo ejecutas. Si quiero pausar un adset, lo pausas. 
Si quiero subir el presupuesto, lo subes. Si quiero una campaña nueva 
con copies por país, la creas. Operas en español y confirmas cada acción 
antes de ejecutarla.

Para empezar, crea el proyecto Node.js desde cero.

Stack propuesto: ESM modules, fetch nativo, dotenv, Meta Marketing API.

Archivos a crear:
- .env → META_ACCESS_TOKEN y META_API_VERSION=v21.0
- src/api.js → cliente HTTP base con manejo de errores
- src/campaigns.js → listar cuentas, campañas, adsets, ads, insights; pausar/activar; cambiar presupuesto
- src/analyze-countries.js → gasto por país, CPA, ranking de mejor a peor
- src/analyze-ads.js → top performers por compras y por CPA
- src/cli.js → comandos: accounts, campaigns, insights, pause, activate, budget, adsets, ads
- CLAUDE.md → Créalo con lo que necesitamos,

Cuando termines avísame. Pego el token y corremos node src/cli.js accounts para verificar.

MI TOKEN: [pega aquí tu access token]
```

---

**Lo que viene**

El siguiente paso natural es conectar esto con un generador de crea.
