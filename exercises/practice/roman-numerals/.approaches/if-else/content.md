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
        res +=  m * 'M'
    
    if 4 > c > 0:
        res +=  c * 'C'
    elif c == 4:
        res +=  'CD'
    elif 9 > c > 4:
        res +=  'D' + ((c - 5) * 'C')
    elif c == 9:
        res +=  'CM'

    if 4 > x >  0:
        res += x * 'X'
    elif x == 4:
        res += 'XL'
    elif 9 > x > 4:
        res += 'L' + ((x - 5) * 'X')
    elif x == 9:
        res +=  'XC'

    if 4 > i >  0:
        res += i * 'I'
    elif i == 4:
        res += 'IV'
    elif 9 > i > 4:
        res += 'V' + ((i - 5) * 'I')
    elif i == 9:
        res += 'IX'
    
    return res
```

This gets the job done.
Something like it would work in most languages, though Python's range test (`a > x > b`) saves some boolean logic.

## Refactoring

The code above is quite long and a bit repetitive.
We should explore ways to make it more concise.

The first block is just a way to extract the digits from the input number.
This can be done with a list comprehension, left-padding with zeros as necessary:

```python
digits = ([0, 0, 0, 0] + [int(d) for d in str(number)])[-4:]
```

The blocks for hundreds, tens and units are all essentially the same, so we can put that code in a function.
We just need to pass in the digit, plus a tuple of translations for `(1, 4, 5, 9)` or their 10x and 100x equivalents.

It is also unnecessary to keep retesting the lower bounds within an `elif`, as the code line will only be reached if that is satisfied.

Using `return` instead of `elif` is a matter of personal preference.
Given that, the code simplifies to:

```python
def roman(number: int) -> str:
    def translate_digit(digit: int, translations: iter) -> str:
        assert isinstance(digit, int) and 0 <= digit <= 9

        units, four, five, nine = translations
        if digit < 4:
            return digit * units
        if digit == 4:
            return four
        if digit < 9:
            return five + (digit - 5) * units
        return nine

    assert isinstance(number, int)
    m, c, x, i = ([0, 0, 0, 0] + [int(d) for d in str(number)])[-4:]
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
```

The last few lines are quite similar and it would be possible to refactor them into a loop, but this is enough to illustrate the principle.

