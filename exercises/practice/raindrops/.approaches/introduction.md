# Introduction


The goal of the Raindrops exercise is to convert a number to a string of "raindrop sounds", based on whether the number
is divisible by any combination of 3, 5, or 7.
Numbers not divisible by any of these factors are returned as a string.

There are many different ways to solve this exercise in Python, with many many variations.
Some strategies optimize for simplicity, others for efficiency or extendability.
Others explore interesting features of Python.

Here, we go over 7 approaches:


1.  Using `if` statements and `+` to assemble a return string.
2.  Exploiting "Truthy" and "Falsy" values in ternary checks and an `f-string`
3.  Using one or more sequences, a `loop`, and an `f-string`.
4.  Using one or more sequences and a `generator-expression` within `join()`.
5.  Using a `dict` of `{factors : sounds}` for lookup and a `generator-expression` within `join()`.
6.  Using `itertools.compress()` and a `generator expression` within `join()`.
7.  Using `functools.reduce()` and `join()`.


## General Guidance


The goal of the Raindrops exercise is to return a string that represents which factors (`3`, `5` or `7`) evenly divide the input number.
Each factor has a _sound_ assigned ('Pling' (3), 'Plang' (5), or 'Plong'(7)).


Determining which factors divide into the input number without a remainder can most easily be accomplished via the [modulo][modulo] `%` operator.
However, it is also possible to import the [`math`][math-module] module and use the [`math.fmod()`][fmod] function for similar results, or the general built-in [`divmod()`][divmod] .
Keep in mind that `math.fmod()` returns a _float_ and `divmod()` returns a `tuple` of (quotient, remainder) that must be unpacked before use.
Using [`math.remainder()`][remainder] is **not** recommended for this exercise.


The challenge is to efficiently assemble a results string while also keeping in mind how the code might be maintained or extended.
How might you add additional factors without a complete rewrite of code?
How can you keep the code concise?
Do you use string concatenation, or are there other options you can choose?
What tradeoffs will you make between readability, space, and speed of processing?


## Approach: Using `if` statements

```python
def convert(num):
    sounds = ''
    
    if num % 3 == 0: sounds += 'Pling'
    if num % 5 == 0: sounds += 'Plang'
    if num % 7 == 0: sounds += 'Plong'
        
    return sounds if sounds else str(num)
```

This approach is the most straightforward or 'naive' - it replicates in code what the instructions say, using `if` statements to check the modulus for each factor.
Each is then concatenated to the 'sounds' string.
If the 'sounds' string is empty, a string version of the number is returned instead.

For more details, see the [if statement][approach-if-statements] approach.


## Approach: Using "Truthy" and "Falsy" Values with `f-string`s

```python
def convert(number):
    threes = '' if number % 3 else 'Pling' # Empty string if there is a remainder
    fives =  '' if number % 5 else 'Plang'
    sevens = '' if number % 7 else 'Plong'
    
    return f'{threes}{fives}{sevens}' or str(number)
  
  ###OR###
  
def convert(number):
    threes = 'Pling' if not number % 3 else '' # Sound if there is NOT a remainder
    fives =  'Plang' if not number % 5 else ''
    sevens = 'Plong' if not number % 7 else ''
    
    return f'{threes}{fives}{sevens}' or str(number)
```

This approach uses [ternary expressions][ternary expression] (_also known as 'conditional expressions'_) to build strings for each factor.
The result strings are combined via an `f-string`, avoiding the use of `join()`, or a `loop`.
If the `f-string` is empty _(evaluating to False in a [boolean context][truth-value-testing]_), a `str` of the input number is returned instead.

For more information, see the [Truthy and Falsy with f-string][approach-truthy-and-falsey-with-fstring]  approach.


## Approach: Using a `loop`, and an `f-string`


```python
def convert(number):
    sounds = ''
    drops = ("i", 3), ("a", 5), ("o", 7)

    for vowel, factor in drops:
        if number % factor == 0:
            sounds += f'Pl{vowel}ng'
    
    return sounds or str(number)
```

This approach loops through the _drops_ `tuple` (_although any iterable sequence can be used_), unpacking each `vowel` and `factor`.
If the input number is evenly divisible by the factor (_modulus == 0_), the corresponding vowel is inserted into the `f-string` for that factor.
The `f-string` is then concatenated to _sounds_ string via `+`.
 _Sounds_ is returned if it is not empty.
 Otherwise, a string version of the input number is returned.

For more details, see the [loop and f-string][approach-loop-and-fstring] approach.


## Approach: Using Sequence(s) with `join()`

```python
def convert(number):
    drops = ["Pling","Plang","Plong"]
    factors = [3,5,7]
    sounds = ''.join(drops[index] for 
                     index, factor in 
                     enumerate(factors) if (number % factor == 0))

    return sounds or str(number)
```


This approach is very similar to the  [loop and f-string][approach-loop-and-fstring] approach, but uses two `lists` to hold factors and sounds.
 It also converts the loop that calculates the remainders and sounds into a [`generator expression`][generator-expression] within `join()`, which assembles the 'sounds' string.
_Sounds_ is returned if it is not empty.
 Otherwise, a `str` version of the input number is returned.

For more information, see the [tuple with join][approach-sequence-with-join]  approach.


## Approach: Using a `dict` and `join()`

```python
def convert(number):

    sounds = {3: 'Pling',
              5: 'Plang', 
              7: 'Plong'}

    results = ''.join(sounds[divisor] for 
                      divisor in sounds.keys()
                      if number % divisor == 0)

    return results or str(number)
```

This approach uses a dictionary to hold the factor -> sound mappings and a `generator-expression` within `join()` to assemble results.
If 'results' is empty, a string version of the input number is returned.

For more details, read the [`dict` and `join()`][approach-dict-and-join]  approach.


## Approach:  Using `itertools.compress` and a `list` Mask

```python
from itertools import compress

def convert(number):
    sounds =('Pling','Plang','Plong')
    mask =  ((number % factor) == 0 for factor in (3,5,7))
    return ''.join(compress(sounds, mask)) or str(number)

```


This approach uses [`itertools.compress`][itertools-compress] to filter a list of sounds using a mask of `True` and `False` values.
The mask is formed by calculating `bool((input % factor) == 0)` for each factor (_which will return True or False_).
If the result of `itertools.compress` is empty, a string version of the input number is returned instead.

For more details, see the [itertools.compress][approach-itertools-compress] approach.


## Approach: Using `functools.reduce()` and `zip()`


```python
from functools import reduce

def convert(number):
    sounds = ('Pling','Plang','Plong')
    factors = ((number % factor) == 0 for factor in (3,5,7))
    result = reduce(lambda sound, item : sound + (item[0] * item[1]), zip(sounds, factors), '')
    
    return result or str(number)
```

This approach uses `functools.reduce` to join _sounds_ together using  the `int` value of `True` (1) and `False` (0).
Sounds are combined with their corresponding factor values in pairs via `zip()`, and subsequently unpacked for use in the [`functools.reduce`][functools-reduce] [`lambda` expression][lambda].
It is very similar to the `itertools.compress` method, but uses multiplication rather than mask to add or omit a given string value.

For more information, read the [functools.reduce][approach-functools-reduce] approach.


## Other approaches

Besides these seven approaches, there are a multitude of possible variations using different data structures and joining methods.

One can also use the new [structural pattern matching][structural-pattern-matching], although it is both more verbose and harder to read.
It (unnecessarily) lists out all of the mask variations from the [itertools compress][itertools-compress] approach and would be hard to extend without the potential of making a mistake with the factors, the sounds, or the masks:


```python
def convert(number):

    match [(number % factor) == 0 for factor in (3,5,7)]:
        case [True, True, True]:
            return 'PlingPlangPlong'
        case [True, True, False]:
            return 'PlingPlang'
        case [False, True, True]:
            return 'PlangPlong'
        case [True, False, True]:
            return 'PlingPlong'
        case [True, False, False]:
            return 'Pling'
        case [False, False, True]:
            return 'Plong'
        case [False, True, False]:
            return 'Plang'
        case _:
            return str(number)
```


## Which Approach to Use?

All approaches are idiomatic, and show multiple paradigms and possibilities.

Some additional considerations include readability and maintainability.
Approaches using separate data structures to hold sounds/factors are very helpful when additional data needs to be added, even if there is memory or performance overhead associated with them.
No one wants to add to an ever-growing block of `if-statements`, or reap the consequences of troubleshooting a typo in some strange embedded set of parenthesis.
Approaches using `join()` or `loops` are fairly succinct, and might be more easily understood by others reading your code, so that they can adjust or add to the logic.
Additionally, using an `f-string` can cut down on visual "noise" as you assemble the return string.

So an approach that balances maintenance needs with succinctness is likely the best option:

```python
def convert(number):
    #This is clear and easily added to.  Unless the factors get
    # really long, this won't take up too much memory.
    sounds = {3: 'Pling',
              5: 'Plang', 
              7: 'Plong'}

    results = (sound for 
               divisor, sound in sounds.items()
               if number % divisor == 0)

    return ''.join(results) or str(number)
```


This separates the code that calculates the results string from the factors themselves.
If a factor needs to be added, only the dictionary needs to be touched.
This code need only iterate over the items of the dictionary to do its calculation, making this `O(1)` in time complexity.
This does take `O(m)` space, where `m` is equal to the number of factor entries.
Since the number of factors is fixed here, this is unlikely to create issues unless a great many more are added to the 'sounds' `dict`.

To compare the performance of this and the other approaches, take a look at the [Performance article][article-performance].

[approach-dict-and-join ]: https://exercism.org/tracks/python/exercises/raindrops/approaches/dict-and-join
[approach-functools-reduce]:  https://exercism.org/tracks/python/exercises/raindrops/approaches/functools-reduce
[approach-if-statements]:  https://exercism.org/tracks/python/exercises/raindrops/approaches/if-statements
[approach-itertools-compress]:  https://exercism.org/tracks/python/exercises/raindrops/approaches/itertools-compress
[approach-loop-and-fstring]: https://exercism.org/tracks/python/exercises/raindrops/approaches/loop-and-fstring
[approach-sequence-with-join]: https://exercism.org/tracks/python/exercises/raindrops/approaches/sequence-with-join
[approach-truthy-and-falsey-with-fstring]:   https://exercism.org/tracks/python/exercises/raindrops/approaches/truthy-and-falsey-with-fstring
[article-performance]: https://exercism.org/tracks/python/exercises/raindrops/articles/performance
[divmod]: https://docs.python.org/3/library/functions.html#divmod
[fmod]: https://docs.python.org/3/library/math.html#math.fmod
[functools-reduce]: https://docs.python.org/3/library/functools.html#functools.reduce
[generator-expression]: https://peps.python.org/pep-0289/
[itertools-compress]: https://docs.python.org/3/library/itertools.html#itertools.compress
[lambda]: https://dbader.org/blog/python-lambda-functions
[math-module]: https://docs.python.org/3/library/math.html
[modulo]: https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/
[remainder]: https://docs.python.org/3/library/math.html#math.remainder
[ternary expression]: https://docs.python.org/3/reference/expressions.html#conditional-expressions
[truth-value-testing]: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
[structural-pattern-matching]: https://peps.python.org/pep-0622/
