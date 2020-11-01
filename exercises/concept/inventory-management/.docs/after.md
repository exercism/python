Python dictionaries are very powerful and you will be using them a lot if you're working with APIs and such. Dictionaries are essentially an array of _keys_ paired with _values_.

## Dictionaries and lists

Just like `lists`, dictionaries are ordered by insertion order, they are mutable (which means you can change their content without changing their identity). They can also (just like `lists`) be nested, which means that a dictionary can contain another dictionary. Dictionaries are generally used in databases for use cases where looking up things by _key_ are used over and over, although they are not generally used for use cases with demand for high-speed insertion. This [blog post][listsvdicts] by _Jessica Yung_ goes into what data type is preferred in what use cases, on a more _scientific_ level.

## Dealing with dictionaries

Dictionaries have different methods to change them, like getting a value from a specific key in the dictionary, setting a default value for a key and many more. Dictionaries are also iterable by their keys. For a full explanation of dictionaries in python refer to the [official documentation][docs] and on how to use them look at [W3-Schools.com'][how-to] tutorial.

Now that you know the basics of _creation_, _membership_ and _retrieval_ here are some useful `dict` methods. You can get values from a dictionary by using the `.get(key, [default])`, which returns the value of the given key in the dictionary, if the key does not exist it returns the `default` value. Dictionaries also have the `.setdefault(key, [default])` method, which is almost the same as `.get()`, but it also places that key with the default value if it does not exist inside the dictionary.

## The collections module

The [`collections`][collections-docs] module adds more functionality to Python's standard collection-based datatypes (`dictionary`, `set`, `list`, `tuple`). A handy member of this module is the [`Counter`][counter-dicts] class, which can count items and return them in a dictionary form. There is also [`OrderedDict`][ordered-dicts-docs] which has methods specialized for re-arranging the order of a dictionary. Finally, there is `defaultdict`- a subclass of the built-in `dict` module that overrides one method and adds one new one. The `collections` module is a handy module to use if you need some _extra_ or extended functionality for your container-based datatypes.

[listsvdicts]: https://www.jessicayung.com/python-lists-vs-dictionaries-the-space-time-tradeoff/
[docs]: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
[how-to]: https://www.w3schools.com/python/python_dictionaries.asp
[collections-docs]: https://docs.python.org/3/library/collections.html
[counter-dicts]: https://docs.python.org/3/library/collections.html#collections.Counter
[ordered-dicts-docs]: https://docs.python.org/3/library/collections.html#collections.OrderedDict
