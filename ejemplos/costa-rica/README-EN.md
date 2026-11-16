# Reference case: Costa Rica

[Español](README.md) | **English**

This is the **reference example of the BSA 2.0 workflow**. It gathers the inputs and the results of a real run of the tool over Costa Rica's national road network, so that anyone can see how the data are organized, which parameters are entered and which results are obtained.

> ⚠️ **Status of the example: incomplete.** The 22 hazard rasters are missing (folder [`Hazard/`](Hazard/)), so **the run cannot be reproduced yet**. The rest of the inputs and the reference results are included. See [Status of the example](#status-of-the-example) and [Known limitations](#known-limitations-of-the-case).

## Status of the example

| Item | Folder | Status |
| --- | --- | --- |
| Exposure layers (roads, bridges, tunnels, drainage) | [`Exposure/`](Exposure/) | ✅ Included (rebuilt, see [Origin](#origin-of-the-files)) |
| Vulnerability functions (FVU) | [`Vulnerability/`](Vulnerability/) | ✅ Included |
| Vehicle operating costs (OCO) | [`Operations/`](Operations/) | ✅ Included |
| Hazard rasters (22 GeoTIFF) | [`Hazard/`](Hazard/) | ❌ **Pending** |
| Results of the reference run | [`Reference_results/`](Reference_results/) | ✅ Included |
| ArcGIS Pro project (`.aprx`) | — | ❌ Pending (the original was not portable; see [Limitations](#known-limitations-of-the-case)) |

## Folder structure

The folder follows the data organization recommended by the documentation ([Data Organization](https://joseafitoria0704.github.io/BSA2-Tool/en/getting-started/organizacion-datos/)).

```
ejemplos/costa-rica/
├── Exposure/                      exposure layers (shapefiles, WGS 84)
│   ├── crc_RVN_WGS84.shp          national road network (1,453 segments)     → parameter 0
│   ├── crc_rvn_puentes2.shp       bridges (1,562)                            → parameter 1
│   ├── cr_tuneles_rvn_WGS84.shp   tunnels (1)                                → parameter 2
│   └── crc_rvn_drenaje2.shp       drainage (371)                             → parameter 3
├── Hazard/                        hazard rasters (PENDING, see its README)
├── Vulnerability/
│   └── FVU_BSA_V3.csv             60 vulnerability curves                    → parameter 10
├── Operations/
│   └── OCO_BSA_CR_V1.csv          operating costs and occupancy (T9–T15)     → parameter 11
└── Reference_results/
    ├── BSA2_CostaRica_results_20260413_172736.gpkg   results of the reference run
    └── run_config_20260413_172736.loc                parameters of that run
```

## Using the example: the workflow

The full workflow is explained in the [User Guide](https://joseafitoria0704.github.io/BSA2-Tool/en/guia-usuario/flujo-trabajo/). This is how it applies to this case:

| Workflow stage | In the Costa Rica case |
| --- | --- |
| 1. Collect and standardize the data | The inputs are in `Exposure/`, `Hazard/`, `Vulnerability/` and `Operations/` |
| 2. Prepare the exposure layers | Each layer already has its required attributes (`ID_TRAMO`, `vul_f`, `vul_eq`, `rep_cost_k`/`rep_cost`, traffic `T9`–`T15` on roads) |
| 3. GDP per capita per day | `45249.62` (see the [note on units](#known-limitations-of-the-case)) |
| 4. Segment length | `30` m |
| 5. Run the BSA2 toolbox | See the steps below |
| 6. Review the results | Compare with `Reference_results/` |

### Steps to run it

Requires ArcGIS Pro 3.2 or later with the **Spatial Analyst** extension (see the [installation guide](../../README-EN.md#installation-guide)).

1. **Prepare a working folder.** Copy this folder (`ejemplos/costa-rica/`) to your computer, for example to `C:\BSA2_CostaRica\`.
2. **Copy the toolbox next to the data.** Copy `toolbox/BSA2.atbx` and `toolbox/BSA2.py` into that working folder. The tool creates its outputs (`BSA2.gdb` and `Loc/`) in the folder where `BSA2.py` is located, and both files must be in the same folder.
3. **Add the hazard rasters** to `Hazard/` (pending; see [`Hazard/README.md`](Hazard/README.md)).
4. **Create an ArcGIS Pro project** in the working folder, add the `BSA2.atbx` toolbox from the *Catalog* pane and open the **BSA2** tool.
5. **Enter the parameters** from the table below and run.
6. **Compare** the new layers (`roads_results_<date>`, etc.) with those in `Reference_results/`.

### Parameters of the reference run

| # | Parameter | Value |
| --- | --- | --- |
| 0 | Road network (`roads_path`) | `Exposure/crc_RVN_WGS84.shp` |
| 1 | Bridges (`bridge_path`) | `Exposure/crc_rvn_puentes2.shp` |
| 2 | Tunnels (`tunnel_path`) | `Exposure/cr_tuneles_rvn_WGS84.shp` |
| 3 | Drainage (`draina_path`) | `Exposure/crc_rvn_drenaje2.shp` |
| 4 | Riverine flood (`fl_rive_raw`) | `Hazard/ri_h_CR_{10,20,50,75,100,200,500}.tif` (7 files) |
| 5 | Coastal flood (`fl_coas_raw`) | `Hazard/c_h_CR_{1,2,5,10,25,50,100,250,500,1000}.tif` (10 files) |
| 6 | Tsunami (`ts_coas_raw`) | *(empty)* |
| 7 | Earthquake (`earthqu_raw`) | `Hazard/EQ_CR_PGA_{100,225,475,2475,4975}.tif` (5 files) |
| 8 | Liquefaction (`liquefa_raw`) | *(empty)* |
| 9 | Climate change (`mod_tp_poly`) | *(empty)* |
| 10 | Vulnerability (`vulner_data`) | `Vulnerability/FVU_BSA_V3.csv` |
| 11 | Operating costs (`operat_data`) | `Operations/OCO_BSA_CR_V1.csv` |
| 12 | GDP per capita per day (`gdppca_doub`) | `45249.62` |
| 13 | Segment length (`road_segme`) | `30` |

These are the same values recorded in [`run_config_20260413_172736.loc`](Reference_results/run_config_20260413_172736.loc).

## Reference results

[`BSA2_CostaRica_results_20260413_172736.gpkg`](Reference_results/BSA2_CostaRica_results_20260413_172736.gpkg) is a GeoPackage (it opens in ArcGIS Pro and QGIS) with the four layers generated by the run of 13 April 2026:

| Layer | Records |
| --- | --- |
| `roads_results_20260413_172736` | 1,453 |
| `bridges_results_20260413_172736` | 1,562 |
| `tunnels_results_20260413_172736` | 1 |
| `drainage_results_20260413_172736` | 371 |

Values to validate your own run (road network; magnitudes in the monetary unit of the run):

| Field | Sum |
| --- | --- |
| `DAE_river` | 1.885 × 10¹⁰ |
| `DAE_coast` | 1.213 × 10⁷ |
| `DAE_earthquake` | 1.951 × 10¹⁰ |
| **`DAE_total`** | **3.838 × 10¹⁰** |
| `PAE_total` | 6.543 × 10⁹ |
| **`Priority`** (`DAE_total` + `PAE_total`) | **4.492 × 10¹⁰** |

Highest-`Priority` segments: National Route 34 (`ID_TRAMO` 755), National Route 2 (1197), National Route 245 (716), National Route 36 (678) and National Route 36 (250).

For the components, the sum of `DAE` is 1.426 × 10⁹ for bridges, 1.833 × 10⁶ for the tunnel and 4.065 × 10⁸ for drainage.

## Known limitations of the case

These limitations are documented here so that they are not mistaken for expected behavior of the tool. They are pending review by the project team.

1. **Components are not linked to the roads.** The `ID_TRAMO` of bridges, tunnels and drainage (10001 to 70740) does not match any of the road network's (0 to 1472). As a result, in the reference results `DAE_bridge`, `DAE_tunnel` and `DAE_drainage` are 0 on every road, and the components' `PAE_total` is 0. The road network's `DAE_total` only includes the segments' own damage.
2. **Monetary unit to be confirmed.** The input data sheet and the documentation express costs in USD, but the magnitudes in this case (for example `rep_cost_k` with a median of 3.8 × 10⁸ and operating costs `COV` of 137 to 246 per km) only make sense in local currency (colones). The same applies to GDP per capita per day (`45249.62`). Until this is confirmed, treat the figures as "monetary units of the run".
3. **Duplicate segment.** `ID_TRAMO` 1278 appears in two records of the road network.
4. **ArcGIS Pro project missing.** The original `CostaRica.aprx` contained a Dominican Republic map and a Costa Rica map that pointed to the authors' local folders (thousands of absolute paths) and to results of other runs; for that reason it was removed. It must be replaced by a new project with relative paths.

## Origin of the files

The files come from the `BSA2_CostaRica.zip` package in the original documentation repository (`andresabarca-atlas/bsa-docs`), which is kept in the Git history (for example, in the `v0.3.0` tag). To organize them, the following was done:

- **`Exposure/`**: the package did not include the input layers, only the results layers. They were **rebuilt** from them, keeping the original geometry and attributes and removing the fields computed by the tool (`damage_*`, `loss_*`, `DAE*`, `PAE*`, `Priority`). Numeric attributes and geometries were verified to match the original geodatabase exactly; only one text value made of a single blank space became empty because of a DBF format limitation. The names match those in the `.loc` file.
- **`Reference_results/`**: the four results layers were converted from the geodatabase (`BSA2.gdb`) to a GeoPackage, without changing values. The automatic `Shape_Length` field, which was in degrees, was omitted. The original geodatabase also carried a processing history with the authors' personal paths, which is not kept.
- **`Vulnerability/` and `Operations/`**: the original CSV files, unchanged.
- **`run_config_20260413_172736.loc`**: the run log with the authors' local paths replaced by file names.
