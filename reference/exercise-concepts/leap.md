# Concepts of `leap`

## Example implementation

From the current [example.py](https://github.com/exercism/python/blob/master/exercises/leap/example.py):

```python
def leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
```

## Concepts

- [Functions][functions]: the exercise relies on a `def` statement to create a named function
- [Parameters][parameters]: the exercise requires a single positional parameter in the function signature
- [Return Value][return-value]: the exercise must use a `return` statement to return a value to the caller
- [Expressions][expressions]: the exercise relies on writing an expression that will be evaluated to a return value
- [Modular Division][modular-division]: the exercise relies on the `%` operator to check if one number is evenly divisible by another
- [Boolean Operators][boolean-operators]: the exercise relies on `and`, `or`, and (optionally) `not` to form Boolean predicates
- [Boolean Logic][boolean-logic]: the exercise relies on `and` and `or` to combine Boolean predicates into a single logical answer
- [Comparision][comparision]: the exercise relies on the `==` and `!=` operators to make binary comparisons between values
- [Equivalence][equivalence]: the exercise relies on the `==` and `!=` operators to check that two values are equivalent (or not)
- [Order of Evaluation][order-of-evaluation]: the exercise relies on parentheses to explicitly modify the normal order of evaluation of an expression
- [Operator Precedence][operator-precedence]: the exercise is most simply stated when the student understands the operator precedence binding rules of Python
- [Short-Circuiting][short-circuiting]: the exercise relies on short-circuiting to avoid unnecessary calculations
- [Generics][generics]: the exercise is polymorphic across numerical types (ie int, float, Decimal)
- [Duck Typing][duck-typing]: the exercise supports any argument that supports modular division and comparison to integers (ie int, float, Decimal)
