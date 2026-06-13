# 📝 Maquetación MVP

> Ruta: Vibe-Coding › 📝 Maquetación MVP

**🎬 Vídeo (28.6 min):** https://youtu.be/ftQs8rDs3B0

**📎 Recursos:**
- [GEM Generador de PRDs](https://gemini.google.com/gem/f3be5f5276c7)

---

## Parte IV. Mejores prácticas, metaprompting y maquetación del MVP

En esta lección vas a aprender la forma correcta de trabajar con Antigravity y agentes de IA para construir rápido sin hacer un desastre.  
Aquí definimos el método. Si entiendes esto, el resto del curso se vuelve 10 veces más fácil.

### Qué vamos a ver en esta lección

En este video cubrimos 3 cosas:

1. **Qué es metaprompting** y por qué importa en vibe coding.
2. **Qué es un PRD** y por qué es “la biblia” cuando trabajas con agentes.
3. Cómo usar **Google AI Studio** para maquetar el MVP de Automation Opportunity Finder y luego llevarlo a Antigravity con control de versiones en GitHub.

## 1. Qué es metaprompting

Metaprompting es un método para **refinar prompts usando IA**.  
En lugar de escribir un prompt a mano y esperar que funcione, le pides a la IA que:

1. Analice tu idea.
2. Identifique huecos o ambigüedades.
3. Y te genere el mejor prompt posible para construir el producto.

En este curso usamos metaprompting para transformar una idea general en un documento claro, usable y ejecutable.

## 2. Qué es un PRD y por qué lo necesitas

PRD significa **Product Requirements Document**.  
Es un documento que define el producto con claridad.

Un buen PRD incluye:

- Visión y objetivo.
- Problema que resuelve.
- Público objetivo.
- Funcionalidades.
- Restricciones.
- Criterios de aceptación.
- Prioridades.
- Métricas de éxito.
- Flujos de usuario.
- Tech stack.

En vibe coding el PRD no es “algo bonito”.  
Es literalmente la referencia principal para que el agente no invente cosas.  
Mientras más claro el PRD, mejores resultados obtienes.

## 3. Mejores prácticas para vibe coding (y para Antigravity)

Estas son las reglas que seguimos en el curso:

### Regla 1. Trabaja por “features”, no por “hazme toda la app”

Nunca le digas a un agente: “*hazme toda la aplicación*”.  
Divide el proyecto en piezas.

Ejemplos de features del Automation Opportunity Finder:

- Autenticación con Supabase.
- Dashboard con métricas.
- Wizard para crear diagnóstico.
- Pantalla de resultados.
- Módulo de clientes.
- Cotizaciones.
- Seguimientos.

Cada feature es una tarea.  
Así controlas calidad, velocidad y errores.

### Regla 2. Maneja el trabajo como un equipo de desarrollo real

Aunque sea IA, funciona igual que un equipo.

- Un agente puede trabajar en un feature.
- Otro agente puede corregir un bug.
- Otro puede hacer refactor.

No metas todo en una sola conversación interminable.  
Usa ciclos cortos, objetivos claros y revisa cambios.

### Regla 3. Primer prompt en Antigravity: “analiza el proyecto”

Cuando arrancas, lo primero que debes pedirle al agente es:

- Que analice el proyecto completo.
- Que lea carpetas y archivos.
- Que entienda el stack.
- Que te pregunte lo que falta.

No le pidas cambios antes de que entienda el sistema.

### Regla 4. Especifica el objetivo y limita el alcance

En cada tarea, define:

- Qué quieres lograr.
- Qué archivos puede tocar.
- Qué NO debe cambiar.

Deja que proponga cambios.  
Tú revisas el diff.  
Aceptas o corriges.  
Y sigues.

### Regla 5. Usa guías internas cuando escales

Antigravity permite reglas, archivos markdown y guías internas para que el agente:

- Siga lineamientos de autenticación.
- Respete estilo de UI.
- No rompa estructura.
- Mantenga calidad.

En el MVP no nos vamos a meter profundo en eso, pero sí vas a entender la idea para cuando subas de nivel.

## 4. Maquetación del MVP en Google AI Studio

En este video hacemos lo siguiente:

1. Partimos de la idea del producto.
2. [La pasamos por el “gem” que genera el PRD para vibe coding.](https://gemini.google.com/gem/f3be5f5276c7)
3. Revisamos el PRD y corregimos lo que no nos gusta.
4. Copiamos el PRD a Google AI Studio para que nos genere la app base.

Importante.  
En esta etapa, el objetivo NO es que todo funcione perfecto.  
El objetivo es definir:

- UI/UX.
- Estructura del proyecto.
- Rutas y pantallas.
- Componentes principales.

La funcionalidad real la terminamos en Antigravity.

## 5. Ajustes que hacemos después de la primera maqueta

Después de generar la primera versión, hacemos iteraciones rápidas, por ejemplo:

- Cambiar toda la interfaz a español.
- Ajustar el tech stack mostrado dentro de la app.
- Validar formularios. Ejemplo: no avanzar sin nombre.
- Crear una pantalla real de settings con dark mode y light mode.
- Mejorar el flujo de diagnóstico.

También revisamos un detalle importante:  
Si agregamos input de audio, debe haber confirmación clara de que:

- Se guardó.
- Se analizó.
- Y se refleja en el resumen del diagnóstico.

## 6. Control de versiones con GitHub (lo mínimo que debes hacer)

En este video también te muestro el flujo básico:

- Conectar repo a GitHub.
- Hacer commits por cambios.
- Revisar historial.
- Ver diferencias entre commits.

No vamos a profundizar en Git.  
Pero sí quiero que lo uses, porque sin versionado te vas a disparar en el pie.

### Resultado esperado al terminar esta página

Al finalizar esta lección debes tener:

- Un PRD usable para el MVP.
- Una primera versión maquetada en Google AI Studio.
- El proyecto guardado y versionado en GitHub.
- Claridad total de cómo trabajar por features y ciclos cortos.
- Una app base lista para continuar el desarrollo en Antigravity.

### Errores comunes

- Pedirle al agente “haz toda la app”.
- No tener PRD. Resultado: el agente inventa.
- No trabajar por features.
- No revisar cambios antes de aceptar.
- No usar commits. Luego no puedes volver atrás.
- Confundir maqueta con app funcional. La maqueta es solo el inicio.
