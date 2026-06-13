# 🏗️ Despliegue en Local

> Ruta: Vibe-Coding › 🏗️ Despliegue en Local

**🎬 Vídeo (20.8 min):** https://youtu.be/uQEPoSNfLX4

---

## Parte V. Clonar el repo, plan de desarrollo, correr en local y primeros fixes

En esta lección vas a pasar de “maqueta” a “proyecto real corriendo en tu máquina”.

Aquí hacemos 4 cosas clave:

1. Clonamos el repositorio desde GitHub a Antigravity.
2. Le pedimos al agente que analice el proyecto y nos regrese un plan de desarrollo.
3. Configuramos variables de entorno y corremos la app en local con Vite.
4. Arreglamos los primeros bugs típicos. Tailwind, dark mode y legibilidad.

Si no terminas esta página con el proyecto corriendo en local, no avances.

## 1. Clonar el repositorio en Antigravity

En Antigravity seleccionamos **Clone Repository**.

Qué sucede aquí:

1. Antigravity te pide autenticar con GitHub.
2. Te da un código.
3. Pegas el código en GitHub y autorizas.
4. Seleccionas tu repo.
5. Eliges una carpeta local donde guardarlo.
6. Abres el proyecto.

Resultado:

- **Proyecto clonado en local.**
- **Archivos visibles en el explorador.**
- **Git listo para trabajar desde Antigravity.**

## 2. Primer paso antes de tocar nada. Pídele al agente que entienda el proyecto

Antes de pedir cambios, hacemos esto:

- Ponemos el agente en **modo Planning**.
- Elegimos un modelo “fuerte” para pensar.
- Le pedimos que: - Lea el PRD.
- Lea los README.
- Identifique el tech stack.
- Liste features completos y pendientes.
- Proponga un plan de desarrollo por fases.
- Priorice para lanzar un MVP hoy.
- Considere deploy final en Vercel, pero primero local.

Este paso evita el error clásico:  
Pedir cambios sin que el agente entienda el sistema.

## 3. Segundo agente en paralelo. Preparar “agent skills”

En paralelo abrimos otra conversación en modo Fast y le pedimos al agente:

- Investigar qué son los **agent skills** en Antigravity.
- Recomendar la mejor forma de usarlos.
- Crear carpetas y placeholders para futuros skills.

Ojo:  
Esto no es obligatorio para que corra el MVP, pero sí prepara el proyecto para escalar mejor.

Aquí vas a ver por qué Antigravity pide permisos antes de aplicar cambios.  
Tú revisas. Tú aceptas. Ese es el flujo.

## 4. Ejecutar el proyecto en local

Una vez que el agente nos da el plan, le pedimos algo práctico:

- Confirmar el estado real de features según el PRD.
- Decirnos cómo correr el proyecto local con Vite.
- Decirnos qué variables de entorno necesitamos.

Normalmente el flujo es:

1. Crear un archivo `.env.local` en la raíz.
2. Pegar las variables necesarias.
3. Instalar dependencias si aplica.
4. Correr el comando de desarrollo.

En el video ejecutamos el comando de Vite en terminal y abrimos el localhost.

## 5. Variables de entorno. Qué necesitas y de dónde salen

En este paso el agente te guía para conseguir:

- API key de Google AI Studio.
- Project URL y API Key de Supabase.

Importante:  
Estas variables solo son para desarrollo local.  
No compartas tus keys. No las subas a GitHub.

## 6. Problema típico. “Abre en blanco” y no carga UI

Después de correr Vite, en el video pasa algo clásico:

- La app abre, pero se ve en blanco.
- Parece que no hay UI.

El agente detecta la causa.  
En este caso fue un tema de configuración de Tailwind con Vite.

Solución:

- Parar el servidor con Ctrl + C.
- Volver a correr con la configuración corregida.
- Recargar el navegador.

Resultado:  
La UI aparece correctamente.

## 7. Dark mode. Funciona, pero se rompe el diseño

Luego probamos el toggle de tema.

Problemas típicos que aparecen:

- Cambia a dark mode pero algunos componentes siguen en light.
- Cambia a dark mode pero el texto queda ilegible.
- Títulos o labels con color demasiado oscuro contra fondo oscuro.

Aquí sucede algo importante:  
Le pedimos al agente que lo arregle y que verifique con pruebas reales.

## 8. Lo más potente del video. Antigravity probando en el navegador

En esta parte Antigravity pide permiso para usar el navegador.

Qué hace:

- Abre un navegador controlado.
- Navega la app.
- Reproduce el bug.
- Verifica el problema visual.
- Toma evidencia.
- Aplica cambios.

Eso es oro. Porque ya no es “yo creo que…”.  
Es el agente viendo lo mismo que tú.

Resultado:

- Dark mode funciona.
- El texto se ve bien.
- La interfaz es legible.

## Resultado esperado al terminar esta página

Al final de esta lección debes tener:

- Repo clonado en Antigravity.
- Plan de desarrollo definido por el agente.
- `.env.local` creado y configurado.
- App corriendo en local con Vite.
- UI visible correctamente.
- Dark mode funcionando y legible.
- Cambios guardados con commits.

## Errores comunes

- No clonar el repo correctamente, o no autorizar GitHub.
- No crear `.env.local` o poner variables incorrectas.
- Subir keys por accidente al repo.
- Confundir “maqueta” con app funcional.
- No reiniciar Vite después de cambios de config.
- Pensar que dark mode “ya está” cuando el texto no se lee.

### Qué sigue

En la siguiente página vamos con el siguiente paso del MVP:

- Conectar Antigravity con **n8n** vía MCP.
- Ejecutar un flujo real.
- Y empezar a generar automatizaciones desde prompts.

Después:

- Conexión y notificaciones con Supabase.
- Deploy final en Vercel.
