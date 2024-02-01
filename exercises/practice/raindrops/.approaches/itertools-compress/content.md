# Use itertools.compress()


```python
from itertools import compress

def convert(number):
    sounds ='Pling','Plang','Plong'
    mask =  ((number % factor) == 0 for factor in (3,5,7))
    return ''.join(compress(sounds, mask)) or str(number)
```

This approach uses both a `tuple` for storing sound strings and mask to filter them with.
For each factor, the `generator-expression` calculates `True` (_evenly divisible_) or `False` (_remainder left over_).
This mask is used with [`itertools.compress()`][compress] to 'mask over' any unwanted values in 'sounds'.
Finally, the returned string is created with [`str.join()`][join].
If the 'sounds' string is empty, a string version of the number is returned instead.

This is very succinct code that avoids string concatenation.
However, it does require the overhead of importing `compress()` from the [itertools][itertools] module.
The code is also harder to maintain should there be additional factors/sounds needed.
Because the factors and sounds are seperated, there is a chance mistakes could be made like forgetting a number or swapping which factor is paired with which sound.

A better approach for maintenance might be to turn the 'sounds' `tuple` into a dictionary where the factors and sounds can be stored separate from the logic that does the calculations and string creation:

```python
from itertools import compress

def convert(number):
    sounds = {3 : 'Pling',
              5 : 'Plang',
              7 : 'Plong'
             }
    mask =  ((number % factor) == 0 for factor in sounds.keys())
    return ''.join(compress(sounds.values(), mask)) or str(number)
```


In this rewrite, factors are keys with the sounds as values in a dictionary.
The mask then uses a [`dict.keys()`][dict-keys] [view][view objects] to iterate over the factors and calculate the `True`/`False` values.
This mask is used with `compress()` to filter a `dict.values()` view that is used by `join()` to construct the return string.
If the string is empty, a string version of the input number is returned instead.

[compress]: https://docs.python.org/3/library/itertools.html#itertools.compress
[dict-keys]: https://docs.python.org/3/library/stdtypes.html#dict.keys
[itertools]: https://docs.python.org/3/library/itertools.html
[join]: https://docs.python.org/3/library/stdtypes.html#str.join
[view objects]: https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects
