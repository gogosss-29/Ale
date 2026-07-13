# B-roll — Estilo "Gráfico / Motion" (data-viz fintech)

> Estilo reutilizable para B-rolls de contenido financiero/inversión generados con
> **Omni Flash** (APImart). Pensado para ir **por encima de la voz** (UGC voz-off),
> sincronizado con los timestamps de palabra del video.
>
> ⚠️ **Regla de oro:** los modelos de video IA NO escriben texto/números legibles.
> Estos prompts generan **fondos animados abstractos** (barras, líneas, partículas,
> paneles) SIN texto. Los tickers, porcentajes y montos reales (`TLSMO`, `9%`,
> `$2.000`, `EWZ`, `Visa`, `Vista`) se **encima en edición** como overlays.

## Bloque de estilo (se antepone a cada prompt)

```
STYLE: Clean modern motion-graphics, animated financial data visualization.
Dark navy background with a subtle glowing grid. Smooth animated bar charts and
line graphs, floating 3D glass UI panels, teal and amber accent glow, particle
data streams, shallow depth of field with soft bokeh, premium minimal fintech
aesthetic, soft ambient lighting, cinematic, ultra-detailed, smooth 30fps motion,
9:16 vertical.
```

## Negative prompt (para gráficos)

```
legible text, readable numbers, letters, words, logos, watermark, gibberish text,
distorted typography, flicker, warping, low quality, jpeg artifacts, cluttered,
cartoonish, oversaturated
```

## Paleta para los overlays de texto (encima, en edición)

- Fondo/base: navy `#0B1220`
- Acento positivo (sube): teal `#2DD4BF`
- Acento alerta/caída: amber `#F59E0B`
- Texto: blanco `#F8FAFC` / gris `#94A3B8`

---

# Mapa de beats — Video "Cartera $5.000" (53s)

Cada B-roll es un clip de 8s (Omni Flash), colocado al inicio del beat.
`prompt` = STYLE + escena. Duración objetivo 8s, 9:16.

| # | Tiempo | Concepto | Overlay a encimar (texto real) |
|---|--------|----------|-------------------------------|
| B1 | 0.0–3.7 | Hook: cartera se arma | `$5.000` · "Cartera moderada" · 3 slices |
| B2 | 3.7–12.3 | Bono / renta fija estable | `TLSMO` · `9% anual USD` · $10M ARS |
| B3 | 12.3–19.4 | Volatilidad / riesgo | "Mediano plazo" · dial de riesgo |
| B4 | 19.4–26.2 | ETF Brasil | `EWZ` · `$2.000` · 🇧🇷 |
| B5 | 26.2–35.8 | Visa: red global, márgenes | `VISA` · `$2.000` · "margen alto / poca deuda" |
| B6 | 36.2–44.5 | Petróleo cae → entrada Vista | `VISTA` · `$1.000` · petróleo ▼ |
| B7 | 44.8–53.2 | Dashboard + seguimiento + CTA | 3 posiciones · "seguimiento 6 meses" · CTA |

## Prompts (uno por B-roll)

**B1 — Hook / armado de cartera (0.0–3.7)**
```
STYLE. A single glowing donut/allocation chart assembling itself from three
animated segments that slide into place, coins stacking in the background,
upward momentum, sense of a portfolio being built. No text.
```

**B2 — Bono estable / renta fija (3.7–12.3)**
```
STYLE. A steady, calm horizontal line chart with a gentle upward slope
representing stable fixed-income yield, soft pulsing dots along the line,
a floating glass panel with abstract bar rows, reassuring and stable mood.
No text.
```

**B3 — Volatilidad / riesgo mediano plazo (12.3–19.4)**
```
STYLE. A line chart whose amplitude gradually increases into larger waves,
a semicircular risk gauge needle moving from low toward medium, subtle
turbulence in the particle streams, tension building. No text.
```

**B4 — ETF EWZ / Brasil (19.4–26.2)**
```
STYLE. A stylized 3D map of Brazil glowing on the grid, a rising bar chart of
several large company blocks emerging from it, green-teal upward arrows, a
basket icon aggregating multiple bars into one, national scale. No text.
```

**B5 — Visa / red global y márgenes (26.2–35.8)**
```
STYLE. A glowing 3D globe wrapped in a dense network of connecting payment
lines and pulsing nodes across continents, a tall profit-margin bar rising
high next to a very short debt bar, contactless-payment ripple motion,
dominant global network. No text.
```

**B6 — Caída del petróleo / entrada Vista (36.2–44.5)**
```
STYLE. A sharp descending line chart (oil price falling steeply), an amber
warning glow at the drop, then a single marker lighting up at the bottom of
the dip signaling an entry opportunity, oil-barrel silhouettes as abstract
3D shapes, contrarian buy moment. No text.
```

**B7 — Dashboard final / seguimiento + CTA (44.8–53.2)**
```
STYLE. A clean portfolio dashboard with three glowing position panels side by
side, a 6-month timeline bar filling up, a subtle question-mark pulse inviting
engagement, confident and resolved mood. No text.
```

---

## Cómo generar (cuando esté la API key)

```bash
# 1) cargar credenciales
export APIMART_API_KEY="..."        # (o en avatarhype/.env)

# 2) generar los 7 B-rolls (8s, 9:16, omni-flash) — ver script de generación
#    avatarhype usa engines/apimart.py -> ApimartVideo(modelo="omni-flash")
```

> ⚠️ Antes de generar hay que **verificar los endpoints reales de APImart**
> (`SUBMIT_PATH`/`STATUS_PATH` en `avatarhype/engines/apimart.py` están marcados
> como "a confirmar"). Sin eso, la llamada fallará aunque la key sea válida.

## Montaje

1. Generar los 7 clips → `salida/broll/B1..B7.mp4`.
2. Encimar cada uno sobre el video de la voz en su timestamp (`B#` → tiempo del beat).
3. Añadir los overlays de texto real (columna "Overlay") con la paleta de arriba.
4. Mantener el audio del avatar; el B-roll es solo imagen.
