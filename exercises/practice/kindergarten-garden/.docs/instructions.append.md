# Instructions append

## Python Implementation

The tests for this exercise expect your program to be implemented as a Garden `class` in Python.
If you are unfamiliar with classes in Python, [classes][classes in python] from the Python docs is a good place to start.

Your `class` should implement a `method` called plants, which takes a student's name as an argument and returns the `list` of plant names belonging to that student.

## Constructors

Creating the example garden

```
[window][window][window]
VRCGVVRVCGGCCGVRGCVCGCGV
VRCCCGCRRGVCGCRVVCVGCGCV
```

would, in the tests, be represented as `Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")`.

To make this representation work, your `class` will need to implement an `__init__()` method.
If you're not familiar with `__init__()` or _constructors_, [class and instance objects][class vs instance objects in python] from the Python docs gives a more detailed explanation.


## Default Parameters

In some tests, a `list` of students is passed as an argument to `__init__()`.
This should override the twelve student roster provided in the problem statement.
Both of these statements need to work with your `__init__()` method:

```Python
# Make a garden based on the default 12-student roster.
Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV") 

# Make a garden based on a 2-student roster.
Garden("VRCC\nVCGG", students=["Valorie", "Raven"]) 
```


One approach is to make the student `list` a [default argument][default argument values]; the Python docs describe `default parameters` in depth while explaining [function definitions][function definitions].


[classes in python]: https://docs.python.org/3/tutorial/classes.html
[class vs instance objects in python]: https://docs.python.org/3/tutorial/classes.html#class-objects
[default argument values]: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values
[function definitions]: https://docs.python.org/3/reference/compound_stmts.html#function-definitions
