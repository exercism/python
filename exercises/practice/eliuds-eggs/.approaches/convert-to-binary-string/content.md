# Convert to a Binary String

```python
def egg_count(display_value):
    binary_value = bin(display_value)[2:] #<- Slice off the first two characters.
    eggs = 0
    for digit in binary_value:
        eggs += int(digit)
    return eggs
```

This approach uses [`bin()`][bin-built-in] to convert `display_value` to a binary string.
Next, the first two characters of the binary string are removed via slice, as the string has "0b" as a prefix before the binary digits.

After the binary digits are obtained, this solution loops across all of them, turning each one into an `int` and adding it to `eggs`.
This counts up all of the instances of "1" in the binary string, as 0 and 1 are the only valid binary digits.

Those less familiar with binary may find this approach to be simpler than the others.
However, it does have the added overhead of converting to and from a string.


~~~~exercism/note
There are three other Pythonic ways of obtaining a binary string.
These strategies use the [string format specification][string-format-spec] in different ways.  
  
The first is to use an [`f-string`][f-string] 

```python
# This uses the 'binary' format code.
binary_value = f"{display_value:b}"
```  

Another is to use [`str.format()`][str-format]:

```python
# This also uses the 'binary' format code with different syntax.
binary_value = "{:b}".format(display_value)
```

Lastly, you could use the [`format()` built-in][format-built-in]:

```python
# This uses the 'binary' format code passed as a quoted string.
binary_value = format(display_value, "b")
```

These methods have the added benefit of not producing the "0b" prefix that then needs to removed.
However, some variations of this approach use other ways to get around the prefix.

[f-string]: https://docs.python.org/3/reference/lexical_analysis.html#f-strings
[format-built-in]: https://docs.python.org/3/library/functions.html#format
[str-format]: https://docs.python.org/3/library/stdtypes.html#str.format
[string-format-spec]: https://docs.python.org/3/library/string.html#format-specification-mini-language
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
The main difference is that it avoids slicing & copying the binary string by using an `if` clause in the generator expression.
This also avoids the overhead of calling `int()` on each digit.


## Variation #3: Using `len()` Instead of `sum()`

```python
def egg_count(display_value):
    return len([True for digit in bin(display_value) if digit == "1"])
```

This variant replaces the generator expression with a [list comprehension][list-comprehension].
This way, it can use `len()` to get the number of ones (_which evaluate to True_), after the comprehension filters the other digits (_which evaluate to False_) out.

Here, `True` is used for the list elements, but we could use any other value as well, as we only care about the length of the "1"s list.
`bool()` could also be used here, but would require that each digit be converted via `int()` before evaluating:

```python
def egg_count(display_value):
    return len([bool(int(digit)) for digit in bin(display_value)[2:]])
```


## Variation #4: Using `map()` Instead of a Generator Expression or List Comprehension

```python
def egg_count(display_value):
    return sum(map(int, bin(display_value)[2:]))
```

Here, we directly [`map`][map-built-in] the elements of the binary string to `int()` without using a generator expression or a list comprehension.

This variant is the most concise, but it may be not very comprehensible to those unfamiliar with functional programming.
It also somewhat hides the overhead that is incurred calling `int()` on every digit.


## Variation #5: Using `filter()` with a `lambda`

```python
def egg_count(display_value):
    return len(list(filter(lambda digit: digit == "1", bin(display_value))))
```

Another alternative to a generator expression (or list comprehension) is to use the [`filter()` built-in][filter-built-in] along with a [`lambda` expression][lambda-expression].
However, the creation and repeated calling of the `lambda` adds unnecessary overhead to the solution and `filter()` typically runs slower than the equivalent list comprehension.


## Variation #6: Using `functools.reduce()` with a `lambda`

```python
from functools import reduce

def egg_count(display_value):
    return reduce(lambda eggs, digit: eggs + int(digit), bin(display_value)[2:], 0)
```

This variant uses [`reduce()`][functools-reduce] from the [`functools` module][functools-module] along with a `lambda` expression.
Here, `functools.reduce()` calls the `lambda` on each codepoint in `bin(display_value)[2:]`, accumulating the value of `eggs` from the initial `0`.

Similar to the previous variant, the creation and repeated calling of the `lambda` causes extra overhead, as does importing the `functools` module.


[bin-built-in]: https://docs.python.org/3/library/functions.html#bin
[filter-built-in]: https://docs.python.org/3/library/functions.html#filter
[functools-module]: https://docs.python.org/3/library/functools.html
[functools-reduce]: https://docs.python.org/3/library/functools.html#functools.reduce
[generator-expression]: https://dbader.org/blog/python-generator-expressions
[lambda-expression]: https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
[list-comprehension]: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
[map-built-in]: https://docs.python.org/3/library/functions.html#map
