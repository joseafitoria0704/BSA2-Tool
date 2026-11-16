# Caso de ejemplo — Costa Rica

Esta página describe la aplicación del BSA 2.0 al caso de referencia de Costa Rica, que sirve como **ejemplo del flujo de trabajo**: muestra cómo se organizan los insumos, qué parámetros se ingresan y qué resultados se obtienen. Los archivos están en la carpeta [`ejemplos/costa-rica/`](https://github.com/joseafitoria0704/BSA2-Tool/tree/main/ejemplos/costa-rica) del repositorio.

!!! note "Propósito del caso de ejemplo"
    El caso de Costa Rica es un conjunto de datos de referencia que ilustra el funcionamiento completo del toolbox. No representa un análisis oficial del país; su función es pedagógica y de validación técnica.

!!! warning "Estado del ejemplo: incompleto"
    Faltan los 22 rásters de amenaza, por lo que **todavía no puede reproducirse la corrida**. Tampoco incluye un proyecto de ArcGIS Pro, y los resultados de referencia tienen [limitaciones conocidas](#limitaciones-conocidas). El estado actualizado está en el [README del ejemplo](https://github.com/joseafitoria0704/BSA2-Tool/blob/main/ejemplos/costa-rica/README.md).

## Contenido del caso de ejemplo

La carpeta sigue la estructura recomendada en [Organización de datos](../getting-started/organizacion-datos.md):

| Carpeta | Contenido | Estado |
|---------|-----------|--------|
| `Exposure/` | Cuatro shapefiles (WGS 84) con las capas de exposición: vías, puentes, túneles y drenajes. | Incluida |
| `Hazard/` | Los 22 rásters de amenaza (GeoTIFF). | **Pendiente** |
| `Vulnerability/` | `FVU_BSA_V3.csv`: base de funciones de vulnerabilidad (física y de tránsito), con 60 curvas. | Incluida |
| `Operations/` | `OCO_BSA_CR_V1.csv`: costos de operación y ocupación por tipo de vehículo. | Incluida |
| `Reference_results/` | Un GeoPackage con las cuatro capas de resultados de la corrida de referencia y el archivo `.loc` con sus parámetros. | Incluida |

## Insumos utilizados

### Capas de exposición (`Exposure/`)

| Archivo | Tipo | Registros | Descripción |
|---------|------|-----------|-------------|
| `crc_RVN_WGS84.shp` | Polilíneas | 1 453 | Red vial nacional de Costa Rica en datum WGS84. |
| `crc_rvn_puentes2.shp` | Puntos | 1 562 | Inventario de puentes en corredores principales. |
| `cr_tuneles_rvn_WGS84.shp` | Puntos | 1 | Inventario de túneles de la red vial nacional. |
| `crc_rvn_drenaje2.shp` | Puntos | 371 | Elementos de drenaje en la red vial. |

!!! info "Capas reconstruidas"
    El paquete original del caso traía solo las capas de resultados. Las capas de exposición se reconstruyeron a partir de ellas, conservando la geometría y los atributos originales y quitando los campos que calcula la herramienta.

### Mallas de amenaza (`Hazard/`)

La corrida de referencia usó 22 rásters (ver el detalle en el [README de `Hazard/`](https://github.com/joseafitoria0704/BSA2-Tool/blob/main/ejemplos/costa-rica/Hazard/README.md)):

| Amenaza | Archivos | Períodos de retorno (años) |
|---------|----------|----------------------------|
| Inundación fluvial (7) | `ri_h_CR_{Tr}.tif` | 10, 20, 50, 75, 100, 200, 500 |
| Inundación costera/pluvial (10) | `c_h_CR_{Tr}.tif` | 1, 2, 5, 10, 25, 50, 100, 250, 500, 1 000 |
| Sismo, PGA (5) | `EQ_CR_PGA_{Tr}.tif` | 100, 225, 475, 2 475, 4 975 |

Tsunami y licuefacción no estuvieron disponibles para esta corrida.

### Parámetros económicos

| Parámetro | Valor |
|-----------|-------|
| PIB per cápita por día | 45 249.62 (la unidad monetaria está por confirmar; ver [Limitaciones conocidas](#limitaciones-conocidas)) |
| Longitud de segmento | 30 metros |

## Parámetros de la corrida

| # | Parámetro | Valor |
|---|-----------|-------|
| 0 | Red vial | `Exposure/crc_RVN_WGS84.shp` |
| 1 | Puentes | `Exposure/crc_rvn_puentes2.shp` |
| 2 | Túneles | `Exposure/cr_tuneles_rvn_WGS84.shp` |
| 3 | Drenajes | `Exposure/crc_rvn_drenaje2.shp` |
| 4 | Inundación fluvial | 7 rásters de `Hazard/` |
| 5 | Inundación costera | 10 rásters de `Hazard/` |
| 6 | Tsunami | *(vacío)* |
| 7 | Sismo | 5 rásters de `Hazard/` |
| 8 | Licuefacción | *(vacío)* |
| 9 | Cambio climático | *(vacío)* |
| 10 | Vulnerabilidad | `Vulnerability/FVU_BSA_V3.csv` |
| 11 | Costos de operación | `Operations/OCO_BSA_CR_V1.csv` |
| 12 | PIB per cápita por día | `45249.62` |
| 13 | Longitud de segmento | `30` |

## Cómo reproducir el análisis

Requiere ArcGIS Pro 3.2 o superior con la extensión Spatial Analyst (ver [Instalación](../getting-started/instalacion.md)).

1. **Prepare una carpeta de trabajo.** Copie la carpeta `ejemplos/costa-rica/` a su equipo, por ejemplo a `C:\BSA2_CostaRica\`.
2. **Copie el toolbox junto a los datos.** Copie `BSA2.atbx` y `BSA2.py` (carpeta `toolbox/` del repositorio) a la carpeta de trabajo. La herramienta crea sus resultados (`BSA2.gdb` y `Loc/`) donde está `BSA2.py`, y ambos archivos deben estar juntos.
3. **Agregue los rásters** de amenaza a la carpeta `Hazard/`.
4. **Cree un proyecto** de ArcGIS Pro en la carpeta de trabajo, agregue el toolbox `BSA2.atbx` desde el panel *Catalog* y abra la herramienta **BSA2**.
5. **Ingrese los parámetros** de la tabla anterior (ver también [Configuración de una corrida](configuracion-corrida.md#ejemplo-de-configuracion-costa-rica)) y haga clic en **Run**.
6. **Compare** las capas `roads_results_*` nuevas con las de `Reference_results/` para validar la reproducibilidad.

## Resultados de referencia

El GeoPackage `Reference_results/BSA2_CostaRica_results_20260413_172736.gpkg` contiene las cuatro capas que generó la corrida del 13 de abril de 2026. Se abre en ArcGIS Pro y en QGIS.

- **`roads_results_20260413_172736`** — 1 453 tramos con campos de DAE por amenaza (fluvial, costera, sísmica), DAE total, PAE por amenaza, PAE total y `Priority`.
- **`bridges_results_20260413_172736`** — 1 562 puentes con sus propias métricas de DAE, PAE y `Priority`.
- **`tunnels_results_20260413_172736`** — 1 túnel con métricas individuales.
- **`drainage_results_20260413_172736`** — 371 elementos de drenaje con métricas individuales.

Valores para validar una corrida propia (sumas sobre la red vial, en la unidad monetaria de la corrida):

| Campo | Suma |
|-------|------|
| `DAE_river` | 1,885 × 10¹⁰ |
| `DAE_coast` | 1,213 × 10⁷ |
| `DAE_earthquake` | 1,951 × 10¹⁰ |
| **`DAE_total`** | **3,838 × 10¹⁰** |
| `PAE_total` | 6,543 × 10⁹ |
| **`Priority`** | **4,492 × 10¹⁰** |

Los tramos con mayor `Priority` son la Ruta Nacional 34 (`ID_TRAMO` 755), la Ruta Nacional 2 (1197) y la Ruta Nacional 245 (716).

!!! tip "Validación rápida"
    Filtre la capa de resultados por los tramos con mayor `Priority` y compárelos geográficamente con los registros históricos de daños viales del país. Una coincidencia espacial entre tramos de alta `Priority` y zonas históricamente afectadas es un indicador de la coherencia del modelo.

## Limitaciones conocidas

Estas limitaciones del caso están pendientes de revisión por el equipo del proyecto. No son comportamiento esperado de la herramienta.

!!! warning "Los componentes no se vinculan con las vías"
    El `ID_TRAMO` de puentes, túneles y drenajes (de 10001 a 70740) no coincide con ninguno de los de la red vial (de 0 a 1472). Por eso, en los resultados de referencia los campos `DAE_bridge`, `DAE_tunnel` y `DAE_drainage` de las vías valen 0, y la `PAE_total` de los componentes también vale 0. El `DAE_total` de la red vial incluye solo el daño propio de los tramos.

!!! warning "Unidad monetaria por confirmar"
    Esta documentación y la ficha de datos de entrada expresan los costos en USD, pero las magnitudes de este caso (por ejemplo, `rep_cost_k` con mediana de 3,8 × 10⁸ y costos de operación de 137 a 246 por km) solo tienen sentido en moneda local (colones). Hasta que se confirme, interprete las cifras como "unidades monetarias de la corrida".

- El `ID_TRAMO` 1278 aparece en dos registros de la red vial.
- El proyecto de ArcGIS Pro original (`CostaRica.aprx`) no era portable: apuntaba a carpetas locales de los autores. Se retiró y debe sustituirse por un proyecto nuevo.
