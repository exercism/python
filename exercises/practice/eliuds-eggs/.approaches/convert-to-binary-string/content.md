# Convert to a Binary String

```python
def egg_count(display_value):
    binary_value = bin(display_value)[2:]
    eggs = 0
    for digit in binary_value:
        eggs += int(digit)
    return eggs
```

This approach uses [`bin()`][bin-built-in] to convert `display_value` to a binary string.
Then, the first two characters of the binary string are removed, as the string has "0b" prefixed before the binary digits.

After the binary digits are obtained, this solution loops across all of them, turning each one into an integer and adding it to `eggs`.
This effectively counts up all of the instances of "1" in the binary string, as 0 and 1 are the only valid binary digits.

Those less familiar with binary may find this approach to be simpler than the others.
However, it does have the added overhead of converting to and from a string.

~~~~exercism/note
There are three other Pythonic ways of obtaining the binary string. One is to use an [`f-string`][f-string]:

```python
binary_value = f"{display_value:b}"
```

Another is to use [`str.format()`][str-format]:

```python
binary_value = "{:b}".format(display_value)
```

Lastly, you could use the [`format()` built-in][format-built-in]:

```python
binary_value = format(display_value, "b")
```

These methods have the added benefit of not producing the "0b" prefix that then needs to removed.
However, some variations of this approach use other ways to get around the prefix.

[format-built-in]: https://docs.python.org/3/library/functions.html#format
[f-string]: https://docs.python.org/3/reference/lexical_analysis.html#f-strings
[str-format]: https://docs.python.org/3/library/stdtypes.html#str.format
~~~~


## Variation #1: Using `sum()` with a Generator Expression

```python
def egg_count(display_value):
    return sum(int(digit) for digit in bin(display_value)[2:])
```

This variant uses a [generator expression][generator-expression] with the `sum()` built-in to collect the digits into the result.
Otherwise, it is the same as the previous version.


## Variation #2: Using `sum()` Without String Slicing

```python
def egg_count(display_value):
    return sum(1 for digit in bin(display_value) if digit == "1")
```

Similar to the previous variant, this one uses `sum()` with a generator expression.
The main difference is that it avoids slicing the binary string by using an `if` clause in the generator expression.


## Variation #3: Using `len()` Instead of `sum()`

```python
def egg_count(display_value):
    return len([True for digit in bin(display_value) if digit == "1"])
```

This variant replaces the generator expression with a [list comprehension][list-comprehension].
This way, it can simply use `len()` to get the number of ones, after the comprehension filters the other digits out.

Here, `True` is used for the list elements, but we could any other value as well, as we only care about the length of the list.


## Variation #4: Using `map()` Instead of a Generator Expression

```python
def egg_count(display_value):
    return sum(map(int, bin(display_value)[2:]))
```

Here, we directly `map` the elements of the binary string to `int`s without using a generator expression or a list comprehension.

This variant is the most concise of them all, but it may be not very comprehensible to those unfamilar with functional programming.


## Variation #5: Using `filter()` with a `lambda`

```python
def egg_count(display_value):
    return len(list(filter(lambda digit: digit == "1", bin(display_value))))
```

Another alternative to a generator expression (or list comprehension) is to use the `filter()` built-in along with a [`lambda` expression][lambda-expression].
However, the creation and repeated calling of the `lambda` adds unnecessary overhead to the solution.


[bin-built-in]: https://docs.python.org/3/library/functions.html#bin
[generator-expression]: https://dbader.org/blog/python-generator-expressions
[lambda-expression]: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
[list-comprehension]: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
