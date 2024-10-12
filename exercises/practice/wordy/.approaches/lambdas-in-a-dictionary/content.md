# Lambdas in a Dictionary to Return Functions


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
    
    equation = question.replace("by", "").split()

    while len(equation) > 1:
        try:
            x_value, operation, y_value, *rest = equation
            equation = [OPERATIONS[operation](int(x_value), int(y_value)),
                        *rest]
        except:
            raise ValueError("syntax error")
    
    return equation[0]
```

This approach is nearly identical to the [string, list, and dict methods][approach-string-list-and-dict-methods] and the [import callables from the operator][approach-import-callables-from-operator] approaches, so it is recommended that you review those before going over this one.
The major difference here is the use of [`lambda expressions`][lambdas] in place of `operator` methods or string representations in the OPERATIONS dictionary.

`lambda expressions` are small "throwaway" expressions that are simple enough to not require a formal function definition or name.
They are most commonly used in [`key functions`][key-functions], the built-ins [`map`][map] and [`filter`][filter], and in [`functools.reduce`][functools-reduce].
 `lambdas` are also often defined in areas where a function is needed for one-time use or callback but it would be onerous or confusing to create a full function definition.
The two forms are parsed identically (_they are both function definitions_), but in the case of [`lambdas`][lambda], the function name is always "lambda" and the expression cannot contain statements or annotations.

For example, the code above could be re-written to include user-defined functions as opposed to `lambda expressions`:


```python
def add_(x, y):
    return x + y

def mul_(x, y):
    return x * y

def div_(x, y):
    return x//y

def sub_(x, y):
    return x - y

def answer(question):
    operations = {'minus': sub_,'plus': add_,'multiplied': mul_,'divided': div_}
    
    if not question.startswith("What is") or "cubed" in question:
        raise ValueError("unknown operation")
    
    question = question.removeprefix("What is").removesuffix("?").strip()

    if question.isdigit(): 
        return int(question)
    
    if not question: 
        raise ValueError("syntax error")
    
    equation = question.replace("by", "").split()    
     
    while len(equation) > 1:
        try:
            x_value, operation, y_value, *rest = equation
            equation = [operations[operation](int(x_value), int(y_value)),
                        *rest]
        except:
            raise ValueError("syntax error")
    
    return equation[0]
```

However, this makes the code more verbose and does not improve readability.
In addition, the functions need to carry a trailing underscore to avoid potential shadowing or name conflict.
It is better and cleaner in this circumstance to use `lambda expressions` for the functions - although it could be argued that importing and using the methods from `operator` is even better and clearer.

[approach-import-callables-from-operator]: https://exercism.org/tracks/python/exercises/wordy/approaches/import-callables-from-operator
[approach-string-list-and-dict-methods]: https://exercism.org/tracks/python/exercises/wordy/approaches/string-list-and-dict-methods
[filter]: https://docs.python.org/3/library/functions.html#filter
[functools-reduce]: https://docs.python.org/3/library/functools.html#functools.reduce
[key-functions]: https://docs.python.org/3/howto/sorting.html#key-functions
[lambda]: https://docs.python.org/3/reference/expressions.html#lambda
[lambdas]: https://docs.python.org/3/howto/functional.html#small-functions-and-the-lambda-expression
[map]: https://docs.python.org/3/library/functions.html#map
