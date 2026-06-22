# Ternary operator

```python
def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    counter = 0
    while number != 1:
        number = number / 2 if number % 2 == 0 else number * 3 + 1
        counter += 1
    return counter
```

This approach starts with checking if the number is less than or equal to zero.
If it is, then a [`ValueError`][value-error] is raised.

After that, a `counter` variable is assigned to zero.
Then we start a `while loop` that will run until the number is equal to one, at which point it will terminate.

Inside the `loop`, we have a [ternary operator][ternary-operator] (also called a [conditional expression][conditional-expression]).
A `ternary operator` (_`conditional expression`_) can be viewed as a one-line `if`/`else` statement.
Using a one-line construct can make the code more concise.


The first part of the `ternary operator` divides the number by two if it is even.
The `else` part of the expression (_where the number is not even_) multiplies the number by three and adds one.
Then the `counter` is incremented by one.
When the `loop` completes, the `counter` value is returned.

[conditional-expression]: https://docs.python.org/3/reference/expressions.html#conditional-expressions
[ternary-operator]: https://www.pythontutorial.net/python-basics/python-ternary-operator/
[value-error]: https://docs.python.org/3/library/exceptions.html#ValueError
