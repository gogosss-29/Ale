# 🚀 Instalación completa de EvolutionAPI en VPS

> Ruta: Automatizaciones n8n › 🚀 Instalación completa de EvolutionAPI en VPS

**🎬 Vídeo (50.9 min):** https://www.loom.com/share/65017562294c4506af96f8bee37bf121

---

### 🤔 Qué es EvolutionAPI y por qué usarlo

EvolutionAPI es una API open source que expone WhatsApp usando el protocolo Baileys y lo lleva a endpoints HTTP y webhooks.  
Sirve para:

- Bots de soporte y atención al cliente
- Automatizaciones con n8n y Make
- Agentes de IA con memoria de conversación usando Redis

No es proveedor oficial de Meta. Si lo usas para spam o blasts masivos te van a banear el número.

![CleanShot 2025-12-01 at 11.09.38.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c581fc080d0945ee852e5d3f270bb0338ff98eb902eb49eba7da2c795fe1b8fb.png)

### 🧱 Prerrequisitos antes de tocar nada

- VPS con Ubuntu 22.04 o posterior, que sea version LTS, Docker y EasyPanel funcionando
- n8n instalado en ese mismo servidor
- Un número con WhatsApp o WhatsApp Business para vincular vía QR
- Criterio mínimo para no usar esto como cañón de spam

### 🎯 Lo que hacemos exactamente en el video

1. Levantamos Redis en EasyPanel

- Explico qué es Redis y cómo n8n lo usa como “memoria” para el agente
- Caso real. juntar varios mensajes del usuario en un buffer para mandar todo el contexto a la IA - “Hola”
- “Cómo estás”
- “Me das informes”
- En vez de responder cada uno por separado, guardamos en Redis y enviamos. “Hola, cómo estás, me das informes”

1. Creamos PostgreSQL en EasyPanel

- Postgres como base de datos de apoyo para EvolutionAPI
- Comentamos otras opciones. Mongo, MySQL, etc. pero usamos Postgres por velocidad y porque está en el mismo VPS

1. Instalamos EvolutionAPI desde Templates en EasyPanel

- Projects → New Project → evolution-api
- Templates → EvolutionAPI → Create → Deploy
- Sin comandos raros de Docker. el template ya viene armado

1. Entramos al Evolution Manager y sacamos la API Key

- Abrimos el servicio desde EasyPanel con el botón “Open”
- Entramos al Manager y mostramos dónde está la API Key en las variables de entorno
- Usamos esa API Key para loguearnos en el Evolution Manager

![CleanShot 2025-12-01 at 11.11.53.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/44bb78ec22334d42beea415c3e6f0ae5ba85b9acb7d0450c92f5c5e915905a68-md.png)

1. Creamos la instancia Baileys y escaneamos el QR

- Manager → Instances → New → canal Baileys
- Le ponemos nombre. por ejemplo “soporte” o el nombre del cliente
- Get QR, escaneamos desde WhatsApp → Dispositivos vinculados
- Se sincronizan contactos, chats y mensajes. el número queda “conectado”
- Ajustamos settings para no hacer el ridículo

Recomendado en el video.

- Ignorar grupos. no quieres tu bot spameando grupos personales
- Rechazar llamadas
- Opcional. - No marcar mensajes como leídos
- No mantener el número “siempre en línea”
- Conectamos EvolutionAPI a n8n por webhook

- En Evolution activamos `messages.upsert` como evento principal
- En n8n creamos un Webhook (POST) con un path corto. por ejemplo `/evolution`
- Explico la diferencia entre URL de prueba y URL de producción en n8n. - Test. `/webhook-test/evolution`
- Prod. `/webhook/evolution`
- Pegamos la URL de prueba en el Manager y disparamos un mensaje de WhatsApp para verificar que n8n recibe el payload correctamente
- Instalamos el nodo de comunidad `n8n-nodes-evolution-api`

- n8n → Settings → Community Nodes → Install
- Buscamos `n8n-nodes-evolution-api`
- Lo instalamos y revisamos que aparezca en el buscador de nodos

![CleanShot 2025-12-01 at 11.13.07.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/c1d677bb1c8c40d58949b288cfe92df542ad00f00f93429e978bb6627efb712c.png)

1. Creamos credenciales de EvolutionAPI en n8n

- Server URL. la del Manager pero sin el `/manager` al final
- API Key. la misma que copiamos de las variables de entorno en EasyPanel
- Probamos la conexión desde n8n hasta EvolutionAPI

1. Enviamos el primer mensaje de prueba por WhatsApp

- Nodo EvolutionAPI → `Send Text`
- `instanceName` = el nombre de tu instancia
- `number` = número de destino con formato correcto
- `text` = mensaje de prueba
- Ejecutamos el flujo y mostramos cómo llega el mensaje “Hola, mi bot recibió tu mensaje”

### 🧠 Buenas prácticas para no matar tu número

- No lo uses para envíos masivos ni campañas de marketing
- Úsalo para inbound. soporte y clientes que te escriben primero
- Calienta el número con uso humano los primeros días
- Agrega delays aleatorios de 1 a 5 segundos antes de cada respuesta
- Usa Redis para agrupar mensajes en una ventana de tiempo y pasar contexto a la IA
