# Introduction

`Complex numbers` are not complicated.
They just need a less alarming name.

They are so useful, especially in engineering and science (_everything from JPEG compression to quantum mechanics_), that Python includes [`complex`][complex] as a standard numeric type alongside integers ([`int`s][ints]) and floating-point numbers ([`float`s][floats]).

A `complex` value in Python is essentially a pair of floating-point numbers:

```python
>>> my_complex = 5.443+6.77j
(5.443+6.77j)
```

These are called the "real" and "imaginary" parts.
You may have heard that "`i` (or `j`) is the square root of -1".
For now, all this means is that the imaginary part _by definition_ satisfies the equality `1j * 1j == -1`.
This is a simple idea, but it leads to interesting mathematical consequences.

In Python, the "imaginary" part is designated with `j` (_not `i` as you would see in math textbooks_), and
the `j` must immediately follow a number, to prevent Python seeing it as a variable name:


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


## Arithmetic

Most of the [`operators`][operators] used with floats and ints also work with complex numbers.

Integer division is _**not**_ possible on complex numbers, so the `//` and `%` operators and `divmod()` functions will fail for the complex number type.

Explaining the rules for complex number multiplication and division is out of scope for this concept (_and you are unlikely to have to perform those operations "by hand" very often_).

Any [mathematical][math-complex] or [electrical engineering][engineering-complex] introduction to complex numbers will cover these scenarios, should you want to dig into the topic.

The Python standard library has a [`math`][math-module] module full of useful functionality for working with real numbers and the [`cmath`][cmath] module is its equivalent for working with complex numbers.


[cmath]: https://docs.python.org/3/library/cmath.html
[complex]: https://docs.python.org/3/library/functions.html#complex
[engineering-complex]: https://www.khanacademy.org/science/electrical-engineering/ee-circuit-analysis-topic/ee-ac-analysis/v/ee-complex-numbers
[floats]: https://docs.python.org/3/library/functions.html#float
[ints]: https://docs.python.org/3/library/functions.html#int
[math-complex]: https://www.nagwa.com/en/videos/143121736364/
[math-module]: https://docs.python.org/3/library/math.html
[operators]: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
