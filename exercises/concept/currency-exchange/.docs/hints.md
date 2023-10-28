# Hints

## General

- [The Python Numbers Tutorial][python-numbers-tutorial] and [Python numeric types][python-numeric-types] can be a great introduction.

## 1. Estimate value after exchange

- You can use the [division operator][division-operator] to get the value of exchanged currency.

## 2. Calculate currency left after an exchange

- You can use the [subtraction operator][subtraction-operator] to get the amount of change.

## 3. Calculate value of bills

- You can use the [multiplication operator][multiplication-operator] to get the value of bills.

## 4. Calculate number of bills

- You need to divide `amount` into `denomination`.
- You need to use type casting to `int` to get the exact number of bills.
- To remove decimal places from a `float`, you can convert it to `int`.

  **Note:** The `//` operator also does floor division. But, if the operand has `float`, the result is still `float`.

## 5. Calculate leftover after exchanging into bills

- You need to find the remainder of `amount` that does not equal a whole `denomination`.
- The Modulo operator `%` can help find the remainder.

## 6. Calculate value after exchange

- You need to calculate `spread` percent of `exchange_rate` using multiplication operator and add it to `exchange_rate` to get the exchanged currency.
- The actual rate needs to be computed. Remember to add exchange _rate_ and exchange _fee_.
- You can get exchanged money affected by commission by using divide operation and type casting to `int`.


[division-operator]: https://docs.python.org/3/tutorial/introduction.html#numbers
[multiplication-operator]: https://docs.python.org/3/tutorial/introduction.html#numbers
[python-numbers-tutorial]: https://docs.python.org/3/tutorial/introduction.html#numbers
[python-numeric-types]: https://docs.python.org/3.9/library/stdtypes.html#numeric-types-int-float-complex
[subtraction-operator]: https://docs.python.org/3/tutorial/introduction.html#numbers
