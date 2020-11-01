In Python, an enum is a set of names that are bound to unique `literal`, or `constant` values. Enums are defined the way classes are defined in python.

```python
class Color(enum.Enum):
    RED = 1
    GREEN = 2
```

Note that the values of the enum members can be even not int types such as str, tuple, float etc.

```python
class Color(enum.Enum):
    RED = 'red'
    GREEN = 'green'
```

Enums can also be created via Functional API.

```python
Animal = Enum('Animal', 'ANT BEE CAT DOG')
list(Animal)
#=> [<Animal.ANT: 1>, <Animal.BEE: 2>, <Animal.CAT: 3>, <Animal.DOG: 4>]
```

When you assign the same value to 2 members in an enum, the latter assigned member will be an alais to the formed one.

```python
class Color(enum.Enum):
    RED = 1
    GREEN = 2
    ALAIS_OF_RED = 1
Color.ALAIS_OF_RED
#=> Color.RED
```

You can iterate through all the members of the enum by 2 ways.

```python
for member in Color
    print((member.name, member.value))
#=> (RED, 1)
#=> (GREEN, 2)

# __members__.items() helps you to loop through alias as well
for member in Color.__members__.items():
    print(member)
#=>('RED', <Color.RED: 1>)
#=>('GREEN', <Color.GREEN: 2>)
#=>('ALAIS_OF_RED', <Color.RED: 1>)
```

You can check and compare enum members by using the (identity)`is` or `is not` operators. We can also use the `==` or `!=` operator.

```python
a = Color.RED

a is Color.RED
#=> True

a == Color.RED
#=> True
```
