# Periodic Table
This repo contains two projects:
1. Element SVG generator - if you run `python3 main.py` after installing requirements, Python will generate SVG(s) for every element of the periodic table with respective color and info as detailed in `table.json`.
2. Table visualizer - you can also check out the result after generating SVG(s).
3. Periodic Table API - fetch info about one element, get a element's vector or list all elements in order

[Visit here](https://vortexprime24.github.io/periodic-table/)

## API
### Get all elements
GET `/api/elements`

### Get info about an element
GET `/api/elements/<element_name>`
e.g. `/api/elements/sodium`

### Get vector of a element
GET `/vector/elements/<element_name>`
e.g. `/vector/elements/sodium`