import unittest

try:
    from hello_world import (
        hello,
    )

except ImportError as import_fail:
    message = import_fail.args[0].split("(", maxsplit=1)
    item_name = import_fail.args[0].split()[3]

    item_name = item_name[:-1] + "()'"

    # pylint: disable=raise-missing-from
    raise ImportError(
        "\n\nMISSING FUNCTION --> In your 'hello_world.py' file, we can not find or import the"
        f" function named {item_name}. \nThe tests for this first exercise expect a function that"
        f' returns the string "Hello, World!"'
        f'\n\nDid you use print("Hello, World!") instead?'
    ) from None


class HelloWorldTest(unittest.TestCase):
    def test_say_hi(self):
        msg = "\n\nThis test expects a return of the string 'Hello, World!' \nDid you use print('Hello, World!') by mistake?"
        self.assertEqual(hello(), "Hello, World!", msg=msg)
