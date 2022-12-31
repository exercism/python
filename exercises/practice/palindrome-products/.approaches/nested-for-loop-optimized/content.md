# Nested For Loop Optimized

The point of this approach is to show with just a few changes, the runtime can be improved by a lot.

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

This approach is very similar to the [nested for loop approach][approach-nested-for-loop], but it has a few optimizations that make it faster.
To optimize the largest function, we have to start the inner loop from the maximum factor and go down to the minimum factor.
This way, we can stop the inner loop earlier than before.
We also in the inner loop set the minimum value to the current value of the outer loop.

Here is an example of how the algorithm work and why we have to modify the loops.
Say we take max to be 99 and min 10.
It would go first round:

```
x => [99 , 98, 97 ...]
y => [99]
```

And already here we have our result which is `9009[91,99]`
Although the loops has to continue to make us sure there are no higher value.

```
x => [98, 97, 96 ...]
y => [99, 98]
...
x => [90, 89, 88 ...]
y => [99, 98,97,96,95,94,93,92,91,90]
```

Here we can see that the highest value for this "run" is 90 \* 99 = 8910.
Meaning running beyond this point wont give us any higher value than 9009.

That is why we introduce the `was_bigger` variable.
With that variable we can check the inner loop if it has been bigger than the current result.
If there has not been a bigger value, we can stop the inner loop and stop the outer loop.
We do that by using the [`break`][break] statement.

If we hadn't modified the inner loop, it would have started from the minimum factor and gone up to the maximum factor.
This would mean that for every new run in the outer loop, the values would be bigger than the previous run.

The smallest function is optimized in a similar way as largest function compared to the original approach.
The only difference is that we have to start the inner loop and outer loop from the minimum factor and go up to the maximum factor.
Since what we want is the smallest value, we have to start from the smallest value and go up to the biggest value.

[approach-nested-for-loop]: https://exercism.org/tracks/python/exercises/palindrome-products/approaches/nested-for-loop
[break]: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
