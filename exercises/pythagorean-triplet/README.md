# Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, {a, b, c}, for
which,

```text
a**2 + b**2 = c**2
```

For example,

```text
3**2 + 4**2 = 9 + 16 = 25 = 5**2.
```

The test cases assume two functions are defined:

  - `triplets_in_range(min, max)`
      Compute all pythagorean triplets `(a,b,c)` with `min <= a,b,c <= max`

  - `primitive_triplets(b)`
      Find all primitive pythagorean triplets having `b` as one of their
      components

      Args:
         `b` - an integer divisible by 4 (see explanantion below)

Note that in the latter function the components other than the argument can
be quite large.

A primitive pythagorean triplet has its 3 componentes coprime. So, `(3,4,5)` is
a primitive pythagorean triplet since 3,4 and 5 don't have a common factor.
On the other hand, `(6,8,10)`, although a pythagorean triplet, is not primitive
since 2 divides all three components.

A method for finding all primitive pythagorean triplet is given in
([wikipedia](http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple)).
The triplet `a=(m^2-n^2)`, `b=2*m*n` and `c=(m^2+n^2)`, where `m` and `n` are coprime and
`m-n>0` is odd, generate a primitive triplet. Note that this implies that `b` has
to be divisible by 4 and `a` and `c` are odd. Also note that we may have either
`a>b` or `b>a`.

The function `primitive_triplets` should then use the formula above with `b` set
to its argument and find all possible pairs `(m,n)` such that `m>n`, `m-n` is odd,
`b=2*m*n` and `m` and `n` are coprime.

## Exception messages

Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to
indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. Not
every exercise will require you to raise an exception, but for those that do, the tests will only pass if you include
a message.

To raise a message with an exception, just write it as an argument to the exception type. For example, instead of
`raise Exception`, you should write:

```python
raise Exception("Meaningful message indicating the source of the error")
```

## Running the tests

To run the tests, run the appropriate command below ([why they are different](https://github.com/pytest-dev/pytest/issues/1629#issue-161422224)):

- Python 2.7: `py.test pythagorean_triplet_test.py`
- Python 3.4+: `pytest pythagorean_triplet_test.py`

Alternatively, you can tell Python to run the pytest module (allowing the same command to be used regardless of Python version):
`python -m pytest pythagorean_triplet_test.py`

### Common `pytest` options

- `-v` : enable verbose output
- `-x` : stop running tests on first failure
- `--ff` : run failures from previous test before running other test cases

For other options, see `python -m pytest -h`

## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `$EXERCISM_WORKSPACE/python/pythagorean-triplet` directory.

You can find your Exercism workspace by running `exercism debug` and looking for the line that starts with `Workspace`.

For more detailed information about running tests, code style and linting,
please see [Running the Tests](http://exercism.io/tracks/python/tests).

## Source

Problem 9 at Project Euler [http://projecteuler.net/problem=9](http://projecteuler.net/problem=9)

## Submitting Incomplete Solutions

It's possible to submit an incomplete solution so you can see how others have completed the exercise.
