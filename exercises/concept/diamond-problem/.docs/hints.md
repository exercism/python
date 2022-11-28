# Hinsts

## 1. Class creation

- Is good practice to start the names of `classes` with an upper case letter.
- Is important to be consistent with your syntax scheme.

## 2. Constructor creation

- Remember, if during `inheritance` the `methods` and `attributes` of the `parent class` become visible under the `child class` (if those are not designated as prived).

## 3. Initializing sequence

- Remember, the order in which the classes are `extended` between the parentesis of our new class influences how they will be call in case we made use of the `super()` method.

```python
>>>class Child(Parent1, Parent2, Parent3):
...     pass
```
> Extended: sinonim of inherit.

- Using `super()` calls and `class calls` for initialization at the same time can be messy, try to stick to one method.
- Remember, the order and position in which the diferent `__init__` methods get call influence in the final result.

## 4. Return sequence method

- Try to use a `mix-in` class.
- The atributes this class works with doesn't have to be present on intself, because a `mix-in` class isn't meant to be initialize.
- Remember, `mix-in` classes follow the naming convention of `<name>Mixin`.