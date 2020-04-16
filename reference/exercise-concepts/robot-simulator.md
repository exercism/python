# Concepts of `robot-simulator`

## Example implementation

From the current [example.py](https://github.com/exercism/python/blob/master/exercises/robot-simulator/example.py):

```python
NORTH, EAST, SOUTH, WEST = range(4)


class Compass:
    compass = [NORTH, EAST, SOUTH, WEST]

    def __init__(self, direction=NORTH):
        self.direction = direction

    def left(self):
        self.direction = self.compass[self.direction - 1]

    def right(self):
        self.direction = self.compass[(self.direction + 1) % 4]


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.compass = Compass(direction)
        self.x = x
        self.y = y

    def advance(self):
        if self.direction == NORTH:
            self.y += 1
        elif self.direction == SOUTH:
            self.y -= 1
        elif self.direction == EAST:
            self.x += 1
        elif self.direction == WEST:
            self.x -= 1

    def turn_left(self):
        self.compass.left()

    def turn_right(self):
        self.compass.right()

    def move(self, commands):
        instructions = {'A': self.advance,
                        'R': self.turn_right,
                        'L': self.turn_left}
        for cmd in commands:
            if cmd in instructions:
                instructions[cmd]()

    @property
    def direction(self):
        return self.compass.direction

    @property
    def coordinates(self):
        return (self.x, self.y)
```

## Concepts

- [Constants][constants]: are not enforced by the runtime, but are used via the convention of `UPPER_CASE` to signal that these values are expected to remain unchanged. Preferably, constants are defined at a module level. The example solution uses the `UPPER_CASE` convention to define NORTH, SOUTH, EAST, and WEST constants.
- [Multiple Assignment][multiple-assignment]: Python allows multiple assignment, assigning the items on the left of `=` _in order_ to the values on the right of `=` by forming tuples and then "unpacking" them. This exercise solution uses multiple assignment for the constant values NORTH, EAST, SOUTH, WEST.
- [Range][range]: the `range()` built-in type represents an immutable sequence of numbers (or any object that implements the `__index__` dunder method). Used in the example to represent the values from zero to 3 as assigned to NORTH, EAST, SOUTH, WEST.
- [Class][class]: the exercise objective is to define a `robot` type. Tested methods are linked to a `robot` class.
- [Instantiation][instantiation]: creating different instances of the `robot` class with different data representing different starting positions and bearing are tested.
- [Initialization][initialization]: customizing object instatiation with actions and persisting data. The example uses `__init__` to persist a `compass` object and x, y coordinates assigned to instance attributes.
- [Return Value][return-value]: knowing that functions need not have _explicit_ return statements or values but will return `None` if `return` is not specified. Except for the two `@property`-decorated functions, all of the functions in the example omit an explicit `return` statment and all return `None`.
- [Implicit Argument][implicit-argument]: the example uses `self` for methods and properties linked to a specific instance of the class.
- [Namespaces][namespaces]: knowing to use `self.<propertyname>` for instance attributes and `self` as first argument to instance methods in a class. Additionally, the example uses `self.<methodname>()` to call a previously stored method name.
- [Instance Methods][instance-methods]: tests for this exercises require one or more instance methods that will take in a set of starting coordinates and a bearing and then accept a series of instructions that "move" the instance to a new set of coordinates and bearing.
- [Function Decorator][function-decorator]: a higher-order function that takes another function as an argument. The "decorating" function extends the behavior of the "decorated" function without explicitly modifying it (i.e. it _wraps_ or _decorates_ it). Called in python by using the `@` symbol and the function name ahead of the function being decorated. The example uses pythons built-in `property()` as a decorator (`@property`) to return a "compound" read-only instance property made up of two separate instance attributes.
- [Higher-Order Function][higher-order-function]: a function that takes one or more other functions as arguments, _returning_ a function as its return value. The example uses the built-in `property()` as a higher-order function through `@property`.
- [Property][property]: the `property()` built-in is a function that returns a property attribute. When used as a decorator, this transforms the passed-in method into a _getter_ method for read-only attribute with the same name and docstring.
- [Assignment][assignment]: the example uses assignment for all the instance properties and `instructions` dictionary.
- [Instance Attributes][instance-attributes]: this exercise rquires one or more instance attributes to persist passed in data.
- [Mutability][mutability]: in the example, knowing there are no protected or private properties in python and so consciously mutating `self.x`, `self.y` and `self.compass` through the called instance methods.
- [Method Parameters][method-parameters]: the example `__init__` method has `self`, direction, x, and y (coordinates) as parameters. It also uses `self` and `commands` (a string) for parameters of the `move()` method.
- [Default Arguments][default-arguments]: pre-setting function arguments to protect against them not being passed by a caller. The example uses `direction = NORTH` and `x=0, y=0` to ensure those values for a `robot` even if they are not initally passed.
- [Dictionary][dictionary]: the example uses a dictionary to map paassed in move arguments to methods that perform the moves. The example also uses a dictionary/mapping created by calling `str.maketrans()`.
- [Indexing][indexing]: finding a value by key in a dictionary using `<dictionary name>[<key name>]` The example uses passed in move arguments as `keys` to look up corresponding `values` (_method names_) for moving the robot in the _instructions_ dictionary.
- [Iteration][iteration]: the example uses a `for loop` to iterate through the letters of the passed-in `commands` string and looks up the corresponding values in a dictionary, so that the appropriate methods can be called to move the `robot`.
- [Composition][composition]: adding functionality from a class by incorporating an instance of that class in a class you are creating. The example creates a `robot` by instantiating a `compass` and assigning it to the `self`.compass attribute of `robot`.
- [Modular Division][modular-division]: the example uses the modulus operator to calculate the appropriate _compass_ setting when calling the `right` compass method
- [Lists][lists]: the example stores compass direction constants in a `list`
- [Call Semantics][call-semantics]: knowing that appending `()` to the name of an instance method _calls_ it, since instance methods are _callable_.
- [Equality Operator][equality-operator]: the `==` operator calls the dunder method `__eq__()`. By default, objects of different types are never considered equal to each other unless they are numerical types (ie int, float) or have otherwise overloaded the default implementation of the `__eq__` dunder method. `==` is always defined, but for some object types (_like class objects_) it is equivalent to calling `is`. See [`__eq__`](https: //docs.python.org/3/reference/datamodel.html#object.**eq**) for additional details. This exercise uses the equality operator to test that the `self.direction` attribute is equal to one of the constant values defined.
- [Dunder Methods][dunder-methods]: The example uses `__init__` as a constructor for the class, which also calls `__new__`. In addition, the example uses `__call__()` via the appending of `()` to instance method names, and `__eq__()` (_rich compairison_) via the use of `==`
