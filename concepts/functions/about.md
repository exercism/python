# About

A [`function`][function] is a block of organized, reusable code that is used to perform a single, related action.
`Functions` provide better modularity for your application and a high degree of code reuse.
Like other programming languages, python provides _pre-defined functions_ ([`print`][print], [`map`][map] etc) that are readily available in the Python language. 
You can also define your own functions. Those are called [`user-defined functions`][user defined functions].
Functions can run something as simple as _printing a message to the console_ or they can be quite complex.

To execute the code inside a function, you need to call the function, which is done by using the function name followed by parenthesis [`()`].
Data. known as `parameters`, can be passed to the function by placing them inside the parenthesis. A broader term for parameters is `arguments`. Functions can perform different tasks depending on the value of the parameters.

A function can also return a value using the `return` keyword. The value returned by the function is known as the `return value`. The return value is returned to the caller of the function.

## Creation

In python, functions are created using the `def` keyword. The function definition is followed by the function name and parenthesis [`()`]. Inside the parenthesis, the parameters are specified, separated by commas. After the close parenthesis, the colon (`:`) is used to separate the function signature from the function body.

The function body is a block of code that is executed when the function is called. The body of the function is indented. The indentation is important because Python relies on it to know where that block of code ends. A value can be returned from the function by using the `return` keyword, which can then be used by the caller of the function.

```python
def function_name(parameter1, parameter2, ...):
    # function body
    return value
```

We can also define a function without any parameters or return value.
```python
def function_name():
    # function body
```


## Calling a Function

To call a function, use the function name followed by parenthesis [`()`]. Parameters passed to the function are placed inside the parenthesis, separated by commas.

Consider the following function:
```python
def wish():
    print("Hello")
```

The above function can be called by using the following syntax:
```python
>>> wish()
Hello
```

## Parameters

Parameters are values that are passed to the function when it is called. They are known as `arguments`.

Let's define a function `add` which adds two numbers together:
```python
def add(x, y):
    print(x + y)
```

When the function is called, the parameters are passed to the function. We need to pass values for both the parameters, otherwise a [`TypeError`][type-error] will be raised.
```python
>>> add(2, 3)
5

# Function can be called multiple times, with different parameters
>>> add(4, 3)
7
>>> add(5, 6)
11

# Passing an incorrect number of parameters will raise a `TypeError`
>>> add(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() missing 1 required positional argument: 'y'

>>> add(2, 3, 4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() takes 2 positional arguments but 3 were given
```

## Return Value

The return value is a value that is returned to the caller of the function. Return value can be of any data type. It can be used by caller of the function to perform further operations. If the function does not explicitly return a value, the value `None` is returned.

Let's define a function `add`:
```python
def add(x, y):
    return x + y
```

We can store the return value in a variable and then print it:
```python
>>> result = add(2, 3)
>>> print(result)
5
# Type of result is `int`
>>> type(result)
<class 'int'>

# We can also perform operations on the return value
>>> result * 2
10

# A function without an explicit return value will return `None`
>>> def log(message):
    print(message)

# Hello is printed because of print(message), but return value is `None`
>>> return_value = log("Hello")
Hello
>>> return_value
None
```

Use of `return` immediately exits the function and returns the value to the caller.
```python
>>> def show(x, y):
    print(x)
    return x
    print(y)

# y never gets printed, because the function exits after the return statement
>>> show(1, 2)
1
```

## Modularity

Complex programs can be broken down into smaller parts. Different functions can be used to perform different specific tasks.

Assume a program has to perform the following tasks:
  * Calculate the area of a circle
  * Calculate the area of a rectangle
  * Calculate the area of a triangle

We can break down the program into smaller parts.

```python
def circle_area(r):
    return 3.14 * r * r

def rectangle_area(length, breadth):
    return length * breadth

def triangle_area(base, height):
    return 0.5 * base * height
```

Now, we can call the functions in the order we want.

```python
>>> circle_area(2)
12.56
>>> rectangle_area(2, 3)
6
>>> triangle_area(2, 3)
1.5
```

## Scope of Variables

If variable is defined inside a function, then it will be only accessible inside the function. If we want to access the variable outside the function, we need to use the [`global`][global] keyword. [`nonlocal`][nonlocal] keyword is used to access the variable inside a nested function.

```python
def outer():
    x = 10
    print('Inside function:', x)
```

variable `x` is defined inside the outer function. It is limited to the scope of the outer function only. It will not alter the value of the variable outside the outer function.

```python
>>> x = 30

# regardless of whether we call the function or not, the value of x will be 30
>>> outer()
Inside function: 10
>>> x
30
```

We can access the variable inside the outer function using the `global` keyword.
```python
def outer():
    global x
    x = 10
    print('Inside function:', x)
```

As we have used the `global` keyword, the value of `x` will be changed.

```python
>>> x = 30
>>> outer()
Inside function: 10
>>> x
10
```


## Functions as first class objects

In python, functions can be assigned to variables and passed as arguments to other functions. They can be used as return values. Functions can also be placed into a sequence([`list`][list], [`tuple`][tuple] etc) or as value in a [`dict`][dict]. Functions can be used anywhere than any other object can be used. This is because _functions are [`first class objects`][first class objects]_.


```python
# print is a function

# A function can be assigned to a variable.
>>> fake_print = print
>>> fake_print("Hello")
Hello
>>> type(fake_print)
<class 'builtin_function_or_method'>

# Functions can be passed as an argument to another function.
>>> def check_print(func):
    func("Hello")
>>> check_print(print)
Hello

# Function can be used as an item in a sequence.
>>> my_list = [print, "Hello"]
>>> my_list[0]("Hello")
Hello

# Functions can be used as a value in a dictionary.
>>> my_dict = {"key": print}
>>> my_dict["key"]("Hello")
Hello

# Functions can be returned from a function.
>>> def return_func():
    return print
>>> return_func()("Hello")
Hello
```

Functions can also be nested inside other functions.
```python
def outer():
    x = 10
    def inner():
        print(x)
    inner()
```

The inner function can access the variable `x` defined in the outer function.

```python
>>> outer()
10
```

## Special Attributes

Functions in python have special attributes. Some of them are:
  * `__name__`: Name of the function
  * `__doc__`: Documentation string of the function
  * `__module__`: Module in which the function is defined
  * `__globals__`: Dictionary of global variables in the function
  * `__code__`: Code object containing the instructions of the function

```python
>>> def add(x, y):
      return x + y

# Function name
>>> print.__name__
'print'
>>> len.__name__
'len'
>>> add.__name__
'add'

# Function documentation
>>> abs.__doc__
'Return the absolute value of the argument.'

# Module
>>> len.__module__
'builtins'
>>> add.__module__
'__main__'
```

The full list of function attributes can be found at [Python DataModel][attributes].


[attributes]: https://docs.python.org/3/reference/datamodel.html#index-33
[first class objects]: https://en.wikipedia.org/wiki/First-class_object
[list]: https://docs.python.org/3/tutorial/datastructures.html#list-objects
[tuple]: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
[dict]: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
[global]: https://docs.python.org/3/reference/compound_stmts.html#global
[nonlocal]: https://docs.python.org/3/reference/compound_stmts.html#nonlocal
[function]: https://en.wikipedia.org/wiki/Function_(computer_science)
[print]: https://docs.python.org/3/library/functions.html#print
[map]: https://docs.python.org/3/library/functions.html#map
[user defined functions]: https://en.wikipedia.org/wiki/User-defined_function
[type-error]: https://docs.python.org/3/library/exceptions.html#TypeError
