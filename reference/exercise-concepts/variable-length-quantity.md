# Concepts of `variable-length-quantity`

## Example implementation

From the current [example.py](https://github.com/exercism/python/blob/master/exercises/variable-length-quantity/example.py):

```python
EIGHTBITMASK = 0x80
SEVENBITSMASK = 0x7f


def encode_single(n):
    bytes_ = [n & SEVENBITSMASK]
    n >>= 7

    while n > 0:
        bytes_.append(n & SEVENBITSMASK | EIGHTBITMASK)
        n >>= 7

    return bytes_[::-1]


def encode(numbers):
    return sum((encode_single(n) for n in numbers), [])


def decode(bytes_):
    values = []
    n = 0

    for i, byte in enumerate(bytes_):
        n <<= 7
        n += (byte & SEVENBITSMASK)

        if byte & EIGHTBITMASK == 0:
            values.append(n)
            n = 0
        elif i == len(bytes_) - 1:
            raise ValueError('incomplete byte sequence')

    return values
```

## Concepts

- [Loops][loops]: the knowledge of `while` and `for` loops are useful to solve this exercise
- [Comparison][comparison]: concept required to solve the exercise, `==`, `>`, `<`
- [Builtin Functions][builtin-functions]: the `sum()` built-in function is a useful concept to solve the exercise
- [Lists][lists]: knowledge of lists and iteration on lists is required for this exercise
- [Builtin Functions][builtin-functions]: the `len()` built-in function is a useful concept in this exercise
- [Conditionals][conditionals]: knowledge of `if...else` statements is required
- [List Methods][list-methods]: the use of methods of list could be useful in this exercise. Methods like `append`, `pop`...
- [Parameters][parameters]: concept over arguments of a function and how to use them is required
- [Return Value][return-value]: the knowledge of `return` statement could be a useful concept in this exercise
- [List Comprehensions][list-comprehensions]: the use of list comprehension can be useful in this exercise
- [Binary Numbers][binary-numbers]: binary numbers are a core important concept for this exercise
- [Bitwise Operators][bitwise-operators]: bitwise operators such as `<<`, `>>`, `&`, `|`, `~`, `^` are central to this exercise
- [Iteration][iteration]: the `for ... in` concept is useful to loop over the lists
- [Builtin Functions][builtin-functions]: the `enumerate` built-in function is a useful concept in this exercise
- [Raise][raise]: the user could find useful the `Exception` concept to `raise` a `ValueError` for incorrect input
- [Exception Message][exception-message]: the user can use a custom error message inside the mentioned `ValueError`
- [Inheritance][inheritance]: the knowledge of inheritance can be useful in this exercises because all `Exceptions` types inherit from the base class
