# Hints

## 1. Create the Alien Class

- Remember that `object methods` are always passed `self` as the first parameter.
- Remember the double underscores on _both_ sides of `__init__()`.
- Instance variables are unique to the `class` instance (_object_) that possesses them.
- Class variables are the same across all instances of a `class`.

## 2. The `hit` Method

- Remember that `object methods` are always passed `self` as the first parameter.
- You can choose to allow the Alien's health to fall below zero, or require that it does not.

## 3. The `is_alive` Method

- Remember that `object methods` are always passed `self` as the first parameter.
- 0 may not be the only 'dead' condition, depending on how `hit()` is implemented.

## 4. The `teleport` Method

- Remember that `object methods` are always passed `self` as the first parameter.
- Instance attributes can be updated from a method by using `self.<attribute>` = `<new attribute value>`.

## 5. The `collision_detection` Method

- Remember that `object methods` are always passed `self` as the first parameter.
- This method seems like an excellent place to use some kind of placeholder…

## 6. Alien Counter

- Class attributes are the same across all instances of a `class`.
- Ideally, this counter would increment whenever someone _made an new Alien_.
- Class attributes can be changed from an instance method by using the _class name_:  `Alien.<class attribute name>`.
- `__init__()` is considered an instance method since it _initializes a new object_.

## 7. Object Creation

- A `tuple` would be a _single_ parameter.
- The Alien constructor takes _2 parameters_.
- Unpacking what is _inside_ the tuple would yield two parameters.
- The standalone function is outside of the `class`
