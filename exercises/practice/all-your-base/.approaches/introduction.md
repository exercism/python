# Introduction

The main aim of `All Your Base` is to understand how non-negative integers work in different bases.
Given that mathematical understanding, implementation can be relatively straightforward.


For this approach and its variations, no attempt was made to benchmark performance as this would distract from the main focus of writing clear, correct code for conversion.


## General guidance

All successful solutions for base conversion involve three steps:

1. Check that inputs are valid (no non-integer or negative values).
2. Convert the input list to a Python `int`, per the examples given in the instructions.
3. Convert the `int` from step 2 into an output list in the new base.

Some programmers prefer to separate the two conversions into separate functions, others put everything in a single function.
This is largely a matter of taste, and either structure can be made reasonably concise and readable.


## 1. Checking the inputs

Solution code should check that the input base is at least 2, and that the output base is 2 or greater.
Bases outside the range should rase `ValueError`s for input base and output base respectively.

```python
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if not all( 0 <= digit < input_base for digit in digits) :
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if not output_base >= 2:
        raise ValueError("output base must be >= 2")

```

Additionally, all input numbers should be positive integers greater or equal to 0 and strictly less than the given number base.
For the familiar base-10 system, that would mean 0 to 9.
As implemented, the tests require that invalid inputs raise a `ValueError` with  "all digits must satisfy 0 <= d < input base" as an error message.


## 2. Convert the input digits to an `int`

The next step in the conversion process requires that the input list of numbers be converted into a single integer.
The four code fragments below all show variations of this conversion:

```python
# Simple loop
    value = 0
    for digit in digits:
        value = input_base * value + digit

# Loop, separating the arithmetic steps
    value = 0
    for digit in digits:
        value *= input_base
        value += digit

# Sum a generator expression over reversed digits
    value = sum(digit * input_base ** position for position, digit in enumerate(reversed(digits)))

# Sum a generator expression with alternative reversing
    value = sum(digit * (input_base ** (len(digits) - 1 - index)) for index, digit in enumerate(digits))
```

In the first two, the `value *= input_base` step essentially left-shifts all the previous digits, and `value += digit` adds a new digit on the right.
In the two generator expressions, an exponentation like `input_base ** position` left-shifts the current digit to the appropriate position in the output.


````exercism/note

It is important to think about these procedures until they makes sense: these short code fragments are the main point of the exercise. 
In each code fragment, the Python `int` is called `value`, a deliberately neutral identifier. 
Surprisingly many students use names like `decimal` or `base10` for the intermediate value, which is misleading.  

A Python `int` is an object with a complicated (but largely hidden) implementation.
There are methods to convert an `int` to string representations such as octal, binary or hexadecimal, but these do not change the internal representation.
````


## 3. Convert the intermediate `int` to output digits

The `int` created in step 2 can now be reversed, using a different base.

Again, there are multiple code snippets shown below, which all do the same thing (essentially).
In each case, we need the value and the remainder of integer division.
The first snippet adds new digits at the start of the `list`, while the next two add them at the end.
The final snippet uses [`collections.deque()`][deque] to prepend, then converts to a `list` in the `return` statement.


These snippets represent choices of where to take the performance hit: appending to the end is a **much** faster and more memory efficient way to grow a `list` (O(1)), but the solution then needs an extra reverse step, incurring O(n) performance for the reversal.
_Prepending_ to the `list` is very expensive, as every addition needs to move all other elements of the list "over" into new memory.
The `deque` has O(1) prepends and appends, but then needs to be converted to a `list` before being returned, which is an  O(n) operation.


```python
from collections import deque


out = []

# Step forward, insert new digits at index 0 (front of list).
# Least performant, and not recommended for large amounts of data.
    while value > 0:
        out.insert(0, value % output_base)
        value = value // output_base

# Append values to the end (mor efficient), then reverse the list.
    while value:
        out.append(value % output_base)
        value //= output_base
    out.reverse()

# Use divmod() and reverse list, same efficiency a above.
    while value:
        div, mod = divmod(value, output_base)
        out.append(mod)
        value = div
    out.reverse()
    
# Use deque() for effcient appendleft(), convert to list.
    converted_digits = deque()

    while number > 0:
        converted_digits.appendleft(number % output_base)
        number  = number // output_base

    return list(converted_digits) or [0]
```


Finally, we return the digits just calculated.

A minor complication is that a zero value needs to be `[0]`, not `[]` according to the tests.
Here, we cover this case in the `return` statement, but it could also have been trapped at the beginning of the program, with an early `return`:


```python
# return, with guard for empty list
    return out or [0]
```

## Recursion option

An unusual solution to the two conversions is shown below.
It works, and the problem is small enough to avoid stack overflow (Python has no tail recursion).


In practice, few Python programmers would take this approach without carefully thinking about the bounds of the program and any possible memoization/performance optimizations they could take to avoid issues.
While Python *allows* recursion, it does nothing to *encourage* it, and the default recursion limit is set to only 1000 stack frames.


```python
def base_to_dec(input_base, digits):
    if not digits:
        return 0
    return input_base * base_to_dec(input_base, digits[:-1]) + digits[-1]


def dec_to_base(number, output_base):
    if not number:
        return []
    return [number % output_base] + dec_to_base(number // output_base, output_base)
```

[deque]: https://docs.python.org/3/library/collections.html#collections.deque

