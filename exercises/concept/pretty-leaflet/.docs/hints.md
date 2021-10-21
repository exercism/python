# Hints

## General

Use only f-strings or the `format()` method to build a leaflet containing basic information about an event.

- [Introduction to string formatting in Python][str-f-strings-docs]
- [Article on realpython.com][realpython-article]

## 1. Capitalize the header

- Capitalize the title using the str method `capitalize`.

## 2. Format the date

- The `date` should be formatted manually using `f''` or `''.format()`.
- The `date` should use this format: 'Month day, year'.

## 3. Render the unicode characters as icons

- One way of rendering with `format` would be to use the unicode prefix `u'{}'`.

## 4. Display the finished leaflet

- Find the right [format_spec field][formatspec-docs] to align the asterisks and characters.
- Section 1 is the `header` as a capitalized string.
- Section 2 is the `date`.
- Section 3 is the list of artists, each artist is associated with the unicode character having the same index.
- Each line should contain 20 characters.
- Write concise code to add the necessary empty lines between each section.
- If the date is not given, replace it with a blank line.

```python
******************** # 20 asterisks
*                  *
*     'Header'     * # capitalized header
*                  *
* Month day, year  * # Optional date
*                  *
* Artist1       ⑴ * # Artist list from 1 to 4
* Artist2       ⑵ *
* Artist3       ⑶ *
* Artist4       ⑷ *
*                  *
********************
```

[str-f-strings-docs]: https://docs.python.org/3/reference/lexical_analysis.html#f-strings
[realpython-article]: https://realpython.com/python-formatted-output/
[formatspec-docs]: https://docs.python.org/3/library/string.html#formatspec
