# Caso de referencia: Costa Rica

**Español** | [English](README-EN.md)

Este es el **ejemplo de referencia del flujo de trabajo del BSA 2.0**. Reúne los insumos y los resultados de una corrida real de la herramienta sobre la red vial nacional de Costa Rica, para que cualquier persona pueda ver cómo se organizan los datos, qué parámetros se ingresan y qué resultados se obtienen.

> ⚠️ **Estado del ejemplo: incompleto.** Faltan los 22 rásters de amenaza (carpeta [`Hazard/`](Hazard/)), por lo que **todavía no puede reproducirse la corrida**. El resto de los insumos y los resultados de referencia sí están. Ver [Estado del ejemplo](#estado-del-ejemplo) y [Limitaciones conocidas](#limitaciones-conocidas-del-caso).

## Estado del ejemplo

| Elemento | Carpeta | Estado |
| --- | --- | --- |
| Capas de exposición (vías, puentes, túneles, drenajes) | [`Exposure/`](Exposure/) | ✅ Incluidas (reconstruidas, ver [Origen](#origen-de-los-archivos)) |
| Funciones de vulnerabilidad (FVU) | [`Vulnerability/`](Vulnerability/) | ✅ Incluida |
| Costos de operación vehicular (OCO) | [`Operations/`](Operations/) | ✅ Incluida |
| Rásters de amenaza (22 GeoTIFF) | [`Hazard/`](Hazard/) | ❌ **Pendientes** |
| Resultados de la corrida de referencia | [`Reference_results/`](Reference_results/) | ✅ Incluidos |
| Proyecto de ArcGIS Pro (`.aprx`) | — | ❌ Pendiente (el original no era portable; ver [Limitaciones](#limitaciones-conocidas-del-caso)) |

## Estructura de la carpeta

La carpeta sigue la organización de datos que recomienda la documentación ([Organización de datos](https://joseafitoria0704.github.io/BSA2-Tool/getting-started/organizacion-datos/)).

```
ejemplos/costa-rica/
├── Exposure/                      capas de exposición (shapefiles, WGS 84)
│   ├── crc_RVN_WGS84.shp          red vial nacional (1 453 tramos)           → parámetro 0
│   ├── crc_rvn_puentes2.shp       puentes (1 562)                            → parámetro 1
│   ├── cr_tuneles_rvn_WGS84.shp   túneles (1)                                → parámetro 2
│   └── crc_rvn_drenaje2.shp       drenajes (371)                             → parámetro 3
├── Hazard/                        rásters de amenaza (PENDIENTE, ver su README)
├── Vulnerability/
│   └── FVU_BSA_V3.csv             60 curvas de vulnerabilidad                → parámetro 10
├── Operations/
│   └── OCO_BSA_CR_V1.csv          costos de operación y ocupación (T9–T15)   → parámetro 11
└── Reference_results/
    ├── BSA2_CostaRica_results_20260413_172736.gpkg   resultados de la corrida de referencia
    └── run_config_20260413_172736.loc                parámetros de esa corrida
```

## Cómo usar el ejemplo: el flujo de trabajo

El flujo completo está explicado en la [Guía de Usuario](https://joseafitoria0704.github.io/BSA2-Tool/guia-usuario/flujo-trabajo/). Así se aplica en este caso:

| Etapa del flujo | En el caso de Costa Rica |
| --- | --- |
| 1. Recopilar y estandarizar los datos | Los insumos están en `Exposure/`, `Hazard/`, `Vulnerability/` y `Operations/` |
| 2. Preparar las capas de exposición | Cada capa ya trae sus atributos requeridos (`ID_TRAMO`, `vul_f`, `vul_eq`, `rep_cost_k`/`rep_cost`, TPDA `T9`–`T15` en las vías) |
| 3. PIB per cápita por día | `45249.62` (ver la [nota sobre unidades](#limitaciones-conocidas-del-caso)) |
| 4. Longitud de segmento | `30` m |
| 5. Ejecutar el toolbox BSA2 | Ver los pasos de abajo |
| 6. Revisar los resultados | Comparar con `Reference_results/` |

### Pasos para ejecutarlo

Requiere ArcGIS Pro 3.2 o superior con la extensión **Spatial Analyst** (ver [Guía de instalación](../../README.md#guía-de-instalación)).

1. **Prepare una carpeta de trabajo.** Copie esta carpeta (`ejemplos/costa-rica/`) a su equipo, por ejemplo a `C:\BSA2_CostaRica\`.
2. **Copie el toolbox junto a los datos.** Copie `toolbox/BSA2.atbx` y `toolbox/BSA2.py` a esa carpeta de trabajo. La herramienta crea sus resultados (`BSA2.gdb` y `Loc/`) en la carpeta donde está `BSA2.py`, y los dos archivos deben estar en la misma carpeta.
3. **Agregue los rásters** de amenaza a `Hazard/` (pendiente de aportar; ver [`Hazard/README.md`](Hazard/README.md)).
4. **Cree un proyecto** de ArcGIS Pro en la carpeta de trabajo, agregue el toolbox `BSA2.atbx` desde el panel *Catalog* y abra la herramienta **BSA2**.
5. **Ingrese los parámetros** de la tabla siguiente y ejecute.
6. **Compare** las capas nuevas (`roads_results_<fecha>`, etc.) con las de `Reference_results/`.

### Parámetros de la corrida de referencia

| # | Parámetro | Valor |
| --- | --- | --- |
| 0 | Red vial (`roads_path`) | `Exposure/crc_RVN_WGS84.shp` |
| 1 | Puentes (`bridge_path`) | `Exposure/crc_rvn_puentes2.shp` |
| 2 | Túneles (`tunnel_path`) | `Exposure/cr_tuneles_rvn_WGS84.shp` |
| 3 | Drenajes (`draina_path`) | `Exposure/crc_rvn_drenaje2.shp` |
| 4 | Inundación fluvial (`fl_rive_raw`) | `Hazard/ri_h_CR_{10,20,50,75,100,200,500}.tif` (7 archivos) |
| 5 | Inundación costera (`fl_coas_raw`) | `Hazard/c_h_CR_{1,2,5,10,25,50,100,250,500,1000}.tif` (10 archivos) |
| 6 | Tsunami (`ts_coas_raw`) | *(vacío)* |
| 7 | Sismo (`earthqu_raw`) | `Hazard/EQ_CR_PGA_{100,225,475,2475,4975}.tif` (5 archivos) |
| 8 | Licuefacción (`liquefa_raw`) | *(vacío)* |
| 9 | Cambio climático (`mod_tp_poly`) | *(vacío)* |
| 10 | Vulnerabilidad (`vulner_data`) | `Vulnerability/FVU_BSA_V3.csv` |
| 11 | Costos de operación (`operat_data`) | `Operations/OCO_BSA_CR_V1.csv` |
| 12 | PIB per cápita por día (`gdppca_doub`) | `45249.62` |
| 13 | Longitud de segmento (`road_segme`) | `30` |

Son los mismos valores que registra [`run_config_20260413_172736.loc`](Reference_results/run_config_20260413_172736.loc).

## Resultados de referencia

[`BSA2_CostaRica_results_20260413_172736.gpkg`](Reference_results/BSA2_CostaRica_results_20260413_172736.gpkg) es un GeoPackage (se abre en ArcGIS Pro y en QGIS) con las cuatro capas que generó la corrida del 13 de abril de 2026:

| Capa | Registros |
| --- | --- |
| `roads_results_20260413_172736` | 1 453 |
| `bridges_results_20260413_172736` | 1 562 |
| `tunnels_results_20260413_172736` | 1 |
| `drainage_results_20260413_172736` | 371 |

Valores para validar una corrida propia (red vial; magnitudes en la unidad monetaria de la corrida):

| Campo | Suma |
| --- | --- |
| `DAE_river` | 1,885 × 10¹⁰ |
| `DAE_coast` | 1,213 × 10⁷ |
| `DAE_earthquake` | 1,951 × 10¹⁰ |
| **`DAE_total`** | **3,838 × 10¹⁰** |
| `PAE_total` | 6,543 × 10⁹ |
| **`Priority`** (`DAE_total` + `PAE_total`) | **4,492 × 10¹⁰** |

Tramos de mayor `Priority`: Ruta Nacional 34 (`ID_TRAMO` 755), Ruta Nacional 2 (1197), Ruta Nacional 245 (716), Ruta Nacional 36 (678) y Ruta Nacional 36 (250).

En los componentes, la suma del `DAE` es 1,426 × 10⁹ en puentes, 1,833 × 10⁶ en el túnel y 4,065 × 10⁸ en drenajes.

## Limitaciones conocidas del caso

Estas limitaciones están documentadas aquí para que no se tomen como comportamiento esperado de la herramienta. Están pendientes de revisión por el equipo del proyecto.

1. **Los componentes no se vinculan con las vías.** El `ID_TRAMO` de puentes, túneles y drenajes (de 10001 a 70740) no coincide con ninguno de los de la red vial (de 0 a 1472). Por eso, en los resultados de referencia `DAE_bridge`, `DAE_tunnel` y `DAE_drainage` valen 0 en todas las vías, y la `PAE_total` de los componentes vale 0. Los `DAE_total` de la red vial incluyen solo el daño propio de los tramos.
2. **Unidad monetaria por confirmar.** La ficha de datos de entrada y la documentación expresan los costos en USD, pero las magnitudes de este caso (por ejemplo, `rep_cost_k` con mediana de 3,8 × 10⁸ y costos de operación `COV` de 137 a 246 por km) solo tienen sentido en moneda local (colones). Lo mismo aplica al PIB per cápita por día (`45249.62`). Hasta que se confirme, trate las cifras como "unidades monetarias de la corrida".
3. **Tramo duplicado.** El `ID_TRAMO` 1278 aparece en dos registros de la red vial.
4. **Falta el proyecto de ArcGIS Pro.** El `CostaRica.aprx` original contenía un mapa de República Dominicana y un mapa de Costa Rica que apuntaban a carpetas locales de los autores (miles de rutas absolutas) y a resultados de otras corridas; por eso se retiró. Debe sustituirse por un proyecto nuevo con rutas relativas.

## Origen de los archivos

Los archivos provienen del paquete `BSA2_CostaRica.zip` del repositorio original de documentación (`andresabarca-atlas/bsa-docs`), que se conserva en el historial de Git (por ejemplo, en la etiqueta `v0.3.0`). Para ordenarlos se hizo lo siguiente:

- **`Exposure/`**: el paquete no incluía las capas de entrada, sino solo las de resultados. Se **reconstruyeron** a partir de ellas, conservando la geometría y los atributos originales y quitando los campos que calcula la herramienta (`damage_*`, `loss_*`, `DAE*`, `PAE*`, `Priority`). Se verificó que los atributos numéricos y las geometrías coinciden exactamente con los de la geodatabase original; solo un valor de texto formado por un espacio en blanco quedó vacío por la limitación del formato DBF. Los nombres coinciden con los del archivo `.loc`.
- **`Reference_results/`**: las cuatro capas de resultados se pasaron de la geodatabase (`BSA2.gdb`) a un GeoPackage, sin cambiar valores. Se omitió el campo automático `Shape_Length`, que estaba en grados. La geodatabase original traía además el historial de procesamiento con rutas personales de los autores, que no se conserva.
- **`Vulnerability/` y `Operations/`**: los CSV originales, sin cambios.
- **`run_config_20260413_172736.loc`**: el registro de la corrida con las rutas locales de los autores reemplazadas por nombres de archivo.
