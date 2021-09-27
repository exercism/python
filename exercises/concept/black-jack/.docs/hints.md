# General

[The Python comparisons tutorial][python comparisons tutorial] and [Python comparisons examples][python comparisons examples] are a great introduction covering the content of this exercise.

## 1. Calculate the value of a card

- You can use the equality comparison operator `==` to determine specific cards, e.g. `card == 'J'`.
- You can use the [`int` constructor][int constructor] to get an integer number from an integer literal, e.g. `int(card)`.

## 2. Calculate the value of an ace

- You can use the order comparison operator `>` to decide the appropriate course of action, e.g. `hand_value + 11 > 21`.

## 3. Determine Blackjack

- You can use the [`if`/`elif`/`else` syntax][if syntax] to handle different combinations of cards.
- You can reuse the already implemented `value_of_card` function.

## 4. Splitting pairs

- You can handle the `A` case (when at least one of the cards in an ace) separately.

## 5. Doubling down

- You can chain comparison operators, e.g. `9 <= hand_value <= 11`.
- You can use the [conditional expression][conditional expression] (sometimes called a "ternary operator")
to shorten simple `if`/`else` statements, e.g. `1 if card == 'A' else value_of_card(card)`.

[python comparisons tutorial]: https://docs.python.org/3/reference/expressions.html#comparisons
[python comparisons examples]: https://www.tutorialspoint.com/python/comparison_operators_example.htm
[int constructor]: https://docs.python.org/3/library/functions.html#int
[if syntax]: https://docs.python.org/3/tutorial/controlflow.html#if-statements
[conditional expression]: https://docs.python.org/3/reference/expressions.html#conditional-expressions
