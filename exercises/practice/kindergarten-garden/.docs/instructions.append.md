# Instructions append

## Python Implementation

The tests for this exercise expect your program to be implemented as a Garden `class` in Python.
If you are unfamiliar with classes in Python, [classes][classes in python] from the Python docs is a good place to start.

Your class should implement a `method` plants, which takes a student's name and returns the list of plant names.

## Constructors

Creating the example garden

```
[window][window][window]
VRCGVVRVCGGCCGVRGCVCGCGV
VRCCCGCRRGVCGCRVVCVGCGCV
```

would, in the tests, be represented as `Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")`.

To make this work, your class will need to implement a constructor (the `__init__` method).
If you're not familiar with constructors, [class and instance objects][class vs instance objects in python] from the Python docs gives a more detailed explanation of the `__init__` method.


## Default Parameters

In some tests, a list of students is passed to the constructor. This should override the twelve student roster provided in the problem statement.
This requires making both of these statements work:

```
Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV") # Makes a garden based on the default 12-student roster
Garden("VRCC\nVCGG", students=["Valorie", "Raven"]) # Makes a garden based on a 2-student roster
```

One approach is to make students a default parameter; the Python docs describe default parameters while explaining [function definitions][function definitions]


[classes in python]: https://docs.python.org/3/tutorial/classes.html
[class vs instance objects in python]: https://docs.python.org/3/tutorial/classes.html#class-objects
[function definitions]: https://docs.python.org/3/reference/compound_stmts.html#function-definitions
