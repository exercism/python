# Concepts for `markdown`

## Example implementation

A less than ideal approach from the current [example.py](https://github.com/exercism/python/blob/master/exercises/markdown/example.py):

```python
import re

def parse(markdown):
    lines = markdown.split('\n')
    html = ''
    in_list = False
    in_list_append = False
    for line in lines:
        result = parse_line(line, in_list, in_list_append)
        html += result['line']
        in_list = result['in_list']
        in_list_append = result['in_list_append']
    if in_list:
        html += '</ul>'
    return html

def wrap(line, tag):
    return '<{tag}>{line}</{tag}>'.format(line=line, tag=tag)

def check_headers(line):
    pattern = '# (.*)'
    for index in range(6):
        if re.match(pattern, line):
            return wrap(line[(index + 2):], 'h' + str(index + 1))
        pattern = '#' + pattern
    return line

def check_bold(line):
    bold_pattern = '(.*)__(.*)__(.*)'
    bold_match = re.match(bold_pattern, line)
    if bold_match:
        return bold_match.group(1) + wrap(bold_match.group(2), 'strong')\
            + bold_match.group(3)
    else:
        return None

def check_italic(line):
    italic_pattern = '(.*)_(.*)_(.*)'
    italic_match = re.match(italic_pattern, line)
    if italic_match:
        return italic_match.group(1) + wrap(italic_match.group(2), 'em')\
            + italic_match.group(3)
    else:
        return None

def parse_line(line, in_list, in_list_append):
    result = check_headers(line)

    list_match = re.match(r'\* (.*)', result)

    if (list_match):
        if not in_list:
            result = '<ul>' + wrap(list_match.group(1), 'li')
            in_list = True
        else:
            result = wrap(list_match.group(1), 'li')
    else:
        if in_list:
            in_list_append = True
            in_list = False

    if not re.match('<h|<ul|<li', result):
        result = wrap(result, 'p')

    if list_match is None:
        result = re.sub('(.*)(<li>)(.*)(</li>)(.*)',
                        r'\1\2<p>\3</p>\4\5', result)

    while check_bold(result):
        result = check_bold(result)
    while check_italic(result):
        result = check_italic(result)

    if in_list_append:
        result = '</ul>' + result
        in_list_append = False

    return {
        'line': result,
        'in_list': in_list,
        'in_list_append': in_list_append
    }
```

An alternate example using [regular expressions](https://exercism.io/tracks/python/exercises/markdown/solutions/daf30e5227414a61a00bac391ee2bd79):

```python
import re


def parse(markdown):
    s = markdown
    s = re.sub(r'__([^\n]+?)__', r'<strong>\1</strong>', s)
    s = re.sub(r'_([^\n]+?)_', r'<em>\1</em>', s)
    s = re.sub(r'^\* (.*?$)', r'<li>\1</li>', s, flags=re.M)
    s = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', s, flags=re.S)
    for i in range(6, 0, -1):
        s = re.sub(r'^{} (.*?$)'.format('#' * i), r'<h{0}>\1</h{0}>'.format(i), s, flags=re.M)
    s = re.sub(r'^(?!<[hlu])(.*?$)', r'<p>\1</p>', s, flags=re.M)
    s = re.sub(r'\n', '', s)
    return s
```

Another alternate example using [Python with Regex](https://exercism.io/tracks/python/exercises/markdown/solutions/a1f1d7b60bfc42818b2c2225fe0f8d7a)

```python
import re

BOLD_RE = re.compile(r"__(.*?)__")
ITALICS_RE = re.compile(r"_(.*?)_")
HEADER_RE = re.compile(r"(#+) (.*)")
LIST_RE = re.compile(r"\* (.*)")


def parse(markdown: str) -> str:
    """
    Parse a simple markdown-formatted string to HTML.
    """
    result = []
    for line in markdown.splitlines():
        # expand inline bold tags
        line = BOLD_RE.sub(r"<strong>\1</strong>", line)
        # expand inline italics tags
        line = ITALICS_RE.sub(r"<em>\1</em>", line)

        # line may be a header item or a list item
        is_header = HEADER_RE.match(line)
        is_list = LIST_RE.match(line)

        # a header is not itself a paragraph
        if is_header:
            result.append("<h{0}>{1}</h{0}>".format(len(is_header.group(1)),
                                                    is_header.group(2)))
        # neither is any part of a list
        elif is_list:
            # we may be appending to an existing list
            if result and result[-1] == "</ul>":
                result.pop()
            # or starting a new one
            else:
                result.append("<ul>")
            result.extend(["<li>" + is_list.group(1) + "</li>", "</ul>"])
        # everything else is a paragraph
        else:
            result.append("<p>" + line + "</p>")
    return "".join(result)
```

## Concepts

- [Refactor][refactor]: Reviewing and rewriting (or re-organizing) code for clarity and efficiency. This exercise requires a re-write of pre-existing code that uses functions to parse passed-in text in markdown.
- [Functions][functions]: Tests for this exercise expect a function named `parse` that can be called to transform the _markdown_ formatted text and return HTML formatted text.
- [Function arguments][function-arguments]: The example solutions use functions that take function arguments to operate on passed in markdown strings.
- [Regular Expressions][regular-expressions]: Both the original code to be refactored for this exercise and the example solution import and use the `re` module for Regular Expressions in python.
- [Importing][importing]: Both the original code to be refactored for the exercise and the example solution use the `import` keyword to import the `re` module in support of Regular Expressions in python.
- [String Splitting][string-splitting]: The example solution uses `str.split()` to break the passed in markdown string into a list of lines broken up by the `\n` character. The alternate Python example solution uses `str.splitlines()` for the same effect across all line end characters.
- [Regular Expressions][regular-expressions]: the `re.match()` function from the `re` module returns a `match` object with any matched values from a specified Regular Expression or pre-compliled Regular Expression. The example uses `re.match()` in multiple places to search for text patterns that need re-formatting or subsitituting.
- [Regular expressions][regular-expressions]: A Domain Specific Language (DSL) for text processing. Like many other programming languages in use, python supports a quasi-dialect of PCRE (_Perl compatible regular expressions_). `Regular expressions` can be used via the core python `re` module, or the third-party `regex` module. Both the original code to be refactored for this exercise and the example solutions use the core `re` module to access `regular expressions` functionality.
- [Return value][return-value]: Most of the functions in the example solution specify a _return_ value using the `return` keyword.
- [None][none]: Pythons null type, referred to when a null or "placeholder" is needed. It is in and of itself a singleton in any given python program.
- [Booleans][booleans]: True and False of type `bopl`. The example solution uses `True` and `False` as return values from functions that test membership in a list of values.
- [Assignment][assignment]: The example solution uses assignment for variables and other values.
- [Regular Expressions][regular-expression]: the `re.sub()` function of the `re` module that replaces a `regular expression` match with a new value. The example solutions use this function in various places to substitute _markdown_ syntax for _HTML_ syntax in the passed in markdown text.
- [Dictionaries][dictionaries]: Mapping type. The example solution employes a dictionary to return values from the `parse_line()` function.
- [For loops][for-loops]: The example solution uses `for` loops to iterate over various function inputs.
- [Iteration][iterable]: The example solution uses the `for _ in _` syntax to iterate over a list of lines. This is possible because a list is an `iterable`.
- [Conditionals][conditionals]: The example solution uses `if` to check for pattern matching and membership conditions in different functions for processing different markdown patterns.
- [Regular Expressions][regular-expressions]: Various functions in the re module return a `re.Match` _instance_ which in turn has a `Match.group` method. `Match.group` exists even if there are no groups specified in the pattern. See the [Match.group docs](https://docs.python.org/3/library/re.html#re.Match.group) for more detail.
- [Lists][lists]: The example uses lists in several places to hold text to be processed or searched - or for tracking the state of pieces of the passed-in text.
- [Range][range]: the `range()` built-in represents an immutable sequence of numbers (or any object that implements the **index** magic method). Used in the example to control the number of loops while iterating through a passed-in line or list.
