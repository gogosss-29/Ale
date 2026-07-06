# 🎬 B-Rolls Cerebro — Estaciones 6-7

> Porta el método documentado por Alexander ("Sistema Creador de B-Rolls"). El
> avatar narra el 100%; los B-rolls se montan en edición encima (~50% del
> timeline). Genera **prompts para Google Flow**, no edita.

## Flujo de trabajo (cuando llega un guion / lista de B-rolls)
1. **Lectura completa** del guion: tema central, arco, hook→desarrollo→punch→cierre.
2. **Identificar momentos cubribles** (NO todos): frases con metáfora visual
   fuerte, conceptos abstractos que aclara una imagen, enumeraciones,
   transiciones, hooks que necesitan retención.
   - **3 a 5 B-rolls** por video de 60-90s (excepcionalmente 6+ si es muy denso).
   - **Nunca cubrir todos los bloques:** el video respira con la cámara del avatar.
3. **Asignar estilo** a cada momento (de la Biblioteca). Se pueden mezclar, sin
   pasar de 3 estilos por video (coherencia).
4. **Proponer 2-4 conceptos visuales** al usuario por cada momento y recomendar
   una favorita con fundamento. **NO armar el prompt antes de que elija.**
5. **Armar el prompt** con la Plantilla Maestra de 8 bloques (1.800-3.000 chars).
6. **Documentar** el resultado (qué funcionó / qué ajustar) para futuros prompts.

## Plantilla Maestra — 8 bloques (orden fijo, no se omite ninguno)
```
[STYLE]: formato 9:16 + 24fps + duración (4/6/8s) + referencia estética clara.
[BACKGROUND]: fondo con código hex + textura + viñeta.
[MAIN ELEMENT]: lo más largo; describe TODO el frame posición por posición.
   Usar subdivisiones cuando hay varios elementos:
   UPPER-LEFT / LOWER-RIGHT / CONNECTING THEM / DECORATIVE.
   Cada elemento: forma, textura, color, tamaño relativo, cómo se conecta al fondo.
[ANIMATION]: movimientos en orden cronológico. Cerrar SIEMPRE con
   "Camera completely static" (excepto Estilo #08, que pide movimiento).
[TEXT ON SCREEN]: si no hay → "NONE. No letters, no numbers, no words anywhere."
[COLOR PALETTE]: lista cerrada de hex (evita que Flow invente colores).
[MOOD]: 1-2 frases con la emoción/tono.
[AUDIO]: Parte 1 "NO voice, NO narration, NO speech of any kind." +
   Parte 2 sound design analógico específico, alineado a los elementos.
[NEGATIVE]: lista consolidada de lo que NO debe aparecer (ver abajo).
```
Target: **1.800-3.000 caracteres** (límite duro de Flow 4.000; prompts comprimidos rinden mejor).

## Biblioteca de estilos (8 validados)
| ID | Nombre | Universo visual | Cuándo usarlo |
|----|--------|-----------------|---------------|
| #01 | Editorial Bodegón | Cenital monocromo de objetos físicos | objetos cenitales, dispersión editorial |
| #02 | Collage Vintage Editorial | recortes B&N + doodles a mano | storytelling con personas/escenas reales |
| #05 | Collage Anatómico Surrealista | esculturas/anatomía B&N + acento rojo | metáforas conceptuales |
| #06 | Educativo Vintage Color | ilustración color vintage construyéndose | storytelling didáctico, histórico |
| #07 | 3D Render Hero Object | objeto 3D fotográfico sobre fondo plano | publicidad premium, hooks de impacto |
| #08 | Beast Motion Graphics Tutorial | tipografía gigante + foto B&N + cámara movida | reels virales, estilo dominante |
| #09 | Vector Neón Minimalista | motion graphics 2D vectorial, neón sobre negro | datos/finanzas tech, pasos/objetivos |
| #10 | Editorial Premium Mixed-Media | grilla + props reales + 3D + tipografía cinética | hooks de impacto, intros, transiciones |
| **#11** | **Premium Motion Graphics (Data-Viz)** | **grid claro + glass/3D + texto kinético + cámara** | **B-rolls INFORMATIVOS: KPIs, charts, comparativas, alertas, números** → ver `estilo-premium-dataviz.md` |
| **#12** | **Dark Tech Reveal** | **void azul-noche + pantallas glass glow cian + texto fino futurista** | **mostrar plataforma/app/dashboard/herramienta** (fit Invertí Sin Vueltas) → ver `estilo-12-dark-tech-reveal.md` |
| **#13** | **Kinetic Typography Punch** | **fondo sólido que flipea (negro/crema) + texto bold + keyword en rojo** | **hooks, frases citeables, punchlines, intros de lista** (puro texto) → ver `estilo-13-kinetic-typography.md` |
| **#99** | **🧠✨ Cerebro Signature (INSIGNIA)** | **grafito + oro fundido + line-art que se dibuja · caos→orden · glifo Cerebro** | **estilo propio de marca:** hooks/cierres de alto impacto, firma. Original, premium → ver `estilo-99-cerebro-signature.md` |
> #11 es la EXCEPCIÓN a "sin texto": acá el dato/número ES el contenido. Para datos/finanzas, **usar #11**; para metáfora/concepto, #05/#06.
> #03 y #04 descartados (no alinean con marca); los IDs se conservan por trazabilidad, no reasignar.
> Para datos/prueba priorizar B-roll **informativo** (#06, #09); para impacto/metáfora, **generativo**.

## Banco de Metáforas Visuales (concepto → metáfora → estilo)
Cuando un concepto del guion aparezca, buscar primero acá una dirección probada:
- **Ganar vs facturar** → persona celebrando arriba / angustiada abajo · #02
- **CAC** → balanza: figura humana vs monedas · #05
- **Costo oculto** → iceberg (visible/hundido) · #05
- **Margen / Punto de equilibrio / Flujo de caja / Rentabilidad** → fórmula que se construye / dos líneas que se cruzan / río-tubería / gráfica ascendente · #06
- **Trabajar a ciegas** → escultura clásica con venda · #05
- **Datos dispersos** → cenital de escritorio con planillas/post-its · #01
- **Datos centralizados / Tablero de control** → dashboard con datos convergiendo / 4 medidores · #06
- **Automatización** → varios objetos manuales reemplazados por un dispositivo · #05/#07
- **Estructura / Profesionalización** → edificio clásico, columnas / caos→orden · #05/#06
- **Crecimiento** → flecha ascendente, planta, gráfico subiendo · #06
- **Diagnóstico / Auditoría** → estetoscopio sobre edificio / lupa + documentos · #05
- **Cómo respira el negocio** → escultura clásica exhalando vapor hacia fábrica · #05
- **Atraer clientes / Embudo / Branding** → imán con gente / embudo clásico / mano sosteniendo la "marca" · #07,#06,#07
> Si no hay match: inventar una metáfora **universal, concreta y compatible** con
> un estilo. Si funciona y gusta, agregarla al banco.

## Reglas inmutables (no se rompen NUNCA)
1. **Sin voz humana** en el audio: bloques AUDIO y NEGATIVE siempre niegan
   voz/narración (Flow mete locución al ver texto o narrativa).
2. **Sin texto en pantalla** cuando se puede evitar (se agrega en edición: control
   tipográfico, sin deformar tildes, sin locución no deseada). Excepción: #08 o si
   el usuario lo pide.
   **⭐ Actualización (Ale, 2026-07-06): en OMNI el texto en pantalla SÍ sale
   bien** — si el b-roll se genera en Omni, el texto puede ir en el render.
   La regla "sin texto" aplica a Veo por API (comprobado: lo deforma) y a
   Flow/Veo cuando no se usa Omni.
3. **Duración 6s** por defecto (4s inserts rápidos; 8s solo si la idea respira).
4. **Vertical 9:16, 24fps** siempre.
5. **1.800-3.000 caracteres** por prompt.

## NEGATIVE base (adaptar acentos de color por estilo)
```
No humans, no live-action, no full-color photos, no neon, no glow, no sci-fi,
no digital particles, no flat vector design, no bright colors except [acentos],
no shaky camera, no readable text, no logos, no voiceover, no narration,
no narrator, no spoken language, no human speech, no talking, no vocals,
no singing, no lyrics, no commentary, no whispers, no breathing, no synthesizers.
```

## Variación dentro del mismo estilo (anti-repetición)
Si hay varios B-rolls del mismo estilo, cambiar **al menos 3 de 5**: composición ·
cantidad de elementos · tipo de conector · naturaleza de los elementos ·
movimiento clave. Fijo (la firma del estilo): paleta, textura del fondo,
tipografía de doodles, tipo de cutouts.

## Anti-patrones
Proponer todos los estilos en vez de 2-4 curados · armar el prompt sin proponer
concepto antes · cualquier voz/narración · mezclar +3 estilos · copiar tal cual
una referencia de Pinterest · prompts genéricos sin metáfora concreta · olvidar
el bloque NEGATIVE. **Metáforas a evitar:** cerebros con circuitos sci-fi,
empresarios trajeados de stock, manos saliendo del teléfono, engranajes
metálicos, bombillitas de idea, flechas verde neón de trading, gente con
auriculares en oficinas modernas.
