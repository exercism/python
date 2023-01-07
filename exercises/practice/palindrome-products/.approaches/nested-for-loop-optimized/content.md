# Nested For Loop Optimized

This approach shows that just a few changes can improve the running time of the solution significantly.

```python
def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    result = 0
    answer = []
    for number_a in range(max_factor, min_factor - 1,-1):
        was_bigger = False
        for number_b in range(max_factor, number_a - 1, -1):
            if number_a * number_b >= result:
                was_bigger = True
                test_value  = str(number_a * number_b)
                if test_value == test_value[::-1]:
                    if number_a * number_b > result:
                        answer = []
                        result = int(test_value)
                    answer.append([number_a, number_b])
        if not was_bigger:
            break
    if result == 0:
        result = None
    return (result, answer)


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    result = 0
    answer = []
    for number_a in range(min_factor, max_factor+1):
        was_smaller = False
        for number_b in range(min_factor, max_factor+1):
            if number_a * number_b <= result or result == 0:
                was_smaller = True
                test_value = str(number_a * number_b)
                if test_value == test_value[::-1]:
                    if number_a * number_b < result:
                        answer = []
                    result = int(test_value)
                    answer.append([number_a, number_b])
        if not was_smaller:
            break
    if result == 0:
        result = None
    return (result, answer)
```

This approach is very similar to the [nested for loop approach][approach-nested-for-loop], but it has a few optimizations.
To optimize the `largest` function, we have to start the inner loop from the maximum factor and proceed down to the minimum factor.
This allows us to stop the inner loop earlier than before.
We also set the minimum value in the _inner_ loop to the current value of the _outer_ loop.

Here is an example of how the algorithm works and why the loops need to be modified.
Say we take maximum to be 99 and the minimum 10.
In the first round:

```
x = [99 , 98, 97 ...]
y = [99]
```

And already we have our result: `9009[91,99]`
Although the loops have to continue to make us sure there are no higher values.

```
x = [98, 97, 96 ...]
y = [99, 98]
...
x = [90, 89, 88 ...]
y = [99, 98,97,96,95,94,93,92,91,90]

Here we can see that the highest value for this "run" is 90 \* 99 = 8910.
Meaning that running beyond this point won't give us any values higher than 9009.

That is why we introduce the `was_bigger` variable.
With `was_bigger`, we can check if the inner loop has a bigger value than the current result.
If there has not been a bigger value, we can stop the inner loop and stop the outer loop.
We do that by using the [`break`][break] statement.

If we hadn't modified the direction of the inner loop, it would have started from the minimum factor and gone up to the maximum factor.
This would mean that for every new run in the outer loop, the values would be bigger than the previous run.

The `smallest` function is optimized in a similar way as `largest` function compared to the original approach.
The only difference is that we have to start the inner loop and outer loop from the minimum factor and go up to the maximum factor.
Since what we want is the smallest value, we have to start from the smallest value and go up to the biggest value.

[approach-nested-for-loop]: https://exercism.org/tracks/python/exercises/palindrome-products/approaches/nested-for-loop
[break]: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
