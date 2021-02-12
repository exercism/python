# After

All variables that are assigned `None` point to the same object. New instances of `None` are not created, that is `None` by nature is of type Singleton.

Example, when you assign 2 variables with `None`, both point to the same object.

```python
a = None
b = None
a == b
#=> True
```

Python will also return `None` from a function that doesn't already have a stated `return` value, making it easy to check if the function completed without errors.

```python
def test_func():
    pass
test_func()
#=> returns None

def test_func2():
    return
#=> returns None
```

The `None` Object is a singleton of class `NoneType`. So when you find the type of a variable which is assigned with `None` it will always be of type `NoneType`.

```python
a = None
type(a)
#=> <class 'NoneType'>
```

When you toggle a variable between a value and `None`, what basically happens is a reset of the variable.

```python

a = [] #=> Variable 'a' is pointing to a list

a = None #=> Variable 'a' is reset to an empty state. the value of a is now absent.

```
