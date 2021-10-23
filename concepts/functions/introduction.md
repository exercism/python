# Introduction

A [`function`][function] is a named block of code that takes input and produces output when invoked. Functions are used to perform specific and repetitive tasks throughout a program.

More formally:  a function is any Python object to which the [`function call`][calls] operation can be applied. The body of the function contains one or more statements which will return some value to the calling code/caller. The function object can define/receive zero or more parameters/arguments (_including other functions_).

[Function definitions][function-definitions] (`def <function_name>:`) form an _executable statement_ which binds the `<function_name>` to the function object definition (_the wrapper around the executable statements in the function body_) in the current local namespace.

Functions are [_first class objects_][first-class objects], which means they can be assigned to variables, passed as arguments to other functions, used as a `return` value, and wrapped around/nested to form decorators and closures.

Python also provides many top-level [_built-in functions_][built-in functions] for common operations.

[built-in functions]: https://docs.python.org/3/library/functions.html
[calls]: https://docs.python.org/3/reference/expressions.html#calls
[first-class objects]: https://realpython.com/lessons/functions-first-class-objects-python/
[function]: https://docs.python.org/3/glossary.html#term-function
[function-definitions]: https://docs.python.org/3/reference/compound_stmts.html#function-definitions
