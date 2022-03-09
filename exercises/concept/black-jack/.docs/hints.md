# General

[The Python comparisons tutorial][python comparisons tutorial] and [Python comparisons examples][python comparisons examples] are a great introduction covering the content of this exercise.

## 1. Calculate the value of a card

- You can use the equality comparison operator `==` to determine if a card is an ace card: `card == 'A'`.
- You can use the containment operator `in` to determine if a substring is contained inside a string: `'Q' in 'KJQ'`.
- You can use the [`int` constructor][int constructor] to convert a `str` of an `int` to an `int`: `int('13')`.

## 2. Determine which card has a higher value

- Once you have defined the `value_of_card` function, you can call it from other functions.
- You can use the value comparison operators `>` and `<` to determine if specific cards are _greater than_ or _less than_ a given value: `3 < 12`.
- You can use the equality comparison operator `==` to determine if two values are equal to one another.

## 3. Calculate the value of an ace

- Once you have defined the `value_of_card` function, you can call it from other functions.
- You can use the order comparison operator `>` to decide the appropriate course of action here.

## 4. Determine Blackjack

- Remember, you can use the [`if`/`elif`/`else` syntax][if syntax] to handle different combinations of cards.
- You can chain BOTH comparison operators and boolean operators _arbitrarily_: `y < z < x` or `(y or z) and (x or z)`
- You can reuse the already implemented `value_of_card` function.

## 5. Splitting pairs

- You can reuse the already implemented `value_of_card` function.
- You can handle the `A` case (when at least one of the cards in an ace) separately.

## 6. Doubling down

- An `A` scored at 11 will never allow doubling down if there are two cards in the hand.
- Given the first point, you _should_ be able to reuse the already implemented `value_of_card` function.
- You can chain comparison operators _arbitrarily_: `y < z < x`.
- You can use the [conditional expression][conditional expression] (_sometimes called a "ternary operator"_)
  to shorten simple `if`/`else` statements: `13 if letter == 'M' else 3`.

[conditional expression]: https://docs.python.org/3/reference/expressions.html#conditional-expressions
[if syntax]: https://docs.python.org/3/tutorial/controlflow.html#if-statements
[int constructor]: https://docs.python.org/3/library/functions.html#int
[python comparisons examples]: https://www.tutorialspoint.com/python/comparison_operators_example.htm
[python comparisons tutorial]: https://docs.python.org/3/reference/expressions.html#comparisons
