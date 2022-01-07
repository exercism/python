# About

Decorators are a feature of the Python language that can modify or register a function.

## How to use them

Decorators are placed just above a function in the code like so:

```python
@decorator
def function():
    pass
```

Some decorators take arguments:

```python
@decorator2(name="Bob")
def function2():
    pass
```

If a decorator takes any arguments, but you don't wish to pass any, you must still call it with parentheses for the decorator to work:

```python
@decorator3()
def function3():
    pass
```

Decorators are just syntactic sugar.
An alternative way of doing the same as the above three examples is using higher-order functions:
```python
def function():
    pass

function = decorator(function)


def function2():
    pass

function2 = decorator2(name="Bob")(function2)


def function3():
    pass

function3 = decorator3()(function3)
```

## How to write them

As said before, decorators can modify or register a function.
The simplest decorator however, does absolutely nothing.

Decorators are functions which return functions.
They take one argument - the function which they have been added to.
They also return one thing - the function which will be run by the program.
This is usually either the function they were added to or a slightly modified version of that function, but it does not have to be - it can be any function whatsoever.

The simplest decorator - one that does nothing - can be written as follows:
```python
def do_nothing(function):
    return function
```
```python
def function4a():
    return 4

@do_nothing
def function4b():
    return 4
```
```python
>>>function4a()
4
>>>function4b()
4
```
As you can see, both functions do the same thing, and when the decorator is added nothing changes.

A decorator that registers a function could be written as follows:
```python
functions = []

def register_function(function):
    functions.append(function)
    return function
```
```python
>>>functions
[]
```
```python
@register_function
def function5():
    return 5
```
```python
>>>functions
[<function function5 at 0x000001CA840AA700>]
>>>function5()
5
```
As you can see, adding the decorator to the function adds the function into the list.
It is important to note that this happens when the function is declared, not when it is called.

Many decorators you write will change what is run when the function is called.
These will need to return a different function to the one passed.
This different function is written inside the decorator's function.

This decorator doubles the result of the function:
```python
def double(function):
    def wrapper():
        function_result = function()
        doubled = function_result * 2
        return doubled
    return wrapper
```
```python
def function6a():
    return 6

@double
def function6b():
    return 6
```
```python
>>>function6a()
6
>>>function6b()
12
```
As you can see the decorator modifies the result of the function.

Now lets take a look at what is actually happening in this decorator.

On the first line, we have the normal function definition.
But, when we go inside this function and take a look at the next line, we get another function definition.
This function is what we will return at the end of the decorator.
This means we are not returning the original function.
Because of this, Python will not actually call the original function when a call is made to what looks like that function.
Instead, Python will call the function we created, `wrapper()`.

If we look inside our `wrapper()` function, we first see a call to the original function.
This call will do exactly the same as if we had called the original function without the decoration to the function.
Then we get a line that modifies this result.
Finally we return the modified result, which is what we get when calling the function.

If we apply this decorator to a function which takes a single number and triples it, then we should get a function that sextuples our number.
Lets see what happens:
```python
@double
def triple(number):
    return number * 3
```
```python
>>>triple(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: wrapper() takes 0 positional arguments but 1 was given
```
Unfortunately, we get an error.
This happens because, as said earlier, python does not call the original function when you appear to call it.
Python actually calls the function in the decorator, `wrapper()`, which does not have any parameters.

To rectify this, we can add a parameter to our `wrapper()` function.
An updated `@double` decorator is shown below:
```python
def double(function):
    def wrapper(value):
        function_result = function(value)
        doubled = function_result * 2
        return doubled
    return wrapper
```
```python
>>>triple(5)
30
```
However, if we now call our function which took no parameters earlier, it will fail:
```python
>>>function6b()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: wrapper() mising 1 required positional argument: 'value'
```
It would also fail for any other number of parameters too.

Fortunately we can write decorators that don't care about the number of parameters a function may take by using the `*args` and `**kwargs` syntax.
Here's an update `@double` decorator:
```python
def double(function):
    def wrapper(*args, **kwargs):
        function_result = function(*args, **kwargs)
        doubled = function_result * 2
        return doubled
    return wrapper
```
Now we should be to use this decorator on functions which accept zero, one, two or even one million (though we wouldn't recommend that many!) parameters:
```python
>>>triple(5)
30
>>>function6b()
12
```
