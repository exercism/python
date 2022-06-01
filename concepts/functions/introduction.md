# Introduction

A [`function`][function] is a way to compartmentalize code so it can be called by name from one or more places in the program.
Functions are used to perform specific and repetitive tasks.

More formally: a function is any Python object to which the [`function call`][calls] operation can be applied.
A function may be used to [`return`][return] one or more values as a result of some operation(s), or it may be used for one or more [`side effects`][side effects].
If a function does not specify a return value it will still return `None`. 

Following is an example of a function with a side effect:

```python
>>> def hello():
...        print("Hello")
...
>>> hello()
Hello

```

In the example above, the [`def`][def] keyword is used to signal the beginning of the function definition.
`hello` is the name of the function.
The empty parentheses represent that no values are being passed to the function.
The body of the function is the single `print("Hello")` statement.
`print` is also a function.
The `"Hello"`  in the `print` function's parentheses is known as an [`argument`][arguments].
The argument is used by the `print` function to know what to print.
Note that the body of the function is indented.
The indentation is important because Python relies on it to know where that block of code ends.
The function body ends at either the end of the program or just before the next line of code that is _not_ indented.
Since `hello()` does not specify a `return` value, it executes its side effect - which is calling `print()`  -- and then returns `None`.
Finally, we call the function by using its name and the parentheses.

Following is an example of a function with a return value:

```python
>>> def hello():
...     return "Hello"
... 
print(hello())
Hello

```

The body of the function has been changed from calling `print` to returning `"Hello"`.
The program still prints `"Hello"`, but the side effect takes place in the calling code instead of in the `hello` function.
If the parentheses were left off from  calling the `hello` function (e.g. `print(hello)`), then `print` would output something like

```
<function hello at 0x0000026E18E93E20>
```

It's important that, even if a function accepts no arguments, the empty parentheses must be used to call it correctly.
This is different from a language such as Ruby which does not require empty parentheses for calling a function without any arguments.

A function can define zero or more [`parameters`][parameters]. A parameter defines what argument(s) the function accepts.

Following is an example of a function which accepts an argument:

```python
>>> def hello(name):
...     return f"Hello, {name}"
... 
>>>print(hello("Bob"))
Hello, Bob

```

The parameter is defined as `name`.
`"Bob"` is the argument which the program passes to the `hello` function.
The program outputs `Hello, Bob`.

What if someone calls `hello` without passing an argument?
The program would error with a report that an argument is missing.
If we don't want the program to error with no argument (_but want to allow the calling code to not supply one_), we can define a [default argument][default arguments].
A default argument defines what value to use if the argument is missing when the function is called.

Following is an example of a function with a default argument:

```python
>>> def hello(name="you"):
...     return f"Hello, {name}"
... 
>>> print(hello())
Hello, you

```

The `name` parameter is given the default argument of `"you"`, so the program outputs `Hello, you`, if not passed a `name` argument.

For more about function arguments, please see the [function arguments][function arguments] concept.


[arguments]: https://www.w3schools.com/python/gloss_python_function_arguments.asp
[built-in functions]: https://docs.python.org/3/library/functions.html
[calls]: https://docs.python.org/3/reference/expressions.html#calls
[def]: https://www.geeksforgeeks.org/python-def-keyword/
[default arguments]: https://www.geeksforgeeks.org/default-arguments-in-python/
[first-class objects]: https://realpython.com/lessons/functions-first-class-objects-python/
[function]: https://docs.python.org/3/glossary.html#term-function
[function arguments]: ../function-arguments/about.md
[function-definitions]: https://docs.python.org/3/reference/compound_stmts.html#function-definitions
[parameters]: https://www.codecademy.com/learn/flask-introduction-to-python/modules/learn-python3-functions/cheatsheet
[return]: https://www.geeksforgeeks.org/python-return-statement/
[side effects]: https://runestone.academy/ns/books/published/fopp/Functions/SideEffects.html
