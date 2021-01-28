## Conditionals

Conditionals are the most common statements used in programming. Conditionals determine the flow of control in a program. In python the `if` statement is used to control the flow of execution. An important aspect of conditions in an `if` statement is that it will be resolved to a `boolean` type to determine the flow of execution.

The basic syntax of an `if` statement is as follows

```python
x = 10
y = 5
# Variant 1
if x > y:
    print("x is greater than y")

>>> x is greater than y

# Variant 2
x = 5
y = 10

if x > y:
    print("x is greater than y")
else:
    print("y is greater than x")

>>> y is greater than x

# Variant 3
x = 5
y = 10
z = 20
if x > y:
    print("x is greater than y and z")
elif y > z:
    print("y is greater than x and z")
else:
    print("z is great than x and y")
>>> z is great than x and y
```

There are mainly 3 variants of the `if` statement as seen in above example

- Single `if` statement
- `if` with `else` clause
- `if` with `elif` clause
