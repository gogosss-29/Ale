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
