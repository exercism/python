# Functools.reduce for Calculation


```python
from operator import add, mul, sub
from operator import floordiv as div
from functools import reduce


# Define a lookup table for mathematical operations
OPERATORS = {"plus": add, "minus": sub, "multiplied": mul, "divided": div}

def answer(question):
    # Check for basic validity right away, and fail out with error if not valid.
    if not question.startswith( "What is") or "cubed" in question:
        raise ValueError("unknown operation")
        
    # Using the built-in filter() to clean & split the question..
    question = list(filter(lambda x: 
                    x not in ("What", "is", "by"), 
                    question.strip("?").split()))

    # Separate candidate operators and numbers into two lists.
    operations = question[1::2]
    
    # Convert candidate elements to int(), checking for "-".
    # All other values are replaced with None.
    digits = [int(element) if 
             (element.isdigit() or element[1:].isdigit()) 
              else None for element in question[::2]]
    
    # If there is a mis-match between operators and numbers, toss error.
    if len(digits)-1 != len(operations) or None in digits:
        raise ValueError("syntax error")

    # Evaluate the expression from left to right using functools.reduce().
    # Look up each operation in the OPERATORS dictionary.
    return reduce(lambda x, y: OPERATORS[operations.pop(0)](x, y), digits)
```

This approach replaces the `while-loop` or `recursion` used in many solutions with a call to [`functools.reduce`][functools-reduce].
It requires that the question be separated into candidate digits and candidate operators, which is accomplished here via [list-slicing][sequence-operations] (_for some additional information on working with `lists`, see [concept: lists](/tracks/python/concepts/lists)_).

A nested call to `filter()` and `split()` within a `list` constructor is used to clean and process the question into an initial `list` of digit and operator strings.
However, this could easily be accomplished by either using [chained][method-chaining] string methods or a `list-comprehension`:


```python
    # Alternative 1 is chaining various string methods together.
    # The wrapping () invoke implicit concatenation for the chained functions
    return (question.removeprefix("What is")
            .removesuffix("?")
            .replace("by", "")
            .strip()).split() # <-- this split() turns the string into a list.
            
    
    # Alternative 2 to the nested calls to filter and split is to use a list-comprehension:
    return [item for item in 
            question.strip("?").split() 
            if item not in ("What", "is", "by")] #<-- The [] of the comprehension invokes implicit concatenation.
```


Since "valid" questions are all in the form of `digit-operator-digit` (_and so on_), it is safe to assume that every other element beginning at index 0 is a "number", and every other element beginning at index 1 is an operator.
By that definition, the operators `list` is 1 shorter in `len()` than the digits list.
Anything else (_or having None/an unknown operation in the operations list_) is a `ValueError("syntax error")`.


The final call to `functools.reduce` essentially performs the same steps as the `while-loop` implementation, with the `lambda-expression` passing successive items of the digits `list` to the popped and looked-up operation from the operations `list` (_made [callable][callable] by adding `()`_), until it is reduced to one number and returned.
A `try-except` is not needed here because the error scenarios are already filtered out in the `if` check right before the call to `reduce()`.

`functools.reduce` is certainly convenient, and makes the solution much shorter.
But it is also hard to understand what is happening if you have not worked with a reduce or foldl function in the past.
It could be argued that writing the code as a `while-loop` or recursive function is easier to reason about for non-functional programmers.

<br>

## Variation 1:  Use a Dictionary of `lambdas` instead of importing from operator


The imports from operator can be swapped out for a dictionary of `lambda-expressions` (or calls to `dunder-methods`), if so desired.
The same cautions apply here as were discussed in the [lambdas in a dictionary][approach-lambdas-in-a-dictionary] approach:


```python
from functools import reduce

# Define a lookup table for mathematical operations
OPERATORS = {"plus": lambda x, y: x + y,
             "minus": lambda x, y: x - y,
             "multiplied": lambda x, y: x * y,
             "divided": lambda x, y: x / y}

def answer(question):
    
    # Check for basic validity right away, and fail out with error if not valid.
    if not question.startswith( "What is") or "cubed" in question:
        raise ValueError("unknown operation")
    
    # Clean and split the question into a list for processing.
    question = [item for item in 
                question.strip("?").split() if 
                item not in ("What", "is", "by")]
    
    # Separate candidate operators and numbers into two lists.
    operations = question[1::2]
    
    # Convert candidate elements to int(), checking for "-".
    # All other values are replaced with None.
    digits = [int(element) if 
              (element.isdigit() or element[1:].isdigit()) 
              else None for element in question[::2]]
    
    # If there is a mis-match between operators and numbers, toss error.
    if len(digits)-1 != len(operations) or None in digits:
        raise ValueError("syntax error")
    
    # Evaluate the expression from left to right using functools.reduce().
    # Look up each operation in the operation dictionary.
    result = reduce(lambda x, y: OPERATORS[operations.pop(0)](x, y), digits)
    
    return result
```

[approach-lambdas-in-a-dictionary]: https://exercism.org/tracks/python/exercises/wordy/approaches/lambdas-in-a-dictionary
[callable]: https://treyhunner.com/2019/04/is-it-a-class-or-a-function-its-a-callable/
[functools-reduce]: https://docs.python.org/3/library/functools.html#functools.reduce
[method-chaining]: https://www.tutorialspoint.com/Explain-Python-class-method-chaining
[sequence-operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
