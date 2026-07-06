# Equipo de Marketing — sistema multi-cliente

Sistema automático de creación de contenido y marketing para los clientes de la
consultora Cerebro. **Diseño completo y fuentes:**
[`cerebro-agentico/02-SISTEMA-CONTENIDO-MARKETING.md`](../cerebro-agentico/02-SISTEMA-CONTENIDO-MARKETING.md).

## Estructura
- `clientes/_plantilla/` — expediente modelo. Para dar de alta un cliente:
  copiar la carpeta con su nombre y correr el onboarding (§3 del diseño).
- `clientes/<nombre>/` — un expediente por cliente: sus datos, su voz, su
  calendario, sus guiones aprobados. **El motor es compartido; los datos viven
  aquí.**

## Motor compartido (no duplicar por cliente)
- Pipeline de guiones: `.claude/skills/cerebro-guiones/` (parametrizada por cliente).
- Estilos de B-roll y escenarios: `cerebro/maquina-contenido/`.
- Prompts del curso: `docs-skool/imperio/17-biblioteca-de-prompts/`.
- Método CCC y flujo de producción: ver diseño (§1).

## Regla de oro (del Gran Consejo)
El resultado de toda tarea queda registrado en el expediente del cliente
(bitácora + archivos). Si no está registrado, no está terminado.
