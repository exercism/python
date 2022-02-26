# About

A `Class` is a template/blueprint representing a group of objects that share common properties and relationships.
Inheritance is one of the Object Oriented Programming(OOP) concept. Understanding inheritance is important to 
understanding the whole point behind object oriented programming.

## More on Classes

### Access Modifiers

### Class Functions


## Single Inheritance

When a subclass inherits only from one base class, it is known as single inheritance.

```python
#Base class
class Odin:
    def func1(self):
        print("Odin: father of thor")

#Derived/Subclass class
class Thor(Odin):
    def func2(self):
        print("Thor: son of Odin")


object = Thor()
object.func1()
object.func2()
```
The derived class will print both the statements of `func1` and `func2`.

## Multiple Inheritance




