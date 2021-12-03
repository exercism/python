# Hints

## General

- [The Python Numbers Tutorial][python-numbers-tutorial] and [Python numeric types][python-numeric-types] can be a great introduction.

## 1. Estimate value after exchange

- You can use the [division operator][division-operator] to get the value of exchanged currency.

## 2. Calculate currency left after an exchange

- You can use the [subtraction operator][subtraction-operator] to get the amount of changes.

## 3. Calculate value of bills

- You can use the [multiplication operator][multiplication-operator] to get the value of bills.

## 4. Calculate number of bills

- You need to divide `budget` into `denomination`.
- You need to use type casting to _int_ to get the exact number of bills.
- To remove decimal places from a `float`, you can convert it to `int`.

  **Note:** The `//` operator also does floor division. But, if the operand has `float`, the result is still `float`.

## 5. Calculate value after exchange

- You need to calculate `spread` percent of `exchange_rate` using multiplication operator and add it to `exchange_rate` to get the exchanged currency.
- The actual rate needs to be computed. Remember to add exchange rate and exchange fee.
- You can get exchanged money affected by commission by using divide operation and type casting _int_.


[python-numbers-tutorial]: https://docs.python.org/3/tutorial/introduction.html#numbers
[python-numeric-types]: https://docs.python.org/3.9/library/stdtypes.html#numeric-types-int-float-complex
[division-operator]: https://docs.python.org/3/tutorial/introduction.html#numbers
[subtraction-operator]: https://docs.python.org/3/tutorial/introduction.html#numbers
[multiplication-operator]: https://docs.python.org/3/tutorial/introduction.html#numbers
