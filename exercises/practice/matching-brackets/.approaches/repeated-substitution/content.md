# Repeated Substitution

```python
def is_paired(text):
    text = "".join([x for x in text if x in "()[]{}"])
    while "()" in text or "[]" in text or "{}" in text:
        text = text.replace("()","").replace("[]", "").replace("{}","")
    return not text
```

In this approach, the steps are:

- Remove all non-brackets characters.
- Iteratively remove all bracket pairs: this reduces nesting in the string from the inside outwards.
- Test for an empty string, meaning all brackets are paired.

The code above spells out the approach particularly clearly, but there are (of course) several possible variants.

```python
def is_paired(input_string):
    symbols = "".join(char for char in input_string if char in "{}[]()")
    while (pair := next((pair for pair in ("{}", "[]", "()") if pair in symbols), False)):
        symbols = symbols.replace(pair, "")
    return not symbols
```

The second solution above does essentially the same thing, but using a generator expression assigned with a [walrus operator][walrus] `:=` (introduced in Python 3.8).

Regex enthusiasts can modify the approach further, using `re.sub()` instead of `string.replace()`:

```python
import re

def is_paired(str_: str) -> bool:
    str_ = re.sub(r'[^{}\[\]()]', '', str_)
    while str_ != (str_ := re.sub(r'{\}|\[]|\(\)', '', str_)):
        pass
    return not bool(str_)
```

It is even possible to combine regexes and recursion in the same solution, though not everyone would view this as idiomatic Python:

```python
import re

def is_paired(input_string):
    replaced = re.sub(r"[^\[\(\{\}\)\]]|\{\}|\(\)|\[\]", "", input_string)
    return not input_string if input_string == replaced else is_paired(replaced)
```

Note that both solutions using regular expressions ran slightly *slower* than `string.replace()` solutions in benchmarking, so adding this type of complexity brings no benefit in this problem.

[walrus]: ***Can we merge the `walrus-operator` concept?***