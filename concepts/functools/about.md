# About

The functools module is for higher-order functions: functions that act on or return other ***[functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)***. It provides functions for working with other functions and callable objects to use or extend them without completely rewriting them.

## Memoizing the function calls

**Memoizing:** Storing the result of some expensive function, which is called with the same input again and again. So, we don't have to run the function repeatedly.  

### ```@functools.lru_cache(maxsize=128, typed=False)```

***[@functools.lru_cache(maxsize=128, typed=False)](https://docs.python.org/3/library/functools.html#functools.lru_cache)*** Decorator to wrap a function with a memoizing callable that saves up to the maxsize most recent calls. It can save time when an expensive or I/O bound function is periodically called with the same arguments.

Since a dictionary is used to cache results, the positional and keyword arguments to the function must be hashable.

Here ```maxsize = 128``` means that it is going to memoize latest 128 function calls at max.

The lru_cache works the same way but it can cache at max maxsize calls and if type = True, then the function arguments of different types will be cached separately i.e. 5 and 5.0 will be cached differently.

### ```@functools.cache(user_function)```

***[@functools.cache(user_function)](https://docs.python.org/3/library/functools.html#functools.cache)***  the same as lru_cache(maxsize=None), creating a thin wrapper around a dictionary lookup for the function arguments. Because it never needs to evict old values, this is smaller and faster than ```lru_cache()``` with a size limit.

```python

>>> @cache
>>> def factorial(n):
>>>    return n * factorial(n-1) if n else 1

>>> factorial(10)      # no previously cached result, makes 11 recursive calls
3628800
>>> factorial(5)       # just looks up cached value result
120
>>> factorial(12)      # makes two new recursive calls, the other 10 are cached
479001600

# The lru_cache works the same way but it can cache at max maxsize calls and if type = True, then the function arguments of different types will be cached separately. 

# Some types such as str and int may be cached separately even when typed is false.

>>> @lru_cache(maxsize = 128)
>>> def factorial(n):
>>>     return n * factorial(n-1) if n else 1

>>> factorial(10)
3628800

# by the Following we can fetch the information about the cache.
>>> factorial.cache_info()
CacheInfo(hits=0, misses=11, maxsize=128, currsize=11)
```

## Generic functions

***[Generic functions](https://pymotw.com/3/functools/#generic-functions)*** are those which perform the operation based on the argument given to them. In statically typed languages it can be done by function overloading.

In python functools provides the `singledispatch()` decorator to register a set of generic functions for automatic switching based on the type of the first argument to a function.

The ```register()``` attribute of the function serves as another decorator for registering alternative implementations.To add overloaded implementations to the function, use the ```register(type)``` attribute of the generic function.

When user is going to call the function with the integer argument, then it will be redirected  to the function decorated with ```register(int)``` decorator.

The first function wrapped with singledispatch() is the default implementation if no other type-specific function is found, default implementation will be called.

```python

>>> from functools import singledispatch

>>> @singledispatch
    def fun(arg):
        print("default argument string: ", arg)


>>> fun.register(int)
    def _(arg): 
        print("This is an integer: ", arg)

>>> fun.register(list)
    def _(arg):
        print("This is a list: ", arg)

>>> fun("Hello")
"default argument string: Hello"

>>> fun(10)
"This is an integer: 10"

>>> fun([1,2,3])
"This is a list: [1,2,3]"

# This will call the default function as we didn't registered any function with float.
>>> fun(2.45)
"default argument string: 2.45"

```

For class methods we can use ***[singledispatchmethod(func)](https://docs.python.org/3/library/functools.html#functools.singledispatchmethod)*** to register a set of generic methods for automatic switching based on the type of the first non-self or non-class argument to a function.

```python

>>> class Negator:
        @singledispatchmethod
        def neg(self, arg):
            raise NotImplementedError("Cannot negate a")

        @neg.register(int)
        def _(self, arg):
            return -arg

        @neg.register(bool)
        def _(self, arg):
            return not arg

>>> obj = Negator()

# Going to call function which is register with bool datatype.
>>> obj.neg(True) 
False

# Going to call function which is register with int datatype.
>>> obj.neg(10)
-10

# Going to call default function and will display an error message.
>>> obj.neg("String")

```

## Partial

`functools.partial(func, /, *args, **keywords)` return a new ***[partial object](https://docs.python.org/3/library/functools.html#partial-objects)*** which when called will behave like func called with the positional arguments args and keyword arguments keywords. If more arguments are supplied to the call, they are appended to args.The ***[partial](https://docs.python.org/3/library/functools.html#functools.partial)*** is used for partial function application which “freezes” some portion of a function’s arguments and/or keywords resulting in a new object with a simplified signature.

```python

>>> def add(a, b):
    print(f"got a={a}, b={b}")
    print(a+b)

>>> a = partial(add, 10)
>>> a(4)
"got a=10, b=4"
14

# 10 got assigned to a because partial start assigning arguments from the left.

>>> a = partial(add, b=10)
>>> a(4)
"got a=4, b=10"
14

# But By using the keywords we can assign the value to the arguments at right

```

### partial Objects

partial objects are callable objects created by partial(). They have three read-only attributes:

```partial.func```

A callable object or function. Calls to the partial object will be forwarded to func with new arguments and keywords.

```partial.args```

The leftmost positional arguments that will be prepended to the positional arguments provided to a partial object call.

```partial.keywords```

The keyword arguments that will be supplied when the partial object is called.

```python

>>> from functools import partial

>>> pow_2 = partial(pow, exp = 2)

>>> pow_2.func == pow
True

>>> pow_2.args
()

>>> pow_2.keywords
{'exp': 2}

>>> two_pow = partial(pow, 2)

>>> two_pow(3) # 2(frezzed) ^ 3 = 8   == pow(2 [fixed] ,3 [passed by user])
8

>>> pow_2.args
(2,)

```

The ```pow_2.func``` is same as the ```pow``` function.

Here ```pow_2.args``` returns an empty tuple because we do not pass any positional argument to our partial object call.

```pow_2.keywords``` returns a dictionary of keywords argument which will be supplied when the partial object is called.

Here ```two_pow.args``` returns a ```(2,)``` tuple because we passed 2 as an argument while creating the partial object, which fixed the value of ```base``` argument as ```2```.

### ```partialmethod```

***[functools.partialmethod(func, /, *args, **keywords)](https://docs.python.org/3/library/functools.html#functools.partialmethod)*** Return a new partialmethod descriptor which behaves like partial except that it is designed to be used as a method definition rather than being directly callable.

```python

>>> class Cell:
        def __init__(self):
            self.alive = False
        
        def set_state(self, state):
            self.alive = bool(state)
        
        # going to return a method set_state with argument state = True
        set_alive = partialmethod(set_state, True)
        # going to return a method set_state with argument state = False
        set_dead = partialmethod(set_state, False)

>>> c = Cell()
>>> c.alive
False
>>> c.set_alive()
>>> c.alive
True

```

## Wraps

### `functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)`

***[functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)](https://docs.python.org/3/library/functools.html#functools.update_wrapper)*** Update a wrapper function to look like the wrapped function. The optional arguments are tuples to specify which attributes of the original function are assigned directly to the matching attributes on the wrapper function and which attributes of the wrapper function are updated with the corresponding attributes from the original function.

WRAPPER_ASSIGNMENTS (which assigns to the wrapper function’s `__module__`, `__name__`, `__qualname__`, `__annotations__` and `__doc__`, the documentation string)

WRAPPER_UPDATES (which updates the wrapper function’s `__dict__`, i.e. the instance dictionary).

```python

# without update_wrapper()

>>> def decorator(func):
        def wrapper(name):
            """Going to say Hello"""
            print("hello",name)
            func(name)
        return wrapper


>>> @decorator
    def fun(name):
        """Going to Wish"""
        print("good morning",name)

# In bigger python code base this will cause problem while debugging the code.
>>> fun.__name__
'wrapper'
>>> fun.__doc__
'Going to say Hello'

# with update_wrapper()

>>> def decorator(func):
        def wrapper(name):
            """Going to say Hello"""
            print("hello",name)
            func(name)
        update_wrapper(wrapper, func)
        return wrapper


>>> @decorator
    def fun(name):
        """Going to Wish"""
        print("good morning",name)

# Now the wrapper function just look like the wrapped(fun) function
>>> fun.__name__
'fun'
>>> fun.__doc__
'Going to Wish'
```

### `functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)`

***[functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)](https://docs.python.org/3/library/functools.html#functools.wraps)*** is a convenience function for invoking update_wrapper() as a function decorator when defining a wrapper function. It is equivalent to partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated).

```python

# This going to work same as the above where we are using the update_wrapper() function
>>> def decorator(func):
        @wraps(fun)
        def wrapper(name):
            """Going to say Hello"""
            print("hello",name)
            func(name)
        return wrapper


>>> @decorator
    def fun(name):
        """Going to Wish"""
        print("good morning",name)

# Now the wrapper function just look like the wrapped(fun) function
>>> fun.__name__
'fun'
>>> fun.__doc__
'Going to Wish'
```
