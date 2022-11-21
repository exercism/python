# Introduction

## Class Inheritance in Python

`Class inheritance` is one powerfull feature of [OOP (Object Oriented Programming)][oop], that will allow us to inherit atrubutes and functionality ([methods][methods]) from other clases. Thanks to it we can recicle and reuse the code and build real world relationships between objects.

## Nomenclature

* The class which got inherited is called a `parent class`, `superclass` or `base class`.

* The class which inherited the parent class is designated as `child class`, `subclass`, `derived class` or `extended class`.

## Syntax and key concepts
To inherit from a class in Python we simply need to put the name of the parent class inside de parentesis when defining a new class, and all it's functionality and atributes will be parse to our new child class.

```python
>>> class Parent():
...     def hello_parent(self):
...         return "Hello from parent class."
... 
>>> class Child(Parent):
...     pass
... 
>>> child_object = Child()
>>> child_object.hello_parent()
'Hello from parent class.'
```
### [Pythons MRO][mro]
Python will try always to find our method or attribute in the `child class` first and in case there is no much for it there, it will move on and check on the `parent class`. In case it is not able to find it on the parent class then it will move on to the `parent parent class`. This path of resolution is what is demonimated as `Pythons MRO (method resolution order)`.

### [super()][super]
In case we want Python to search for the resolution directly on the `parent class`, we can made use of the [build-in][build in] funcion `super()`. This function will reference the `parent class` and search under his scope with out event trying to resolve it first on our `child class`.

One of the most use cases for the `super()` function is on the [constructor][calss constructor] in which we will make use of `super()` to call our [dunder method][magic] `__init__()` and initialize the `parent class`.

```python
>>> class Parent():
...     def __init__(self, x):
...             self.x = x
... 
>>> class Child(Parent):
...     def __init__(self, x, y):
...             super().__init__(x)
...             self.y = y
... 
>>> object_child = Child(4, 8)
>>> object_child.x
4
>>> object_child.y
8
```
In the [Pythonic][pythonic] way, if you want to call the parents costructor, you should do it at the beginning of the childs constructor.

In case you do not define any constructor the parent constructor will be use as fallback.

> ### Side note
> One comon use of inheritance where you use the parent constructor is on [exceptions][python exceptions].
> Exceptios in Python inherit all from the same base class called [Exception][exception class] and you will often see a declaration of a new exception class like the following.
> ```python
> >>> class My_own_exception(Exception):
> ...     pass
> ```
> Where we are just creating a new type of exception to handle a particular case. Python exceptions present a well defined [hierarchical structure we can apreciate here][exceptions hierarchy].

## Tools
Python also put to our reach two handy [build-in][build in] fucntions that can help us to identify inheritance relationships between clasees.

### [isinstance()][isinstance]

This function will tell us if an object is and instance of a particular class.

```python
>>> parent_object = Parent()
>>> child_object = Child()

# Parent object.
>>> isinstance(parent_object, Parent)
True
>>> isinstance(parent_object, Child)
False

# Child object
>>> isinstance(child_object, Parent)
True
>>> isinstance(child_object, Child)
True
```
As we can see a child object is an instance of the parent class becouse as one of its denominations estate relly well, a `extended class` is no more than a superset of the `base class` or `parent class`.

### [issubclass()][issubclass]

Is subclass function simply tell us if a certain class in below or abovo in the inheritance herarchy.

```python
>>> issubclass(Parent, Child)
False
>>> issubclass(Child, Parent)
True
```

As we can see the inheritance is unidirectional, the child inherits from the parent but not vice versa.

## Types of inheritance

Python offers multiple [types of inheritance][inheritance types], which we can utilaze to grow the snow ball of code reusability and recicliability.


### Single Inheritance

```python
>>> class Parent():
...     pass
... 
>>> class Child(Parent):
...     pass
... 
```
As we saw before this is the base example where a `child class` inherits from the `parent class`.


### Multiple Inheritance
Unlike other [OOP][oop] languages Python can handle multiple inheritance.

```python
>>> class Father():
...     pass
... 
>>> class Mother():
...     pass
... 
>>> class Child(Father, Mother):
...     pass
... 
>>> isinstance(Child(), Father)
True
>>> isinstance(Child(), Mother)
True
```
Multiple inheritance let a `child class` to inherit from two `parent classes` at the same time.

Multipe inheritance makes tricky the use of `super()`, because now we have two `parent classes`. **So which one do you think will be called first?**

```python
>>> class Father():
...     def __init__(self, s):
...             super().__init__("was called by father.")
...             print("Father " + s)
...             self.s = "Father."
... 
>>> class Mother():
...     def __init__(self, s):
...             print("Mother " + s)
...             self.s = "Mother."
... 
>>> class Child(Father, Mother):
...     def __init__(self):
...             super().__init__("was called by child.")
...             print("Child constructor.")
...             print('-' * 20)
...             print(self.s)
... 
>>> Child()
Mother was called by father.
Father was called by child.
Child constructor.
--------------------
Father.
```

We can see the preference when using the `super()` method is from `Left to Right` of the `parent classes`, but because we are calling `super()` at the begining of our constructor, the first constructor to get completly executed is the last one on our list `(Mother)`. When the execution goes back trought the hearchy levels `(Mother)` attribute get overriden.

To simplify this flows and be able to avoid the `override` of contents of a class. Pythong give as another way to acces the internals of a `parent class`, by referencing directly the name of the class.

```python
>>> class Father():
...     def __init__(self, s):
...             print("Father " + s)
...             self.s = "Father."
... 
>>> class Mother():
...     def __init__(self, s):
...             print("Mother " + s)
...             self.s = "Mother."
... 
>>> class Child(Father, Mother):
...     def __init__(self):
...             Mother.__init__(self, "was called by child.")
...             Father.__init__(self, "was called by child.")
...             print("Child constructor.")
...             print('-' * 20)
...             print(self.s)
... 
>>> Child()
Mother was called by child.
Father was called by child.
Child constructor.
--------------------
Father.
```
Because we are referencing the class, now we will need to pass the instance as a argument on the `__init__()` call. 


### Multilevel Inheritance

In multilevel inheritance you have many layers where each one of it adds or increments the functionality of it's parent.

```python
>>> class Parent():
...     pass
... 
>>> class Child(Parent):
...     pass
... 
>>> class Grandchild(Child):
...     pass
... 
>>> isinstance(Grandchild(), Parent)
True
>>> issubclass(Grandchild, Parent)
True
```
In Python all classes inherit from the base class `object`.
```python
issubclass(Parent, object)
True
```

### Hierarchical Inheritance

Herarchical inheritance is the chain of inheritance or linage of our class. In this case to reference one level up on the chain, we could made use of `super()`, and in order to get farther (more than one level jump), we will need to use the class notation.

```python
>>> class Parent():
...     pass
... 
>>> class Child(Parent):
...     pass
... 
>>> class Grandchild(Child):
...     pass
... 
>>> isinstance(Grandchild(), Parent)
True
>>> issubclass(Grandchild, Parent)
True
```

### Hybrid Inheritance

```python
>>> class Parent():
...     pass
... 
>>> class Child(Parent):
...     pass
... 
>>> class Grandchild(Child):
...     pass
... 
>>> isinstance(Grandchild(), Parent)
True
>>> issubclass(Grandchild, Parent)
True
```

## Inheritance derived concepts

### Overload
`Overload` a method is to create the same declaration, modifiying the number of arguments or in other typed languages the types of them. This let us call the same method with different type or number of arguments.

```python
>>> class Parent():
...     def hello(self):
...             return "Hello World!"
... 
>>> class Child(Parent):
...     def hello(self, w):
...             return "Hello " + w + "!"
... 
>>> object_child = Child()
>>> object_child.hello()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Child.hello() missing 1 required positional argument: 'w'
>>> object_child.hello("World")
'Hello World!'
```
Python will overwrite the method with the last definicion we have suplied to it.

### Overwrriding
As we just saw in Python a `child class` can `overrride` a method from the `parent class` by defining a method with the same declaration.

```python
>>> class Parent():
...     def hello(self):
...             return "Hello World!"
... 
>>> class Child(Parent):
...     def __init__(self):
...             self.hello = "Hi!"
... 
>>> object_child = Child()
>>> object_child.hello
'Hi!'
>>> object_child.hello()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
```

Cause Python defines all it's data types, it can not distinguis between a reference to a function or method and a variable or attribute. Because of this reasson an attribute will also overwrite a method.

[oop]: [https://www.educative.io/blog/object-oriented-programming]
[methods]: [https://realpython.com/python3-object-oriented-programming/#instance-methods]
[mro]: [https://docs.python.org/3/glossary.html#term-method-resolution-order]
[magic]: [https://www.geeksforgeeks.org/dunder-magic-methods-python/]
[class constructor]: [https://realpython.com/python-class-constructor/]
[super]: [https://docs.python.org/3/library/functions.html#super]
[python exceptions]: [https://www.dataquest.io/blog/python-exceptions/]
[exception class]: [https://docs.python.org/3/library/exceptions.html#Exception]
[exceptions hierarchy]: [https://docs.python.org/3/library/exceptions.html#exception-hierarchy]
[pythonic]: [https://www.codementor.io/blog/pythonic-code-6yxqdoktzt]
[build in]: [https://docs.python.org/3/library/functions.html]
[isinstance]: [https://docs.python.org/3/library/functions.html#isinstance]
[issubclass]: [https://docs.python.org/3/library/functions.html#issubclass]
[inheritance types]: [https://pythongeeks.org/inheritance-in-python/]