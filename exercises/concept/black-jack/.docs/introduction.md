## Comparisons

There are some different kinds of comparison operators in Python

| Operator | Operation                | Description                                              |
| -------- | ------------------------ | -------------------------------------------------------- |
| `>`      | Greater than             | `a > b` is `True` if `a` is greater than `b`             |
| `<`      | Less than                | `a < b` is `True` if `a` is less than `b`                |
| `==`     | Equal to                 | `a == b` is `True` if `a` is equals to `b`               |
| `>=`     | Greater than or equal to | `a >= b` is `True` if `a > b` or `a == b` is `True`      |
| `<=`     | Less than or equal to    | `a <= b` is `True` if `a < b` or `a == b` is `True`      |
| `!=`     | Not equal to             | `a != b` is `True` if `a = b` is `False`                 |
| `is`     | Identity                 | `a is b` is `True` if `a` and `b` is same object         |
| `is not` | Identity                 | `a is not b` is `True` if `a` and `b` is not same object |
| `in`     | Containment test         | `a in b` is `True` if `a` is member of `b`               |
| `not in` | Containment test         | `a not in b` is `True` if `a` is not a member of `b`     |

## Greater than

Operator `>` tests if the first operand's value is greater than the second one's.

```python
>>> 3 > 1
True
>>> 2.99 > 3
False
>>> 1 > 1
False
>>> 0 > 1
False
```

## Less than

Operator `<` tests if the first operand's value is less than the second one's.

```python
>>> 3 < 1
False
>>> 2.99 < 3
True
>>> 1 < 1
False
>>> 0 < 1
True
```

## Equal to

Operator `==` tests if the first operand's value is equal to the second one's

```python
>>> 3 == 1
False
>>> 2.99 == 3
False
>>> 1 == 1
True
>>> 0 == 1
False
```

## Greater than or equal to

Operator `>=` tests if the first operand's value is equal to or greater than the second one's.

```python
>>> 3 >= 1
True
>>> 2.99 >= 3
False
>>> 1 >= 1
True
>>> 0 >= 1
False
```

## Less than or equal to

Operator `<=` tests if the first operand's value is equal to or less than the second one's.

```python
>>> 3 <= 1
False
>>> 2.99 <= 3
True
>>> 1 <= 1
True
>>> 0 <= 1
True
```

## Not equal to

Operator `!=` tests if the first operand's value is not equal to the second one's

```python
>>> 3 != 1
True
>>> 2.99 != 3
True
>>> 1 != 1
False
>>> 0 != 1
True
```

## Identity test

Operator `is` tests if the first and second operand is the same object.

```python
# comparing non-object type `is` will raise warning
>>> 1 is 1
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
True
>>> 1 is 2
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
False
>>> x = int(4)
>>> y = x
>>> x is y
True
>>> y = int(5)
>>> x is y
False
```

Operator `is not` tests if the first and second operand is not the same object.

```python
>>> 1 is not 1
<stdin>:1: SyntaxWarning: "is not" with a literal. Did you mean "!="?
False
>>> 1 is not 2
<stdin>:1: SyntaxWarning: "is not" with a literal. Did you mean "!="?
True
>>> x = int(4)
>>> y = x
>>> x is not y
False
>>> y = int(5)
>>> x is not y
True
```

## Containment test

Operator `in` tests if the first operand is a member of the second operand.

```python
>>> x = [1, 2, 3, 4, 5]
>>> 1 in x
True
>>> 2 in x
True
>>> 3 in x
True
>>> 4 in x
True
>>> 5 in x
True
>>> 6 in x
False
```

Operator `not in` tests if the first operand is not a member of the second operand.

```python
>>> x = [1, 2, 3, 4, 5]
>>> 1 not in x
False
>>> 2 not in x
False
>>> 3 not in x
False
>>> 4 not in x
False
>>> 5 not in x
False
>>> 6 not in x
True
```

[python3-docs]: https://docs.python.org/3/library/operator.html