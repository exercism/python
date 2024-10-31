# Introduction

The objective of the Wordy exercise is to parse and evaluate small/simple mathematical word problems, returning the result as an integer.
These questions do not require complex or [PEMDAS][PEMDAS]-based evaluation and are instead processed from left-to-right _in sequence_.
This means that for some of the test cases, the solution will not be the same as if the word problem was evaluated like a traditional math problem.

<br>


## General Guidance

The key to a Wordy solution is to remove the "question" portion of the sentence (_"What is", "?"_) and process the remaining words between numbers as [operators][mathematical operators].
If a single number remains after removing the "question" pieces, it should be converted to an [`int`][int] and returned as the answer.


Any words or word-number combinations that do not fall into the simple mathematical evaluation pattern (_number-operator-number_) should [`raise`][raise-statement] a ["ValueError('syntax error")`][value-error] with a message.
This includes any "extra" spaces between numbers.
As shown in various approaches, there are multiple strategies for validating questions, with no one "canonical" solution.


A whole class of error can be eliminated up front by checking if a question starts with "What is", ends with "?", and does not include the word "cubed".
Any other question formulation becomes a `ValueError("unknown operation")`.
This could lead to future maintenance issues if the definition of a question ever changes or operations are added, but for the purposes of passing the current Wordy tests, it works well.

<br>

~~~~exercism/note
There are many Pythonic ways to go about the cleaning, parsing, and calculation steps of Wordy.
However, solutions all follow the same general steps:  


1.  Remove the parts of the question string that do not apply to calculating the answer.
2.  Iterate over the question, determining which words are numbers, and which are meant to be mathematical operations.
    — _Converting the question string into a `list` of words is hugely helpful here._
3.  **_Starting from the left_**,  take the first three elements and convert number strings to `int` and operations words to the mathematical operations +, -, *, and /.
4. Apply the operation to the numbers, which should result in a single number.
   — _Employing a `try-except` block can trap any errors thrown and make the code both "safer" and less complex._
5. Use the calculated number from step 4 as the start for the next "trio" (_number, operation, number_) in the question. The calculated number + the remainder of the question becomes the question being worked on in the next iteration.
   — _Using a `while-loop` with a test on the length of the question to do calculation is a very common strategy._
6.  Once the question is calculated down to a single number, that is the answer.  Anything else that happens in the loop/iteration or within the accumulated result is a `ValueError("syntax error")`.
~~~~

<br>

For question cleaning, [`str.removeprefix`][removeprefix] and
[`str.removesuffix`][removesuffix] introduced in `Python 3.9` can be very useful:


```python
>>> 'Supercalifragilisticexpialidocious'.removeprefix('Super')
'califragilisticexpialidocious'

>>> 'Supercalifragilisticexpialidocious'.removesuffix('expialidocious')
'Supercalifragilistic'


#The two methods can be chained to remove both a suffix and prefix in one line.
>>> 'Supercalifragilisticexpialidocious'.removesuffix('expialidocious').removeprefix('Super')
'califragilistic'
```


You can also use [`str.startswith`][startswith] and [`str.endswith`][endswith] in conjunction with [string slicing][sequence-operations] for cleaning:


```python
>>> if 'Supercalifragilisticexpialidocious'.startswith('Super'):
        new_string = 'Supercalifragilisticexpialidocious'[5:]
>>> new_string
'califragilisticexpialidocious'


>>> if new_string.endswith('expialidocious'):
        new_string = new_string[:15]
>>> new_string
'califragilistic'
```


Different combinations of [`str.find`][find], [`str.rfind`][rfind], or [`str.index`][index] with string slicing could also be used to clean up the initial question.
A [regex][regex] could be used to process the question as well, but might be considered overkill given the fixed nature of the prefix/suffix and operations.
Finally, [`str.strip`][strip] and its variants are very useful for cleaning up any leftover leading or trailing whitespace.

Many solutions then use [`str.split`][split] to process the remaining "cleaned" question into a `list` for convenient looping/iteration, although other strategies can also be used:


```python
>>> sentence = "The quick brown fox jumped over the lazy dog 10 times"
>>> sentence.split()
['The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog', '10', 'times']
```


For math operations, many solutions involve importing and using methods from the [operator][operator] module.
Some solutions use either [lambda][lambdas] expressions, [dunder/"special" methods][dunder-methods], or even `eval()` to replace words with arithmetic operations.


However, the exercise can be solved without using `operator`, `lambdas`, `dunder-methods` or `eval`.
 It is recommended that you first start by solving it _without_ "advanced" strategies, and then refine your solution into something more compact or complex as you learn and practice.

<br>

~~~~exercism/caution
Using [`eval`][eval] for the operations might seem convenient, but it is a [dangerous][eval-danger] and possibly [destructive][eval-destructive] approach.
It is also entirely unnecessary, as the other methods described here are safer and equally performant.

[eval-danger]: https://softwareengineering.stackexchange.com/questions/311507/why-are-eval-like-features-considered-evil-in-contrast-to-other-possibly-harmfu
[eval-destructive]: https://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html
[eval]: https://docs.python.org/3/library/functions.html?#eval
~~~~

<br>

_____________


## Approach: String, List, and Dictionary Methods


```python
def answer(question):
    if not question.startswith("What is") or "cubed" in question:
        raise ValueError("unknown operation")
    
    question = question.removeprefix("What is")
    question = question.removesuffix("?")
    question = question.replace("by", "")
    question = question.strip()

    if not question:
        raise ValueError("syntax error")

    formula = question.split()
    while len(formula) > 1:
        try:
            x_value = int(formula[0])
            y_value = int(formula[2])
            symbol = formula[1]
            remainder = formula[3:]

            if symbol == "plus":
                formula = [x_value + y_value] + remainder
            elif symbol == "minus":
                formula = [x_value - y_value] + remainder
            elif symbol == "multiplied":
                formula = [x_value * y_value] + remainder
            elif symbol == "divided":
                formula = [x_value / y_value] + remainder
            else:
                raise ValueError("syntax error")
        except:
            raise ValueError("syntax error")

    return int(formula[0])
```

This approach uses only data structures and methods (_[str methods][str-methods], [list()][list], loops, etc._) from core Python, and does not import any extra modules.
It may have more lines of code than average, but it is clear to follow and fairly straightforward to reason about.
It does use a [try-except][handling-exceptions] block for handling unknown operators.

Alternatives could use a [dictionary][dict] to store word --> operator mappings that could be looked up in the `while-loop` using [`<dict>.get()`][dict-get], among other strategies.

For more details and variations, read the [String, List and Dictionary Methods][approach-string-list-and-dict-methods] approach.

<br>

## Approach: Import Callables from the Operator Module


```python
from operator import add, mul, sub
from operator import floordiv as div

OPERATIONS = {"plus": add, "minus": sub, "multiplied": mul, "divided": div}

def answer(question):
    if not question.startswith("What is") or "cubed" in question:
        raise ValueError("unknown operation")
    
    question = question.removeprefix("What is").removesuffix("?").strip()

    if question.isdigit(): 
        return int(question)
    
    if not question: 
        raise ValueError("syntax error")
    
    equation = [word for word in question.split() if word != 'by']
    
    while len(equation) > 1:
        try:
            x_value, operation, y_value, *rest = equation
            equation = [OPERATIONS[operation](int(x_value), int(y_value)),
                        *rest]
        except:
            raise ValueError("syntax error")
    
    return equation[0]
```

This solution imports methods from the `operator` module, and uses them in a dictionary/lookup map.
Like the first approach, it uses a [try-except][handling-exceptions] block for handling unknown operators.
 It also uses a [list-comprehension][list-comprehension] to create the parsed "formula" and employs [concept: unpacking and multiple assignment](/tracks/python/concepts/unpacking-and-multiple-assignment).

For more details and options, take a look at the [Import Callables from the Operator Module][approach-import-callables-from-operator] approach.

<br>

## Approach: Regex and the Operator Module


```python
import re
from operator import add, mul, sub
from operator import floordiv as div

OPERATIONS = {"plus": add, "minus": sub, "multiplied by": mul, "divided by": div}
REGEX = {
    'number': re.compile(r'-?\d+'),
    'operator': re.compile(f'(?:{"|".join(OPERATIONS)})\\b')
}


def get_number(question):
    pattern = REGEX['number'].match(question)
    if not pattern:
        raise ValueError("syntax error")
    return [question.removeprefix(pattern.group(0)).lstrip(), 
            int(pattern.group(0))]

def get_operation(question):
    pattern = REGEX['operator'].match(question)
    if not pattern:
        raise ValueError("unknown operation")
    return [question.removeprefix(pattern.group(0)).lstrip(),
            OPERATIONS[pattern.group(0)]]

def answer(question):
    prefix = "What is"
    if not question.startswith(prefix):
        raise ValueError("unknown operation")
    
    question = question.removesuffix("?").removeprefix(prefix).lstrip()
    question, result = get_number(question)

    while len(question) > 0:
        if REGEX['number'].match(question):
            raise ValueError("syntax error")

        question, operation = get_operation(question)
        question, num = get_number(question)

        result = operation(result, num)

    return result
```


This approach uses a dictionary of regex patterns for matching numbers and operators, paired with a dictionary of operations imported from the `operator` module.
It pulls number and operator processing out into separate functions and uses a while loop in `answer()` to evaluate the word problem.
It also uses multiple assignment for various variables.
It is longer than some solutions, but clearer and potentially easier to maintain due to the separate `get_operation()` and `get_number()` functions.

For more details, take a look at the [regex-with-operator-module][approach-regex-with-operator-module] approach.

<br>

## Approach: Lambdas in a Dictionary to return Functions


```python
OPERATIONS = {
        'minus': lambda a, b: a - b,
        'plus': lambda a, b: a + b,
        'multiplied': lambda a, b: a * b,
        'divided': lambda a, b: a / b
    }


def answer(question):
    if not question.startswith("What is") or "cubed" in question:
        raise ValueError("unknown operation")
    
    question = question.removeprefix("What is").removesuffix("?").strip()

    if question.isdigit(): 
        return int(question)
    
    if not question: 
        raise ValueError("syntax error")
    
    equation = [word for word in question.split() if word != 'by']
    
    while len(equation) > 1:
        try:
            x_value, operation, y_value, *rest = equation
            equation = [OPERATIONS[operation](int(x_value), int(y_value)),
                        *rest]
        except:
            raise ValueError("syntax error")
    
    return equation[0]
```


Rather than import methods from the `operator` module, this approach defines a series of [`lambda expressions`][lambdas] in the OPERATIONS dictionary.
These `lambdas` then return a function that takes two numbers as arguments, returning the result.

One drawback of this strategy over using named functions or methods from `operator` is the lack of debugging information should something go wrong with evaluation.
Lambda expressions are all named `"lambda"` in stack traces, so it becomes less clear where an error is coming from if you have a number of lambda expressions within a large program.
Since this is not a large program, debugging these `lambdas` is fairly straightforward.
These "hand-crafted" `lambdas` could also introduce a mathematical error, although for the simple problems in Wordy, this is a fairly small consideration.

For more details, take a look at the [Lambdas in a Dictionary][approach-lambdas-in-a-dictionary] approach.

<br>

## Approach: Recursion


```python
from operator import add, mul, sub
from operator import floordiv as div

OPERATIONS = {"plus": add, "minus": sub, "multiplied": mul, "divided": div}

def answer(question):
    return calculate(clean(question))

def clean(question):
    if not question.startswith("What is") or "cubed" in question:
        raise ValueError("unknown operation")

    return (question.removeprefix("What is")
            .removesuffix("?")
            .replace("by", "")
            .strip()).split()
    
def calculate(equation):
    if len(equation) == 1:
        return int(equation[0])
    else:
        try:
            x_value, operation, y_value, *rest = equation
            equation = [OPERATIONS[operation](int(x_value), 
                        int(y_value)), *rest]
        except:
            raise ValueError("syntax error")
            
        return calculate(equation)
```


Like previous approaches that substitute methods from `operator` for `lambdas` or `list-comprehensions` for `loops` that append to a `list` -- `recursion` can be substituted for the `while-loop` that many solutions use to process a parsed word problem.
Depending on who is reading the code, `recursion` may or may not be easier to reason about.
It may also be more (_or less!_) performant than using a `while-loop` or `functools.reduce` (_see below_), depending on how the various cleaning and error-checking actions are performed.

The dictionary in this example could use functions from `operator`, `lambdas`, `dunder-methods`, or other strategies -- as long as they can be applied in the `calculate()` function.

For more details, take a look at the [recursion][approach-recursion] approach.

<br>

## Approach:  functools.reduce()


```python
from operator import add, mul, sub
from operator import floordiv as div
from functools import reduce


OPERATORS = {"plus": add, "minus": sub, "multiplied": mul, "divided": div}

def answer(question):
    if not question.startswith( "What is") or "cubed" in question:
        raise ValueError("unknown operation")
        
    question = list(filter(lambda x: 
                x not in ("What", "is", "by"), 
                question.strip("?").split()))          

    operations = question[1::2]
    digits = [int(element) if (element.isdigit() or 
              element[1:].isdigit()) else None for 
              element in question[::2]]

    if len(digits)-1 != len(operations) or None in digits:
        raise ValueError("syntax error")

    result = reduce(lambda x, y: OPERATORS[operations.pop(0)](x, y), digits)
    
    return result
```


This approach replaces the `while-loop` used in many solutions (_or the `recursion` strategy outlined in the approach above_) with a call to [`functools.reduce`][functools-reduce].
It also employs a lookup dictionary for methods imported from the `operator` module, as well as a `list-comprehension`, the built-in [`filter`][filter] function, and multiple string [slices][sequence-operations].
If desired, the `operator` imports can be replaced with a dictionary of `lambda` expressions or `dunder-methods`.

This solution may be a little less clear to follow or reason about due to the slicing syntax and the particular syntax of both `filter` and `fuctools.reduce`.

For more details and variations, take a look at the [functools.reduce for Calculation][approach-functools-reduce] approach.

<br>

## Approach: Dunder methods with `__getattribute__`


```python
OPS = {
    "plus": "__add__",
    "minus": "__sub__",
    "multiplied by": "__mul__",
    "divided by": "__truediv__"
}


def answer(question):
    question = question.removeprefix("What is").removesuffix("?").strip()
    if not question: raise ValueError("syntax error")
    if question.isdigit(): return int(question)

    found_op = False
    for name, op in OPS.items():
        if name in question:
            question = question.replace(name, op)
            found_op = True
    if not found_op: raise ValueError("unknown operation")

    ret = question.split()
    while len(ret) > 1:
        try:
            x, op, y, *tail = ret
            if op not in OPS.values(): raise ValueError("syntax error")
            ret = [int(x).__getattribute__(op)(int(y)), *tail]
        except:
            raise ValueError("syntax error")
    return ret[0]

```

This approach uses the [`dunder methods`][dunder-methods] / ["special methods"][special-methods] / "magic methods" associated with the `int()` class, using the `dunder-method` called [`<object>.__getattribute__`][getattribute] to find the [callable][callable] operation in the `int()` class [namespace][namespace] / dictionary.
This works because the operators for basic math (_"+, -, *, /, //, %, **"_) have been implemented as callable methods for all integers (_as well as floats and other number types_) and are automatically loaded when the Python interpreter is loaded.

As described in the first link, it is considered bad form to directly call a `dunder method` (_there are some exceptions_), as they are intended mostly for internal Python use, user-defined class customization, and operator overloading (_a specific form of class-customization_).

This is why the `operator` module exists - as a vehicle for providing callable methods for basic math when **not** overloading or customizing class functionality.

For more detail on this solution, take a look at the [dunder method with `__getattribute__` approach][approach-dunder-getattribute].


[PEMDAS]: https://www.mathnasium.com/math-centers/eagan/news/what-pemdas-e
[approach-dunder-getattribute]: https://exercism.org/tracks/python/exercises/wordy/approaches/dunder-getattribute
[approach-functools-reduce]: https://exercism.org/tracks/python/exercises/wordy/approaches/functools-reduce
[approach-import-callables-from-operator]: https://exercism.org/tracks/python/exercises/wordy/approaches/import-callables-from-operator
[approach-lambdas-in-a-dictionary]: https://exercism.org/tracks/python/exercises/wordy/approaches/lambdas-in-a-dictionary
[approach-recursion]: https://exercism.org/tracks/python/exercises/wordy/approaches/recursion
[approach-regex-with-operator-module]: https://exercism.org/tracks/python/exercises/wordy/approaches/regex-with-operator-module
[approach-string-list-and-dict-methods]: https://exercism.org/tracks/python/exercises/wordy/approaches/string-list-and-dict-methods
[callable]: https://treyhunner.com/2019/04/is-it-a-class-or-a-function-its-a-callable/
[dict-get]: https://docs.python.org/3/library/stdtypes.html#dict.get
[dict]: https://docs.python.org/3/library/stdtypes.html#dict
[dunder-methods]: https://www.pythonmorsels.com/what-are-dunder-methods/?watch
[endswith]: https://docs.python.org/3.9/library/stdtypes.html#str.endswith
[filter]: https://docs.python.org/3/library/functions.html#filter
[find]: https://docs.python.org/3.9/library/stdtypes.html#str.find
[functools-reduce]: https://docs.python.org/3/library/functools.html#functools.reduce
[getattribute]: https://docs.python.org/3/reference/datamodel.html#object.__getattribute__
[handling-exceptions]: https://docs.python.org/3.11/tutorial/errors.html#handling-exceptions
[index]: https://docs.python.org/3.9/library/stdtypes.html#str.index
[int]: https://docs.python.org/3/library/stdtypes.html#typesnumeric
[lambdas]: https://docs.python.org/3/howto/functional.html#small-functions-and-the-lambda-expression
[list-comprehension]: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
[list]: https://docs.python.org/3/library/stdtypes.html#list
[mathematical operators]: https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp
[namespace]: https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces
[operator]: https://docs.python.org/3/library/operator.html#module-operator
[raise-statement]: https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
[regex]: https://docs.python.org/3/library/re.html#module-re
[removeprefix]: https://docs.python.org/3.9/library/stdtypes.html#str.removeprefix
[removesuffix]: https://docs.python.org/3.9/library/stdtypes.html#str.removesuffix
[rfind]: https://docs.python.org/3.9/library/stdtypes.html#str.rfind
[sequence-operations]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[special-methods]: https://docs.python.org/3/reference/datamodel.html#specialnames
[split]: https://docs.python.org/3.9/library/stdtypes.html#str.split
[startswith]: https://docs.python.org/3.9/library/stdtypes.html#str.startswith
[strip]: https://docs.python.org/3.9/library/stdtypes.html#str.strip
[str-methods]: https://docs.python.org/3/library/stdtypes.html#string-methods
[value-error]: https://docs.python.org/3.11/library/exceptions.html#ValueError
