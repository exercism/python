## Hints

To support `list()`, see [implementing an iterator for a class.](https://docs.python.org/3/tutorial/classes.html#iterators)

Additionally, note that Python2's `next()` has been replaced by `__next__()` in Python3. For dual compatibility, `next()` can be implemented as:

```Python
def next(self):
    return self.__next__()
```
