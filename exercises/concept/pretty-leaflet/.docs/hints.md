## General

Use only f-strings or the `format()` method to build a leaflet containing basic information about an event.

- [Introduction to string formatting in Python][str-f-strings-docs]
- [Article on realpython.com][realpython-article]

## 1. Capitalize the header

- Make sure your class is named `Leaflet`.
- Make sure the constructor `__init__` accepts three parameters: the header, the artists, the unicode characters.
- Capitalize the title using the str method `capitalize`.
- Store the header in an instance variable in the constructor.

## 2. Add an optional date

- The instance variable `date` should be formatted manually using `f''` or `''.format()`.
- The `date` should use this format: 'Month day, year'.
- The year argument can be `None`, in that case, only the month name and the day should be displayed.
- If `set_date` is not called before the leaflet is printed, no date should be displayed.
- Verify your instance variable `date` is initialized with an empty string in the constructor.

## 3. Render the unicode characters as icons

- One way of rendering with `format` would be to use the unicode prefix `u'{}'`.

## 4. Display the finished leaflet

- Find the right [format_spec field][formatspec-docs] to align the asterisks and characters.
- Section 1 is the `header` as a capitalized string.
- Section 2 is the `date` instance variable.
- Section 3 is the list of artists, each artist is associated with the unicode character having the same index.
- Each line should contain 20 characters.
- Write concise code to add the necessary empty lines between each section.

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
