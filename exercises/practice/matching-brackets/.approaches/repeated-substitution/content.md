# Repeated Substitution


```python
def is_paired(text):
    text = "".join([element for element in text if element in "()[]{}"])
    while "()" in text or "[]" in text or "{}" in text:
        text = text.replace("()","").replace("[]", "").replace("{}","")
    return not text
```

In this approach, the steps are:

1.  Remove all non-bracket characters from the input string (_as done through the filter clause in the list-comprehension above_).
2.  Iteratively remove all remaining bracket pairs: this reduces nesting in the string from the inside outwards.
3.  Test for a now empty string, meaning all brackets have been paired.


The code above spells out the approach particularly clearly, but there are (of course) several possible variants.


## Variation 1:  Walrus Operator within a Generator Expression


```python
def is_paired(input_string):
    symbols = "".join(char for char in input_string if char in "{}[]()")
    while (pair := next((pair for pair in ("{}", "[]", "()") if pair in symbols), False)):
        symbols = symbols.replace(pair, "")
    return not symbols
```

The second solution above does essentially the same thing as the initial approach, but uses a generator expression assigned with a [walrus operator][walrus] `:=` (_introduced in Python 3.8_) in the `while-loop` test.


## Variation 2:  Regex Substitution in a While Loop

Regex enthusiasts can modify the previous approach, using `re.sub()` instead of `string.replace()` in the `while-loop` test:

```python
import re

def is_paired(text: str) -> bool:
    text = re.sub(r'[^{}\[\]()]', '', text)
    while text != (text := re.sub(r'{\}|\[]|\(\)', '', text)):
        continue
    return not bool(text)
```


## Variation 3: Regex Substitution and Recursion


It is possible to combine `re.sub()` and recursion in the same solution, though not everyone would view this as idiomatic Python:


```python
import re

def is_paired(input_string):
    replaced = re.sub(r"[^\[\(\{\}\)\]]|\{\}|\(\)|\[\]", "", input_string)
    return not input_string if input_string == replaced else is_paired(replaced)
```

Note that solutions using regular expressions ran slightly *slower* than `string.replace()` solutions in benchmarking, so adding this type of complexity brings no benefit to this problem.

[walrus]: https://martinheinz.dev/blog/79/
