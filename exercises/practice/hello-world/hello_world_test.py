# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/hello-world/canonical-data.json
# File last updated on 2023-07-19

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

if __name__ == '__main__':
    # Why is this if implanted?
    # This prevents the contents within the if statement of this script from being run indirectly, when it is imported as a module in another script/module, or from recurring loops.
    # So it runs only when you execute the test, i.e. this module/script.
    # What does the naming mean?
    # The name is __main__ because this is the default module that is run when the script is executed directly.
    # If the script is run from another script, its name would be the name of the module it is imported as, i.e. hello_world_test.
    unittest.main()
