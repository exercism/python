# If Else

```python
def roman(number):
    # The notation: I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
    m = number // 1000
    m_rem = number % 1000
    c = m_rem // 100
    c_rem = m_rem % 100
    x = c_rem // 10
    x_rem = c_rem % 10
    i = x_rem

    res = ''

    if m > 0:
        res += m * 'M'
    
    if c < 4:
        res += c * 'C'
    elif c == 4:
        res += 'CD'
    elif c < 9:
        res += 'D' + ((c - 5) * 'C')
    elif c == 9:
        res += 'CM'

    if x < 4:
        res += x * 'X'
    elif x == 4:
        res += 'XL'
    elif x < 9:
        res += 'L' + ((x - 5) * 'X')
    elif x == 9:
        res += 'XC'

    if i < 4:
        res += i * 'I'
    elif i == 4:
        res += 'IV'
    elif i < 9:
        res += 'V' + ((i - 5) * 'I')
    elif i == 9:
        res += 'IX'
    
    return res
```

Though this approach is rather naive, but it gets the job done.
Something similar would work in most languages, though the usage of the `*` operator for string repetition is fairly Python-specific.

Here, the first block of code uses the floor division operator (`//`) and the modulo operator (`%`) to extract each digit from the input number.
Then, the following blocks determine the Roman equivalent for each digit and append it to the resulting string.

A more concise variation of the approach is discussed below.


## Variation #1

```python
def roman(number):
    m, c, x, i = ([0, 0, 0, 0] + [int(digit) for digit in str(number)])[-4:]
    res = ''

    if m > 0:
        res += m * 'M'
    if c > 0:
        res += translate_digit(c, ('C', 'CD', 'D', 'CM'))
    if x > 0:
        res += translate_digit(x, ('X', 'XL', 'L', 'XC'))
    if i > 0:
        res += translate_digit(i, ('I', 'IV', 'V', 'IX'))

    return res


def translate_digit(digit, translations):
    units, four, five, nine = translations
    if digit < 4:
        return digit * units
    if digit == 4:
        return four
    if digit < 9:
        return five + (digit - 5) * units
    return nine
```

In this variant, a [list comprehension][list-comprehension] is used to extract the digits from the input number, left-padding with zeros as necessary.
For determining the Roman equivalent for each digit, this solution uses a helper function that takes a digit and a tuple of translations for `(1, 4, 5, 9)` (or their 10x and 100x equivalents).

The last few lines are quite similar and it would be possible to refactor them into a loop, but this is enough to illustrate the principle.


[list-comprehension]: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
