# Reading and Troubleshooting Stack Traces in Python

## Frame Object

When a function is called, a frame object is created to hold the local variables and arguments passed to a function.
When the function is returns, the frame object is destroyed.
When function `B` is called within function `A`, function `B`'s values are put into a frame object, which is then placed on top of function `A`'s frame object on the call stack.

## Call Stack

The call stack is a collection of frame objects for the currently active functions.
If function `A` has called function `B` and function `B` has called function `C`, then the frame objects for all three functions will be on the call stack.
Once function `C` returns, then its frame object will be popped off the stack and only the frame objects for functions `A` and `B` will remain on the call stack.

## Traceback

A Traceback is a report of all the frame objects on the stack at a specific time.
When a Python program encounters an unhandled exception, it will print the exception message and a Traceback.
The Traceback will show where the exception was raised and what functions were called leading up to it.

## How to Read a Traceback

`ValueError` is a common exception.

The following is an example of `ValueError` resulting from trying to assign two variables on the left from only one value on the right:

```python
>>> first, second = [1]
Traceback (most recent call last):
File <stdin>, line 1, in <module>
    first, second = [1]
ValueError: not enough values to unpack (expected 2, got 1)

```

Tracebacks are organized with the most recent call is last, so the place to start reading the Traceback is with the exception at the bottom.
By reading upwards from there, we can see how that statement was reached.
If we place the offending line in a function and then call the function we see a longer trace:

```python
>>> def my_func():
...     first, second = [1]
...
>>> my_func()
Traceback (most recent call last):
  File <stdin>, line 5, in <module>
    my_func()
  File <stdin>, line 2, in my_func
    first, second = [1]
ValueError: not enough values to unpack (expected 2, got 1)

```

Working backwards from the bottom, we see that the call where the exception happened is on line 2 in `my_func`.
We got there by calling `my_func` on line 5.

## Common Exceptions

Python defines over 60 [built-in exception classes][exception-hierarchy].
Here is a brief overview of some of the more common exceptions and what they indicate.

### **SyntaxError**

Python raises a `SyntaxError` when it is unable to understand the code due to invalid syntax.
For example, there may be an open parenthesis without a matching closing parenthesis.


<details>
<summary>Click here for a code example.</summary>


Running this code:

```python
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length."  # This is missing the closing parenthesis
```

will result in a stack trace similar to this (_note the message on the final line_):

```
.usr.local.lib.python3.10.site-packages._pytest.python.py:608: in _importtestmodule
    mod = import_path(self.path, mode=importmode, root=self.config.rootpath)
.usr.local.lib.python3.10.site-packages._pytest.pathlib.py:533: in import_path
    importlib.import_module(module_name)
.usr.local.lib.python3.10.importlib.__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1050: in _gcd_import ???
<frozen importlib._bootstrap>:1027: in _find_and_load ???
<frozen importlib._bootstrap>:1006: in _find_and_load_unlocked ???
<frozen importlib._bootstrap>:688: in _load_unlocked ???
.usr.local.lib.python3.10.site-packages._pytest.assertion.rewrite.py:168: in exec_module
    exec(co, module.__dict__)
.mnt.exercism-iteration.hamming_test.py:3: in <module>
    from hamming import (  
E     File ".mnt.exercism-iteration.hamming.py", line 10
E       raise ValueError("Strands must be of equal length."
E                       ^
E   SyntaxError: '(' was never closed
```


</details>


### **AssertionError**
Python raises an `AssertionError` when an `assert` statement (see below) fails.


<details>
<summary>Click here for a code example.</summary>


Running this code:

```python
def distance(strand_a, strand_b):
    assert len(strand_a) == len(strand_b)


distance("ab", "abc")
```

will result in a stack trace similar to this (_note the message on the final line_):

```
hamming_test.py:3: in <module>
    from hamming import (
hamming.py:5: in <module>
    distance("ab", "abc")
hamming.py:2: in distance
    assert len(strand_a) == len(strand_b)
E   AssertionError
```


</details>


### **AttributeError**
An `AttributeError` is raised when code (or a unit test!) tries to access the attribute of an object but that object has no such attribute.
For example, a unit test expects a `Robot` object to have a `direction` attribute, but when it tried to access `robot.direction`, it does not exist.

This could also indicate a typo, such as using `"Hello".lowercase()` when the correct syntax is `"Hello".lower()`.
`"Hello".lowercase()` raises `AttributeError: 'str' object has no attribute 'lowercase'`.


<details>
<summary>Click here for a Robot class example.</summary>


Running this code:

```python
class Robot:
    def __init__():
        #note that there is no self.direction listed here
        self.position = (0, 0)
        self.orientation = 'SW'

    def forward():
        pass
        

robby = Robot
robby.direction
```

will result in a stack trace similar to this (_note the message on the final line_):

```
robot_simulator_test.py:3: in <module>
    from robot_simulator import (
robot_simulator.py:12: in <module>
    robby.direction
E   AttributeError: type object 'Robot' has no attribute 'direction'
```


</details>


<details>
<summary>Click here for a string example.</summary>


Running this code:

```python
def distance(strand_a, strand_b):
    if strand_a.lowercase() == strand_b:
        return 0


distance("ab", "abc")
```

will result in a stack trace similar to this (_note the message on the final line_):

```
    def distance(strand_a, strand_b):
>       if strand_a.lowercase() == strand_b:
E       AttributeError: 'str' object has no attribute 'lowercase'
```


</details>



### **ImportError**
An `ImportError` is raised when code tries to import something, but Python is unable to do so.
For example, a unit test for `Guidos Gorgeous Lasagna` does `from lasagna import bake_time_remaining`, but the `lasgana.py` solution file might not define `bake_time_remaining`.


<details>
<summary>Click here for code example</summary>


Running the `lasgana.py` file without the defined function would result in the following error:

```python
We received the following error when we ran your code:

  ImportError while importing test module '.mnt.exercism-iteration.lasagna_test.py'.
Hint: make sure your test modules.packages have valid Python names.

Traceback:
.mnt.exercism-iteration.lasagna_test.py:6: in <module>
    from lasagna import (EXPECTED_BAKE_TIME,
E   ImportError: cannot import name 'bake_time_remaining' from 'lasagna' (.mnt.exercism-iteration.lasagna.py)

During handling of the above exception, another exception occurred:
.usr.local.lib.python3.10.importlib.__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
.mnt.exercism-iteration.lasagna_test.py:23: in <module>
    raise ImportError("In your 'lasagna.py' file, we can not find or import the"

E   ImportError: In your 'lasagna.py' file, we can not find or import the function named 'bake_time_remaining()'. Did you mis-name or forget to define it?
```

### **IndexError**

Python raises an `IndexError` when an invalid index is used to look up a value in a sequence.
This often indicates the index is not computed properly and is often an off-by-one error.


<details>
<summary>Click here for code example</summary>


Consider the following code.

```python
def distance(strand_a, strand_b):
    same = 0
    for i in range(len(strand_a)):
        if strand_a[i] == strand_b[i]:
            same += 1
    return same


distance("abc", "ab")  # Note the first strand is longer than the second strand.
```

Running that code will result in an error similar to this one.
(_Note the last line._)

```
hamming_test.py:3: in <module>
    from hamming import (
hamming.py:9: in <module>
    distance("abc", "ab")  # Note the first strand is longer than the second strand.
hamming.py:4: in distance
    if strand_a[i] == strand_b[i]:
E   IndexError: string index out of range
```


</details>


### **KeyError**
Similar to `IndexError`, this exception is raised when using a key to look up a dictionary value but the key is not set in the dictionary.


<details>
<summary>Click here for code example</summary>


Consider the following code.

```python
def to_rna(dna_letter):
    translation = {"G": "C", "C": "G", "A": "U", "T": "A"}
    return translation[dna_letter]


print(to_rna("Q"))  # Note, "Q" is not in the translation.
```

Running that code will result in an error similar to this one.
(_Note the last line._)

```
rna_transcription_test.py:3: in <module>
    from rna_transcription import to_rna
rna_transcription.py:6: in <module>
    print(to_rna("Q"))
rna_transcription.py:3: in to_rna
    return translation[dna_letter]
E   KeyError: 'Q'
```

</details>


### **TypeError**
Typically, a `TypeError` is raised when the wrong type of data is passed to a function or used in an operation.



<details>
<summary>Click here for code example</summary>


Consider the following code.

```python
def hello(name):  # This function expects a string.
    return 'Hello, ' + name + '!'


print(hello(100))  # 100 is not a string.
```

Running that code will result in an error similar to this one.
(_Note the last line._)

```
hello_world_test.py:3: in <module>
    import hello_world
hello_world.py:5: in <module>
    print(hello(100))
hello_world.py:2: in hello
    return 'Hello, ' + name + '!'
E   TypeError: can only concatenate str (not "int") to str
```


</details>


### **ValueError**
A `ValueError` is usually raised when an invalid value is passed to function.


<details>
<summary>Click here for code example</summary>


Note, real square roots only exist for positive numbers.
Calling `math.sqrt(-1)` will raise `ValueError: math domain error` since `-1` is not a valid value for a square root.
In (mathematical) technical terms, -1 is not in the domain of square roots.


```python
import math

math.sqrt(-1)
```

Running that code will result in an error similar to this one.
(_Note the last line._)

```
square_root_test.py:3: in <module>
    from square_root import (
square_root.py:3: in <module>
    math.sqrt(-1)
E   ValueError: math domain error
```


</details>


## Using the `print` function

Sometimes an error is not being raised, but a value is not what is expected.
This can be especially perplexing if the value is the result of a chain of calculations.
In such a situation it can be helpful to look at the value at each step to see which step is the one that isn't behaving as expected.
The [print][print] function can be used for printing the value to the console.
The following is an example of a function that doesn't return the value expected:

```python
# the intent is to pass an integer to this function and get an integer back
def halve_and_quadruple(num):
    return (num / 2) * 4
```

When the function is passed `5`, the expected value is `8`, but it it returns `10.0`.
To troubleshoot, the calculating is broken up so that the value can be inspected at every step.

```python
# the intent is to pass an integer to this function and get an integer back
def halve_and_quadruple(num):
    # verify the number in is what is expected
    # prints 5
    print(num)
    # we want the int divided by an integer to be an integer
    # but this prints 2.5! We've found our mistake.
    print(num / 2)
    # this makes sense, since 2.5 x 4 = 10.0
    print((num / 2) * 4)
    return (num / 2) * 4

What the `print` calls revealed is that we used `/` when we should have used `//`, the [floor divison operator][floor divison operator].

## Logging

[Logging][logging] can be used similarly to `print`, but it is more powerful.
What is logged can be configured by the logging severity (e.g., 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'.)
A call to the `logging.error` function can pass `True` to the `exc_info` parameter, which will additionally log the stack trace.
By configuring multiple handlers, logging can write to more than one place with the same logging function.

Following is an example of logging printed to the console:

```python

>>> import logging
>>>
>>> # configures minimum logging level as INFO
>>> logging.basicConfig(level=logging.INFO)
>>>
>>> def halve_and_quadruple(num):
...     # prints INFO:root: num == 5
...     logging.info(f" num == {num}")
...     return (num // 2) * 4
...
>>> print(halve_and_quadruple(5))

```

The level is configured as `INFO` because the default level is `WARNING`.
For a persistent log, the logger can be configured to write to a file, like so:

```python
>>> import logging
...
>>> # configures the output file name to example.log, and the minimum logging level as INFO
>>> logging.basicConfig(filename='example.log', level=logging.INFO)
...
... def halve_and_quadruple(num):
...     # prints INFO:root: num == 5 to the example.log file
...     logging.info(f" num == {num}")
...     return (num // 2) * 4
...
>>> print(halve_and_quadruple(5))
```

## assert

[`assert`][assert] is a statement which should always evaluate to `True` unless there is a bug in the program.
When an `assert` evaluates to `False` it will raise an [`AssertionError`][AssertionError].
The Traceback for the `AssertionError` can include an optional message that is part of the `assert` statement.
Although a message is optional, it is good practice to always include one in the `assert` definition.

The following is an example of using `assert`:

```python
>>> def int_division(dividend, divisor):
...     assert divisor != 0, "divisor must not be 0"
...     return dividend // divisor
...
>>> print(int_division(2, 1))
2
>>> print(int_division(2, 0))
Traceback (most recent call last):
  File <stdin>, line 7, in <module>
    print(int_division(2, 0))
          ^^^^^^^^^^^^^^^^^^
  File <stdin>, line 2, in int_division
    assert divisor != 0, "divisor must not be 0"
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: divisor must not be 0

```

If we start reading the Traceback at the bottom (as we should) we quickly see the problem is that `0` should not be passsed as the `divisor`.

`assert` can also be used to test that a value is of the expected type:

```python
>>> import numbers
...
...
... def int_division(dividend, divisor):
...     assert divisor != 0, "divisor must not be 0"
...     assert isinstance(divisor, numbers.Number), "divisor must be a number"
...     return dividend // divisor
...
>>> print(int_division(2, 1))
2
>>> print(int_division(2, '0'))
Traceback (most recent call last):
  File <stdin>, line 11, in <module>
    print(int_division(2, '0'))
          ^^^^^^^^^^^^^^^^^^^^
  File <stdin>, line 6, in int_division
    assert isinstance(divisor, numbers.Number), "divisor must be a number"
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: divisor must be a number
```

Once a bug is identified, consider replacing the `assert` with error handling.
This is because all `assert` statements can be disabled through running Python with the `-O` or `-OO` options, or from setting the `PYTHONOPTIMIZE` environment variable to `1` or `2`.
Setting `PYTHONOPTIMIZE` to `1` is equivalent to running Python with the `-O` option, which disables assertions.
Setting `PYTHONOPTIMIZE` to `2` is equivalent to running Python with the `-OO` option, which both disables assertions and removes docstrings from the bytcode.
Reducing bytecode is one way to make the code run faster.

## Python Debugger

Python has a built in debugger, [pdb][pdb].
It can be used to step through code and inspect variables.
You can also set breakpoints with it.
To get started you have to first `import pdb` and then call `pdb.set_trace()` where you want to start debugging:

```python
import pdb

def add(num1, num2):
    return num1 + num2

pdb.set_trace()
sum = add(1,5)
print(sum)
```

Running this code will give you a pdb prompt where you can type in commands.
Write `help` to get a list of commands.
The most common ones are `step` which steps into a function called at that line.
`next` steps over a function call and move to the next line. `where` tells you which line you are on.
Some other useful commands are `whatis <variable>` which tells you the type of a variable and `print(<variable>)` which prints the value of a variable.
You can also just use `<variable>` to print the value of a variable.
Another command is `jump <line number>` which jumps to a specific line number.

Here is a small example of how to use the debugger based on the code earlier.
Note that for this and following examples, MacOS or Linux platforms would have file paths using forward slashes:

```python
>>> python pdb.py
... > c:\pdb.py(7)<module>()
... -> sum = add(1,5)
... (Pdb)
>>> step
... > c:\pdb.py(3)add()
... -> def add(num1, num2):
... (Pdb)
>>> whatis num1
... <class 'int'>
>>> print(num2)
... 5
>>> next
... > c:\pdb.py(4)add()
... -> return num1 + num2
... (Pdb)
>>> jump 3
... > c:\pdb.py(3)add()
... -> def add(num1, num2):
... (Pdb)
```

Breakpoints are set up by `break <filename>:<line number> <condition>` where the condition is an optional condition that has to be true for the breakpoint to be hit.
You can simply write `break` to get a list of the breakpoints you have set.
To disable a breakpoint you can write `disable <breakpoint number>`.
To enable a breakpoint you can write `enable <breakpoint number>`.
To delete a breakpoint you can write `clear <breakpoint number>`.
To continue execution you can write `continue` or `c`. To exit the debugger you can write `quit` or `q`.

Here is an example of how to use the above debugger commands based on the code earlier:

```python
>>> python pdb.py
... > c:\pdb.py(7)<module>()
... -> sum = add(1,5)
... (Pdb)
>>> break
...
>>> break pdb:4
... Breakpoint 1 at c:\pdb.py:4
>>> break
... Num Type         Disp Enb   Where
... 2   breakpoint   keep yes   at c:\pdb.py:4
>>> c # continue
... > c:\pdn.py(4)add()
... -> return num1 + num2
>>> disable break 1
... Disabled breakpoint 1 at c:\pdb.py:4
>>> break
... Num Type         Disp Enb   Where
... 1   breakpoint   keep no    at c:\pdb.py:4
...         breakpoint already hit 1 time
>>> clear break 1
... Deleted breakpoint 1 at c:\pdb.py:4
>>> break
...
```

In Python 3.7+ there is an easier way to create breakpoints.
Simply writing `breakpoint()` where needed will create one.

```python
def add(num1, num2):
    breakpoint()
    return num1 + num2

breakpoint()
sum = add(1,5)
print(sum)
```

```python
>>> python pdb.py
... > c:\pdb.py(7)<module>()
... -> sum = add(1,5)
... (Pdb)
>>> c # continue
... > c:\pdb.py(5)add()
... -> return num1 + num2
```

[assert]: https://realpython.com/python-assert-statement/
[assertionerror]: https://www.geeksforgeeks.org/python-assertion-error/
[floor divison operator]: https://www.codingem.com/python-floor-division
[logging]: https://docs.python.org/3/howto/logging.html
[print]: https://www.w3schools.com/python/ref_func_print.asp
[pdb]: https://www.geeksforgeeks.org/python-debugger-python-pdb/
[exception-hierarchy]: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
