# Using a Dictionary and `dict.get()`


```python
def score(x_coord, y_coord):
    point = (x_coord**2 + y_coord**2)
    scores = {
        point <= 100: 1,
        point <= 25: 5,
        point <= 1: 10
    }
    
    return scores.get(True, 0)
```

At first glance, this approach looks similar to the [Booleans as Integers][approach-boolean-values-as-integers] approach, due to the Boolean evaluation used in the dictionary keys.
However, this approach is **not** interpreting Booleans as integers and is instead exploiting three key properties of [dictionaries][dicts]:


1.  [Keys must be hashable][hashable-keys] — in other words, keys have to be _unique_.
2.  Insertion order is preserved (_as of `Python 3.7`_), and evaluation/iteration happens in insertion order.
3.  Duplicate keys _overwrite_ existing keys.
    If the first key is `True` and the third key is `True`, the _value_ from the third key will overwrite the value from the first key.

Finally, the `return` line uses [`dict.get()`][dict-get] to `return` a default value of 0 when a toss is outside the existing circle radii.
To see this in action, you can view this code on [Python Tutor][dict-get-python-tutor].


Because of the listed dictionary qualities, **_order matters_**.
This approach depends on the outermost scoring circle containing all smaller circles and that
checks proceed from largest --> smallest circle.
Iterating in the opposite direction will not resolve to the correct score.
The following code variations do not pass the exercise tests:


```python

def score(x_coord, y_coord):
    point = (x_coord**2 + y_coord**2)
    scores = {
        point <= 1: 10,
        point <= 25: 5,
        point <= 100: 1,
    }
    
    return scores.get(True, 0)
    
    #OR#

def score(x_coord, y_coord):
    point = (x_coord**2 + y_coord**2)
    scores = {
        point <= 25: 5,
        point <= 1: 10,
        point <= 100: 1,
    }
    
    return scores.get(True, 0)
    
```

While this approach is a _very clever_ use of dictionary properties, it is likely to be very hard to reason about for those who are not deeply knowledgeable.
Even those experienced in Python might take longer than usual to figure out what is happening in the code.
Extensibility could also be error-prone due to needing a strict order for the `dict` keys.

This approach offers no space or speed advantages over using `if-statements` or other strategies, so is not recommended for use beyond a learning context.

[approach-boolean-values-as-integers]: https://exercism.org/tracks/python/exercises/darts/approaches/boolean-values-as-integers
[dicts]: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
[dict-get]: https://docs.python.org/3/library/stdtypes.html#dict.get
[dict-get-python-tutor]: https://pythontutor.com/render.html#code=def%20score%28x_coord,%20y_coord%29%3A%0A%20%20%20%20point%20%3D%20%28x_coord**2%20%2B%20y_coord**2%29%0A%20%20%20%20scores%20%3D%20%7B%0A%20%20%20%20%20%20%20%20point%20%3C%3D%20100%3A%201,%0A%20%20%20%20%20%20%20%20point%20%3C%3D%2025%3A%205,%0A%20%20%20%20%20%20%20%20point%20%3C%3D%201%3A%2010%0A%20%20%20%20%7D%0A%20%20%20%20%0A%20%20%20%20return%20scores.get%28True,%200%29%0A%20%20%20%20%0Aprint%28score%281,3%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false
[hashable-keys]: https://www.pythonmorsels.com/what-are-hashable-objects/#dictionary-keys-must-be-hashable
