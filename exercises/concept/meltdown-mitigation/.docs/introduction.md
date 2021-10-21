# Conditionals

In Python, [`if`][if statement], `elif` (_a contraction of 'else and if'_) and `else` statements are used to [control the flow][control flow tools] of execution and make decisions in a program.
Unlike many other programming languages, Python versions 3.9 and below do not offer a formal case-switch statement, instead using multiple `elif` statements to serve a similar purpose.

Python 3.10 introduces a variant case-switch statement called `pattern matching`, which will be covered separately in another concept.

Conditional statements use expressions that must resolve to `True` or `False` -- either by returning a `bool` directly, or by evaluating ["truthy" or "falsy"][truth value testing].

```python
x = 10
y = 5

# The comparison '>' returns the bool 'True',
# so the statement is printed.
if x > y:
    print("x is greater than y")
...
>>> x is greater than y
```

When paired with `if`, an optional `else` code block will execute when the original `if` condition evaluates to `False`:

```python
x = 5
y = 10

# The comparison '>' here returns the bool 'False',
# so the 'else' block is executed instead of the 'if' block.
if x > y:
    print("x is greater than y")
else:
    print("y is greater than x")
...
>>> y is greater than x
```

`elif` allows for multiple evaluations/branches.

```python
x = 5
y = 10
z = 20

# The 'elif' statement allows for the checking of more conditions.
if x > y:
    print("x is greater than y and z")
elif y > z:
    print("y is greater than x and z")
else:
    print("z is great than x and y")
...
>>> z is great than x and y
```

[Boolean operations][boolean operations] and [comparisons][comparisons] can be combined with conditionals for more complex testing:

```python

>>> def classic_fizzbuzz(number):
        if number % 3 == 0 and number % 5 == 0:
            return 'FizzBuzz!'
        elif number % 5 == 0:
            return 'Buzz!'
        elif number % 3 == 0:
            return 'Fizz!'
        else:
            return str(number)

>>> classic_fizzbuzz(15)
'FizzBuzz!'

>>> classic_fizzbuzz(13)
'13'
```

[if statement]: https://docs.python.org/3/reference/compound_stmts.html#the-if-statement
[control flow tools]: https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools
[truth value testing]: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
[boolean operations]: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
[comparisons]: https://docs.python.org/3/library/stdtypes.html#comparisons
