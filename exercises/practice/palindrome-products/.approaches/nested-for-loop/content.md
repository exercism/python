# Nested For Loop

```python
def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    result = 0
    answer = []
    for number_a in range(min_factor, max_factor+1):
        for number_b in range(min_factor, max_factor+1):
            if number_a * number_b >= result:
                test_value = str(number_a * number_b)
                if test_value == test_value[::-1]:
                    if number_a * number_b > result:
                        answer = []
                        result = int(test_value)
                    answer.append([number_a, number_b])
    if result == 0:
        result = None
    return (result, answer)


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    result = 0
    answer = []
    for number_a in range(min_factor, max_factor+1):
        for number_b in range(min_factor, max_factor+1):
            if number_a * number_b <= result or result == 0:
                test_value = str(number_a * number_b)
                if test_value == test_value[::-1]:
                    if number_a * number_b < result:
                        answer = []
                    result = int(test_value)
                    answer.append([number_a, number_b])
    if result == 0:
        result = None
    return (result, answer)
```

The `largest` and `smallest` functions are very similar here.
Although there are some small differences.

The `largest` function starts with checking if the min_factor is bigger than the max_factor.
If it is, it raises a [`ValueError`][value-error].

After that, it initializes the result to 0 and the answer to an empty list.
Then it starts a  `for in range` loop.
The outer `for` loop iterates over the range of numbers from min_factor to max_factor.
The inner `for` loop iterates over the same range of numbers.
Then it checks if the product of the two numbers is bigger than the result.
If it is, it converts the product to a string and checks if it is a palindrome.

We can check if a string is a palindrome by comparing it to its reverse.
There are multiple ways to reverse a string.
The most common way is to use [slice notation][slice-notation].
The slice notation is `string[start:stop:step]`.
You can read more about it in: [reverse string with slice][string-reverse].

If the string is a palindrome, the solution next checks if the product is bigger than the current result.
If the product is bigger, the answer list is cleared, and the current result is set to the most recent product.
Then it appends the two numbers to the answer list.

After the two for loops, it checks if the result is 0.
If it is, it sets the result to [`None`][none].
Then it returns the result and the answer.

The `smallest` one is very similar.
The differences are that it checks if the product is smaller than the result or if the result is 0.
And that it reset result outside of the if statement.
Instead of inside of it.

[none]: https://realpython.com/null-in-python/
[slice-notation]: https://www.learnbyexample.org/python-list-slicing/
[string-reverse]: https://realpython.com/reverse-string-python/#reversing-strings-through-slicing
[value-error]: https://docs.python.org/3/library/exceptions.html#ValueError
