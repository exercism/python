# About

A [`function`][function] is a block of organized, reusable code that is used to perform a specific task.
`Functions` provide better modularity for your application and a high degree of code reuse.
Python, like other programming languages, has [_built-in functions_][build-in functions] ([`print`][print], [`map`][map], and so on) that are readily available.
You can also define your own functions. Those are called [`user-defined functions`][user defined functions].
Functions can run something as simple as _printing a message to the console_ or they can be quite complex.

To execute the code inside a function, you need to call the function, which is done by using the function name followed by parenthesese [`()`].
Data, known as [`arguments`][arguments], can be passed to the function by placing them inside the parenthesese.
A function definition may include zero or more [`parameters`][parameters].
Parameters define what argument(s) the function accepts.
A parameter defines what _type_ of argument is to be passed.
The argument is the actual _value_ passed when the function is called.
Functions can perform different tasks depending on the arguments passed to the parameters.

A function can also return a value using the [`return`][return] keyword.
The value returned by the function is known as the `return value`.
The return value is returned to the caller of the function.

## Creation

In python, functions are created using the [`def`][def] keyword.
The function definition is followed by the function name and parentheses [`()`].
Inside the parentheses, the parameters are specified, separated by commas.
After the close parenthesis, the colon (`:`) is used to separate the function signature from the function body.

The function body is a block of code that is executed when the function is called.
The body of the function is indented.
The indentation is important because Python relies on it to know where that block of code ends.
A value can be returned from the function by using the `return` keyword, which can then be used by the caller of the function.

```python
def function_name(parameter1, parameter2, ...):
    # function body
    return parameter1 + parameter2

```

We can also define a function without any parameters or return value.

```python
def function_name():
    # function body
    pass

```

Note that the function does need a body, even if the body does nothing, or trying to run the program will generate an indentation error:

```python
>>> def my_bodyless_func():
...      

File ~/temp.py:1
    
    ^
IndentationError: expected an indented block
```

## Calling a Function

To call a function, use the function name followed by parenthesese [`()`].
Parameters passed to the function are placed inside the parenthesese, separated by commas.

Consider the following function:

```python
def greet():
    print("Hello")

```

The above function can be called by using the following syntax:

```python
>>> greet()
Hello
```

## Parameters and their Arguments

Arguments are values that are passed to the function when it is called.
They can be of any data type, including other functions or classes.

Let's define a function `add` which adds two numbers together:

```python
def add(first, second):
    print(first + second)

```

The parameters `first` and `second` define what arguments the `add` function will accept.
(It should be noted that the words `parameter` and `argument` are often used interchangeably, albeit imprecisely.)
When the function is called, the arguments are passed to the function.
We need to pass arguments for both of the parameters, otherwise a [`TypeError`][type-error] will be raised.

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
TypeError: add() missing 1 required positional argument: 'second'

>>> add(2, 3, 4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add() takes 2 positional arguments but 3 were given
```

## Return Value

The return value is a value that is returned to the caller of the function.
A `return value` can be any data type including other functions or classes.
It can be used by caller of the function to perform further operations.
If a function does not explicitly define a `return value`, the value `None` will be returned by the Python interpreter.

Let's define a function `add`:

```python
def add(first, second):
    return first + second

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
>>> def show(first, second):
    print(first)
    return first
    print(second)

# second never gets printed, because the function exits after the return statement
>>> show(1, 2)
1
```

## Modularity

Complex programs can be broken down into smaller parts.
Different functions can be used to perform different specific tasks.

Assume a program has to perform the following tasks:

* Calculate the area of a circle
* Calculate the area of a rectangle
* Calculate the area of a triangle

We can break down the program into smaller parts.

```python
def circle_area(radius):
    return 3.14 * radius * radius

def rectangle_area(length, breadth):
    return length * breadth

def triangle_area(base, height):
    return 0.5 * base * height

```

Now, we can call the functions in the order we want.

```python
>>> circle_area(2)
12.56
>>> triangle_area(2, 3)
3.0
>>> rectangle_area(2, 3)
6
>>> rectangle_area(1, 2) + circle_area(2) + triangle_area(1, 2)
15.56
```

## Scope of Variables

If a variable (_or name_) is defined inside a function, it will be only accessible _inside_ the function scope (_or local namespace_), even if there is a variable with the same name outside the function scope.

Variables defined outside a function at the _module level_ are considered in the _global namespace_.
Variables defined outside a function but _inside_ an enclosing function or class are in the _nonlocal namespace_.


Python uses the [LEGB Rule][LEGB Rule] (**L**ocal, **E**nclosing, **G**lobal, **B**uilt-in) to resolve variable names when a program is running:

1. Lookup in the **local** (or _function_) namespace.
2. Lookup in the **enclosing** (or _nonlocal_) namespace if a name is not found in local.
3. Lookup in the **global** namespace (_module level_) if the name is not found in nonlocal/enclosing.
4. Lookup in the **built-in** (_program or python-wide_) namespace if the name is not found in global.

If the name remains unresolved, Python will raise a `NameError exception`.

```python
# Global namespace.
general_favorite = "apples"


def alices_favorite():
   # Local namespace.  
   favorite = "cherries"
   
   # This works because Python will eventually find general_favorite in the global namespace.
   # Python will find 'print' in the built-in namespace.
   print(f'Alice has always liked {favorite}, but most people like {general_favorite}.')

   
def our_favorite_fruits():
    # Enclosing or nonlocal namespace.
    yours = "peaches"
    
    def my_favorite():
        # Local namespace.
        mine = "pears"
        
        # This works because Python will eventually find 'yours' in the enclosing/nonlocal namespace.
        print(f'My favorite is {mine}, but you like {yours} instead.')
        
        # This works because Python will eventually find 'general_favorite' in the global namespace.
        print(f'Everyone seems to like {general_favorite}')
    
    # This function is in the local namespace of the 'our_favorite_fruits' function.  
    my_favorite()

    
# This will raise NameError: name 'favorite' is not defined, because the variable favorite is local to alices_favorite.
print(favorite)

```

If we want to make a variable name accessible _outside_ the local function scope (_or modify a variable that has been defined outside the function scope_), we need to use either the [`global`][global] or [`nonlocal`][nonlocal] keywords.

Using the `global` keyword signals Python to start the lookup in the _global namespace_.
Assignments to the variable will then modify the _global_ variable, instead of creating a _local_ version.
When `global` is used to declare a variable, the variable will be _added_ to the global namespace.
As a result, `global` should be used cautiously, as adding or modifying a global variable could have effects on all other code that uses its value.

The `nonlocal` keyword signals to Python to look for/create the variable in the _nonlocal or enclosing namespace_.
It is used when a function is nested inside another function or class, and needs access to the outer functions variables and scope.


## Functions as first class objects

In python, functions can be assigned to variables and passed as arguments to other functions.
They can be used as return values.
Functions can also be placed into a sequence([`list`][list], [`tuple`][tuple] etc) or as value in a [`dict`][dict].
Functions can be used anywhere any other object can be used.
This is because _functions are [_first class objects_][first class objects]_.
As such, they carry special attributes, and can even define getting and setting custom attributes of their own. 

```python
# print is a function

# A function can be assigned to a variable.
>>> function_as_variable = print
>>> function_as_variable("Hello")
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
    num = 10
    
    # This is a nested, or "inner" function.
    def inner():
        print(num)
    
    # Outer function calling inner function
    inner()
```

The inner function can access the variable `num` defined in the outer function.

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
>>> def add(first, second):
      return first + second

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

[LEGB Rule]: https://realpython.com/python-scope-legb-rule/
[arguments]: https://www.w3schools.com/python/gloss_python_function_arguments.asp
[attributes]: https://docs.python.org/3/reference/datamodel.html#index-33
[build-in functions]: https://docs.python.org/3/library/functions.html
[def]: https://www.geeksforgeeks.org/python-def-keyword/
[dict]: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
[first class objects]: https://en.wikipedia.org/wiki/First-class_object
[function]: https://docs.python.org/3/glossary.html#term-function
[global]: https://www.programiz.com/python-programming/global-keyword
[list]: https://docs.python.org/3/tutorial/datastructures.html#list-objects
[map]: https://docs.python.org/3/library/functions.html#map
[nonlocal]: https://www.geeksforgeeks.org/python-nonlocal-keyword/
[parameters]: https://www.codecademy.com/learn/flask-introduction-to-python/modules/learn-python3-functions/cheatsheet
[print]: https://docs.python.org/3/library/functions.html#print
[return]: https://www.geeksforgeeks.org/python-return-statement/
[tuple]: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
[type-error]: https://docs.python.org/3/library/exceptions.html#TypeError
[user defined functions]: https://en.wikipedia.org/wiki/User-defined_function
