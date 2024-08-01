# Performance

All functions were tested on three inputs, a short string from the exercise tests plus two scientific papers in $\LaTeX$ format.

Python reported these string lengths:

```
    short: 84
    mars_moons: 34836
    galaxy_cnn: 31468
```

A total of 9 community solutions were tested: 5 variants of stack-match and 4 of repeated-substitution.
Full details are in the [benchmark code][benchmark-code], including URLs for the downloaded papers.
Results are summarized in the table below, with all times in seconds:


|                        |    short |   mars_moons |   galaxy_cnn |
|:-----------------------|:--------:|:------------:|:------------:|
| stack_match4           | 1.77e-06 |     5.92e-04 |     5.18e-04 |
| stack_match2           | 1.71e-06 |     7.38e-04 |     6.64e-04 |
| stack_match3           | 1.79e-06 |     7.72e-04 |     6.95e-04 |
| stack_match5           | 1.70e-06 |     7.79e-04 |     6.97e-04 |
| stack_match1           | 5.64e-06 |     21.9e-04 |     39.7e-04 |
| repeated_substitution1 | 1.20e-06 |     3.50e-04 |     3.06e-04 |
| repeated_substitution2 | 1.86e-06 |     3.58e-04 |     3.15e-04 |
| repeated_substitution3 | 4.27e-06 |     14.0e-04 |     12.5e-04 |
| repeated_substitution4 | 4.96e-06 |     14.9e-04 |     13.5e-04 |


Overall, most of these solutions had fairly similar performance, and runtime scaled similarly with input length.

There is certainly no evidence for either class of solutions being systematically better than the other.

The slowest was `stack_match1`, which did a lot of lookups in dictionary.
keys and values. Searching instead in sets or strings gave a small but perhaps useful improvement.

Among the repeated-substitution solutions, the first two used standard Python string operations, running slightly faster than the second two which use regular expressions.


[benchmark-code]: https://github.com/exercism/python/blob/main/exercises/practice/matching-brackets/.articles/performance/code/Benchmark.py
