# Instructions

After each generation, the cells interact with their eight neighbors, which are cells adjacent horizontally, vertically, or diagonally.

The following rules are applied to each cell:

- Any live cell with two or three live neighbors lives on.
- Any dead cell with exactly three live neighbors becomes a live cell.
- All other cells die or stay dead.

Given a matrix of 1s and 0s (corresponding to live and dead cells), apply the rules to each cell, and return the next generation.
