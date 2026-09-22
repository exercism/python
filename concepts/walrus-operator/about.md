# About

Added in Python 3.8, assignment expressions use the `:=` operator, popularly called the ["walrus operator"][whats-new].

The central idea is that a variable can be assigned within the context of another statement.
A simple example is when something tested in a condition is needed again within the body of an `if` statement:

```python
# without walrus operator
a = 'short'
if len(a) < 10:
    print(f"{len(a)} characters is too short")

#  => "5 characters is too short"

# with walrus operator 
# Note the parentheses around the assignment (necessary)
if (n := len(a)) < 10:
    print(f"{n} characters is too short")

#  => "5 characters is too short"
```

Thus, setting the `n` variable saves calculating `len(a)` twice.
The saving is fairly trivial in this case, but becomes significant for a more expensive operation such as file I/O:

```python
# Loop over fixed length blocks
while (block := f.read(256)) != '':
    process(block)
```

## Use cases

The walrus operator was [controversial][controversy] in the Python community when [first introduced][pep-572] in 2018.
It is now an established part of the core language, simplifying code in some particular situations, but should not be over-used.
As so often in programming, we should consider if use of a feature increases or decreases the readability of the code.

Some applications of the walrus operator are listed below.

### Comprehensions

List comprehensions, dictionary comprehensions, generator expressions, _etc_, all allow Python to do a lot in a terse piece of code.

Including a walrus operator can _sometimes_ make such code shorter and clearer, especially if a value calculated in the `if` clause is also needed in other parts of the comprehension.

```python
[clean_name.title() for name in names
 if (clean_name := name.strip().lower()) in allowed_names]
```

Note that the calculated value `clean_name` is only in scope within the comprehension.
It cannot be used in other parts of the program.

### RegEx matching

Use of the walrus operator can simplify nested `if...else` statements.
Handling regular expression matches is [an example][walrus-blog] of this:

```python
import re

test = "Something we want to search"
pattern1 = r"^.*(thing).*"
pattern2 = r"^.*(missing).*"

# without walrus
m = re.match(pattern1, test)
if m:
    print(f"Matched the 1st pattern: {m.group(1)}")
else:
    m = re.match(pattern2, test)
    if m:
        print(f"Matched the 2nd pattern: {m.group(1)}")
# => "Matched 1st pattern: 'thing'"       

# Cleaner with walrus
if m := (re.match(pattern1, test)):
    print(f"Matched 1st pattern: '{m.group(1)}'")
elif m := (re.match(pattern2, test)):
    print(f"Matched 2nd pattern: '{m.group(1)}'")
# => "Matched 1st pattern: 'thing'"       
```

### Inside f-strings

This is not a particularly common use of walrus operators, but it can sometimes simplify code.
As usual, the assignment must be within parentheses.

```python
from datetime import datetime

print(f"Today is: {(today:=datetime.today()):%Y-%m-%d}, which is {today:%A}")

#  => "Today is: 2024-01-06, which is Saturday"
```

[whats-new]: https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions
[walrus-blog]: https://martinheinz.dev/blog/79
[pep-572]: https://peps.python.org/pep-0572/
[controversy]: https://dev.to/renegadecoder94/the-controversy-behind-the-walrus-operator-in-python-4k4e
