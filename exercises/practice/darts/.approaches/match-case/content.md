# Use `match/case` (Structural Pattern Matching)


```python
from math import hypot, ceil


def score(x, y):
    toss = ceil(hypot(x, y))
    
    match toss:
        case 0 | 1: return 10
        case 2 | 3 | 4 | 5: return 5
        case 6 | 7 | 8 | 9 | 10: return 1
        case _: return 0

#OR#

def score(x, y):
    match ceil(hypot(x, y)):
        case 0 | 1: return 10
        case 2 | 3 | 4 | 5: return 5
        case 6 | 7 | 8 | 9 | 10: return 1
        case _: return 0
```

This approach uses `Python 3.10`'s [`structural pattern matching`][structural-pattern-matching] with `return` values on the same line as `case`.
Because the match is numeric, each case explicitly lists allowed values using the `|` (OR) operator.
A fallthrough case (`_`) is used if the dart throw is greater than 10  (_the outer circle radius of the target_).
This is equivalent to using `if-statements` to check toss values although some might argue it is clearer to read.
An `if-statement` equivalent would be:

```python
from math import hypot, ceil


def score(x, y):
    toss =  ceil(hypot(x, y))
    
    if toss in (0, 1): return 10
    if toss in (2, 3, 4, 5): return 5
    if toss in (6, 7, 8, 9, 10): return 1
    
    return 0
```

One can also use `<`, `>`, or `<=` and `>=` in structural pattern matching, although the syntax becomes almost identical to using them with `if-statements`, but more verbose:


```python
from math import hypot, ceil


def score(x, y):
    toss = ceil(hypot(x, y))
    
    match toss:
        case toss if toss <= 1: return 10
        case toss if toss <= 5: return 5
        case toss if toss <= 10: return 1
        case _: return 0
```


Finally, one can use an [assignment expression][assignment-expression] or [walrus operator][walrus] to calculate the toss value rather than calculating and assigning a variable on a separate line.
This isn't necessary (_the first variations shows this clearly_) and might be harder to reason about/understand for some programmers:


```python
from math import hypot, ceil

def score(x, y):
    match toss := ceil(hypot(x, y)):
        case toss if toss <= 1: return 10
        case toss if toss <=5: return 5
        case toss if toss <=10: return 1
        case _: return 0
```

Using structural pattern matching for this exercise doesn't offer any clear performance advantages over the `if-statement`, but might be "cleaner", more "organized looking", or easier for others to scan/read.


[assignment-expression]: https://docs.python.org/3/reference/expressions.html#grammar-token-python-grammar-assignment_expression
[structural-pattern-matching]: https://peps.python.org/pep-0636/
[walrus]: https://peps.python.org/pep-0572/
