# About

`Complex numbers` are not complicated.
They just need a less alarming name.

They are so useful, especially in engineering and science, that Python includes [`complex`][complex] as a standard numeric type alongside integers ([`int`s][ints]) and floating-point numbers ([`float`s][floats]).


## Basics

A `complex` value in Python is essentially a pair of floating-point numbers.
These are called the "real" and "imaginary" parts, for unfortunate historical reasons.
Again, it is best to focus on the underlying simplicity and not the strange names.

There are two common ways to create complex numbers.

1) The [`complex(real, imag)`][complex] constructor takes two `float` parameters:

```python
>>> z1 = complex(1.5, 2.0)
>>> z1
(1.5+2j)
```

The constructor can also parse string input.
This has the odd limitation that it fails if the string contains spaces.

```python
>>> complex('4+2j')
(4+2j)

>>> complex('4 + 2j')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: complex() arg is a malformed string
```


2) The complex number can be specified as `<real part> + <complex part>j` literal, or just `<complex part>j` if the real part is zero:


```python
>>> z2 = 2.0 + 1.5j
>>> z2
(2+1.5j)
```
The end result is identical to using the `complex()` constructor.


There are two rules for that imaginary part of the complex number:


- It is designated with `j` (not `i` as you may see in math textbooks).

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

Most engineers are happy with `j`.
Most scientists and mathematicians prefer the mathematical notation `i` for _imaginary_, but that notation conflicts with the use of `i` to mean _current_ in Electrical Engineering.
So in designing Python, the Electrical Engineers won.


To access the parts of a complex number individually:

```python
>>> z2.real
2.0
>>> z2.imag
1.5
```

Either part can be zero and mathematicians may then talk of the number being "wholly real" or "wholly imaginary".
However, it is still a complex number in Python:


```python
>>> complex(0, 1)
1j
>>> type(complex(0, 1))
<class 'complex'>

>>> complex(1, 0)
(1+0j)
```

You may have heard that "`i` (or `j`) is the square root of -1".

For now, all this means is that the imaginary part _by definition_ satisfies the equality
```python
1j * 1j == -1  # => True
```

This is a simple idea, but it leads to interesting consequences.

## Arithmetic

Most of the [`operators`][operators] used with floats and ints also work with complex numbers:


```python
>>> z1 = (1.5+2j)
>>> z2 = (2+1.5j)


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

>>> 1j ** 2  # j * j == -1
(-1+0j)
```

Explaining the rules for complex number multiplication and division is out of scope for this concept (_and you are unlikely to have to perform those operations "by hand" very often_).

Any [mathematical][math-complex] or [electrical engineering][engineering-complex] introduction to complex numbers will cover this, should you want to dig into the topic.

Alternatively, Exercism has a `Complex Numbers` practice exercise where you can implement a complex number class with these operations from first principles.


Integer division is ___not___ possible on complex numbers, so the `//` and `%` operators and `divmod()` functions will fail for the complex number type.


There are two functions implemented for numeric types that are very useful when working with complex numbers:

- `<complex number>.conjugate()` simply flips the sign of the imaginary part of a complex number (_from + to - or vice-versa_).
    - Because of the way complex multiplication works, this is more useful than you might think.
- `abs(<complex number>)` is guaranteed to return a real number with no imaginary part.


```python
>>> z1
(1.5+2j)

>>> z1.conjugate() # flip the z1.imag sign
(1.5-2j)

>>> abs(z1) # sqrt(z1.real ** 2 + z1.imag ** 2)
2.5
```

## The `cmath` module

The Python standard library has a [`math`][math-module] module full of useful functionality for working with real numbers.

It also has an equivalent [`cmath`][cmath] module for working with complex numbers.


We encourage you to read through the module and experiment, but the main categories are:

- Conversion between Cartesian and polar coordinates,
- Exponential and log functions,
- Trigonometric functions,
- Hyperbolic functions,
- Classification functions, and
- Useful constants.

Here is an example using some constants:

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
So they are used widely in electrical engineering, audio processing, physics, computer gaming, and navigation - to name only a few applications.

You can see things rotate.
Complex numbers may not make the world go round, but they are great for explaining _what happens_ as a result of the world going round: look at any satellite image of a major storm.


Less obviously, sound is wave-like, light is wave-like, radio signals are wave-like, and even the economy of your home country is at least partly wave-like.


A lot of this wave processing can be done with trig functions (`sin()` and `cos()`) but that gets messy quite quickly.

Complex exponentials are ___much___ easier to work with.

### But I don't need complex numbers!


Only true if you are living in a cave and foraging for your food.

If you are reading this on any sort of screen, you are utterly dependent on some useful 20th-Century advances made through the use of complex numbers.


1. __Semiconductor chips__. 
    - These make no sense in classical physics and can only be explained (and designed) by quantum mechanics (QM).
    - In QM, everything is complex-valued by definition. (_its waveforms all the way down_)

2. __The Fast Fourier Transform algorithm__. 
    - FFT is an application of complex numbers, and it is in _everything_ connected to sound transmission, audio processing, photos, and video.

    -MP3 and other audio formats use FFT for compression, ensuring more audio can fit within a smaller storage space. 
    - JPEG compression and MP4 video, among many other image and video formats also use FTT for compression.

    - FFT is also deployed in the digital filters that allow cellphone towers to separate your personal cell signal from everyone else's.


So, you are probably using technology that relies on complex number calculations thousands of times per second.


[complex]: https://docs.python.org/3/library/functions.html#complex
[cmath]: https://docs.python.org/3/library/cmath.html
[operators]: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
[math-module]: https://docs.python.org/3/library/math.html
[math-complex]: https://www.nagwa.com/en/videos/143121736364/
[engineering-complex]: https://www.khanacademy.org/science/electrical-engineering/ee-circuit-analysis-topic/ee-ac-analysis/v/ee-complex-numbers
[ints]: https://docs.python.org/3/library/functions.html#int
[floats]: https://docs.python.org/3/library/functions.html#float

