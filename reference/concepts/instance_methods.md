# Instance methods

TODO: ADD MORE

- the exercise relies on the `def` statement to create an instance method [allergies](../exercise-concepts/allergies.md)
- use of `def` to define a class's methods [clock](../exercise-concepts/clock.md)
- classes can have instance _methods_ which are called from an instance of the class (as opposed to class methods, called from the Class itself). The first parameter of an instance method is always `self`, which is provided when calling from the instance (i.e. the programmer does not need to pass it as an argument explicitly). Static methods are methods called from the class itself, and are not connected to an instance of the class. They have access to class attributes (those defined on the class, not connected to the `self`), and do not require an instance of the class to exist. Classes can also define a `property` by using the `@property` decorator (not shown here); a `property` can be "lazily evaluated" to avoid uneeded computation [phone-number](../exercise-concepts/phone-number.md)
- tests for this exercises require one or more instance methods that will return a specified row or column list of the `matrix`. [matrix](../exercise-concepts/matrix.md)
- tests for this exercises require one or more instance methods that will take in a set of starting coordinates and a bearing and then accept a series of instructions that "move" the instance to a new set of coordinates and bearing. [robot-simulator](../exercise-concepts/robot-simulator.md)
