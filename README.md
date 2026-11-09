*Esta herramienta digital forma parte del catálogo de herramientas del **Banco Interamericano de Desarrollo**. Puedes conocer más sobre la iniciativa del BID en [https://knowledge.iadb.org/es/codigo-para-el-desarrollo](https://knowledge.iadb.org/es/codigo-para-el-desarrollo)*

<p align="center"><img src="docs/assets/logo-bid.png" alt="Banco Interamericano de Desarrollo" height="80"/></p>

<h1 align="center">Blue Spot Analysis 2.0 (BSA 2.0)</h1>

<p align="center"><b>Priorización de inversiones en infraestructura de transporte a partir del riesgo ante amenazas naturales</b></p>

<p align="center"><img src="docs/assets/metodologia/image16.png" alt="Mapa de priorización de tramos viales del BSA en República Dominicana" width="640"/><br/><sub>Ejemplo de resultado: nivel de priorización de tramos viales a escala provincial (República Dominicana). Fuente: BSA 2.0 Concept Report.</sub></p>

![version](https://img.shields.io/badge/version-0.3.0-blue)
![ArcGIS Pro](https://img.shields.io/badge/ArcGIS%20Pro-3.2%2B-2C7AC3)
![python](https://img.shields.io/badge/python-arcgispro--py3-3776AB)
![docs](https://img.shields.io/badge/docs-MkDocs%20Material-526CFE)
![license](https://img.shields.io/badge/license-IDB%20Open%20Source-lightgrey)
<!-- Badge de SonarQube Cloud (solicitado por Código para el Desarrollo); se activa al configurar el proyecto en EL-BID:
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=EL-BID_BSA2-Tool&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=EL-BID_BSA2-Tool)
-->

**Español** | [English](README-EN.md)

<p align="center"><a href="https://joseafitoria0704.github.io/BSA2-Tool/"><img src="https://img.shields.io/badge/Documentaci%C3%B3n%20en%20l%C3%ADnea-Abrir%20el%20sitio-0B5394?style=for-the-badge" alt="Abrir la documentación en línea"/></a></p>

> 📘 **Documentación completa en línea:** [https://joseafitoria0704.github.io/BSA2-Tool/](https://joseafitoria0704.github.io/BSA2-Tool/) — metodología, instalación, guía de usuario, dashboard y glosario.

---

## Tabla de contenidos

- [Descripción y contexto](#descripción-y-contexto)
- [Guía de usuario](#guía-de-usuario)
- [Guía de instalación](#guía-de-instalación)
- [Archivos de entrada y de salida](#archivos-de-entrada-y-de-salida)
- [Descripción del motor de cálculo](#descripción-del-motor-de-cálculo)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Documentación completa](#documentación-completa)
- [Cómo contribuir](#cómo-contribuir)
- [Código de conducta](#código-de-conducta)
- [Autores](#autores)
- [Información adicional](#información-adicional)
- [Licencia](#licencia)
- [Limitación de responsabilidades](#limitación-de-responsabilidades)

---

# Descripción y contexto

El **Blue Spot Analysis 2.0 (BSA 2.0)** es una metodología, una herramienta de escritorio y un dashboard de resultados desarrollados por el **Banco Interamericano de Desarrollo (BID)**. Sirven para **priorizar inversiones en infraestructura de transporte** a partir de un análisis simplificado del riesgo ante amenazas naturales, a escala nacional o regional.

El análisis combina cuatro componentes:

| Módulo | Qué representa |
| --- | --- |
| **Amenaza** | Intensidad de los eventos naturales para varios periodos de retorno: inundación fluvial, inundación pluvial/costera, sismo, tsunami y licuefacción, con modificadores opcionales por cambio climático |
| **Exposición** | Red vial y sus componentes (tramos, puentes, túneles y drenajes), con costos de reposición y tránsito |
| **Vulnerabilidad** | Funciones de vulnerabilidad (relación media de daño) por taxonomía de activo y tipo de amenaza |
| **Criticidad** | Importancia funcional de cada tramo, que se estima con rutas alternas (algoritmo de Dijkstra) y costos de operación vehicular |

Con ellos la herramienta estima, para cada activo:

- **DAE**, Daño Anual Esperado (*EAD*): daño físico directo a la infraestructura.
- **PAE**, Pérdida Anual Esperada (*EAL*): pérdida económica por la interrupción del tránsito.
- **PML**, Pérdida Máxima Probable, asociada a un evento de diseño.
- Un **índice de priorización** de activos.

Los resultados alimentan mapas de daños y de pérdidas, curvas de excedencia y rankings de priorización, y se publican en un dashboard en línea para los tomadores de decisión.

El BSA 2.0 ya se aplicó en **República Dominicana** (caso de referencia), **Costa Rica** y **El Salvador**. La herramienta es fruto del trabajo conjunto de las divisiones de **Transporte (TSP)**, **Gestión de Riesgo de Desastres (DRM)** y **Cambio Climático (CCS)** del BID.

Este repositorio reúne en un solo lugar:

1. el **motor de cálculo** (`toolbox/BSA2.py`) y el toolbox de ArcGIS Pro (`toolbox/BSA2.atbx`);
2. el **caso de referencia de Costa Rica** (`ejemplos/costa-rica/`);
3. el **sitio de documentación** bilingüe, en español e inglés (`docs/`, MkDocs + Material), publicado en **[https://joseafitoria0704.github.io/BSA2-Tool/](https://joseafitoria0704.github.io/BSA2-Tool/)**.

---

# Guía de usuario

El BSA 2.0 se usa por completo desde la interfaz gráfica de ArcGIS Pro, sin programar. El flujo de trabajo tiene seis etapas:

1. **Recopilar y estandarizar los datos**: capas de exposición, rásters de amenaza por periodo de retorno y bases de vulnerabilidad y de costos (ver [Datos de entrada](https://joseafitoria0704.github.io/BSA2-Tool/guia-usuario/datos-entrada/) en el sitio de documentación).
2. **Preparar las capas de exposición** con sus atributos requeridos (`ID_TRAMO`, `vul_f`, `vul_eq`, `rep_cost_k`, TPDA `T9`–`T15`, etc.).
3. **Calcular el PIB per cápita por día** del país.
4. **Definir la longitud de segmento** de la red vial (por ejemplo, 30 m en el caso de Costa Rica).
5. **Ejecutar el toolbox BSA2** en ArcGIS Pro, con sus 14 parámetros:

    | # | Parámetro | Descripción |
    | --- | --- | --- |
    | 0 | `roads_path` | Red vial (obligatorio) |
    | 1–3 | `bridge_path`, `tunnel_path`, `draina_path` | Puentes, túneles y drenajes (opcionales) |
    | 4–8 | `fl_rive_raw`, `fl_coas_raw`, `ts_coas_raw`, `earthqu_raw`, `liquefa_raw` | Rásters de amenaza: inundación fluvial, pluvial/costera, tsunami, sismo y licuefacción |
    | 9 | `mod_tp_poly` | Polígono de modificadores por cambio climático (opcional) |
    | 10 | `vulner_data` | Base de funciones de vulnerabilidad, por ejemplo `FVU_BSA_V3.csv` (obligatorio) |
    | 11 | `operat_data` | Base de costos de operación vehicular, por ejemplo `OCO_BSA_CR_V1.csv` (opcional) |
    | 12 | `gdppca_doub` | PIB per cápita por día (opcional) |
    | 13 | `road_segme` | Longitud de segmento en metros (obligatorio) |

6. **Revisar los resultados y cargarlos al dashboard.** La herramienta crea en `BSA2.gdb`, junto al script, las capas `roads_results_<fecha>`, `bridges_results_<fecha>`, `tunnels_results_<fecha>` y `drainage_results_<fecha>`, con los campos DAE, PAE y Priority. También guarda un registro de la corrida en `Loc/run_config_<fecha>.loc`.

El paso a paso detallado está en la sección **Guía de Usuario** del [sitio de documentación](#documentación-completa). Los dashboards de resultados de cada país están en la sección **Dashboard → Resultados por país**.

---

# Guía de instalación

## Requisitos del sistema

| Componente | Versión | Notas |
| --- | --- | --- |
| Sistema operativo | Windows 10/11 (64 bits) | ArcGIS Pro no está disponible para macOS ni Linux |
| ArcGIS Pro | 3.2.x o superior | Requiere licencia activa (Basic, Standard o Advanced) |
| Spatial Analyst | Extensión de ArcGIS Pro | Necesaria para muestrear los rásters de amenaza |
| Python | `arcgispro-py3` | Incluido con ArcGIS Pro |
| Hardware | 16 GB de RAM (se recomiendan 32 GB) | Los análisis nacionales con rásters de alta resolución consumen mucha memoria |

## Dependencias

El motor de cálculo usa solo paquetes incluidos en el entorno `arcgispro-py3`:

| Dependencia | Uso | Licencia |
| --- | --- | --- |
| [`arcpy`](https://pro.arcgis.com/es/pro-app/latest/arcpy/main/arcgis-pro-arcpy-reference.htm) (ArcGIS Pro, Esri) | Geoprocesamiento, lectura de capas y rásters | **Propietaria (Esri)**; requiere licencia de ArcGIS Pro |
| [`numpy`](https://numpy.org/) | Cálculo numérico | BSD-3-Clause |
| Biblioteca estándar de Python (`csv`, `re`, `os`, `heapq`, `ast`, `datetime`, `typing`, `collections`) | Utilidades | PSF |

> ⚠️ **Dependencia de software propietario.** El BSA 2.0 depende de ArcGIS Pro y `arcpy`, que son software comercial de Esri. Su ejecución requiere una licencia válida de ArcGIS Pro con la extensión Spatial Analyst.

## Instalación del toolbox

1. Clonar o descargar este repositorio:

    ```bash
    git clone https://github.com/joseafitoria0704/BSA2-Tool.git
    ```

2. Abrir ArcGIS Pro y activar la extensión **Spatial Analyst** en **Project → Licensing**.
3. En el panel **Catalog**, hacer clic derecho en **Toolboxes → Add Toolbox** y seleccionar `toolbox/BSA2.atbx`.
4. Hacer doble clic en la herramienta **BSA2** para abrir el diálogo de parámetros.

> `BSA2.atbx` enlaza el script `BSA2.py` por ruta relativa, así que ambos archivos deben quedar en la misma carpeta.

Para comprobar el entorno, ejecute lo siguiente en la ventana de Python de ArcGIS Pro:

```python
import arcpy, numpy
print(arcpy.__version__, numpy.__version__)
```

## Variables de entorno

La herramienta **no requiere variables de entorno** ni archivos de configuración adicionales. Todos los insumos se ingresan en el diálogo de parámetros del toolbox.

## Caso de referencia (Costa Rica)

`ejemplos/costa-rica/BSA2_CostaRica.zip` contiene la carpeta de trabajo del caso: el proyecto `CostaRica.aprx`, la geodatabase `BSA2.gdb` con las capas de exposición (red vial, puentes, túneles y drenajes), el toolbox y el script. También incluye las bases `FVU_BSA_V3.csv` y `OCO_BSA_CR_V1.csv`, que además están sueltas en la misma carpeta. Los parámetros de la corrida de referencia están en `ejemplos/costa-rica/Loc/run_config_20260413_172736.loc`.

> ⚠️ **Los rásters de amenaza del caso no están incluidos.** Faltan las inundaciones fluvial y costera y el sismo (`ri_h_CR_*.tif`, `c_h_CR_*.tif` y `EQ_CR_PGA_*.tif`). Además, `CostaRica.aprx` conserva referencias a carpetas locales de los autores. Para reproducir la corrida hay que obtener esos rásters del equipo del proyecto y volver a vincular las capas en ArcGIS Pro.

## Construir el sitio de documentación

La documentación necesita Python 3.9 o superior, independiente de ArcGIS Pro:

```bash
pip install -r requirements-docs.txt
mkdocs serve          # sitio local en http://127.0.0.1:8000/
mkdocs build --strict # genera el sitio estático en site/
```

También puede usar el entorno de desarrollo de `.devcontainer/` (VS Code o GitHub Codespaces).

## Pruebas

El motor depende de `arcpy`, por lo que no tiene pruebas unitarias automatizadas. Se valida con el caso de referencia de Costa Rica. El workflow `docs.yml` comprueba en cada *push* que el sitio de documentación se construya sin errores.

---

# Archivos de entrada y de salida

## Archivos de entrada

| Insumo (parámetro) | Formato | Contenido |
| --- | --- | --- |
| Red vial (`roads_path`, 0) | Capa de polilíneas | `ID_TRAMO`, `vul_f` (taxonomía de inundación), `vul_eq` (taxonomía sísmica), `rep_cost_k` (miles de USD por metro), `Longitud` (m), TPDA por tipo de vehículo `T9`–`T15` |
| Puentes, túneles y drenajes (1–3) | Capas de puntos | `ID_TRAMO` (tramo al que pertenecen), `vul_f`, `vul_eq`, `rep_cost` (USD) |
| Amenazas (4–7) | Varios GeoTIFF por amenaza, uno por periodo de retorno | Tirante (m) para inundación, altura de ola (m) para tsunami y PGA para sismo. El periodo de retorno se toma del **último número del nombre del archivo** (`ri_h_CR_100.tif` → Tr = 100) |
| Licuefacción (8) | Un GeoTIFF | Susceptibilidad en escala 1–4. Modifica la función de vulnerabilidad sísmica |
| Cambio climático (9) | Capa de polígonos | Campos `TP###S#M` con los periodos de retorno modificados por escenario |
| Vulnerabilidad (10) | CSV, una fila por curva: `taxonomy,[intensidades],[valores]` | Ejemplo: `FL_RMD_H_TRNP,[0,0.2,0.5,1.5,50],[0,1,2,20,20]`. Ver `ejemplos/costa-rica/FVU_BSA_V3.csv` (60 curvas) |
| Costos de operación (11) | CSV `taxonomy,COV,OCU` | Costo de operación vehicular (USD/km) y ocupación promedio para `T9`–`T15`. Ver `ejemplos/costa-rica/OCO_BSA_CR_V1.csv` |
| PIB per cápita por día (12) | Número | Valor del tiempo de las personas usuarias durante la interrupción |
| Longitud de segmento (13) | Número (m) | Distancia entre los puntos de muestreo sobre la red, por ejemplo 30 m |

El detalle de los datos obligatorios y opcionales está en la página [Datos de entrada](https://joseafitoria0704.github.io/BSA2-Tool/guia-usuario/datos-entrada/) del sitio de documentación.

## Archivos de salida (en `BSA2.gdb`, junto a `BSA2.py`)

| Salida | Contenido |
| --- | --- |
| `roads_results_<AAAAMMDD_HHMMSS>` | Red vial con los resultados por tramo, incluido el DAE de sus componentes |
| `bridges_results_<…>`, `tunnels_results_<…>`, `drainage_results_<…>` | Resultados por componente (solo si se ingresó la capa) |
| `Loc/run_config_<AAAAMMDD_HHMMSS>.loc` | Registro de los parámetros usados en la corrida |

Campos principales de las capas de resultados:

| Campo | Descripción |
| --- | --- |
| `damage_{amenaza}_{Tr}` y `loss_{amenaza}_{Tr}` | Daño físico y pérdida funcional (USD) por amenaza y periodo de retorno |
| `DAE_{amenaza}`, `DAE` / `DAE_total` | Daño Anual Esperado por amenaza y total (en la red vial, `DAE_total` suma los componentes) |
| `PAE_{amenaza}`, `PAE_total` | Pérdida Anual Esperada por interrupción, por amenaza y total |
| `Priority` | Índice de priorización: `DAE_total + PAE_total` |
| `*_mod_{escenario}`, `Priority_mod_{escenario}` | Resultados bajo cada escenario de cambio climático (solo con el parámetro 9) |

Los resultados se añaden automáticamente al mapa activo de ArcGIS Pro.

---

# Descripción del motor de cálculo

`toolbox/BSA2.py` contiene un solo script con la función `main()` y funciones auxiliares agrupadas por etapa:

| Etapa | Funciones | Qué hacen |
| --- | --- | --- |
| Utilidades | `ensure_field`, `find_field`, `parse_TR_from_name`, `get_endpoints`, `create_consolidated_copy` | Gestión de campos y capas, lectura del Tr desde el nombre del ráster, copia de las capas a `BSA2.gdb` |
| Amenaza | `sample_raster_to_points`, `add_raster_field`, `liquefaction_once` | Muestreo de los rásters de amenaza y de licuefacción sobre la red y sus componentes |
| Exposición | `road_geometry` | Genera puntos de muestreo cada `road_segme` metros y su longitud tributaria |
| Vulnerabilidad y daño | `read_vul_db`, `build_vul_key`, `process_roads`, `process_component`, `create_damage_fields`, `write_damage_by_oid` | Lectura de las curvas, selección de la curva por taxonomía, amenaza y licuefacción, y cálculo del daño por evento |
| Riesgo | `compute_DAE_fields`, `compute_PAE_fields`, `sum_component_DAE_by_tramo` | Integración sobre los periodos de retorno para obtener el DAE y la PAE, y agregación por tramo |
| Criticidad | `dijkstra`, `read_taxonomy_csv`, `road_loss_analysis`, `tramo_dlt_from_roads`, `map_component_dlt_by_tramo` | Ruta alterna más corta al cortar cada tramo, costo diario de la interrupción (operación vehicular y tiempo de las personas) y asignación a los componentes |
| Cambio climático | `parse_tp_fields`, `apply_TRmods`, `compute_mod_totals` | Recalcula el DAE y la PAE con los periodos de retorno modificados de cada escenario |

El orden de `arcpy.GetParameterAsText(0…13)` en `main()` debe coincidir con el de los parámetros de `toolbox/BSA2.atbx`, que además declara 4 salidas derivadas (índices 14–17). La metodología de cada módulo se explica en la sección **Metodología** del sitio de documentación. El historial de versiones está en [CHANGELOG.md](CHANGELOG.md).

---

# Estructura del repositorio

```
/
├── toolbox/
│   ├── BSA2.py               motor de cálculo (toolbox de ArcGIS Pro)
│   └── BSA2.atbx             definición del toolbox y de sus 14 parámetros
├── ejemplos/
│   └── costa-rica/           caso de referencia
│       ├── CostaRica.aprx    proyecto de ArcGIS Pro
│       ├── FVU_BSA_V3.csv    funciones de vulnerabilidad
│       ├── OCO_BSA_CR_V1.csv costos de operación vehicular
│       ├── Loc/              registro de la corrida de referencia
│       └── BSA2_CostaRica.zip  carpeta de trabajo completa (incluye BSA2.gdb)
├── docs/                     sitio de documentación MkDocs (ES: *.md, EN: *.en.md)
├── licenses/legacy/          licencia anterior (AM-331-A3)
├── mkdocs.yml                configuración del sitio
├── requirements-docs.txt     dependencias para construir el sitio
├── sonar-project.properties  configuración del análisis de SonarQube
├── .github/
│   ├── workflows/            CI: build.yml (SonarQube), docs.yml (sitio), scorecard.yml (OpenSSF)
│   ├── ISSUE_TEMPLATE/       plantilla de reporte de problemas (ES/EN)
│   └── PULL_REQUEST_TEMPLATE.md
├── .devcontainer/            entorno de desarrollo para la documentación
├── README-EN.md              README en inglés
├── CHANGELOG.md              historial de versiones
├── CONTRIBUTING.md
├── CODE-OF-CONDUCT.md
└── LICENSE.md
```

---

# Documentación completa

El sitio de documentación (en `docs/`) es bilingüe y tiene estas secciones:

| Sección | Contenido |
| --- | --- |
| Metodología | Antecedentes, propósito y alcances, conceptos clave, arquitectura, módulos de amenaza, exposición, vulnerabilidad y criticidad, cálculo de riesgo, estructura de datos |
| Primeros pasos | Requisitos, instalación, organización de datos, interfaz de la herramienta |
| Guía de Usuario | Flujo de trabajo, datos de entrada, configuración de una corrida, resultados, caso de ejemplo |
| Dashboard | Descripción general, exploración de métricas, resultados por país |
| Recursos | Descargas, referencias bibliográficas, preguntas frecuentes |
| Glosario | Conceptos y diccionario de siglas |

**Consulte el sitio en línea: [https://joseafitoria0704.github.io/BSA2-Tool/](https://joseafitoria0704.github.io/BSA2-Tool/)** (versión en inglés: [https://joseafitoria0704.github.io/BSA2-Tool/en/](https://joseafitoria0704.github.io/BSA2-Tool/en/)).

El workflow `docs.yml` lo compila y publica en GitHub Pages automáticamente en cada *push* a `main`. Para consultarlo localmente, ver [Construir el sitio de documentación](#construir-el-sitio-de-documentación).

---

# Cómo contribuir

Las contribuciones son bienvenidas. Haga un *fork*, desarrolle el cambio en una rama y abra un *pull request* que lo documente. Para reportar fallos, abra un *issue* con la versión de ArcGIS Pro, los parámetros usados y el mensaje de error. Las guías de estilo y la terminología obligatoria (DAE / PAE / PML) están en [CONTRIBUTING.md](CONTRIBUTING.md).

# Código de conducta

Este proyecto adopta el [Código de Conducta](CODE-OF-CONDUCT.md) de la iniciativa Código para el Desarrollo del BID, basado en el *Contributor Covenant* 1.4.

---

# Autores

La metodología y el motor de cálculo del BSA 2.0 los desarrollan las divisiones de **Transporte (TSP)**, **Gestión de Riesgo de Desastres (DRM)** y **Cambio Climático (CCS)** del **Banco Interamericano de Desarrollo**.

- **Motor de cálculo (`toolbox/BSA2.py`):** Kenneth Otárola. Su historial de versiones proviene del repositorio [keom0891/BSA2](https://github.com/keom0891/BSA2).
- **Sitio de documentación (`docs/`):** Andrés Abarca. Proviene del repositorio [andresabarca-atlas/bsa-docs](https://github.com/andresabarca-atlas/bsa-docs).
- **Liderazgo del programa:** Manuel Rodríguez (TSP) y Ginés Suárez (DRM).
- **Dirección del producto:** María Alejandra Escovar (DRM), Juan Camilo Olaya (TSP) y Kenneth Otárola.

El equipo completo está en la sección [Equipo del proyecto](https://joseafitoria0704.github.io/BSA2-Tool/#equipo-del-proyecto) del sitio de documentación.

**Contacto del proyecto:** María Alejandra Escovar (DRM, BID).

---

# Información adicional

- **Dashboards de resultados** (ArcGIS Experience): [República Dominicana](https://experience.arcgis.com/experience/f9ef8a09343e49b8828d590fbc82bae0) · [Costa Rica](https://experience.arcgis.com/experience/e1c2ebe138554254b29f5f0ea74f2302) · [El Salvador](https://experience.arcgis.com/experience/a9258d5c9ffe4cd0aa6b5fdef675c659)
- **Herramienta relacionada:** [LEC Tool](https://github.com/EL-BID/LEC-Tool), del mismo equipo DRM del BID, para curvas de excedencia de pérdidas y evaluación de estrategias de gestión financiera del riesgo.
- **Origen del repositorio:** consolida `andresabarca-atlas/bsa-docs` y `keom0891/BSA2` y conserva el historial de commits de ambos.

---

# Licencia

El software se distribuye bajo la **Licencia de Software de Código Abierto del BID** (vigente desde diciembre de 2025). Consulte [LICENSE.md](LICENSE.md). La Documentación de Soporte y Uso está licenciada bajo **Creative Commons CC-BY 4.0**. La licencia anterior del proyecto (AM-331-A3) se conserva en [licenses/legacy/](licenses/legacy/LICENSE_AM-331-A3.md) como referencia histórica.

Copyright © 2026. Banco Interamericano de Desarrollo ("BID"). Uso autorizado.

## Limitación de responsabilidades

El BID no será responsable, bajo circunstancia alguna, de daño ni indemnización, moral o patrimonial; directo o indirecto; accesorio o especial; o por vía de consecuencia, previsto o imprevisto, que pudiese surgir:

i. Bajo cualquier teoría de responsabilidad, ya sea por contrato, infracción de derechos de propiedad intelectual, negligencia o bajo cualquier otra teoría; y/o

ii. A raíz del uso de la Herramienta Digital, incluyendo, pero sin limitación de potenciales defectos en la Herramienta Digital, o la pérdida o inexactitud de los datos de cualquier tipo. Lo anterior incluye los gastos o daños asociados a fallas de comunicación y/o fallas de funcionamiento de computadoras, vinculados con la utilización de la Herramienta Digital.


## Acknowledgments / Reconocimientos

**Copyright © [2026]. Inter-American Development Bank ("IDB"). Authorized Use.**  
The procedures and results obtained based on the execution of this software are those programmed by the developers and do not necessarily reflect the views of the IDB, its Board of Executive Directors or the countries it represents.

**Copyright © [2026]. Banco Interamericano de Desarrollo ("BID"). Uso Autorizado.**  
Los procedimientos y resultados obtenidos con la ejecución de este software son los programados por los desarrolladores y no reflejan necesariamente las opiniones del BID, su Directorio Ejecutivo ni los países que representa.

### Support and Usage Documentation / Documentación de Soporte y Uso

**Copyright © [2026]. Inter-American Development Bank ("IDB").** The Support and Usage Documentation is licensed under the Creative Commons License CC-BY 4.0 license. The opinions expressed in the Support and Usage Documentation are those of its authors and do not necessarily reflect the opinions of the IDB, its Board of Executive Directors, or the countries it represents.

**Copyright © [2026]. Banco Interamericano de Desarrollo (BID).** La Documentación de Soporte y Uso está licenciada bajo la licencia Creative Commons CC-BY 4.0. Las opiniones expresadas en la Documentación de Soporte y Uso son las de sus autores y no reflejan necesariamente las opiniones del BID, su Directorio Ejecutivo ni los países que representa.
