# Recursion for Iteration


[Any function that can be written iteratively (_with loops_) can be written using recursion][recursion-and-iteration], and [vice-versa][recursion-is-not-a-superpower].
A recursive strategy [may not always be obvious][looping-vs-recursion] or easy — but it is always possible.
So the `while-loop`s used in other approaches to Wordy can be re-written to use recursive calls.

<br>

That being said, Python famously does not perform [tail-call optimization][tail-call-optimization], and limits recursive calls on the stack to a depth of 1000 frames, so it is important to only use recursion where you are confident that it can complete within the limit (_or something close to it_).
[Memoization][memoization] and other strategies in [dynamic programming][dynamic-programming] can help to make recursion more efficient and "shorter" in Python, but it's always good to give it careful consideration.

<br>

Recursion works best with problem spaces that resemble trees, include [backtracking][backtracking], or become progressively smaller.
 Some examples include financial processes like calculating [amortization][amortization] and [depreciation][depreciation], tracking [radiation reduction through nuclei decay][nuclei-decay], and algorithms like [biscetion search][bisection-search], [depth-first search][dfs], and [merge sort][merge-sort].

 <br>

Other algorithms such as [breadth-first search][bfs], [Dijkstra's algorithm][dijkstra], and the [Bellman-Ford Algorithm][bellman-ford] lend themselves better to loops.

<br>

```python
from operator import add, mul, sub
from operator import floordiv as div

# Define a lookup table for mathematical operations
OPERATIONS = {"plus": add, "minus": sub, "multiplied": mul, "divided": div}


def answer(question):
    # Call clean() and feed it to calculate()
    return calculate(clean(question))

def clean(question):
    # It's not a question unless it starts with 'What is'.
    if not question.startswith("What is") or "cubed" in question:
        raise ValueError("unknown operation")

    # Remove the unnecessary parts of the question and
    # parse the cleaned question into a list of items to process.
    # The wrapping () invoke implicit concatenation for the chained functions
    return (question.removeprefix("What is")
            .removesuffix("?")
            .replace("by", "")
            .strip()).split() # <-- this split() turns the string into a list.

# Recursively calculate the first piece of the equation, calling 
# calculate() on the product + the remainder.
# Return the solution when len(equation) is one.
def calculate(equation):
    if len(equation) == 1:
        return int(equation[0])
    else:
        try:
            # Unpack the equation into first int, operator, and second int.
            # Stuff the remainder into *rest
            x_value, operation, y_value, *rest = equation
            
            # Redefine the equation list as the product of the first three
            # variables concatenated with the unpacked remainder.
            equation = [OPERATIONS[operation](int(x_value), 
                        int(y_value)), *rest]
        except:
            raise ValueError("syntax error")
        
        # Call calculate() with the redefined/partially reduced equation.
        return calculate(equation)
```

This approach separates the solution into three functions:

1.  `answer()`, which takes the question and calls `calculate(clean())`, returning the answer to the question.
2.  `clean()`, which takes a question string and returns a `list` of parsed words and numbers to calculate from.
3.  `calculate()`, which performs the calculations on the `list` recursively, until a single number (_the base case check_) is returned as the answer — or an error is thrown.

<br>

The cleaning logic is separate from the processing logic so that the cleaning steps aren't repeated over and over with each recursive `calculate()` call.
This separation also makes it easier to make changes without creating conflict or confusion.

`calculate()` performs the same steps as the `while-loop` from [Import Callables from the Operator Module][approach-import-callables-from-operator] and others.
The difference being that the `while-loop` test for `len()` 1 now occurs as an `if` condition in the function (_the base case_), and the "looping" is now a call to `calculate()` in the `else` condition.
`calculate()` can also use many of the strategies detailed in other approaches, as long as they work with the recursion.

<br>

`clean()` can also use any of the strategies detailed in other approaches, two of which are below:

```python
    # Alternative 1 to the chained calls is to use a list-comprehension:
    return [item for item in 
            question.strip("?").split() 
            if item not in ("What", "is", "by")] #<-- The [] of the comprehension invokes implicit concatenation.
    
    
    # Alternative 2 is the built-in filter(), but it can be somewhat hard to read.
    return list(filter(lambda x: 
                x not in ("What", "is", "by"), 
                question.strip("?").split())) #<-- The () in list() also invokes implicit concatenation.
```

<br>

## Variation 1:  Use Regex for matching, cleaning, and calculating


```python

import re
from operator import add, mul, sub
from operator import floordiv as div

# This regex looks for any number 0-9 that may or may not have a - in front of it.
DIGITS = re.compile(r"-?\d+")

# These regex look for a number (x or y) before and after a phrase or word. 
OPERATORS = {
            mul: re.compile(r"(?P<x>-?\d+) multiplied by (?P<y>-?\d+)"),
            div: re.compile(r"(?P<x>-?\d+) divided by (?P<y>-?\d+)"),
            add: re.compile(r"(?P<x>-?\d+) plus (?P<y>-?\d+)"),
            sub: re.compile(r"(?P<x>-?\d+) minus (?P<y>-?\d+)"),
            }

# This regex looks for any digit 0-9 (optionally negative) followed by any valid operation,
# ending in any digit (optionally negative).
VALIDATE = re.compile(r"(?P<x>-?\d+) (multiplied by|divided by|plus|minus) (?P<y>-?\d+)")


def answer(question):
    if (not question.startswith( "What is") or "cubed" in question):
        raise ValueError("unknown operation")
    
    question = question.removeprefix( "What is").removesuffix("?").strip()

    # If after cleaning, there is only one number, return it as an int().
    if DIGITS.fullmatch(question):
        return int(question)

    # If after cleaning, there isn't anything, toss an error.
    if not question:
        raise ValueError("syntax error")
    
    # Call the recursive calculate() function.
    return calculate(question)

# Recursively calculate the first piece of the equation, calling 
# calculate() on the product + the remainder.
# Return the solution when len(equation) is one.
def calculate(question):
    new_question = ""
    
    for symbol, pattern in OPERATORS.items():
        # Declare match variable and assign the pattern match as a value
        if match := pattern.match(question):
        
            # Attempt to calculate the first num symbol num trio.
            # Convert strings to ints where needed.
            first_calc = f"{symbol(int(match['x']), int(match['y']))}"
            
            # Strip the pattern from the question
            remainder = question.removeprefix(match.group())
            
            # Create new question with first calculation + the remainder
            new_question = first_calc + remainder
    
    # Check if there is just a single number, so that it can be returned.
    # This is the "base case" of this recursive function.
    if DIGITS.fullmatch(new_question):
        return int(new_question)
    
    # Check if the new question is still a "valid" question.
    # Error out if not.
    elif not VALIDATE.match(new_question):
        raise ValueError("syntax error")
           
    # Otherwise, call yourself to process the new question.
    else:
        return calculate(new_question)
```


This variation shows how the dictionary of operators from `operator` can be augmented with [regex][re] to perform string matching for a question.
Regex are also used here to check that a question is a valid and to ensure that the base case (_nothing but digits are left in the question_) is met for the recursive call in `calculate()`.
The regex patterns use [named groups][named-groups] for easy reference, but it's not necessary to do so.


Interestingly, `calculate()` loops through `dict.items()` to find symbols, using a [walrus operator][walrus] to complete successive regex matches and composing an [f-string][f-string] to perform the calculation.
The question remains a `str` throughout the process, so `question.removeprefix(match.group())` is used to "reduce" the original question to form a remainder that is then concatenated with the `f-string` to form a new question.


Because each new iteration of the question needs to be validated, there is an `if-elif-else` block at the end that returns the answer, throws a `ValueError("syntax error")`, or makes the recursive call.


Note that the `for-loop` and VALIDATE use [`re.match`][re-match], but DIGITS validation uses [`re.fullmatch`][re-fullmatch].

<br>

## Variation 2: Use Regex, Recurse within the For-loop


```python
import re
from operator import add, mul, sub
from operator import floordiv as div

DIGITS = re.compile(r"-?\d+")
OPERATORS = (
    (mul, re.compile(r"(?P<x>.*) multiplied by (?P<y>.*)")),
    (div, re.compile(r"(?P<x>.*) divided by (?P<y>.*)")),
    (add, re.compile(r"(?P<x>.*) plus (?P<y>.*)")),
    (sub, re.compile(r"(?P<x>.*) minus (?P<y>.*)")),
    )

def answer(question):
    if not question.startswith( "What is") or "cubed" in question:
        raise ValueError("unknown operation")
    
    question = question.removeprefix( "What is").removesuffix("?").strip()

    if not question:
        raise ValueError("syntax error")
    
    return calculate(question)

def calculate(question):
    if DIGITS.fullmatch(question):
        return int(question)
        
    for operation, pattern in OPERATORS:
        if match := pattern.match(question):
            return operation(calculate(match['x']), calculate(match['y'])) #<-- the loop is paused here to make the two recursive calls.
    raise ValueError("syntax error")
```

This solution uses a `tuple` of nested `tuples` containing the operators from `operator` and regex in place of the dictionaries that have been used in the previous approaches.
This saves some space, but requires that the nested `tuples` be unpacked as the main `tuple` is iterated over (_note the `for operation, pattern in OPERATORS:` in the `for-loop`_ ) so that operations can be matched to strings in the question.
 The regex is also more generic than the example above (_anything before and after the operation words is allowed_).

Recursion is used a bit differently here from the previous variations — the calls are placed [within the `for-loop`][recursion-within-loops].
Because the regex are more generic, they will match a `digit-operation-digit` trio in a longer question, so the line `return operation(calculate(match['x']), calculate(match['y']))` is effectively splitting a question into parts that can then be worked on in their own stack frames.


For example:

1. "1 plus -10 multiplied by 13 divided by 2" would match on "1 plus -10" (_group x_) **multiplied by** "13 divided by 2" (_group y_).
2. This is re-arranged to `mul(calculate("1 plus -10"), calculate("13 divided by 2"))`
3. At this point, the loop pauses as the two recursive calls to `calculate()` spawn
4. The loop runs again — and so do the calls to `calculate()` — until there isn't any match that splits the question or any errors.
5. One at a time, the numbers are returned from the `calculate()` calls on the stack, until the main `mul(calculate("1 plus -10"), calculate("13 divided by 2"))` is solved, at which point the answer is returned.

For a more visual picture, you can step through the code on [pythontutor.com][recursion-in-loop-pythontutor].

[amortization]: https://www.investopedia.com/terms/a/amortization.asp
[approach-import-callables-from-operator]: https://exercism.org/tracks/python/exercises/wordy/approaches/import-callables-from-operator
[backtracking]: https://en.wikipedia.org/wiki/Backtracking
[bellman-ford]: https://www.programiz.com/dsa/bellman-ford-algorithm
[bfs]: https://en.wikipedia.org/wiki/Breadth-first_search
[bisection-search]: https://en.wikipedia.org/wiki/Bisection_method
[depreciation]: https://www.investopedia.com/terms/d/depreciation.asp
[dfs]: https://en.wikipedia.org/wiki/Depth-first_search
[dijkstra]: https://www.programiz.com/dsa/dijkstra-algorithm
[dynamic-programming]: https://algo.monster/problems/dynamic_programming_intro
[f-string]: https://docs.python.org/3.11/reference/lexical_analysis.html#formatted-string-literals
[looping-vs-recursion]: https://softwareengineering.stackexchange.com/questions/303242/is-there-anything-that-can-be-done-with-recursion-that-cant-be-done-with-loops
[memoization]: https://inventwithpython.com/recursion/chapter7.html
[merge-sort]: https://www.digitalocean.com/community/tutorials/merge-sort-algorithm-java-c-python
[named-groups]: https://docs.python.org/3/howto/regex.html#non-capturing-and-named-groups
[nuclei-decay]: https://courses.lumenlearning.com/suny-physics/chapter/31-5-half-life-and-activity/
[re-fullmatch]: https://docs.python.org/3/library/re.html#re.full-match
[re-match]: https://docs.python.org/3/library/re.html#re.match
[re]: https://docs.python.org/3/library/re.html
[recursion-and-iteration]: https://web.mit.edu/6.102/www/sp23/classes/11-recursive-data-types/recursion-and-iteration-review.html#:~:text=The%20converse%20is%20also%20true,we%20are%20trying%20to%20solve.
[recursion-in-loop-pythontutor]: https://pythontutor.com/render.html#code=import%20re%0Afrom%20operator%20import%20add,%20mul,%20sub%0Afrom%20operator%20import%20floordiv%20as%20div%0A%0ADIGITS%20%3D%20re.compile%28r%22-%3F%5Cd%2B%22%29%0AOPERATORS%20%3D%20%28%0A%20%20%20%20%28mul,%20re.compile%28r%22%28%3FP%3Cx%3E.*%29%20multiplied%20by%20%28%3FP%3Cy%3E.*%29%22%29%29,%0A%20%20%20%20%28div,%20re.compile%28r%22%28%3FP%3Cx%3E.*%29%20divided%20by%20%28%3FP%3Cy%3E.*%29%22%29%29,%0A%20%20%20%20%28add,%20re.compile%28r%22%28%3FP%3Cx%3E.*%29%20plus%20%28%3FP%3Cy%3E.*%29%22%29%29,%0A%20%20%20%20%28sub,%20re.compile%28r%22%28%3FP%3Cx%3E.*%29%20minus%20%28%3FP%3Cy%3E.*%29%22%29%29,%0A%20%20%20%20%29%0A%0Adef%20answer%28question%29%3A%0A%20%20%20%20if%20not%20question.startswith%28%20%22What%20is%22%29%20or%20%22cubed%22%20in%20question%3A%0A%20%20%20%20%20%20%20%20raise%20ValueError%28%22unknown%20operation%22%29%0A%20%20%20%20%0A%20%20%20%20question%20%3D%20question.removeprefix%28%20%22What%20is%22%29.removesuffix%28%22%3F%22%29.strip%28%29%0A%0A%20%20%20%20if%20not%20question%3A%0A%20%20%20%20%20%20%20%20raise%20ValueError%28%22syntax%20error%22%29%0A%20%20%20%20%0A%20%20%20%20return%20calculate%28question%29%0A%0Adef%20calculate%28question%29%3A%0A%20%20%20%20if%20DIGITS.fullmatch%28question%29%3A%0A%20%20%20%20%20%20%20%20return%20int%28question%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20for%20operation,%20pattern%20in%20OPERATORS%3A%0A%20%20%20%20%20%20%20%20if%20match%20%3A%3D%20pattern.match%28question%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20operation%28calculate%28match%5B'x'%5D%29,%20calculate%28match%5B'y'%5D%29%29%20%23%3C--%20the%20loop%20is%20paused%20here%20to%20make%20the%20two%20recursive%20calls.%0A%20%20%20%20raise%20ValueError%28%22syntax%20error%22%29%0A%0Aprint%28answer%28%22What%20is%201%20plus%20-10%20multiplied%20by%2013%20divided%20by%202%3F%22%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false
[recursion-is-not-a-superpower]: https://inventwithpython.com/blog/2021/09/05/recursion-is-not-a-superpower-an-iterative-ackermann/
[recursion-within-loops]: https://stackoverflow.com/questions/4795527/how-recursion-works-inside-a-for-loop
[tail-call-optimization]: https://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html
[walrus]: https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-assignment_expression
