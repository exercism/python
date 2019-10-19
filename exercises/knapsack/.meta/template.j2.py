{%- import "generator_macros.j2" as macros with context -%}
{{ macros.header() }}

class {{ exercise | camel_case }}Test(unittest.TestCase):
    {% for case in cases -%}
    def test_{{ case["description"] | to_snake }}(self):
        maximum_weight = {{ case["input"]["maximumWeight"] }}
        items = {{ case["input"]["items"] }}
        expected = {{ case["expected"] }}
        self.assertEqual({{ case["property"] | to_snake }}(maximum_weight, items), expected)

    {% endfor %}

{{ macros.footer() }}