# skool/ — Extractor autenticado de comunidades Skool

Guarda **todo** el classroom de una comunidad de Skool de la que eres miembro:
estructura (cursos→módulos→lecciones), notas escritas de cada lección y
transcripciones de los vídeos. Reusa **tu** sesión (cookie); no elude ningún pago.

> Lee primero `docs-skool/METODO-ACCESO-SKOOL.md` para el cómo y los avisos legales.

## Instalación
```bash
pip install -r ../requirements.txt   # requests
pip install yt-dlp                    # para las transcripciones (Fase 2)
```

## Configuración (tu cookie, nunca se commitea)
```bash
# opción A: variable de entorno
export SKOOL_COOKIE='auth_token=...; client_id=...; i18next=es-419'
# opción B: fichero local (fuera del repo)
export SKOOL_COOKIE_FILE=/tmp/skool_cookie.txt
```
Obtener la cookie: navegador logueado → F12 → Network → recargar → clic en la
petición a `www.skool.com` → Request Headers → copiar el valor de `cookie:`.

## Uso
```bash
# Verificar sesión
python skool/session.py

# Fase 1 — estructura + notas + links de vídeo  → docs-skool/<community>/
python -m skool.extract imperio --out docs-skool

# Fase 2 — transcripciones de los vídeos (anexadas a cada .md)
python -m skool.transcripts imperio --out docs-skool          # todas
python -m skool.transcripts imperio --out docs-skool --limit 5 # prueba
```

## Qué genera
```
docs-skool/<community>/
  INDICE.md          índice navegable de todos los cursos y lecciones
  estructura.json    árbol completo legible por máquina (ids, títulos, vídeos)
  videos.jsonl       1 línea por vídeo (curso, lección, url, duración) — input Fase 2
  NN-<curso>/
    NNN-<leccion>.md título + link de vídeo + recursos + notas + transcripción
```

## Módulos
| Fichero | Rol |
|---|---|
| `session.py` | sesión HTTP autenticada con la cookie (reintentos, pausas) |
| `api.py` | cliente de los endpoints `_next/data` de Skool (cursos, árbol, lección) |
| `prosemirror.py` | convierte las notas (`desc` Prosemirror JSON) a Markdown |
| `extract.py` | Fase 1: recorre cursos y vuelca todo a Markdown |
| `transcripts.py` | Fase 2: baja subtítulos de YouTube/Loom y los anexa |

## Notas
- **Resumible:** Fase 2 salta las lecciones que ya tienen transcripción.
- **Reutilizable:** sirve para cualquier comunidad de Skool, cambiando el slug y la
  cookie (siempre que seas miembro con acceso).
- El entorno de red usaba un CA propio → yt-dlp se invoca con `--no-check-certificates`.
