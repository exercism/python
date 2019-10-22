# Exercism Python Track Test Generator

The Python track uses a generator script and [Jinja2] templates for
creating test files from the canonical data.

## Table of Contents

- [Exercism Python Track Test Generator](#exercism-python-track-test-generator)
  * [Script Usage](#script-usage)
  * [Test Templates](#test-templates)
    + [Conventions](#conventions)
    + [Layout](#layout)
    + [Overriding Imports](#overriding-imports)
    + [Ignoring Properties](#ignoring-properties)
  * [Learning Jinja](#learning-jinja)
  * [Creating a templates](#creating-a-templates)

## Script Usage

Test generation requires a local copy of the [problem-specifications] repository.

Run `bin/generate_tests.py --help` for usage information.

## Test Templates

Test templates support [Jinja2] syntax, and have the following context
variables available from the canonical data:
- `exercise`: The hyphenated name of the exercise (ex: `two-fer`)
- `version`: The canonical data version (ex. `1.2.0`)
- `cases`: A list of case objects or a list of `cases` lists. For exact
structure for the exercise you're working on, please consult
`canonical-data.json`
- `has_error_case`: Indicates if any test case expects an
error to be thrown (ex: `False`)
- `additional_cases`: similar structure to `cases`, but is populated from the exercise's `.meta/additional_tests.json` file if one exists (for an example, see `exercises/word-count/.meta/additional_tests.json`)

Additionally, the following template filters are added for convenience:
- `to_snake`: Converts a string to snake_case (ex: `{{ "CamelCaseString" | to_snake }}` -> `camel_case_string`)
- `camel_case`: Converts a string to CamelCase (ex: `{{ "snake_case_string" | camel_case }}` -> `SnakeCaseString` )
- `error_case`: Checks if a test case expects an error to be thrown (ex: `{% for case in cases%}{% if case is error_case}`)
- `regex_replace`: Regex string replacement (ex: `{{ "abc123" | regex_replace("\\d", "D") }}` -> `abcDDD`)

### Conventions

- General-use macros for highly repeated template structures are defined in `config/generator_macros.j2`.
  - These may be imported with the following:
  `{%- import "generator_macros.j2" as macros with context -%}`
- All test templates should end with `{{ macros.footer() }}`.
- All Python class names should be in CamelCase (ex: `TwoFer`).
  - Convert using `{{ "two-fer" | camel_case }}`
- All Python module and function names should be in snake_case
(ex: `high_scores`, `personal_best`).
  - Convert using `{{ "personalBest" | to_snake }}`
- Track-specific tests are defined in the option file `.meta/additional_tests.json`. The JSON object defined in this file is to
have a single key, `cases`, which has the same structure as `cases` in
`canonical-data.json`.
- Track-specific tests should be placed after canonical tests in test
files.
- Track-specific tests should be marked in the test file with the following comment:
```
# Additional tests for this track
```

### Layout

Most templates will look something like this:

```Jinja2
{%- import "generator_macros.j2" as macros with context -%}
{{ macros.header() }}

class {{ exercise | camel_case }}Test(unittest.TestCase):
    {% for case in cases -%}
    def test_{{ case["description"] | to_snake }}(self):
        value = {{ case["input"]["value"] }}
        expected = {{ case["expected"] }}
        self.assertEqual({{ case["property"] }}(value), expected)

    {% endfor %}

{{ macros.footer() }}
```

### Overriding Imports

The names imported in `macros.header()` may be overridden by adding
a list of alternate names to import (ex:`clock`):

```Jinja2
{{ macros.header(["Clock"])}}
```

### Ignoring Properties

On rare occasion, it may be necessary to filter out properties that
are not tested in this track. The `header` macro also accepts an
`ignore` argument (ex: `high-scores`):

```Jinja2
{{ macros.header(ignore=["scores"]) }}
```

## Learning Jinja

Starting with the [Jinja Documentation] is highly recommended, but a complete reading is not strictly necessary.

Additional Resources:
- [Primer on Jinja Templating]
- [Python Jinja tutorial]


## Creating a templates

1. Create `.meta/template.j2` for the exercise you are implementing,
  and open it in your editor.
2. Copy and paste the [example layout](#Layout) in the template file
  and save.
3. Make the appropriate changes to the template file until it produces
  valid test code, referencing the exercise's `canonical-data.json` for
  input names and case structure.
    - Use the [available macros](../config/generator_macros.j2) to avoid re-writing standardized sections.
    - If you are implementing a template for an existing exercise,
    matching the exact structure of the existing test file is not a
    requirement, but minimizing differences will make PR review a much smoother process for everyone involved.



[Jinja2]: https://jinja.pocoo.org/
[Jinja Documentation]: https://jinja.palletsprojects.com/en/2.10.x/
[Primer on Jinja Templating]: https://realpython.com/primer-on-jinja-templating/
[Python Jinja tutorial]: http://zetcode.com/python/jinja/
[problem-specifications]: https://github.com/exercism/problem-specifications
