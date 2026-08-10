# Instructions

Given a name and a number, your task is to produce a sentence using that name and that number as an [ordinal numeral][ordinal-numeral].
Yaʻqūb expects to use numbers from 1 up to 999.

Rules:

- Numbers ending in 1 (unless ending in 11) → `"st"`
- Numbers ending in 2 (unless ending in 12) → `"nd"`
- Numbers ending in 3 (unless ending in 13) → `"rd"`
- All other numbers → `"th"`

Examples:

- `"Mary", 1` → `"Mary, you are the 1st customer we serve today. Thank you!"`
- `"John", 12` → `"John, you are the 12th customer we serve today. Thank you!"`
- `"Dahir", 162` → `"Dahir, you are the 162nd customer we serve today. Thank you!"`

[ordinal-numeral]: https://en.wikipedia.org/wiki/Ordinal_numeral
