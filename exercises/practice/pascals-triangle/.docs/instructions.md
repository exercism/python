# Instructions

Your task is to output the first N rows of Pascal's triangle.

[Pascal's triangle][wikipedia] is a triangular array of positive integers.

In Pascal's triangle, the number of values in a row is equal to its row number (which starts at one).
Therefore, the first row has one value, the second row has two values, and so on.

The first (topmost) row has a single value: `1`.
Subsequent rows' values are computed by adding the numbers directly to the right and left of the current position in the previous row.

If the previous row does _not_ have a value to the left or right of the current position (which only happens for the leftmost and rightmost positions), treat that position's value as zero (effectively "ignoring" it in the summation).

## Example

Let's look at the first 5 rows of Pascal's Triangle:

```text
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

The topmost row has one value, which is `1`.

The leftmost and rightmost values have only one preceding position to consider, which is the position to its right respectively to its left.
With the topmost value being `1`, it follows from this that all the leftmost and rightmost values are also `1`.

The other values all have two positions to consider.
For example, the fifth row's (`1 4 6 4 1`) middle value is `6`, as the values to its left and right in the preceding row are `3` and `3`:

[wikipedia]: https://en.wikipedia.org/wiki/Pascal%27s_triangle
