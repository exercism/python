# Introduction

Functions are first-class objects in Python, which means they can also be passed as arguments to other functions.
Decorators are [higher-order functions][hofunc] that take another function as an argument and return it after extending or modifying its behavior.
Decorators are defined in the same way as any other function, but they are applied on the line above the functions they are decorating using the `@` symbol before their names (`@my_decorator`). While they can take multiple arguments, decorators must take _at least_ the function they are decorating as an argument.
They can also be applied to class methods and even whole classes for the same reason - to extend them or modify their behaviors.

[hofunc]:https://en.wikipedia.org/wiki/Higher-order_function
