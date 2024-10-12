# Regex and the Operator Module


```python
import re
from operator import add, mul, sub
from operator import floordiv as div

OPERATIONS = {"plus": add, "minus": sub, "multiplied by": mul, "divided by": div}

REGEX = {
    'number': re.compile(r'-?\d+'),
    'operator': re.compile(f'(?:{"|".join(OPERATIONS)})\\b')
}

# Helper function to extract a number from the question.
def get_number(question):
    # Match a number.
    pattern = REGEX['number'].match(question)
    
    # Toss an error if there is no match.
    if not pattern:
        raise ValueError("syntax error")
    
    # Remove the matched pattern from the question, and convert 
    # that same pattern to an int. Return the modified question and the int.
    return [question.removeprefix(pattern.group(0)).lstrip(), 
            int(pattern.group(0))]

# Helper function to extract an operation from the question.
def get_operation(question):
    # Match an operation word
    pattern = REGEX['operator'].match(question)
    
    # Toss an error if there is no match.
    if not pattern:
        raise ValueError("unknown operation")
        
    # Remove the matched pattern from the question, and look up 
    # that same pattern in OPERATIONS. Return the modified question and the operator.
    return [question.removeprefix(pattern.group(0)).lstrip(),
            OPERATIONS[pattern.group(0)]]

def answer(question):
    prefix = "What is"
    
    # Toss an error right away if the question isn't valid.
    if not question.startswith(prefix):
        raise ValueError("unknown operation")
    
    # Clean the question by removing the suffix and prefix and whitespace.
    question = question.removesuffix("?").removeprefix(prefix).lstrip()

    # the question should start with a number
    question, result = get_number(question)

    # While there are portions of the question left, continue to process.
    while len(question) > 0:
        # can't have a number followed by a number
        if REGEX['number'].match(question):
            raise ValueError("syntax error")

        # Call get_operation and unpack the result
        # into question and operation.
        question, operation = get_operation(question)
        
        # Call get_number and unpack the result 
        # into question and num
        question, num = get_number(question)

        # Perform the calculation, using result and num as 
        # arguments to operation.
        result = operation(result, num)

    return result
```

This approach uses two dictionaries:  one of operations imported from `operators`, and another that holds regex for matching digits and matching operations in the text of a question.

It defines two "helper" functions, `get_number()` and `get_operation`, that take a question and use the regex patterns to remove, convert, and return a number (_`get_number()`_) or an operation (_`get_operation()`_), along with a modified "new question".

In the `answer()` function, the question is checked for validity (_does it start with "What is"_), and a `ValueError("unknown operation")` it raised if it is not a valid question.
Next, the question is cleaned with [`str.removeprefix`][removeprefix] & [`str.removesuffix`][removesuffix], removing "What is" and "?".
Left-trailing white space is stripped with the help of [`lstrip()`][lstrip].
After that, the variable `result` is declared with an initial value from `get_number()`.

The question is then iterated over via a `while-loop`, which calls `get_operation()` and `get_number()` — "reducing" the question by removing the leading numbers and operator.
The return values from each call are [unpacked][unpacking] into a "leftover" question portion, and the number or operator.
The returned operation is then made [callable][callable] using `()`, with result and the "new" number (_returned from `get_number()`_) passed as arguments.
The `loop` then proceeds with processing of the "new question", until the `len()` is 0.

Once there is no more question to process, `result` is returned as the answer.

[callable]: https://treyhunner.com/2019/04/is-it-a-class-or-a-function-its-a-callable/
[lstrip]: https://docs.python.org/3/library/stdtypes.html#str.lstrip
[removeprefix]: https://docs.python.org/3.9/library/stdtypes.html#str.removeprefix
[removesuffix]: https://docs.python.org/3.9/library/stdtypes.html#str.removesuffix
[unpacking]: https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/
