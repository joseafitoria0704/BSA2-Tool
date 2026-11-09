# Cómo contribuir al BSA 2.0

## Por qué contribuir

El **Blue Spot Analysis 2.0 (BSA 2.0)** es una herramienta digital del **Banco
Interamericano de Desarrollo (BID)**, en línea con la iniciativa
[Código para el Desarrollo](https://knowledge.iadb.org/es/codigo-para-el-desarrollo).
En el BID entendemos el código como un bien de conocimiento que debe estar abierto a
los ciudadanos y gobiernos de la región. Por eso animamos a quien mejore esta
herramienta a devolver sus aportes al bien público. Cada contribución quedará
reconocida en la lista de atribuciones del `README.md`.

## Qué tipo de contribuciones son bienvenidas

- Nuevas funcionalidades del motor de cálculo (`toolbox/BSA2.py`), por ejemplo nuevas
  amenazas, componentes de exposición o funciones de vulnerabilidad.
- Mejoras de compatibilidad con nuevas versiones de ArcGIS Pro o `arcpy`.
- Corrección de errores.
- Mejoras de la documentación (`docs/`), en español o en inglés.

## Pasos para contribuir

1. Haga un *fork* del repositorio y cree una rama descriptiva (por ejemplo,
   `feat/amenaza-deslizamientos` o `docs/corrige-glosario`).
2. Desarrolle el cambio. Si modifica el motor, valide la corrida con el caso de
   referencia de `ejemplos/costa-rica/`.
3. Si modifica la documentación, compruebe que el sitio se construye sin errores:

    ```bash
    pip install -r requirements-docs.txt
    mkdocs build --strict
    ```

4. Abra un *pull request* que describa en detalle los cambios propuestos e incluya su
   nombre de usuario y organización para añadirlo a las atribuciones.

Para reportar un fallo, abra un *issue* que indique la versión de ArcGIS Pro, el
sistema operativo, los parámetros usados y el mensaje de error.

Si no ha contribuido código, pero la herramienta le ha sido útil, nos encantaría
conocer su experiencia: cuéntenosla en un *issue* o escríbanos a
[code@iadb.org](mailto:code@iadb.org).

## Guía de estilo

### Código (`toolbox/BSA2.py`)

- Python compatible con el entorno `arcgispro-py3` de ArcGIS Pro. No agregue
  dependencias externas sin documentarlas en el `README.md`.
- Mantenga el orden de los parámetros de `arcpy.GetParameterAsText()`, porque está
  vinculado a la definición del toolbox `toolbox/BSA2.atbx`. Si agrega o cambia un
  parámetro, actualice también el toolbox y la página `docs/getting-started/interfaz.md`.
- El archivo `BSA2.atbx` enlaza el script por ruta relativa (`BSA2.py` en la misma
  carpeta), así que no separe esos dos archivos.
- Documente cada función con un *docstring* breve.

### Documentación (`docs/`)

- El sitio usa [MkDocs](https://www.mkdocs.org/) con
  [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) y es bilingüe. El
  idioma base (español) va en `pagina.md` y la traducción al inglés en `pagina.en.md`.
  Todo cambio debe reflejarse en ambos idiomas.
- Tono técnico pero accesible. Hay dos audiencias: usuarios técnicos (especialistas en
  riesgo, unidades SIG, consultores) y usuarios estratégicos (ministerios y tomadores de
  decisión).
- Use las *admonitions* de Material (`note`, `tip`, `warning`) para destacar ideas,
  fórmulas con `$...$` y `$$...$$` (extensión arithmatex) y diagramas Mermaid cuando
  aporten claridad.
- Guarde las imágenes en `docs/assets/` y cite la fuente de figuras y datos.
- Respete los derechos de autor: no copie bloques largos de los documentos fuente del
  proyecto (Concept Report, presentaciones); redacte con palabras propias.

### Terminología obligatoria

- **DAE** = Daño Anual Esperado = *EAD (Expected Annual Damage)*: daño físico directo a
  la infraestructura.
- **PAE** = Pérdida Anual Esperada = *EAL (Expected Annual Loss)*: pérdida económica por
  interrupción del servicio o del tránsito.
- **PML** = Pérdida Máxima Probable: pérdida asociada a un evento de diseño (por
  ejemplo, Tr = 500 años).
- Distinga siempre **daño** (físico) de **pérdida** (funcional o económica por
  interrupción), como lo hacen el código y el dashboard.
- Amenazas implementadas en la versión actual: inundación fluvial, inundación
  pluvial/costera, sismo, tsunami y licuefacción. Los deslizamientos y huracanes solo se
  mencionan como amenazas previstas para fases futuras.

## Código de conducta

Este proyecto tiene un [Código de Conducta](CODE-OF-CONDUCT.md). Esperamos que todas
las personas que participen lo respeten.

## Limitación de responsabilidades

El BID no será responsable, bajo circunstancia alguna, de daño ni indemnización, moral o patrimonial; directo o indirecto; accesorio o especial; o por vía de consecuencia, previsto o imprevisto, que pudiese surgir:

i. Bajo cualquier teoría de responsabilidad, ya sea por contrato, infracción de derechos de propiedad intelectual, negligencia o bajo cualquier otra teoría; y/o

ii. A raíz del uso de la Herramienta Digital, incluyendo, pero sin limitación de potenciales defectos en la Herramienta Digital, o la pérdida o inexactitud de los datos de cualquier tipo. Lo anterior incluye los gastos o daños asociados a fallas de comunicación y/o fallas de funcionamiento de computadoras, vinculados con la utilización de la Herramienta Digital.
