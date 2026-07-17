# Invertí Sin Vueltas — sitio web (invertisinvueltas.com.ar)

Landing estática + `.htaccess` de Apache. Pixel de Meta: `1452374586665261`
(dataset "Invertí sin vueltas", ID 1665959001369348).

## Qué cambió (jul 2026) — tracking Meta Pixel + Calendly

Antes los botones "Agendar llamada" abrían Calendly en **otra pestaña
(calendly.com)**, por lo que los pasos del funnel dentro de Calendly
(seleccionar día, confirmar la llamada) ocurrían fuera de nuestro dominio y el
pixel de la web no podía medirlos; dependíamos 100% de la integración nativa
Calendly → Meta Pixel.

Ahora Calendly se abre como **popup embebido en la misma página** (widget
oficial de Calendly) y la web escucha los eventos `postMessage` del iframe para
disparar el pixel propio:

| Paso | Evento que dispara el pixel |
|---|---|
| Cargar la página | `PageView` (estándar) |
| Click en cualquier botón "Agendar" | `Lead` (estándar) |
| Calendly: elegir día y horario | `CalendlySeleccionarDia` (personalizado) |
| Calendly: llamada confirmada | `Schedule` (estándar) |
| Click en WhatsApp | `Contact` (estándar) |
| Play en videos | `ViewContent` (estándar) |

Si el widget de Calendly no llega a cargar, el link hace fallback al
comportamiento anterior (nueva pestaña).

Ventajas: los eventos se disparan desde invertisinvueltas.com.ar con nuestro
pixel (aparecen en "Probar eventos"), no dependen del plan ni del banner de
cookies de Calendly, y conservan la atribución (`fbclid`/UTM se siguen pasando
en la URL de Calendly).

## Deploy

Subir `index.html` y `.htaccess` a la raíz del hosting (reemplazar los
existentes).

## Verificación después de deployar

1. Meta Events Manager → dataset → **Probar eventos** → abrir la web.
2. Click en "Agendá tu llamada" → debe registrarse `Lead` y abrirse el popup.
3. Elegir día y horario → debe registrarse `CalendlySeleccionarDia`.
4. Confirmar con datos de prueba → debe registrarse `Schedule`.

## Recordatorios al cambiar de cuenta publicitaria / pixel

- Las **conversiones personalizadas** viven en cada cuenta publicitaria: las de
  la cuenta vieja no se migran solas. Recrearlas en la cuenta nueva apuntando a
  los eventos de esta tabla (o usar directamente `Schedule` como evento de
  conversión de las campañas, que ya es estándar).
- Si se vuelve a cambiar el pixel: actualizar el ID en los DOS lugares de
  `index.html` (script `fbq('init', ...)` y el `<noscript>`).
- La integración nativa de Calendly (Configuración → Integraciones → Meta
  Pixel) puede quedar activa como refuerzo, pero ya no es necesaria para medir
  el funnel.
