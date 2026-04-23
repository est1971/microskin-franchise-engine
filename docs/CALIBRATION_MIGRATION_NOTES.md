# Calibration and Spreadsheet Migration Notes

The original HTML calculator is treated as a prototype and concept source, not as production logic.

## Preserved concepts

- territory status colors
- territory-aware commercial presentation
- country, city, territory navigation
- premium clinical aesthetic

## Replaced concepts

- radial slicing
- population-led territory sizing
- hardcoded single-core metro assumptions
- fixed polygons detached from opportunity clusters

## Workbook importer

`scripts/import_calibration.py` is the migration entry point for:

- `Microskin_India_Territory_Analysis_v5.xlsx`
- `Microskin_USA_Territory_Analysis_v3.xlsx`

When the files are not present, the importer records the absence and keeps the runtime on transparent demo calibration instead of silently fabricating imported assumptions.

