# About

A comparison operator in python, also called python relational operator, compares the values of two operands and returns `True` or `False` based on whether the condition is met. The most common comparison operators are `"<"`, `">"`, `"=="`, `">="`, `"<="`, `"!="`, `"is"`

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
>>> 6 != 6 # not equal to
False
>>> 5 != 6
True
```

## Comparison Chaining

Comparisons can be chained arbitrarily, e.g., `x < y <= z` is equivalent to `x < y` `and` `y <= z`, except that `y` is evaluated only once (but in both cases `z` is _not_ evaluated at all when `x < y` is found to be `False`).

Also unlike `C`, expressions like `a < b < c` have the interpretation that is conventional in mathematics.

```python
>>> x, y, z = 2, 5, 10
>>> x < y < z
True
>>> x < y > z
False
>>> x > y < z
False
```

## Comparison of different data types

Since everything in `python` represents an `object` things start getting interesting when we compare objects of different types. For example, the `string` value of a number is considered a completely different value from the `integer` or `floating-point` version, an `integer` can be equal to a `floating point`.

```python
>>> 17 == '17'
False
>>> 17 == 17.0
True
>>> 17.0 == 0017.000
True
```

Python makes this distinction because strings are text, while `integers` and `floats` are both numbers.

## Value Comparison

The operators `<`, `>`, `==`, `>=`, `<=`, and `!=` compare the `values` of two objects. The objects do not need to have the same type. Remember that in python
every object has a `value` in addition to `type` and `identity`

Following are comparison behaviour of most `built-ins` types

Numbers of built-in numeric types like `int`, `float` and of the standard library types `fractions.Fraction` and `decimal.Decimal` can be compared within and across their types.

Any ordered comparison of a number to a not-a-number value is `False`. A counter-intuitive implication is that not-a-number values are not equal to themselves.

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

`Strings` compare lexicographically using the numerical Unicode code points (the result of the built-in function ord()) of their characters. `Strings` and `binary` sequences cannot be directly compared.

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
```

Collections like `list`, `set`, `tuple` and `dict` can be compared too if they are of the same type, have the same length, and each pair of corresponding elements must compare equal.

```python
>>> [1,2] == [1, 2]
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

The operators `is` and `is not` test for an object’s identity. An Object’s identity is determined using the `id()` function.

`x is y` is `True` if and only if `x` and `y` are the same object. `x` is not y` yields the inverse truth value.

```python
>>> x = [1,2,3]
>>> y = x
>>> x == y
True
>>> id(x)
4462635008
>>> id(y)
4462635008
>>> x is not y
False
```

## Membership test operations

The operators `in` and `not in` test for membership. `a` in `s` evaluates to `True` if `a` is a member of s, and `False` otherwise. `a not in s` returns the negation of `a in s`.

For the string and bytes types, `a` in `s` is `True` if and only if `a` is a substring of `b`.

```python
s = {11, 22, 33}
>>> 22 in s
True
>>> 44 in s
False
>>>
>>> employee = {'name': 'John Doe', 'id': 67826, 'age': 33, 'title': 'ceo'}
>>> 'age' in employee
True
>>> 33 in employee
False
>>> 'lastname' not in employee
True
>>>
>>> name = "Super Batman"
>>> "Bat" in name
True
>>> "Batwoman" in name
False
```
