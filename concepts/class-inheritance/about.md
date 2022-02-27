# About

A `Class` is a template/blueprint representing a group of objects that share common properties and relationships.
Inheritance is one of the Object Oriented Programming(OOP) concept. Understanding inheritance is important to 
understanding the whole point behind object oriented programming.

## More on Classes

### Access Modifiers
Access modifications are used to restrict access to the variables and methods of the class in various object-oriented languages such as C++, Java, and Python. In most programming languages, there are three types of access modifiers in a class: `Public`, `Protected`, and `Private`.

The access control for a specific data member or a member function of a class is determined by the `_` symbol in Python. In Python, access specifiers serve a crucial role in protecting data from unwanted access and preventing it from being misused.

Python has three types of access modifiers:
1. Public access modifier
1. Protected access modifier
1. Private access modifier

#### 1. Public Access Modifier:
The members of a class that are declared public are easily accessible from any part of the program. All data members and member functions of a class are public by default. 
```python
class School:
    #constructor
    def __init__(self, name, location):
        #public data members
        self.school_name = name
        self.school_loc = location
    
    # public member function
    def school_details(self):
        print("Location:", self.school_loc)
        
obj = School("Harvard", "USA")
#Accessing public data members outside the class
print("Name:", obj.school_name)
obj.school_details()
```
In the above program, the `school_name`, `school location` and `school_details()` are public data members. These data members can be accessed from anywhere in the program. They also can be inherited.

#### 2. Protected Access Modifier:
Protected members of a class can only be accessed by a class that is derived from it. A single underscore `_` symbol is added before the data member of a class to declare it protected.
```python
# parent class
class Student:
    
     # protected data members
     _name = None
     _roll = None
     _branch = None
    
     # constructor
     def __init__(self, name, roll, branch): 
          self._name = name
          self._roll = roll
          self._branch = branch
    
     # protected member function  
     def _displayRollAndBranch(self):
 
          # accessing protected data members
          print("Roll: ", self._roll)
          print("Branch: ", self._branch)
 
 
# derived class
class About(Student):
 
       # constructor
       def __init__(self, name, roll, branch):
                Student.__init__(self, name, roll, branch)
         
       # public member function
       def displayDetails(self):
                   
                 # accessing protected data members of super class
                print("Name: ", self._name)
                   
                 # accessing protected member functions of super class
                self._displayRollAndBranch()
 
# creating objects of the derived class       
obj = Student("ABC", 122333, "Physics")
 
# calling public member functions of the class
obj.displayDetails()
```
`_name`, `_roll`, and `_branch` are protected data members in the preceding application, while the `_displayRollAndBranch()` function is a protected method of the super class `Student`. The `displayDetails()` method is a public member function of the `About` class, which is derived from the Student class. The `displayDetails()` method in the `About` class accesses the `Student` class's protected data members.

#### 3. Private Access Modifier:
The members of a class that are declared private are accessible within the class only. Private data members cannot be inherited by the derive class. A double underscore `__` sign is added before the data member of a class to make it private.

```python
class Student:
    
     # private members
     __name = None
     __roll = None
     __division = None
 
     # constructor
     def __init__(self, name, roll, division): 
          self.__name = name
          self.__roll = roll
          self.__division = division
 
     # private member function 
     def __displayDetails(self):
           
           # accessing private data members
           print("Name: ", self.__name)
           print("Roll: ", self.__roll)
           print("Branch: ", self.__division)
    
     # public member function
     def accessPrivateFunction(self):
            
           # accessing private member function
           self.__displayDetails() 
 
# creating object   
obj = Student("ABC", 122333, "Physics")
 
# accessing public member function of the class
obj.accessPrivateFunction()
```
`__name`, `__roll`, and `__division` are private members of the class `Student`, while the `__displayDetails()` method is a private member function (accessible only within the class), and the `accessPrivateFunction()` method is a public member function of the class `Student` that can be accessed from anywhere within the programme. The `accessPrivateFunction()` method gives you access to the `Student` class's private members.
### Class Functions
The member functions of a class can be categorized into following two categories:

__1. Accessor Functions__: These are those number functions that allow us to access data fields of the object. However, these functions cannot/do not change the value of the data members.

```python
class Student:
    # private members
     __name = None
     __roll = None
     __marks = None
     __div = None
     
     # constructor
    def __init__(self, name, roll, marks, div): 
        self.__name = name
        self.__roll = roll
        self.__marks = marks
        self.__div = div
     
     # public member function 
     def displayDetails(self):
         # accessing private data members
         print("Name: ", self.__name)
         print("Roll: ", self.__roll)
         print("Marks:", self.__marks)
         print("Division: ", self.__div)
         
     # Accessor Function    
     def getRollNo(self):
        return self.__roll
     
     # Mutator Function
     def setDiv(self):
        if self.__marks>=60:
            self.__div = 'A'
        elif self.__marks<60:
            self.__div = 'B'
        return self.__div
```
__2. Mutator Function__: This method is used to change the state of an object, i.e. it changes the data variable's hidden value. It has the ability to change the value of a variable on the fly. The update method is another name for this function. We can also use the word _set_ to name these procedures.

As per the above example, `getRollNo()` is an accessor function and `setDiv` is a mutator function.

## Inheritance

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
As we've seen, a class inherits from another class in this scenario. On the other side, multiple inheritance is a feature that allows a class to inherit characteristics and methods from many parent classes.
```python
class SubclassName(BaseClass1, BaseClass2, BaseClass3, ...):
    pass
```
### Diamond Inheritance

### Method resolution order(MRO)

### Mixins

#### Pros and Cons of Mixins

## __super()__



