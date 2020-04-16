# Concepts of `phone-number`

## Example implementation:

From the current [example.py](https://github.com/exercism/python/blob/master/exercises/phone-number/example.py):

```python
import re


class PhoneNumber:
    def __init__(self, number):
        self.number = self._clean(number)
        self.area_code = self.number[:3]
        self.exchange_code = self.number[3:6]
        self.subscriber_number = self.number[-4:]

    def pretty(self):
        return "({}) {}-{}".format(
            self.area_code, self.exchange_code, self.subscriber_number
        )

    def _clean(self, number):
        return self._normalize(re.sub(r"[^\d]", "", number))

    def _normalize(self, number):
        if len(number) == 10 or len(number) == 11 and number.startswith("1"):
            valid = number[-10] in "23456789" and number[-7] in "23456789"
        else:
            valid = False

        if valid:
            return number[-10:]
        else:
            raise ValueError("{} is not a valid phone number".format(number))
```

## Concepts

- [Class][class]: classes are defined with the `class <ClassName>:` syntax
- [Dunder Methods][dunder-methods]: User defined classes can (and generally do) overload the `__init__` method, whose first argument is `self`, because the result of `__init__` is a class _instance_.
- [Inheritance][inheritance]: The default `__str___` method is inherited from `Object`, which every class in Python inherits from. (See: inheritance)
- [Methods][methods]: classes can have instance _methods_ which are called from an instance of the class (as opposed to class methods, called from the Class itself). The first parameter of an instance method is always `self`, which is provided when calling from the instance (i.e. the programmer does not need to pass it as an argument explicitly). Static methods are methods called from the class itself, and are not connected to an instance of the class. They have access to class attributes (those defined on the class, not connected to the `self`), and do not require an instance of the class to exist. Classes can also define a `property` by using the `@property` decorator (not shown here); a `property` can be "lazily evaluated" to avoid uneeded computation
- [Non-Public Methods][non-public-methods]: Methods or attributes (including those of an imported module) prefixed with an underscore, `_`, are conventionally treated as "non-public" methods. Python does not support data privacy in the way a language like Java does. Instead convention dictates that methods and attributes that are not prefixed with a single underscore can be expected to remain stable along with semver, i.e. a public method will be backwards compatible with minor version updates, and can change with major version updates. Generally, importing non-public functions or using non-public methods is discouraged, though Python will not explicitly stop the programmer from doing so.
- [Implied Argument][implied-argument]: within the class definition, methods and properties can be accessed via the `self.` notation
- [Inheritance][inheritance]: a "subclass" will inherit all methods, attributes from it's parent class, and can then override methods as needed. Overriding means the logic in the parent class is not used. The `super` builtin function (not shown here) exists to allow the programmer to defer logic up the inheritance chain to the parent class when needed.
- [Standard Library][standard-library]: the `re` module is an example of the Python stdlib (standard library), or included code libraries and tools that are frequently used in Python
- [Import][import]: to use the module, the `import` syntax can be used
- [Iterables][iterables]: characters in a string are _iterables_ and are subject to index and slice access as described below
- [Immutable][immutable]: strings are immutable, and so cannot have values assigned; new strings can be created, however
- [String Formatting][string-formatting]: `str.format` can be used to format a string
- [Membership Testing][membership-testing]: the `in` keyword, as in `"s" in "string`, allows the user to check membership in the longer string
- [String Methods][string-methods]: strings (and other types) have built in instance methods - in this case, `"string".startswith("s")` which are called from the instance of the string itself
- [Indexing][indexing]: for iterables, individual items can be accessed with `stringname[x]` notation. Negative numbers start to count backwards
- [Slicing][slicing]: a slice within an iterable, i.e. the slice of items from `<iterable>[x]` to `<iterable>[y]`, can be accessed via `<iterable>[x:y]` notation; a third parameter allows "skipping" by `z`, i.e. `stringname[x:y:z]`
- [Regular Expressions][regular-expressions]: regular expressions is a language of sorts that can detect substrings and extract groups from a string, as well as replace them with something else
- [Conditionals][conditionals]: `if ... else` and `elif` allow a programmer to switch code branches depending on some condition
- [Boolean Logic][boolean-logic]: the `or` and `and` keywords are used
- [Raise][raise]: an appropriate Exceptions must be raised with the `raise` keyword
