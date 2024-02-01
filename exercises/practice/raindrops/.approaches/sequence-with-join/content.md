# Sequence(s) with str.join()

```python
def convert(number):
    drops = ["Pling","Plang","Plong"]
    factors = [3,5,7]
    sounds = ''.join(drops[index] for 
                     index, factor in 
                     enumerate(factors) if (number % factor == 0))

    return sounds or str(number)
```

This approach is very similar to the [loop and f-string][approach-loop-and-fstring] approach, but uses two `lists` to hold factors and sounds and [`enumerate()`][enumerate] to extract an index.
 It also converts the loop that calculates the remainders and sounds into a [`generator expression`][generator-expression] within `join()`.
_Sounds_ is returned if it is not empty.
 Otherwise, a `str` version of the input number is returned.

 This, like most approaches described here is `O(1)` time and space complexity.
 In benchmark timings, the `generator-expression` and multiple variables add a bit of overhead.

 Readability here might not be the easiest for those not used to reading generator expressions inside calls to other functions, so if that is the case, this can be re-written as:


 ```python
def convert(number):
    drops = ["Pling","Plang","Plong"]
    factors = [3,5,7]
    sounds = (drops[index] for index, factor in 
              enumerate(factors) if (number % factor == 0))

    return ''.join(sounds) or str(number)
```

[approach-loop-and-fstring]: https://exercism.org/tracks/python/exercises/raindrops/approaches/loop-and-fstring
[generator-expression]: https://peps.python.org/pep-0289/
[enumerate]: https://docs.python.org/3/library/functions.html#enumerate
