# Concepts of `rna-transcription`

## Example implementation

Modified from the existing [example.py](https://github.com/exercism/python/blob/master/exercises/rna-transcription/example.py) to remove Python 2 compatiblity noise:

```python
DNA_TO_RNA = str.maketrans("AGCT", "UCGA")

def to_rna(dna_strand):
    return dna_strand.translate(DNA_TO_RNA)
```

## Concepts

- [Static Methods][static-methods]: Distinct from built-in functions, instance methods, and class methods, these are methods that are bound to a class, rather than an instance, and called _without_ explicitly or implicitly passing in an object of the class. The example solution for this exercise uses the `static` `str` method `maketrans`.
- [String Methods][string-methods]: this exercise uses `str.maketrans()` (a static method of `str` that returns a dictionary to create a _translation table_ as required by the `str.translate()` instance method. This method is unusual in that it takes either a single dictionary or two strings of equal length. The example solution for this exercise uses `str.maketrans()` with a two-string argument.
- [Dictionary][dictionary]: mapping type that has key-value pairs. Returned by `str.maketrans` in the example code. Also one of the argument types accepted by `str.maketrans()`.
- [String Translation][string-translation]: the `str.translate()` _instance method_ is called on an object from the `str` class (e.g. `<my string>`.translate()). Returns a copy of the inital string with each character re-mapped through the given _translation table_. The _translation table_ is typically a mapping or sequence type that implements indexing via the magic method `__getitem__()`.
- [Function][function]: A named (_and often reusable_) section of code that performs a specific task. It may or may not have _arguments_ passed in, and may or may not _return_ data. Created using the `def` keyword.
- [Function Arguments][function-arguments]: Parameters passed into a function. In python, these are noted in the `()` following a function name. The example code uses a function named `to_rna()` with an argument of `dna_strand`.
- [Return Value][return-value]: the `return` keyword is used in a _return statement_ at the end of a function. Exits a function and may or may not pass data or an expression back to calling code. Functions in python without an expicit `return` keyword and statment will return (pass back) the singleton object `none`. The example code _returns_ a copy of the passed-in argument (assumed to be a string) that has been mapped through `str.translate()`, using the table made from `str.maketrans()`
