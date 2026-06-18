# Use the Built-In Bit-Count Functionality

~~~~exercism/caution
This approach does _not_ follow the instructions, as it uses the bit-count functionality from the standard library.
It is only described here to show what an idiomatic way of counting bits in a _different context_ would be. 
~~~~

```python
def egg_count(display_value):
    return display_value.bit_count()
```

This approach uses [`int.bit_count()`][int-bit_count] from the Python standard library to count the number of ones in the binary representation of `display_value`.

This works because Python does _not_ have separate types for binary, octal, or hexadecimal numbers.
Instead, all of these are considered _representations_ or display formats of `int`.
Even if a binary literal is declared with the `0b` prefix, Python stores it internally as type `int`:

```python
>>> 0b00110101 #<- 53 in binary
53
>>> type(0b00110101)
<class 'int'>

>>> 0O65 #<- 53 in octal
53
>>> type(0O65)
<class 'int'>
```

Due to this, all methods that work with binary numbers in the standard library actually operate on `int`s.


## Variation #1: Using `str.count()`

```python
def egg_count(display_value):
    return bin(display_value).count("1")
```

This variant uses [`bin()`][bin-built-in] (_or any other method discussed in the [convert to a binary string][approach-convert-to-binary-string] approach_) to convert `display_value` to a `binary string`.
Then, [`str.count()`][sequence-count] is used to count how many times "1" appears in the string.

Though one could argue that this _technically_ doesn't use the built-in bit-count functionality, the solution still defeats the purpose of the exercise.


## Variation #2: Using Function Aliasing

```python
egg_count = int.bit_count
```

This solution is the shortest of them all, but it can also be rather confusing (_and does not follow the instructions_).
It also can throw what appears to be a non-related error:

```python
>>> egg_count(3.5)
Traceback (most recent call last):
  File "<python-input-77>", line 1, in <module>
    egg_count(3.5)
    ~~~~~~~~~^^^^^
TypeError: descriptor 'bit_count' for 'int' objects doesn't apply to a 'float' object
```

This variant makes clever use of [function/method aliasing][function-aliasing], which creates a new name that refers to the existing `int.bit_count()` method.
This means when `egg_count(display_value)` is called, `int.bit_count(display_value)` is being used.
However, you should be careful when using function aliasing, as it often makes code _less_ readable (_as with the error shown above_), and it doesn't have many practical applications outside of backward compatibility.

This solution works because `int.bit_count(<integer_variable>)` becomes just another way of saying `<integer_variable>.bit_count()`, as instance methods of a class (_the class here being `int`_) have `self` implicitly passed as the first argument when called on an instance (_but not when called directly on the class!_).
See the [Classes Concept in the Syllabus][concept-classes: methods] or the [Official Python Classes Tutorial][class-method-objects-tutorial] for more detail on how `self` works.

[approach-convert-to-binary-string]: https://exercism.org/tracks/python/exercises/eliuds-eggs/approaches/convert-to-binary-string
[bin-built-in]: https://docs.python.org/3/library/functions.html#bin
[class-method-objects-tutorial]: https://docs.python.org/3/tutorial/classes.html#method-objects
[concept-classes: methods]: https://exercism.org/tracks/python/concepts/classes#h-methods
[function-aliasing]: https://tutorialreference.com/python/examples/faq/python-how-to-use-function-aliasing
[int-bit_count]: https://docs.python.org/3/library/stdtypes.html#int.bit_count
[sequence-count]: https://docs.python.org/3/library/stdtypes.html#sequence.count
