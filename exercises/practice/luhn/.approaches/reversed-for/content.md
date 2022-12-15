# `reversed()` with a `for` loop

```python
class Luhn:

    def __init__(self, card_num):
        self.isValid = Luhn.luhny_bin(card_num)

    def valid(self):
        return self.isValid

    @staticmethod
    def luhny_tune(num):
        return dbl - 9 if (dbl := 2 * num) > 9 else dbl

    @staticmethod
    def luhny_bin(num):
        total = 0
        pos = 0
        for ltr in reversed(num):
            if ltr.isdigit():
                if not pos % 2:
                    total+= int(ltr)
                else:
                    total += Luhn.luhny_tune(int(ltr))
                pos += 1
            elif ltr != " ":
                return False
        return pos > 1 and not total % 10

```

The `Luhn` object is initialzed with the `card_num` value, which is the number to be validated with the Luhn algorithm.
The result of the validation is returned from `Luhn`'s `valid()` method.
In this approach, a member variable is set to the result of running the Luhn algorithm.
That variable is returned from the `valid()` method.

The methods that do the work have the [`@staticmethod`][static-method] decorator.
This indicates that the method belongs to the class and is not recreated for every object instance.

In the code example the `luhny_bin()` method initializes the `total` and `pos` variables to `0`.
It then calls [`reversed()`][reversed] on the input and iterates the characters from right to left with a [`for`][for] loop.

The [`isdigit()`][isdigit] method is used to see if the character is a digit.
If so, the [modulo operator][modulo-operator] is used to check if the character's position is evenly divided by `2`.
By using the [falsiness][falsiness] of `0`, the [`not` operator][not-operator] can be used instead of comparing equality to `0`.
It can be thought of as the expression _not_ having a remainder.

If the position is evenly divided by `2`, then it is even, and the character is converted to an [`int()`][int] and added to the total variable.

If the position is odd, then the number is converted to an `int` and is passed to the static method which always doubles it,
and will subtract `9` from the doubled value if the doubled value is greater than `9`.
It does this using a [ternary operator][ternary-operator].
Inside the ternary operator an [assignment expression][assignment-expression] assigns the doubled value to the `dbl` variable with `(dbl := 2 * num)`.
The ternary operator returns `dbl - 9` if `dbl` is greater than `9`, otherwise it returns `dbl`.
The resulting value is added to the total variable.

Whether the digit is even or odd, the position is incremented by `1`.
If the character is not a digit, the method returns `False` if the character is not a space.
If the character is a space, the loop will go to the next iteration without incrementing the position variable.

After the iteration of the characters is done, the method returns if the position is greater than `1` and if the total is evenly divisible by `10`.

[static-method]: https://docs.python.org/3/library/functions.html?#staticmethod
[reversed]: https://docs.python.org/3/library/functions.html?#reversed
[for]: https://docs.python.org/3/tutorial/controlflow.html#for-statements
[isdigit]: https://docs.python.org/3/library/stdtypes.html?#str.isdigit
[modulo-operator]: https://realpython.com/python-modulo-operator/
[falsiness]: https://www.pythontutorial.net/python-basics/python-boolean/
[not-operator]: https://realpython.com/python-not-operator/
[int]: https://docs.python.org/3/library/functions.html?#int
[ternary-operator]: https://www.pythontutorial.net/python-basics/python-ternary-operator/
[assignment-expression]: https://peps.python.org/pep-0572/
