# Performance

The [Approaches page][approaches-page] discusses three ways to approach this exercise, with very different performance.
Adding in some ways to vary the coding details, we will discuss 5 implementations.


## Cubic-time code

We need to find sets of three variables meeting some criteria, so the most naive approach is to scan over the variables in nested loops, with a test for the criteria in the innermost loop.

This is simple and clear but _very_ slow, and the run-time increases proportional to `n ** 3`.
When tested, `n = 1_000` took about 8 seconds to complete, and we can extrapolate that `n = 100_000` would take nearly 3 months.

This is impractical!


## Quadratic-time code

For `cubic`, the loops were nested 3-deep.
Not coincidentally, the run time scaled as the third power of `n`.

As we know that `a + b + c == n`, it is fairly obvious that we only need to scan through two variables.
The third on can be calculated, for example `c = n - a - b`.

Nesting loops 2-deep means, in this case, that the run  time is:
- Always faster than cubic.
- Increases as `n ** 2`, so it is called quadratic-time.

In practice, this means that a `n = 30_000` test ran in a few seconds.
However, `n = 100_000` would take several minutes per repetition (and we want to average several runs), so this was excluded from performance testing.

Tightening up the loop's upper and lower bounds can achieve a small speedup. Results are shown below for `quad_loose` and `quad_tight`, respectively.

However, the difference is only 3- to 4-fold and scaling is still quadratic, so large-`n` testing is still impractical.

As a general principle: if run time varies as `a * n ** x`, this sort of coding trickery only changes the proportionality constant `a`.

The exponent `x` is ***very much*** more important, and only a better algorithm can change it.


## Linear-time code

The approaches discussed above have a strictly programming focus.
To take the next step, we need to look at the problem as mathematicians &mdash; or as programmers who read what real mathematicians have already published.

The [Approaches page][approaches-page] discusses two implementations with code that looks very different but uses a similar underlying algorithm.
These are shown in the analyses as `linear_loop` and `linear_comp` (the latter using generator expressions and list comprehensions).
Performance is similarly impressive in both cases.


## Measured timings

The five code implementations were [benchmarked][benchmark-code], using appropriate values for the upper limit of `n` and number of runs too average over, to keep the total testing time reasonable.

Numerical results are tabulated below.

|             |  n = 12 |      30 |     100 |     300 |   1_000 |   3_000 |  10_000 |  30_000 | 100_000 |
|:------------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| cubic       | 1.2e-05 | 1.8e-04 | 7.1e-03 | 1.9e-01 | 7.6e+00 |         |         |         |         |
| quad_loose  | 4.7e-06 | 2.5e-05 | 2.7e-04 | 2.3e-03 | 2.7e-02 | 2.5e-01 | 2.8e+00 | 2.5e+01 |         |
| quad_tight  | 1.1e-06 | 5.2e-06 | 5.9e-05 | 5.9e-04 | 7.3e-03 | 7.0e-02 | 7.9e-01 | 7.3e+00 |         |
| linear_loop | 4.4e-07 | 5.7e-07 | 1.1e-06 | 3.4e-06 | 1.1e-05 | 3.1e-05 | 1.0e-04 | 3.1e-04 | 1.2e-03 |
| linear_comp | 5.3e-07 | 1.1e-06 | 2.8e-06 | 9.0e-06 | 2.8e-05 | 8.3e-05 | 2.8e-04 | 8.1e-04 | 3.1e-03 |

Note the missing values, which also affect the graphical representation.
Also, note the logarithmic y-axis in the graph output when running the Benchmark.py script.
These run times vary over more than 7 orders of magnitude!


## Testing algorithmic complexity

We have discussed these solutions as `cubic`, `quadratic` or `linear`.
Do the experimental data support this?

For a [power law][power-law] relationship, we have a run time `t` given by `t = a * n**x`, where `a` is a proportionality constant an `x` is the power.

Taking logs of both sides, `log(t) = x * log(n) + constant.`

Plots of `log(t)` against `log(n)` will be a straight line with slope equal to the power `x`, which you can produce by running the Benchmark.py code.

Encouragingly, these are all straight lines for larger values of `n`, as we expected.

Linear least-squares fits to each line gave these slope values:

| method      |  slope |
|:------------|-------:|
| cubic       |   3.01 |
| quad_loose  |   2.00 |
| quad_tight  |   2.03 |
| linear_loop |   0.90 |
| linear_comp |   0.96 |

Cubic, quadratic and linear algorithms have theoretical slopes of 3, 2, and 1 respectively, so the experimental values are pretty close.

Algorithmic complexity is an analysis of the high-`n` limit, so including all the points (done for simplicity) is perhaps inappropriate.
For the linear-time solutions, there is noticeable curvature at the low end, where some fixed overhead made a non-negligible contribution to run time.
Removing these points and fitting only the linear portion would give a slope closer to 1.0.


[approaches-page]: https://exercism.org/tracks/python/exercises/pythagorean-triplet/approaches
[benchmark-code]: https://exercism.org/tracks/python/exercises/pythagorean-triplet/
[power-law]: https://en.wikipedia.org/wiki/Power_law
