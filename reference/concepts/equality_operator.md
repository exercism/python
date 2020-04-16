# Equality operator

TODO: ADD MORE

- the `==` operator calls the dunder method `__eq__()`. By default, objects of different types are never considered equal to each other unless they are numerical types (ie int, float) or have otherwise overloaded the default implementation of the `__eq__` dunder method. `==` is always defined, but for some object types (_like class objects_) it is equivalent to calling `is`. See [`__eq__`](https: //docs.python.org/3/reference/datamodel.html#object.**eq**) for additional details. This exercise uses the equality operator to test that the `self.direction` attribute is equal to one of the constant values defined. [robot-simulator](../exercise-concepts/robot-simulator.md)
