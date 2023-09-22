
## `if-checks`

Straightforward, but verbose.

```python
def convert(number):
    sound = ''
    if number % 3 == 0:
        sound += 'Pling'
    if number % 5 == 0:
        sound += 'Plang'
    if number % 7 == 0:
        sound += 'Plong'
    if sound == '':
        return str(number)
    return sound
```


## Let's Play with `f-strings`


This strategy reads a bit better, and is faster than using `+` --  with or without a variable.
Also uses `f-strings` (fun!).

However, it's probably fiddly and error prone to maintain - code has to be added/changed in two places, and that encourages typos and mis-matches.
This would also quickly get out of hand with more than about 5 sounds/factors.

```python
def convert(number):
    threes = '' if number % 3 else 'Pling'
    fives =  '' if number % 5 else 'Plang'
    sevens = '' if number % 7 else 'Plong'
    
    sounds = f'{threes}{fives}{sevens}' 
    
    return sounds if sounds else str(number)
    
    
    """ 
    sounds can also be written like this:
    sounds = (f'{"" if number % 3 else "Pling"}'
              f'{"" if number % 5 else "Plang"}'
              f'{"" if number % 7 else "Plong"}')
    """   
```


## Be Lazy and Enumerate

We can use `enumerate()` and `index` into a list.
But we're using two `lists` - so two places to change things, and two chances to mess them up.
And do we really need that ternary  to check if the string is empty??


```python
def convert(number):
    sounds = ''
    results = ['Pling', 'Plang', 'Plong']
    
    for index, factor in enumerate([3, 5, 7]):  # enumerating the factors so that results can be indexed.
        if number % factor == 0:
            sounds += results[index]
    
    return sounds if souds else str(number)
```


## Tuples with `f-strings` are cool

So let's use a nested tuple.
It can't be accidentally mutated, it's a bit smaller in memory, and then we have only one data structure to deal with/change.
We can also get away with only using the _vowel_ for each word, and use an `f-string` to make each full sound, based on changing the vowel.
We're back to using string concatenation via `+` though, which is ... not great.
And we're re-making the `drops` tuple every time we call the function.
An `or` in the return eliminates the excess ternary.


```python
def convert(number):
    sounds = ''
    drops = ("i", 3), ("a", 5), ("o", 7)

    for vowel, factor in drops:      #unpacking each tuple
        if number % factor == 0:
            sounds += f'Pl{vowel}ng' #not really sure if this is easily readable, tho.
    
    return sounds or str(number)  # An empty string is considered 'falsy' and evaluates to False in a boolean context.
```


## Going Global, Losing Explicit Loops, and `''.join()`-ing


We move the tuple to the global/module scope, so it is made on module load and not function call.
We can eliminate that verbose loop by using a `list-comprehension`.
And we can avoid the overhead of `+` by using `str.join()` to assemble the result.
But we don't really need that list taking up memory - it just gets immediately unpacked by `''.join()`.


```python
# Tuple now moves to module/global context & doesn't need re-allocation for each function invocation.
DROPS = ("i", 3), ("a", 5), ("o", 7) 

def convert(number):
    # The below takes advantage of False being a subclass of 
    # `int`, &  so not 0 --> True in this context.  
    sounds = [f"Pl{vowel}ng" for vowel, factor in DROPS if not number % factor] 

    return ''.join(sounds) or str(number)
```

## Generate the Join

Now the sounds are in a `generator expression`, which doesn't take up memory space in the same way a list does.
But that tuple could get out of hand if a lot moe letters or factors were added.
Some people like dictionaries better - and while that `f-string` is cool, maybe it would be clearer if we spelled everything out?

```python
DROPS = ("i", 3), ("a", 5), ("o", 7) 

def convert(number):
    sounds = ''.join(f"Pl{vowel}ng" for vowel, factor in DROPS if not number % factor)

    return sounds or str(number)
```


## Lookups Read Better

So we swap the `tuple` for a bulkier (but hopefully more maintainable) dictionary.
The syntax changes in the generator to reflect dict lookups.
And we're more or less done.


```python
DROPS = {3: "Pling",5: "Plang", 7: "Plong"}

def convert(number):
    answer =  ''.join(DROPS[divisor] for divisor in DROPS.keys() if number % divisor == 0)
    
    return answer or str(number)
```


## Bonus Code Golfing Round

For the code golfer in all of us....


```python
DROPS = {3: "Pling",5: "Plang", 7: "Plong"}

def convert(number):
    return ''.join(DROPS[divisor] for divisor in 
                   DROPS.keys() if 
                   not number % divisor) or str(number)
```

And here we're eliminating the constant (and going back to using a nested tuple). Again, having a return line this dense is a bit of an anti-pattern  - but it is short.

```python
def convert(number):
    return ''.join(sound for sound, divisor in 
                   (("Pling", 3), ("Plang", 5), ("Plong", 7))  if 
                   not number % divisor) or str(number)
```
