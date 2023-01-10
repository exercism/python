# If / Else

```python
def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    counter = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1
        counter += 1
    return counter
```

This approach starts with checking if the number is less than or equal to zero.
If it is, then it raises a [`ValueError`][value-error].
After that, we declare a counter variable and set it to zero.
Then we start a [`while` loop][while-loop] that will run until the number is equal to one.
Meaning the loop won't run if the number is already one.

Inside the loop we check if the number is even.
If it is, then we divide it by two.
If it isn't, then we multiply it by three and add one.
After that, we increment the counter by one.
After the loop completes, we return the counter variable.

We use a `while` loop here because we don't know exactly how many times the loop will run.

[value-error]: https://docs.python.org/3/library/exceptions.html#ValueError
[while-loop]: https://realpython.com/python-while-loop/
