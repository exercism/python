# Introduction

## String Formatting in Python

The [Zen of Python][zen-of-python] asserts there should be "one _obvious_ way to do something in Python".
For Python 3.6+, **literal string interpolation** (**`f-strings`**) is often the obvious and preferred way to format strings:

```python
>>> adjective = "easy"
>>> f"This is an {adjective} way to format strings!"
'This is an easy way to format strings!'
```

However, given Python's long history and different considerations, it might not be surprising that there are **three** other common ways to perform string formatting in Python:

1. `str.format()` is versatile, very powerful and compatible with both `gnu gettext` and most versions of Python.
2. If simplicity, safety, and/or heavy internationalization is what you need, `string.Template()` can be used to mitigate risks when inputs need to be handled and for wrapping translation strings.
3. The `%` operator is generally considered deprecated for new code, though it still works in modern Python.
It should mostly be used for compatibility with older codebases. `%` formatting can lead to issues displaying non-ASCII and Unicode characters and has more errors and less functionality than other methods.Check your specific Python distribution for support details if you intend to use it.

If you want to go further: [all about formatting][all-about-formatting] and [Python String Formatting Best Practices][formatting best practices] are good places to start.

[zen-of-python]: https://www.python.org/dev/peps/pep-0020/
[all-about-formatting]: https://realpython.com/python-formatted-output
[formatting best practices]: https://realpython.com/python-string-formatting/
