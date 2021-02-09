## Notes regarding the implementation of `smallest` and `largest`:

Both functions must take two keyword arguments:
- `max_factor`: int
- `min_factor`: int, default 0

Their return value must be a tuple (value, factors) where value is the
palindrome itself, and factors is an iterable containing both factors of the
palindrome in arbitrary order.