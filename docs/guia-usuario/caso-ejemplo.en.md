# Case Study — Costa Rica

This page describes the application of BSA 2.0 to the Costa Rica reference case, which serves as an **example of the workflow**: it shows how the inputs are organized, which parameters are entered and which results are obtained. The files are in the repository folder [`ejemplos/costa-rica/`](https://github.com/joseafitoria0704/BSA2-Tool/tree/main/ejemplos/costa-rica).

!!! note "Purpose of the case study"
    The Costa Rica case is a reference dataset that illustrates the complete operation of the toolbox. It does not represent an official analysis of the country; its function is pedagogical and technical validation.

!!! warning "Status of the example: incomplete"
    The 22 hazard rasters are missing, so **the run cannot be reproduced yet**. It also lacks an ArcGIS Pro project, and the reference results have [known limitations](#known-limitations). The up-to-date status is in the [example's README](https://github.com/joseafitoria0704/BSA2-Tool/blob/main/ejemplos/costa-rica/README-EN.md).

## Contents of the case study

The folder follows the structure recommended in [Data Organization](../getting-started/organizacion-datos.md):

| Folder | Content | Status |
|--------|---------|--------|
| `Exposure/` | Four shapefiles (WGS 84) with the exposure layers: roads, bridges, tunnels and drainage. | Included |
| `Hazard/` | The 22 hazard rasters (GeoTIFF). | **Pending** |
| `Vulnerability/` | `FVU_BSA_V3.csv`: vulnerability function database (physical and traffic), with 60 curves. | Included |
| `Operations/` | `OCO_BSA_CR_V1.csv`: operating costs and occupancy by vehicle type. | Included |
| `Reference_results/` | A GeoPackage with the four results layers of the reference run and the `.loc` file with its parameters. | Included |

## Inputs used

### Exposure layers (`Exposure/`)

| File | Type | Records | Description |
|------|------|---------|-------------|
| `crc_RVN_WGS84.shp` | Polylines | 1,453 | Costa Rica's national road network in WGS84 datum. |
| `crc_rvn_puentes2.shp` | Points | 1,562 | Inventory of bridges on main corridors. |
| `cr_tuneles_rvn_WGS84.shp` | Points | 1 | Inventory of tunnels on the national road network. |
| `crc_rvn_drenaje2.shp` | Points | 371 | Drainage elements on the road network. |

!!! info "Rebuilt layers"
    The original case package only contained the results layers. The exposure layers were rebuilt from them, keeping the original geometry and attributes and removing the fields computed by the tool.

### Hazard grids (`Hazard/`)

The reference run used 22 rasters (see the details in the [`Hazard/` README](https://github.com/joseafitoria0704/BSA2-Tool/blob/main/ejemplos/costa-rica/Hazard/README.md)):

| Hazard | Files | Return periods (years) |
|--------|-------|------------------------|
| Riverine flood (7) | `ri_h_CR_{Tr}.tif` | 10, 20, 50, 75, 100, 200, 500 |
| Coastal/pluvial flood (10) | `c_h_CR_{Tr}.tif` | 1, 2, 5, 10, 25, 50, 100, 250, 500, 1,000 |
| Earthquake, PGA (5) | `EQ_CR_PGA_{Tr}.tif` | 100, 225, 475, 2,475, 4,975 |

Tsunami and liquefaction were not available for this run.

### Economic parameters

| Parameter | Value |
|-----------|-------|
| GDP per capita per day | 45,249.62 (the monetary unit is to be confirmed; see [Known limitations](#known-limitations)) |
| Segment length | 30 meters |

## Run parameters

| # | Parameter | Value |
|---|-----------|-------|
| 0 | Road network | `Exposure/crc_RVN_WGS84.shp` |
| 1 | Bridges | `Exposure/crc_rvn_puentes2.shp` |
| 2 | Tunnels | `Exposure/cr_tuneles_rvn_WGS84.shp` |
| 3 | Drainage | `Exposure/crc_rvn_drenaje2.shp` |
| 4 | Riverine flood | 7 rasters from `Hazard/` |
| 5 | Coastal flood | 10 rasters from `Hazard/` |
| 6 | Tsunami | *(empty)* |
| 7 | Earthquake | 5 rasters from `Hazard/` |
| 8 | Liquefaction | *(empty)* |
| 9 | Climate change | *(empty)* |
| 10 | Vulnerability | `Vulnerability/FVU_BSA_V3.csv` |
| 11 | Operating costs | `Operations/OCO_BSA_CR_V1.csv` |
| 12 | GDP per capita per day | `45249.62` |
| 13 | Segment length | `30` |

## How to reproduce the analysis

Requires ArcGIS Pro 3.2 or later with the Spatial Analyst extension (see [Installation](../getting-started/instalacion.md)).

1. **Prepare a working folder.** Copy the `ejemplos/costa-rica/` folder to your computer, for example to `C:\BSA2_CostaRica\`.
2. **Copy the toolbox next to the data.** Copy `BSA2.atbx` and `BSA2.py` (the repository's `toolbox/` folder) into the working folder. The tool creates its outputs (`BSA2.gdb` and `Loc/`) where `BSA2.py` is located, and both files must be together.
3. **Add the hazard rasters** to the `Hazard/` folder.
4. **Create an ArcGIS Pro project** in the working folder, add the `BSA2.atbx` toolbox from the *Catalog* pane and open the **BSA2** tool.
5. **Enter the parameters** from the table above (see also [Configuring a Run](configuracion-corrida.md#configuration-example-costa-rica)) and click **Run**.
6. **Compare** the new `roads_results_*` layers with those in `Reference_results/` to validate reproducibility.

## Reference results

The GeoPackage `Reference_results/BSA2_CostaRica_results_20260413_172736.gpkg` contains the four layers generated by the run of 13 April 2026. It opens in ArcGIS Pro and QGIS.

- **`roads_results_20260413_172736`** — 1,453 segments with DAE fields by hazard (riverine, coastal, seismic), total DAE, PAE by hazard, total PAE and `Priority`.
- **`bridges_results_20260413_172736`** — 1,562 bridges with their own DAE, PAE and `Priority` metrics.
- **`tunnels_results_20260413_172736`** — 1 tunnel with individual metrics.
- **`drainage_results_20260413_172736`** — 371 drainage elements with individual metrics.

Values to validate your own run (sums over the road network, in the monetary unit of the run):

| Field | Sum |
|-------|-----|
| `DAE_river` | 1.885 × 10¹⁰ |
| `DAE_coast` | 1.213 × 10⁷ |
| `DAE_earthquake` | 1.951 × 10¹⁰ |
| **`DAE_total`** | **3.838 × 10¹⁰** |
| `PAE_total` | 6.543 × 10⁹ |
| **`Priority`** | **4.492 × 10¹⁰** |

The segments with the highest `Priority` are National Route 34 (`ID_TRAMO` 755), National Route 2 (1197) and National Route 245 (716).

!!! tip "Quick validation"
    Filter the results layer by the segments with the highest `Priority` and compare them geographically with the country's historical road damage records. A spatial match between high-`Priority` segments and historically affected areas is an indicator of the model's coherence.

## Known limitations

These limitations of the case are pending review by the project team. They are not expected behavior of the tool.

!!! warning "Components are not linked to the roads"
    The `ID_TRAMO` of bridges, tunnels and drainage (10001 to 70740) does not match any of the road network's (0 to 1472). As a result, in the reference results the roads' `DAE_bridge`, `DAE_tunnel` and `DAE_drainage` fields are 0, and the components' `PAE_total` is also 0. The road network's `DAE_total` only includes the segments' own damage.

!!! warning "Monetary unit to be confirmed"
    This documentation and the input data sheet express costs in USD, but the magnitudes in this case (for example `rep_cost_k` with a median of 3.8 × 10⁸ and operating costs of 137 to 246 per km) only make sense in local currency (colones). Until this is confirmed, interpret the figures as "monetary units of the run".

- `ID_TRAMO` 1278 appears in two records of the road network.
- The original ArcGIS Pro project (`CostaRica.aprx`) was not portable: it pointed to the authors' local folders. It was removed and must be replaced by a new project.
