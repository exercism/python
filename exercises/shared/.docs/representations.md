# Representations

The [Python representer][representer] processes and normalizes student solutions into a more "generic" form:

- Code is converted to an AST using the [Python AST module][python-ast].
- Final AST tree is converted to a string without whitespace or indentation, and output as `representation.txt`.
- For troubleshooting purposes, `representation.out` includes starting AST, edited AST, and a code representation with normalizations applied.

- Removals:
    - typehints
    - `print()` statements
    - `if __name__ == __main__` blocks
    -  comments
    -  docstrings

-  Replacements:
    - user-defined names are replaced with placeholders (_including function names, parameters, and variables in lambdas_)

- Normalizations:
  - stringquotes `'` are changed to `"` (_doublequotes_), unless escapes are needed, then they remain unchanged.
  - number literals have any underscores removed and scientific notation is calculated by place:
    - **66_777_888_433** --> 66777888433
    - **1_999_878_473.66** --> 1999878473.66
    - **77_555_998_125.445_779** --> 77555998125.44579
    - **44_573_123.445_312+123_674.889_12j** --> 44573123.445312 + 123674.88912j
    - **1e6** --> 1000000.0 #1000000
    -  **1e2+.23** --> 100.0 + 0.23 #100.23
    - **1e2+1_23e0+4.4e-1** --> 100.0 + 123.0 + 0.44 #223.44
    - **7e6+7e5+5e4+9.98e2+4.45_779e-1** -->7000000.0 + 700000.0 + 50000.0 + 998.0 + 0.445779 #7750998.445779
    - **(7e6+7e5+5e4+9.98e1+4.457_79e-1)+(1e2+1.23e1+4.444_23e-1)*1*j** --> (7000000.0 + 700000.0 + 50000.0 + 99.8 + 0.445779 + (100.0 + 12.3 + 0.444423) * 1j)  #7750100.245779+112.744423j

[representer]: https://github.com/exercism/python-representer/tree/main/representer
[python-ast]: https://docs.python.org/3/library/ast.html#module-ast

