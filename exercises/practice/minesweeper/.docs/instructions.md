# Instructions

Your task is to add the mine counts to empty squares in a completed Minesweeper board.
The board itself is a rectangle composed of squares that are either empty (`' '`) or a mine (`'*'`).

For each empty square, count the number of mines adjacent to it (horizontally, vertically, diagonally).
If the empty square has no adjacent mines, leave it empty.
Otherwise replace it with the adjacent mines count.

For example, you may receive a 5 x 4 board like this (empty spaces are represented here with the '·' character for display on screen):

```text
·*·*·
··*··
··*··
·····
```

Which your code should transform into this:

```text
1*3*1
13*31
·2*2·
·111·
```
