# Sequence(s) with a Loop and f-string


```python
def convert(number):
    sounds = ''
    drops = ("i", 3), ("a", 5), ("o", 7)

    for vowel, factor in drops:
        if number % factor == 0:
            sounds += f'Pl{vowel}ng'
    
    return sounds or str(number)
```


This approach loops through the _drops_ `tuple` (_although any iterable sequence(s) can be used_), unpacking each `vowel` and `factor`.
If the input number is evenly divisible by the factor (_modulus == 0_), the corresponding vowel is inserted into the `f-string` for that factor.
The `f-string` is then concatenated to _sounds_ string via `+`.
 _Sounds_ is returned if it is not empty.
 Otherwise, a string version of the input number is returned.

 This takes `O(1)` time and `O(1)` space.

It is a very efficient and clever way of building up the return string, since only one vowel is changing per 'drop'.
However, it might take a moment for others reading the code to understand what exactly is going on.
It also (may) create maintenance difficulties should there be future factors and sounds that do not conform to the pattern of only changing the vowel in the sound.

A much less exciting (_but perhaps easier to maintain_) rewrite would be to store the whole drop sound and build up the return string out of whole drops:


```python
def convert(number):
    sounds = (3, 'Pling'), (5, 'Plang'), (7, 'Plong')
    output = ''
    
    for factor, sound in sounds:
       if number % factor == 0:
           output += sound
    
    return output or str(number)
```

This has the same time and space complexity as the first variation.
