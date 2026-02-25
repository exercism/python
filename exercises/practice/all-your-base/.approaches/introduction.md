# Introduction

The main aim of this exercise is to understand how non-negative integers work in different bases.

Given that mathematical understanding, the code to implement it can be relatively simple.

For this exercise, no attempt was made to benchmark performance, as this would distract from the main focus of writing clear, correct code.

## General guidance

Essentially all succesful solutions involve three steps:

1. Check that inputs are valid.
2. Convert the input list to a Python `int`.
3. Convert that `int` to an output list in the new base.

Some programmers prefer to separate the two conversions into separate functions, others put everything in a single function.

This is largely a matter of taste, and either structure can be made reasonably concise and readable.

## 1. Check the inputs

```python
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if not all( 0 <= digit < input_base for digit in digits) :
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if not output_base >= 2:
        raise ValueError("output base must be >= 2")

```

A valid number base must be `>=2` and all digits must be at least zero and strictly less than the number base.

For the familiar base-10 system, this means 0 to 9.

As implemented, the tests require that invalid input raise a `ValueError` with a suitable error message.

## 2. Convert the input digits to an `int`

These four code fragments all do essentially the same thing:

```python
# Simplest loop
    val = 0
    for digit in digits:
        val = input_base * val + digit

# Loop, separating the arithmetic steps
    val = 0
    for digit in digits:
        val *= input_base
        val += digit

# Sum a comprehension over reversed digits
    val = sum(digit * input_base ** pos for pos, digit in enumerate(reversed(digits)))

# Sum a comprehension with alternative reversing
    val = sum((digit * (input_base ** (len(digits) - 1 - i)) for i, digit in enumerate(digits)))
```

In the first two, the `val *= input_base` step essentially left-shifts all the previous digits, and `val += digit` adds a new digit on the right.

In the two comprehensions, an exponentation like `input_base ** pos` left-shifts the current digit to the appropriate position in the output.

*Please think about this until it makes sense:* these short code fragments are the main point of the exercise.

In each code fragment, the Python `int` is called `val`, a deliberately neutral identifier.

Surprisingly many students use names like `decimal` or `base10` for the intermediate value, which is misleading.

A Python `int` is an object with a complicated (but largely hidden) implementation.

There are methods to convert an `int` to string representations such as decimal, binary or hexadecimal, but the internal representation of `int` is certainly not decimal.

## 3. Convert the intermediate `int` to output digits

Now we have to reverse step 2, with a different base.

```python
    out = []

# Step forward, insert new digits at beginning
    while val > 0:
        out.insert(0, val % output_base)
        val = val // output_base

# Insert at end, then reverse
    while val:
        out.append(val % output_base)
        val //= output_base
    out.reverse()

# Use divmod()
    while val:
        div, mod = divmod(val, output_base)
        out.append(mod)
        val = div
    out.reverse()
```

Again, there are multiple code snippets shown above, which all do the same thing.

In each case, we essentially need the value and remainder of an integer division.

The first snippet above adds new digits at the start of the list, while the next two add at the end.

This is a choice of where to take the performance hit: appending to the end is a faster way to grow the list, but needs an extra reverse step.

The choice of append-reverse would be obvious in Lisp or SML, but the difference is less important in Python.

```python
# return, with guard for empty list
    return out or [0]
```

Finally, we return the digits just calculated.

A minor complcation is that a zero value should be `[0]`, not `[]`.

Here, we cover this case in the `return` statement, but it could also have been trapped at the beginning of the program, with an early `return`.

## Recursion option

```python
def base2dec(input_base: int, digits: list[int]) -> int:
    if not digits:
        return 0
    return input_base * base2dec(input_base, digits[:-1]) + digits[-1]


def dec2base(number: int, output_base: int) -> list[int]:
    if not number:
        return []
    return [number % output_base] + dec2base(number // output_base, output_base)
```

An unusual solution to the two conversions is shown above.

It works, and the problem is small enough to avoid stack overflow (Python has no tail recursion).

In practice, few Python programmers would take this approach in a language without the appropriate performance optimizations.

To simplify: Python only *allows* recursion, it does nothing to *encourage* it: in contrast to Scala, Elixir, and similar languages.

