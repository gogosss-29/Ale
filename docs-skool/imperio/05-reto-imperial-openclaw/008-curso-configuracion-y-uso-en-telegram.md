# [Curso] 💬 Configuración y uso en Telegram

> Ruta: 🦞 Reto Imperial OpenClaw › [Curso] 💬 Configuración y uso en Telegram

**🎬 Vídeo (26.5 min):** https://www.loom.com/share/7cd649403fc2458299c18aab073be308

---

## 🎯 Objetivo

Dejar OpenClaw **operativo**, **conectado a un modelo**, **con Telegram funcionando**, y **configurado como servicio persistente**, no como algo que muere cuando cierras la terminal.

## 🧭 Paso 1. Quick Start y navegación inicial

En el asistente inicial de OpenClaw:

- Navega usando **flechas**
- Confirma con **Enter**
- Selecciona **Quick Start**

## 🧠 Paso 2. Selección del modelo

OpenClaw soporta múltiples proveedores:

- Anthropic
- Gemini
- OpenRouter
- Minimax
- Moonshot (Kimi)
- OpenAI
- Otros

### Recomendación del curso

👉 **Anthropic + Opus 4.5**

Motivos:

- Calidad de razonamiento
- Estabilidad
- Ideal para agentes
- Control fino de costos vía API Key

### 📌 IMPORTANTE

❌ No uses sesión directa de tu plan personal  
✔️ Usa **API Key dedicada**

Evitas:

- Consumir tu plan personal
- Bucles que quemen tokens
- Accidentes caros

```
Seleccionar proveedor: Anthropic
Seleccionar modelo: Opus 4.5

```

## 🔑 Paso 3. Configurar Anthropic API Key

Selecciona:

- **API Key** (NO token de sesión)

```
ANTHROPIC_API_KEY=PEGAR_AQUI_TU_API_KEY

```

📌 Recomendación:

- Crea una key **solo para OpenClaw**
- Presupuesto bajo ($5–$10 para pruebas)

![CleanShot 2026-02-06 at 15.38.28.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/92c546a2ccec46598cdd8ea418b38abf851a67bfcc8b49ed8f7ffd0f02c21399)

## 🗨️ Paso 4. Seleccionar canal de comunicación

Selecciona:

- **Telegram**

Motivos:

- Fácil
- Estable
- Ideal para bots
- Excelente UX en Mac / Windows

## 🤖 Paso 5. Crear bot en Telegram (BotFather)

En Telegram:

1. Busca `@BotFather`
2. Ejecuta `/newbot`
3. Asigna: - Nombre visible
- Username único (DEBE terminar en `bot`)

Ejemplo:

- Nombre: `OpenClaw`
- Username: `openclaw_amigo_bot`

```
TELEGRAM_BOT_TOKEN=PEGAR_AQUI_TOKEN_DE_BOTFATHER

```

---

## 🧩 Paso 6. Selección inicial de skills

📌 Regla clave:

> **No instales todo. Instala solo lo necesario.**

Los skills pueden:

- Ejecutar código
- Acceder a servicios externos
- Introducir riesgos si no los revisas

### Skills recomendados en esta etapa

Seleccionar:

- ✅ CloudHub CLI
- ✅ Gemini CLI
- ✅ OpenAI Whisper

No seleccionar todavía:

- Password managers
- Mail servers
- Twitter / X
- Bases de datos externas

## 🔑 Paso 7. Configurar Gemini API Key (opcional pero recomendado)

Si seleccionas Gemini:

```
GEMINI_API_KEY=PEGAR_AQUI_TU_API_KEY

```

📌 Recomendación:

- Proyecto dedicado en Google Cloud
- Billing activo
- Límites bajos al inicio

## 🎙️ Paso 8. Configurar OpenAI Whisper (audio en Telegram)

Permite:

- Enviar audios
- Transcripción automática
- Respuestas inteligentes

```
OPENAI_API_KEY=PEGAR_AQUI_API_KEY_WHISPER
```

## 🚦 Paso 9. Finalizar setup inicial

- Saltar hooks avanzados
- Omitir configuraciones complejas
- Continuar

Resultado:

- Dashboard inicial activo
- Puerto local asignado (ej. 1627)

## 🌐 Paso 10. Crear túnel (Gateway) para acceder al dashboard

OpenClaw corre en el VPS.  
Necesitamos un **túnel** para acceder desde nuestra máquina.

### ⬇️ PLACEHOLDER COMANDO GATEWAY

```
openclaw gateway --port 18789 --verbose

```

⚠️ Usa el nombre correcto del binario (`openclaw`, no cloudbot).

## 🔁 Paso 11. Conexión SSH adicional (túnel local)

En una **nueva pestaña de terminal**:

```
ssh openclaw@IP_DE_TU_VPS

```

📌 Password:

- **Usuario OpenClaw**
- NO root

## 💬 Paso 12. Primera prueba de chat (web)

- Abre el dashboard
- Envía un mensaje de prueba
- Verifica respuesta

![CleanShot 2026-02-06 at 15.41.47.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/ecc86739d51a44e5b8e6fed59a3c5e17ba19211c0a3440ebaf03965fb2ebac84-md.png)

## 📲 Paso 13. Conectar Telegram desde el chat

Desde el dashboard, dile al agente:

> “Quiero usar Telegram como canal principal”

Sigue instrucciones:

- Código de pairing
- Confirmación en Telegram

## 🎧 Paso 14. Prueba de audio (Whisper)

Envía:

- Un mensaje de voz por Telegram

Verifica:

- Transcripción correcta
- Respuesta coherente
- Auto-reparación si falla

## ⚙️ Paso 15. Configurar OpenClaw como servicio persistente

Esto evita que OpenClaw muera al cerrar la terminal.

```
sudo nano /etc/systemd/system/openclaw-gateway.service

```

```
[Unit]
Description=Openclaw Gateway (always-on)
After=network-online.target
Wants=network-online.target

[Service]
User=openclaw
WorkingDirectory=/home/openclaw
Environment=PATH=/home/openclaw/.npm-global/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ExecStart=/home/openclaw/.npm-global/bin/openclaw gateway --bind loopback --port 18789 --verbose
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target


```

```
sudo systemctl daemon-reload
sudo systemctl enable openclaw-gateway
sudo systemctl start openclaw-gateway
sudo systemctl status openclaw-gateway

```

## ✅ Resultado final de esta página

- Modelo configurado
- API Keys separadas
- Telegram operativo
- Audio funcionando
- Gateway activo
- Servicio persistente
