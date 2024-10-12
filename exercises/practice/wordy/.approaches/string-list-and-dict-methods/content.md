# String, List, and Dictionary Methods


```python
OPERATIONS = {"plus": '+', "minus": '-', "multiplied": '*', "divided": '/'}


def answer(question):
    if not question.startswith("What is") or "cubed" in question:
        raise ValueError("unknown operation")
    
    question = question.removeprefix("What is").removesuffix("?").strip()

    if not question:
        raise ValueError("syntax error")

    formula = []
    for operation in question.split():
        if operation == 'by':
            continue
        else:
            formula.append(OPERATIONS.get(operation, operation))

    while len(formula) > 1:
        try:
            x_value, y_value = int(formula[0]), int(formula[2])
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

Within the `answer()` function, the question is first checked for "unknown operations" by validating that it starts with "What is" ([`str.startswith`][startswith], [`str.endswith`][endswith]) and does not include the word "cubed" (_which is an invalid operation_).
This eliminates all the [current cases][unknown-operation-tests] where a [`ValueError("unknown operation")`][value-error] needs to be [raised][raise-statement].
Should the definition of a question expand or change, this strategy would need to be revised.


The question is then "cleaned" by removing the prefix "What is" and the suffix "?" ([`str.removeprefix`][removeprefix], [`str.removesuffix`][removesuffix]) and [stripping][strip] any leading or trailing whitespaces.


If the question is now an empty string, a `ValueError("syntax error")` is raised.


Next, the question is [split][split] into a `list` and iterated over, with each element looked up and replaced from the OPERATIONS dictionary.
The [`dict.get`][dict-get] method is used for this, as it takes a default argument for when a [`KeyError`][keyerror] is thrown.
Here the default for `dict.get` is set to the element being iterated over, which is effectively  _"if not found, skip it"_.
 This avoids error handling, extra logic, or interruption when an element is not found.
 One exception here is the word "by", which is explicitly skipped within the `for-loop`, so that it doesn't appear in the formula to be processed.
 This filtering out could also be accomplished by using [`str.replace`][str-replace] in the cleaning step or during the `split` step.
 The results of iterating through the question are then appended to a new formula `list`.



````exercism/note
There are a couple of common alternatives to the `loop-append`:

1.  [`list-comprehensions`][list-comprehension] duplicate the same process in a more succinct and declarative fashion:
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


After the formula `list` is composed, it is processed in a `while-loop`.

The processing within the `loop` is wrapped in a [try-except][handling-exceptions] block to trap any errors and raise them as `ValueError("syntax error")`.
While each type of error could be checked for individually, it is not necessary since only `ValueError("syntax error")` is required here.

1.  `x_value` and `y_value` are assigned to the first element and third element of the list using [bracket notation][bracket-notation], and converted to integers.
     - Rather than indexing and slicing, [concept: unpacking and multiple assignment](/tracks/python/concepts/unpacking-and-multiple-assignment) can be used to assign the variables.
     This does require a modification to the returned formula `list`:
     ```python
        x_value, operation, y_value, *remainder = formula  # <-- Unpacking won't allow conversion to int() here.
        
        ...
         if symbol == "+":
             formula = [int(x_value) + int(y_value)] + remainder # <-- Instead, conversion to int() must happen here.
        ...
        
          return int(formula[0])
     ```

2.  `symbol` is assigned to the second element of the list.
3.  `remainder` is assigned to a [slice][list-slice] of everything else in the `list`.

The `symbol` is then tested in the `if-elif-else` block and the formula `list` is modified by calculating the operation on `x_value` and `y_value` and then appending whatever part of the question remains.

Once the formula `list` is calculated down to a number, that number is converted to an `int` and returned as the answer.


````exercism/note
Introduced in Python 3.10, [structural pattern matching][structural-pattern-matching] can be used to replace the `if-elif-else` chain in the `while-loop`.
In some circumstances, this could be easier to read and/or reason about: 


```python
    while len(formula) > 1:
        try:
            x_value, symbol, y_value, *remainder = formula

             match symbol:
                case "+":
                    formula = [int(x_value) + int(y_value)] + remainder
                case "-":
                    formula = [int(x_value) - int(y_value)] + remainder
                case "*":
                    formula = [int(x_value) * int(y_value)] + remainder
                case "/":
                    formula = [int(x_value) / int(y_value)] + remainder
                case _:
                    raise ValueError("syntax error")
        except: 
        raise ValueError("syntax error")
```  

[structural-pattern-matching]: https://peps.python.org/pep-0636/
````

[bracket-notation]: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
[dict-get]: https://docs.python.org/3/library/stdtypes.html#dict.get
[endswith]: https://docs.python.org/3.9/library/stdtypes.html#str.endswith
[handling-exceptions]: https://docs.python.org/3.11/tutorial/errors.html#handling-exceptions
[keyerror]: https://docs.python.org/3/library/exceptions.html#KeyError
[list-slice]: https://www.pythonmorsels.com/slicing/
[raise-statement]: https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement
[removeprefix]: https://docs.python.org/3.9/library/stdtypes.html#str.removeprefix
[removesuffix]: https://docs.python.org/3.9/library/stdtypes.html#str.removesuffix
[split]: https://docs.python.org/3.9/library/stdtypes.html#str.split
[startswith]: https://docs.python.org/3.9/library/stdtypes.html#str.startswith
[str-replace]: https://docs.python.org/3/library/stdtypes.html#str.replace
[strip]: https://docs.python.org/3.9/library/stdtypes.html#str.strip
[unknown-operation-tests]: https://github.com/exercism/python/blob/main/exercises/practice/wordy/wordy_test.py#L58-L68
[value-error]: https://docs.python.org/3.11/library/exceptions.html#ValueError
