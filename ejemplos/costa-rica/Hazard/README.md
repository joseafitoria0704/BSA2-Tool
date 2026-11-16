# Hazard: rásters de amenaza del caso de Costa Rica

> ⚠️ **Esta carpeta está pendiente de completar.** Los 22 rásters que usó la corrida de referencia no forman parte todavía del repositorio. Sin ellos la herramienta no puede ejecutarse con este caso.

*Pending: the 22 hazard rasters used by the reference run are not yet part of the repository. Without them the tool cannot be run with this case.*

## Archivos que deben colocarse aquí

La corrida de referencia ([`../Reference_results/run_config_20260413_172736.loc`](../Reference_results/run_config_20260413_172736.loc)) usó estos GeoTIFF. La herramienta toma el periodo de retorno (Tr) del **último número del nombre del archivo**, por lo que no deben renombrarse.

| Parámetro | Amenaza | Archivos | Tr (años) | Valor del ráster |
| --- | --- | --- | --- | --- |
| 4 · `fl_rive_raw` | Inundación fluvial | `ri_h_CR_10.tif`, `ri_h_CR_20.tif`, `ri_h_CR_50.tif`, `ri_h_CR_75.tif`, `ri_h_CR_100.tif`, `ri_h_CR_200.tif`, `ri_h_CR_500.tif` (7) | 10, 20, 50, 75, 100, 200, 500 | Tirante de agua (m) |
| 5 · `fl_coas_raw` | Inundación costera | `c_h_CR_1.tif`, `c_h_CR_2.tif`, `c_h_CR_5.tif`, `c_h_CR_10.tif`, `c_h_CR_25.tif`, `c_h_CR_50.tif`, `c_h_CR_100.tif`, `c_h_CR_250.tif`, `c_h_CR_500.tif`, `c_h_CR_1000.tif` (10) | 1, 2, 5, 10, 25, 50, 100, 250, 500, 1000 | Tirante de agua (m) |
| 7 · `earthqu_raw` | Sismo | `EQ_CR_PGA_100.tif`, `EQ_CR_PGA_225.tif`, `EQ_CR_PGA_475.tif`, `EQ_CR_PGA_2475.tif`, `EQ_CR_PGA_4975.tif` (5) | 100, 225, 475, 2475, 4975 | Aceleración pico del suelo, PGA |

Los parámetros 6 (tsunami) y 8 (licuefacción) quedaron vacíos en la corrida de referencia, así que no se necesitan rásters para ellos.

## Información que falta documentar

El equipo del proyecto debe aportar, junto con los archivos:

- [ ] Origen de cada conjunto de datos y su licencia de uso. Por los nombres de carpeta del proyecto original, parecen provenir de GloFAS (fluvial), Aqueduct (costera, escenario histórico) y un modelo de amenaza sísmica, pero esto **debe confirmarse**.
- [ ] Resolución espacial y sistema de referencia de los rásters (las capas de `../Exposure/` están en WGS 84, EPSG:4326).
- [ ] Peso total de los archivos. GitHub rechaza archivos de más de 100 MB; si el conjunto es mayor habrá que usar Git LFS, un *release* o un enlace externo.
