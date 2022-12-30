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

If it is, then it raises a [`ValueError`][value-error].
After that we declare a counter variable and set it to zero.

Then we start a `while` loop that will run until the number is equal to one.
Meaning the loop wont run if the number is already one.

Inside of the loop we have a [ternary operator][ternary-operator].
The ternary operator is a one-line `if` and `else` statement.
That means that we can make the code more concise by using it.
We declare that number is equal to the result of the ternary operator.
The ternary operator checks if the number is even.
If it is, then we divide it by two.
If it isn't, then we multiply it by three and add one.
After that we increment the counter by one.
After the loop is done, we return the counter variable.

[ternary-operator]: https://www.pythontutorial.net/python-basics/python-ternary-operator/
[value-error]: https://docs.python.org/3/library/exceptions.html#ValueError
