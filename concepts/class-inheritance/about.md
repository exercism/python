# About

Inheritance is one of the ['four pillars'][four-pillars] of Object Oriented Programming (`OOP`).
In situations where only a small amount of functionality needs to be customized for a new class, `inheritance` allows code re-use from one or more parent classes, and can help make programs cleaner and more maintainable.

## Inheritance

`Inheritance` describes `is a kind of` relationship between two or more classes, abstracting common details into super class and storing specific ones in the subclass.
To create a child class, specify the parent class name inside the pair of parenthesis, followed by it's name.
Example
```python
class Child(Parent):  
   pass
```
Every child class inherits all the behaviours exhibited by their parent class.

## Single Inheritance

When a derived (or child) class inherits only from one base (or parent) class, it is known as single inheritance.

```python
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
class Employee(Person):
    all_employees = []
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.empid = empid
        Employee.all_employees.append(self)
```
`Employee` class is derived from `Person`.
Now, we can create an `Employee` object.
```python
...
p1 = Person('George', 'smith')
print(p1.fname, '-', p1.lname)
e1 = Employee('Jack', 'simmons', 456342)
e2 = Employee('John', 'williams', 123656)
print(e1.fname, '-', e1.empid)
print(e2.fname, '-', e2.empid)
```
After running the program we will get the following output
```cmd
George - smith
Jack - 456342
John - 123656
```
## Multiple Inheritance
As we've seen, a class inherits from another class in this scenario. On the other side, multiple inheritance is a feature that allows a class to inherit characteristics and methods from many parent classes.
```python
class SubclassName(BaseClass1, BaseClass2, ...):
    pass
```
### Diamond Problem
The "diamond problem" (also known as the "deadly diamond of death") refers to an ambiguity that occurs when two classes B and C inherit from a superclass A, while another class D inherits from both B and C. If A has a method "m" that B or C (or even both of them) has overridden, and if it does not override this method, the question becomes which version of the method D inherits. It's possible that it's from A, B, or C.
Let's have a look at the problem using an example:

```python
class A:
    def m(self):
        print("m of A called")
class B(A):
    def m(self):
        print("m of B called")
class C(A):
    def m(self):
        print("m of C called")
class D(B,C):
    pass
```
If we call an instance x of class D, we will get the output as `m of B called`. But if we interchange the order of inheritance in class D i.e. `Class D(C, D)`. We will get the output as `m of C called`. 
To solve the diamond problem in python, we will look into a new method `mro()`.
### Method resolution order(MRO)

To get the method resolution order of a class we can use either `__mro__` attribute or `mro()` method. By using these methods we can display the order in which methods are resolved. For Example

```python
class A:
    def m(self):
        print(" m of A called")
class B:
    def m(self):
        print(" m of B called")
  
# classes ordering
class C(A, B):
    def __init__(self):
        print("Constructor C")
  
r = C()
  
# it prints the lookup order 
print(C.__mro__)
print(C.mro())
```
The output 
```cmd
Constructor C
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
```
### Mixins
A mixin is a type of multiple inheritance that is unique. Mixins are typically employed in one of two scenarios:

1. We wish to give a class a number of optional features.
1. We want to use a specific feature in a variety of classes.

For example 
```python
class A1(object):
    def method(self):
        return 1

class A2(object):
    def method(self):
        return 2

class B1(object):
    def usesMethod(self):
        return self.method() + 10

class B2(object):
    def usesMethod(self):
        return self.method() + 20

class C1_10(A1, B1): pass
class C1_20(A1, B2): pass
class C2_10(A2, B1): pass
class C2_20(A2, B2): pass
```
Mixins helps us to recombine functionalities with different choices of base classes.
#### Pros and Cons of Mixins
| Advantages | Disadvantages |
|:-- | :-- |
|Mixin classes tend to be simple because they represent simple orthogonal concepts. | Execution of statements at run time tends to jump around in different mixins, making it hard to follow and debug|
|Helps us to recombine functionalities with different choices | Potential for long compile times|
## __super()__
In a nutshell, `super()` gives us access to methods in a superclass from the subclass that inherits from it.
`super()` by itself returns a temporary object of the superclass, which may subsequently be used to call the methods of that superclass.

But why we want to use `super()`?

Using `super()` to call already created methods avoids having to rebuild those methods in our subclass and allows us to swap out superclasses with little code modifications.

[four-pillars]: https://www.educative.io/edpresso/what-are-the-four-pillars-of-oops-in-python

[four-pillars]: https://www.educative.io/edpresso/what-are-the-four-pillars-of-oops-in-python

