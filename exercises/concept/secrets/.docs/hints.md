
# Hints

## General

- Make use of [lambdas][lambdas].

## 1. Create an adder

- Return a lambda which adds the argument from the lambda to the argument passed in to `secret_add`.

## 2. Create a multiplier

- Return a lambda which multiplies the argument from the lambda to the argument passed in to `secret_multiply`.

## 3. Create a "max"-er

- Return a lambda which returns either the argument from the lambda or the argument passed in to `secret_max`, whichever one's product is bigger.
- Use the `key` argument with the [`max`][max] function.

## 4. Create a sorter

- Return a lambda which takes one argument, a list of lists of an unknown amount of numbers. The lambda should return the list of lists, but sorted by `sublist[secret_index]`.
- Use the `key` argument with the [`sorted`][sorted] function.

## 5. Create a function combiner

- Return a lambda which [composes the functions][fn-composition] passed in to `secret_combine`.

[fn-composition]: https://en.wikipedia.org/wiki/Function_composition_(computer_science)
[lambdas]: https://docs.python.org/3/howto/functional.html?highlight=lambda%20expression#small-functions-and-the-lambda-expression
[max]: https://docs.python.org/3/library/functions.html#max
[sorted]: https://docs.python.org/3/library/functions.html#sorted