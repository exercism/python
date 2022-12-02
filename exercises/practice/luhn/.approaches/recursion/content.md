# Recursion

```python
class Luhn:
    def __init__(self, card_num):
        self.isValid = Luhn.luhny_bin(0, 0, list(card_num[::-1]))

    def valid(self):
        return self.isValid

    @staticmethod
    def luhny_tune(num):
        return dbl - 9 if (dbl := 2 * num) > 9 else dbl

    @staticmethod
    def luhny_bin(pos, sum, chars):
        if not chars:
            return pos > 1 and sum % 10 == 0
        else:
            head, *tail = chars
            if head.isdigit():
                if not pos % 2:
                    return Luhn.luhny_bin(pos + 1, sum + int(head), tail)
                else:
                    return Luhn.luhny_bin(pos + 1, sum + Luhn.luhny_tune(int(head)), tail)
            if head == " ":
                return Luhn.luhny_bin(pos, sum, tail)
            return False

```

The `Luhn` object is initialzed with the `card_num` value, which is the number to be validated with the Luhn algorithm.
The result of the validation is returned from `Luhn`'s `valid()` method.
In this approach, a member variable is set to the result of running the Luhn algorithm.
That variable is returned from the `valid()` method.

The methods that do the work have the [`@staticmethod`][static-method] decorator.
This indicates that the method belongs to the class and is not recreated for every object instance.

In the code example the `__init__` method uses [slicing][slicing] syntax (`[::-1]`) to reverse the characters in the input,
which is then passed into the [list][list] constructor.
The `luhny_bin()` method takes that list, along with two `0` values that represent the initialized values for the position and the sum.

The `luhny_bin()` can call itself, which is a behavior called [recursion][recursion].
Since `luhny_bin()` can call itself, the first thing it does is to check that it is done calling itself.

```exercism/note
This check is called the terminating condition.
It's critical to have a terminating condition, since every call of a recursive function to itself places another
[frame on the stack](https://realpython.com/lessons/stack-frames-and-stack-traces/#:~:text=A%20stack%20frame%20represents%20a,is%20removed%20from%20the%20stack.).
If there is no terminating condition, then the recursive function will keep calling itself until the stack runs out of space
and a stack overflow error will occur.
```

The `luhny_bin()` method should terminate when there are no more characters to process.
By using the [falsiness][falsiness] of an empty list, the [`not` operator][not-operator] can be used instead of comparing the `len()` of the list to `0`.
When all of the characters have been iterated, the method returns if the position is greater than `1` and if the sum is evenly divisible by `10`.

While there are still characters in the list to iterate, the list is [destructured][destructure] into `head, *tail`.
The [`isdigit()`][isdigit] method is used to see if the head character is a digit.
If so, the [modulo operator][modulo-operator] is used to check if the character's position is evenly divided by `2`.
By using the [falsiness][falsiness] of `0`, the [`not` operator][not-operator] can be used instead of comparing equality to `0`.
It can be thought of as the expression _not_ having a remainder.

If the position is evenly divided by `2`, then it is even, and the character is converted to an [`int()`][int] and will be added to the sum variable.

If the position is odd, then the number is converted to an `int` and is passed to the static method which always doubles it,
and will subtract `9` from the doubled value if the doubled value is greater than `9`.
It does this using a [ternary operator][ternary-operator].
Inside the ternary operator an [assignment expression][assignment-expression] assigns the doubled value to the `dbl` variable with `(dbl := 2 * num)`.
The ternary operator returns `dbl - 9` if `dbl` is greater than `9`, otherwise it returns `dbl`.
The resulting value will be added to the sum variable.

Whether the digit is even or odd, the position is added to `1` when it and the sum are passed into the next call of the recursive method.
Also passed in is the tail of the list, which is the list of all the remaining characters after the head character.
Note that the sum and position variables are not being directly changed.
(In other words, they are not being mutated.)
The new sum and position values are calculated as the new arguments to the recursive method.

If the head character is a space, the recursive method calls itself with the same position and sum values, and the tail.

If the head character is neither a digit or a space, the method returns `False`.

[static-method]: https://docs.python.org/3/library/functions.html?#staticmethod
[slicing]: https://www.learnbyexample.org/python-string-slicing/
[list]: https://docs.python.org/3/library/functions.html?#func-list
[recursion]: https://realpython.com/python-recursion/
[stack-frame]: https://realpython.com/lessons/stack-frames-and-stack-traces/#:~:text=A%20stack%20frame%20represents%20a,is%20removed%20from%20the%20stack.
[destructure]: https://riptutorial.com/python/example/14981/destructuring-assignment
[isdigit]: https://docs.python.org/3/library/stdtypes.html?#str.isdigit
[modulo-operator]: https://realpython.com/python-modulo-operator/
[falsiness]: https://www.pythontutorial.net/python-basics/python-boolean/
[not-operator]: https://realpython.com/python-not-operator/
[int]: https://docs.python.org/3/library/functions.html?#int
[ternary-operator]: https://www.pythontutorial.net/python-basics/python-ternary-operator/
[assignment-expression]: https://peps.python.org/pep-0572/
