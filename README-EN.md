*This digital tool is part of the tool catalog of the **Inter-American Development Bank**. Learn more about the IDB initiative at [https://knowledge.iadb.org/en/code-development](https://knowledge.iadb.org/en/code-development)*

<p align="center"><img src="docs/assets/logo-bid.png" alt="Inter-American Development Bank" height="80"/></p>

<h1 align="center">Blue Spot Analysis 2.0 (BSA 2.0)</h1>

<p align="center"><b>Prioritizing transport infrastructure investments based on natural hazard risk</b></p>

<p align="center"><img src="docs/assets/metodologia/image16.png" alt="BSA prioritization map of road segments in the Dominican Republic" width="640"/><br/><sub>Sample output: prioritization level of road segments at provincial scale (Dominican Republic). Source: BSA 2.0 Concept Report.</sub></p>

![version](https://img.shields.io/badge/version-0.3.0-blue)
![ArcGIS Pro](https://img.shields.io/badge/ArcGIS%20Pro-3.2%2B-2C7AC3)
![python](https://img.shields.io/badge/python-arcgispro--py3-3776AB)
![docs](https://img.shields.io/badge/docs-MkDocs%20Material-526CFE)
![license](https://img.shields.io/badge/license-IDB%20Open%20Source-lightgrey)
<!-- SonarQube Cloud badge (requested by Code for Development); enable it once the project is configured in EL-BID:
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=EL-BID_BSA2-Tool&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=EL-BID_BSA2-Tool)
-->

[Español](README.md) | **English**

<p align="center"><a href="https://joseafitoria0704.github.io/BSA2-Tool/en/"><img src="https://img.shields.io/badge/Online%20documentation-Open%20the%20site-0B5394?style=for-the-badge" alt="Open the online documentation"/></a></p>

> 📘 **Full online documentation:** [https://joseafitoria0704.github.io/BSA2-Tool/en/](https://joseafitoria0704.github.io/BSA2-Tool/en/): methodology, installation, user guide, dashboard and glossary.

---

## Table of contents

- [Description and context](#description-and-context)
- [User guide](#user-guide)
- [Installation guide](#installation-guide)
- [Input and output files](#input-and-output-files)
- [Calculation engine](#calculation-engine)
- [Repository structure](#repository-structure)
- [Full documentation](#full-documentation)
- [How to contribute](#how-to-contribute)
- [Code of conduct](#code-of-conduct)
- [Authors](#authors)
- [Additional information](#additional-information)
- [License](#license)
- [Limitation of responsibilities](#limitation-of-responsibilities)

---

# Description and context

The **Blue Spot Analysis 2.0 (BSA 2.0)** is a methodology, a desktop tool and a results dashboard developed by the **Inter-American Development Bank (IDB)**. They are used to **prioritize investments in transport infrastructure** through a simplified natural hazard risk analysis at national or regional scale.

The analysis combines four components:

| Module | What it represents |
| --- | --- |
| **Hazard** | Intensity of natural events for several return periods: riverine flooding, pluvial/coastal flooding, earthquake, tsunami and liquefaction, with optional climate change modifiers |
| **Exposure** | Road network and its components (segments, bridges, tunnels and drainage), with replacement costs and traffic |
| **Vulnerability** | Vulnerability functions (mean damage ratio) by asset taxonomy and hazard type |
| **Criticality** | Functional importance of each segment, estimated from alternative routes (Dijkstra's algorithm) and vehicle operating costs |

With these components the tool estimates, for each asset:

- **EAD** (*DAE* in Spanish), Expected Annual Damage: direct physical damage to the infrastructure.
- **EAL** (*PAE* in Spanish), Expected Annual Loss: economic loss caused by traffic disruption.
- **PML**, Probable Maximum Loss, associated with a design event.
- An asset **prioritization index**.

The results feed damage and loss maps, exceedance curves and prioritization rankings, and are published in an online dashboard for decision makers.

BSA 2.0 has been applied in the **Dominican Republic** (reference case), **Costa Rica** and **El Salvador**. The tool is a joint effort of the IDB's **Transport (TSP)**, **Disaster Risk Management (DRM)** and **Climate Change (CCS)** divisions.

This repository brings together:

1. the **calculation engine** (`toolbox/BSA2.py`) and the ArcGIS Pro toolbox (`toolbox/BSA2.atbx`);
2. the **Costa Rica reference case** (`ejemplos/costa-rica/`);
3. the bilingual Spanish/English **documentation site** (`docs/`, MkDocs + Material), published at **[https://joseafitoria0704.github.io/BSA2-Tool/en/](https://joseafitoria0704.github.io/BSA2-Tool/en/)**.

---

# User guide

BSA 2.0 runs entirely from the ArcGIS Pro graphical interface, with no programming. The workflow has six stages:

1. **Collect and standardize the data**: exposure layers, hazard rasters by return period, and vulnerability and cost databases (see [Input Data](https://joseafitoria0704.github.io/BSA2-Tool/en/guia-usuario/datos-entrada/) on the documentation site).
2. **Prepare the exposure layers** with their required attributes (`ID_TRAMO`, `vul_f`, `vul_eq`, `rep_cost_k`, traffic `T9`–`T15`, etc.).
3. **Compute the country's GDP per capita per day.**
4. **Define the road segment length** (for example, 30 m in the Costa Rica case).
5. **Run the BSA2 toolbox** in ArcGIS Pro with its 14 parameters:

    | # | Parameter | Description |
    | --- | --- | --- |
    | 0 | `roads_path` | Road network (required) |
    | 1–3 | `bridge_path`, `tunnel_path`, `draina_path` | Bridges, tunnels and drainage (optional) |
    | 4–8 | `fl_rive_raw`, `fl_coas_raw`, `ts_coas_raw`, `earthqu_raw`, `liquefa_raw` | Hazard rasters: riverine flood, pluvial/coastal flood, tsunami, earthquake and liquefaction |
    | 9 | `mod_tp_poly` | Climate change modifier polygon (optional) |
    | 10 | `vulner_data` | Vulnerability function database, e.g. `FVU_BSA_V3.csv` (required) |
    | 11 | `operat_data` | Vehicle operating cost database, e.g. `OCO_BSA_CR_V1.csv` (optional) |
    | 12 | `gdppca_doub` | GDP per capita per day (optional) |
    | 13 | `road_segme` | Segment length in meters (required) |

6. **Review the results and load them into the dashboard.** The tool creates the layers `roads_results_<date>`, `bridges_results_<date>`, `tunnels_results_<date>` and `drainage_results_<date>` in `BSA2.gdb`, next to the script, with the DAE, PAE and Priority fields. It also saves a run log in `Loc/run_config_<date>.loc`.

The detailed step-by-step guide is in the **User Guide** section of the [documentation site](#full-documentation). The results dashboards for each country are in **Dashboard → Results by Country**.

---

# Installation guide

## System requirements

| Component | Version | Notes |
| --- | --- | --- |
| Operating system | Windows 10/11 (64-bit) | ArcGIS Pro is not available for macOS or Linux |
| ArcGIS Pro | 3.2.x or later | Requires an active license (Basic, Standard or Advanced) |
| Spatial Analyst | ArcGIS Pro extension | Required to sample the hazard rasters |
| Python | `arcgispro-py3` | Included with ArcGIS Pro |
| Hardware | 16 GB RAM (32 GB recommended) | National analyses with high-resolution rasters are memory-intensive |

## Dependencies

The calculation engine only uses packages included in the `arcgispro-py3` environment:

| Dependency | Use | License |
| --- | --- | --- |
| [`arcpy`](https://pro.arcgis.com/en/pro-app/latest/arcpy/main/arcgis-pro-arcpy-reference.htm) (ArcGIS Pro, Esri) | Geoprocessing, reading layers and rasters | **Proprietary (Esri)**; requires an ArcGIS Pro license |
| [`numpy`](https://numpy.org/) | Numerical computing | BSD-3-Clause |
| Python standard library (`csv`, `re`, `os`, `heapq`, `ast`, `datetime`, `typing`, `collections`) | Utilities | PSF |

> ⚠️ **Proprietary software dependency.** BSA 2.0 depends on ArcGIS Pro and `arcpy`, which are commercial Esri software. Running it requires a valid ArcGIS Pro license with the Spatial Analyst extension.

## Installing the toolbox

1. Clone or download this repository:

    ```bash
    git clone https://github.com/joseafitoria0704/BSA2-Tool.git
    ```

2. Open ArcGIS Pro and enable the **Spatial Analyst** extension under **Project → Licensing**.
3. In the **Catalog** pane, right-click **Toolboxes → Add Toolbox** and select `toolbox/BSA2.atbx`.
4. Double-click the **BSA2** tool to open the parameter dialog.

> `BSA2.atbx` links to the `BSA2.py` script by relative path, so both files must stay in the same folder.

To check the environment, run the following in the ArcGIS Pro Python window:

```python
import arcpy, numpy
print(arcpy.__version__, numpy.__version__)
```

## Environment variables

The tool **does not require any environment variables** or additional configuration files. All inputs are entered in the toolbox parameter dialog.

## Reference case (Costa Rica)

`ejemplos/costa-rica/BSA2_CostaRica.zip` contains the working folder of the case: the `CostaRica.aprx` project, the `BSA2.gdb` geodatabase with the exposure layers (road network, bridges, tunnels and drainage), the toolbox and the script. It also includes the `FVU_BSA_V3.csv` and `OCO_BSA_CR_V1.csv` databases, which are also available unzipped in the same folder. The parameters of the reference run are recorded in `ejemplos/costa-rica/Loc/run_config_20260413_172736.loc`.

> ⚠️ **The hazard rasters of the case are not included.** The riverine flood, coastal flood and earthquake rasters (`ri_h_CR_*.tif`, `c_h_CR_*.tif` and `EQ_CR_PGA_*.tif`) are missing. In addition, `CostaRica.aprx` still references the authors' local folders. To reproduce the run, obtain the rasters from the project team and relink the layers in ArcGIS Pro.

## Tests

The engine depends on `arcpy`, so it has no automated unit tests. It is validated with the Costa Rica reference case. The `docs.yml` workflow checks on every *push* that the documentation site builds without errors.

---

# Input and output files

## Input files

| Input (parameter) | Format | Content |
| --- | --- | --- |
| Road network (`roads_path`, 0) | Polyline layer | `ID_TRAMO`, `vul_f` (flood taxonomy), `vul_eq` (seismic taxonomy), `rep_cost_k` (thousand USD per meter), `Longitud` (m), traffic by vehicle type `T9`–`T15` |
| Bridges, tunnels and drainage (1–3) | Point layers | `ID_TRAMO` (segment they belong to), `vul_f`, `vul_eq`, `rep_cost` (USD) |
| Hazards (4–7) | Several GeoTIFFs per hazard, one per return period | Water depth (m) for floods, wave height (m) for tsunami and PGA for earthquake. The return period is read from the **last number in the file name** (`ri_h_CR_100.tif` → RP = 100) |
| Liquefaction (8) | One GeoTIFF | Susceptibility on a 1–4 scale. Modifies the seismic vulnerability function |
| Climate change (9) | Polygon layer | `TP###S#M` fields with the modified return periods per scenario |
| Vulnerability (10) | CSV, one row per curve: `taxonomy,[intensities],[values]` | Example: `FL_RMD_H_TRNP,[0,0.2,0.5,1.5,50],[0,1,2,20,20]`. See `ejemplos/costa-rica/FVU_BSA_V3.csv` (60 curves) |
| Operating costs (11) | CSV `taxonomy,COV,OCU` | Vehicle operating cost (USD/km) and average occupancy for `T9`–`T15`. See `ejemplos/costa-rica/OCO_BSA_CR_V1.csv` |
| GDP per capita per day (12) | Number | Value of users' time during the disruption |
| Segment length (13) | Number (m) | Spacing of the sampling points along the network, e.g. 30 m |

The mandatory and optional data are detailed on the [Input Data](https://joseafitoria0704.github.io/BSA2-Tool/en/guia-usuario/datos-entrada/) page of the documentation site.

## Output files (in `BSA2.gdb`, next to `BSA2.py`)

| Output | Content |
| --- | --- |
| `roads_results_<YYYYMMDD_HHMMSS>` | Road network with per-segment results, including the DAE of its components |
| `bridges_results_<…>`, `tunnels_results_<…>`, `drainage_results_<…>` | Per-component results (only if the layer was provided) |
| `Loc/run_config_<YYYYMMDD_HHMMSS>.loc` | Log of the parameters used in the run |

Main fields of the result layers:

| Field | Description |
| --- | --- |
| `damage_{hazard}_{RP}` and `loss_{hazard}_{RP}` | Physical damage and functional loss (USD) per hazard and return period |
| `DAE_{hazard}`, `DAE` / `DAE_total` | Expected Annual Damage per hazard and total (on the road network, `DAE_total` adds up its components) |
| `PAE_{hazard}`, `PAE_total` | Expected Annual Loss from disruption, per hazard and total |
| `Priority` | Prioritization index: `DAE_total + PAE_total` |
| `*_mod_{scenario}`, `Priority_mod_{scenario}` | Results under each climate change scenario (only with parameter 9) |

The results are added automatically to the active ArcGIS Pro map.

---

# Calculation engine

`toolbox/BSA2.py` is a single script with a `main()` function and helper functions grouped by stage:

| Stage | Functions | What they do |
| --- | --- | --- |
| Utilities | `ensure_field`, `find_field`, `parse_TR_from_name`, `get_endpoints`, `create_consolidated_copy` | Field and layer management, reading the RP from the raster name, copying layers to `BSA2.gdb` |
| Hazard | `sample_raster_to_points`, `add_raster_field`, `liquefaction_once` | Sampling of the hazard and liquefaction rasters over the network and its components |
| Exposure | `road_geometry` | Generates sampling points every `road_segme` meters and their tributary length |
| Vulnerability and damage | `read_vul_db`, `build_vul_key`, `process_roads`, `process_component`, `create_damage_fields`, `write_damage_by_oid` | Reads the curves, selects the curve by taxonomy, hazard and liquefaction, and computes the damage per event |
| Risk | `compute_DAE_fields`, `compute_PAE_fields`, `sum_component_DAE_by_tramo` | Integration over return periods to obtain DAE and PAE, and aggregation by segment |
| Criticality | `dijkstra`, `read_taxonomy_csv`, `road_loss_analysis`, `tramo_dlt_from_roads`, `map_component_dlt_by_tramo` | Shortest alternative route when each segment is cut, daily cost of the disruption (vehicle operation and users' time) and assignment to the components |
| Climate change | `parse_tp_fields`, `apply_TRmods`, `compute_mod_totals` | Recomputes DAE and PAE with the modified return periods of each scenario |

The order of `arcpy.GetParameterAsText(0…13)` in `main()` must match the parameters in `toolbox/BSA2.atbx`, which also declares 4 derived outputs (indexes 14–17). The methodology behind each module is explained in the **Methodology** section of the documentation site. The version history is in [CHANGELOG.md](CHANGELOG.md).

---

# Repository structure

```
/
├── toolbox/
│   ├── BSA2.py               calculation engine (ArcGIS Pro toolbox)
│   └── BSA2.atbx             toolbox definition and its 14 parameters
├── ejemplos/
│   └── costa-rica/           reference case
│       ├── CostaRica.aprx    ArcGIS Pro project
│       ├── FVU_BSA_V3.csv    vulnerability functions
│       ├── OCO_BSA_CR_V1.csv vehicle operating costs
│       ├── Loc/              log of the reference run
│       └── BSA2_CostaRica.zip  complete working folder (includes BSA2.gdb)
├── docs/                     MkDocs documentation site (ES: *.md, EN: *.en.md)
├── licenses/legacy/          previous license (AM-331-A3)
├── mkdocs.yml                site configuration
├── requirements-docs.txt     dependencies to build the site
├── sonar-project.properties  code-quality analysis configuration (SonarQube, required by the IDB)
├── .github/
│   ├── workflows/            CI: build.yml (SonarQube), docs.yml (site), scorecard.yml (OpenSSF)
│   ├── ISSUE_TEMPLATE/       issue report template (ES/EN)
│   └── PULL_REQUEST_TEMPLATE.md
├── .devcontainer/            development environment for the documentation
├── README-EN.md              this file
├── CHANGELOG.md              version history
├── CONTRIBUTING.md
├── CODE-OF-CONDUCT.md
└── LICENSE.md
```

---

# Full documentation

The documentation site (in `docs/`) is bilingual and has these sections:

| Section | Content |
| --- | --- |
| Methodology | Background, purpose and scope, key concepts, architecture, hazard, exposure, vulnerability and criticality modules, risk calculation, data structure |
| Getting Started | Requirements, installation, data organization, tool interface |
| User Guide | Workflow, input data, configuring a run, results, case study |
| Dashboard | Overview, metrics exploration, results by country |
| Resources | Downloads, bibliographic references, FAQ |
| Glossary | Concepts and acronym dictionary |

**Browse the site online: [https://joseafitoria0704.github.io/BSA2-Tool/en/](https://joseafitoria0704.github.io/BSA2-Tool/en/)** (Spanish version: [https://joseafitoria0704.github.io/BSA2-Tool/](https://joseafitoria0704.github.io/BSA2-Tool/)).

The `docs.yml` workflow builds and publishes it to GitHub Pages automatically on every *push* to `main`.

---

# How to contribute

Contributions are welcome. Fork the repository, develop the change in a branch and open a documented *pull request*. To report bugs, open an *issue* with the ArcGIS Pro version, the parameters used and the error message. The style guides and the mandatory terminology (DAE / PAE / PML) are in [CONTRIBUTING.md](CONTRIBUTING.md) (in Spanish).

# Code of conduct

This project adopts the [Code of Conduct](CODE-OF-CONDUCT.md) of the IDB's Code for Development initiative, based on the *Contributor Covenant* 1.4.

---

# Authors

The BSA 2.0 methodology and calculation engine are developed by the **Transport (TSP)**, **Disaster Risk Management (DRM)** and **Climate Change (CCS)** divisions of the **Inter-American Development Bank**.

- **Calculation engine (`toolbox/BSA2.py`):** Kenneth Otárola. Its version history comes from the [keom0891/BSA2](https://github.com/keom0891/BSA2) repository.
- **Documentation site (`docs/`):** Andrés Abarca. It comes from the [andresabarca-atlas/bsa-docs](https://github.com/andresabarca-atlas/bsa-docs) repository.
- **Program leadership:** Manuel Rodríguez (TSP) and Ginés Suárez (DRM).
- **Product direction:** María Alejandra Escovar (DRM), Juan Camilo Olaya (TSP) and Kenneth Otárola.

The full team is listed in the [Project team](https://joseafitoria0704.github.io/BSA2-Tool/en/#project-team) section of the documentation site.

**Project contact:** María Alejandra Escovar (DRM, IDB).

---

# Additional information

- **Results dashboards** (ArcGIS Experience): [Dominican Republic](https://experience.arcgis.com/experience/f9ef8a09343e49b8828d590fbc82bae0) · [Costa Rica](https://experience.arcgis.com/experience/e1c2ebe138554254b29f5f0ea74f2302) · [El Salvador](https://experience.arcgis.com/experience/a9258d5c9ffe4cd0aa6b5fdef675c659)
- **Related tool:** [LEC Tool](https://github.com/EL-BID/LEC-Tool), by the same IDB DRM team, for loss exceedance curves and the evaluation of financial risk management strategies.
- **Repository origin:** it consolidates `andresabarca-atlas/bsa-docs` and `keom0891/BSA2` and keeps the commit history of both.

---

# License

The software is distributed under the **IDB Open-Source Software License** (effective December 2025); see [LICENSE.md](LICENSE.md). The Support and Usage Documentation is licensed under **Creative Commons CC-BY 4.0**. The project's previous license (AM-331-A3) is kept in [licenses/legacy/](licenses/legacy/LICENSE_AM-331-A3.md) for historical reference.

Copyright © 2026. Inter-American Development Bank ("IDB"). Authorized Use.

## Limitation of responsibilities

The IDB will not be responsible, under any circumstance, for damage or compensation, moral or patrimonial; direct or indirect; accessory or special; or by way of consequence, foreseen or unforeseen, that could arise:

i. Under any theory of liability, whether by contract, infringement of intellectual property rights, negligence or under any other theory; and/or

ii. As a result of the use of the Digital Tool, including, but not limited to, potential defects in the Digital Tool, or the loss or inaccuracy of data of any kind. The foregoing includes expenses or damages associated with communication failures and / or computer malfunctions, related to the use of the Digital Tool.


## Acknowledgments / Reconocimientos

**Copyright © [2026]. Inter-American Development Bank ("IDB"). Authorized Use.**  
The procedures and results obtained based on the execution of this software are those programmed by the developers and do not necessarily reflect the views of the IDB, its Board of Executive Directors or the countries it represents.

**Copyright © [2026]. Banco Interamericano de Desarrollo ("BID"). Uso Autorizado.**  
Los procedimientos y resultados obtenidos con la ejecución de este software son los programados por los desarrolladores y no reflejan necesariamente las opiniones del BID, su Directorio Ejecutivo ni los países que representa.

### Support and Usage Documentation / Documentación de Soporte y Uso

**Copyright © [2026]. Inter-American Development Bank ("IDB").** The Support and Usage Documentation is licensed under the Creative Commons License CC-BY 4.0 license. The opinions expressed in the Support and Usage Documentation are those of its authors and do not necessarily reflect the opinions of the IDB, its Board of Executive Directors, or the countries it represents.

**Copyright © [2026]. Banco Interamericano de Desarrollo (BID).** La Documentación de Soporte y Uso está licenciada bajo la licencia Creative Commons CC-BY 4.0. Las opiniones expresadas en la Documentación de Soporte y Uso son las de sus autores y no reflejan necesariamente las opiniones del BID, su Directorio Ejecutivo ni los países que representa.
