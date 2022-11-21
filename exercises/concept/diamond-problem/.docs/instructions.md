# Instructions

In this exercise we will see the so called `daimon inheritance problem`. This problem is derive from the multiple inheritance Python is capable of. Lest imagine we have the following inheritance hierarchy.
```
    A
   / \
  /   \
 B     C
  \   /
   \ /
    D
```

The classes `B` and `C` inherit from our class `A`, and at the same time a fouth class `D` extends classes `B` and `C`. The problem raises at the time of initializing the classes that reside at the same hierarchy level. *Which one will be inicialized first?*, *And which one will override the other?*.

In **this exercise** we would like to solve the following `diamon problem`, this consist of 4 main classes related as follows:

```
     A
   / | \
  /  |  \
 B   C   D
  \  |  /
   \ | /
     E
```

## 1. Inheritance hierarchy

We want our classes to present the hierarchy represented on the ASCII diagram above.

The classes on our Python code will be named as on the following way:

Letter|Class Name|
------|----------|
 `A`  | `ClassA` |
 `B`  | `ClassB` |
 `C`  | `ClassC` |
 `D`  | `ClassD` |
 `E`  | `ClassE` |

## 2. Creating constructors

We need to create the `constructors` (`__init__`) for each of the classes with the folloing:

1. Create an attribute on class `A` named `sequence` and initialize it to a empty string.
1. Create an attribute on all classes named `name` that will be initialize with a single character indicating the name of the class in capital leters.
1. Add the functionality needed so whenever a class is initialize, it will append the character on the attribute `name` to the string on the attribute `sequence`.

## 3. Initializing secuence

By standing for initialize the full execution of the `__init__` method, When instanciating an object of `ClassE` the sequence in which all the related classes should be initialize must look:

**==> `A` then `D` then `B` then `C` then `E`**

## 4. Return sequence

Classes `B`, `C`, `D` and `E` should implement a method named `sequence_as_tuple` that will return the sequence stored on the `sequence` atribute as a tuple of characters. This method should not be implemented on class `A`.

> ### Recomendation:
> Try to avoid code duplication as much as possible.