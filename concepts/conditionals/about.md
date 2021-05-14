# About

The [conditionals][control flow tools] [`if`][if statement], `elif` (_a contraction of 'else and if'_) and `else` are used in Python to control the flow of execution and make decisions in a program.
Unlike many other programming langauges, Python versions 3.9 and below do not offer a formal case-switch statement, using multiple `elif` statements to serve a similar purpose.
Python 3.10 introduces a variant case-switch statement called `pattern matching`, which will be covered in another exercise.
Conditional statements pair with expressions and objects that must resolve to `True` or `False` -- either by returning a `bool` directly, or by evaluating ["truthy" or "falsy"][truth value testing].


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
if x > y:
    print("x is greater than y and z")
elif y > z:
    print("y is greater than x and z")
else:
    print("z is great than x and y")
...
>>> z is great than x and y
```

[Boolen operations][boolean operations] and [comparisons][comparisons] can be combined with conditionals for more complex testing:

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

Conditionals can also be nested.

```python
>>> def driving_status(driver_age, test_score):
        if test_score >= 80: 
            if 18 > driver_age >= 16:
                return "Student driver, needs supervision."
            elif driver_age == 18:
                return "Permitted driver, on probation."
            elif driver_age > 18:
                return "Fully licensed driver."
        else:
            return "Unlicensed!"


>>> driving_status(63, 78)
'Unlicsensed!'

>>> driving_status(16, 81)
'Student driver, needs supervision.'

>>> driving_status(23, 80)
'Fully licsensed driver.'
```

## Conditional expressions or "ternary operators"

While Python has no specific `?` ternary operator, it is possible to write single-line `conditional expressions`.
These take the form of `<value if True>` if `<conditional test>` else `<value if False>`.
Since these expressions can become hard to scan, it's recommended to use this single-line form only if it shortens code and helps readability.

```python
def just_the_buzz(number):
    return 'Buzz!' if number % 5 == 0 else str(number)
    
>>> just_the_buzz(15)
'Buzz!'

>>> just_the_buzz(10)
'10'
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


[if statement]: https://docs.python.org/3/reference/compound_stmts.html#the-if-statement
[control flow tools]: https://docs.python.org/3/tutorial/controlflow.html#more-control-flow-tools
[conditional statements in python]: https://realpython.com/python-conditional-statements/
[truth value testing]: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
[boolean operations]: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
[comparisons]: https://docs.python.org/3/library/stdtypes.html#comparisons

