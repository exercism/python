# About

`Complex numbers` are not complicated.
They just need a less alarming name.

They are so useful, especially in engineering and science, that Python includes [`complex`][complex] as a standard numeric type alongside integers ([`int`s][ints]) and floating-point numbers ([`float`s][floats]).


## Basics

A `complex` value in Python is essentially a pair of floating-point numbers.
These are called the "real" and "imaginary" parts, for unfortunate historical reasons.
Again, it is best to focus on the underlying simplicity and not the strange names.

There are two common ways to create complex numbers.

The `complex(real, imag)` constructor takes two `float` parameters:

```python
>>> z1 = complex(1.5, 2.0)
>>> z1
(1.5+2j)
```

Most engineers are happy with `j`.
Most scientists and mathematicians prefer the mathematical notation `i`, but in designing Python the engineers won.


So there are two rules for an imaginary part:
- It is designated with `j` not `i`.
- The `j` must immediately follow a number, to prevent Python seeing it as a variable name. If necessary, use `1j`.

```python
>>> j
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'j' is not defined

>>> 1j
1j

>>> type(1j)
<class 'complex'>
```

With this, we have a second and perhaps clearer way to create a complex number:
```python
>>> z2 = 2.0 + 1.5j
>>> z2
(2+1.5j)
```
The end result is identical to using a constructor.

To access the parts individually:
```python
>>> z2.real
2.0
>>> z2.imag
1.5
```

## Arithmetic

Most of the [`operators`][operators] used with floats and ints also work with complex numbers:


```python
>>> z1, z2
((1.5+2j), (2+1.5j))

>>> z1 + z2  # addition
(3.5+3.5j)

>>> z1 - z2  # subtraction
(-0.5+0.5j)

>>> z1 * z2  # multiplication
6.25j

>>> z1 / z2  # division
(0.96+0.28j)

>>> z1 ** 2  # exponentiation
(-1.75+6j)

>>> 2 ** z1  # another exponentiation
(0.5188946835878313+2.7804223253571183j)

>>> 1j ** 2 # j is the square root of -1
(-1+0j)
```

Explaining the rules for complex multiplication and division is out of scope here.
Any introduction to complex numbers will cover this.
Alternatively, Exercism has a `Complex Numbers` practice exercise where you can implement this from first principles.

Integer division is ___not___ possible on complex numbers, so the `//` and `%` operators and `divmod()` function will fail.

There are two functions that are useful with complex numbers:
- `conjugate()` simply flips the sign of the complex part.
Because of the way complex multiplication works, this is more useful than you might think.
- `abs()` is guaranteed to return a real number with no imaginary part.

```python
>>> z1
(1.5+2j)

>>> z1.conjugate() # flip the z1.imag sign
(1.5-2j)

>>> abs(z1) # sqrt(z1.real ** 2 + z1.imag ** 2)
2.5
```

## The `cmath` module

The Python standard library has a `math` module full of useful functionality for working with real numbers.
It also has an equivalent `cmath` module for complex numbers.

Details are available in the [`cmath`][cmath] module documents, but the main categories are:
- conversion between Cartesian and polar coordinates
- exponential and log functions
- trig functions
- hyperbolic functions
- classification functions
- useful constants

```python
>>> import cmath

>>> euler = cmath.exp(1j * cmath.pi) # Euler's equation

>>> euler.real
-1.0
>>> round(euler.imag, 15) # round to 15 decimal places
0.0
```

So a simple expression with three of the most important constants in nature `e`, `i` (or `j`) and `pi` gives the result `-1`. 
Some people believe this is the most beautiful result in all of mathematics.
It dates back to around 1740.

-----

## Optional section: a Complex Numbers FAQ

This part can be skipped, unless you are interested.

### Isn't this some strange new piece of pure mathematics?

It was strange and new in the 16th century.

500 years later, it is central to most of engineering and the physical sciences.

### Why would anyone use these?

It turns out that complex numbers are the simplest way to describe anything that rotates or anything with a wave-like property.

You can see things rotate.
Complex numbers may not make the world go round, but they are great for explaining what happens as a result of the world going round: look at any satellite image of a major storm.

Less obviously, sound is wave-like, light is wave-like, radio signals are wave-like, The economy of your home country is at least partly wave-like.

A lot of this can be done with trig functions (`sin()` and `cos()`) but that gets messy quickly.
Complex exponentials are ___much___ easier to work with.

### But I never use complex numbers!

Only true if you are living in a cave and foraging for your food.

If you read this on any sort of screen, you are utterly dependent on some useful 20th-centry advances.

1. __Semiconductor chips__. 
    - These make no sense in classical physics and can only be explained (and designed) by quantum mechanics (QM).
    - In QM, everything is complex-valued by definition.
2. __The Fast Fourier Transform algorithm__. 
    - FFT is an application of complex numbers, and it is in everything.
    - Audio files? MP3 and other formats use FFT for compression. So does MP4 video, JPEG photos, among many others.
    - Also, it is in the digital filters that let a cellphone mast separate your signal from everyone else's.

So, you are probably using complex numbers thousands of times per second.
Be grateful to the tech people who understand this stuff so that you maybe don't need to.

[complex]: https://docs.python.org/3/library/functions.html#complex
[cmath]: https://docs.python.org/3/library/cmath.html
[operators]: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
