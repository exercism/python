# About

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

# The comparison '>' here returns the bool False,
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

# The elif statement allows for the checking of more conditions.
if x > y > z:
    print("x is greater than y and z")
elif y > x > z:
    print("y is greater than x and z")
else:
    print("z is greater than x and y")
...
>>> z is greater than x and y
```

[Boolean operations][boolean operations] and [comparisons][comparisons] can be combined with conditionals for more complex testing:

```python

>>> def classic_fizzbuzz(number):
        if number % 3 == 0 and number % 5 == 0:
            say = 'FizzBuzz!'
        elif number % 5 == 0:
            say = 'Buzz!'
        elif number % 3 == 0:
            say = 'Fizz!'
        else:
            say = str(number)
        
        return say

>>> classic_fizzbuzz(15)
'FizzBuzz!'

>>> classic_fizzbuzz(13)
'13'
```

As an alternative, the example above can be re-written to only use `if` statements with `returns`.
However, re-writing in this way might obscure that the conditions are intended to be [_mutually exclusive_][mutually-exclusive] and could lead to future bugs or maintenance issues.


```python
>>> def classic_fizzbuzz(number):
        if number % 3 == 0 and number % 5 == 0:
            return 'FizzBuzz!'
        if number % 5 == 0:
            return 'Buzz!'
        if number % 3 == 0:
            return 'Fizz!'
        
        return str(number)

>>> classic_fizzbuzz(15)
'FizzBuzz!'

>>> classic_fizzbuzz(13)
'13'
```


Conditionals can also be nested.

```python
>>> def driving_status(driver_age, test_score):
        if test_score >= 80: 
            if 18 > driver_age >= 16:
                status = "Student driver, needs supervision."
            elif driver_age == 18:
                status = "Permitted driver, on probation."
            elif driver_age > 18:
                status = "Fully licensed driver."
        else:
             status = "Unlicensed!"
        
        return status


>>> driving_status(63, 78)
'Unlicensed!'

>>> driving_status(16, 81)
'Student driver, needs supervision.'

>>> driving_status(23, 80)
'Fully licensed driver.'
```

## Conditional expressions or "ternary operators"

While Python has no specific `?` ternary operator, it is possible to write single-line `conditional expressions`.
These take the form of `<value if True>` if `<conditional test>` else `<value if False>`.
Since these expressions can become hard to read, it's recommended to use this single-line form only if it shortens code and helps readability.


```python
def just_the_buzz(number):
    return 'Buzz!' if number % 5 == 0 else str(number)
    
>>> just_the_buzz(15)
'Buzz!'

>>> just_the_buzz(7)
'7'
```

## Truthy and Falsy

In Python, any object can be tested for [truth value][truth value testing], and can therefore be used with a conditional, comparison, or boolean operation.
Objects that are evaluated in this fashion are considered "truthy" or "falsy", and used in a `boolean context`.

```python
>>> def truthy_test(thing):
        if thing:
            print('This is Truthy.')
        else:
            print("Nope. It's Falsey.")


# Empty container objects are considered Falsey.
>>> truthy_test([])
Nope. It's Falsey.

>>> truthy_test(['bear', 'pig', 'giraffe'])
This is Truthy.

# Empty strings are considered Falsey.
>>> truthy_test('')
Nope. It's Falsey.

>>> truthy_test('yes')
This is Truthy.

# 0 is also considered Falsey.
>>> truthy_test(0)
Nope. It's Falsey.
```

[boolean operations]: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
[comparisons]: https://docs.python.org/3/library/stdtypes.html#comparisons
[control flow tools]: https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools
[if statement]: https://docs.python.org/3/reference/compound_stmts.html#the-if-statement
[mutually-exclusive]: https://stackoverflow.com/a/22783232
[truth value testing]: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
