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

After that, a counter variable is assigned to zero.
Then we start a `while` loop that will run until the number is equal to one.
Meaning the loop won't run if the number is already one.

Inside the loop we have a [ternary operator][ternary-operator] or [conditional expression][conditional-expression].
A ternary operator/conditional expression can be viewed as a one-line `if/else` statement.
Using a one-line construct can make the code more concise.

We assign the number value to the result of the ternary operator.
The ternary operator/conditional expression checks if the number is even.
If it is, then we divide it by two.
If the number is not even, we multiply by three and add one.
Then the counter is incremented by one.
When the loop completes, we return the counter value.

[ternary-operator]: https://www.pythontutorial.net/python-basics/python-ternary-operator/
[value-error]: https://docs.python.org/3/library/exceptions.html#ValueError
