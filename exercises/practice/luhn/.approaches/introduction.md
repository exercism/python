# Introduction

There are many idiomatic ways to solve Luhn.
Among them are:
- You can use a for loop on a `reversed()` iterator.
- You can scrub the input with `replace()` and test with `isdigit()` before reversing the input to `enumerate()` it.

## General guidance

One important aspect to solving Luhn is to allow for spaces in the input and to disallow all other non-numeric characters.
Another important aspect is to handle the value of each digit according to its position in the string.
Another consideration may be to calculate the validity only once, no matter how many times `valid()` is called.

## Approach: `reversed()` `for` loop

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

For more information, check the [`reversed()` `for` loop approach][approach-reversed-for].

## Approach: `replace()`, reverse, `enumerate()`

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
        num = num.replace(' ', '')
        if not num.isdigit():
            return False
        total = 0
        for pos, ltr in enumerate(num[::-1]):
            if not pos % 2:
                total+= int(ltr)
            else:
                total += Luhn.luhny_tune(int(ltr))
            pos += 1
        return pos > 1 and not total % 10

```

For more information, check the [`replace()`, reverse, `enumerate()` approach][approach-replace-reverse-enumerate].

## Other approaches

Besides the aforementioned, idiomatic approaches, you could also approach the exercise as follows:

### Other approach: recursion

Another approach can use recursion to validate the number.
For more information, check the [recursion approach][approach-recursion].

## Which approach to use?

The `replace()`, reverse, `enumerate()` approach benchmarked the fastest.

To compare performance of the approaches, check the [Performance article][article-performance].

[approach-reversed-for]:  https://exercism.org/tracks/python/exercises/luhn/approaches/reversed-for
[approach-replace-reverse-enumerate]: https://exercism.org/tracks/python/exercises/luhn/approaches/replace-reverse-enumerate
[approach-recursion]: https://exercism.org/tracks/python/exercises/luhn/approaches/recursion
[article-performance]: https://exercism.org/tracks/python/exercises/luhn/articles/performance
