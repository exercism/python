# Instructions

Optical Character Recognition or OCR is software that converts images of text into machine-readable text.
Given a grid of characters representing some digits, convert the grid to a string of digits.
If the grid has multiple rows of cells, the rows should be separated in the output with a `","`.

- The grid is made of one of more lines of cells.
- Each line of the grid is made of one or more cells.
- Each cell is three columns wide and four rows high (3x4) and represents one digit.
- Digits are drawn using pipes (`"|"`), underscores (`"_"`), and spaces (`" "`).

## Edge cases

- If the input is not a valid size, your program should indicate there is an error.
- If the input is the correct size, but a cell is not recognizable, your program should output a `"?"` for that character.

## Examples

The following input (without the comments) is converted to `"1234567890"`.

```text
      _  _     _  _  _  _  _  _  #
    | _| _||_||_ |_   ||_||_|| | # Decimal numbers.
    ||_  _|  | _||_|  ||_| _||_| #
                                 # The fourth line is always blank,
```

The following input is converted to `"123,456,789"`.

<!-- prettier-ignore-start -->

```text
    _  _ 
  | _| _|
  ||_  _|
         
    _  _ 
|_||_ |_ 
  | _||_|
         
 _  _  _ 
  ||_||_|
  ||_| _|
         
```

<!-- prettier-ignore-end -->
