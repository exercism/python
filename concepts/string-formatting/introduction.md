# Introduction

## String Formatting in Python

The [Zen of Python][zen-of-python] asserts there should be "one _obvious_ way to do something in Python".
But when it comes to string formatting, things are a little .... _less zen_.
It can be surprising to find out that there are **four** main ways to perform string formatting in Python - each for a different scenario.
Some of this is due to Python's long history and some of it is due to considerations like internationalization or input sanitation.

With 4 different paths to take, how do you decide what to use?

1. `f-strings` are the newest and easiest to read.
If you don't need to internationalize, they should be the Python 3.6+ preferred method.
2. `str.format()` is versatile, very powerful and compatible with both `gnu gettext` and most versions of Python.
3. If simplicity, safety, and/or heavy internationalization is what you need, `string.Template()` can be used to mitigate risks when inputs need to be handled and for wrapping translation strings.
4. The `%` operator should mostly be used for compatibility with old code.
`%` formatting` can lead to issues displaying non-ascii and unicode characters and has more errors and less functionality than other methods.

If you want to go further: [all about formatting][all-about-formatting] and [Python String Formatting Best Practices][formatting best practices] are good places to start.

[zen-of-python]: https://www.python.org/dev/peps/pep-0020/
[all-about-formatting]: https://realpython.com/python-formatted-output
[formatting best practices]: https://realpython.com/python-string-formatting/
