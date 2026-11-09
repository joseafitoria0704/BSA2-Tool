# Registro de cambios

Todos los cambios relevantes del BSA 2.0 se documentan en este archivo. El formato
sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y las versiones siguen
[Versionado Semántico](https://semver.org/lang/es/).

La historia anterior a la consolidación se reconstruyó a partir de los repositorios de
origen: [keom0891/BSA2](https://github.com/keom0891/BSA2) (motor de cálculo) y
[andresabarca-atlas/bsa-docs](https://github.com/andresabarca-atlas/bsa-docs)
(documentación). Sus commits se conservan en el historial de este repositorio.

## [Sin publicar]

### Añadido
- Plantillas de *issue* y de *pull request* (`.github/`) y workflow de OpenSSF Scorecard,
  según `EL-BID/Plantilla-de-repositorio`.
- `README-EN.md`, versión en inglés del README.
- README ampliado con los archivos de entrada, las capas y campos de salida y la
  descripción de las funciones del motor.
- Trazabilidad "fuente → sección del sitio" en `referencias/README.md`.

### Cambiado
- `requirements-docs.txt` declara versiones mínimas.
- La página *Interfaz de la herramienta* aclara que el diálogo muestra todos los
  parámetros como opcionales y que la obligatoriedad la valida `BSA2.py` al ejecutarse.
- El README y la página *Caso de ejemplo* advierten que los rásters de amenaza del caso de
  Costa Rica no están incluidos.

## [0.3.0] - 2026-11-08 — Repositorio conjunto

Se consolidan el motor de cálculo y la documentación en el repositorio `BSA2-Tool`.

### Añadido
- Licencia de Software de Código Abierto del BID (diciembre de 2025) en `LICENSE.md`,
  `CONTRIBUTING.md`, `CODE-OF-CONDUCT.md`, configuración de SonarQube, CI del sitio de
  documentación y `.devcontainer`.
- README según la plantilla de documentación del BID.

### Cambiado
- Estructura: `toolbox/` (motor y toolbox), `ejemplos/costa-rica/` (caso de referencia) y
  `referencias/` (material base, antes `fuentes/`).
- La licencia anterior AM-331-A3 se conserva en `licenses/legacy/`.

### Eliminado
- Configuración local de los autores (`CLAUDE.md`, `.claude/`) y la copia duplicada de
  `BSA2.py`.

## Motor de cálculo (`keom0891/BSA2`)

### v0.3 - 2026-03-02
- Versión marcada como `Base_code_v0.3`. No modifica el código respecto de v0.2; es la
  versión distribuida en el caso de Costa Rica (`ejemplos/costa-rica/`).

### v0.2 - 2026-02-17
- **Cambio climático**: nuevo parámetro 9 (`mod_tp_poly`), un polígono con los periodos
  de retorno modificados por escenario. Nuevas funciones `parse_tp_fields`, `apply_TRmods`
  y `compute_mod_totals`, y nuevos campos `DAE_*_mod_{scen}`, `PAE_*_mod_{scen}` y
  `Priority_mod_{scen}`.
- El toolbox `BSA2.atbx` pasa a 14 parámetros de entrada y 4 capas de salida derivadas.
- Reorganización y documentación interna de las funciones.

### v0.1.1 - 2025-12-19
- PAE para los componentes (puentes, túneles y drenajes): la pérdida diaria por
  interrupción (DLT) del tramo se asigna a cada componente mediante `ID_TRAMO`
  (`tramo_dlt_from_roads`, `map_component_dlt_by_tramo`).

### v0.1 - 2025-12-17
- Versión inicial del motor: muestreo de rásters de amenaza sobre la red vial y sus
  componentes, funciones de vulnerabilidad (RMD), DAE por amenaza, análisis de rutas
  alternas con Dijkstra para la PAE de tramos e índice `Priority`.

## Documentación (`andresabarca-atlas/bsa-docs`)

### 2026-09-09
- Se integró y luego se revirtió una actualización integral de la documentación (PR #1:
  55 archivos, nueva página de priorización y 23 imágenes; PR #2: revert). Sus commits
  (`0273add`, `0a9bd16`) se conservan en el historial y se identifican con los tags
  `archivo/actualizacion-documentacion-2026` y `archivo/revert-actualizacion-documentacion-2026`.

### 2026-07-09
- Traducción completa al inglés (`*.en.md`) con `mkdocs-static-i18n`.

### 2026-05-22 / 2026-05-25
- Primera versión del sitio en español: Metodología, Primeros pasos, Guía de Usuario,
  Dashboard, Recursos, Glosario y Licencia, con 18 figuras extraídas del Concept Report.
  Se publicó en GitHub Pages.

[Sin publicar]: https://github.com/joseafitoria0704/BSA2-Tool/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/joseafitoria0704/BSA2-Tool/releases/tag/v0.3.0
