# Instructions

In this exercise, you are going to create a helpful program so that you don't have to remember the values of the bands.
The program will take 1, 4, or 5 colors as input and output the correct value in ohms.
The color bands are encoded as follows:

- black: 0
- brown: 1
- red: 2
- orange: 3
- yellow: 4
- green: 5
- blue: 6
- violet: 7
- grey: 8
- white: 9

In [`Resistor Color Trio`][resistor-color-trio-exercise] you decoded the first three color bands.
For instance: orange-orange-brown translated to the main value `330`.
In this exercise you will need to add _tolerance_ to the mix.
Tolerance is the maximum amount that a value can be above or below the main value.
For example, if the last band is green, the maximum tolerance will be `±0.5%`.

The tolerance band will have one of these values:

- grey - 0.05%
- violet - 0.1%
- blue - 0.25%
- green - 0.5%
- brown - 1%
- red - 2%
- gold - 5%
- silver - 10%

The four-band resistor is built up like this:

| Band_1  | Band_2  | Band_3     | band_4    |
| ------- | ------- | ---------- | --------- |
| Value_1 | Value_2 | Multiplier | Tolerance |

Examples:

- orange-orange-brown-green would be `330` ohms with a `±0.5%` tolerance.
- orange-orange-red-grey would be `3300` ohms with `±0.05%` tolerance.

The difference between a four and five-band resistor is that the five-band resistor has an extra band to indicate a more precise value.

| Band_1  | Band_2  | Band_3  | Band_4     | band_5    |
| ------- | ------- | ------- | ---------- | --------- |
| Value_1 | Value_2 | Value_3 | Multiplier | Tolerance |

Examples:

- orange-orange-orange-black-green would be `333` ohms with a `±0.5%` tolerance.
- orange-red-orange-blue-violet would be `323M` ohms with a `±0.10` tolerance.

There are also one band resistors.
One band resistors only have the color black with a value of 0.


Your program should translate an input `list` of resistor band colors into a label:

"... ohms ...%"

So an input `list` of `["orange", "orange", "black", "green"]` should return:

"33 ohms ±0.5%"

When there are more than a thousand ohms, we say "kiloohms".
 That's similar to saying "kilometer" for 1000 meters, and "kilograms" for 1000 grams.

So an input `list` of `["orange", "orange", "orange", "grey"]` should return:

"33 kiloohms ±0.05%"

When there are more than a million ohms, we say "megaohms".

So an input `list` of `["orange", "orange", "blue", "red"]` should return:

"33 megaohms ±2%"

[resistor-color-trio-exercise]: https://exercism.org/tracks/python/exercises/resistor-color-trio
