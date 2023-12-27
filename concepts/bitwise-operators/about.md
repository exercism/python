# About

Down at the hardware level, transistors can only be on or off: two states that we traditionally represent with `1` and `0`.
These are the [`binary digits`][binary-digits], abbreviated as [`bits`][bits].
Awareness of `bits` and `binary` is particularly important for systems programmers working in low-level languages.

However, for most of the history of computing the programming priority has been to find increasingly sophisticated ways to _abstract away_ this binary reality.
In Python (and many other [high-level programming languages][high-level-language]), we work with `int`, `float`, `string` and other defined _types_, up to and including audio and video formats.
We let the Python internals take care of (eventually) translating everything to bits.

Nevertheless, using [bitwise-operators][python-bitwise-operators] and [bitwise operations][python-bitwise-operations] can sometimes have significant advantages in speed and memory efficiency, even in a high-level language like Python.


## Entering and Displaying Binary Numbers

Unsurprisingly, Python interacts with the user using decimal numbers, but a programmer can override this default.
In fact, Python will readily accept an `int` in `binary`, `hexadecimal`, or `octal` format, and will happily perform mathematical operations between them.
For more details, you can review the [concept:python/binary-octal-hexadecimal]() concept.

Binary numbers are entered with a `0b` prefix, just as `0x` can be used for hexadecimal (_hex numbers are a concise way to represent groups of 4 bits_), and `oct` can be used for octal numbers.

There are multiple ways to convert integers to binary strings, varying in whether they include the `0b` prefix and whether they support left-padding with zeros:


```python
# Binary entry.
>>> 0b10111
23

# Converting an int display to binary string, with prefix.
>>> bin(23)  
'0b10111'

>>> number = 23

# Binary without prefix, padded to 8 digits.
>>> format(number, '08b')  
'00010111'

# Same format, but using an f-string.
>>> f"{number} in decimal is {number:08b} in binary and {number:x} in hex" 
'23 in decimal is 00010111 in binary and 17 in hex'
```


## [`Bitwise Logic`][python-bitwise-operations]

In the [concept:python/bools]() concept, we discussed the _logical operators_ `and`, `or` and `not` used with Boolean (_`True` and `False`_) values.
The same logic rules apply when working with bits.

However, the bitwise equivalents of the logical operators `&` (_and_), `|` (_or_), `~` (_not_), and  `^` (_[XOR][xor]_), are applied to each _bit_ in a binary representation, treating `1` as `True` ("on") and `0` as `False` ("off").
An example with the bitwise `&` might make this clearer:


```python
>>> x = 0b01100110
>>> y = 0b00101010

>>> format(x & y, '08b')
'00100010'
```

Only positions with a `1` in _**both**_ the input numbers are set to `1` in the output.

Bitwise `&` is commonly used as a way to isolate single bits in a compacted set of `True`/`False` values, such as user-configurable settings in an app.
This enables the value of individual bits to control program logic:


```python
>>> number = 0b0110
>>> number & 0b0001 > 0
False

>>> number & 0b0010 > 0
True
```


For a bitwise `|` (or), a `1` is set in the output if there is a `1` in _**either**_ of the inputs:


```python
>>> x = 0b01100110
>>> y = 0b00101010

>>> format(x | y, '08b')
'01101110'
```


With the `^` operator for bitwise e**x**clusive **or** (xor), a `1` is set if it appears in _**either**_ of the inputs _**but not both**_ inputs.
This symbol might seem familiar from the [concept:python/sets]() concept, where it is used for `set` _symmetric difference_, which is the same as [xor applied to sets][symmetric-difference].
If xor `^` seems strange, be aware that this is by far the [most common operation in cryptography][xor-cipher].


```python
>>> x = 0b01100110
>>> y = 0b00101010

>>> format(x ^ y, '08b')
'01001100'
```


Finally, there is the `~` operator (_the [tilde][tilde] character_), which is a bitwise `not` that takes a single input and _**inverts all the bits**_, which might not be the result you were expecting!
Each `1` in the representation changes to `0`, and vice versa.
See the section below for details.


## Negative Numbers and Binary Representation

In decimal representation, we distinguish positive and negative numbers by using a `+` or `-` sign to the left of the digits.
Using these symbols at a binary level proved inefficient for digital computing and raised the problem that `+0` is not the same as `-0`.

Rather than using `-` and `+`, all modern computers use a [`twos-complement`][twos-complement] representation for negative numbers, right down to the silicon chip level.
This means that all bits are inverted and a number is _**interpreted as negative**_ if the left-most bit (also termed the "most significant bit", or MSB) is a `1`.
Positive numbers have an MSB of `0`.
This representation has the advantage of only having one version of zero, so that the programmer doesn't have to manage `-0` and `+0`.

This way of representing negative and positive numbers adds a complication for Python: there are no finite-integer concepts like `int32` or `int64` internally in the core langauge.
In 'modern' Python, `int`s are of unlimited size (_limited only by hardware capacity_), and a negative or bit-inverted number has a (_theoretically_) infinite number of `1`'s to the left, just as a positive number has unlimited `0`'s.

This makes it difficult to give a useful example of `bitwise not`:

```python
>>> x = 0b01100110
>>> format(x, '08b')
'01100110'

# This is a negative binary (not twos-complement display).
>>> format(~x, '08b')
'-1100111'  

 # Decimal representation.
>>> x
102

# Using the Bitwise not, with an unintuitive result.
>>> ~x
-103
```

This is **not** the `0b10011001` we would see in languages with fixed-size integers.

The `~` operator only works as expected with _**unsigned**_ byte or integer types, or with fixed-sized integer types.
These numeric types are supported in third-party packages such as [`NumPy`][numpy], [`pandas`][pandas], and [`sympy`][sympy] but not in core Python.

In practice, Python programmers quite often use the shift operators described below and `& | ^` with positive numbers only.
Bitwise operations with negative numbers are much less common.
One technique is to add [`2**32 (or 1 << 32)`][unsigned-int-python] to a negative value to make an `int` unsigned, but this gets difficult to manage.
Another strategy is to work with the [`ctypes`][ctypes-module] module, and use c-style integer types, but this is equally unwieldy.


## [`Shift operators`][bitwise-shift-operators]

The left-shift operator `x << y` simply moves all the bits in `x` by `y` places to the left, filling the new gaps with zeros.
Note that this is arithmetically identical to multiplying a number by `2**y`.

The right-shift operator `x >> y` does the opposite.
This is arithmetically identical to integer division `x // 2**y`.

Keep in mind the previous section on negative numbers and their pitfalls when shifting.


```python
>>> x = 8
>>> format(x, '08b')
'00001000'

# A left bit shift. 
>>> x << 2  
32

>>> format(x << 2, '08b')
'00100000'

# A right bit shift. 
>>> format(x >> 2, '08b')
'00000010'
```

[binary-digits]: https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:digital-information/xcae6f4a7ff015e7d:binary-numbers/v/the-binary-number-system
[bits]: https://en.wikipedia.org/wiki/Bit
[bitwise-shift-operators]: https://docs.python.org/3/reference/expressions.html#shifting-operations
[ctypes-module]: https://docs.python.org/3/library/ctypes.html#module-ctypes
[high-level-language]: https://en.wikipedia.org/wiki/High-level_programming_language
[numpy]: https://numpy.org/doc/stable/user/basics.types.html
[pandas]: https://pandas.pydata.org/docs/reference/arrays.html#nullable-integer
[python-bitwise-operations]: https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations
[python-bitwise-operators]: https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations
[symmetric-difference]: https://math.stackexchange.com/questions/84184/relation-between-xor-and-symmetric-difference#:~:text=It%20is%20the%20same%20thing,they%20are%20indeed%20the%20same.
[sympy]: https://docs.sympy.org/latest/modules/codegen.html#predefined-types
[tilde]: https://en.wikipedia.org/wiki/Tilde
[twos-complement]: https://en.wikipedia.org/wiki/Two%27s_complement#:~:text=Two's%20complement%20is%20the%20most,number%20is%20positive%20or%20negative.
[unsigned-int-python]: https://stackoverflow.com/a/20768199
[xor-cipher]: https://en.wikipedia.org/wiki/XOR_cipher
[xor]: https://stackoverflow.com/a/2451393
