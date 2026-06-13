# 🗂️ Scraping de Videos de YouTube con Transcript

> Ruta: Automatizaciones n8n › 🗂️ Scraping de Videos de YouTube con Transcript

**🎬 Vídeo (32.3 min):** https://www.loom.com/share/25f9a42af2304f50b0b2720fe21a4c64

**📎 Recursos:**
- YT Scraping Imperio

---

Hoy les traigo un flujo de scraping de YouTube con n8n que quedó realmente brutal.

Con este proyecto puedes sacar de forma automática.

- IDs de videos de un canal o playlist
- Transcripts completos de esos videos
- Guardarlo todo en Airtable listo para hacer resúmenes, búsquedas y análisis

Este es el “backend”. En una segunda parte se conecta a un front con Lovable para que un usuario no técnico solo pegue un link y reciba resumen.

📌 ¿Qué resuelve este flujo?

- Sacar el transcript de videos de YouTube
- Generar un resumen rápido por cada video
- Dejar la información guardada en una base de datos
- Sin entrar a cada video a mano ni copiar nada.

🧱 Stack que se usa en el video

- n8n self hosted en un VPS administrado con EasyPanel
- YouTube Data API v3 para obtener los videos de una playlist
- YouTube Transcript API ([https://www.youtube-transcript.io/api](https://www.youtube-transcript.io/api)) para sacar el texto
- Airtable como base de datos para guardar transcripts y resúmenes
- Google Cloud Console para generar la API key de YouTube

![CleanShot 2025-11-25 at 18.05.32.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/29bd4178ad2d4cf3ad0a296a29e049d03175578d057b44dfbd148ab3a90fb059-md.png)

## 🔄 Paso 1. Mantener n8n actualizado

Antes de construir el flujo, en el video se actualiza n8n dentro de EasyPanel.

1. Entrar a EasyPanel y abrir el servicio de n8n.
2. Ir a la pestaña `Source` o donde esté configurada la imagen.
3. Ver versión actual, por ejemplo `1.16.2`.
4. Ir a GitHub Releases de n8n y buscar la última versión estable, no las “pre-release”. - Ejemplo. `1.120.4` liberada hace pocas horas.
5. Copiar esa versión en EasyPanel, guardar y hacer deploy de nuevo.

Resultado. n8n corre en la última versión estable sin tocar nada de código.

![CleanShot 2025-11-25 at 18.08.44.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/8083645bf94941c3a9b791f5098ad950b98e3389b5d5427da3f881d40eee4937.png)

## 🔑 Paso 2. Preparar las APIs de YouTube

Se necesitan dos cosas.

1. Canal o playlist de YouTube - Se usa el canal de Benja como ejemplo.
- Para obtener la playlist correcta, no se usa el `channel_id` sino el `playlist_id`.
- Una forma sencilla. usar herramientas como youtubetranscript.io para sacar los datos del canal y ubicar la playlist.
2. API Key de YouTube Data API v3 - Ir a Google Cloud Console.
- Seleccionar el proyecto que ya usas con n8n o crear uno nuevo.
- Habilitar `YouTube Data API v3`.
- Ir a `Credenciales` y crear una “clave de API”.
- Opcional pero recomendable. restringir la API key para que solo pueda usar YouTube y solo desde tus servidores o dominios.

![CleanShot 2025-11-25 at 18.09.40.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/0587300d30544305844560ea506d4283c9930f14520b40b786b4f8a385dc8cce.png)

## 🧩 Paso 3. Flujo en n8n para sacar videos de una playlist

Empezamos con un flujo manual para pruebas.

1. Trigger manual - Nodo inicial de tipo “Manual Trigger”.
- Esto se cambiará más adelante por un webhook cuando se conecte al front.
2. HTTP Request a YouTube Data API - Método. GET
- Endpoint. `https://www.googleapis.com/youtube/v3/playlistItems`
- Parámetros clave. - `part = contentDetails`
- `playlistId = [ID de la playlist, no del canal]`
- `maxResults = 50` (límite por llamada)
- `key = [tu API key de YouTube]` Se probaron dos formas. - Pasar los parámetros directamente en la URL
- Usar la pestaña de `Query Parameters` en el nodo de n8n

Conclusión. es más limpio mandarlos como parámetros en el nodo, porque es más fácil debuguear cuando algo falla.

1. Validación importante - Si usas el `channelId` (el que empieza con `UC...`), falla.
- Lo correcto para playlistItems es usar el `playlistId` (el que empieza con `UU...` o similar).

![CleanShot 2025-11-25 at 18.10.49.png](https://assets.skool.com/f/4e1ca14852434c0abdefff35382cdf66/dbe08e9ea43e483ea19b36310ccd8593382d3ed202c044e5bea50e088038820a.png)

Este es un ejemplo del output en JSON:  


```
[
  {
    "kind": "youtube#playlistItemListResponse",
    "etag": "KpkWqdlI85w-nuVMJqWgPeipmAU",
    "nextPageToken": "EAAaHlBUOkNESWlFREF5T0RBM1JEazJRalV3UlRRMFFVVQ",
    "items": [
      {
        "kind": "youtube#playlistItem",
        "etag": "jnBgQx2qoy26-B2qdoPRyxYtRbM",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLlBjWGU5b2VqX3o0",
        "contentDetails": {
          "videoId": "PcXe9oej_z4",
          "videoPublishedAt": "2025-11-19T22:47:01Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "6aV2XdnC82qZXElmPMnE2_zH7zg",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLjZJSm9aaXZBUVln",
        "contentDetails": {
          "videoId": "6IJoZivAQYg",
          "videoPublishedAt": "2025-11-13T20:56:35Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "YeWS2eptTd_XO8RcucJQFiksQ2A",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLlNPQjFrb091VkFj",
        "contentDetails": {
          "videoId": "SOB1koOuVAc",
          "videoPublishedAt": "2025-11-04T02:56:45Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "CGnuVG4f2Tf5NSO8hV2OU-65j8U",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLm55LW9IcV9uZW1R",
        "contentDetails": {
          "videoId": "ny-oHq_nemQ",
          "videoPublishedAt": "2025-10-07T22:23:00Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "9WigKATY_BiMl7LjBqPjlCv_YQM",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLlI2cnFwNWFMeDBV",
        "contentDetails": {
          "videoId": "R6rqp5aLx0U",
          "videoPublishedAt": "2025-09-29T17:14:00Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "FnXotIOJcElw9WXWKMSdmrGHok4",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLlU3eXJ0T3Vfb21V",
        "contentDetails": {
          "videoId": "U7yrtOu_omU",
          "videoPublishedAt": "2025-09-17T14:34:04Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "T3un5yqKYv00RbySjRsejw_Jgxo",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLkszSmcxSjZ1R1hZ",
        "contentDetails": {
          "videoId": "K3Jg1J6uGXY",
          "videoPublishedAt": "2025-09-10T19:50:01Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "pUifz_nR_I5dMUTU1jLTMVln26s",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLjdkSzcxdUc0ME9n",
        "contentDetails": {
          "videoId": "7dK71uG40Og",
          "videoPublishedAt": "2025-09-03T14:14:09Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "IMA1EpkK4K06C6gMx10SRYs5SWU",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLnpTUHZ4cVNjM2tj",
        "contentDetails": {
          "videoId": "zSPvxqSc3kc",
          "videoPublishedAt": "2025-08-27T23:40:42Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "rCAU074_-7khQw8tBIC376WNATE",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLkx1eXh0U21ZZVhV",
        "contentDetails": {
          "videoId": "LuyxtSmYeXU",
          "videoPublishedAt": "2025-08-22T19:54:22Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "S2dIiCu32iYxmPykrvLJumtKGlE",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLjRaZjVzX2RMSXVZ",
        "contentDetails": {
          "videoId": "4Zf5s_dLIuY",
          "videoPublishedAt": "2025-08-13T18:40:42Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "FHRBVQ7KPp7SHcY6Oz6PKlceGhQ",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLjVtcVZQRXdOX2RR",
        "contentDetails": {
          "videoId": "5mqVPEwN_dQ",
          "videoPublishedAt": "2025-08-08T03:58:40Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "OvgXfK5EkmjzPvpuLTP7kwNa6do",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLmFKLUxTZTNHblZV",
        "contentDetails": {
          "videoId": "aJ-LSe3GnVU",
          "videoPublishedAt": "2025-07-29T16:43:47Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "DO3xBhHcZSLw2v8-_7b4VIikC74",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLm5zcTFrX3V6WC1F",
        "contentDetails": {
          "videoId": "nsq1k_uzX-E",
          "videoPublishedAt": "2025-07-15T17:56:58Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "Wi9BN8iRJjvD9sVsv8O1AYaC9TI",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLlVWeGg2R1ZxVnlN",
        "contentDetails": {
          "videoId": "UVxh6GVqVyM",
          "videoPublishedAt": "2025-07-01T01:14:12Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "jpQEqToKWpCjPz---VqIkUAer-k",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLnNrUHFHNU9TQ1dr",
        "contentDetails": {
          "videoId": "skPqG5OSCWk",
          "videoPublishedAt": "2025-06-19T18:30:24Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "MXq9wK3ZVqDqgWNXqXc237nrYq8",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLkdkY0V3QnlPaWt3",
        "contentDetails": {
          "videoId": "GdcEwByOikw",
          "videoPublishedAt": "2025-06-08T02:38:19Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "ya6rjXhzktL1vksrmlT3nfDKTHs",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLnBTNzRPMEV2WS1j",
        "contentDetails": {
          "videoId": "pS74O0EvY-c",
          "videoPublishedAt": "2025-05-31T21:18:04Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "jKU7l4nCZLTRLdhL75g-Y2e8GBc",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLi1fSWwwbGF1SlFz",
        "contentDetails": {
          "videoId": "-_Il0lauJQs",
          "videoPublishedAt": "2025-05-23T19:29:34Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "KTi8po5-7NG_d7sY9AQTcsabNAE",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLjZKYjYyMkNtRUFv",
        "contentDetails": {
          "videoId": "6Jb622CmEAo",
          "videoPublishedAt": "2025-05-15T20:25:46Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "6RBUTj3nmZoML_2k2ZxhrR19Ypw",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLkZxa3B1dy1EQ1JN",
        "contentDetails": {
          "videoId": "Fqkpuw-DCRM",
          "videoPublishedAt": "2025-04-25T20:21:31Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "fET_XiKcG220S465kr9-8DmnIZs",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLlFOM0o5cUJfNFZ3",
        "contentDetails": {
          "videoId": "QN3J9qB_4Vw",
          "videoPublishedAt": "2025-04-25T19:37:16Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "JpV005EaQk7_nHhvBPlIhU_jOOk",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLjkwM2p0RzJ2d1VZ",
        "contentDetails": {
          "videoId": "903jtG2vwUY",
          "videoPublishedAt": "2025-04-11T14:04:11Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "M7g8mj34BqUWqV_nDb-caMQMoyE",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLjZJNzgwemhlSHpV",
        "contentDetails": {
          "videoId": "6I780zheHzU",
          "videoPublishedAt": "2025-03-27T12:04:34Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "HJoPw8kxCbDaZCHkF_-_X4LzWFw",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLkN2TDk1YWt0bzhZ",
        "contentDetails": {
          "videoId": "CvL95akto8Y",
          "videoPublishedAt": "2025-02-28T18:32:14Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "x80PXfJh8DzkFQqCTjw4SI-Rqq8",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLlVRbWpzM1F5emlZ",
        "contentDetails": {
          "videoId": "UQmjs3QyziY",
          "videoPublishedAt": "2025-02-19T19:47:12Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "MVQoTw0E9_y16pXSb1iJ0pAY9GM",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLlhZUVgtQTNzaDlj",
        "contentDetails": {
          "videoId": "XYQX-A3sh9c",
          "videoPublishedAt": "2025-02-05T22:03:15Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "dE1j-a4NhPkfwMBWbKG7sANIQPo",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLmJhcW5lMk1WZUdR",
        "contentDetails": {
          "videoId": "baqne2MVeGQ",
          "videoPublishedAt": "2025-01-24T05:47:22Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "iOEKt-jUHh-8YcqeJPZPR3r9nZo",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLkZIXzdrSHNGZkcw",
        "contentDetails": {
          "videoId": "FH_7kHsFfG0",
          "videoPublishedAt": "2025-01-16T21:08:03Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "XECvvOM_zm-siuk418b_8BWYbXE",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLmNfVlZDYWRhT3gw",
        "contentDetails": {
          "videoId": "c_VVCadaOx0",
          "videoPublishedAt": "2025-01-02T20:54:55Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "Df6rSzHfnR0IGkeo8LqOd9sG1DM",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLmxFRWZhRmJoVy1Z",
        "contentDetails": {
          "videoId": "lEEfaFbhW-Y",
          "videoPublishedAt": "2024-12-26T23:56:23Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "_A7-Qv8-oNTefpX3wQDE1TyrQqU",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLmxWR1Y1LTVUZFRV",
        "contentDetails": {
          "videoId": "lVGV5-5TdTU",
          "videoPublishedAt": "2024-12-19T22:33:15Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "XAlqbKNdLJJYhEFVquMzoZh5q0U",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLmZRbVVSLWpJelow",
        "contentDetails": {
          "videoId": "fQmUR-jIzZ0",
          "videoPublishedAt": "2024-12-17T00:23:45Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "eBfmozDayNLKZ_GOHsYnsuWb6hw",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLjcwNjc3SHpxajBN",
        "contentDetails": {
          "videoId": "70677Hzqj0M",
          "videoPublishedAt": "2024-12-06T19:19:02Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "13Db8M0BxPCK_0ku4pvm6IvMmps",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLlU1YmdDbXQ3S1Jv",
        "contentDetails": {
          "videoId": "U5bgCmt7KRo",
          "videoPublishedAt": "2024-11-21T16:31:19Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "urMWH_UwxduPojfPGM4yhmyHK84",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLlBmdXoxbDBuMjRv",
        "contentDetails": {
          "videoId": "Pfuz1l0n24o",
          "videoPublishedAt": "2024-11-13T21:43:11Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "Up_0rZ7HnOImEp5u9KpIEvYqs3Y",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLnQ5aGd3cnp5Wmc4",
        "contentDetails": {
          "videoId": "t9hgwrzyZg8",
          "videoPublishedAt": "2024-11-12T00:55:57Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "bFuPTvVwPPn5pUjyGbdlFp0rAZc",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLm56dkdfOHh2ZGxN",
        "contentDetails": {
          "videoId": "nzvG_8xvdlM",
          "videoPublishedAt": "2024-11-01T00:01:52Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "El-Q9LNyV0wRP8Geu1mnGqzbN34",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLjEwdWZzRFNoWktZ",
        "contentDetails": {
          "videoId": "10ufsDShZKY",
          "videoPublishedAt": "2024-10-18T23:26:02Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "SzwmYOizIrjKRKdk1bco2pE2MmA",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLjY2LUd3SEQ1MjRn",
        "contentDetails": {
          "videoId": "66-GwHD524g",
          "videoPublishedAt": "2024-10-18T03:14:53Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "e2maOk9mMSasUh6S9Zd1lmLBYaA",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLmFKOGV5X1dKMGY4",
        "contentDetails": {
          "videoId": "aJ8ey_WJ0f8",
          "videoPublishedAt": "2024-10-14T00:27:39Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "fBRrQuBboBD1xzo1bGIYAGa96jc",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLmx4SlI1a0ZvbU1n",
        "contentDetails": {
          "videoId": "lxJR5kFomMg",
          "videoPublishedAt": "2024-10-07T20:16:34Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "-SoyAmR9UaXnPA8xkbDgwscTJo8",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLktWdW5aRFJPRzJz",
        "contentDetails": {
          "videoId": "KVunZDROG2s",
          "videoPublishedAt": "2024-09-23T21:09:49Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "K9VynlxOwSUrqVFhRtrUliLn04M",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLk14eE9XbTNQUk9Z",
        "contentDetails": {
          "videoId": "MxxOWm3PROY",
          "videoPublishedAt": "2024-09-13T01:04:13Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "mf7h9tNXwMyFhgYXG4EPFy1v6iM",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLk9kaU5LRkpBd1dB",
        "contentDetails": {
          "videoId": "OdiNKFJAwWA",
          "videoPublishedAt": "2024-09-03T03:55:21Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "sapyXtVfzwqSJVledOeTVmfw0uo",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLnFLUkJFUWJGdFRz",
        "contentDetails": {
          "videoId": "qKRBEQbFtTs",
          "videoPublishedAt": "2024-08-25T23:35:14Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "iTHFHuXzyeYmmQx3Qn2JP3EaJgY",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLmYzUjdQeEIybWZF",
        "contentDetails": {
          "videoId": "f3R7PxB2mfE",
          "videoPublishedAt": "2024-08-10T01:34:05Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "cBrl0D-Dml-bykVoa97DpQPwiug",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLmRiRVRzbWFKX1FR",
        "contentDetails": {
          "videoId": "dbETsmaJ_QQ",
          "videoPublishedAt": "2024-08-05T19:10:30Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "EFcTV1JhOOaLKH5QFGJ9AxXyOG4",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLlVfNzhVRndyWDdj",
        "contentDetails": {
          "videoId": "U_78UFwrX7c",
          "videoPublishedAt": "2024-08-02T21:32:41Z"
        }
      },
      {
        "kind": "youtube#playlistItem",
        "etag": "qiDbuovw1G4Kr8Jm705KwwYcDtg",
        "id": "VVVwcThsSEhsaUNTM29CdC1nZkwwYktRLjI0TzVlSTg5YUhN",
        "contentDetails": {
          "videoId": "24O5eI89aHM",
          "videoPublishedAt": "2024-07-29T19:54:16Z"
        }
      }
    ],
    "pageInfo": {
      "totalResults": 108,
      "resultsPerPage": 50
    }
  }
]
```

## 💻 Paso 4. Code node para extraer video IDs

El JSON de respuesta trae mucha información. No sirve mandar todo al siguiente nodo.

Se usa un Code node en JavaScript para.

- Recorrer `items` del JSON
- Crear un array limpio con cada `videoId`
- Opcionalmente limitar a X cantidad, por ejemplo 25, para no pasar del límite gratuito de la API de transcripts

En pseudo.

- Leer `items`
- Para cada item, tomar `contentDetails.videoId`
- Generar un array de IDs

Resultado. casi 50 videos convertidos en un array limpio de `["id1","id2",...]`.

## Codigo en JavaScript

```
const output = [];

for (const entry of items) {
  const playlistItems = entry.json.items || [];

  playlistItems.forEach(p => {
    output.push({
      json: {
        videoId: p.contentDetails.videoId,
        publishedAt: p.contentDetails.videoPublishedAt
      }
    });
  });
}

return output;

```

## 📜 Paso 5. Llamar a la API de transcripts en bloque

Aquí entra la API de YouTube Transcript.

1. Registrar cuenta en youtubetranscript.io - Plan gratuito. 25 transcripts al mes
- Plan de pago. 10 USD por 1000 transcripts mensuales
2. Nodo HTTP Request en n8n hacia la API de transcripts - Método. POST
- Endpoint. `/api/transcripts` (según doc de ellos)
- Body. JSON con un array de IDs, algo así como. - `{ "ids": ["videoId1","videoId2",...] }`

Para armar el body se usa una expresión.

- `JSON.stringify({ ids: $json.ids })` o similar, según cómo hayan quedado los datos en el Code node.

1. Límite de 25 - Como el plan free solo da 25 transcripts, en el Code node previo se limita el array a 25.
- El nodo HTTP entonces llama solo por esos 25 videos.

**Codigo para crear el Array (JS)**

```
const output = [];

for (const entry of items) {
  const playlistItems = entry.json.items || [];

  playlistItems.forEach(p => {
    output.push({
      json: {
        videoId: p.contentDetails.videoId,
        publishedAt: p.contentDetails.videoPublishedAt
      }
    });
  });
}

return output;

```

## 📊 Paso 6. Estructurar datos y guardarlos en Airtable

Con la respuesta de transcripts ya en n8n, se pasan a Airtable.

1. Tabla `youtube_transcripts` con campos. - `video_id`
- `title`
- `description`
- `transcript` (campo texto largo)
- `agent` o `resumen` (campo de texto generado por IA)
- `created_at` u otra fecha
2. ¿Por qué Airtable y no Google Sheets? - Google Sheets tiene limitación de caracteres por celda, alrededor de 5,000
- Un transcript completo de un video largo se la vuela sin problema
- Airtable maneja mucho mejor texto largo y sirve como “mini base de datos”
3. Nodo Airtable en n8n - Conectar la base `Scraping` o similar
- Elegir la tabla `youtube_transcripts`
- Mapear campos uno a uno. - `video_id` ← id del video
- `title` ← título del video (desde YouTube Data API)
- `description` ← descripción del video
- `transcript` ← texto de la API de transcript
4. Manejo de errores - En el flujo del video, 23 de 25 se guardaron bien, 2 fallaron
- Se configuró el nodo para `continue on fail`, así el proceso no se detiene por un error puntual

## 🤖 Paso 7. Resúmenes automáticos y usos posteriores

Una vez que tienes todos los transcripts en Airtable, puedes hacer varias cosas.

- Usar un campo tipo “agent” o alguna integración de IA en Airtable para generar resúmenes por fila
- Conectar un GPT propio vía API usando n8n, para crear. - Resumen corto
- Bullet points
- Títulos alternativos
- Crear un chatbot sobre tus videos. - Preguntas tipo “¿en qué video explican cómo instalar n8n en Ionos?”
- Responder en base a transcripts almacenados

Este flujo ya deja la base lista para todo eso.

## 🚀 ¿Por qué este proyecto es perfecto para empezar?

Porque.

- Combina APIs reales con un caso de negocio concreto
- Te enseña a trabajar con JSON “sucio” y transformarlo en algo útil
- Te obliga a entender límites, paginación y planes gratuitos
- Te deja una base en Airtable que se puede conectar a cualquier otra cosa

Es un proyecto sencillo a nivel concepto, pero muy completo a nivel práctica para quien está empezando serio con n8n.

📥 Plantilla lista para importar

Con eso, cualquiera puede replicar el flujo, adaptarlo a su canal y tener sus propios transcripts y resúmenes listos para automatizar contenido y análisis.

## 🎙️ Transcripción

Estaba grabando muy bien, en este video les voy a enseñar un proyecto bastante sencillo, con lo que pueden ir, para que vayan a hacer las pruebas, esto es un escraping de Youtube, es algo lo que estaba trabajando ayer. En mi aprecio donde trabajo me pidieron una forma de sacar el transcript y un resumen de videos de youtube entonces creé un pequeño flujo en el hn en la segunda parte te voy a hacer esto con lobo-bol para hacer una interfaz gráfica, el front tentigamos para la que sea más fácil para el usuario, el usuario final. Les voy a enseñar también un poco cómo actualizar su N8N, cómo crear su. los creenciarios o aut de google, etc. Entonces lo plano que vamos a hacer es ver aquí si estamos cuatro versiones detrás de el urbps, vamos a nuestro vps, en este caso yo estoy utilizando Easy Panel para para administrar el docker, vamos a iniciar sesión y vamos a ver aquí en el 8n, vamos a a source y vamos a ver que tengo la versión 116.2 vamos a ver el hecho de Geethoob y de este lado vamos a buscar felices y vamos a buscar al que se enlea este fue liberado hace 2 horas y es que podemos repetir lo que cambió básicamente es la versión más actual estable por si se le iras, si se fijan y el gavio de otras versiones se mueque el gavio el lisa es veo la 102.1 pero es a spree release que quiere decir que no es una versión estable entonces a mí siempre me gusta irme con las versiones estable en este caso está 120.4 vamos de vuelta a isi panel y vamos a poner aquí 120.4, le damos safe, le damos deploy y nos vamos a ver vídeos, está reiniciando servicio de N8N, vamos a esperar a que reinicie. para poder acceder en el 8M, que vamos a usar ahorita vamos a ocupar un canal de youtube en cual que vamos a sacar un trascit, voy a utilizar el de venja como ejemplo y estamos también creo una cuenta en youtube trascit esto nos va a hacer para sacar todos los transcripts, que tienen una cuenta gratuita que les permite sacar 25 transcripts, de ahí pueden pagar una suscripción cuesta 10 dólares y te da 1000 transcripts al mes vamos a amen a ocupar ero table para poder guardar todos los transcripts ustedes pueden usar Google Cheats porque uso youtuber table porque para vidos largos pues el transcript es largo y Google cheats tiene una restricción que por Zelda no puede haber más de cinco mil caracteres entonces por lo estoy ocupando verte y voy a ver más que me gusta más para poder crear interfazes vamos a ver cómo va listo y si quieres te va a hacer vamos a refrescar perfecto vamos a crear primero una carpeta para poder hacer pruebas, voy a poner interior y tal y dentro de esta carpeta como les comentaba esto va a ser de prueba que quiere decir que lo primero que vamos a hacer es vamos a hacer un de formado un flujo de forma muy manual y entonces vamos a subir este. un trigger manual para este caso, pero ya después en la segunda versión vamos a utilizar un web group para poderlo disparar desde un front end hecho con la bobo. Ok, entonces mi primer trigger, manual como vimos, y lo segundo que tengo que que hacer va a ser un htp request a la API de youtube para poder sacar el playlist como lo lo saca el playlist en este primer canal, pero yo no puedo venir aquí y utilizar este Arraba Vencord, porque no me lo va a aceptarme, necesito la id y una de las formas fáciles que lo pueden sacar es simplemente reducción de este herramienta, se lo voy a dejar por la descripción todos los videos. Gracias youtube transcre.io boy, vamos a darle tracking para medir, pongo aquí el canal Y, Ajarle, Vamos a usar ese río. y si les va a pedir que creo una cuenta, así que voy a crear una cuenta de rápido de lo iniciación, listo, entonces vamos de nuevo para acá, para acá, vamos a ver qué Channelinfo. y esto no está ahí, ahorita la vamos a ocupar vamos a continuar y después de esto necesitamos sacar una piqui de Google Apps. Para esto nos vamos a ir a nuestro cloud, ya que estamos en nuestro cloud, no que ya la consola Para tener que iniciar sesión obviamente ya tenemos vídeos en la comunidad de cómo sacar estas credenciales es importante que tener un proyecto si es que no lo tienen o escogan un proyecto en en este caso voy a ir a lo tengo y Y vamos a seleccionar este proyecto y vamos a ir a la parte de ver las papis que tenemos habilitadas. Nos vamos aquí para abajo donde dice el proyecto de noche en el cine, si vio lo tengo seleccionado el proyecto a pisis servicios habilita la pisisero servicios y vamos a buscar que dice youtube data a pv3 y es importante que lo habiliternos. Voy a exponer mis apiquís ahorita para, las cuestiones de poder les mostrar, pero una vez que termine las voy a eliminar, nos vamos a ir a credenciales, si se fijan yo tengo mi layout porque ya utilicé este proyecto para Ya utilicé este proyecto para conectar el drive, el cheat, el game y todo, pero no tengo ninguna clave a pintos, lo voy a generar la clave a P, igual que las cadenciales, clave a P, vamos a esperar a que cargue y Y aquí ya dice que tengo mi clave, voy a copiar y antes de usarla podemos seritarla y podemos añadir aquí varias cosas, pero los recomiendo que restrijan su clave a p y que pongan que solamente estéis poniendo. nible para lo que voy a ocupar en este caso que es youtube y pude ir a una registra restrujirla perdón tenuto por un doscientos web y agregando aquí la dirección de donde van a estar siendo los llamados los callbacks de ¿Qué vamos a hacer? Vamos de vuelta de noche, tenemos este HTTP y como les comentábamos les voy a dejar lo que es En la URL y todo el link de Notion, es la URL que vamos a instar, es un método GET, es la URL de Google Apps Official, YouTube v3, Playlist, Playlist Items. y vamos a pasarle parámetros, los parámetros lo separamos con sin interrogación, vamos a pasarle parte, igual content, details, vamos Vamos a pasar el simulo de un person más que su siguiente parametro Playlist AID con en mi escuela va a ser igual y Vamos a tomar la ILED que nos lleva a este. Lo pegamos, después de pleris ID. Necesitamos ponerle el máximo de resultados que nos va a arrojar Tengo en cuenta que solo te acepta o solo te puede mostrar hasta 50 resultados al mismo tiempo En este caso como tenemos una restricción de 25 5, tras la que podemos hacer, la zona va a poner 50, les voy a enseñar cómo pueden hacer ustedes, cómo pueden limitar eso. Entonces ya que tenemos esto, vamos a poner el siguiente parámetro que es justamente el Max Results. No sé qué es el final, por si no saben esto lo supone en las orillas y lo pueden hacer igual gran de pláxoma fácil que trabajen con esto y serian max En el momento de la pantalla, nosotros vamos a los voy a dejar aquí, match results igual a 50 y, aquí vuelta a la pic que generamos que es esto. No hay un desnonizado de mandar parámetros de aquí porque la estamos mandando en la URL podríamos ponerle parámetros aquí y ponerle por ejemplo este que dice vamos a hacer los dos para que van la diferencia, si yo lo amanecita el cual lo ejecuto, va a succeler y chiquio parámetros Ok, algo de botella de mani. Debo tener mal algún tipo, content details, content details y playing list. I D I say 1 A E Damascus Suárez en 50 un, un, un, un, extremo aquí escenore ver que tengo más y ahora ahorita, Ok, ya vi que a lo que tenia mal, estoy tomando el channel AID, que es empecé con use, pero esto es incorrecto, es error mío, porque de hecho yo estoy llamando playlist items, no estoy llamando al canal, entonces no me, este id de acá, lo que necesitamos es este id que empieza con www, acuerden que aquí de hecho, aquí te lo dice, este con character c, de chánero id, with you, se se fijan, termina con vela cacu y ese es veca cú, entonces simplemente tengo que regresarme para acá y cambiar esta seme y escula por humey y escula y le doy ejecutar, he listo, ya funcionó no está regresando en este caso los haydis de los vídeos que encontró ¿Cuántos encontró 700 y 700 videos? No está regresando 50 porque es el máximo que pueda regresarte por página. Si quisieramos escrepear hasta acá la información de los otros, ni estaríamos pasarle otro valor. que sería un expage pagination y hacer un segundo recuedes y así por cada bloque de 50. Para este caso no lo vamos a hacer, pero este es una forma de hacerlo, y vamos a hacer una prueba voy a duplicar esto para que, se puede enseñar y vamos a hacer lo mismo pero vamos a quitarlo de la URL y vamos a mandarlos para metros directamente aquí para que ven la diferencia si lo doy parte y le doy content el tencho, compropego, agrego lo nuevo y sería playlist id y ese sería mi value nuevo que se llama Match Results y mi value será 50 y por último mi key y la key sería la no tengo que copiar y, Así que ya puedo borrar a partir del sinutroresión en adelante Vamos a mandarlo y listo Si se fijan es exactamente lo mismo, pueden mandarlos para metros en la URL o los pueden mandar directamente aquí Creo que es más limpio y los mandamos desde aquí porque es más fácil ir y ver si algo está fallando entonces nos vamos a quedar con éste sin embargo esto no lo voy a borrar. Ya que tenemos todo esto que seguiría podríamos sacar directamente generar un output con un array, con todo lo que son los Vamos a iris para poderlos pasar a la siguiente app. y que necesitamos o de en este caso siquiera más quieren hacer uno podemos hacer vamos a hacer entonces el código obviamente estos códigos no los hago yo a manos simplemente le voy a chagir petit Mi Output es este, hasta el cual me voy aquí, lo copio, porque es más fácil si lo va aquí. Ok, aquí le digo este es mi Output, he visto que me generé un código en JavaScript para el 8n, donde me generé una array con todo. y listo. Entonces en este caso yo lo había hecho les voy a dejar el código a todas formas en la descripción, pero así tal cual es como lo pregunté HGPT. Vamos a sustituirlo aquí, pero básicamente tenemos una constante. que estamos creando, que se llama Output y esto le estamos diciendo que es una reglo, es una fort, que quiere decir que por cada número de items que tengamos lo va a agregar al a la no y qué es lo que está tomando está tomando en entre punto json.items, que es items, este es un array, tenemos el item 0, item 1, recuerde que en la array siempre empezamos por el 0, y quiero lo que necesitamos mafiar aquí lo que es el id video id que tenemos aquí este vídeo aquí está dentro de content details, por esos desfijanes p.content details, punto video id, porque lo que tenemos que sacar y también el video pub, está simplemente corremos y si se fijan tenemos un output de 50 items, ya que tenemos esto podemos hacerlo un loop para que corra uno por uno o podemos simplemente un tercorreto de golpe. Después de esto vamos a usar lo que es el no oficial de youtube y vamos a utilizar el que dice que es video. Gracias video. Gracias. y aquí nos va a pedir que creemos una crucial, vamos a darle que sí, nos vamos a ir de nuevo acá en este caso yo ya la tengo en el 8nout que ya hay muchos videos Como hacerlo, en la comunidad, entonces se pasa, no lo voy a hacer porque no quiero tener que cambiar mis secretos de mis IDs, entonces lo va a poner pausa, la warrina y continuamos. Ok, ya que pues yo me trae una idea y me secreto del, Mour particulier, struggles de rol, pero constad somewhere, pero no energaría más de momento, a través de todo es nuestro 찾 limitado, es unATORY. Bueno, sin embargo деревoren, os permitimos que dijamos que tendrías 1996 momento un poder ver, y vamos a escoger esta credencial que es lo que sigue, es un tipo de recursos video get, el video ahi, lo tomamos de acá y aquí, si el filz, básicamente, es que el filz que queremos traer de las tribus, porque si queremos traer todos y vamos a, esto va a correr 50 veces obviamente que tenemos 50 items con 50 outputs y se fijan que lo lo que nos trae, vamos a hacer esto más pequeño, nos trae el channel ID, el tib, y tú lo la descripción y inclusive nos trae la miniatura vamos a ver con eso ustedes pueden estrepiar, pueden hacer muchas cosas vamos a continuar la siguiente parte, después vamos a crear un código para obtener un array, por ¿Por qué? Porque si no lo vamos a la api, ya que estamos aquí. vamos a la pida aquí para poder traer el transcrib si te fijas aquí tenemos estos cochetes que quiere decir que es una rey nos pide que nos traegamos una rey para poder sacar todos los transcribis En este caso, aquí nosotros tenemos una cuestión que solo te acepta o no tenemos 25. 25 gratis, entonces para no infurrir ahorita no tiene ningún problema. voy a agregar aquí yo, le voy a ponerlo en el límite y mi límite va a ser de 25 y lo corro perfecto luego aquí voy a poner mi código y vamos a hacer una constante vamos a llamarle a re y va a ser el carrer desigual a items porque hay items, porque tenemos los items, los que queremos sacar, ¿verdad? para hacerle ítems.com Toma y y acá y ponte y es junto a ir y ponte como y vamos a ser el rey de vamos armando la rey Jason y vamos a poner el rey si es igual la rey Ok, ¿y qué me está regresando esto? Una rey con todos los AIDs cuántos 25 que pusimos un límite, que es justo lo que nos está pidiendo nuestra API de este lado, ok? Pasa genera un lo que estáis. y voy a ser toquiendo voy a revocar terminando y vamos a estar el siguiente nodo, ok, los siguientes sería que tengamos, dejamos una HTTP. Per request, es igual get, a cierta esposa, ¿cómo sabemos? Porque la documentación no lo está diciendo aquí, así que es un post, API, transcripts, Ok, entonces igual aquí tenemos un colo. que hace un cul por ejemplo les voy a enseñar si ustedes le dan copian esto y nos vamos en nuevo para el chene que lo podamos import curl lo pego y me va a confiarme va a rellenar todo ya el método la url los gds, el bod y todo lo que necesitamos, aquí nos pide nuestra token que acabamos de generar, pegamos open y se fijan aquí pues esto es manual porque estamos mandando solamente una idea. No quisamos mandar este arrais. Esta reida iris, perdón. Entonces, vamos a borrar esto, parece una frase de trabajarla, vamos a abrir una expresión, y la vamos a poner en JSON.StreamGify este es para poder convertir a ver formato que necesitamos de mandarlo en arrais abrimos paréntesis y antes se le quedes a iris, es igual a ¿Por qué? ¿Por qué es mi nodio inmediata anterior a Edith? Si no quisiera poner en el json.gd tendrás que poner algo como code n ya va a escribir Fíjate a escrito del cual 1, cierro, cierro para antes y punto items, punto item, punto item punto a edis, pero como es el nodo de media anterior lo puedo dejarse y eso es punto a edis y de aquí cerramos esto cerramos paréntesis se cerramos la expresión y ahorita lo voy a disparar y esto nos va a consumir por los veinticinco, aquí veis que está el gomal con el gayson, la verificar, gayson. punto de string G5, abro paréntesis, falto, eston, abro abro, hay D, 2 punto, 10 en punto hay D, 7, 8, 7, 8, 7, 8, 7, y antes de continuar voy a hacer una vez el table y voy a ver un record para poderlo guardar y vamos a antes que nada crear una tabla vamos a usar Obni, tu deseo necesito una tabla para guardar transcripts de videos de YouTube y la tabla así llame youtube trans tips y la base y llame scrapping latabla baja A tener cuatro tempos, el principal de este video, ahí, después, título, después, Transcript es un texto largo con formato en el que he sido por último un campo tipo agente que es, un resumen con el obni la verdad se ahorra en mucho tiempo y tan a ver lo que va a pasar va a estar creando todo esto va a creer la tabla nos va a quedar todo y se fijan aquí estoy viendo que fallo o no me entendió bien de si no he generado y ya vio que pase me está añadiendo datos de monstruos porque lo estoy creando desde ovni directamente como una app no le dije que me crearon una tabla ahí fue el rol mio vamos a pausar esto Vamos mejor para atrás, debo así que si quiero salir, voy a crear uno nuevo, vamos a ponerlo aquí Scraping. Y aquí si le puedes ir a hoy. Crea una tabla y amada en periódigitán con los siguientes campos. B.I.L.I.Y. Tintula transcript texterlarro en tweet. Hacía un campo agente para generar las líneas de la campora. Fue una creación. salente y vamos a esperar Esto, vamos a ir y me haré esta, vamos a verlo aquí en mi prego, un pedo digital, video ID, títulos, transcript, la gente fecha de creción, pero quiero que esta no sea fecha si no quiero que sea de este otro sentido, así que vamos a hacerle, creo que se nos Vamos, vamos, vamos, vamos, vamos. Y esto, va a ser liminar este de aquí, vamos a necesitarmos, nos volzamos en la chena y buscamos la base que estamos de crear se le echamos imperial digital, vamos a mapear y para mapear pues tenemos el correo verdad así que vamos a la hora y la verdad, vamos a correr nuestro secreto y nos llora Ah, Jason, vamos a tener este devalí Jason, ok, si, lo que nos estáis haciendo aquí, ah, es porque no tenia activa la expresión. Voy a dormirme, vamos a mejorarlo así. entonces obviamente aquí tenemos el título de la disrupción, tenemos categoría, tenemos aquí más la descripción del vídeo como tal, tenemos todo el transcript, lo tenemos en por si quiero descargar lo que tiene a un CRT con el timestamp y todo. Obviamente la forma en la que yo lo hice, ya no estamos ocupando este digera vídeo, es por si la parte quien saca a ustedes más información, pero si se fijan eso también está bastante completo, simplemente estoy sufriendo los dos para que van a dos formas lo te dedicar, pero fácilmente podrá quitar esto de aquí, quitar estos dos y funcionar. vamos a aprovechar que tenemos una descripción, así que vamos a agregarlo a nuestro ya me des, Vamos a crear campo, vamos a ver table, vamos a actualizar y ahora si vamos a mapear. vídeo edí vídeo edí y titulo, titulo, descripción, descripción, esto lo pongo en su tarp, transcripción, sería text, vamos a, Darle un retrayon fail y se falla que continúe manera regular y vamos a ejecutarlo. son 25 bitems que me diré que crear, vamos los mientras hayan nuestras tables Vamos a empezar a generar todo, 2234, y aquí se vuelva a medir a dos rars. Vamos a la última Están, Otra noche en el, Se fijan a más me generó 23, porque dos dieron error, pero como yo le puse con, continuo ahora por eso continuo, entonces vamos a eliminar este y vamos a dejarlo así en 23 ahora este es un campo que lo pongo a utilizar directamente para no tener que usar en algún un módulo o el módulo. Como algo un nodo de AI en H&N, simplemente le da en clica aquí, le pueden decir todas las elas en la vista y eso nos va a generar un resumen, en el caso no de esto, de el transcript completo, ya con esto ustedes pueden ver. Siga, pueden conectar, inclusive, un chat GPT, un GPT que ustedes creen, lo pueden conectar con un open a Steam a AirTable y preguntar la cerca de los videos o de cualquier de la información y listo de profundidad vasto. bastante corto, útil y algo sencilla para que pueda empezar con sus primeros proyectos en el hn y les voy a dejar todos los recursos incluido el, Daniel Jason en la comunidad.
