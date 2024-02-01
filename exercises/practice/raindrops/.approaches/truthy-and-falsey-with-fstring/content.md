# Truthy and Falsey Values with f-strings


```python
def convert(number):
    threes = '' if number % 3 else 'Pling' # Empty string if modulo == 1 (0 evaluates to False)
    fives =  '' if number % 5 else 'Plang'
    sevens = '' if number % 7 else 'Plong'
    
    return f'{threes}{fives}{sevens}' or str(number)
  
  #OR#
  
def convert(number):
    threes = 'Pling' if not number % 3 else '' # Sound if NOT modulo == 0 
    fives =  'Plang' if not number % 5 else ''
    sevens = 'Plong' if not number % 7 else ''
    
    return f'{threes}{fives}{sevens}' or str(number)
```

This is very similar to the [`if-statement`][approach-if-statements] approach logic, but uses [ternary expressions][ternary expression] to assign either an empty string or a drop sound to a variable.
The variables are then used in an `f-string` to compose the result, avoiding the use of `join()`, or a `loop`.
If the `f-string` is empty _(evaluating to False in a [boolean context][truth-value-testing]_), a `str` of the input number is returned instead.

This has `O(1)` time and space complexity.

These two variations both exploit the fact that boolean `True` and `False` are a subtype of `int` in Python.
0 evaluates to `False`, and 1 to `True`.
So the expression `'Pling' if not number % 3 else ''` can be read as "return 'Pling" if number % 3 not False" where `False` is 0, and (not `False`) is 1.
The expression `'' if number % 3 else 'Pling'` is the inverse: "return '' if number % 3 is True" - where number % 3 > 0 is `True`, and number % 3 == 0 is `False`.

Like the `if-statement` approach, these solutions are nicely readable and to-the-point, but will grow in length and get harder to read if many more factors are added or business logic changes.
The `f-string` in particular could get unwieldy beyond about 5 factors.
Other solutions using data structures to hold factors and `join()` to assemble strings might be a better option in 'high change' situations.

[approach-if-statements]:  https://exercism.org/tracks/python/exercises/raindrops/approaches/if-statements
[ternary expression]: https://docs.python.org/3/reference/expressions.html#conditional-expressions
[truth-value-testing]: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
