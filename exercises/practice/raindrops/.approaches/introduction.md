# Introduction

There are multiple Pythonic ways to solve the Raindrops exercise.
Among them are:

- Using `if` statements and `+`to assemble a return string.
- Using a `loop` , an `f-string`, and  `+` to assemble the return string.
- Using a `tuple` of (factor, sound) pairs and a generator expression with `join()` to assemble the return string.
- Exploiting "Truthy" and "Falsy" values in ternary checks and an `f-string`
- Using a `dict` of `{factors : sounds}` for lookup and a generator expression with `join()` to assemble the return string.
- Using itertools compress and  a `generator expression` with `join()` to assemble the return string..
- Using `functools.reduce()`


## General guidance


The goal of the Raindrops exercise is to return a string that represents which which factors (`3`, `5` or `7`) evenly divide the input number.

Each factor has a _sound_  assigned ('Pling' (3), 'Plang' (5), or 'Plong'(7)).


Determining which factors evenly divide the input number can most easily be accomplished via the [modulo][modulo] `%` operator.
The challenge is to efficiently determine the factors while assembling a results string (_sounds_).


## Approach: Using `if` statements

```python
def convert(num):
    sounds = ''
    
    if num % 3 == 0:
        sounds += 'Pling'
    if num % 5 == 0:
        sounds += 'Plang'
    if num % 7 == 0:
        sounds += 'Plong'
        
    return sounds if sounds else str(num)

```

This approach uses `if` statements to check the modulus for each factor.
If the number is evenly divisible by the factor (modulo == 0), the corresponding string is concatenated to  _sounds_ via the `+` operator.
If _sounds_ is returned if it is not empty (_see [Truth Value Testing][truth-value-testing] for more info_).  Otherwise, a `str` version of the input number is returned.

For more details, see the [if statement][approach-if-statements] approach.


## Approach: Using a `loop` and an  `f-string`

```python
def convert(number):
    sounds = ''
    drops = ("i", 3), ("a", 5), ("o", 7)

    for vowel, factor in drops:
        if number % factor == 0:
            sounds += f'Pl{vowel}ng'
    
    return sounds or str(number)
```


This approach loops through the _drops_ `tuple`, unpacking each `vowel` and `factor`.
If the input number is evenly divisible by the factor (modulus == 0), the corresponding vowel is inserted into the `f-string`.
The `f-string` is then concatenated to _sounds_ via `+`.
 _Sounds_ is returned if it is not empty.
 Otherwise, a `str` version of the input number is returned.

For more details, see the [loop and f-string][approach-loop-and-fstring] approach.


## Approach: Using a `tuple` with `join()`

```python
def convert(num):
    drops = ('i', 3), ('a', 5), ('o', 7)
    sounds = ''.join(f'Pl{vowel}ng'
                      for vowel, factor in drops
                      if num % factor == 0)
    
    return  sounds or str(num)
```


This approach is very similar to the  [loop and f-string][approach-loop-and-fstring] approach, but puts the `loop` inside `str.join()` as a [`generator expression`][generator-expression].
_Sounds_ is returned if it is not empty.
 Otherwise, a `str` version of the input number is returned.

For more information, see the [tuple with join][approach-tuple-with-join]  approach.



## Approach: Using "Truthy" and "Falsy" Values with an `f-string`

```python
def convert(number):
    threes = '' if number % 3 else 'Pling' # Empty string if there is a remainder
    fives =  '' if number % 5 else 'Plang'
    sevens = '' if number % 7 else 'Plong'
    
    return f'{threes}{fives}{sevens}' or str(number)
  
  #OR#
  
def convert(number):
    threes = 'Pling' if not number % 3 else '' # Sound if there is NOT a remainder
    fives =  'Plang' if not number % 5 else ''
    sevens = 'Plong' if not number % 7 else ''
    
    return f'{threes}{fives}{sevens}' or str(number)
```

This approach uses [ternary expressions][ternary-expression] to build strings for each factor.
The result strings are combined via an `f-string`, avoiding the use of `join()` or `loops`.
If the `f-string` is empty _(evaluating to False in a boolean context_), a `str` of the input number is returned instead.

For more information, see the [Truthy and Falsy with f-string][approach-truthy-and-falsey-with-fstring]  approach.




## Approach: Using a `dict` and `join()`

```python
def convert(number):

    sounds = {3: 'Pling', 5: 'Plang', 7: 'Plong'}

    results = ''.join(sounds[divisor] for 
                      divisor, sound in sounds.items()
                      if number % divisor == 0)

    return results or str(number)
```


This approach uses a dictionary to hold the factor -> sound mappings and a generator expression inside of `join()` to assemble _results_.
If _results_ is empty, a string version of the input number is returned.

For more details, read the [`dict` and `join()`][approach-dict-and-join]  approach.


## Approach:  Using `itertools.compress` and a `list` Mask

```python
from itertools import compress

def convert(number):
    sounds =('Pling','Plang','Plong')
    mask =  ((number % factor) == 0 for factor in (3,5,7))
    return ''.join(compress(sounds, mask)) or str(number)

```


This approach uses [`itertools.compress`][itertools-compress] to filter a list of sounds using a mask of True and False values.
The mask is formed by calculating `bool((input % factor) == 0)` for each factor (_which will return True or False_).
If the result of `itertools.compress` is empty, a string version of the input number is returned instead.

For more details, see the [itertools.compress][approach-itertools-compress] approach.


## Approach: Using `functools.reduce` and `zip()`

```python
from functools import reduce

def convert(number):
    sounds = ('Pling','Plang','Plong')
    factors = ((number % factor) == 0 for factor in (3,5,7))
    result = reduce(lambda sound, item : sound + (item[0] * item[1]), zip(sounds, factors), '')
    
    return result or str(number)
```

This approach uses `functools.reduce` to join _sounds_ together using  the `int` value of True (1) and False (0).
Sounds are combined with their corresponding factor values in pairs via `zip()`, and subsequently unpacked for use in the `itertools.reduce` [lambda expression][lambda].
It is very similar to the `itertools.compress` method, but uses multiplication to add or omit a given string value.

For more information, read the [functools.reduce][approach-functools-reduce] approach.



## Other approaches

Besides these seven idiomatic approaches, there are a multitude of possible variations using different data structures and joining methods.

One can also use the new [structural pattern matching][structural-pattern-matching], although it is both more verbose and harder to read, so is not recommended.


```python
def convert(number):
    phrase ='PlingPlangPlong'
    factor_array =  [(number % factor) == 0 for factor in (3,5,7)] # Creates a list of True and False
    
    match factor_array:
        case [True, True, True]:
            return phrase
        case [True, True, False]:
            return phrase[:10]
        case [True, False, True]:
            return phrase[:5] + phrase[10:]
        case [False, True, True]:
            return phrase[5:]
        case [True, False, False]:
            return phrase[:5]
        case [False, True, False]:
            return phrase[5:10]
        case [False, False, True]:
            return phrase[10:]
        case _:
            return str(number)
```



## Which approach to use?

All seven approaches are idiomatic, and show multiple paradigms and possibilities.

The fastest is

While the slowest is

Some additional considerations include readability and maintainability.
Approaches using separate data structures to hold sounds/factors are very helpful when additional data needs to be added, even if there is memory or performance overhead associated with them.
Approaches using `join()` or `loops` are fairly succinct, and might be more easily understood by others reading your code,  so that they can adjust or add to the logic.
Additionally, `f-strings` can cut down on visual "noise" as you assemble the return string.


To compare the performance and other tradeoffs of the approaches, take a look at the [Performance article][article-performance].

[ approach-dict-and-join ]:  https://exercism.org/tracks/python/exercises/raindrops/approaches/dict-and-join
[ approach-tuple-with-join ]:   https://exercism.org/tracks/python/exercises/raindrops/approaches/tuple-with-join
[approach-functools-reduce]:  https://exercism.org/tracks/python/exercises/raindrops/approaches/functools-reduce
[approach-if-statements]:  https://exercism.org/tracks/python/exercises/raindrops/approaches/if-statements
[approach-itertools-compress]:  https://exercism.org/tracks/python/exercises/raindrops/approaches/itertools-compress
[approach-loop-and-fstring]: https://exercism.org/tracks/python/exercises/raindrops/approaches/loop-and-fstring
[approach-truthy-and-falsey-with-fstring]:   https://exercism.org/tracks/python/exercises/raindrops/approaches/truthy-and-falsey-with-fstring
[article-performance]: ttps://exercism.org/tracks/python/exercises/raindrops/articles/performance
[generator-expression]: https://peps.python.org/pep-0289/
[itertools-compress]: https://docs.python.org/3/library/itertools.html#itertools.compress
[lambda]: https://dbader.org/blog/python-lambda-functions
[modulo]: https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/
[truth-value-testing]: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
