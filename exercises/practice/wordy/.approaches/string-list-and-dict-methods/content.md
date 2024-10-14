# String, List, and Dictionary Methods


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

Within the `answer()` function, the question is first checked for "unknown operations" by validating that it starts with "What is" ([`str.startswith`][startswith], [`str.endswith`][endswith]) and does not include the word "cubed" (_which is an invalid operation_).
This eliminates all the [current cases][unknown-operation-tests] where a [`ValueError("unknown operation")`][value-error] needs to be [raised][raise-statement].
Should the definition of a question expand or change, this strategy would need to be revised.


The question is then "cleaned" by removing the prefix "What is" and the suffix "?" ([`str.removeprefix`][removeprefix], [`str.removesuffix`][removesuffix]), replacing "by" with "" ([`str.replace`][str-replace]), and [stripping][strip] any leading or trailing whitespaces.


If the question is now an empty string, a `ValueError("syntax error")` is raised.


The remaining question string is then converted into a `list` of elements via [`str.split`][split], and that `list` is iterated over using a `while-loop` with a `len()` > 1  condition.

Within a [`try-except`][handling-exceptions] block to trap/handle any errors (_which will all map to `ValueError("syntax error")`_), the question `list` is divided up among 4 variables using [bracket notation][bracket-notation]:

1. The first element, `x_value`. This is assumed to be a number, so it is converted to an `int()`
2. The third element, `y_value`. This is also assumed to be a number and converted to an `int()`.
3. The second element, `symbol`.  This is assumed to be an operator, and is left as-is.
4. The `remainder` of the question, if there is any. This is a [slice][list-slice] starting at index 3, and going to the end.


`symbol` is then tested for "plus, minus, multiplied, or divided", and the `formula` list is modified by applying the given operation, and creating a new `formula` `list` by concatenating a `list` of the first product with the `remainder` list.
If `symbol` doesn't match any known operators, a `ValueError("syntax error")` is raised.

Once `len(formula) == 1`, the first element (`formula[0]`) is converted to an `int()` and returned as the answer.


## Variation 1:  Use a Dictionary for Lookup/Replace


```python
OPERATIONS = {"plus": '+', "minus": '-', "multiplied": '*', "divided": '/'}


def answer(question):
    if not question.startswith("What is") or "cubed" in question:
        raise ValueError("unknown operation")
    
    question = question.removeprefix("What is").removesuffix("?").replace("by", "").strip()

    if not question:
        raise ValueError("syntax error")

    formula = []
    for operation in question.split():
        formula.append(OPERATIONS.get(operation, operation))

    while len(formula) > 1:
        try:
            x_value = int(formula[0])
            y_value = int(formula[2])
            symbol = formula[1]
            remainder = formula[3:]

            if symbol == "+":
                formula = [x_value + y_value] + remainder
            elif symbol == "-":
                formula = [x_value - y_value] + remainder
            elif symbol == "*":
                formula = [x_value * y_value] + remainder
            elif symbol == "/":
                formula = [x_value / y_value] + remainder
            else:
                raise ValueError("syntax error")
        except:
            raise ValueError("syntax error")

    return int(formula[0])
```


````exercism/note
[chaining][method-chaining] is used in the clean step for this variation, and is the equivalent of assigning and re-assigning `question` as is done in the initial approach.
 This is because `str.startswith`, `str.endswith`, and `str.replace` all return strings, so the output of one can be used as the input to the next.  
 
 [method-chaining]: https://www.tutorialspoint.com/Explain-Python-class-method-chaining
````


This variation creates a dictionary to map operation words to symbols.
It pre-processes the question string into a `formula` list by looking up the operation words and replacing them with the symbols via the [`<dict>.get`][dict-get] method, which takes a [default argument][default-argument] for when a [`KeyError`][keyerror] is thrown.
Here the default for `dict.get()` is set to the element being iterated over, which is effectively  _"if not found, skip it"_.
This means the number strings will be passed through, even though they would otherwise toss an error.
 The results of iterating through the question are appended to `formula` via [`list.append`][list-append].


This dictionary is not necessary, but does potentially make adding/tracking future operations easier, although the `if-elif-else` block in the `while-loop` is equally awkward for maintenance (_see the [import callables from operator][approach-import-callables-from-operator] for a way to replace the block_).

The `while-loop`, `if-elif-else` block, and the `try-except` block are then the same as in the initial approach.


````exercism/note
There are a couple of common alternatives to the `loop-append` used here:

1.  [`list-comprehensions`][list-comprehension] duplicate the same process in a more succinct and declarative fashion. This one also includes filtering out "by":
    ```python
       
    formula = [OPERATIONS.get(operation, operation) for 
               operation in question.split() if operation != 'by']
    ```  

2. The built-in [`filter()`][filter] and [`map()`][map] functions used with a [`lambda`][lambdas] to process the elements of the list. 
   This is identical in process to both the `loop-append` and the `list-comprehension`, but might be easier to reason about for those coming from a more functional programming language:

    ```python
    formula = list(map(lambda x : OPERATIONS.get(x, x), 
                   filter(lambda x: x != "by", question.split())))
    ```

[list-comprehension]: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
[lambdas]: https://docs.python.org/3/howto/functional.html#small-functions-and-the-lambda-expression
[filter]: https://docs.python.org/3/library/functions.html#filter
[map]: https://docs.python.org/3/library/functions.html#map
````

 Rather than indexing and slicing, [concept: unpacking and multiple assignment](/tracks/python/concepts/unpacking-and-multiple-assignment) can be used to assign the variables.
 However, this does require a modification to the returned formula `list`:


 ```python
    x_value, operation, y_value, *remainder = formula  # <-- Unpacking won't allow conversion to int() here.
    
    ...
     if symbol == "+":
         formula = [int(x_value) + int(y_value)] + remainder # <-- Instead, conversion to int() must happen here.
    ...
    
      return int(formula[0])
 ```


## Variation 2:  Structural Pattern Matching to Replace `if-elif-else`


Introduced in Python 3.10, [structural pattern matching][structural-pattern-matching] can be used to replace the `if-elif-else` chain in the `while-loop` used in the two approaches above.
In some circumstances, this could be easier to read and/or reason about: 


```python
def answer(question):
    if not question.startswith("What is") or "cubed" in question:
        raise ValueError("unknown operation")
    
    question = question.removeprefix("What is").removesuffix("?").replace("by", "").strip()

    if not question:
        raise ValueError("syntax error")
    
    formula = question.split()
    while len(formula) > 1:
        try:
            x_value, symbol, y_value, *remainder = formula #<-- unpacking and multiple assignment.

            match symbol:
                case "plus": 
                    formula = [int(x_value) + int(y_value)] + remainder
                case "minus": 
                    formula = [int(x_value) - int(y_value)] + remainder
                case "multiplied": 
                    formula = [int(x_value) * int(y_value)] + remainder
                case "divided": 
                    formula = [int(x_value) / int(y_value)] + remainder
                case _: 
                    raise ValueError("syntax error") #<-- "fall through case for no match."
        except: raise ValueError("syntax error") # <-- error handling for anything else that goes wrong.
    
    return int(formula[0])
```  

[approach-import-callables-from-operator]: https://exercism.org/tracks/python/exercises/wordy/approaches/import-callables-from-operator
[bracket-notation]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[default-argument]: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values
[dict-get]: https://docs.python.org/3/library/stdtypes.html#dict.get
[endswith]: https://docs.python.org/3.9/library/stdtypes.html#str.endswith
[handling-exceptions]: https://docs.python.org/3.11/tutorial/errors.html#handling-exceptions
[keyerror]: https://docs.python.org/3/library/exceptions.html#KeyError
[list-append]: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
[list-slice]: https://www.pythonmorsels.com/slicing/
[raise-statement]: https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
[removeprefix]: https://docs.python.org/3.9/library/stdtypes.html#str.removeprefix
[removesuffix]: https://docs.python.org/3.9/library/stdtypes.html#str.removesuffix
[split]: https://docs.python.org/3.9/library/stdtypes.html#str.split
[startswith]: https://docs.python.org/3.9/library/stdtypes.html#str.startswith
[str-replace]: https://docs.python.org/3/library/stdtypes.html#str.replace
[strip]: https://docs.python.org/3.9/library/stdtypes.html#str.strip
[structural-pattern-matching]: https://peps.python.org/pep-0636/
[unknown-operation-tests]: https://github.com/exercism/python/blob/main/exercises/practice/wordy/wordy_test.py#L58-L68
[value-error]: https://docs.python.org/3.11/library/exceptions.html#ValueError
