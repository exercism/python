# Hints

## General

This exercise has many potential solutions and many paths you can take along the way.
No path is manifestly "better" than another, although a particular path may be more interesting or better suited to what you want to learn or explore right now.
Some paths may trade speed for clarity, others might take up more memory but be more scalable or maintainable.
We encourage you to try out more than one strategy to see what happens.

_______
-  Python has a robust set of tools to work with strings. [`str.split`][str.split] [`str.replace`][str.replace] [`str.lower`][str.lower] and [`str.strip`][str.strip] can be particularly helpful with this challenge.
-  String methods can be chained together (_as long as the method returns a `str`_))
-  While `str.split()` is very _specific_, `str.strip()` behaves differently, and allows multiple combinations.
-  The [`string`][string] module (as opposed to `str`) has some constants that can be useful for filtering and comparison when processing strings.
________

-  [Dictionaries][dict] can be helpful for tabulating when items (keys) appear more than once in a string.
-  [`dict.setdefault()`][dict.setdefault] can help in processing when a key might be missing from a dictionary.
-  The [Collections][collections] module implements some really useful subtypes to the core `dict` (dictionary), purpose-built to do things like [tally][collections.counter].
________
-  Exploring the [`re`][re] module and regular expressions can be fun, but is by no means necessary to solve this challenge.
-  [Regex101][regex101] is very helpful for experimenting with regular expression logic.
-  Both [`re.sub`][re.sub] and [`re.findall`][re.findall] can be interesting strategies to employ.
________
-  [Comprehensions][comprehensions] can often "flatten" loops where items are being appended to a list or inserted into a dictionary.
-  [Generator expressions][generator expressions] can often "stand in" for a list comprehension when an iterable is needed.
  Generator expressions are evaluated in a "lazy" fashion, and take up less space in memory than a corresponding list comprehension.


[collections.counter]: https://docs.python.org/3/library/collections.html#collections.Counter
[collections]: https://docs.python.org/3/library/collections.html#module-collections
[comprehensions]: https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
[dict.setdefault]: https://docs.python.org/3/library/stdtypes.html#dict.setdefault
[dict]: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
[generator expressions]: https://dbader.org/blog/python-generator-expressions
[re.findall]: https://docs.python.org/3/library/re.html?highlight=re#re.findall
[re.sub]: https://docs.python.org/3/library/re.html?highlight=re#re.sub
[re]: https://docs.python.org/3/library/re.html?highlight=re#module-re
[regex101]: https://regex101.com/
[str.lower]: https://docs.python.org/3/library/stdtypes.html#str.lower
[str.replace]: https://docs.python.org/3/library/stdtypes.html#str.replace
[str.split]: https://docs.python.org/3/library/stdtypes.html#str.split
[str.strip]: https://docs.python.org/3/library/stdtypes.html#str.strip
[string]: https://docs.python.org/3/library/string.html
