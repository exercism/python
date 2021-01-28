## General

Programs without conditional statements run sequentially (i.e. the code is executed line by line). However, this doesn't allow for the implementation of more complex logic. Conditional statements allow the program to execute different lines of code based on some factors. Python uses `if/else` statements to achieve this.

Let's look at the basic structure of python's `if/else` .

```python
if <expression>:
    <code block 1 >
else:
    <code block 2>
```

Now look at the following examples

```python
x = 5
y = 10

if x > y:                           # expression is True
    print("x is greater than y")
>>> x is greater than y

if x < y:                           # expression is False
    print("x is lower than y")
>>>                                 # Nothing is executed

```

Here in the first `if` statement, the expression evaluates to `True`. Therefore, the statement associated with the `if` statement gets executed. In the next example, the expression evaluates to `False`, and therefore the statement associated with it is not executed.

## The indentation and blocks

The Python examples shown below are arranged into blocks using indentation. So, if there are multiple expressions that needs to be executed from one `if` statement we can put it in a block by having a uniform indentation throughout.

```python
if x > y:                           # expression is True
    print("x is greater than y")
    print("This is part of same block")
    print("This is part of same block")

print("this is not part of the if block")
```

## The else clause

So far we made a single `if` statement. What if we wanted a program to execute one statement if the expression evaluates to `True` or execute an another statement if the expression evaluates to `False`
In such scenarios we can use the `else` clause

```python

x = 5

if x > 10:                          # Expression evaluvates to False
    print("x is greater than 10")
else:
    print("x is less or equal than 10")      # Expression evaluates to True
>>> x is less or equal than 10

```

In this example we see that the `if` condition evaluates to `False` so the statement in the `else` block is executed.

A real world analogy to `if/else` statement is like this. If its sunny outside, then go to park. Otherwise read a book.

## The elif clause

Now that we have understood branching for sing `if` statement. What if we need to make several such alternatives in such cases we need to rely on `elif` clause. Which literally means else if. Here is an example using `elif`

```python
x = 20

if x < 5:
    print("x is less than 5")
elif x < 10:
    print("x is less than 10")
elif x < 30:
    print("x is less than 30")
else:
    print("None of the above")
>>> x is less than 30
```

Here first the code checks the first `if` condition. It finds that the expression evaluates to `False`. Therefore it goes into `elif` statement and sees if the expression inside `elif` evaluates to `True` if not it will continue to go through each `elif` expressions. If none of them evaluates to `True` then the conditional goes to the `else` clause and executes the statement in the `else` clause. Note that in the case where `elif` is used. The `else` clause can come only at the end of the expression.

## One line If statments

It is possible to write `if` conditionals in a single line ,However, as per the [PEP8][pep8-link] standards, the use of multiple statements on same lines are discouraged
[pep8-link]: https://www.python.org/dev/peps/pep-0008/#other-recommendations

Example

```python
x = 5
if x == 5: print("Came inside the if statement "); print("x equals 5 "); print("came to this part");
>>> Came inside the if statement x equals 5 came to this part
```

Here all the statements separated by a semicolon are considered as part of a single block. We can have more complicated ones like the example shown below. This is highly discouraging as this goes against Python's strength which is readability.

```python
x = 10
if x == 10: print('x '); print(' contains '); print(' 10')
    elif x == 20: print('x '); print(' contains '); print(' 20')
    else: print('x '); print(' contains '); print(' something else')

```

## Additional information

In the `if` clause python strictly doesn't need a `True/False` value. This will become evident with the following example.

```python

string = ""
string_1 = "Hello,World"

if string:
    print(string)
elif string_1:
    print(string_1)
else:
    print("All are empty")

>>> Hello,World
```

In this example we did not evaluate if condition like this `if str == "":`. Even then it's understood by Python that if a string is empty evaluate it to `False` and evaluate to `True` otherwise.

Here is another on some pythonic expressions inside `if`

```python
x = ["A", "B", "C"]

if "A" in x:
    print("A is inside x")
>>> A is inside x
```
