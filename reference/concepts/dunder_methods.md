# Dunder methods

TODO: ADD MORE

- the exercise relies on the `__init__` dunder method to control class instantiation [allergies](../exercise-concepts/allergies.md)
- student needs to know when to use dunder methods `__init__` and `__str__` [binary-search-tree](../exercise-concepts/binary-search-tree.md)
- "dunder" -> "double under", referring to the names of these methods being prefixed with two underscores, e.g. `__init__`. There is no formal privacy in Python, but conventionally a single underscore indicates a private method, or one that the programmer should assume may change at any time; methods without an underscore are considered part of an object's public API. Double underscores are even more special - they are used by Python's builtin functions like `len()`, for example, to allow objects to implement various interfaces and functionality. They can also be used for operator overloading. If you have a custom class that you would like to be able to compare to other instances of the same class, implementing `__lt__`, `__gt__`, `__eq__` etc. allow programmers to use the `>`, `<`, `=` operators. Dunder methods allow programmers to build useful objects with simple interfaces, i.e. you can add two instances together using `+` instead of writing something like `instance1.add(instance2)`. [hamming](../exercise-concepts/hamming.md)
- the example uses the `__init__` magic method as its constructor for the class [matrix](../exercise-concepts/matrix.md)
- User defined classes can (and generally do) overload the `__init__` method, whose first argument is `self`, because the result of `__init__` is a class _instance_. [phone-number](../exercise-concepts/phone-number.md)
- The example uses `__init__` as a constructor for the class, which also calls `__new__`. In addition, the example uses `__call__()` via the appending of `()` to instance method names, and `__eq__()` (_rich compairison_) via the use of `==` [robot-simulator](../exercise-concepts/robot-simulator.md)
