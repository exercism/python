# Concepts of `clock`

# Example implementation

From the current [example.py](https://github.com/exercism/python/blob/master/exercises/clock/example.py):

```python
class Clock:
    'Clock that displays 24 hour clock that rollsover properly'

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.cleanup()

    def __repr__(self):
        return "{:02d}:{:02d}".format(self.hour, self.minute)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __add__(self, minutes):
        self.minute += minutes
        return self.cleanup()

    def __sub__(self, minutes):
        self.minute -= minutes
        return self.cleanup()

    def cleanup(self):
        self.hour += self.minute // 60
        self.hour %= 24
        self.minute %= 60
        return self
```

## Concepts

- [PEP 8 Style][pep-8-style]: PEP 8 is the Python official style guide. Black is emerging as the defacto "pyfmt" tool: should we recommend it? (since the advent of `gofmt` and then `rustfmt`, I'm totally sold on opinionated auto-format tools: saves time and no more bikeshedding)
- [Constants][constants]: Avoid "magic numbers", defining instead meaningfully named constants. PEP 8 convention for constants: `UPPER_SNAKE_CASE`
- [Classes][classes]: use of `class` to create a custom data structure
- [Methods][methods]: use of `def` to define a class's methods
- [Operator overloading][operator-overloading]: How to overload the `+` and `-` operators using the `__add__` and `__sub__` special methods.
- [Rich comparison methods][rich-comparison-methods]: The `__eq__` method is overloaded
- [String formatting][string-formatting]: How to format strings, ie `%` operator, `str.format`, f-strings
