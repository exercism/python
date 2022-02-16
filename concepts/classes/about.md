# About

`Classes` combine data with behaviour.
Class are used to create copies or `instances`, commonly known as `objects`.
Objects can represent real world entities (_such as Cars or Cats_) - or more abstract concepts (_such as integers, vehicles, or mammals_).
Classes are integral to an [object oriented programming][oop] (OOP) approach, which asks the programmer to think about modeling a problem as one or more objects that interact with one another, keep state, and act upon data.

## Classes

Classes are the definitions of new _object types_, and from which new `instances` of objects are created.
They often bundle data (_known as `fields`, `attributes`, `properties`, `data members`, or `variables`_) with code or functions (_known as `methods`_) that operate on that data.
In this sense, classes are _blueprints_ or sets of instructions from which many objects of a similar type can be built and used.
A complex program can have many classes, each building many different flavors of objects.
The process of building and customizing an object from a class is known as `instantiation` (_or creating an instance of the class_).

A class definition in Python is straightforward:

```python
class My_Class:
    # Class body goes here
```

### Class Attributes

Class fields (_otherwise known as properties, attributes, data members, or variables_) can be added to the body of the class.

```python
class My_Class:
    number = 5
    string = "Hello!"
```

An instance (_object_) of `My_Class` can be created and bound to a name:

```python
>>> new_object = My_Class()

# class is instantiated and resulting object is bound to the "new_object" name.
# note: the object address 'at 0x15adc55b0' will vary by computer.
>>> new_object
<__main__.My_Class at 0x15adc55b0>
```

`Class attributes` are shared across all objects (_or instances_) created from a class, and can be accessed via [`dot notation`][dot notation]  -  a `.` placed after the object name and before the attribute name:

```python
>>> new_object = My_Class()

# Accessing the class attribute number via dot-notation.
>>> new_object.number
5

# Accessing the class attribute string via dot-notation.
>>> new_object.string
'Hello!'

# Intantiating an additional object and binding it to the "second_new_object" name.
>>> second_new_object = My_Class()

>>> second_new_object
<__main__.My_Class at 0x15ad99970>

# second_new_object shares the same class attributes as new_object.
>>> new_object.number == second_new_object.number
True
```

Class attributes are defined in the body of the class itself, before any other methods.
They are owned by the class - allowing them to be shared across instances.
Because these attributes are shared by all instances of the class, their value can be accessed and manipulated from the class directly.
Altering the value of class attributes alters the value _**for all objects instantiated from the class**_:

```python
>>> obj_one = My_Class()
>>> obj_two = My_Class()

# Accessing a class attribute from an object.
>>> obj_two.number
5

# Accessing the class attribute from the class itself.
>>> My_Class.number
5

# Modifying the value of the "number" class attribute.
>>> My_Class.number = 27

#  Modifying the "number" class attribute changes the "number" attribute for all intantiated objects.
>>> obj_one.number
27

>>> obj_two.number
27
```

Having a bunch of objects with synchronized data at all times is not particularly useful.
Fortunately, objects created from a class can be customized with their own `instance attributes` (_or instance properties, variables, or fields_).
As their name suggests, instance attributes are unique to each object, and can be modified independently.

## Customizing Object Instantiation with `__init__()`

The special ["dunder method"][dunder] (_short for "double underscore method"_) `__init__()` is used to customize class instances, and can be used to initialize instance attributes or properties for objects.
For its role in initializing instance attributes, `__init__()` is also referred to as a `class constructor` or  `initializer`.
`__init__()` takes one required parameter called `self`, which refers to the newly initiated or created object.
Instance attributes or properties can then be defined as parameters of `__init__()`, following the self parameter.


Below, `My_Class` now has an instance attributes called `location_x` and `location_y`.
As you can see, the two attributes have been assigned to the first and second indexes of the `location` (_a tuple_) argument that has been passed to `__init__()`.
The `location_x` and `location_y` attributes for a class instance will now be initialized when you instantiate an object from the class:

```python
class My_Class:
    # These are class attributes, variables, or fields.
    number = 5
    string = "Hello!"

    # This is the class "constructor", with a "location" parameter that is a tuple.
    def __init__(self, location):

        # This is an instance or object property, attribute, or variable.
        # Note that we are unpacking the tuplue argument into two seperate instance variables.
        self.location_x = location[0]
        self.location_y = location[1]

# Create a new object "new_object_one", with object property (1,2).
>>> new_object_one = My_Class((1,2))

# Create a second new object "new_object_two" with object property (-8,-9).
>>> new_object_two = My_Class((-8,-9))

# Note that new_object_one.location_x and new_object_two.location_x two different values.
>>> new_object_one.location_x
1

>>> new_object_two.location_x
-8
```

Note that you only need to pass one argument when initializing `My_Class` above -- Python takes care of passing `self` when the class is called.

~~~~exercism/advanced
Another way of creating an instance variable is to simply access a class variable via an object, and change it to something else:

```python
>>> obj_one = My_Class()
>>> obj_two = My_Class()
>>> My_Class.string
'Hello!'

>>> obj_two.string = "Hi!"
>>> obj_two.string
'Hi!'

>>> obj_one.string
'Hello!'
```

Now, watch what happens when the class variable changes:

```python
>>> My_Class.string = "World!"
>>> obj_two.string

# obj_two.string has not changed
'Hi!' 

>>> obj_one.string

# obj_one.string changed
'World!'
```

The attribute `string` is now an _instance variable_ in the case of `obj_two`, but remains a _class variable_ in `obj_one`.

This can also be done from within the class:

```python
class Demo:
    new_var = 3

    def add_two(self):
        self.new_var += 2
```

The moment that `<object>.add_two()` is called, and `self.new_var += 2` is read, `new_var` changes from a class variable to an instance variable of the same name.

This can be useful during initialization when all instances of a class will need some attribute(s) to start with the same value.
However, the instance variable then shadows* the class variable, making the class variable inaccessible from the instance where it is shadowed.  Given this situation, it may be safer and clearer to set instance attributes from the `__init__()` method as `self.<attribute>`.
~~~~
_*[_shadows_][shadowing]


## Methods

A `method` is a `function` that is bound to either the class itself (_known as a [class method][class method], which will be discussed in depth in a later exercise_) or an _instance_ of the class (object).
Methods that operate on an object or instance need to be defined with `self` as the first parameter.
You can then define the rest of the parameters as you would for a "normal" or non-bound function.
Methods that operate on a class need to be defined with both the `@classmethod` decorator and with `cls` as the first parameter.
Class methods are called on a class directly without first instatiating an object from the class.


```python
class My_Class:
    number = 5
    string = "Hello!"

    #Class constructor.
    def __init__(self, location):

        # Instance properties
        self.location_x = location[0]
        self.location_y = location[1]
        
    #Class Method.  Uses the @classmethod decorator, and cls as the first parameter.
    #Can be called without first making an intance of the class.
    @classmethod
    def change_string(cls, new_string):
        #Class attributes are referred to with cls.
        cls.string = new_string
        return cls.string

    #Instance method.  Note "self" as first parameter.
    def change_location(self, amount):
        self.location_x += amount
        self.location_y += amount
        return self.location_x, self.location_y
```

Like attribute access, calling a method simply requires putting a `.` after the object name,  and before the method name.
The called method does not need a copy of the object as a first parameter -- Python fills in `self` automatically:

```python
class My_Class:
    number = 5
    string = "Hello!"

    def __init__(self, location):
        self.location_x = location[0]
        self.location_y = location[1]

    def change_location(self, amount):
        self.location_x += amount
        self.location_y += amount
        return  self.location_x, self.location_y

# Make a new test_object with location (3,7)
>>> test_object = My_Class((3,7))
>>> (test_object.location_x, test_object.location_y)
(3,7)

# Call change_location to increase location_x and location_y by 7.
>>> test_object.change_location(7)
(10, 14)
```

Class attributes can be accessed from within instance methods in the same way that they are accessed outside of the class:

```python
class My_Class:
    number = 5
    string = "Hello!"

    def __init__(self, location):
        self.location_x = location[0]
        self.location_y = location[1]

    #Alter instance variable location_x and location_y
    def change_location(self, amount):
        self.location_x += amount
        self.location_y += amount
        return  self.location_x, self.location_y

    #Alter class variable number for all instances from within an instance.
    def increment_number(self):
        # Increment the 'number' class variable by 1.
        My_Class.number += 1

        
>>> test_object_one = My_Class((0,0))
>>> test_object_one.number
5

>>> test_object_two = My_Class((13, -3))
>>> test_object_two.increment_number()
>>> test_object_one.number
6
```

## Placeholding or Stubbing Implementation with Pass

In previous concept exercises and practice exercise stubs, you will have seen the `pass` keyword used within the body of  functions in place of actual code.
The `pass` keyword is a syntactically valid placeholder - it prevents Python from throwing a syntax error or `NotImplemented` error for an empty function or class definition.
Essentially, it is a way to say to the Python interpreter, 'Don't worry! I _will_ put code here eventually, I just haven't done it yet.'

```python
class My_Class:
    number = 5
    string = "Hello!"

    def __init__(self, location):
        self.location_x = location[0]
        self.location_y = location[1]

    #Alter instance variable location_x and location_y
    def change_location(self, amount):
        self.location_x += amount
        self.location_y += amount
        return  self.location_x, self.location_y

    #Alter class variable number for all instances
    def increment_number(self):
        # Increment the 'number' class variable by 1.
        My_Class.number += 1
    
    #This will compile and run without error, but has no current functionality.   
    def pending_functionality(self):
       #Stubbing or placholding the body of this mehtod.
       pass
```

[class method]: https://stackoverflow.com/questions/17134653/difference-between-class-and-instance-methods
[dunder]: https://www.dataindependent.com/python/python-glossary/python-dunder/
[oop]: https://www.educative.io/blog/object-oriented-programming
[dot notation]: https://stackoverflow.com/questions/45179186/understanding-the-dot-notation-in-python
[shadowing]: https://oznetnerd.com/2017/07/17/python-shadowing/
