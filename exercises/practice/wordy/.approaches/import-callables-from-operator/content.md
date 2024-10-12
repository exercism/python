# Import Callables from the Operator Module


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


This approach is nearly identical to the [string, list, and dict methods][approach-string-list-and-dict-methods] approach, so it is recommended to review that before going over this one.
The two major differences are the `operator` module, and the elimination of the `if-elif-else` block.


The solution begins by importing basic mathematical operations as methods from the [`operator`][operator] module.
These functions (_floordiv is [aliased][aliasing] to "div"_) are stored in a dictionary that serves as a lookup table when the problems are processed.
These operations are later made [callable][callable] by using `()` after the name, and supplying arguments.


In `answer()`, the question is first checked for validity, cleaned, and finally split into a `list` using [`str.startswith`][startswith], [`str.removeprefix`][removeprefix]/[`str.removesuffix`][removesuffix], [strip][strip], and [split][split].
Checks for digits and an empty string are done, and the word "by" is filtered from the equation `list` using a [`list-comprehension`][list-comprehension].


The equation `list` is then processed in a `while-loop` within a [try-except][handling-exceptions] block.
The `list` is [unpacked][unpacking] (_see also  [concept: unpacking and multiple assignment](/tracks/python/concepts/unpacking-and-multiple-assignment)_) into `x_value`, `operation`, `y_value`, and `*rest`, and reduced by looking up and calling the mathematical function in the OPERATIONS dictionary and passing in `int(x_value)` and `int(y_value)` as arguments.


The processing of the equation `list` continues until it is of `len()` 1, at which point the single element is returned as the answer.


To walk through this step-by-step, you can interact with this code on [`pythontutor.com`][pythontutor].


Using a `list-comprehension` to filter out "by" can be replaced with the [`str.replace`][str-replace] method during question cleaning.
[Implicit concatenation][implicit-concatenation] can be used to improve the readability of the [chained][chaining-method-calls] method calls:


```python
question = (question.removeprefix("What is")
            .removesuffix("?")
            .replace("by", "")
            .strip()) #<-- Enclosing () means these lines are automatically joined by the interpreter.
```


The call to `str.replace` could instead be chained to the call to `split` when creating the equation `list`:


```python
equation = question.replace("by", "").split()
```

[aliasing]: https://mimo.org/glossary/python
[approach-string-list-and-dict-methods]: https://exercism.org/tracks/python/exercises/wordy/approaches/string-list-and-dict-methods
[callable]: https://treyhunner.com/2019/04/is-it-a-class-or-a-function-its-a-callable/
[chaining-method-calls]: https://nikhilakki.in/understanding-method-chaining-in-python
[handling-exceptions]: https://docs.python.org/3.11/tutorial/errors.html#handling-exceptions
[implicit-concatenation]: https://docs.python.org/3/reference/lexical_analysis.html#implicit-line-joining
[list-comprehension]: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
[operator]: https://docs.python.org/3/library/operator.html#module-operator
[pythontutor]: https://pythontutor.com/render.html#code=from%20operator%20import%20add,%20mul,%20sub%0Afrom%20operator%20import%20floordiv%20as%20div%0A%0AOPERATIONS%20%3D%20%7B%22plus%22%3A%20add,%20%22minus%22%3A%20sub,%20%22multiplied%22%3A%20mul,%20%22divided%22%3A%20div%7D%0A%0Adef%20answer%28question%29%3A%0A%20%20%20%20if%20not%20question.startswith%28%22What%20is%22%29%20or%20%22cubed%22%20in%20question%3A%0A%20%20%20%20%20%20%20%20raise%20ValueError%28%22unknown%20operation%22%29%0A%20%20%20%20%0A%20%20%20%20question%20%3D%20question.removeprefix%28%22What%20is%22%29.removesuffix%28%22%3F%22%29.strip%28%29%0A%0A%20%20%20%20if%20question.isdigit%28%29%3A%20%0A%20%20%20%20%20%20%20%20return%20int%28question%29%0A%20%20%20%20%0A%20%20%20%20if%20not%20question%3A%20%0A%20%20%20%20%20%20%20%20raise%20ValueError%28%22syntax%20error%22%29%0A%20%20%20%20%0A%20%20%20%20equation%20%3D%20%5Bword%20for%20word%20in%20question.split%28%29%20if%20word%20!%3D%20'by'%5D%0A%20%20%20%20%0A%20%20%20%20while%20len%28equation%29%20%3E%201%3A%0A%20%20%20%20%20%20%20%20try%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20x_value,%20operation,%20y_value,%20*rest%20%3D%20equation%0A%20%20%20%20%20%20%20%20%20%20%20%20equation%20%3D%20%5BOPERATIONS%5Boperation%5D%28int%28x_value%29,%20int%28y_value%29%29,%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20*rest%5D%0A%20%20%20%20%20%20%20%20except%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20raise%20ValueError%28%22syntax%20error%22%29%0A%20%20%20%20%0A%20%20%20%20return%20equation%5B0%5D%0A%20%20%20%20%0Aprint%28answer%28%22What%20is%202%20plus%202%20plus%203%3F%22%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false
[removeprefix]: https://docs.python.org/3.9/library/stdtypes.html#str.removeprefix
[removesuffix]: https://docs.python.org/3.9/library/stdtypes.html#str.removesuffix
[split]: https://docs.python.org/3.9/library/stdtypes.html#str.split
[startswith]: https://docs.python.org/3.9/library/stdtypes.html#str.startswith
[str-replace]: https://docs.python.org/3/library/stdtypes.html#str.replace
[strip]: https://docs.python.org/3.9/library/stdtypes.html#str.strip
[unpacking]: https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/