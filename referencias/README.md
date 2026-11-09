# Referencias: material base del BSA 2.0

Esta carpeta guarda el material original que se usó para redactar el sitio de
documentación del **Blue Spot Analysis 2.0 (BSA 2.0)** del BID. Antes estaba en la
carpeta `fuentes/` del repositorio `bsa-docs`. No forma parte del sitio publicado. Se
conserva como referencia y para la trazabilidad de la documentación.

> **Aviso:** el material de esta carpeta es de uso interno del proyecto. Antes de
> hacer público el repositorio, el equipo del BID debe confirmar qué documentos
> pueden publicarse.

## Contenido

| Carpeta | Archivo | Qué es | Alimenta principalmente |
|---|---|---|---|
| `01_metodologia/` | `BSA 2.0 Concept Report.md` | Informe conceptual preliminar (V0.1, jul. 2025). **Solo las líneas 1–1027 son texto. De la 1028 en adelante son imágenes en base64.** | Secciones **Metodología** y **Glosario** |
| `02_presentaciones/` | `Ppt_BSA_Ejecutiva_15042026_v3_ENG.pdf` | Deck ejecutivo corto (10 láminas, en inglés). | **Inicio**, visión general |
| `02_presentaciones/` | `Presentación_BSA2_23022026_V3.pdf` | Deck extenso orientado a usuarios (17 láminas, en español). | **Primeros pasos**, **Guía de Usuario**, **Dashboard** |
| `03_datos_entrada/` | `IDB_InputData_BSA_V1_25022026 1.xlsx` | Ficha de datos de entrada: 22 hojas con las capas obligatorias y opcionales, sus atributos y formatos. | **Guía de Usuario → Datos de entrada** |
| `_guia/` | `Document_Guide.txt` | Guía original sobre qué hacer con cada documento. | Referencia de trabajo |
| `_guia/` | `Proposed Documentation Structure.txt` | Estructura inicial propuesta para el sitio. | Referencia de trabajo |
| `_guia/` | `Mapa_Actores_BSA2.md` | Equipo completo del proyecto (mapa de actores). | **Inicio → Créditos** |
| `_guia/` | `License_Snippet_README.md` | Fragmento de la licencia anterior del BID (AM-331-A3) que iba en el README. | Histórico, ya reemplazado (ver `LICENSE.md`) |

## Dónde quedó el resto del material

En la carpeta original `fuentes/04_codigo/` estaban el código y el caso de Costa Rica.
Ahora están en otras carpetas:

- `toolbox/BSA2.py` y `toolbox/BSA2.atbx`: el motor de cálculo y el toolbox de ArcGIS Pro.
  `BSA2.py` incluye el historial de versiones del repositorio `keom0891/BSA2`.
- `ejemplos/costa-rica/`: el proyecto `CostaRica.aprx`, las bases de datos de
  vulnerabilidad (`FVU_BSA_V3.csv`) y de costos de operación (`OCO_BSA_CR_V1.csv`), un
  registro de corrida (`Loc/*.loc`) y el paquete `BSA2_CostaRica.zip`, que contiene la
  geodatabase `BSA2.gdb` con los datos y resultados del caso.

Las 18 figuras del Concept Report se extraen con `scripts/extract_images.py` a
`docs/assets/metodologia/`.
