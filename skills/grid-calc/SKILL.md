---
name: grid-calc
description: Convert lat/lon to Maidenhead grid, decode a grid, or distance and bearing between two grids.
user-invocable: true
---

# Grid calc

Script: {baseDir}/scripts/grid.py

Lat/lon to grid:
python3 {baseDir}/scripts/grid.py enc 35.08 -106.65

Grid to approx center:
python3 {baseDir}/scripts/grid.py dec DM65qe

Distance and bearing:
python3 {baseDir}/scripts/grid.py path DM65 EM00

Use only the numbers or grids the operator gave. Do not invent a grid. West longitude is negative.
