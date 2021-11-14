# About

A [comparison operator][comparisons] in Python (_also called a Python relational operator_), looks at the values of two operands and returns `True` or `False` based on whether the `comparison` condition is met. The most common comparison operators are `"<"`, `">"`, `"=="`, `">="`, `"<="`, and `"!="`. They all have the same priority (which is higher than that of the Boolean operations)

```python
>>> 7 > 5
True
>>> 99 < 100
True
>>> 4 < 4
False
>>> 4 <= 4
True
>>> 1 >= 1
True
>>> 5 == 5
True
>>> 6 != 6  # not equal to
False
>>> 5 != 6
True
>>> not 3 == 3  # interpreted as not(3 == 3)
False
```

## Comparison Chaining

Comparisons can be chained arbitrarily, e.g., `x < y <= z` is equivalent to `x < y` `and` `y <= z`, except that `y` is evaluated only once (but in both cases `z` is _not_ evaluated at all when `x < y` is found to be `False`). This is also called `short-circuit` evaluation which means the execution is stopped if the truth value of the expression has already been determined. Note that the evaluation of expression takes place from left to right. In python, short circuiting is supported by various boolean operators, functions and, in this case, comparison chaining.

Also unlike `C`, expressions like `a < b < c` have the interpretation that is conventional in mathematics.

```python
>>> x = 2
>>> y = 5
>>> z = 10
>>> x < y < z
True
>>> x < y > z
False
>>> x > y < z
False
```

## Comparison between different data types

Since everything in Python is an `object`, things can get interesting when objects of different types are compared. For example, the `str` value of a number is considered completely different from the `integer` or `floating-point` value. However, an `integer` **can** be considered equal to a `float`, as they are both numeric types that Python can implicitly convert to compare. For other numeric types, comparison operators are defined where they "make sense", but throw a `TypeError` if the underlying objects cannot be converted for comparison. For more information on the rules that python uses for numeric conversion, see [arithmetic conversions][arithmetic conversions] in the Python documentation.

```python
>>> 17 == '17'
False
>>> 17 == 17.0
True
>>> 17.0 == 0017.000
True
>>> complex(1, 2) == complex(1.0, 2.00)
True
```

Python makes this distinction because strings are text, while `integers` and `floats` are numeric types.

## Value Comparison

The operators `<`, `>`, `==`, `>=`, `<=`, and `!=` compare the _values_ of two different objects. The objects do not need to have the same type. Remember that in Python

every object has a `value` in addition to `type` and `identity`.

### Following are comparison behaviour of most `built-ins` types.

Numbers of built-in numeric types like `int`, `float` and of the standard library types `fractions.Fraction` and `decimal.Decimal` can be compared within and across their types.

Any ordered comparison of a number to a `NaN` (_not a number_) value is `False`. A counter-intuitive implication is that `NaN` never compares equal to `NaN`.


```python
>>> x = float('NaN')
>>> x
nan
>>> 3 < x
False
>>> x < 3
False
>>> x == x
False
```

Strings (`str`) are compared _lexicographically_ using their individual numerical Unicode code points (_the result of passing each code point in the `str` to the built-in function `ord()`_). `str` and `binary` sequences cannot be directly compared.

```python
>>> 'santa' < 'claus'
False
>>> 'Santa' < 'claus'
True
>>> ord('s')
115
>>> ord('S')
83
>>> ord('c')
99
>>> '龙波' < '王想'  # chinese words
False
>>> # check ord() of first letters
>>> ord('龙')
40857
>>> ord('王')
29579
>>>
>>>
>>> # let's try korean words
>>> '이서윤' < '김은정'
False
# compare their first letters
>>> ord('이') < ord('김')
False
```

Collections like `list`, `set`, `tuple` and `dict` can also be compared -- provided they are of the same `type`, have the same length, and each _**pair**_ of corresponding elements within the collection are comparable.

```python
>>> [1, 2] == [1, 2]
True
>>> (1, 2) == [1, 2]
False
>>> [1, 2] < [1, 2, 3]
True
>>> # comparison of dicts
>>> {'name': 'John', 'age': 19} == {'name': 'John', 'age': 18}
False
>>> {'name': 'John', 'age': 19} == {'name': 'John', 'age': 19}
True
```

## Identity comparisons

The operators `is` and `is not` test for an object's _identity_. An object's identity is determined using the `id()` function.

`apple is orange` is `True` if and only if `apple` and `orange` are the same object. `apple is not orange` yields the inverse truth value.

```python
>>> my_fav_numbers = [1, 2, 3]
>>> your_fav_numbers = my_fav_numbers
>>> my_fav_numbers == your_fav_numbers
True
>>> id(my_fav_numbers)
4462635008
>>> id(your_fav_numbers)
4462635008
>>> my_fav_numbers is not your_fav_numbers
False
```

## Membership test operations

The operators `in` and `not in` test for _membership_. `fish in soup` evaluates to `True` if `fish` is a member of `soup`, and evaluates `False` otherwise. `fish not in soup` returns the negation, or _opposite of_ `fish in soup`.

For the string and bytes types, `name` in `fullname` is `True` if and only if `name` is a substring of `fullname`.

```python
lucky_numbers = {11, 22, 33}
>>> 22 in lucky_numbers
True
>>> 44 in lucky_numbers
False
>>>
>>> employee = {
    'name': 'John Doe',
    'id': 67826,
    'age': 33,
    'title': 'ceo'
    }
>>> 'age' in employee
True
>>> 33 in employee
False
>>> 'lastname' not in employee
True
>>>
>>> name = 'Super Batman'
>>> 'Bat' in name
True
>>> 'Batwoman' in name
False
```

[comparisons]: https://docs.python.org/3/library/stdtypes.html?highlight=comparisons#comparisons
[arithmetic conversion]: https://docs.python.org/3/reference/expressions.html?highlight=number%20conversion#arithmetic-conversions
