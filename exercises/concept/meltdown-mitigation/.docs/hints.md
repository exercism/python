# Hints

## General

- The Python Docs on [Control Flow Tools][control flow tools] and the Real Python tutorial on [conditionals][real python conditionals] are great places to start.
- The Python Docs on [Boolean Operations][boolean operations] can be a great refresher on `bools`, as can the Real Python tutorial on [booleans][python booleans].
- The Python Docs on [Comparisons][comparisons] and [comparisons examples][python comparisons examples] can be a great refresher for comparisons.

## 1. Check for criticality

- Comparison operators and boolean operations can be combined and used with conditionals.
- Conditional expressions must evaluate to `True` or `False`.
- `else` can be used for a code block that will execute when all conditional tests return `False`.

  ```python
     >>> item = 'blue'
     >>> item_2 = 'green'
     
     >>>  if len(item) >=3 and len(item_2) < 5:
            print('Both pass the test!')
          elif len(item) >=3 or len(item_2) < 5:
            print('One passes the test!')
          else:
            print('None pass the test!')
    ...
    One passes the test!
  ```

## 2. Determine the Power output range

- Comparison operators can be combined and used with conditionals.
- Any number of `elif` statements can be used as "branches".
- Each "branch" can have a separate `return`

## 3. Fail Safe Mechanism

- Comparison operators can be combined and used with conditionals.
- Any number of `elif` statements can be used as "branches".
- Each "branch" can have a separate `return`


[python comparisons examples]: https://www.tutorialspoint.com/python/comparison_operators_example.htm
[boolean operations]: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
[comparisons]: https://docs.python.org/3/library/stdtypes.html#comparisons
[python booleans]: https://realpython.com/python-boolean/
[real python conditionals]: https://realpython.com/python-conditional-statements/
[control flow tools]: https://docs.python.org/3/tutorial/controlflow.html

