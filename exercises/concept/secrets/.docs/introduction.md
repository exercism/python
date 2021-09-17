# Lambdas

Python has a [`lambda`][lambdas] expression, which is a shorter way to create functions than using `def`. It looks like this:

```python
lambda num: num + 1
```

In short, a `lambda expression` starts with the keyword `lambda`, followed by parameters (_separated by a comma, as you would do with a `def`-defined function_), a colon, and a `return` value.

```exercism/caution
Be warned: unlike functional-first programming languages, Python's [lambdas][lambdas] are quite limited. They can only contain code that is computable as a single expression, and be written on a single line. [They can't contain statements.][statements]
```

It is customary to only use them in very constrained situations -- most often as [`sort`][sort], [`min`][min], or [`max`][max] keys, or as arguments to [`map()`][map], [`filter()`][filter] and [`functools.reduce()`][reduce]. They also execute in their own frame, which makes error handling and stack traces more effort, and often slows code execution if you're not careful.

[lambdas]: https://docs.python.org/3/howto/functional.html?highlight=lambda%20expression#small-functions-and-the-lambda-expression
[statements]: https://docs.python.org/3/faq/design.html#why-can-t-lambda-expressions-contain-statements
[sort]: https://realpython.com/python-sort/
[min]: https://docs.python.org/3/library/functions.html#min
[max]: https://docs.python.org/3/library/functions.html#max
[map]: https://realpython.com/python-map-function/
[filter]: https://realpython.com/python-filter-function/
[reduce]: https://realpython.com/python-reduce-function/